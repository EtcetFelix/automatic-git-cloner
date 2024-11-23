import os
import dotenv

dotenv.load_dotenv(override=True)

repo_url = input("Enter the GitHub repository URL: ")
base_path = os.getenv("FOLDER_PATH")

# Ensure base_path is valid
if not base_path:
    raise ValueError("FOLDER_PATH environment variable is not set.")

repo_name = os.path.splitext(os.path.basename(repo_url))[0]  # Extract repo name
target_path = os.path.join(base_path, repo_name)

# Create the target directory if it doesn't exist
if not os.path.exists(target_path):
    os.makedirs(target_path)

os.system(f"git clone {repo_url} {target_path}")

print(f"Cloned repository into: {target_path}")