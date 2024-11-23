# automatic-git-cloner
Quick script to automatically clone projects to a specified location

I clone repositories from github a lot to a specific folder on my computer. I got tired of typing the same command over and over again, so I made this script to do it for me.
The only prompt from the user is the GitHub repository URL.

It creates a folder at a specified path (specified in the `.env` file), and just uses the `git clone` command.

The cloner.py file is run with a .bat file on Windows. Feel free to make a .sh file for Linux or MacOS.

## Installation
1. Clone the repository
2. Create a virtual environment
3. Activate the virtual environment
4. `pip install .`
5. Create a `.env` file in the root of the project and add the following:
FOLDER_PATH="[specific folder path to clone repos to]"
6. (Optional) Create a shortcut to `clone_repo.bat` in your Start Menu (Windows):
    - Right-click on `clone_repo.bat` and select "Create shortcut"
    - Move it into the following location: C:\Users\[YourUsername]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
    - or Desktop: C:\Users\[YourUsername]\Desktop

## Usage
1. Run `clone_repo.bat`
2. Enter the GitHub repository URL when prompted
3. The repository will be cloned to the folder specified in the `.env` file
