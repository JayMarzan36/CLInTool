import json, os




TEMPLATESPATH = os.path.join(os.path.dirname(__file__), "templates")
projectType = "python"

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

print(loadTemplate(projectType))
for i in loadTemplate(projectType):
    print(f"File: {i}")
    print(f"Content: {loadTemplate(projectType)[i]}")
    print("\n") 