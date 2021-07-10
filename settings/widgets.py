from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
#  widget.TextBox(
#             text=" ₿",
#             padding=0,
#             foreground=colors[4],
#             background=colors[0],
#             fontsize=18
#         ),


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='SFMono Nerd Font Heavy',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
        separator(),
        separator(),
        widget.TextBox(
            text=" ₿",
            padding=0,
            background=colors['color2'],
            foreground=colors['text'],
            fontsize=18
        ),
        widget.BitcoinTicker(
            background=colors['color2'],
            foreground=colors['text'],
            padding=5,
            fontsize=15
        ),
        separator(),
        widget.TextBox(
            text=" ",
            padding=2,
            background=colors['color3'],
            foreground=colors['text'],
            fontsize=18
        ),
        widget.ThermalSensor(
            background=colors['color3'],
            foreground=colors['text'],
            padding=5
        ),
        separator(),
        widget.TextBox(
            text=" ",
            background=colors['color1'],
            foreground=colors['text'],
            padding=0,
            fontsize=22
        ),
        widget.Memory(
            background=colors['color1'],
            foreground=colors['text'],
            padding=5
        ),
        separator(),
        widget.TextBox(
            text=" Vol:",
            background=colors['color2'],
            foreground=colors['text'],
            padding=0
        ),
        widget.Volume(
            background=colors['color2'],
            foreground=colors['text'],
            padding=5
        ),

    ]


primary_widgets = [
    *workspaces(),


    separator(),
    icon(bg="color3", text=' '),  # Icon: nf-fa-feed

    widget.Net(**base(bg='color3'), interface='wlp2s0'),

    separator(),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    separator(),
    widget.Systray(background=colors['dark'], padding=5),
    separator(),
    icon(bg="color1", fontsize=17, text=' '),  # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%m/%d/%Y - %H:%M '),




]

secondary_widgets = [
    *workspaces(),

    separator(),



    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    separator(),


    widget.Clock(**base(bg='color2'), format='%m/%d/%Y - %H:%M '),


]

widget_defaults = {
    'font': 'SFMono Nerd Font Heavy',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
