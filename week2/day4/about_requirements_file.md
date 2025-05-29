# About requirements.txt

requirements.txt is a plain text file that lists all the external libraries (and their exact versions) used in a Python project.

It helps recreate the same environment on another system by installing all necessary packages in one step.

## How It's Created

When you go in your project directory, then run this command in command prompt:-

    pip freeze > requirements.txt 
This saves all installed external libraries of that particular project into the file.

## How It's Used

To install everything listed in the file in other machine, for ensuring consistent setup for team members and deployment, 
we could use requirements.txt, we need to run the following command in command prompt:-



To install all the requirements of the project, we use requirements.txt saved. To install all listed packages in a new environment, we use the following command:-

    pip install -r requirements.txt
## Benefit:-
* Ensures consistent setup for team members and deployment
* Makes projects easier to share, deploy, and maintain