import sys
import readline
def readOFF(fileName):
    file = open(fileName.strip(), 'rt')
    if 'OFF' != file.readline().strip():
        print('Not a valid OFF header')
    firstLine = file.readline().strip().split(' ')
    nVerts = int(firstLine[0])
    nFaces = int(firstLine[1])
    verts = []
    for iVert in range(nVerts):
        verts.append([float(s) for s in file.readline().strip().split(' ')])
    faces = []
    for iFace in range(nFaces):
        faces.append([int(float(s)) for s in file.readline().strip().split(' ')][1:])
    return verts, faces
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
            verts.append(v)
        elif values[0] == 'vn':
            n = map(float,values[1:4])
            normals.append(n)
        elif values[0] == 'vt': continue
        elif values[0] in ('usemtl', 'usemat'): continue
        elif values[0] == 'mtllib': continue
        elif values[0] == 'f':
            f = []
            n = []
            for v in values[1:]:
                w = v.split('/')
                f.append(int(w[0]))
            faces.append(f);
    return verts, faces,normals

class triMesh:
    def __init__(self, fileName):
        self.vertices = []
        self.normals = []
        self.faces = []
        if fileName[-3:] == 'off':
            [self.vertices,self.faces] = readOFF(fileName)
        elif fileName[-3:] == 'obj':
            [self.vertices, self.faces,self.normals] = readOBJ(fileName)
        else : print("current not support the " + fileName[-3:] + " format")




