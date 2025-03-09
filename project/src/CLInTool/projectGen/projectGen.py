import os
import argparse
import shutil

def createProject(name : str, lang : str, git : bool, venv : bool) -> None:
    projectPath = os.path.join(os.getcwd(), name)
    os.makedirs(projectPath, exist_ok=True)
    
    templates = {
        "python": [],
        "c" : [],
        "java" : []
    }
    
    for file in templates.get(lang, []):
        with open(os.path.join(projectPath, file), "w") as f:
            f.write(f"// {file} template\n")
    
    if git:
        os.system(f"cd {projectPath} && git init")
    
    if venv and lang == "python":
        os.system(f"python -m venv {os.path.join(projectPath, 'venv')}")
    
    print(f"Project {name} created at {projectPath}")

def interactiveMode() -> None:
    name = input("Enter project name: ")
    lang = input("Enter project language: ")
    git = input("Initialize git repository? (y/n): ").lower() == "y"
    venv = input("Create virtual environment? (y/n): ").lower() == "y"
    
    createProject(name, lang, git, venv)

def main() -> None:
    interactiveMode()
        
        
if __name__ == "__main__":
    main()