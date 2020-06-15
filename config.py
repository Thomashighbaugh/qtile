#
##### IMPORTS #####
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, hook
from libqtile.config import Group
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401
from screens import screens
##### DEFINING SOME VARIABLES #####
mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"  # My terminal of choice
myConfig = "/home/dt/.config/qtile/config.py"  # The Qtile config file location

##### KEYBINDINGS #####
keys = [
    ### The essentials
    Key(
        [mod], "Return",
        lazy.spawn(myTerm + " -e zsh"),
        desc='Launches My Terminal With Fish Shell'
    ),
    Key(
        [mod, "shift"], "Return",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc='Dmenu Run Launcher'
    ),
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
    ),
    Key(
        [mod, "shift"], "c",
        lazy.window.kill(),
        desc='Kill active window'
    ),
    Key(
        [mod, ], "r",
        lazy.restart(),
        desc='Restart Qtile'
    ),
    Key(
        [mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
    ),
    ### Switch focus to specific monitor (out of three)
    Key([mod, "shift"], "w",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod, "shift"], "e",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),
    Key([mod, "shift"], "r",
        lazy.to_screen(2),
        desc='Keyboard focus to monitor 3'
        ),
    ### Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
    ### Treetab controls
    Key([mod, "control"], "k",
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "control"], "j",
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
        ),
    ### Window controls
    Key(
        [mod], "k",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
    ),
    Key(
        [mod], "j",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
    ),
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
    ),
    Key(
        [mod], "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),
    Key(
        [mod], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),
    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
    ),
    Key(
        [mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
    ),
    Key(
        [mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
    ),
    ### Stack controls
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
    ),
    Key(
        [mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
    ),
    Key(
        [mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
    ),
    ### Dmenu scripts launched with ALT + CTRL + KEY

    ### My applications launched with SUPER + ALT + KEY
    Key([mod, ], "F1",
        lazy.spawn("rofi -dpi  -show drun -theme ~/.config/qtile/rofi/appmenu/rofi.rasi"),
        desc='Launch App Menu'
        ),
    Key(
        [mod, ], "F2",
        lazy.spawn("firefox-developer-edition"),
        desc='Browser'
    ),
    Key(
        [mod, ], "F3",
        lazy.spawn("thunar"),
        desc='lynx browser'
    ),
    Key(
        [mod, "control"], "F3",
        lazy.spawn(myTerm + " -e gksu ranger"),
        desc='lynx browser'
    ),
    Key(
        [mod, "control"], "F4",
        lazy.spawn("emojipick"),
        desc='newsboat'
    ),
    Key(
        [mod, ], "F4",
        lazy.spawn("fa-rofi"),
        desc='newsboat'
    ),
    Key(
        [mod, "mod1"], "r",
        lazy.spawn(myTerm + " -e rtv"),
        desc='reddit terminal viewer'
    ),
    Key(
        [mod, "mod1"], "e",
        lazy.spawn(myTerm + " -e neomutt"),
        desc='neomutt'
    ),
    Key(
        [mod, "mod1"], "m",
        lazy.spawn(myTerm + " -e sh ./scripts/toot.sh"),
        desc='toot mastodon cli'
    ),
    Key(
        [mod, "mod1"], "t",
        lazy.spawn(myTerm + " -e sh ./scripts/tig-script.sh"),
        desc='tig'
    ),
    Key(
        [mod, "mod1"], "f",
        lazy.spawn(myTerm + " -e sh ./.config/vifm/scripts/vifmrun"),
        desc='vifm'
    ),
    Key(
        [mod, "mod1"], "j",
        lazy.spawn(myTerm + " -e joplin"),
        desc='joplin'
    ),

]

##### GROUPS #####
group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'monadtall'}),
               ("6", {'layout': 'monadtall'}),
               ("7", {'layout': 'monadtall'}),
               ("8", {'layout': 'monadtall'}),
               ("9", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))  # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))  # Send current window to another group

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

##### THE LAYOUTS #####
layouts = [
    layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Stack(stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
        font="SF Mono Heavy",
        fontsize=13,
        sections=["FIRST", "SECOND"],
        section_fontsize=13,
        bg_color="141414",
        active_bg="90C435",
        active_fg="000000",
        inactive_bg="384323",
        inactive_fg="a0a0a0",
        padding_y=5,
        section_top=10,
        panel_width=320
    ),
    layout.Floating(**layout_theme)
]


##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="SF Mono Heavy",
    fontsize=12,
    padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()



##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
# main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"


##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
