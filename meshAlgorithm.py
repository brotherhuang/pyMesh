#this is for some 3D geomerty  mesh processing
from triMesh import *

#Optimally re-triangulate a mesh by doing edge flips
def edgeflip(mesh):
    return

def faceflip(mesh):
    for i in range(len(mesh.faces)):
        mesh.faces[i][0], mesh.faces[i][2] = mesh.faces[i][2], mesh.faces[i][0]

def umbrella(mesh,stepSize, tangent):
    mesh.need_neighbors()
    mesh.need_adjacentfaces()
    if tangent == True:
        mesh.need_normals()
    disp = [np.array([0.0, 0.0,0.0]) for x in xrange(len(mesh.vertices))]
    for i in range(len(mesh.vertices)):
        if mesh.is_bdy(i) : continue
        nn = len(mesh.neighbors[i])
        for j in range(nn):
            disp[i] += mesh.vertices[mesh.neighbors[i][j]]
        disp[i] /= nn
        disp[i] -= mesh.vertices[i]
    if tangent == True:
        for i in range(len(mesh.vertices)):
            norm = mesh.normals[i]
            mesh.vertices[i] += stepSize * (disp[i] - norm * (np.dot(disp[i], norm)))
    else:
        for i in range(len(mesh.vertices)):
            mesh.vertices[i] += stepSize * disp[i]
def lmsmooth(mesh, iterations):
    mesh.need_neighbors()
    mesh.need_adjacentfaces()
    for i in range(iterations):
        umbrella(mesh,0.330, False)
        umbrella(mesh,-0.331,False)

def remove_vertices(mesh, toremove):
    return

def remove_faces(mesh, toremove):
    return

def remove_sliver_faces(mesh):
    return

def remap_verts(mesh, remap_table):
    return


def diffuse_vector(mesh, field, sigma):
    return

def diffuse_normals(mesh, sigma):
    return




