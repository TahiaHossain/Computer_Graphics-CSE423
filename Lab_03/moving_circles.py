from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
RADIUS = 50

paused = False
circles = []
grow_speed = 0.1

def animate(v):
    global paused, circles, grow_speed

    if not paused:
        for i in range(len(circles)):
            if i < len(circles):
                radius, x, y, color = circles[i]
                radius += grow_speed
                if (x - radius <= 0 or x + radius >= SCREEN_WIDTH or y - radius <= 0 or y + radius >= SCREEN_HEIGHT):
                    circles.pop(i)
                    continue
                circles[i] = (radius, x, y, color)
    
    glutPostRedisplay()
    glutTimerFunc(10, animate, 0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    for radius, x, y, color in circles:
        midPointCircleAlgorithm(radius, x, y, color)
    
    glutSwapBuffers()

def handle_mouse(button, state, x, y):
    global paused, circles
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and not paused:
        color = (random.random(), random.random(), random.random())
        circles.append((RADIUS,x, SCREEN_HEIGHT - y, color))

def handleSpecialKeyboard(key, x, y):
    global grow_speed, paused
    if key == GLUT_KEY_LEFT and not paused:
        print("Speed is increased")
        grow_speed += 0.3

    elif key == GLUT_KEY_RIGHT and not paused:
        print("Speed is decreased")
        grow_speed -= 0.3
        if grow_speed < 0: 
            grow_speed = 0

def handleKeyboard(key, x, y):
    global paused
    if key == b' ':
        paused = not paused

def draw_points(x, y, color = (1, 1, 1), size=2):
    glColor3fv(color)
    glPointSize(size) 
    glBegin(GL_POINTS)
    glVertex2f(x,y) 
    glEnd()

def convert_zone(x,y,zone):
    if zone==0: return x,y
    if zone==1: return y,x
    if zone==2: return -y,x
    if zone==3: return -x,y
    if zone==4: return -x,-y
    if zone==5: return -y,-x
    if zone==6: return y,-x
    if zone==7: return x,-y

def midPointCircleAlgorithm(radius, center_x, center_y, color):
    # Initial d
    d = 1 - radius
    x = 0
    y = radius

    while x < y:
        for i in range(8):
            x_, y_ = convert_zone(x, y, i)
            draw_points(x_ + center_x, y_ + center_y, color, 4)
        
        if d < 0:
            # IF EAST
            d += 2*x + 3
            x += 1
        else:
            # IF SOUTH
            d += 2*x - 2*y + 5
            x += 1
            y -= 1

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
glutCreateWindow(b"Pop the Circles")

# Initialize OpenGL
glClearColor(0.0, 0.0, 0.0, 1.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, -1, 1)
glMatrixMode(GL_MODELVIEW)

# Register callback functions
glutDisplayFunc(display)
glutTimerFunc(10, animate, 0)
glutSpecialFunc(handleSpecialKeyboard)
glutKeyboardFunc(handleKeyboard)
glutMouseFunc(handle_mouse)

glutMainLoop()