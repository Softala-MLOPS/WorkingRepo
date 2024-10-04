import os
import subprocess
import json

repo_name = "ConfigRepoCLI"

def get_repo_owner():

    result = subprocess.run(
        f"gh api -X GET search/repositories -f q='{repo_name} in:name' --jq '.items[] | {{name, owner: .owner.login}}'",
        shell=True,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print("Error fetching repository information:", result.stderr)
        return None
    
    try:
        repo_info = json.loads(result.stdout)
        owner_name = repo_info['owner']
        print(owner_name)
        return owner_name
    except json.JSONDecodeError:
        print("Error decoding repository information")
        return None

def fork_repo(owner):
    # Run the gh command to fork the repo
    subprocess.run(f'gh repo fork {owner}/{repo_name} --clone --fork-name "working-repo"', shell=True)
    print("Repository forked successfully") 

def create_branches():
    # Set the working directory to the cloned repo
    working_repo_path = os.path.join(os.getcwd(), "working-repo")
    
    # Create branches for development
    subprocess.run(f'git checkout -b development', shell=True, cwd=working_repo_path)
    subprocess.run(f'git push origin development', shell=True, cwd=working_repo_path)
    
    subprocess.run(f'git checkout -b staging', shell=True, cwd=working_repo_path)
    subprocess.run(f'git push origin staging', shell=True, cwd=working_repo_path)
    
    subprocess.run(f'git checkout -b production', shell=True, cwd=working_repo_path)
    subprocess.run(f'git push origin production', shell=True, cwd=working_repo_path)
    
    print("Branches created successfully")
    print("List of current branches:")
    subprocess.run(f'git branch -a', shell=True, cwd=working_repo_path, capture_output=True)

def main():

    print("Fetching repository information...")
    repo_owner = get_repo_owner()
    
    print("Forking the repository...")
    fork_repo(repo_owner)

    print("Creating branches...")
    create_branches()



if __name__ == "__main__":
    main()
