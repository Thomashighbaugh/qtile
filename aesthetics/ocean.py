from libqtile.layout.floating import Floating

class Colors(object):

	# Ocean
	black =		["#2d2f3d", "#2d2f3d"]
	grey =		["#3c3f4c", "#3c3f4c"]
	lightgrey =	["#555566", "#555566"]
	white =		["#e9e9ff", "#edeeff"]
	red =		["#ff9cff", "#ff9cff"]
	magenta =	["#f850ac", "#f850ac"]
	green =		["#76dcdd", "#76dcdd"]
	darkgreen =	["#00b6b2", "#00b6b2"]
	blue =		["#00caff", "#00caff"]
	darkblue =	["#61aeee", "#61aeee"]
	orange =	["#f9f871", "#f9f871"]

class Fonts(object):

	base = "SF Mono"
	bold = "SF Mono Heavy"

class Layout_Aesthetics(object):

	layout_theme = {
		"margin":			2,
		"border_width":		2,
		"border_focus":		Colors.blue[0],
		"border_normal":	Colors.black[0],
	}

	floating_layout = Floating(
		border_width = 	2,
		border_focus = 	Colors.blue[0],
		border_normal = Colors.black[0],
	)

class Widget_Aesthetics(object):

	widget_defaults = dict(
		font =			Fonts.base,
		fontsize =		10.5,
		padding =		2,
		foreground =	Colors.white,
		background =	Colors.black
	)

class Extension_Aesthetics(object):

	extension_defaults = dict(
		font =					Fonts.base,
		fontsize =				12,
		dmenu_ignorecase =		True,
		dmenu_prompt =			">",
		selected_foreground =	Colors.blue,
		foreground =			Colors.white,
		selected_background =	Colors.grey,
		background =			Colors.black
	)

# vim: tabstop=4 shiftwidth=4 noexpandtab
