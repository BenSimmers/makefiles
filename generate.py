import os
import re
import sys
from pathlib import Path

def generate_readme(directory: str) -> str:
    """
    Generate a markdown readme file for a project by including introductory text and a list of directories with links.
    """
    # Static introductory content
    intro_content = """# Makefiles

## What is this repository for?

This repository contains various Makefile examples for different programming languages and project setups. It serves as a reference for developers looking to automate common tasks such as building, running, testing, and deploying their applications.

## Something to note
- Feel free to update/contribute to this repository. These are my personal Makefiles that I use in my projects, and I thought it would be a good idea to share them with the community.
- If you do use these Makefiles, please make sure to update the `PROJECT_NAME` variable in the Makefile to match your project name, and please update the configuration to match your project setup.

## Directory List
"""

    dirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

    # Create a list of links to each directory
    links = []
    for d in dirs:
        clean_name = re.sub(r'[^a-zA-Z0-9]', '-', d)
        links.append(f"- [{d}](./{clean_name}/makefile)")

    directory_links = "\n".join(links)
    readme_content = f"{intro_content}\n{directory_links}"

    return readme_content

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generateReadME.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    readme_content = generate_readme(directory)
    with open(os.path.join(directory, "README.md"), "w") as f:
        f.write(readme_content)

    print(f"README.md file generated in {directory} directory.")
    print(readme_content)