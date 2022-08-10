
# Author: Pierce Brooks

import os
import sys
import subprocess

for root, folders, files in os.walk(os.path.join(os.getcwd(), sys.argv[1])):
    for name in files:
        if not (name.lower().endswith(".x")):
            continue
        path = os.path.join(root, name)
        if not (os.path.exists(path+".obj")):
            command = []
            command.append("assimp")
            command.append("export")
            command.append(path)
            command.append(path+".obj")
            print(str(command))
            try:
                result = subprocess.check_output(command).decode()
                print(result)
            except:
                sys.exit(0)
        os.unlink(path)

