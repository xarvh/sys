
from libqtile.manager import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook



# general
mod = "mod4"

layouts = [
  layout.Max(),
  layout.Stack(stacks=2, border_width=1),
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
  'B': 'firefox',
  'Return': 'xterm',

  'equal': 'amixer -c 0 -q set Master 2dB+',
  'minus': 'amixer -c 0 -q set Master 2dB-',
}



keys = [
  Key([mod], "q",  lazy.shutdown()),

  # layouts
  Key([mod], "k",              lazy.layout.down()),
  Key([mod], "j",              lazy.layout.up()),
  Key([mod], "h",              lazy.layout.previous()),
  Key([mod], "l",              lazy.layout.previous()),
  Key([mod, "shift"], "space", lazy.layout.rotate()),
  Key([mod, "shift"], "Return",lazy.layout.toggle_split()),
  Key([mod], "space",         lazy.nextlayout()),
  Key([mod], "x",              lazy.window.kill()),

  # prompts
  Key([mod], "r",              lazy.spawncmd()),
  Key([mod], "g",              lazy.switchgroup()),

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

