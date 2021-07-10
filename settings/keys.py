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
myConfig = "/home/tlh/.config/qtile/config.py"  # The Qtile config file location

##### KEYBINDINGS #####
keys = [
    # The essentials
    Key(
        [mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal With Fish Shell'
    ),
    Key(
        [mod, "shift"], "Return",
        lazy.spawn(
            "rofi -show drun -theme ~/.config/qtile/rofi/appmenu/rofi.rasi 'Run: '"),
        desc='Dmenu Run Launcher'
    ),
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
    ),
    Key(
        [mod, ], "x",
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
    # Switch focus to specific monitor (out of three)
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
    Key([mod, ], "Home",
        lazy.spawn(
            "rofi -dpi  -show drun -theme ~/.config/qtile/rofi/appmenu/rofi.rasi"),
        desc='Launch App Menu'
        ),
    Key([mod, "control"], "Escape",
        lazy.spawn(".config/qtile/rofi/appmenu/applaunch.sh"),
        desc='Launch App Menu'
        ),
    Key(
        [mod, ], "F2",
        lazy.spawn("firefox"),
        desc='Browser'
    ),
    Key(
        [mod, ], "F3",
        lazy.spawn("thunar"),
        desc='lynx browser'
    ),
    Key(
        [mod, "control"], "F3",
        lazy.spawn(myTerm + " -e sudo ranger"),
        desc='lynx browser'
    ),
    Key(
        [mod, "control"], "F4",
        lazy.spawn("emojipick"),
        desc='newsboat'
    ),
    Key(
        [mod], "F4",
        lazy.spawn("fa-rofi"),
        desc='Font Awesome Icon Picker'
    ),
    Key(
        [mod], "F5",
        lazy.spawn(".config/qtile/rofi/network/network.sh"),
        desc='Network Menu'
    ),
    Key(
        [mod, ], "Escape",
        lazy.spawn(".config/qtile/rofi/power/power.sh"),
        desc='Font Awesome Icon Picker'
    ),
    Key(
        [mod, "mod1"], "F6",
        lazy.spawn(myTerm + " -e nvim"),
        desc='nvim'
    ),
    Key(
        [mod], "Print",
        lazy.spawn(".config/qtile/rofi/screenshot/screenshot.sh"),
        desc='print screen'
    ),

]

    # ------------ Hardware Configs ------------

    # # Volume
    # ([], "XF86AudioLowerVolume", lazy.spawn(
    #     "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    # )),
    # ([], "XF86AudioRaiseVolume", lazy.spawn(
    #     "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    # )),
    # ([], "XF86AudioMute", lazy.spawn(
    #     "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    # )),

    # # Brightness
    # ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    # ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

