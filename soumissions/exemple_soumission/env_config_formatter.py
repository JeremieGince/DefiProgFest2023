
def set_default_env_config(env_config: dict):
	env_config.setdefault('render_mode', None)
	env_config.setdefault('id', "LunarLander-v2")
	return env_config
	
	
def convert_str_attr_to_float_env_config(env_config: dict):
	"""
	Cette fonction est utilisée pour convertir les attributs de type str en float dans les paramètres de l'environnement.

	:param env_config: Paramètres de l'environnement.
	:type env_config: dict
	"""
	import numpy as np
	attrs_to_convert_to_range = {
		"wind_power": (0.0, 20.0),
		"turbulence_power": (0.0, 2.0)
	}
	for key, k_range in attrs_to_convert_to_range.items():
		if isinstance(env_config.get(key, None), str):
			env_config[key] = np.random.uniform(*k_range)
	return env_config


def format_env_config(env_config: dict):
	"""
	Cette fonction est utilisée pour formater les paramètres de l'environnement.

	:param env_config: Paramètres de l'environnement.
	:type env_config: dict
	:return: Paramètres de l'environnement formatés.
	:rtype: dict
	"""
	set_default_env_config(env_config)
	return env_config
