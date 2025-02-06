# pythonportfolio

# Django Project Setup with Pipenv

This guide walks you through setting up a Django project using **Pipenv** for managing your dependencies in a virtual environment.

## Prerequisites

Make sure you have the following installed on your system:

- **Python** (version 3.6 or higher): [Download Python](https://www.python.org/downloads/)
- **Pip** (Python's package installer): [Install pip](https://pip.pypa.io/en/stable/installation/)
- **Pipenv**: A tool for managing Python dependencies in isolated environments.

## 1. Install Pipenv

If you haven't installed **Pipenv** already, you can install it globally using **pip**:

```bash
pip install pipenv
```

## 2. Create a Virtual Environment

Navigate to your project folder (or create a new one) and create a Pipenv environment for managing your dependencies.

```bash
mkdir my-django-project
cd my-django-project
pipenv install
```

This will create a virtual environment and a Pipfile in your project directory.

## 3. Install Django

To install Django in the Pipenv virtual environment, use the following command:
```bash
pipenv install django
```

This will install the latest version of Django and add it to your Pipfile


## 4. Start a New Django Project

Once Django is installed, you can start a new Django project using the django-admin tool. Replace myproject with your desired project name:

```bash
pipenv run django-admin startproject myproject
cd myproject
```
This creates a new Django project with a basic structure.

## 5. Set Up the Database

Before you can start the development server, you need to apply the initial migrations. Run the following command to set up the database:

```bash
pipenv run python manage.py migrate
```

This will create the necessary database tables for your Django project.

## 6. Create a Superuser

To access the Django admin panel, you'll need to create a superuser. Run the following command and follow the prompts:

```bash
pipenv run python manage.py createsuperuser
```

This will allow you to create a user with admin privileges for logging into the Django admin interface.

## 7. Run the Django Development Server

Start the development server using:

```bash
pipenv run python manage.py runserver
```

You should now be able to access your Django application by navigating to:
``` bash
http://127.0.0.1:8000/
```
And the admin interface can be accessed at:
```bash
http://127.0.0.1:8000/admin
```
Log in with the superuser credentials you created earlier.

## 8. Deactivate the Virtual Environment

Once you’re done working, you can deactivate the virtual environment by running:

```bash
exit
```
This will return you to your system's global Python environment.

## 9. Install Dependencies from Pipfile

If you're working on this project with others or you need to set up the environment again, you can install all the dependencies specified in the Pipfile by running:

```bash
pipenv install
```
This will recreate the virtual environment and install all the necessary dependencies.

## Command lines

To access the pip env
```bash
pipenv shell
```

To access django shell
```bash
pipenv shell
python manage.py shell
```

To build datastructure from django shell
```bash
# import the data
from main.models import ToDoList
m = dataModel.objects.all() # to get all
m.get(id=1) # get dataModel with id = 1 function will throw exception if not found
m.filter(id=1) # get datamodel with id=1
# m.item_set.all() queryset from model ie.
# m({'item': 'new', 'bool':False }) create new object - make sure variables/fields exists when creating models in models.py
# m.save() save the new object
dataModel.objects.get(id=1).item_set.create(text='javascript', complete=True) # create new item set
# dataModel.objects.get(id=1).delete()  delete object
```

When updating the database make sure to makemigrations then migrate
```bash
python manage.py makemigrations name-ofapp
python manage.py migrate
python manage.py showmigrations # debugging
```

To create new app on pipenv shell
```bash
python manage.py startapp nameofapp
# add new app to settings.py installed apps
# add url to urls.py ie path('nameofapp', views.newapp, name='newapp')
```

To register data models onto the admin panel
```bash
# In admin.py register
admin.site.register(ToDoList)
```

---
## Additional Resources

[Django Documentation](https://docs.djangoproject.com/en/5.1/)
[Pipenv Documentation](https://pipenv.pypa.io/en/latest/dev/contributing.html#documentation-contributions)
[Bootstrap Documentation](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

### Key Sections:
- **Prerequisites**: Lists software needed (Python, Pip, Pipenv).
- **Install Pipenv**: Instructions for installing **Pipenv** globally.
- **Create Virtual Environment**: Setting up the environment for managing dependencies.
- **Install Django**: Installing Django inside the virtual environment.
- **Django Project Setup**: How to start a new Django project.
- **Database Setup**: Run migrations to set up the database.
- **Create Superuser**: Guide for creating an admin user.
- **Running the Server**: Start the development server and access the app/admin interface.
- **Deactivating the Environment**: How to exit the virtual environment.
- **Installing Dependencies**: How to install all project dependencies from the `Pipfile`.

