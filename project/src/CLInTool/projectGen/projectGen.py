import os

def createProject(name : str, lang : str, git : bool, venv : bool) -> None:
    projectPath = os.path.join(os.getcwd(), name)
    os.makedirs(projectPath, exist_ok=True)
    
    templates = {
        "python": ["main.py", "requirements.txt"],
        "c" : ["main.c", "requirements.txt"],
        "java" : ["main.java", "requirements.txt"]
    }
    
    os.makedirs(os.path.join(projectPath, "src"), exist_ok=True)
    
    projectPath = os.path.join(projectPath, "src")
    
    for file in templates.get(lang, []):
        with open(os.path.join(projectPath, file), "w") as f:
            f.write(f"// {file} template\n")
    
    if git:
        os.system(f"cd {projectPath} && git init")
    
    if venv and lang == "python":
        os.system(f"python -m venv {os.path.join(projectPath, 'venv')}")
    
    print(f"Project \033[92m{name}\033[0m created at \033[92m{projectPath}\033[0m")

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