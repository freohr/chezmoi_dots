#!/bin/bash

# Define your monitor you can get it by typing hyprctl monitor
MONITOR="DP-2"
RESOLUTION="2560x1440"

CURRENT_RATE=$(hyprctl monitors | grep "$MONITOR" -A 1 | grep -o '@[0-9.]*' | sed 's/@//')

CURRENT_RATE=$(bc <<MATH
($CURRENT_RATE + 1)/1
MATH)

# Refresh rates to switch between
RATE1="144"
RATE2="60"

if [ "$(echo $CURRENT_RATE)" == "$(echo $RATE1)" ]; then
  hyprctl keyword monitor ${MONITOR},${RESOLUTION}@${RATE2},auto,1
else
  hyprctl keyword monitor ${MONITOR},${RESOLUTION}@${RATE1},auto,1
fi
