import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, hook
from libqtile.config import Group
from libqtile import layout, bar, widget, hook

mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"  # My terminal of choice
myConfig = "/home/dt/.config/qtile/config.py"  # The Qtile config file location

##### KEYBINDINGS #####
keys = [
    ### The essentials
    Key(
        [mod], "Return",
        lazy.spawn(myTerm),
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
    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
    # Treetab controls
    Key([mod, "control"], "k",
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "control"], "j",
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
        ),
    # Window controls
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
   # Stack controls
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


    # Applications = Windows Key + Fn Function Keys
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
