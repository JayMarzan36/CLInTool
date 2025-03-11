def getTemplates(type: str) -> list[str]:
    templates = {
        ".sh": ["""
        #!/bin/sh\n

        # Script description: This script does something useful.\n

        # Exit immediately if a command exits with a non-zero status.\n
        set -e\n

        # Treat unset variables as an error when substituting.\n
        set -u\n

        # Stop the script from exiting on errors during pipes.\n
        set -o pipefail\n

        # Define variables\n
        variable1="value1"\n
        variable2="value2"\n

        # Function definitions\n
        function usage {\n
            echo "Usage: $0 [-options]"\n
            echo "  -h: Display help/usage information"\n
            exit 1\n
        }\n

        function cleanup {\n
            # Code to clean up temporary files or resources\n
            echo "Cleaning up..."\n
        }\n

        # Trap signals for cleanup operations\n
        trap cleanup EXIT\n

        # Parse command-line arguments\n
        while getopts ":h" opt; do\n
            case $opt in\n
                h)\n
                    usage\n
                    ;;\n
                \\?)\n
                    echo "Invalid option: -$OPTARG" >&2\n
                    usage\n
                    ;;\n
                :)\n
                    echo "Option -$OPTARG requires an argument." >&2\n
                    usage\n
                    ;;\n
            esac\n
        done\n

        # Main script logic\n
        main() {\n
            echo "Starting script..."\n
            echo "Variable 1: $variable1"\n
            echo "Variable 2: $variable2"\n

            # Your code goes here\n
            echo "Doing something..."\n

            echo "Script finished."\n
        }\n

        # Execute main function\n
        main "$@"\n

    exit 0\n
    """],
        ".bat": "",
    }

    return templates.get(type, ["", ""])