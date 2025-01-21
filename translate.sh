

#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 -l <language string> -t <text string>"
    exit 1
}

# Initialize variables
language=""
text=""

# Parse command-line arguments
while getopts "l:t:" opt; do
    case "$opt" in
        l) language="$OPTARG" ;;
        t) text="$OPTARG" ;;
        *) usage ;;
    esac
done

# Check if both arguments are provided
if [[ -z "$language" || -z "$text" ]]; then
    usage
fi

# Command to run using the arguments
echo "Running command with -l '$language' and -t '$text'"
# Replace the following line with your actual command
docker run -v $(pwd)/output:/app/output -it sidneysee/just-translate:latest -l "$language" -t "$text"
