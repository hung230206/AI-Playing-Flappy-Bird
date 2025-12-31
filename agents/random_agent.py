import random
from env.flappy_env import FlappyEnv

env = FlappyEnv()

episodes = 5

for ep in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = random.randint(0, 1)
        state, reward, done = env.step(action)
        total_reward += reward

    print(f"Episode {ep+1}: reward = {total_reward:.2f}")
