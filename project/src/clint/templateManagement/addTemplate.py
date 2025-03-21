import os


def addTemplate(templateName: str, templatePath: str, templateType: str) -> None:
    """
    Add a custom template to the template directory

    Args:
        templateName (str): name of the template
        templatePath (str): path to the template .json file
        templateType (str): project or script template
    """
    try:
        if os.path.exists(templatePath):
            savePath = ""

            currentDir = os.path.dirname(os.path.abspath(__file__))

            with open(templatePath, "r") as f:
                template = f.read()

            if templateType == "script":
                savePath = currentDir + "/../scripting/templates"

            elif templateType == "project":
                savePath = currentDir + "/../makeProject/templates"

            else:
                print(f"\033[91mType {templateType} not supported\033[0m")
                return

            with open(f"{savePath}/{templateName}.json", "w") as f:
                f.write(template)

            print(f"\033[92mTemplate added successfully\033[0m")

        else:
            print(f"\033[91mTemplate path {templatePath} does not exist\033[0m")

            return

    except Exception as e:
        print(f"\033[91mError adding template: {e}\033[0m")

        return


def interactiveMode() -> None:
    """
    Interactive mode for addTemplate
    """
    print("Add a template")

    templateName = input("Template Name: ")

    templatePath = input("Template path: ")

    templateType = input("Template Type (script or project): ")

    addTemplate(templateName, templatePath, templateType)


if __name__ == "__main__":
    interactiveMode()
