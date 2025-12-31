import numpy as np
from game.bird import Bird
from game.pipe import Pipe

class FlappyEnv:
    def __init__(self):
        self.width = 400
        self.height = 600
        self.reset()

    def reset(self):
        self.bird = Bird(100, self.height // 2)
        self.pipes = [Pipe(self.width, self.height)]
        self.score = 0
        self.done = False
        return self._get_state()

    def step(self, action):
        if action == 1:
            self.bird.jump()

        self.bird.update()
        reward = 0.1

        for pipe in self.pipes:
            pipe.update()

            if pipe.collide(self.bird):
                self.done = True
                reward = -10

            if pipe.x < self.bird.x and not pipe.passed:
                pipe.passed = True
                self.score += 1
                reward += 5

        if self.pipes[0].x < -60:
            self.pipes.pop(0)
            self.pipes.append(Pipe(self.width, self.height))

        if self.bird.y < 0 or self.bird.y > self.height:
            self.done = True
            reward = -10

        return self._get_state(), reward, self.done

    def _get_state(self):
        pipe = self.pipes[0]
        return np.array([
            self.bird.y / self.height,
            self.bird.vel / 10,
            (pipe.x - self.bird.x) / self.width,
            pipe.gap_y / self.height
        ], dtype=np.float32)
