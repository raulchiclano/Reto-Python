#!/bin/bash

user=$(whoami)
dir=$(ls ~/ | grep -e Descargas -e descargas -e downloads -e Downloads)

echo -e "Directorio: "/home"/$user/$dir\n" && find ~/$dir -maxdepth 1 -type f | awk -F/ '{print $5}'


