Instalation of Django 
-
the commmand used to setup the django  project are:

cmd 1 ) To setup the virtual environment
    
    py -m venv env

use the py -m venv env to create the envirnment inside thee current directoriy

cmd 2 ) To activation of the virtual environment
    
    .\env\scripts\activate

cmd 3 ) To Installation of Django

    pip3 install django
    py -m django version


Starting the new project, create the app, Run the server
- 

cmd 1 ) To Start a new project

    django-admin startproject ......... (project name)

cmd 2 ) To start hte new app

First change the directiory to the app folder. 

    py manage.py startapp ....... (app name)

cmd 3 ) To run the server

    py manage.py runserver



Troubleshooting:
-

1 ) for pproblem you faceto activate the Vietual environment

    Set-ExecutionPolicy Unrestricted -scope currentUser
    
OR

    Set-ExecutionPolicy RemoteSigned