import numpy as np


def get_random_generators(file: str = "./data.json"):
	import json
	with open(file, "r") as f:
		data = json.load(f)
	return data


def get_random_discrete_action(action_space, gen_name: str):
	return getattr(np.random, gen_name)(0, action_space.n)


def get_random_continuous_action(action_space, gen_name: str):
	return getattr(np.random, gen_name)(action_space.low, action_space.high)

