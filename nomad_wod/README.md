# NOMAD WOD

The normal Django workflow, as it is described in the official Django tutorial 
starts a project with the command:

```cmd
$ django-admin startproject [projectname]
```

Your project will look like this:

```txt
[projectname]/
├── [projectname]/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

However, the startproject-command takes an optional argument template which can 
be used to specify a project template to be used for project creation (see 
[Django documentation](https://docs.djangoproject.com/en/1.11/ref/django-admin/#startproject).

The template-argument works with paths on your local machine, but also supports 
URLs. 
So you can easily fetch this skeleton from GitHub using this command:

```cmd
$ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/development.zip [projectname]
```
