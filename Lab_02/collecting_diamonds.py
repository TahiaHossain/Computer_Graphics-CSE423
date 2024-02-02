from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
from math import cos, sin, radians

DIAMOND_COLORS = [
    (1.0, 0.0, 0.0),  # Red
    (0.0, 1.0, 0.0),  # Green
    (0.0, 0.0, 1.0),  # Blue
    (1.0, 1.0, 0.0),  # Yellow
    (1.0, 0.0, 1.0),  # Purple
]

falling_diamond = None

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DIAMOND_SIZE = 20
BAR_WIDTH = 100
BAR_HEIGHT = 50
DIAMOND_FALL_SPEED = 2
NUM_DIAMONDS = 10
RESTART_KEY = b"r"  # Key to restart the game
RESTART_BUTTON_LOCATION = (20, SCREEN_HEIGHT - 50)
PAUSE_BUTTON_LOCATION = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 50)
CROSS_BUTTON_LOCATION = (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50)

# Colors
WHITE = (1.0, 1.0, 1.0)
RED = (1.0, 0.0, 0.0)
TEAL = (0.0, 1.0, 1.0)
AMBER = (1.0, 0.75, 0.0)

# Initialize game variables
score = 0
diamonds = []
falling_diamond = None
game_over = False
BAR_COLOR = WHITE
current_fall_speed = DIAMOND_FALL_SPEED
lives = 1
paused = False
exit_game = False

# Initialize OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, -1, 1)
    glMatrixMode(GL_MODELVIEW)

# Rendering function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw the bar
    draw_bar()

    # Draw the currently falling diamond with a randomized color stroke
    if falling_diamond:
        x, y, color = falling_diamond
        draw_diamond(x, y, color)

    # Draw the score on the screen
    draw_text(10, 10, f"Score: {score}", WHITE)

    # Draw lives
    draw_text(10, 30, f"Lives: {lives}", WHITE)

    # Check if the game is over
    if game_over:
        draw_text(300, 300, "Game Over", WHITE)
        draw_text(300, 280, "Press 'R' to restart", WHITE)

    draw_restart_button(RESTART_BUTTON_LOCATION[0], RESTART_BUTTON_LOCATION[1])
    
    if not paused:
        draw_pause_button(PAUSE_BUTTON_LOCATION[0], PAUSE_BUTTON_LOCATION[1])
    else:
        draw_play_button(PAUSE_BUTTON_LOCATION[0], PAUSE_BUTTON_LOCATION[1])

    draw_cross(CROSS_BUTTON_LOCATION[0], CROSS_BUTTON_LOCATION[1])
    
    glutSwapBuffers()

# Button drawing functions
def draw_restart_button(x, y):
    color = TEAL
    mid_line(x, y, x + 20, y - 20, color)
    mid_line(x, y, x + 20, y + 20, color)
    mid_line(x, y, x + 50, y, color)

def draw_pause_button(x, y):
    color = AMBER
    mid_line(x + 10, y + 20, x + 10, y - 20, color)
    mid_line(x - 10, y + 20, x - 10, y - 20, color)

def draw_play_button(x, y):
    color = AMBER
    mid_line(x - 10, y + 20, x - 10, y - 20, color)
    mid_line(x - 10, y + 20, x + 10, y, color)
    mid_line(x - 10, y - 20, x + 10, y, color)

def draw_cross(x, y):
    color = RED
    mid_line(x - 10, y + 10, x + 10, y - 10, color)
    mid_line(x - 10, y - 10, x + 10, y + 10, color)

def handle_mouse_click(button, state, x, y):
    global paused, exit_game
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if x >= RESTART_BUTTON_LOCATION[0] and x <= RESTART_BUTTON_LOCATION[0] + 50:
            y = SCREEN_HEIGHT - y
            if y >= (RESTART_BUTTON_LOCATION[1] - 20)  and y <= (RESTART_BUTTON_LOCATION[1] + 20):
                handle_restart()

        elif x >= PAUSE_BUTTON_LOCATION[0] - 10 and x <= PAUSE_BUTTON_LOCATION[0] + 10:
            y = SCREEN_HEIGHT - y
            if y >= (PAUSE_BUTTON_LOCATION[1] - 20)  and y <= (PAUSE_BUTTON_LOCATION[1] + 20):
                paused = not paused
        
        elif x >= CROSS_BUTTON_LOCATION[0] - 10 and x <= CROSS_BUTTON_LOCATION[0] + 10:
            y = SCREEN_HEIGHT - y
            if y >= (CROSS_BUTTON_LOCATION[1] - 10)  and y <= (CROSS_BUTTON_LOCATION[1] + 10):
                exit_game = True

# Draw a diamond at the specified position with a colored stroke
def draw_diamond(x, y, color):
    glColor3fv(color)

    glLineWidth(2.0)  # Set the line width for the stroke

    # Define the vertices of the smaller diamond
    size = DIAMOND_SIZE * 0.4  # Adjust the size to make it smaller
    vertices = [
        (x, y - size * 2),
        (x - size, y),
        (x, y + size * 2),
        (x + size, y),
        (x, y - size * 2),
    ]

    glBegin(GL_LINES)

    for i in range(len(vertices) - 1):
        glVertex2f(vertices[i][0], vertices[i][1])
        glVertex2f(vertices[i + 1][0], vertices[i + 1][1])

    glEnd()

    glLineWidth(1.0)  # Reset the line width to the default value


# Draw the bar at the current position
def draw_bar():
    global BAR_COLOR
    x1 = bar_x - BAR_WIDTH / 2
    x2 = bar_x + BAR_WIDTH / 2
    lower_x1, lower_x2 = x1 + 20, x2 - 20
    lower_y = BAR_HEIGHT - 20
    y = BAR_HEIGHT
    
    mid_line(x1, y, x2, y, BAR_COLOR)
    mid_line(lower_x1, lower_y, lower_x2, lower_y, BAR_COLOR)
    mid_line(x1, y, lower_x1, lower_y, BAR_COLOR)
    mid_line(x2, y, lower_x2, lower_y, BAR_COLOR)


# Draw text on the screen at the specified position
def draw_text(x, y, text, color):
    glColor3fv(color)
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

# Function to create a new diamond at the top with a random color
def create_diamond():
    if not game_over:
        new_diamond_x = random.randint(DIAMOND_SIZE, SCREEN_WIDTH - DIAMOND_SIZE)
        new_diamond_y = SCREEN_HEIGHT - DIAMOND_SIZE
        color = random.choice(DIAMOND_COLORS)  # Choose a random color
        diamonds.append((new_diamond_x, new_diamond_y, color))

# Update the game logic
def update(value):
    global score, bar_x, falling_diamond, game_over, BAR_COLOR, lives, current_fall_speed, paused
    
    if not game_over and not paused:
        if not falling_diamond:

            if diamonds:
                falling_diamond = diamonds.pop(0)

        if falling_diamond:
            diamond_x, diamond_y, diamond_color = falling_diamond
            diamond_y -= current_fall_speed
            falling_diamond = (diamond_x, diamond_y, diamond_color)

# collision handle :
            if diamond_y <= BAR_HEIGHT and abs(diamond_x - bar_x) < BAR_WIDTH / 2:
                score += 1
                print("Score:",score)
                falling_diamond = None
                current_fall_speed += 0.5

            elif diamond_y < 0:
                game_over = True
                falling_diamond = None
                BAR_COLOR = RED
                current_fall_speed = DIAMOND_FALL_SPEED
                print("Game Over! Score:",score)
    if exit_game:
        glutLeaveMainLoop()
    
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)


# Handle keyboard input (left and right arrow keys)
def handle_keys(key, x, y):
    global bar_x
    speed = 15
    if key == GLUT_KEY_LEFT and not game_over and not paused:
        bar_x -= speed
        if bar_x < BAR_WIDTH / 2:
            bar_x = BAR_WIDTH / 2
    elif key == GLUT_KEY_RIGHT and not game_over and not paused:
        bar_x += speed
        if bar_x > SCREEN_WIDTH - BAR_WIDTH / 2:
            bar_x = SCREEN_WIDTH - BAR_WIDTH / 2

def handle_restart ():
    global score, lives, game_over, BAR_COLOR, falling_diamond, paused
    
    paused = False
    score = 0
    lives = 1
    game_over = False
    BAR_COLOR = WHITE
    diamonds.clear()
    falling_diamond = None

    # Create initial diamonds
    for _ in range(NUM_DIAMONDS):
        create_diamond()

# Handle keypress events (restart game with "R" key)
def handle_keypress(key, x, y):
    global paused

    if game_over and key == RESTART_KEY:
        handle_restart()
    elif not game_over and key == b'p':
        # Pause the game
        paused = not paused


def draw_points(x, y, color = (1, 1, 1)):
    glColor3fv(color)
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) # jekhane show korbe pixel
    glEnd()

def dezone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y , x
    elif zone == 2:
        return -y , x
    elif zone == 3:
        return -x , y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y , -x
    elif zone == 6:
        return y , -x
    elif zone == 7:
        return x , -y
    else:
        print("problem")
        return x , y

def zone_fnc(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy) and (dx >= 0 and dy >= 0):
        zone = 0
        return x1, y1, x2, y2, zone
    elif abs(dy) > abs(dx) and (dx >= 0 and dy >= 0):
        zone = 1
        return y1, x1, y2, x2, zone
    elif abs(dy) > abs(dx) and (dx < 0 and dy >= 0):
        zone = 2
        return y1, -x1, y2, -x2, zone
    elif abs(dx) >= abs(dy) and (dx < 0 and dy >= 0):
        zone = 3
        return -x1, y1, -x2, y2, zone
    elif abs(dx) >= abs(dy) and (dx < 0 and dy < 0):
        zone = 4
        return -x1, -y1, -x2, -y2, zone
    elif abs(dy) > abs(dx) and (dx < 0 and dy < 0):
        zone = 5
        return -y1, -x1, -y2, -x2, zone
    elif abs(dy) > abs(dx) and (dx >= 0 and dy < 0):
        zone = 6
        return -y1, x1, -y2, x2, zone
    elif abs(dx) >= abs(dy) and (dx >= 0 and dy < 0):
        zone = 7
        return x1, -y1, x2, -y2, zone

def mid_line(x1, y1, x2, y2 , color = (1, 1, 1)):
    x1 , y1 , x2, y2, zone = zone_fnc(x1, y1, x2, y2)
    dx = x2 - x1
    dy = y2 - y1
    d = 2*dy - dx
    incE = 2*dy
    incNE = 2*(dy-dx)
    y = y1
    x = x1
    draw_points(x, y, color)
    while (x<=x2):
        if (d>0):
            y += 1
            d += incNE
        else:
            d += incE
        x += 1
        x_t , y_t = dezone(x , y , zone)
        draw_points(x_t, y_t, color)

# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    glutCreateWindow(b"Catch the Diamonds")

    init()

    # Register callback functions
    glutDisplayFunc(display)
    glutSpecialFunc(handle_keys)
    glutTimerFunc(10, update, 0)
    glutKeyboardFunc(handle_keypress)  # Register keypress callback
    glutMouseFunc(handle_mouse_click)

    # Create initial diamonds
    for _ in range(NUM_DIAMONDS):
        create_diamond()

    glutMainLoop()

if __name__ == "__main__":
    bar_x = SCREEN_WIDTH / 2
    main()