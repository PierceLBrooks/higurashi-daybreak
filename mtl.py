
# Author: Pierce Brooks
# https://stackoverflow.com/questions/6729016/decoding-shift-jis-illegal-multibyte-sequence

import os
import sys
import shutil
import subprocess

renames = {}

for root, folders, files in os.walk(os.path.join(os.getcwd(), sys.argv[1])):
    for name in files:
        if not (name.lower().endswith(".obj")):
            continue
        path = os.path.join(root, name)
        print(path)
        descriptor = open(path, "r")
        lines = descriptor.readlines()
        descriptor.close()
        materials = []
        for line in lines:
            line = line.strip()
            if ((line.startswith("mtllib ")) and (line.endswith(".mtl"))):
                materials.append(os.path.join(root, line.replace("mtllib ", "").strip()))
                break
        for material in materials:
            print(material)
            if not (os.path.exists(material)):
                continue
            descriptor = open(material, encoding="cp932") # https://stackoverflow.com/a/55299163
            lines = descriptor.readlines()
            descriptor.close()
            content = []
            textures = []
            for line in lines:
                line = line.strip()
                if (line.endswith(".bmp")):
                    texture = None
                    parts = line.split(" ")
                    part = parts[len(parts)-1]
                    part = part[:(len(part)-4)]
                    convert = ""
                    for i in range(len(part)):
                        unit = hex(ord(part[i]))[2:]
                        index = 0
                        while (index < len(unit)):
                            convert += chr(int("0x"+unit[index:(index+2)], 16))
                            index += 2
                    part = bytearray()
                    part.extend(map(ord, convert))
                    for i in range(len(files)):
                        other = files[i]
                        if not (other.endswith(".tga")):
                            continue
                        other = other[:(len(other)-4)]
                        convert = ""
                        for j in range(len(other)):
                            unit = hex(ord(other[j]))[2:]
                            index = 0
                            while (index < len(unit)):
                                convert += chr(int("0x"+unit[index:(index+2)], 16))
                                index += 2
                        other = bytearray()
                        other.extend(map(ord, convert))
                        if (other == part):
                            texture = os.path.join(root, files[i])
                            shutil.copy(texture, os.path.join(root, "_".join(list(map(str, part)))+".tga"))
                            renames[texture] = os.path.join(root, "_".join(list(map(str, part)))+".tga")
                            break
                    if not (texture == None):
                        textures.append(texture)
                        content.append(" ".join(parts[:(len(parts)-1)]).strip()+" "+"_".join(list(map(str, part)))+".tga")
                        continue
                content.append(line)
            if not (len(textures) == 0):
                descriptor = open(material, "w")
                for line in content:
                    descriptor.write(line+"\n")
                descriptor.close()

for key in renames:
    os.unlink(key)

