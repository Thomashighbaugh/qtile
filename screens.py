from libqtile.config import Screen
from libqtile import bar
from typing import List  # noqa: F401
from bars import init_widgets_list
##### SCREENS ##### (TRIPLE MONITOR SETUP)

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1  # Slicing removes unwanted widgets on Monitors 1,3


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2  # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=36)),
            Screen(bottom=bar.Bar(widgets=init_widgets_screen2(), opacity=0.95, size=36)),
            Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=36))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()
