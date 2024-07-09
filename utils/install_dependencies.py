import subprocess
import os
import sys

def activate_virtualenv(venv_path):
    activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
    if not os.path.exists(activate_script):
        raise FileNotFoundError(f"The virtual environment activation script not found: {activate_script}")
    os.system(f'cmd /k "{activate_script}"')

def install_requirements():
    try:
        # Run the pip install command
        result = subprocess.run(["pip", "install", "-r", "requirements.txt"], capture_output=True, text=True, check=True)
        print(result.stdout)
        print("All dependencies have been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")

if __name__ == "__main__":
    # Replace 'newenv' with your actual virtual environment path if different
    venv_path = 'newenv'
    try:
        activate_virtualenv(venv_path)
        install_requirements()
    except Exception as e:
        print(f"An error occurred: {e}")