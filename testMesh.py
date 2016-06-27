import sys
from triMesh import *
mesh0 = triMesh('Apple.off')
mesh0.need_normals()
mesh0.need_neighbors()
mesh0.need_adjacentfaces()
print(mesh0.normals[0])
