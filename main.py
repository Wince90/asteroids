import pygame as py
from constants import *
from player import Player

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_color = ("black")

def main():
    py.init()
    time = py.time.Clock()
    dt = 0
    is_on = True

    updatable = py.sprite.Group()
    drawable = py.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20)
    

    while is_on:
        for event in py.event.get():
            if event.type == py.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        screen.fill(background_color)
        
        for obj in drawable:
            obj.draw(dt)

        py.display.flip()
        dt = time.tick(60) / 1000
        



if __name__ == "__main__":
    main()