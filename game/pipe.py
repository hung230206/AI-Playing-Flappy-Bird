import pygame
import random

PIPE_WIDTH = 60
GAP = 150
SPEED = 3

class Pipe:
    def __init__(self, x, screen_height):
        self.x = x
        self.gap_y = random.randint(150, screen_height - 150)
        self.passed = False

    def update(self):
        self.x -= SPEED

    def collide(self, bird):
        top = pygame.Rect(self.x, 0, PIPE_WIDTH, self.gap_y - GAP // 2)
        bottom = pygame.Rect(
            self.x,
            self.gap_y + GAP // 2,
            PIPE_WIDTH,
            screen_height := 600
        )
        return top.colliderect(bird.get_rect()) or bottom.colliderect(bird.get_rect())
