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
#from libqtile.manager import Drag
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
# Run initial scripts
#
system('_qtile_init &')


#
#
#
def commandStdout(cmd):
    return subprocess.check_output([cmd], shell=True).decode('utf-8').split('\n')



#
# sound card
#
def guessAlsaSoundCard():
  try:
    return int(commandStdout('aplay -l |grep card |grep -vi hdmi')[:-1][0][5])
  except Exception as e:
    print(e)
    return 0

sound_card = guessAlsaSoundCard()



#
# Hooks
#
@hook.subscribe.screen_change
def restart_on_screen_change(qtile, ev):
  system('_qtile_on_screen_change &')
  #qtile.cmd_restart()



@hook.subscribe.client_new
def floating_dialogs(window):

    if window.window.get_wm_class() == ('UE4Editor', 'UE4Editor'):
        if window.window.get_name() == None:
            window.floating = True

    if window.window.get_wm_class() == ('Unity', 'Unity'):
        if window.window.get_name() == None:
            window.floating = True


#
# Initialization commands.
# (These run before the qtile instance is available.)
#
mainScreenName = commandStdout('xrandr-list')[0]



#
# GPU Temperatur monitor
#
def getTemperature():
    cmd = "nvidia-smi -q -d TEMPERATURE |grep 'GPU Current'"
    return commandStdout(cmd)[0].split(':')[1]



#
# QTile initialization.
# (main() is run when the qtile instance becomes available.
# http://docs.qtile.org/en/latest/configuration.html#main
#
def main(qtile):

  system('_modmap us')

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
    'b': 'google-chrome',
    'y': term + '-x _calendar',
    'v': 'gvim',
    #'c': term + '-x coffee',
    'e': term + '-x _elm-repl',
    #'F3': term + '-x alsamixer -c %d' % sound_card,
    'F3': term + '-x pulsemixer',
    'F10': 'take_screenshot',
    'F12': 'mount_and_open_all',
    'Return': term,

    's': '_modmap se',
    '0': '_modmap us',

    'equal': '_volume_up',
    'minus': '_volume_down',
    'bracketleft': 'brightness down',
    'bracketright': 'brightness up',

    'Escape': 'gnome-screensaver-command -l',
    'BackSpace': 'qshell -c "restart()"',
  }

  strong_commands = {
#    'g': '_modmap gr',
#    '1': '_modmap it',
  }

  keys.extend([
    Key([],     'XF86MonBrightnessUp',   lazy.spawn('brightness up')),
    Key([],     'XF86MonBrightnessDown', lazy.spawn('brightness down')),
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
    Key(strong, 'equal',          lazy.spawn('xrandr-reset')),
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
#    widget.GenPollText(
#        update_interval=1,
#        func=getTemperature,
#    ),
    widget.Volume(cardid=sound_card, device=None),
    widget.Sep(),
    CustomWindowName(),
    widget.Sep(),
    widget.Notify(default_timeout=1),
    widget.Prompt(),
#    widget.KeyboardLayout(
#        configured_keyboards=['us', 'se', 'gr'],
#    ),
    widget.Battery(
        update_delay=1,
        format='{char} {percent:2.0%}',
        charge_char='⇶',
        discharge_char='▼'
        ),
    widget.Systray(icon_size=25),
    widget.Clock(format='%m%d %a %H:%M'),
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
    if len(key) == 1:
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
      offset = int(offset) % len(self.stacks)
      if self.current_stack_offset == offset:
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
#    Drag(normal, "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
#    Drag(normal, "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size())
  ])


#
# Execute main(), useful to test the file before restarting.
#
if __name__ == '__main__':
  main(None)

