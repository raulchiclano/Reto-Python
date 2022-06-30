 #!/usr/bin/env python3
 # -*- coding: utf-8 -*- 

import os
import getpass
import re

payload = ("jpge", "JPGE", "jpg", "JPG", "PNG", "png")

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
                target = [file for file in ficheros if file.endswith(payload)]
                for index, file in enumerate(target):
                    if re.search(r'.*[0-9].*', file) is not None:
                        if index%2==0:
                            print(index, " =>", file.lower())
                        else:
                            print(index, file.lower())
                    else:
                        if index%2 == 0:
                            print(index, " =>", file.upper())
                        else:
                            print(index, file.upper())


if __name__ == "__main__":
  main()


