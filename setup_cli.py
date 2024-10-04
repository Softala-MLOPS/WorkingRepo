import os
import typer
import subprocess
import sys

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

    print("Pushing the repository to GitHub...")
    push_repo()




    
if __name__ == "__main__":
    typer.run(main)