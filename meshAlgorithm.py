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
    nv = len(mesh.vertices)
    if nv == 0: return
    remap_table = [-1] * nv
    next = 0
    for i in range(nv):
        if toremove[i] :
            remap_table[i] = next
            next += 1
    if next == nv: return
    remap_verts(mesh,remap_table)

def remap_verts(mesh, remap_table):
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


def find_comps(mesh):
    def dfs(comps, neighbors, f, index):
        for i in neighbors[f]:
            if comps[i] == -1:
                comps[i] = index
                dfs(comps, neighbors,i, index)
    nf = len(mesh.faces)
    mesh.need_adjacentfaces()
    comps = [-1] * nf
    compsize = []
    for i in range(nf):
        if comps[i] == - 1:
            index = len(compsize)
            comps = index
            compsize.append[index]
            dfs(comps, mesh.adjacentfaces, i, index)
    for i in range(len(compsize)):
        compsize[i] = comps.count(i)








