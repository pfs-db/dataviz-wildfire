# data-science-viz

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Virtual enviroments

Usage of virtual enviroments to make sure that the project is compatible in every machine.

To create a new virtual enviroment `python -m venv <directory>` In this case it is important to use the naming convention for the directory as .venv or .env. (This folder will be ignore in the .gitignore file).

How to activate the virtual enviroment?

- Windows venv activation:

```
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

- Linux and MacOS venv activation:

```
source myvenv/bin/activate
```

For all platforms it is needed just to call `deactivate` and you are out from this env.

Everytime a package is installed, for example: `pip install numpy`, the requirements.txt file should be updated. To catch up the updated version in a new virtual enviroment you can call `pip install -r requirements.txt` and that is, you project is ready to go.

## Software Requirements

- Python 3.12.2
- anaconda Command line client (version 1.12.3)
- pip 24.0

All the required packages will be listed on the `requirements.txt` file.

## References:

- [Virtual Env](https://python.land/virtual-environments/virtualenv)
