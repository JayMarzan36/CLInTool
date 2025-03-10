import argparse

from .projectGen import projectGen
from .scripting import scriptGen, makeGlobal

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI Tool")
    
    subparser = parser.add_subparsers(dest="command")
    
    # projectGen
    projectGenParser = subparser.add_parser("projectGen")
    projectGenParser.add_argument("-n", "--name", help="Project name")
    projectGenParser.add_argument("-l", "--lang", choices=["python", "c", "java"], help="Project language")
    projectGenParser.add_argument("--git", help="Initialize git repository", action="store_true")
    projectGenParser.add_argument("--venv", help="Create virtual environment", action="store_true")
    
    # scriptGen
    scriptGenParser = subparser.add_parser("scriptGen")
    scriptGenParser.add_argument("-n", "--name", help="Script name")
    
    
    # makeGlobal
    makeGlobalParser = subparser.add_parser("makeGlobal")
    makeGlobalParser.add_argument("-n", "--name", help="Script name")
    
    
    
    
    
    args = parser.parse_args()
    
    
    if args.command == "projectGen":
        projectGen.main()
    elif args.command == "scriptGen":
        if args.name:
            scriptGen.scriptGen(args.name)
        else:
            scriptGen.interactiveMode()
    elif args.command == "makeGlobal":
        if args.name:
            makeGlobal.makeScriptGlobal(args.name)
        else:
            makeGlobal.interactiveMode()
    else:
        parser.print_help()
        
        
        
        
        
        
if __name__ == "__main__":
    main()