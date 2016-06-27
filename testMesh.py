import sys
from triMesh import *
mesh0 = triMesh('Apple.off')
mesh0.write('AppleOut.off');
print(len(mesh0.vertices))
print(len(mesh0.faces))
print(len(mesh0.normals))
mesh1 = triMesh('281.obj')
mesh1.write('281out.obj');
print(len(mesh1.vertices))
print(len(mesh1.faces))
print(len(mesh1.normals))
mesh2 = triMesh('281.txt')
print(len(mesh2.vertices))
print(len(mesh2.faces))
print(len(mesh2.normals))

