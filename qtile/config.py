"""

Guidelines:

  1) ALL WM keyboard commands use the Win mod.
  2) Alt can be used in conjunction with Win to
    - Avoid accidentally issuing especially disruptive commands, or
    - Issue a command related to the non-modified one.

"""

from os import system, uname

from libqtile.config import Key, Screen, Group, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook


#
# exposed globals
#
screens = []
layouts = []
groups = []

keys = []
mouse = []


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
screen_names = {
  'pinky': ['LVDS1', 'VGA1'],
  'salad': ['DVI-0', 'DisplayPort-0'],
  'trash': ['LVDS', 'DFP1'],
}.get(uname()[1], [0, 1])

system(' '.join((
  'xrandr',
  '--output {0} --preferred --primary',
  '--output {1} --preferred --right-of {0}',
  )).format(*screen_names))

#system('setxkbmap -option ctrl:nocaps')
system('xmodmap -e "keycode 66 = Super_L"')
system('xmodmap -e "clear Lock"')
system('fbsetbg -a ~/.usr/gui/bg.jpg') 
system('xsetroot -cursor_name left_ptr')

#
# QTile initialization.
# (main() is run when the qtile instance becomes available.
# http://docs.qtile.org/en/latest/configuration.html#main
#
def main(qtile):

  # TODO: extend for a generic number of screens?
  dualscreen = not qtile or len(qtile.conn.pseudoscreens) > 1

  # key modifiers
  normal = ['mod4']
  strong = ['mod4', 'mod1']


  #
  # commands
  #
  term = 'xterm -fn "*-fixed-*-*-*-20-*" '
  normal_commands = {
    'b': 'chromium-browser',
    'v': 'gvim',
    't': '_tango_newsletter',
    'c': term + '-e coffee',
    'a': term + '-e alsamixer',
    'F12': 'key_u_all',
    'Return': term,

    'equal': 'amixer -c 0 -q set Master 2dB+',
    'minus': 'amixer -c 0 -q set Master 2dB-',
  }

  strong_commands = {
    's': 'setxkbmap -layout se',
    'g': 'setxkbmap -layout gr',
    '1': 'setxkbmap -layout it',
    '0': 'setxkbmap -layout us',
  }

  keys.extend([
    Key(strong, 'q',              lazy.shutdown()),
    Key(normal, 'j',              lazy.layout.switchdown(0)),
    Key(strong, 'j',              lazy.layout.client_to_stack(0)),
    Key(normal, 'k',              lazy.layout.switchdown(1)),
    Key(strong, 'k',              lazy.layout.client_to_stack(1)),
    Key(normal, 'h',              lazy.screen.prevgroup()),
    Key(normal, 'l',              lazy.screen.nextgroup()),
    Key(normal, 'space',          lazy.screen.togglegroup()),
    Key(normal, 'semicolon',      lazy.spawncmd()),
    Key(normal, 't',              lazy.layout.toggle_split()),
    Key(normal, 'r',              lazy.layout.rotate()),
    Key(normal, 'apostrophe',     lazy.nextlayout()),
    Key(normal, 'x',              lazy.window.kill()),
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
        2: lambda: self.qtile.cmd_nextlayout(), # mid mouse, change layout
        3: lambda: screen.group.layout.cmd_switchdown(1), # right mouse, right pane
        4: lambda: screen.cmd_nextgroup(), # wheel up
        5: lambda: screen.cmd_prevgroup(), # wheel down
      }.get(button, lambda: '')()


  main_bar = bar.Bar([
    widget.GroupBox(
      urgent_alert_method='text',
      borderwidth=2,
      padding=1,
      margin_x=1,
      margin_y=1,
      active='FF0000',
      this_current_screen_border='CC0000',
      disable_drag=True,
      inactive='CCCCCC'),
    widget.Sep(),
    CustomWindowName(),
    widget.Sep(),
    widget.Notify(),
    widget.Prompt(),
    widget.Volume(),
    widget.Systray(),
    widget.Clock('%m%d %a %I:%M%P'),
  ], 20)


  lower_bar = bar.Bar([
    CustomWindowName(),
  ], 1)

  screens.extend([ Screen(top = main_bar, bottom = lower_bar), Screen() ])


  #
  # Groups
  #
  group_def = 'n m comma:, period:. u i o p'
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
    CustomStack(stacks=1, border_width=0),
    CustomStack(stacks=2, border_width=1),
  ])


#
# Execute main(), useful to test the file before restarting.
#
if __name__ == '__main__':
  main(None)

