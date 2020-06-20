# from os.path import expanduser
import os
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401
import socket
from libqtile.widget import (
    GroupBox,
    Prompt,
    WindowName,
    TextBox,
    Net,
    CurrentLayout,
    CurrentLayoutIcon,
    CheckUpdates,
    Systray,
    CapsNumLockIndicator,
    TaskList,
    # Battery,
    ThermalSensor,
    Memory,
    Clock
)  # NOQA

from widget.battery import Battery
from widgets import Pipe_Widgets as Separator_Widgets
# from widgets import Colon_Widgets as Separator_Widgets
from widgets import Space_Widgets
from aesthetics import Colors, Fonts

# PROMPT
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
# WIDGETS
# DEFAULTS
widget_defaults = dict(
    font="SF Mono Heavy",
    fontsize=12,
    padding=2,
)
extension_defaults = widget_defaults.copy()


class Widgets_List(object):
    color = Colors()
    font = Fonts()

    space = Space_Widgets()
    separator = Separator_Widgets()

    ##### WIDGETS LIST #####

    def init_top_single(self, tray=True):
        wl = [
            widget.Sep(
                linewidth=0,
                padding=6,
                foreground=self.color.grey,
                background=self.color.black
            ),
            widget.GroupBox(font="SF Mono Heavy",
                            fontsize=9,
                            margin_y=3,
                            margin_x=0,
                            padding_y=5,
                            padding_x=5,
                            borderwidth=3,
                            active=self.color.grey,
                            inactive=self.color.grey,
                            rounded=True,
                            highlight_color=self.color.grey,
                            highlight_method="line",
                            this_current_screen_border=self.color.white,
                            this_screen_border=self.color.blue,
                            other_current_screen_border=self.color.black,
                            other_screen_border=self.color.black,
                            foreground=self.color.grey,
                            background=self.color.black
                            ),
            widget.Prompt(
                prompt=prompt,
                font="SF Mono Heavy",
                padding=10,
                foreground=self.color.white,
                background=self.color.grey
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                foreground=self.color.grey,
                background=self.color.black
            ),
            widget.WindowName(
                foreground=self.color.white,
                background=self.color.black,
                padding=0
            ),
            widget.Systray(
                background=self.color.black,
                padding=5
            ),
            widget.TextBox(
                text=" ₿",
                padding=0,
                foreground=self.color.blue,
                background=self.color.black,
                fontsize=18
            ),
            widget.BitcoinTicker(
                foreground=self.color.grey,
                background=self.color.black,
                padding=5,
                fontsize=15
            ),
            widget.TextBox(
                text=" ",
                padding=2,
                foreground=self.color.red,
                background=self.color.black,
                fontsize=18
            ),
            widget.ThermalSensor(
                foreground=self.color.red,
                background=self.color.black,
                padding=5
            ),
            widget.TextBox(
                text=" ",
                foreground=self.color.blue,
                background=self.color.black,
                padding=0,
                fontsize=22
            ),
            widget.Memory(
                foreground=self.color.blue,
                background=self.color.black,
                padding=5
            ),
            widget.TextBox(
                text=" Vol:",
                foreground=self.color.red,
                background=self.color.black,
                padding=0
            ),
            widget.Volume(
                foreground=self.color.red,
                background=self.color.black,
                padding=5
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                foreground=self.color.blue,
                background=self.color.black,
                padding=0,
                scale=0.5
            ),
            widget.Clock(
                foreground=self.color.grey,
                background=self.color.black,
                format="%B %d  %H:%M "
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.color.black,
                background=self.color.black
            ),

        ]
        return wl

    def init_top_double(self, tray=True):
        wl = [widget.Sep(
            linewidth=0,
            padding=6,
            foreground=self.color.grey,
            background=self.color.black
        ),
            widget.GroupBox(font="SF Mono Heavy",
                            fontsize=9,
                            margin_y=3,
                            margin_x=0,
                            padding_y=5,
                            padding_x=5,
                            borderwidth=3,
                            active=self.color.grey,
                            inactive=self.color.grey,
                            rounded=True,
                            highlight_color=self.color.grey,
                            highlight_method="line",
                            this_current_screen_border=self.color.white,
                            this_screen_border=self.color.blue,
                            other_current_screen_border=self.color.black,
                            other_screen_border=self.color.black,
                            foreground=self.color.grey,
                            background=self.color.black
                            ),
            widget.Prompt(
                prompt=prompt,
                font="SF Mono Heavy",
                padding=10,
                foreground=self.color.white,
                background=self.color.grey
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                foreground=self.color.grey,
                background=self.color.black
            ),
            widget.WindowName(
                foreground=self.color.white,
                background=self.color.black,
                padding=0
            ),
            widget.Systray(
                background=self.color.black,
                padding=5
            ),
            widget.TextBox(
                text=" ₿",
                padding=0,
                foreground=self.color.blue,
                background=self.color.black,
                fontsize=18
            ),
            widget.BitcoinTicker(
                foreground=self.color.grey,
                background=self.color.black,
                padding=5,
                fontsize=15
            ),
            widget.TextBox(
                text=" ",
                padding=2,
                foreground=self.color.red,
                background=self.color.black,
                fontsize=18
            ),
            widget.ThermalSensor(
                foreground=self.color.red,
                background=self.color.black,
                padding=5
            ),
            widget.TextBox(
                text=" ",
                foreground=self.color.blue,
                background=self.color.black,
                padding=0,
                fontsize=22
            ),
            widget.Memory(
                foreground=self.color.blue,
                background=self.color.black,
                padding=5
            ),
            widget.TextBox(
                text=" Vol:",
                foreground=self.color.red,
                background=self.color.black,
                padding=0
            ),
            widget.Volume(
                foreground=self.color.red,
                background=self.color.black,
                padding=5
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                foreground=self.color.blue,
                background=self.color.black,
                padding=0,
                scale=0.5
            ),
            widget.Clock(
                foreground=self.color.grey,
                background=self.color.black,
                format="%B %d  %H:%M "
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.color.black,
                background=self.color.black
            ),
        ]

        return wl

    def init_bottom_double(self):
        wl = [widget.Sep(
            linewidth=0,
            padding=6,
            foreground=self.color.grey,
            background=self.color.black
        ),
            widget.GroupBox(font="SF Mono Heavy",
                            fontsize=9,
                            margin_y=3,
                            margin_x=0,
                            padding_y=5,
                            padding_x=5,
                            borderwidth=3,
                            active=self.color.grey,
                            inactive=self.color.grey,
                            rounded=True,
                            highlight_color=self.color.grey,
                            highlight_method="line",
                            this_current_screen_border=self.color.white,
                            this_screen_border=self.color.blue,
                            other_current_screen_border=self.color.black,
                            other_screen_border=self.color.black,
                            foreground=self.color.grey,
                            background=self.color.black
                            ),
            widget.Prompt(
                prompt=prompt,
                font="SF Mono Heavy",
                padding=10,
                foreground=self.color.white,
                background=self.color.grey
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                foreground=self.color.grey,
                background=self.color.black
            ),
            widget.WindowName(
                foreground=self.color.white,
                background=self.color.black,
                padding=0
            ),
            widget.Systray(
                background=self.color.black,
                padding=5
            ),
            widget.TextBox(
                text=" ₿",
                padding=0,
                foreground=self.color.blue,
                background=self.color.black,
                fontsize=18
            ),
            widget.BitcoinTicker(
                foreground=self.color.grey,
                background=self.color.black,
                padding=5,
                fontsize=15
            ),
            widget.TextBox(
                text=" ",
                padding=2,
                foreground=self.color.red,
                background=self.color.black,
                fontsize=18
            ),
            widget.ThermalSensor(
                foreground=self.color.red,
                background=self.color.black,
                padding=5
            ),
            widget.TextBox(
                text=" ",
                foreground=self.color.blue,
                background=self.color.black,
                padding=0,
                fontsize=22
            ),
            widget.Memory(
                foreground=self.color.blue,
                background=self.color.black,
                padding=5
            ),
            widget.TextBox(
                text=" Vol:",
                foreground=self.color.red,
                background=self.color.black,
                padding=0
            ),
            widget.Volume(
                foreground=self.color.red,
                background=self.color.black,
                padding=5
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                foreground=self.color.blue,
                background=self.color.black,
                padding=0,
                scale=0.5
            ),
            widget.Clock(
                foreground=self.color.grey,
                background=self.color.black,
                format="%B %d  %H:%M "
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.color.black,
                background=self.color.black
            ),
        ]

        return wl

# vim: tabstop=4 shiftwidth=4 noexpandtab
