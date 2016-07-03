#this is for UI like rendering and selection
import sys
from triMesh import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import copy
from math import cos, sin

from ArcBall import * 				# ArcBallT and this tutorials set of points/vectors/matrix types

PI2 = 2.0*3.1415926535			# 2 * PI (not squared!) 		// PI Squared

# *********************** Globals ***********************
# Python 2.2 defines these directly
try:
	True
except NameError:
	True = 1==1
	False = 1==0

g_Transform = Matrix4fT ()
g_LastRot = Matrix3fT ()
g_ThisRot = Matrix3fT ()

g_ArcBall = ArcBallT (640, 480)
g_isDragging = False
g_quadratic = None
ESCAPE = '\033'

mesh0 = triMesh()

def Upon_Drag (cursor_x, cursor_y):
	""" Mouse cursor is moving
		Glut calls this function (when mouse button is down)
		and pases the mouse cursor postion in window coords as the mouse moves.
	"""
	global g_isDragging, g_LastRot, g_Transform, g_ThisRot

	if (g_isDragging):
		mouse_pt = Point2fT (cursor_x, cursor_y)
		ThisQuat = g_ArcBall.drag (mouse_pt)						# // Update End Vector And Get Rotation As Quaternion
		g_ThisRot = Matrix3fSetRotationFromQuat4f (ThisQuat)		# // Convert Quaternion Into Matrix3fT
		# Use correct Linear Algebra matrix multiplication C = A * B
		g_ThisRot = Matrix3fMulMatrix3f (g_LastRot, g_ThisRot)		# // Accumulate Last Rotation Into This One
		g_Transform = Matrix4fSetRotationFromMatrix3f (g_Transform, g_ThisRot)	# // Set Our Final Transform's Rotation From This One
	return

def Upon_Click (button, button_state, cursor_x, cursor_y):
	""" Mouse button clicked.
		Glut calls this function when a mouse button is
		clicked or released.
	"""
	global g_isDragging, g_LastRot, g_Transform, g_ThisRot

	g_isDragging = False
	if (button == GLUT_RIGHT_BUTTON and button_state == GLUT_UP):
		# Right button click
		g_LastRot = Matrix3fSetIdentity ();							# // Reset Rotation
		g_ThisRot = Matrix3fSetIdentity ();							# // Reset Rotation
		g_Transform = Matrix4fSetRotationFromMatrix3f (g_Transform, g_ThisRot);	# // Reset Rotation
	elif (button == GLUT_LEFT_BUTTON and button_state == GLUT_UP):
		# Left button released
		g_LastRot = copy.copy (g_ThisRot);							# // Set Last Static Rotation To Last Dynamic One
	elif (button == GLUT_LEFT_BUTTON and button_state == GLUT_DOWN):
		# Left button clicked down
		g_LastRot = copy.copy (g_ThisRot);							# // Set Last Static Rotation To Last Dynamic One
		g_isDragging = True											# // Prepare For Dragging
		mouse_pt = Point2fT (cursor_x, cursor_y)
		g_ArcBall.click (mouse_pt);								# // Update Start Vector And Prepare For Dragging

	return



def keyPressed(*args):
	global g_quadratic
	# If escape is pressed, kill everything.
	key = args [0]
	if key == ESCAPE:
		gluDeleteQuadric (g_quadratic)
		sys.exit ()


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glMultMatrixf(g_Transform);
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
    glFlush();
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
    global g_quadratic
    g_quadratic = gluNewQuadric()
    gluQuadricNormals(g_quadratic, GLU_SMOOTH)
    gluQuadricDrawStyle(g_quadratic, GLU_FILL)
    mesh0.read(argv[0])
    mesh0.need_normals()
    glutInit(['triMesh'])
    glutInitWindowPosition(112, 84)
    glutInitWindowSize(640, 480)
    # use multisampling if available
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
    wintitle = "triMesh"
    glutCreateWindow(wintitle)
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
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
    glutKeyboardFunc(keyPressed)
    glutMouseFunc(Upon_Click)
    glutMotionFunc(Upon_Drag)
    drawBackground()
    glutMainLoop()

if __name__ == "__main__":
   main(sys.argv[1:])





