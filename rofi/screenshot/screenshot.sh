#!/bin/bash

rofi_command="rofi -theme .config/qtile/rofi/screenshot/screenshot.rasi"

# Options
screen=""
area=""

# Variable passed to rofi
options="$screen\n$area"

chosen="$(echo -e "$options" | $rofi_command -p '' -dmenu -selected-row 1)"
case $chosen in
    $screen)
        sleep 1; scrot 'Screenshot_%Y-%m-%d-%S_$wx$h.png' -e 'mv ~/Pictures/Screenshots'
        ;;
    $area)
        scrot --line style=dash,width=1 --select  'Screenshot_%Y-%m-%d-%S_$wx$h.png' -e 'mv ~/Pictures/Screenshots'
        ;;
esac


