#
##### IMPORTS #####
import os
import re
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, hook
from libqtile.config import Group  # NOQA
from libqtile import layout, bar, widget, hook  # NOQA
from keys import keys  # NOQA
from layouts import layout_theme, layouts  # NOQA
from theme import colors  # NOQA
from bars import init_widgets_list  # NOQA
from groups import group_names, groups, keys  # NOQA

# DEFINING SOME VARIABLES
mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"  # My terminal of choice
myConfig = "/home/dt/.config/qtile/config.py"  # The Qtile config file location


##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="SF Mono Heavy",
    fontsize=12,
    padding=2,
    background=colors[0]
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
focus_on_window_activation = "smart"
auto_fullscreen = True
# SCREENS

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

# FLOATING WINDOWS
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
if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


# STARTUP APPLICATIONS
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# Restart amd Reload Screens
@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    qtile.cmd_restart()


# WM Fakeout for Java
wmname = "LG3D"

##### FLOATING TRANSIENT CLIENTS #####

@hook.subscribe.client_new
def transient_window(window):
    if window.window.get_wm_transient_for():
        window.floating = True

##### RESTART ON SCREEN CHANGE #####

@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    qtile.cmd_restart()
