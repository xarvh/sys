#!/bin/sh
xrandr --output eDP-1-1 --off --output DP-1-1 --off --output HDMI-1-1 --mode 1360x768 --pos 0x0 --rotate normal --output HDMI-1-2 --off
pacmd set-card-profile 0 output:hdmi-stereo
