import pygame as py
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = PLAYER_RADIUS
        self.rotation = 0

    def draw(self, screen):
        py.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = py.Vector2(0, 1).rotate(self.rotation)
        right = py.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = py.key.get_pressed()

        if keys[py.K_a]:
            self.rotate(-dt)
        if keys[py.K_d]:
            self.rotate(dt)
