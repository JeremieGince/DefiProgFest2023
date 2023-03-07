import gymnasium as gym
import numpy as np

env = gym.make("LunarLander-v2",continuous=False, render_mode="null", gravity = -10, enable_wind = True, 
               wind_power = np.random.uniform(0,20), turbulence_power=np.random.uniform(0,2))
observation, info = env.reset()
print(env.action_space)
for _ in range(1000):
   action = env.action_space.sample()  # this is where you would insert your policy
   observation, reward, terminated, truncated, info = env.step(action)
   
   if terminated or truncated:
      observation, info = env.reset()
env.close()