
from libqtile.manager import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

#
# Custom stuff
#
class CustomStack(layout.Stack):
  def __self__(**args):
    layout.Stack.__init__(self, args)

  def cmd_switchdown(self, offset):
    if self.currentStackOffset is offset:
      self.cmd_down()
    else:
      self.group.focus(self.stacks[offset].cw, True)



#
# general
#
mod = 'mod4'

layouts = [
  layout.Max(),
  CustomStack(stacks=2, border_width=1),
]



# screens
main_bar = bar.Bar([
  widget.GroupBox(
    urgent_alert_method='text',
    padding=1,
    margin_x=1,
    margin_y=1,
    active='0000FF',
    inactive='CCCCCC'),
  widget.Sep(),
  widget.WindowName(),
  widget.Sep(),
  widget.Notify(),
  widget.Prompt(),
  widget.Volume(),
  widget.Systray(),
  widget.Clock('%m%d %a %I:%M%P'),
], 20)

screens = [ Screen(bottom = main_bar) ]



# keys and groups
commands = {
  's': 'setxkbmap -layout se',
  'g': 'setxkbmap -layout gr',
  'i': 'setxkbmap -layout it',
  '0': 'setxkbmap -layout us',
  'b': 'chromium-browser',
  'v': 'gvim',
  'F12': 'key_u_all',
  'Return': 'xterm',

  'equal': 'amixer -c 0 -q set Master 2dB+',
  'minus': 'amixer -c 0 -q set Master 2dB-',
}

keys = [
  Key([mod], "q",              lazy.shutdown()),
  Key([mod], "j",              lazy.layout.switchdown(0)),
  Key([mod], "k",              lazy.layout.switchdown(1)),
  Key([mod], "apostrophe",     lazy.layout.next()),
  Key([mod], "h",              lazy.group.prevgroup()),
  Key([mod], "l",              lazy.group.nextgroup()),
  Key([mod], "space",          lazy.spawncmd()),
  Key([mod], "t",              lazy.layout.toggle_split()),
  Key([mod], "r",              lazy.layout.rotate()),
  Key([mod], "Tab",            lazy.nextlayout()),
  Key([mod], "x",              lazy.window.kill()),

] + [ Key([mod], k, lazy.spawn(v)) for k, v in commands.items()]



groups = []
for key in 'n m comma period u i o p'.split():
  name = key.upper() if len(key) is 1 else key[0]
  groups.append(Group(name))
  keys.append( Key([mod], key, lazy.group[name].toscreen()) )
  keys.append( Key([mod, "mod1"], key, lazy.window.togroup(name)) )



# mouse
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

