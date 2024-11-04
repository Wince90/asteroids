import pygame as py
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shoot

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_color = ("black")

def main():
    py.init()
    time = py.time.Clock()
    dt = 0
    is_on = True

    updatable = py.sprite.Group()
    drawable = py.sprite.Group()
    asteroids = py.sprite.Group()
    shoots = py.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shoot.containers = (drawable, shoots, updatable)
    Player.containers = (updatable, drawable, shoots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20)
    

    while is_on:
        for event in py.event.get():
            if event.type == py.QUIT:
                return

        for obj in asteroids:
            if obj.collision(player):
                print("Game Over!")
                py.quit()
            for shot in shoots:
                if obj.collision(shot):
                    shot.kill()
                    obj.split() 
        
        for obj in updatable:
            obj.update(dt)
        screen.fill(background_color)
        
        for obj in drawable:
            obj.draw(screen)

        py.display.flip()
        dt = time.tick(60) / 1000
        



if __name__ == "__main__":
    main()