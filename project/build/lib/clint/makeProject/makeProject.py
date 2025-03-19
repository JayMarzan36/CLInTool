import os

from ..templateManagement.Template import Template

TEMPLATESPATH = os.path.join(os.path.dirname(__file__), "templates")


def loadTemplate(templateType: str) -> str:
    """
    Load a template

    Args:
        templateType (str): name of template

    Returns:
        dict: contents of template
    """
    try:
        templatePath = os.path.join(TEMPLATESPATH, templateType)

        if os.path.exists(templatePath):
            return templatePath

        else:
            return None

    except Exception as e:
        print(f"\033[91mError loading template: {e}\033[0m")

        return None


def createProject(
    name: str,
    lang: str,
    git: bool,
    venv: bool,
    useLocalTemplate: bool = False,
    templatePath: str = None,
) -> None:
    """
    Create a project

    Args:
        name (str): name of project
        lang (str): programming language
        git (bool): make git repository
        venv (bool): make virtual environment
        useLocalTemplate (bool): use local template instead of built-in
        templatePath (str): path to local template if useLocalTemplate is True

    Returns:
        _type_: None
    """
    projectPath = os.path.join(os.getcwd(), name)

    os.makedirs(projectPath, exist_ok=True)

    os.makedirs(os.path.join(projectPath, "src"), exist_ok=True)

    projectPath = os.path.join(projectPath, "src")

    if useLocalTemplate and templatePath:
        templateSourcePath = templatePath

    else:
        templateSourcePath = loadTemplate(lang)

    if templateSourcePath:
        templateClass = Template(path=templateSourcePath)

        templateClass.makeFromTemplate()

    elif templateSourcePath is None:
        print(
            f"\033[91mTemplate for {lang} not found. Could not generate project\033[0m"
        )

        return

    if git:
        os.system(f"cd {projectPath} && git init")

    if venv == "python" and "python" in lang:
        os.system(f"python -m venv {os.path.join(projectPath, 'venv')}")

    print(f"Project \033[92m{name}\033[0m created at \033[92m{projectPath}\033[0m")


def interactiveMode() -> None:
    """
    Interactive mode for projectGen
    """
    print("Create a project")

    name = input("Enter project name: ")

    lang = input("Enter project language: ")

    useLocalTemplate = input("Use local template? (y/n): ").lower() == "y"

    templatePath = None

    if useLocalTemplate:
        templatePath = input("Enter template path: ")

    git = input("Initialize git repository? (y/n): ").lower() == "y"

    venv = input("Create virtual environment? (y/n): ").lower() == "y"

    createProject(name, lang, git, venv, useLocalTemplate, templatePath)


def main() -> None:
    """
    Main function that calls interactiveMode
    """
    interactiveMode()


if __name__ == "__main__":
    main()
