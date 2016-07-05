import sys
from triMesh import *
from meshAlgorithm import *
mesh0 = triMesh('281.obj')
print "need_normals"
mesh0.need_normals()
print "need_neighbors"
mesh0.need_neighbors()
print "need_adjacentfaces"
mesh0.need_adjacentfaces()
print "need_edges"
#mesh0.need_edges()
print "need_edge_face"
#mesh0.need_edge_face();
print(mesh0.is_bdy(0))
print(mesh0.normals[0])
print(mesh0.normals[15])
print(mesh0.neighbors[0])
print(mesh0.vertices[0])
print "lmsmooth"
lmsmooth(mesh0,50)
print(mesh0.vertices[0])
mesh0.write("apple_def.off")
