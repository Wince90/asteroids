import pygame as py
from constants import *

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_color = ("black")

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def game_run():
    is_on = True
    while is_on:
        for event in py.event.get():
            if event.type == py.QUIT:
                return
        screen.fill(background_color)
        py.display.flip()


if __name__ == "__main__":
    main()
    py.init()
    game_run()