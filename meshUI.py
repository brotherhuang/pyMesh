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
    glDisable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    # paint planes
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)
    glPushMatrix()
    for f in mesh0.faces:
        glBegin(GL_TRIANGLES)
        glColor3f(0.6,0.6,0.6)
        glVertex3f(mesh0.vertices[f[0]][0], mesh0.vertices[f[0]][1], mesh0.vertices[f[0]][2])
        glVertex3f(mesh0.vertices[f[1]][0], mesh0.vertices[f[1]][1], mesh0.vertices[f[1]][2])
        glVertex3f(mesh0.vertices[f[2]][0], mesh0.vertices[f[2]][1], mesh0.vertices[f[2]][2])
        glEnd()
    glPopMatrix()
    glEnable(GL_LIGHTING);
    glutSwapBuffers()
    return

def main(argv):
        mesh0.read(argv[0])
	glutInit(['triMesh'])
	glutInitWindowPosition(112, 84)
	glutInitWindowSize(800, 600)
	# use multisampling if available
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
	wintitle = "triMesh"
	glutCreateWindow(wintitle)
	glutDisplayFunc(draw)
	#glutKeyboardFunc(keyboard)
	#glutVisibilityFunc(visible)
	#
	# This program fails if PyOpenGL-3.0.0b1-py2.5.egg\OpenGL\GLUT\special.py
	# is not corrected at line 158 to read :
	# callbackType = ctypes.CFUNCTYPE( None, ctypes.c_int )
	# instead of :
	# callbackType = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_int )
	#
	# RIGHT-CLICK to display the menu
	#
	#glutCreateMenu(dmenu)
	#glutAddMenuEntry("Add plane", ADD_PLANE)
	#glutAddMenuEntry("Remove plane", REMOVE_PLANE)
	#glutAddMenuEntry("Motion", MOTION_ON)
	#glutAddMenuEntry("Quit", QUIT)
	#glutAttachMenu(GLUT_RIGHT_BUTTON)

	# setup OpenGL state
	glClearDepth(1.0)
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 30)
	glMatrixMode(GL_MODELVIEW)
	# add three initial random planes
	#add_plane()
	#add_plane()
	#add_plane()
	# start event processing */
	#print 'RIGHT-CLICK to display the menu.'
	glutMainLoop()


if __name__ == "__main__":
   main(sys.argv[1:])





