"""

Guidelines:

  1) ALL WM keyboard commands use the Win mod.
  2) Alt can be used in conjunction with Win to
    - Avoid accidentally issuing especially disruptive commands, or
    - Issue a command related to the non-modified one.

"""

from os import system, uname
import subprocess

from libqtile.config import Key, Screen, Group, Click
from libqtile.command import lazy
from libqtile.manager import Drag
from libqtile import layout, bar, widget, hook


#
# exposed globals
#
screens = []
layouts = []
groups = []

keys = []
mouse = []

hostname = uname()[1]


#
# sound card
#
def guessAlsaSoundCard():
  try:
    return int(subprocess.check_output(['aplay -l |grep card |grep -vi hdmi'], shell=True).split('\n')[:-1][0][5])
  except Exception as e:
    print e
    return 0

sound_card = guessAlsaSoundCard()

unmute_command='; '.join('amixer -c %d set %s unmute' % (sound_card, control) for control in ['Master', 'Headphone', 'Speaker'])


#
# Floats
#
floating_layout = layout.Floating(auto_float_types=[
  "notification",
  "toolbar",
  "splash",
  "dialog",
])


#
# Hooks
#
@hook.subscribe.screen_change
def restart_on_screen_change(qtile, ev):
  qtile.cmd_restart()


#
# Initialization commands.
# (These run before the qtile instance is available.)
#
screen_setup = {
  'pinky': 'xrandr --output LVDS1 --preferred --primary --output VGA1 --preferred --right-of LVDS1',
  'salad': 'xrandr --output DVI-0 --preferred --primary --output DisplayPort-0 --preferred --right-of DVI-0',
  'trash': 'xrandr --output LVDS --mode 1280x720 --primary --output DFP1 --mode 640x480 --right-of LVDS',
  'dot':   'xrandr --output LVDS1 --primary --output HDMI1 --right-of LVDS1',
}.get(hostname)

if screen_setup:
  system(screen_setup)

system('fbsetbg -a ~/.usr/gui/bg.jpg')
system('killall syndaemon; syndaemon -dt')
system('xsetroot -cursor_name left_ptr')
system('killall udiskie; udiskie &')
system('killall nm-applet; nm-applet &')
system('killall indicator-cpufreq; indicator-cpufreq &')

#
# QTile initialization.
# (main() is run when the qtile instance becomes available.
# http://docs.qtile.org/en/latest/configuration.html#main
#
def main(qtile):

  system('xmodmap .dati/sys/xmodmap')

  # TODO: extend for a generic number of screens?
  dualscreen = not qtile or len(qtile.conn.pseudoscreens) > 1

  # key modifiers
  normal = ['mod4']
  strong = ['mod4', 'mod1']


  #
  # commands
  #
  term = '_terminal '
  normal_commands = {
    'b': 'chromium-browser',
    'v': 'gvim',
    't': '_tango_newsletter',
    'c': term + '-e coffee',
    'a': term + '-e alsamixer -c %d' % sound_card,
    'F10': 'sh -c "import screenshot$(yymmdd_HHMMSS).png"',
    'F12': 'mount_and_open_all',
    'Return': term,

    'equal': 'amixer -c %d -q set Master 2dB+' % sound_card,
    'minus': 'amixer -c %d -q set Master 2dB-' % sound_card,
    'bracketleft': 'brightness down',
    'bracketright': 'brightness up',
  }

  strong_commands = {
    's': 'setxkbmap -layout se',
    'g': 'setxkbmap -layout gr',
    '1': 'setxkbmap -layout it',
    '0': 'setxkbmap -layout us',
  }

  keys.extend([
    Key([],     'XF86MonBrightnessUp',   lazy.spawn('brightness up')),
    Key([],     'XF86MonBrightnessDown', lazy.spawn('brightness down')),
    Key(strong, 'q',              lazy.shutdown()),
    Key(normal, 'j',              lazy.layout.switchdown(0)),
    Key(strong, 'j',              lazy.layout.client_to_stack(0)),
    Key(normal, 'k',              lazy.layout.switchdown(1)),
    Key(strong, 'k',              lazy.layout.client_to_stack(1)),
    Key(normal, 'h',              lazy.screen.prev_group()),
    Key(normal, 'l',              lazy.screen.next_group()),
    Key(normal, 'space',          lazy.screen.togglegroup()),
    Key(normal, 'semicolon',      lazy.spawncmd()),
    Key(normal, 't',              lazy.layout.toggle_split()),
    Key(normal, 'r',              lazy.layout.rotate()),
    Key(normal, 'apostrophe',     lazy.next_layout()),
    Key(normal, 'x',              lazy.window.kill()),
    Key(normal, 'f',              lazy.window.toggle_floating()),
  ])

  keys.extend([Key(normal, k, lazy.spawn(v)) for k, v in normal_commands.items()])
  keys.extend([Key(strong, k, lazy.spawn(v)) for k, v in strong_commands.items()])


  #
  # Screens and bars
  #
  class CustomWindowName(widget.WindowName):
    def button_press(self, x, y, button):
      screen = self.bar.screen
      {
        1: lambda: screen.group.layout.cmd_switchdown(0), # left mouse, left pane
        2: lambda: self.qtile.cmd_next_layout(), # mid mouse, change layout
        3: lambda: screen.group.layout.cmd_switchdown(1), # right mouse, right pane
        4: lambda: screen.cmd_next_group(), # wheel up
        5: lambda: screen.cmd_prev_group(), # wheel down
      }.get(button, lambda: '')()


  main_bar = bar.Bar([
    widget.GroupBox(
      urgent_alert_method='text',
      borderwidth=2,
      padding=1,
      margin_x=1,
      margin_y=1,
      active='00FF00',
      this_current_screen_border='009900',
      disable_drag=True,
      inactive='CCCCCC'),
    widget.Volume(cardid=sound_card, device=None),
    widget.Sep(),
    CustomWindowName(),
    widget.Sep(),
    widget.Notify(default_timeout=1),
    widget.Prompt(),
    widget.Battery(),
    widget.Systray(icon_size=25),
    widget.Clock(format='%m%d %a %I:%M%P'),
  ], 25)


  lower_bar = bar.Bar([
    CustomWindowName(),
  ], 1)

  screens.extend([ Screen(top = main_bar, bottom = lower_bar), Screen() ])


  #
  # Groups
  #
  group_def = 'n m comma:c period:p u i o p'
  if dualscreen:
    group_def += ' slash:/'

  for key in group_def.split():
    if len(key) is 1:
      name = key.upper()
    else:
      key, name = key.split(':')

    groups.append(Group(name))
    keys.append(Key(normal, key, lazy.screen.togglegroup(name)))
    keys.append(Key(strong, key, lazy.window.togroup(name)))

  if dualscreen:
    lazy.group['/'].toScreen(1)


  #
  # Layouts
  #
  class CustomStack(layout.Stack):
    def cmd_switchdown(self, offset):
      offset %= len(self.stacks)
      if self.currentStackOffset is offset:
        self.cmd_down()
      else:
        self.group.focus(self.stacks[offset].cw, True)

  layouts.extend([
    CustomStack(num_stacks=1, border_width=0),
    CustomStack(num_stacks=2, border_width=1),
  ])


  #
  # Mouse floats
  #
  mouse.extend([
    Drag(normal, "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag(normal, "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size())
  ])


#
# Execute main(), useful to test the file before restarting.
#
if __name__ == '__main__':
  main(None)

