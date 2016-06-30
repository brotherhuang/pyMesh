import sys
from triMesh import *
from meshUI import *
mesh0 = triMesh('car061_low.obj')
mesh0.need_normals()
mesh0.need_neighbors()
mesh0.need_adjacentfaces()
print(mesh0.is_bdy(0))
print(mesh0.normals[0])
print(mesh0.normals[15])
print(mesh0.neighbors[0])
