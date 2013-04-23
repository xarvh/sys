#
#
#
from libqtile.manager import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

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
  Key(normal, "h",              lazy.group.prevgroup()),
  Key(normal, "l",              lazy.group.nextgroup()),
  Key(normal, "semicolon",      lazy.group.group_toggle(True)),
  Key(normal, "space",          lazy.spawncmd()),
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
#  widget.Notify(),
  widget.Prompt(),
  widget.Volume(),
  widget.Systray(),
  widget.Clock('%m%d %a %I:%M%P'),
], 20)

screens = [ Screen(top = main_bar) ]



# mouse
mouse = [
    Drag(normal, "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag(normal, "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click(normal, "Button2", lazy.window.bring_to_front())
]



#
# Groups
#
class CustomGroup(Group):

  def cmd_group_toggle(self, force_previous=False):
    screen = self.qtile.currentScreen
    target_group = self
    if screen.group is self or force_previous:
      try: target_group = screen.previous_group
      except AttributeError: pass

    screen.previous_group = screen.group
    screen.setGroup(target_group)


groups = []
for key in 'n m comma period u i o p'.split():
  name = key.upper() if len(key) is 1 else key[0]
  groups.append(CustomGroup(name))
  keys.append( Key(normal, key, lazy.group[name].group_toggle()) )
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

