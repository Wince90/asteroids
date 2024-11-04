import pygame as py

# Base class for game objects
class CircleShape(py.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = py.Vector2(x, y)
        self.velocity = py.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, obj):
        return self.position.distance_to(obj.position) <= self.radius + obj.radius
        
