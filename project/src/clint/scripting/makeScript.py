import platform, os, json

TEMPLATEPATH = os.path.join(os.path.dirname(__file__), "templates")


def getPlatform() -> str:
    """
    Get the current platform

    Returns:
        str: platform (os)
    """
    return platform.system().lower()


def loadTemplate(fileType: str) -> dict:
    """
    Load a template
    Args:
        fileType (str): file extension

    Returns:
        dict: template contents
    """
    try:
        fileType = fileType.replace(".", "")

        finalTemplate = {}

        template = json.load(open(os.path.join(TEMPLATEPATH, f"{fileType}.json")))

        finalTemplate.update({"content": template.get("content")})

        return finalTemplate

    except Exception as e:
        print(f"\033[91mError loading template: {e}\033[0m")
        return None


def scriptGen(name: str, templateType: str) -> None:
    """
    Generate script

    Args:
        name (str): name of script

    Raises:
        Exception: any error that occurs
    """
    platforms = {
        "windows": ".bat",
        "linux": ".sh",
        "darwin": ".sh",
    }

    try:
        platform = getPlatform()

        ext = platforms.get(platform, ["", ""])

        currentTemplate = None

        try:

            if templateType != None:
                currentTemplate = loadTemplate(templateType)

            else:
                currentTemplate = loadTemplate(ext)

            if len(currentTemplate) > 0:
                print(f"\033[92mTemplate found \033[0m")

            else:
                raise Exception("No template found")

        except Exception as e:
            print(f"\033[91mAn error occured with the template: {e}\033[0m")

        if currentTemplate == None:
            print(f"\033[91mNo template found for {platform}\033[0m")

            print(f"\033[93mCreating empty script\033[0m")

            with open(f"{name}{ext}", "w") as f:
                f.write(currentTemplate.get("content"))

        else:
            print(f"\033[93mCreating script with template\033[0m")

            with open(f"{name}{ext}", "w") as f:
                f.write(currentTemplate.get("content"))

        print(f"Script \033[92m{name}{ext}\033[0m created")

    except Exception as e:
        print(f"\033[91mAn error occurred: {e}\033[0m")


def interactiveMode() -> None:  # Main function
    """
    Interactive mode for scriptGen
    """
    print("Script generator")

    name = input("Enter script name: ")

    useTemplate = input("Use template? (y/n): ")

    if useTemplate == "y":
        templateType = input("Enter template name: ")

        print(f"Using template")

        scriptGen(name, templateType)

    else:
        print(f"Creating script using default template")

        scriptGen(name, templateType=None)


if __name__ == "__main__":
    interactiveMode()