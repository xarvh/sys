
from typing import List  # noqa: F401

from os import system, uname
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal



# key modifiers
normal = ['mod4']
strong = ['mod4', 'mod1']


#
# Keys
#
keys = []

def initKeys():

  #
  # commands
  #
  term = '_terminal '
  normal_commands = {
    'b': 'google-chrome',
    'y': term + '-x _calendar',
    'v': 'gvim',
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
    'BackSpace': '_qtile_restart',
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
    Key(normal, 'space',          lazy.screen.toggle_group()),
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
# Groups
#
groups = []

def initGroups():

  group_def = 'n m comma:c period:p u i o p'
#  if dualscreen:
#   group_def += ' slash:/'

  for key in group_def.split():
    if len(key) == 1:
      name = key.upper()
    else:
      key, name = key.split(':')

    groups.append(Group(name))
    keys.append(Key(normal, key, lazy.screen.toggle_group(name)))
    keys.append(Key(strong, key, lazy.window.togroup(name)))

#  if dualscreen:
#   lazy.group['/'].toScreen(1)



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

layouts = [
        CustomStack(num_stacks=1, border_width=0),
        CustomStack(num_stacks=2, border_width=1),
      ]


#layouts = [
#    layout.Columns(border_focus_stack='#d75f5f'),
#    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
#]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()





#
# Screens
#
screens = []

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


def initScreens():

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
    widget.Volume(), #cardid=sound_card, device=None),
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
# Mouse
#

# Drag floating layouts.
mouse = [
    Drag(normal, "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag(normal, "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click(normal, "Button2", lazy.window.bring_to_front())
]




dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


initKeys()
initScreens()
initGroups()
system('_qtile_init &')
