#!/bin/bash

red=0
green=0
blue=0

while getopts r:g:b: flag
do
    case "${flag}" in
        r) red=${OPTARG};;
        g) green=${OPTARG};;
        b) blue=${OPTARG};;
    esac
done

list="$(find /sys/devices/platform/soc/fe201000.serial/tty/ttyAMA0/hci0/hci0\:11/ -name brightness)"

for file in $list; do
    if [[ "$file" == *"red"* ]]; then
        echo $red > $file;
    elif [[ "$file" == *"green"* ]]; then .- 
        echo $green > $file;
    elif [[ "$file" == *"blue"* ]]; then
        echo $blue > $file;
    fi
done
