from libqtile.config import Group  # NOQA
from libqtile import layout, bar, widget, hook  # NOQA
from keys import keys  # NOQA

from theme import colors  # NOQA
from bars import init_widgets_list  # NOQA

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "00caff",
                "border_normal": "24262d"
                }

# THE LAYOUTS
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
