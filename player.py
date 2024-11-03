import pygame as py
from circleshape import CircleShape
from constants import PLAYER_RADIUS

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