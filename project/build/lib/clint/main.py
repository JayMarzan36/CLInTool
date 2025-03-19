import argparse

from .makeProject import makeProject
from .scripting import makeScript, makeGlobal
from .templateManagement import makeTemplates
from .templateManagement import addTemplate


def main(version :str ="0.5.0") -> None:
    """
    Clint main function
    """
    parser = argparse.ArgumentParser(description="CLI Tool")

    subparser = parser.add_subparsers(dest="command")

    # version
    versionParser = subparser.add_parser("v", help="Show version information")

    # projectGen
    projectGenParser = subparser.add_parser("mp")

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
    scriptGenParser = subparser.add_parser("ms")

    scriptGenParser.add_argument("-n", "--name", help="Script name")

    # makeGlobal
    makeGlobalParser = subparser.add_parser("mg")

    makeGlobalParser.add_argument("-n", "--name", help="Script name")

    # makeTemplates
    makeTemplatesParser = subparser.add_parser("mt")

    makeTemplatesParser.add_argument("-n", "--name", help="Template name")

    makeTemplatesParser.add_argument("-c", "--content", help="Template content")

    makeTemplatesParser.add_argument(
        "-t", "--type", choices=["script", "project"], help="Template type"
    )

    # add Template
    addTemplateParser = subparser.add_parser("at")

    addTemplateParser.add_argument("-n", "--name", help="Template name")

    addTemplateParser.add_argument("-p", "--path", help="Template path")

    addTemplateParser.add_argument(
        "-t", "--type", choices=["script", "project"], help="Template type"
    )

    args = parser.parse_args()

    if args.command == "v":
        print(f"Version {version}")

    elif args.command == "mp":
        if args.name and args.lang:
            makeProject.createProject(args.name, args.lang, args.git, args.venv)

        else:
            makeProject.main()

    elif args.command == "ms":
        if args.name:
            makeScript.scriptGen(args.name)

        else:
            makeScript.interactiveMode()

    elif args.command == "mg":
        if args.name:
            makeGlobal.makeScriptGlobal(args.name)

        else:
            makeGlobal.interactiveMode()

    elif args.command == "mt":
        if args.name and args.content and args.type:
            makeTemplates.makeTemplate(args.name, args.content, args.type)

        else:
            makeTemplates.interactiveMode()

    elif args.command == "at":
        if args.path and args.type and args.name:
            addTemplate(args.name, args.path, args.type)

        else:
            addTemplate.interactiveMode()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
