import os


def createProject(name: str, lang: str, git: bool, venv: bool) -> None:
    """_summary_

    Args:
        name (str): _description_
        lang (str): _description_
        git (bool): _description_
        venv (bool): _description_

    Returns:
        _type_: _description_
    """
    
    projectPath = os.path.join(os.getcwd(), name)
    os.makedirs(projectPath, exist_ok=True)

    templates = {
        "python": {
            "mainFile": "main.py",
            "mainFileContent": "def main() -> None:\n   pass\n\nif __name__ == '__main__':\n    main()",
            "additionalFiles": ["requirements.txt"],
            "additionalFilesContent": "Project requirements",
        },
        "c": {
            "mainFile": "main.c",
            "mainFileContent": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "additionalFiles": ["requirements.txt"],
            "additionalFilesContent": "Project requirements",
        },
        "java": {
            "mainFile": "Main.java",
            "mainFileContent": "public class Main {\n  public static void main(String[] args) {\n  System.out.println('hello world');\n    }\n}",
            "additionalFiles": ["requirements.txt"],
            "additionalFilesContent": ["Project requirements"],
        },
    }

    os.makedirs(os.path.join(projectPath, "src"), exist_ok=True)

    projectPath = os.path.join(projectPath, "src")

    template = templates.get(lang)
    if template:
        with open(os.path.join(projectPath, template["mainFile"]), "w") as f:
            f.write(template["mainFileContent"])

        for i, additionalFile in enumerate(template["additionalFiles"]):
            content = template["additionalFilesContent"]
            # Handle both string and list content types
            file_content = content[i] if isinstance(content, list) else content
            with open(os.path.join(projectPath, additionalFile), "w") as f:
                f.write(file_content)

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
    """
    Main function that calls interactiveMode
    """
    interactiveMode()


if __name__ == "__main__":
    main()
