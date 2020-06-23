#!/bin/bash


rofi_command="rofi -theme  .config/qtile/rofi/appmenu/applaunch.rasi"

# Links
terminal=""
files=""
editor=""
browser=""
music=""
settings=""

# Variable passed to rofi
options="$terminal\n$files\n$editor\n$browser\n$music\n$settings"

chosen="$(echo -e "$options" | $rofi_command -p "Most Used" -dmenu -selected-row 0)"
case $chosen in
    $terminal)
        kitty &
        ;;
    $files)
        pcmanfm &
        ;;
    $editor)
        gedit &
        ;;
    $browser)
        firefox-developer-edition &
        ;;
    $music)
        spotify &
        ;;
    $settings)
        xfce4-settings-manager &
        ;;
esac
