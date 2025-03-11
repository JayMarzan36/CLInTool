import argparse

from .projectGen import projectGen
from .scripting import scriptGen, makeGlobal


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI Tool")

    subparser = parser.add_subparsers(dest="command")

    # projectGen
    projectGenParser = subparser.add_parser("pg")
    projectGenParser.add_argument("-n", "--name", help="Project name")
    projectGenParser.add_argument(
        "-l", "--lang", choices=["python", "c", "java"], help="Project language"
    )
    projectGenParser.add_argument(
        "--git", help="Initialize git repository", action="store_true"
    )
    projectGenParser.add_argument(
        "--venv", help="Create virtual environment", action="store_true"
    )

    # scriptGen
    scriptGenParser = subparser.add_parser("sg")
    scriptGenParser.add_argument("-n", "--name", help="Script name")

    # makeGlobal
    makeGlobalParser = subparser.add_parser("mg")
    makeGlobalParser.add_argument("-n", "--name", help="Script name")

    args = parser.parse_args()

    if args.command == "pg":
        if args.name and args.lang:
            projectGen.createProject(args.name, args.lang, args.git, args.venv)
        else:
            projectGen.main()

    elif args.command == "sg":
        if args.name:
            scriptGen.scriptGen(args.name)
        else:
            scriptGen.interactiveMode()

    elif args.command == "mg":
        if args.name:
            makeGlobal.makeScriptGlobal(args.name)
        else:
            makeGlobal.interactiveMode()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
