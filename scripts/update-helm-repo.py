import sys
import subprocess

"""
This is the python translation of the shell script that clones a Helm chart repository and updates the deployment file with the current build number.

Usage:
    py clone_repo.py <k8s_deployment> <repository_url> [destination_directory]
"""

arguments = sys.argv[1:]

deployment, repo_url = arguments
dest_dir = arguments[3]  if len(arguments) > 3 and arguments[3] else "./repos"

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
        print("Usage: py clone_repo.py <k8s_deployment> <repository_url> [destination_directory]")
        sys.exit(1)
    
    
    clone_repo(repo_url, dest_dir)
    