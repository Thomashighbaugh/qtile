import os
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401
from theme import colors
import socket

# PROMPT
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
# WIDGETS
# DEFAULTS
widget_defaults = dict(
    font="SF Mono Heavy",
    fontsize=12,
    padding=2,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.GroupBox(font="SF Mono Heavy",
                        fontsize=9,
                        margin_y=3,
                        margin_x=0,
                        padding_y=5,
                        padding_x=5,
                        borderwidth=3,
                        active=colors[2],
                        inactive=colors[2],
                        rounded=True,
                        highlight_color=colors[1],
                        highlight_method="line",
                        this_current_screen_border=colors[3],
                        this_screen_border=colors[4],
                        other_current_screen_border=colors[0],
                        other_screen_border=colors[0],
                        foreground=colors[2],
                        background=colors[0]
                        ),
        widget.Prompt(
            prompt=prompt,
            font="SF Mono Heavy",
            padding=10,
            foreground=colors[3],
            background=colors[1]
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=0
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
        widget.TextBox(
            text=" ₿",
            padding=0,
            foreground=colors[4],
            background=colors[0],
            fontsize=18
        ),
        widget.BitcoinTicker(
            foreground=colors[2],
            background=colors[0],
            padding=5,
            fontsize=15
        ),
        widget.TextBox(
            text=" ",
            padding=2,
            foreground=colors[5],
            background=colors[0],
            fontsize=18
        ),
        widget.ThermalSensor(
            foreground=colors[5],
            background=colors[0],
            padding=5
        ),
        widget.TextBox(
            text=" ",
            foreground=colors[4],
            background=colors[0],
            padding=0,
            fontsize=22
        ),
        widget.Memory(
            foreground=colors[4],
            background=colors[0],
            padding=5
        ),
        widget.TextBox(
            text=" Vol:",
            foreground=colors[5],
            background=colors[0],
            padding=0
        ),
        widget.Volume(
            foreground=colors[5],
            background=colors[0],
            padding=5
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[4],
            background=colors[0],
            padding=0,
            scale=0.5
        ),
        widget.Clock(
            foreground=colors[2],
            background=colors[0],
            format="%B %d  %H:%M "
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[0],
            background=colors[0]
        ),

    ]
    return widgets_list
