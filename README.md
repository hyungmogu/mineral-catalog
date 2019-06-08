# THPWD06 - Mineral Catalog

This is the sixth project to team tree house's Python Web Tech Degree.

## Goal
- Build a website that displays information about various minerals

## Deliverables / Objectives
1. Create home page that lists all of minerals in database.
2. Create a detail page that displays information about mineral.

## Steps to accessing admin panel
1. Once the server is running, type `http://127.0.0.1:8000/admin` in a web browser
2. Log into the panel with account registered in `step 5` below

## Steps to Running/Exiting the Program
1. Install pipenv by typing `pip install pipenv` or `pip3 install pipenv` for python3 users
2. In project root folder, install dependencies by typing `pipenv install`
3. In project root folder, enter virtual environment by typing `pipenv shell`
4. In `mineral_catalog` of project root folder, run `python manage.py migrate` or `python3 manage.py migrate` for python3 users.
5. In `mineral_catalog` of project root folder, run `python manage.py createsuperuser` or `python3 manage.py createsuperuser` to create an admin
6. In `mineral_catalog` of project root folder, run `python manage.py loaddata minerals.json` or `python3 manage.py loaddata minerals.json` to pre-populate data
7. In `mineral_catalog` of project root folder, run by typing `python manage.py runserver` or `python3 manage.py runserver` for python3 users.
8. Open chrome and enter given url (i.e. `http://127.0.0.1:8000/`)
9. Once done, exit django by pressing `Ctrl`+`C` and virtual environment by typing `exit`

## FAQ
1. Q: How would a user know which version of python is installed as default?
    - A: Python version can be found by typing `python --version` in terminal. If X in `X.*.*` is 2, then python 2 is installed as default, and if it's 3, then python 3 is being used as default.