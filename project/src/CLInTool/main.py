import argparse

from .projectGen import projectGen 

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI Tool")
    
    subparser = parser.add_subparsers(dest="command")
    
    # projectGen
    projectGenParser = subparser.add_parser("projectGen")
    projectGenParser.add_argument("-n", "--name", help="Project name")
    projectGenParser.add_argument("-l", "--lang", choices=["python", "c", "java"], help="Project language")
    projectGenParser.add_argument("--git", help="Initialize git repository", action="store_true")
    projectGenParser.add_argument("--venv", help="Create virtual environment", action="store_true")
    
    
    
    
    
    args = parser.parse_args()
    
    
    if args.command == "projectGen":
        projectGen.main()
    else:
        parser.print_help()
        
        
        
        
        
        
if __name__ == "__main__":
    main()