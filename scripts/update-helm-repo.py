from dotenv import load_dotenv
import os
import sys
import subprocess

load_dotenv()

"""
This is the python translation of the shell script that clones a Helm chart repository and updates the deployment file with the current build number.

Usage:
    py update-helm-repo.py  <k8s_deployment> <repository_url> [destination_directory]
"""

deployment  = sys.argv[1]
repo_url    = sys.argv[2]
dest_dir    = sys.argv[3]  if len(sys.argv) > 3 and sys.argv[3] else "./repos"

def clone_repo(repo_url, dest_dir=None):
    command = ["git", "clone", repo_url]
    if dest_dir:
        command.append(dest_dir)
    try:
        subprocess.run(command, check=True)
        print(f"Repository cloned from {repo_url}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: py update-helm-repo.py  <k8s_deployment> <repository_url> [destination_directory]")
        sys.exit(1)
    
    
    clone_repo(repo_url, dest_dir)
    