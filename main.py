import os
import subprocess
import sys
import warnings
	

def exec_code_in_venv(
		cmd: str,
		root_folder: str,
		cwd: str = ".",
		venv_name: str = "venv",
		**kwargs
):
	VENV_ACTIVATE_CMD_BY_OS = {
		"win32": r"{}\Scripts\activate.bat",
		"linux": "source {}/bin/activate",
		"darwin": "source {}/bin/activate",
	}
	requirements_path = os.path.join(root_folder, "requirements.txt")
	if os.path.exists(requirements_path):
		pip_install_cmd = f"pip install -r " + requirements_path
	else:
		pip_install_cmd = ""
	activate_cmd = VENV_ACTIVATE_CMD_BY_OS[sys.platform].format(venv_name)
	cmd = f"{activate_cmd} && {pip_install_cmd} && {cmd}"
	venv_path = os.path.join(root_folder, venv_name)
	if not os.path.exists(venv_path):
		cmd = f"python -m venv {venv_path} && {cmd}"
	process = subprocess.Popen(
		cmd,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT,
		shell=True,
		universal_newlines=True,
		encoding="utf8",
		errors='ignore',
		cwd=cwd,
	)
	stdout, stderr = process.communicate(timeout=kwargs.get("timeout", 5*60))
	return stdout, stderr


def main(root_folder: str):
	stdout, stderr = exec_code_in_venv(
		cmd=f"python run_tests.py {root_folder}",
		root_folder=root_folder,
		cwd="."
	)
	print(f"Stdout: {stdout}")
	print(f"Stderr: {stderr}")


if __name__ == "__main__":
	# main(f"./soumissions/exemple_soumission")
	with warnings.catch_warnings():
		warnings.filterwarnings("ignore", category=DeprecationWarning)
		for solution in os.listdir("./soumissions"):
			if solution == "exemple_soumission":
				continue
			print(f"Testing solution: {solution}")
			main(f"./soumissions/{solution}")
