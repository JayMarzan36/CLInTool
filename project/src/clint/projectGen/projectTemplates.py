def getTemplates(lang : str) -> list[str]:
    templates = {
        "python": {
            "mainFile": "main.py",
            "mainFileContent": "def main() -> None:\n   pass\n\nif __name__ == '__main__':\n    main()",
            "additionalFiles": ["requirements.txt"],
            "additionalFilesContent": "Project requirements",
        },
        "c": {
            "mainFile": "main.c",
            "mainFileContent": "#include <stdio.h>\n\nint main() {\n    return 0;\n}",
            "additionalFiles": ["requirements.txt"],
            "additionalFilesContent": "Project requirements",
        },
        "java": {
            "mainFile": "Main.java",
            "mainFileContent": "public class Main {\n  public static void main(String[] args) {\n  System.out.println('hello world');\n    }\n}",
            "additionalFiles": ["requirements.txt"],
            "additionalFilesContent": ["Project requirements"],
        },
    }
    
    return templates.get(lang, None)