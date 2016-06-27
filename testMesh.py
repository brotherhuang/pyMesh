import sys
from triMesh import *
mesh0 = triMesh('Apple.off')
mesh0.need_normals()
print(mesh0.normals[0])
