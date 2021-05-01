# OYSTAR RELOADED #
Welcome to Oystar Reloaded! To run this project:

## External Requirements: ##
1. Docker Desktop: https://www.docker.com/products/docker-desktop
 Note that Windows and Linux users require a separate distribution.

2. Install PostGresSQL: https://www.postgresql.org/download/

3. Download this repo to desktop: 

## How to Run ##
### Create Virtual Env ###
Make sure Python3 is installed on your base machine.

```bash
    python3 -m pip install --user virtualenv
```
   
This command installs the Python virtual env. After this, change directories into your oystar repo.
Create a
virtual env with a name of your choice by replacing the word 'env' with
whatever name you want in the next command.
```bash
    python3 -m venv env
```
After creating the virtual environment, activate it using the following command:
```bash
    source env/bin/activate
```
You will know your virtual environment is running if the name of the virtual environment appears before your system username in terminal.
To leave this virtual environment (to be done AFTER development), just run:
```bash
    deactivate
```
You will be able to activate your virtual environment from the same project directory next time you so wish. Note that Windows users will
require different commands: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

### Run the Application ###

To run initial setup using Docker, run the following command:
```bash
    make build
```
This command will install all development and production requirements. It will also migrate models to the database. After running this command,
start the Docker server using the following command:
```bash
    make compose-start
```
This server can be exited at any time using CTRL-C. If you get an error that processes are already running on servers at any point during attempted startup, try the following command to kill Docker port processes:
```bash
    make compose-stop
```
To run any Django or Python-related command inside the Docker container, run the following command:
```bash
    make compose-manage-py "command"
```











