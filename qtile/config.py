#
#
#
from libqtile.config import Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget

normal = ['mod4']
heavy = ['mod4', 'mod1']




#
# keys and groups
#
xterm = 'xterm -fn "*-fixed-*-*-*-20-*" '
commands = {
  'b': 'chromium-browser',
  'v': 'gvim',
  't': '_tango_newsletter',
  'c': xterm + '-e coffee',
  'a': xterm + '-e alsamixer',
  'F12': 'key_u_all',
  'Return': xterm,

  'equal': 'amixer -c 0 -q set Master 2dB+',
  'minus': 'amixer -c 0 -q set Master 2dB-',
}

heavy_commands = {
  's': 'setxkbmap -layout se',
  'g': 'setxkbmap -layout gr',
  'i': 'setxkbmap -layout it',
  '0': 'setxkbmap -layout us',
}

keys = [
  Key(heavy,  "q",              lazy.shutdown()),
  Key(normal, "j",              lazy.layout.switchdown(0)),
  Key(normal, "k",              lazy.layout.switchdown(1)),
  Key(normal, "h",              lazy.screen.prevgroup()),
  Key(normal, "l",              lazy.screen.nextgroup()),
  Key(normal, "space",          lazy.screen.grouptoggle()),
  Key(normal, "semicolon",      lazy.spawncmd()),
  Key(normal, "t",              lazy.layout.toggle_split()),
  Key(normal, "r",              lazy.layout.rotate()),
  Key(normal, "apostrophe",     lazy.nextlayout()),
  Key(normal, "x",              lazy.window.kill()),
]





#
# Screens and bars
#
class CustomWindowName(widget.WindowName):
  pass
#  def __init__(self):
#    super(CustomWindowName, self).__init__()
#
#  def button_press(self, x, y, button):
#    f = open('qtile.xxx', 'at')
#    f.write("%d %d %d" % (x, y, button))
#    f.close()
#    group = self.qtile.currentGroup
#    if button == 5:
#      group.cmd_prevgroup()
#    elif button == 4:
#      group.cmd_nextgroup()



main_bar = bar.Bar([
  widget.GroupBox(
    urgent_alert_method='text',
    padding=1,
    margin_x=1,
    margin_y=1,
    active='0000FF',
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

screens = [ Screen(top = main_bar) ]



#
# Groups
#
groups = []
for key in 'n m comma period u i o p'.split():
  name = key.upper() if len(key) is 1 else key[0]
  groups.append(Group(name))
  keys.append( Key(normal, key, lazy.screen.grouptoggle(name)) )
  keys.append( Key(heavy, key, lazy.window.togroup(name)) )

keys += [ Key(normal, k, lazy.spawn(v)) for k, v in commands.items()]
keys += [ Key(heavy, k, lazy.spawn(v)) for k, v in heavy_commands.items()]



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

layouts = [
  CustomStack(stacks=1, border_width=0),
  CustomStack(stacks=2, border_width=1),
]



#
# init commands
#
from os import system
system('setxkbmap -option ctrl:nocaps')
system('fbsetbg -a ~/.usr/GUI/bg.jpg') 
system('xsetroot -cursor_name left_ptr')

