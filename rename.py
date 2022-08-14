
# Author: Pierce Brooks

import os
import sys
import shutil
import subprocess

characters = []
characters.append("keiichi")
characters.append("rena")
characters.append("mion")
characters.append("rika")
characters.append("hanyu")
characters.append("satoko")
characters.append("shion")
characters.append("akane")
characters.append("kasai")
characters.append("tomitake")
characters.append("takano")
characters.append("irie")
characters.append("ohishi")
characters.append("akasaka")
characters.append("chie")
characters.append("natumi")

for root, folders, files in os.walk(os.path.join(os.getcwd(), sys.argv[1])):
    base = str(os.path.basename(root)).strip()
    for character in characters:
        if ((base == character) or (base.startswith(character+"_"))):
            print(base)
            base = None
            break
    if not (base == None):
        continue
    for name in files:
        if not (name.lower().endswith(".glb")):
            continue
        path = os.path.join(root, name)
        print(path)
        shutil.copy(path, os.path.join(root, str(os.path.basename(root)).strip())+"_"+name[:name.index(".")]+".glb")
        os.unlink(path)

