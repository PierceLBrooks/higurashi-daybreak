
# Author: Pierce Brooks

import os
import sys

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
        path = os.path.join(root, name)
        print(path)
        descriptor = open(path, "r")
        lines = descriptor.readlines()
        descriptor.close()
        size = []
        content = []
        minimum = []
        maximum = []
        for i in range(3):
            minimum.append(float("inf"))
            maximum.append(float("-inf"))
        for line in lines:
            line = line.strip()
            if not (line.startswith("v ")):
                continue
            line = line[2:].strip().split(" ")
            for i in range(3):
                minimum[i] = min(minimum[i], float(line[i]))
                maximum[i] = max(maximum[i], float(line[i]))
        for i in range(3):
            size.append(abs(maximum[i]-minimum[i]))
        size = max(size[0], max(size[1], size[2]))
        for line in lines:
            line = line.strip()
            if not (line.startswith("v ")):
                content.append(line)
                continue
            line = line[2:].strip().split(" ")
            for i in range(3):
                line[i] = float(line[i])/size
            content.append("v "+" ".join(list(map(str, line))))
        descriptor = open(path, "w")
        for line in content:
            descriptor.write(line+"\n")
        descriptor.close()

