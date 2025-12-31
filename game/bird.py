import pygame

GRAVITY = 0.5
JUMP_VELOCITY = -8

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.radius = 12

    def jump(self):
        self.vel = JUMP_VELOCITY

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel

    def get_rect(self):
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )
