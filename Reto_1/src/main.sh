#!/bin/bash

user=$(whoami)
dir=$(ls ~/ | grep -e Descargas -e descargas -e downloads -e Downloads )

echo -e "Directorio: "/home"/$user/$dir","\n",$(ls -p ~/$dir | grep -v /) | tr ' ' '\n'