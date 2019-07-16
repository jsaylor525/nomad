# Nomad Workout Tracker

Are you tired of having to pay for a good a workout tracker? Or maybe you're tired of having to export and import all of your workout data when you switch to a new gym? If so Nomad Workout Tracker is the solution you've been craving. We a delivering an application that will allow the community to track their workouts individual, compare their results with others, and take this platform with them to whatever gym they want.

Users will be able to create there own groups and invite friends to share workout journals.

# Developing

Right now the project is in the prototyping phase. It is recommended that you use Anaconda to contain you python environment so that dependencies don't clash.

## Prerequisites

* [Anaconda](https://conda.io/docs/_downloads/conda-cheatsheet.pdf)
* git
* [Visual Studio Code](https://code.visualstudio.com/)

## Setup

I've played with Windows 10, Ubuntu 18.04, and MacOS Mojave at the early stages, likely as this project develops all the OS types listed won't work... We're real developers so expect to use Linux ;)

### Environment

Hopefully you read the above and install conda... here's the [cheat-sheet](https://conda.io/docs/_downloads/conda-cheatsheet.pdf)

```bash
conda create -y --name nomad python=3.7
conda activate nomad
pip install - requirements.txt
```

### Website Learning History (Notes)

Django Setups for initial creation.

1. Create the project.
   ```bash
   django-admin startproject nomad
   ```
2. change into the created project directory and test that the project was created successfully.
   ```bash
   cd .\nomad\
   python manage.py runserver
   ```
3. Create a application.
   ```bash
   python .\manage.py startapp clock
   ```
4. Setup Clock For initial integration.
   1. Add a default view in clock/view.py
   2. Create a file clock/url.py and add the url definition.
   3. Connect the nomad/url.py with the clock/url.py
      1. Also give the base "" a page to load
5. Check the server again, fix any issues.
6. Create database.
   ```bash
   python manage.py migrate
   ```
# Development Folders/Files

| Folder / Filename | Description |
|--|--|
| run.py	| This is the file that is invoked to start up a development server. It gets a copy of the app from your package and runs it. This won’t be used in production, but it will see a lot of mileage in development. |
| requirements.txt |	This file lists all of the Python packages that your app depends on. You may have separate files for production and development dependencies. |
| config.py	| This file contains most of the configuration variables that your app needs. |
| /instance/config.py | This file contains configuration variables that shouldn’t be in version control. This includes things like API keys and database URIs containing passwords. This also contains variables that are specific to this particular instance of your application. For example, you might have DEBUG = False in config.py, but set DEBUG = True in instance/config.py on your local machine for development. Since this file will be read in after config.py, it will override it and set DEBUG = True. |
| /nomad/	| This is the package that contains your application.
/nomad/\_\_init\_\_.py | This file initializes your application and brings together all of the various components. |
| /nomad/views.py | This is where the routes are defined. It may be split into a package of its own (nomad/views/) with related views grouped together into modules. |
| /nomad/models.py | This is where you define the models of your application. This may be split into several modules in the same way as views.py. |
| /nomad/static/ | This directory contains the public CSS, JavaScript, images and other files that you want to make public via your app. It is accessible from nomad.com/static/ by default. |
| /nomad/templates/ | This is where you’ll put the Jinja2 templates for your app. |