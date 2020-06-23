from libqtile.config import Key, Drag, Click
from libqtile.command import lazy

from functions import Function


class Keys(object):

    ##### GENERAL KEYBINDINGS #####

    def init_keys(self):
        # Key alias
        mod = "mod4"
        alt = "mod1"
        altgr = "mod3"

        return [
  ]

    ##### GROUPS KEYBINDINGS #####

    def init_group_keybindings(self, groups):
        # Key alias
        mod = "mod4"
        alt = "mod1"
        altgr = "mod3``"

        group_keys = []
        group_keys += [str(i) for i in range(1, 10)]
        group_keys += ["0", "minus", "equal"]

        keys = []

        # For all, less the group for "minimized" windows
        for i, group in enumerate(groups[0:-1]):
            # Switch to another group
            keys.append(Key([mod], group_keys[i], lazy.group[group.name].toscreen()))

            # Move current window to another group
            keys.append(Key([mod, "shift"], group_keys[i], lazy.window.togroup(group.name)))

            # Move with current window to another group
            keys.append(Key([mod, "control"], group_keys[i],
                            lazy.window.togroup(group.name),
                            lazy.group[group.name].toscreen()))

        return keys


class Mouses(object):

    ##### MOUSE #####

    def init_mouse(self):
        # Key alias
        mod = "mod4"
        alt = "mod1"
        altgr = "mod3"

        return [
            # Move floating windows
            Drag(
                [mod], "Button1", lazy.window.set_position_floating(),
                start=lazy.window.get_position()
            ),

            # Resize floating windows
            Drag(
                [mod], "Button3", lazy.window.set_size_floating(),
                start=lazy.window.get_size()
            ),

            # Bring to front
            Click([mod, alt], "Button1", lazy.window.bring_to_front())
        ]

# vim: tabstop=4 shiftwidth=4 noexpandtab
