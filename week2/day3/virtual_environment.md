# What is a Virtual Environment?

A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

Think of a virtual environment as a separate container for each Python project. Each container:

* Has its own Python interpreter
* Has its own set of installed packages
* Is isolated from other virtual environments
* Can have different versions of the same package

Using virtual environments is important because:

* It prevents package version conflicts between projects
* Makes projects more portable and reproducible
* Keeps your system Python installation clean
* Allows testing with different Python versions


## Create a Virtual Environment
Python has the built-in venv module for creating virtual environments.

Run this command in terminal/ command prompt:-

_python -m venv myenv_

This creates a folder named myenv in the current directory and virtual environment gets created.

## Activate the Virtual Environment

Run this command in terminal/ command prompt:-

_myenv\Scripts\activate_

This command will activate the created virtual environment, then you’ll see (myenv) at the start of the command line prompt.

## Installing packages in virtual environment
Once your virtual environment is activated, you can install python packages inside this isolated environment, using pip.
All packages are installed in myenv, not globally.

##  Deactivate the Environment

Once you're done, deactivate the virtual environment:
run this command in terminal/ command prompt:-

_deactivate_

Your terminal will return to normal (no more (myenv)).