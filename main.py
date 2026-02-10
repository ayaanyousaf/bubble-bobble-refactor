import pygame, pgzero, pgzrun, sys
from pgzero.builtins import music

# Constants
WIDTH = 800
HEIGHT = 480
TITLE = "Cavern"

# Check Python version number
if sys.version_info < (3,5):
    print("This game requires at least version 3.5 of Python. Please download it from www.python.org")
    sys.exit()

# Check Pygame Zero version
pgzero_version = [int(s) if s.isnumeric() else s for s in pgzero.__version__.split('.')]
if pgzero_version < [1,2]:
    print("This game requires at least version 1.2 of Pygame Zero. You have version {0}. Please upgrade using the command 'pip3 install --upgrade pgzero'".format(pgzero.__version__))
    sys.exit()

# Initialize the app
from src.app import App
app = App()

# Pygame Zero calls the update and draw functions each frame
def update():
    app.update()

def draw():
    app.draw(screen) 

# Set up sound system and start music
try:
    pygame.mixer.quit()
    pygame.mixer.init(44100, -16, 2, 1024)

    music.play("theme")
    music.set_volume(0.3)
except:
    # If an error occurs, just ignore it
    pass

pgzrun.go()
