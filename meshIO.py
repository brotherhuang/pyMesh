#this is for mesh IO
import sys
import readline
import numpy as np
from plyfile import (PlyData, PlyElement, make2d, PlyParseError, PlyProperty)

def readPLY(fileName):
    plydata = PlyData.read(fileName)
    verts = []
    faces = []
    for ele in plydata.elements:
        if ele.name == 'vertex':
            for v in plydata['vertex']:
                if len(v) == 3:
                    verts.append(np.asarray([v[0], v[1], v[2]]))
                else:
                    verts.append(np.asarray([v[0][0], v[0][1], v[0][2]]))
        if ele.name == 'face':
            for f in plydata['face']:
                if len(f) == 3:
                    faces.append(np.asarray([f[0], f[1], f[2]]))
                else:
                    faces.append(np.asarray([f[0][0], f[0][1], f[0][2]]))
    normals = []
    return verts, faces,normals

def writePLY(fileName,verts,faces = [],normals = [], color = []):
    with open(fileName, 'w') as f:
        f.write("ply\n")
        f.write("format ascii 1.0\n")
        f.write("element vertex  " + str(len(verts)) + "\n")
        f.write("property float x\n")
        f.write("property float y\n")
        f.write("property float z\n")
        f.write("element face  " + str(len(faces)) + "\n")
        f.write("property list uchar int vertex_indices\n")
        f.write("end_header\n")
        for v in verts:
            for i in v:
                f.write("%.4f " % i)
            f.write("\n")
        for p in faces:
            f.write(str(len(p)))
            for i in p:
                f.write(" %d" %  i)
            f.write("\n")

def readOFF(fileName):
    file = open(fileName.strip(), 'rt')
    if 'OFF' != file.readline().strip():
        print('Not a valid OFF header')
    firstLine = file.readline().strip().split(' ')
    nVerts = int(firstLine[0])
    nFaces = int(firstLine[1])
    verts = []
    for iVert in range(nVerts):
        verts.append(np.asarray([float(s) for s in file.readline().strip().split(' ')]))
    faces = []
    for iFace in range(nFaces):
        faces.append([int(float(s)) for s in file.readline().strip().split(' ')][1:])
    return verts, faces
def writeOFF(fineName, verts,faces):
    with open(fineName, 'w') as f:
        f.write("OFF\n")
        f.write("%d %d 0\n" % (len(verts) , len(faces)))
        for v in verts:
            for i in v:
                f.write("%.4f " % i)
            f.write("\n")
        for p in faces:
            f.write("%d " % len(p))
            for i in p:
                f.write(" %d" % i)
            f.write("\n")
def readOBJ(fileName):
    verts = []
    faces = []
    normals = []
    for line in open(fileName, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'v':
            v = map(float, values[1:4])
            verts.append(np.asarray(v))
        elif values[0] == 'vn':
            n = map(float,values[1:4])
            normals.append(np.asarray(n))
        elif values[0] == 'vt': continue
        elif values[0] in ('usemtl', 'usemat'): continue
        elif values[0] == 'mtllib': continue
        elif values[0] == 'f':
            f = []
            n = []
            for v in values[1:]:
                w = v.split('/')
                f.append(int(w[0]) - 1)
            faces.append(f)
    return verts, faces,normals

def writeOBJ(fileName,verts,faces,normals):
    with open(fileName, 'w') as f:
        f.write("# OBJ file\n")
        for v in verts:
            f.write("v ")
            for i in v:
                f.write("%.4f " % i)
            f.write("\n")
        for vn in normals:
            f.write("vn ")
            for i in vn:
                f.write("%.4f " % i)
            f.write("\n")
        for p in faces:
            f.write("f")
            for i in p:
                f.write(" %d" % (i + 1))
            f.write("\n")


