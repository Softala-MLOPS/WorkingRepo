import os
import typer
import subprocess
import sys
import shutil

def check_gh_installed():
    """Check if GitHub CLI is installed."""
    try:
        result = subprocess.run(["gh", "--version"], capture_output=True, text=True)
        if result.returncode != 0:
            typer.echo("GitHub CLI (gh) is not installed.")
            sys.exit(1)
    except FileNotFoundError:
        typer.echo("GitHub CLI (gh) is not installed.")
        sys.exit(1)

def create_repo():
    result = subprocess.run("gh auth status", shell=True, capture_output=True, text=True)
    if "Logged in to github.com account" not in result.stdout:
        subprocess.run("gh auth login", shell=True)
    subprocess.run('gh repo create Softala-MLOPS/configRepoCLI --public --description "Upstream repository" --clone', shell=True)
    os.chdir("configRepoCLI")

def create_repo_structure():
    """Create the repository structure."""
    subprocess.run(f"mkdir -p data", shell=True, capture_output=True)
    os.chdir("data")
    subprocess.run(f'echo "data" > Readme.md', shell=True, capture_output=True)
    os.chdir("../")
    subprocess.run(f"mkdir -p docs", shell=True, capture_output=True)
    os.chdir("docs")
    subprocess.run(f'echo "docs" > Readme.md', shell=True, capture_output=True)
    os.chdir("../")
    subprocess.run(f"mkdir -p models", shell=True, capture_output=True)
    os.chdir("models") 
    subprocess.run(f'echo "models" > Readme.md', shell=True, capture_output=True)
    os.chdir("../")
    subprocess.run(f"mkdir -p notebook", shell=True, capture_output=True)
    os.chdir("notebook")
    subprocess.run(f'echo "notebook" > Readme.md', shell=True, capture_output=True)
    os.chdir("../")
    subprocess.run(f"mkdir -p src", shell=True, capture_output=True)
    os.chdir("src")
    subprocess.run(f'echo "src" > Readme.md', shell=True, capture_output=True)
    os.chdir("../")
    subprocess.run(f"mkdir -p tests", shell=True, capture_output=True)
    os.chdir("tests")
    subprocess.run(f'echo "tests" > Readme.md', shell=True, capture_output=True)
    os.chdir("../")
    subprocess.run(f'touch .gitignore', shell=True, capture_output=True)
    subprocess.run(f'touch LICENSE', shell=True, capture_output=True)
    subprocess.run(f'touch README.md', shell=True, capture_output=True)
    subprocess.run(f'touch requirements.txt', shell=True, capture_output=True)

def set_config():
    """Create a config file for github secrets"""

    print("1 Create config file\n2 Specify file path to an existing config file")
    choise = int(input())

    if choise == 1:
        """No config file"""
        file = open(".config", "w")
        print("Specify Kubeflow endpoint (if empty uses http://localhost:8080 by default)")
        kep = input()
        if kep == "":
            kep = "http://localhost:8080"
        print("Specify Kubeflow username (if empty uses user@example.com by default)")
        kun = input()
        if kun == "":
            kun = "user@example.com"
        print("Specify Kubeflow password (if empty uses 12341234 by default)")
        kpw = input()
        if kpw == "":
            kpw = "12341234"
        print("Add remote cluster private key")
        remote_key = input()
        print("Specify remote cluster IP")
        remote_ip = input()
        print("Add remote cluster username")
        remote_username = input()
        file.write(f'KUBEFLOW_ENDPOINT={kep}\n')
        file.write(f'KUBEFLOW_USERNAME={kun}\n')
        file.write(f'KUBEFLOW_PASSWORD={kpw}\n')
        file.write(f'REMOTE_CSC_CLUSTER_SSH_PRIVATE_KEY={remote_key}\n')
        file.write(f'REMOTE_CSC_CLUSTER_SSH_IP={remote_ip}\n')
        file.write(f'REMOTE_CSC_CLUSTER_SSH_USERNAME={remote_username}\n')
        file.close()
        subprocess.run(f'gh secret set KUBEFLOW_ENDPOINT --body {kep}', shell=True)
        subprocess.run(f'gh secret set KUBEFLOW_USERNAME --body {kun}', shell=True)
        subprocess.run(f'gh secret set KUBEFLOW_PASSWORD --body {kpw}', shell=True)
        subprocess.run(f'gh secret set REMOTE_CSC_CLUSTER_SSH_PRIVATE_KEY --body {remote_key}', shell=True)
        subprocess.run(f'gh secret set REMOTE_CSC_CLUSTER_SSH_IP --body {remote_ip}', shell=True)
        subprocess.run(f'gh secret set REMOTE_CSC_CLUSTER_SSH_USERNAME --body {remote_username}', shell=True)
    elif choise == 2:
        """Already a config file"""
        print('Enter path to config file:')
        file = open(".config", "w")
        fpath = input()
        split_file = open(fpath, "r").read().split('\n')
        for i, split_pair in enumerate(split_file):
            file.write(f'{split_file[i]}')
            split_pair = split_file[i].split(' = ')
            subprocess.run(f'gh secret set {split_pair[0]} --body {split_pair[0]}', shell=True)

def push_repo():
    """Push the repository to GitHub."""
    subprocess.run([f"git", 'add', '.'])
    subprocess.run([f"git", 'commit', '-m', '"Initial commit"'])
    subprocess.run([f"git", 'push', 'origin', 'main'])

def main():

    print("Checking if GitHub CLI is installed...")
    check_gh_installed()

    print("Creating a new repository...")
    create_repo()

    print("Creating the repository structure...")
    create_repo_structure()
    
    set_config()

    print("Pushing the repository to GitHub...")
    push_repo()




    
if __name__ == "__main__":
    typer.run(main)
