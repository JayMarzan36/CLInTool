import os, json


class Template:
    def __init__(self, path):
        self.path = path

        with open(self.path, "r") as f:
            self.template = json.load(f)

        self.keyWords = {
            "file": ["fileName", "content"],
            "dir": ["dirName", "dirContents"],
        }

    def printTemplate(self):
        print(self.template)

    def templateGet(self, name: str):

        return self.template.get(name)

    def visulizeTemplate(self):
        def printNested(item, level=0):
            indent = "  " * level
            if isinstance(item, dict):
                for key, value in item.items():
                    print(f"{indent}{key}:")
                    printNested(value, level + 1)
            elif isinstance(item, list):
                for value in item:
                    printNested(value, level + 1)
            else:
                print(f"{indent}{item}")

        printNested(self.template)

    def makeFromTemplate(self):
        data = self.template

        def makeStruct(data, parentPath=""):
            if isinstance(data, dict):
                currentPath = parentPath
                for key, value in data.items():
                    if key == "dir":
                        for item in value:
                            if "dirName" in item:
                                print(f"Making Dir: {item["dirName"]}")
                                dirPath = os.path.join(currentPath, item["dirName"])
                                os.makedirs(dirPath, exist_ok=True)
                                makeStruct(item, dirPath)  # Pass the new directory path
                            elif "dirContents" in item:
                                makeStruct(item["dirContents"], dirPath)
                    elif key == "file":
                        prevFile = None
                        for item in value:
                            if "fileName" in item:
                                print(f"Making File in: {currentPath}")
                                filePath = os.path.join(currentPath, item["fileName"])
                                prevFile = filePath
                                with open(filePath, "w") as f:
                                    pass
                            elif "content" in item:
                                print(f"Writing File: {prevFile}")
                                if prevFile is None:
                                    continue
                                if os.path.exists(item["content"]):
                                    print(f"Using file for {prevFile} content")
                                    with open(item["content"], "r") as f:
                                        content = f.read()
                                    with open(prevFile, "w") as f:
                                        f.write(content)
                                else:
                                    with open(prevFile, "w") as f:
                                        f.write(item["content"])
                    else:
                        makeStruct(value, currentPath)

            elif isinstance(data, list):
                for item in data:
                    makeStruct(item, parentPath)

        makeStruct(data)
        print("Created Directory with following structure")

        self.visulizeTemplate()


if __name__ == "__main__":
    template = Template(path="python-web-react.json")
    template.makeFromTemplate()
