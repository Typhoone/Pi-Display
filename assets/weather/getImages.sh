#!/bin/bash
names=''
for daynight in d n
do
    for name in 01 02 03 04 09 10 11 13 50
    do
        wget "http://openweathermap.org/img/wn/${name}${daynight}@4x.png"
    done
done

