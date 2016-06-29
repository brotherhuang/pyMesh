import sys
import numpy as np
import math
from numpy import linalg as LA
from meshIO import*
class triMesh:
    def __init__(self, fileName):
        self.vertices = []
        self.normals = []
        self.faces = []
        self.neighbors = []
        self.adjacentfaces =[]
        self.across_edge = []
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

    def need_normals(self):
        if len(self.normals) == 0:
            for v in self.vertices:
                self.normals.append(np.array([0.0,0.0,0.0]))
            for f in self.faces:
                v0 = self.vertices[f[0]]
                v1 = self.vertices[f[1]]
                v2 = self.vertices[f[2]]
                a = v0 - v1
                b = v1 - v2
                c = v2 - v0
                la = LA.norm(a)
                lb = LA.norm(b)
                lc = LA.norm(c)
                if  la == 0 or lb == 0 or lc == 0 : continue
                facenormal = np.cross(a, b)
                self.normals[f[0]] += facenormal * (1.0 / (la * lc))
                self.normals[f[1]] += facenormal * (1.0 / (lb * la))
                self.normals[f[2]] += facenormal * (1.0 / (lc * lb))
            for i in range(len(self.normals)):
                self.normals[i] = self.normals[i] / LA.norm(self.normals[i])

    def need_neighbors(self):
        if len(self.neighbors) == 0:
            self.neighbors = [[] for x in xrange(len(self.vertices))]
            for f in self.faces:
                v0 = f[0]
                v1 = f[1]
                v2 = f[2]
                if self.neighbors[v0].count(v1) == 0: self.neighbors[v0].append(v1)
                if self.neighbors[v0].count(v2) == 0: self.neighbors[v0].append(v2)
                if self.neighbors[v1].count(v0) == 0: self.neighbors[v1].append(v0)
                if self.neighbors[v1].count(v2) == 0: self.neighbors[v1].append(v2)
                if self.neighbors[v2].count(v0) == 0: self.neighbors[v2].append(v0)
                if self.neighbors[v2].count(v1) == 0: self.neighbors[v2].append(v1)

    def need_adjacentfaces(self):
        if len(self.adjacentfaces) == 0 :
            self.adjacentfaces = [[] for x in xrange(len(self.vertices))]
            for i in range(len(self.faces)):
                v0 = self.faces[i][0]
                v1 = self.faces[i][1]
                v2 = self.faces[i][2]
                self.adjacentfaces[v0].append(i)
                self.adjacentfaces[v1].append(i)
                self.adjacentfaces[v2].append(i)

    def need_across_edge(self):
        if len(self.across_edge) == 0:
            self.need_adjacentfaces()
            self.across_edge = [[-1,-1,-1] for x in xrange(len(self.faces))]
            for f in range(len(self.faces)):
                for i in range(3):
                    if self.across_edge[f][i] != -1: continue
                    v1 = self.faces[f][(i + 1) % 3]
                    v2 = self.faces[f][(i + 2) % 3]
                    comomFace = list(set(self.adjacentfaces[v1]).intersection(set(self.adjacentfaces[v2])))
                    for ff in comomFace:
                        if ff != f : self.across_edge[f][i] = ff

    def is_bdy(self,v):
        if len(self.neighbors) == 0 : self.need_neighbors()
        if len(self.adjacentfaces) == 0: self.need_adjacentfaces()
        if len(self.neighbors[v]) != len(self.adjacentfaces[v]): return True
        else : return False

    def centroid(self, f):
        v0 = self.vertices[self.faces[f][0]]
        v1 = self.vertices[self.faces[f][1]]
        v2 = self.vertices[self.faces[f][2]]
        return (v0 + v1 + v2)/3.0

    def trinorm(self,f):
        v0 = self.vertices[self.faces[f][0]]
        v1 = self.vertices[self.faces[f][1]]
        v2 = self.vertices[self.faces[f][2]]
        return 0.5 * np.cross(v1-v0, v2-v0)

    def cornerangle(self,f,v):
        v0 = self.vertices[self.faces[f][v]]
        v1 = self.vertices[self.faces[f][(v + 1) % 3]]
        v2 = self.vertices[self.faces[f][(v + 2) % 3]]
        return math.acos(np.dot(v1 - v0), (v2 - v0))
    



















