import platform


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
        
        with open(f"{name}{ext}", "w") as f:
            f.write(content)
        
        print(f"Script \033[92m{name}{ext}\033[0m created")
    except Exception as e:
        print(f"\033[91mAn error occurred: {e}\033[0m")




def interactiveMode() -> None: #Main function
    name = input("Enter script name: ")
    scriptGen(name)


if __name__ == "__main__":
    interactiveMode()