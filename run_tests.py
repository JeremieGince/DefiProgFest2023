import os
import subprocess
import sys
from importlib import import_module
from tools.tester import LunarLanderPerformanceTest, LunarLanderTester, LunarLanderPEP8Test
import warnings


def get_env_configs(configs_file_path: str = "./env_configs.json"):
	import json
	with open(configs_file_path, "r") as f:
		env_configs = json.load(f)
	return env_configs


def main(root_folder: str, configs_file_path: str = "./env_configs.json"):
	tester = LunarLanderTester()
	pep8_test = LunarLanderPEP8Test(name="PEP8", file_path="./lunar_lander_agent.py")
	tester.add_test(pep8_test)
	env_configs = get_env_configs(configs_file_path=configs_file_path)
	cwd = os.getcwd()
	print(f"Working directory: {os.getcwd()}")
	
	lunar_lander_name = f".lunar_lander_agent"
	lunar_lander_root_importlike = root_folder.replace('./', '').replace('/', '.')
	lunar_lander_cls = getattr(import_module(lunar_lander_name, lunar_lander_root_importlike), "LunarLanderAgent")
	for config_name, env_config in env_configs.items():
		os.chdir(root_folder)
		print(f"Current cwd: {os.getcwd()}")
		agent = lunar_lander_cls(env_config=env_config)
		performance_test = LunarLanderPerformanceTest(
			name=config_name,
			agent=agent,
			env_config=env_config,
		)
		tester.add_test(performance_test)
		os.chdir(cwd)
	tester.run()
	print(tester)
	tester.to_file(file_path=f"{root_folder}/test_results.txt")


if __name__ == "__main__":
	with warnings.catch_warnings():
		warnings.filterwarnings("ignore", category=DeprecationWarning)
		main(sys.argv[1])
