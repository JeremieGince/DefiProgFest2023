from copy import deepcopy
from typing import List, Optional

import gym
import numpy as np
import tqdm

from tools.env_config_formatter import set_default_env_config, convert_str_attr_to_float_env_config


class TestResult:
	def __init__(self, name: str, percent_value: float, message: str = ""):
		self.name = name
		self.percent_value = percent_value
		self.message = message
	
	def __str__(self):
		_str = f'[{self.name}: {self.percent_value:.2f} %'
		if self.message:
			_str += f', ({self.message})'
		_str += ']'
		return _str


class LunarLanderTest:
	def run(self) -> TestResult:
		pass
	

class LunarLanderPerformanceTest(LunarLanderTest):
	def __init__(
			self,
			name: str,
			agent,
			env_config: dict,
			num_episodes: int = 100,
			solved_reward: float = 200.0,
	):
		self.name = name
		self.agent = agent
		self._given_config = deepcopy(env_config)
		self.env_config = deepcopy(env_config)
		self.set_default_env_config()
		self.observation_as_rgb = self.env_config.get("render_mode", None) == "rgb_array"
		self.num_episodes = num_episodes
		self.solved_reward = solved_reward
		self.cumulative_rewards_list = []
	
	def set_default_env_config(self):
		self.env_config = set_default_env_config(self.env_config)
		self.env_config = convert_str_attr_to_float_env_config(self.env_config)
	
	def compute_score(self):
		mean_cr = np.mean(self.cumulative_rewards_list).item()
		score = np.clip(mean_cr / self.solved_reward, 0.0, 1.0) * 100.0
		return score
	
	def run_episode(self, env, seed: int):
		observation, info = env.reset(seed=seed)
		terminal = False
		cumulative_rewards = 0.0
		while not terminal:
			if self.observation_as_rgb:
				rgb_observation = env.render()
				action = self.agent.get_action(rgb_observation)
			else:
				action = self.agent.get_action(observation)
			observation, reward, done, truncated, info = env.step(action)
			cumulative_rewards += reward
			terminal = done or truncated
		return cumulative_rewards
	
	def run(self, verbose: bool = True):
		p_bar = tqdm.tqdm(range(self.num_episodes), desc=f"Running {self.name}", disable=not verbose)
		for i in p_bar:
			try:
				env_config = convert_str_attr_to_float_env_config(self._given_config)
				env = gym.make(**env_config)
				cumulative_rewards = self.run_episode(env, seed=i)
				env.close()
			except Exception as e:
				return TestResult(self.name, 0.0, message=f"Error raised during test: {e}")
			self.cumulative_rewards_list.append(cumulative_rewards)
			curr_score = self.compute_score()
			curr_result = TestResult(self.name, curr_score)
			p_bar.set_postfix_str(f"{curr_result}")
		
		score = self.compute_score()
		result = TestResult(self.name, score)
		p_bar.set_postfix_str(f"{result}")
		p_bar.close()
		return result


class LunarLanderPEP8Test(LunarLanderTest):
	MAX_LINE_LENGTH = 120
	
	def __init__(self, name: str, file_path: str):
		self.name = name
		self.file_path = file_path
	
	def run(self):
		import pycodestyle
		pep8style = pycodestyle.StyleGuide(ignore="W191,E501", max_line_length=self.MAX_LINE_LENGTH, quiet=True)
		result = pep8style.check_files([self.file_path])
		message = ', '.join(set([f"{key}:'{err_msg}'" for key, err_msg in result.messages.items()]))
		err_ratio = result.total_errors / result.counters['physical lines']
		percent_value = np.clip(100.0 - (err_ratio * 100.0), 0.0, 100.0).item()
		return TestResult(self.name, percent_value, message=message)


class LunarLanderTester:
	def __init__(self, tests: Optional[List[LunarLanderTest]] = None):
		if tests is None:
			tests = []
		self.tests = tests
		self.results = []
	
	def add_test(self, test: LunarLanderTest):
		self.tests.append(test)
	
	def run(self):
		for test in self.tests:
			test_result = test.run()
			self.results.append(test_result)
		return self.results
	
	def __str__(self):
		return "\n".join([str(result) for result in self.results])
	
	def to_file(self, file_path: str):
		with open(file_path, "w") as f:
			f.write(str(self))
		print(f"Test results saved to '{file_path}'.")
