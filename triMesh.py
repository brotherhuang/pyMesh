import sys
from meshIO import*
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
    def write(self,fileName):
        if fileName[-3:] == 'off':
            writeOFF(fileName,self.vertices, self.faces)
        elif fileName[-3:] == 'obj':
            writeOBJ(fileName,self.vertices,self.faces,self.normals)
        else: print("current not support the " + fileName[-3:] + " format")







