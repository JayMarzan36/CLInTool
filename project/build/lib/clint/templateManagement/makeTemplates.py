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
        "project": os.path.join(currentDir, "../makeProject/templates"),
    }

    if templateType in acceptedTypes:
        finalTemplate = {}

        if templateType == "script":
            content = input("Content: ")

            finalTemplate["content"] = content

        elif templateType == "project":
            numOfFiles = int(input("Number of files: "))

            finalTemplate["files"] = []

            finalTemplate["files"].append({"numOfFiles": numOfFiles})

            for i in range(numOfFiles):
                currentFileName = input(f"File {i+1} name: ")

                currentFileContent = input(f"File {i+1} content: ")

                finalTemplate["files"].append(
                    {"name": currentFileName, "content": currentFileContent}
                )

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
