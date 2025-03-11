import platform
from . import scriptTemplates as templates

def getPlatform() -> str:
    return platform.system().lower()

def scriptGen(name : str) -> None:
    platforms = {
        "windows" : [".bat", "echo test"],
        "linux" : [".sh", "#!/bin/bash"],
        "darwin" : [".sh", "#!/bin/bash"],
    }

    try:
        platform = getPlatform()
        ext, content = platforms.get(platform, ["", ""])
        currentTemplate = None
        
        try:
            currentTemplate = templates.getTemplates(ext)
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
                f.write(content)
        else:
            print(f"\033[93mCreating script with template\033[0m")
            with open(f"{name}{ext}", "w") as f:
                f.write(currentTemplate[0])
        
        print(f"Script \033[92m{name}{ext}\033[0m created")
    except Exception as e:
        print(f"\033[91mAn error occurred: {e}\033[0m")




def interactiveMode() -> None: #Main function
    name = input("Enter script name: ")
    scriptGen(name)


if __name__ == "__main__":
    interactiveMode()