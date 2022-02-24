#!/usr/bin/env python3

import os
import getpass


def main():
    user = getpass.getuser()
    directory = "/home/"+user+"/"
    
    
    target = ["Descargas", "descargas", "downloads", "Downloads"]

    with os.scandir(directory) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_dir()]

    for name in target:
        if name in ficheros:
            download_directory = "/home/"+user+"/"+name
            with os.scandir(download_directory) as ficheros:
                ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
                print("[+] Directorio: "+download_directory+"\n")
                for f in ficheros:
                    print("    > ",f)

if __name__ == "__main__":
  main()