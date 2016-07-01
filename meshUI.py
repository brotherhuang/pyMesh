#this is for UI like rendering and selection
import sys
from triMesh import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
from random import random, choice, randint, getrandbits
M_PI   = pi
M_PI_2 = pi / 2.0
mesh0 = triMesh()
def draw():
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    for f in mesh0.faces:
        glBegin(GL_TRIANGLES)
        glColor3f(0.6,0.6,0.6)
        glNormal3f(mesh0.normals[f[0]][0], mesh0.normals[f[0]][1], mesh0.normals[f[0]][2])
        glVertex3f(mesh0.vertices[f[0]][0], mesh0.vertices[f[0]][1], mesh0.vertices[f[0]][2])
        glNormal3f(mesh0.normals[f[1]][0], mesh0.normals[f[1]][1], mesh0.normals[f[1]][2])
        glVertex3f(mesh0.vertices[f[1]][0], mesh0.vertices[f[1]][1], mesh0.vertices[f[1]][2])
        glNormal3f(mesh0.normals[f[2]][0], mesh0.normals[f[2]][1], mesh0.normals[f[2]][2])
        glVertex3f(mesh0.vertices[f[2]][0], mesh0.vertices[f[2]][1], mesh0.vertices[f[2]][2])
        glEnd()
    glPopMatrix()
    glEnable(GL_LIGHTING);
    glutSwapBuffers()
    return

def setDefaultLight():
    pos0 = [-3.0, 3.0, 3.0, 0.0]
    col0 = [1.0,  1.0,  1.0, 1.0]
    pos1 = [3.0,  3.0,  3.0, 0.0]
    col1 = [1.0,  1.0,  1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, pos0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, col0)
    glLightfv(GL_LIGHT0, GL_SPECULAR, col0)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT1, GL_POSITION, pos1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, col1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, col1)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHTING)

def setDefaultMaterial():
    mat_diffuse = [0.5, 0.5, 0.5, 1.0]
    mat_specular = [0.5, 0.5, 0.5, 1.0]
    mat_shininess = [0.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, mat_diffuse)

def drawBackground():
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glPushAttrib(GL_ENABLE_BIT)
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING)
    glDisable(GL_TEXTURE_2D)

    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-1, 1)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-1, -1)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(1, 1)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(1, -1)
    glEnd()

    glPopAttrib()
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def main(argv):
    mesh0.read(argv[0])
    mesh0.need_normals()
    glutInit(['triMesh'])
    glutInitWindowPosition(112, 84)
    glutInitWindowSize(800, 600)
    # use multisampling if available
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
    wintitle = "triMesh"
    glutCreateWindow(wintitle)
    glutDisplayFunc(draw)
    #glutKeyboardFunc(keyboard)
    #  setup OpenGL state
    glClearDepth(1.0)
    glClearColor(0.5,0.5, 0.5, 0.0)
    glShadeModel(GL_SMOOTH)
    setDefaultLight()
    setDefaultMaterial()
    glEnable(GL_DEPTH_TEST)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    drawBackground()
    glutMainLoop()

if __name__ == "__main__":
   main(sys.argv[1:])





