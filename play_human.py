import pygame
from env.flappy_env import FlappyEnv

pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

env = FlappyEnv()
state = env.reset()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            state, _, done = env.step(1)

    state, _, done = env.step(0)

    screen.fill((135, 206, 235))
    pygame.draw.circle(screen, (255, 255, 0),
                       (100, int(env.bird.y)), 12)

    for pipe in env.pipes:
        pygame.draw.rect(screen, (0, 200, 0),
                         (pipe.x, 0, 60, pipe.gap_y - 75))
        pygame.draw.rect(screen, (0, 200, 0),
                         (pipe.x, pipe.gap_y + 75, 60, 600))

    pygame.display.flip()

    if done:
        env.reset()

pygame.quit()
