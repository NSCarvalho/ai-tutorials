import subprocess

def generate_requirements():
    try:
        # Run the pip freeze command
        result = subprocess.run(["pip", "freeze"], capture_output=True, text=True, check=True)
        # Write the output to requirements.txt
        with open("requirements.txt", "w") as file:
            file.write(result.stdout)
        print("requirements.txt file has been generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    generate_requirements()