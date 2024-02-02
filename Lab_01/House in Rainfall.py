from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 

raindrops = []
night = False 
rain_direction = 0
screen_color = 1

for i in range(100): 
    x = random.randint(0, 500)
    y = random.randint(500, 800)
    raindrops.append((x,y))
    
def rain():
    global raindrops, rain_direction
    speed=5
    for x,y in raindrops:
        new_y = y - speed  # animation
        if new_y < 255:
            new_y = 500  # upor thk niche

        index = raindrops.index((x,y))  # raindrop er coordinate update hobe
        raindrops[index] = (x,new_y)
    glutPostRedisplay()

def show_raindrops():
    global raindrops
    for x,y in raindrops:
        glLineWidth(2)
        glBegin(GL_LINES)
        glColor3f(0.0, 0.0, 1.0)
        x1, y1 = x, y
        y2 = y - 10
        glVertex2f(x1, y1)
        glVertex2f(x1+rain_direction, y2)
        glEnd()
# -------------------------------------------------------------------------------------

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_lines(x1, y1, x2, y2, w):
    # glPointSize(5) #pixel size. by default 1 thake
    glLineWidth(w)
    glBegin(GL_LINES)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    glVertex2f(x2,y2)
    glEnd()

def draw_triangles(x1, y1, x2, y2, x3, y3):
    glPointSize(5) #pixel size. by default 1 thake
    glColor3f(1.0,0.6,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1) #jekhane show korbe pixel
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# -------------------------------------------------------------------------------------

def draw_house():
    draw_roof(100,250,  400,250,  250,350,  w=15)
    draw_base()

def draw_roof(x1,y1,x2,y2,x3,y3,w):
    draw_lines(x1,y1,x2,y2,w)
    draw_lines(x2,y2,x3,y3,w)
    draw_lines(x3,y3,x1,y1,w)

def draw_base():
    draw_basement(150, 250, 145, 100, 355, 100, 350, 250,w=10)
    draw_door(180,100, 180,180,  230,180,  230,100, w=5)
    draw_window(280,185,280,225,320,225,320,185,w=3)

def draw_basement(x1,y1,x2,y2,x3,y3,x4,y4,w):
    draw_lines(x1,y1,x2,y2,w) 
    draw_lines(x2-20,y2,x3+20,y3,w)
    draw_lines(x3,y3,x4,y4,w)
    draw_lines(x4,y4,x1,y1,w)

def draw_door(x1,y1,x2,y2,x3,y3,x4,y4,w):
    draw_lines(x1,y1,x2,y2+3,w) 
    draw_lines(x2,y2,x3,y3,w)
    draw_lines(x3,y3+3,x4,y4,w)
    draw_lines(x4,y4,x1,y1,w)
    # door knob
    draw_points(215, 140)

def draw_window(x1,y1,x2,y2,x3,y3,x4,y4,w):
    draw_lines(x1,y1-5,x2,y2+5,w) 
    draw_lines(x2-5,y2,x3+5,y3,w)
    draw_lines(x3,y3+5,x4,y4-5,w)
    draw_lines(x4+5,y4,x1-5,y1,w)
    # window railing
    draw_lines(280,195, 320,195, w=2)
    draw_lines(280,215, 320,215, w=2)
    draw_lines(300,225, 300,185, w=2)
    draw_lines(290,225, 290,185, w=2)
    draw_lines(310,225, 310,185, w=2)

# -------------------------------------------------------------------------------------

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
# ------------------------------------------
    global screen_color
    
    glClearColor(screen_color,screen_color,screen_color,screen_color)  # Day Night
    glClear(GL_COLOR_BUFFER_BIT)
    iterate()

    show_raindrops() 
# ------------------------------------------
    glColor3f(0.5, 0.0, 0.0) #konokichur color set (RGB)

    #call the draw methods here
    draw_house()
    draw_triangles(115,255,  385,255,  250,343) # house roof aesthetics
    glutSwapBuffers()

# -------------------------------------------------------------------------------------

def key_pressed(key, x, y):
    global night,screen_color
    if key == b'n':
        night = True
        screen_color -= 0.1
    elif key == b"d":
        night = False    
        screen_color += 0.1
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global rain_direction
    if key == GLUT_KEY_LEFT :
        rain_direction -= 1
        
    elif key == GLUT_KEY_RIGHT :
        rain_direction += 1
        
    glutPostRedisplay()

def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,1,1,1000.0)

# -------------------------------------------------------------------------------------

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Task 1") #window name
glutDisplayFunc(showScreen)

glutIdleFunc(rain)
glutKeyboardFunc(key_pressed) 
glutSpecialFunc(specialKeyListener)

glutMainLoop()