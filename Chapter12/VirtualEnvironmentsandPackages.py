#In python we can create virtual environments. In which a copy of python Interpreter, Standart Library and various supported file...
# we can install different packages for some app's functionality in that vitual environment

# there are 4 steps to create and manage virtaul Environments

# STEP 1 - Creating a virtual environment in shell terminal we use venv module...A common directory location for a virtual environment is .venv
# python3 -m venv tutorial-env


# STEP 2 - Activating the virtual environment
# On Windows, run:
# tutorial-env\Scripts\activate.bat

# On Unix or MacOS, run:
# source tutorial-env/bin/activate


# STEP 3 -install specific package using "pip"
"""
# You can install, upgrade, and remove packages using a program called pip.
# By default pip will install packages from the Python Package Index, <https://pypi.org>.
# pip has a number of subcommands: “install”, “uninstall”, “freeze”, etc.
# (tutorial-env) $ python -m pip install novas

# You can also install a specific version of a package by giving the package name followed by == and the version number:
# (tutorial-env) $ python -m pip install requests==2.6.0
# If you re-run this command, pip will notice that the requested version is already installed and do nothing.
# we can use pip install --update requests to update package to latest version.

# pip uninstall - followed by one or more package names will remove the packages from the virtual environment.

# pip show - will display information about a particular package

# pip list - will display all of the packages installed in the virtual environment:
"""

# pip freeze will produce a similar list of the installed packages, but the output uses the format that pip install expects. A common convention is to put this list in a requirements.txt file

# (tutorial-env) $ pip freeze > requirements.txt

# requirements.txt file will look like this
# novas==3.1.1.3
# numpy==1.9.2
# requests==2.7.0


# The requirements.txt can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with install -r:

#this command will install all the packages in the requirements.txt
# (tutorial-env) $ python -m pip install -r requirements.txt
