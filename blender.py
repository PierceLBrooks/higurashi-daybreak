
# Author: Pierce Brooks

import os
import sys
import platform
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
        if not (name.lower().endswith(".obj")):
            continue
        path = os.path.join(root, name).replace("\\", "/")
        if (os.path.exists(path+".glb")):
            continue
        print(path)
        command = []
        command.append(os.path.join(os.environ["BLENDER_HOME"], "blender"))
        command.append("-b")
        command.append("-P")
        command.append(os.path.join(os.getcwd(), "rignet.py"))
        command.append("--")
        command.append(path)
        if (platform.system().lower() == "windows"):
            command[0] += ".exe"
        print(str(command))
        try:
            result = subprocess.check_output(command).decode()
            print(result)
        except:
            pass
