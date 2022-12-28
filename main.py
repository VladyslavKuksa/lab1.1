from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def build_projection():

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,10, 0.,0.,0., 0.,1.,0.)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10,10, -10,10, 1,30)

    glViewport(0,0,500,500)

def set_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLight(GL_LIGHT0, GL_POSITION, (10, 10, -10, 0))
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_COLOR_MATERIAL)

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    build_projection()
    set_lighting()

    glColor3f(.5,.9,.1)
    glutWireCone(9, 9, 100,  100)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
glutCreateWindow("Window")

glutDisplayFunc(draw_scene)

glutMainLoop()

