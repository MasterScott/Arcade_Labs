""" Lab 7 - User Control """
import arcade
from Control import *
from Drawings import *
# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600





def main():
    window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT, "Lab 7 - User Control")
    arcade.run()


main()