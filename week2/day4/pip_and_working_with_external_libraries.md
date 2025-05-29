# pip and working with external libraries

## pip:-

pip stands for “Pip Installs Packages.”
It is the official package manager for Python.

With pip, you can:
* Download and install third-party Python libraries (like numpy, requests, flask)

* Upgrade or uninstall packages

* Save and manage dependencies in a project

## External libraries:-

External libraries (also called third-party packages) are ready-made bundles of Python code created by others, which you can install and use in your own projects.

They extend Python’s capabilities beyond the built-in features.
example:- matplotlib, numpy, django, etc.

**Note:- These external libraries have to be installed in the project' virtual machine using pip.**

### Why Use External Libraries?
These libraries:
* Save time
* Are well-tested
* Offer specialized functionality (e.g., data science, web development, APIs)

## Working of pip with external libraries

1. ### check if pip is installed:-

open cmd and run command:-

_pip --version_

if version is displayed, then pip is already installed,
else use this command:-  
       
          python -m ensurepip --upgrade

Note:- Once, pip is installed, using pip we install the external libraries in our virtual environments

2. ### installing external libraries:-

To install external libraries, we use following command in the command prompt:-

          pip install <external_library>

e.g.;
            
          pip install requests

3. ### using external libraries:-

import the external library

Now you can use functions/classes from the library using library_name.function()

e.g,; requests.get("https://www.example.com")

4. #### uninstalling an external library:-
use this command:-

         pip uninstall requests

5. ### listing all installed external libraries:-
 To do so, use the following command in the command prompt:-

          pip list
6. ### upgrading an external library:-
 To upgrade an external library, use the following command in the command prompt:-
          
         pip install --upgrade package_name

