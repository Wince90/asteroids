import pygame as py
from circleshape import CircleShape
from shot import Shoot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.timer = 0

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

        self.timer -= dt

        if keys[py.K_a]:
            self.rotate(-dt)
        if keys[py.K_d]:
            self.rotate(dt)
        if keys[py.K_w]:
            self.move(dt)
        if keys[py.K_s]:
            self.move(-dt)
        if keys[py.K_SPACE]:
            if not(self.timer > 0):
                self.shoot()

    def move(self, dt):
        forward = py.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        shot = Shoot(self.position.x, self.position.y)
        shot.velocity = py.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
