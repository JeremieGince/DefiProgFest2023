import DQLearning as dq
import numpy as np 
import matplotlib.pyplot as plt
import tqdm 
import time
import gymnasium as gym
import torch

turbulence = np.random.uniform(0,2)
wind = np.random.uniform(0,20)
env = gym.make("LunarLander-v2",continuous=False, render_mode="human", gravity = -10, enable_wind = True, 
              wind_power = wind, turbulence_power=turbulence)
agent = dq.Agent(gamma=0.99, epsilon=0.9, batch_size=64, n_actions=4, eps_end=0.0000, input_dims=[8,], lr=0.0000)
agent.Q_eval.load_state_dict(torch.load("model_test.pt"))
agent.epsilon = 0
scores = []
nb_of_games = 5


for _ in tqdm.tqdm(range(nb_of_games)):
    score = 0
    terminal = False
    observation, info = env.reset()
    while not terminal:
        action = agent.choose_action(observation)
        new_obs, reward, terminated, truncated, info = env.step(action)
        score += reward
        terminal = terminated or truncated
        agent.store_transition(observation, action, reward, new_obs, terminal=terminal)
        agent.learn()
        observation = new_obs
    scores.append(score)
    
env.close()

# env2 = gym.make("LunarLander-v2",continuous=False, render_mode="human", gravity = -10, enable_wind = True, 
#                wind_power = wind, turbulence_power=turbulence)

# observation, info = env2.reset()
# for _ in range(1000):
#     agent.epsilon = 0
#     action = agent.choose_action(observation)
#     observation, reward, terminated, truncated, info = env2.step(action)
#     if terminated or truncated:
#         observation, info = env2.reset()
torch.save(agent.Q_eval.state_dict(),"model_test.pt")
plt.plot(scores)
plt.show()


