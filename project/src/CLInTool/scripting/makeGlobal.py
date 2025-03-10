import os
from .scriptGen import getPlatform

def makeScriptGlobal(scriptName : str) -> None:
    currentPlatform = getPlatform()
    
    platforms = {
        "windows" : ["C:\Program Files\\CLInTool\\", "move {scriptName}.bat C:\Program Files\\CLInTool\\", "[System.Environment]::SetEnvironmentVariable('Path', $env:Path + ';C:\Program Files\CLInTool', [System.EnvironmentVariableTarget]::Machine)"],
        "linux" : ["sudo mv {scriptName}.sh /usr/local/bin/", "chmod +x /usr/local/bin/{scriptName}.sh", "mv /usr/local/bin/{scriptName}.sh /usr/local/bin/{scriptName}"],
        "darwin" : ["sudo mv {scriptName}.sh /usr/local/bin/", "chmod +x /usr/local/bin/{scriptName}.sh", "mv /usr/local/bin/{scriptName}.sh /usr/local/bin/{scriptName}"],
    }
    
    if currentPlatform == "windows":
        currentPlatform = platforms.get(currentPlatform)
        if (os.path.exists(currentPlatform[0])):
            os.system(currentPlatform[1])
            os.system(currentPlatform[2])
        else:
            os.makedirs(currentPlatform[0])
            os.system(currentPlatform[1])
            os.system(currentPlatform[2])
    else:
        currentPlatform = platforms.get(currentPlatform)
        os.system(currentPlatform[0])
        os.system(currentPlatform[1])
        os.system(currentPlatform[2])
    
    print(f"Script \033[92m{scriptName}\033[0m made global")




def interactiveMode() -> None: #Main function
    scriptName = input("Enter script name: ")
    makeScriptGlobal(scriptName)



if __name__ == "__main__":
    interactiveMode()