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
alt = "mod1"
altgr = "mod3"

##### KEYBINDINGS #####
keys = [
    ### The essentials
    # On root
    Key([mod], "Return",
        lazy.spawn("kitty")),

    Key([mod], "r",
        lazy.restart()),  # Restart Qtile
    Key([mod, alt], "Delete",
        lazy.shutdown()),  # Shutdown Qtile

    Key([mod], "p", lazy.spawncmd()),  # Launch Qtile prompt

    Key([mod, "control"], "Escape",
        lazy.spawn("rofi -dpi  -show drun -theme ~/.config/qtile/rofi/appmenu/rofi.rasi")),

    Key([mod], "Tab",
        lazy.next_layout()),  # Cycle Layouts
        Key([mod, alt], "Tab",
        lazy.next_layout()),  # Cycle Layouts

   
    Key([mod, "shift"], "End",
        lazy.window.togroup("")),  # Move to minimized windows group
    Key([mod, "control"], "End",
        lazy.window.togroup(""),
        lazy.group[""].toscreen()),  # Move with to minimized windows group
    Key([mod], "End",
        lazy.window.toggle_minimize()),  # Toogle minimize
    Key([mod], "j", lazy.layout.down()),  # Switch to next window
    Key([mod], "k", lazy.layout.up()),  # Switch to previous window

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down()),  # Move windows down in current stack
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up()),  # Move windows up in current stack

    Key([mod, "control"], "j",
        lazy.layout.client_to_previous()),  # Move window to previous stack side
    Key([mod, "control"], "k",
        lazy.layout.client_to_next()),  # Move window to next stack side

    Key([alt], "Tab",
        lazy.group.next_window(),  # Switch focus to other window
        lazy.window.bring_to_front()),  # Switch focus to other window + front
    Key([alt, "shift"], "Tab",
        lazy.group.prev_window(),
        lazy.window.bring_to_front()),  # Switch focus to other window

    Key([mod], "x",
        lazy.window.kill()),  # Kill active window
    Key([mod, alt], "x",
        lazy.spawn("xkill")),  # Terminate program


    Key([mod], "f",
        lazy.window.toggle_floating()),  # Toggle floating

    # On layout

    Key([mod], "backslash",
        lazy.layout.swap_main()),  # Swap current window to main pane (Xmonad)

    Key([mod], "m",
        lazy.layout.next()),  # Move focus to another stack (Stack)

 
    Key([mod, "shift"], "Down",
        lazy.layout.decrease_nmaster(),           # Decrease number in master pane (Tile)
        lazy.layout.shrink_main()),  # Shrink size of main window (Xmonad)
    Key([mod, "shift"], "Up",
        # lazy.layout.increase_nmaster(),           # Increase number in master pane (Tile)
        lazy.layout.grow_main()),  # Grow size of main window (Xmonad)

    Key([mod,], "n",
        lazy.layout.normalize()),  # Restore all windows to default size ratios
    Key([mod,], "m",
        lazy.layout.maximize()),  # Toggle a window between min and max sizes

    Key([mod, "shift"], "space",
        lazy.layout.rotate(),  # Swap panes of split stack (Stack)
        lazy.layout.flip()),  # Switch side main pane occupies (Xmonad)

    Key([mod], "s",
        lazy.layout.toggle_split()),  # Toggle between split and unsplit (Stack)


    # On group

   

    Key([mod], "Left",
        lazy.screen.prev_group()),  # Move to previous group
    Key([mod], "Right",
        lazy.screen.next_group()),  # Move to next group


    # On screen

    Key([mod], "Page_Up",
        lazy.prev_screen()),  # Switch to previous screen
    Key([mod], "Page_Down",
        lazy.next_screen()),  # Switch to next screen


    Key([mod, "control"], "Home",
        lazy.spawn(".config/qtile/rofi/appmenu/applaunch.sh")),  # App Quicklauncher
    Key([mod, ], "F2",
        lazy.spawn("firefox-developer-edition")),  # Browser
    Key([mod, ], "F3",
        lazy.spawn("thunar")),  # File Manager
    Key([mod, alt], "F3",
        lazy.spawn("kitty -e sudo ranger")),  # Terminal File Manager
    Key([mod, "control"], "F4",
        lazy.spawn("emojipick")),  # Emoji to Clipboard
    Key([mod], "F4",
        lazy.spawn("fa-rofi")),  # Font Awesome Icon TO Clipboard
    Key([mod], "F5",
        lazy.spawn(".config/qtile/rofi/network/network.sh")),  # Network Menu
    Key([mod, alt], "F5",
        lazy.spawn(".config/qtile/rofi/power/power.sh")),  # Power Menu
    Key([mod], "F6",
        lazy.spawn("emacs --with-profile doom")),  # Note Application
    Key([mod, alt], "F6",
        lazy.spawn("kitty -e joplin")),  # Note Application
    Key([mod], "Print",
        lazy.spawn(".config/qtile/rofi/screenshot/screenshot.sh")),  # Print Screen

]
