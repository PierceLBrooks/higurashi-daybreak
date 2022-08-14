
# Author: Pierce Brooks

import os
import sys
import bpy
import brignet as bn

arguments = sys.argv[(sys.argv.index("--")+1):]
print(arguments)

bpy.ops.object.select_all(action="DESELECT")
bpy.ops.object.select_by_type(type="MESH")
bpy.ops.object.delete()
bpy.ops.import_scene.obj(filepath=arguments[0])
bpy.ops.object.select_all(action="DESELECT")
bpy.ops.object.select_by_type(type="MESH")
for name in bpy.context.selected_objects:
    print(str(name.name))
bn.brignet.predict()
bpy.ops.export_scene.gltf(filepath=arguments[0]+".glb")
bpy.ops.wm.quit_blender()
