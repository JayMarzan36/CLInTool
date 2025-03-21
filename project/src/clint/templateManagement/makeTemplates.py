import os
import json


def makeTemplate(name: str, templateType: str) -> None:
    """
    Create a template main function

    Args:
        name (str): name of template
        content (str): content of template
        templateType (str): project or script template
    """
    currentDir = os.path.dirname(os.path.abspath(__file__))

    acceptedTypes = {
        "script": os.path.join(currentDir, "../scripting/templates"),
    }

    if templateType in acceptedTypes:
        finalTemplate = {}

        if templateType == "script":
            content = input("Content: ")

            finalTemplate["content"] = content

        with open(f"{acceptedTypes[templateType]}/{name}.json", "w") as f:
            json.dump(finalTemplate, f)

        print(f"\033[92mTemplate {name} created\033[0m")

    else:
        print(f"\033[91mType {templateType} not supported\033[0m")

        return


def interactiveMode() -> None:
    """
    Interactive mode for makeTemplate
    """
    print("Make a template")

    name = input("Name: ")

    templateType = input("Template Type: ")

    makeTemplate(name, templateType)


if __name__ == "__main__":
    interactiveMode()
