import sys
import readline
import numpy as np
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

def writeOBJ(fineName,verts,faces,normals):
    with open(fineName, 'w') as f:
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


