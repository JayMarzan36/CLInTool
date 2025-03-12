import os
import json

TEMPLATESPATH = os.path.join(os.path.dirname(__file__), "templates")


def loadTemplate(type: str) -> dict:
    try:
        finalTemplate = {}
        template = json.load(open(os.path.join(TEMPLATESPATH, f"{type}.json")))
        numOfFiles = template.get("files")[0].get("numOfFiles") + 1
        for i in range(numOfFiles):
            if i == 0:
                continue
            finalTemplate[template.get("files")[i].get("name")] = template.get("files")[
                i
            ].get("content")
        return finalTemplate
    except Exception as e:
        print(f"\033[91mError loading template: {e}\033[0m")
        return None


def createProject(name: str, type: str, git: bool, venv: bool) -> None:
    """_summary_

    Args:
        name (str): _description_
        type (str): _description_
        git (bool): _description_
        venv (bool): _description_

    Returns:
        _type_: _description_
    """

    projectPath = os.path.join(os.getcwd(), name)
    os.makedirs(projectPath, exist_ok=True)

    os.makedirs(os.path.join(projectPath, "src"), exist_ok=True)

    projectPath = os.path.join(projectPath, "src")

    template = loadTemplate(type)

    if template:
        for i in template:
            with open(os.path.join(projectPath, i), "w") as f:
                f.write(template[i])
    elif template is None:
        print(
            f"\033[91mTemplate for {type} not found. Could not generate project\033[0m"
        )
        return

    if git:
        os.system(f"cd {projectPath} && git init")

    if venv == "python" and "python" in type:
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
