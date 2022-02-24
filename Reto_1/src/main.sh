#!/bin/bash

USER=$(/usr/bin/whoami)
DIR=$(ls ~/ | grep -e Descargas -e descargas -e downloads -e Downloads)

echo -e "Directorio: "/home"/$USER/$DIR\n" && find ~/$DIR -maxdepth 1 -type f | awk -F/ '{print $5}'


