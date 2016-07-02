import sys
from triMesh import *
from meshUI import *
mesh0 = triMesh('281.obj')
mesh0.need_normals()
mesh0.need_neighbors()
mesh0.need_adjacentfaces()
mesh0.need_edges()
mesh0.need_edge_face();
print(mesh0.is_bdy(0))
print(mesh0.normals[0])
print(mesh0.normals[15])
print(mesh0.neighbors[0])
for i in range(len(mesh0.edges_faces)):
    print mesh0.edges_faces[i]
    print "\n"