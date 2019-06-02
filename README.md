# THPWD06 - Mineral Catalog

This is the sixth project to team tree house's Python Web Tech Degree.

## Goal
- Build a website that displays information about various minerals

## Deliverables / Objectives
1. Create home page that lists all of minerals in database.
2. Create a detail page that displays information about mineral.

## Steps to Running/Exiting the Program
1. Install pipenv by typing `pip install pipenv` or `pip3 install pipenv` for python3 users
2. In project root folder, install dependencies by typing `pipenv install`
3. In project root folder, enter virtual environment by typing `pipenv shell`
4. In `mineral_catalog` of project root folder of virtual environment, run `python manage.py migrate website`
5. In project root folder of virtual environment, run  by typing `python manage.py runserver`
6. Open chrome and enter given url (i.e. `http://127.0.0.1:8000/`)
7. Once done, exit django by pressing `Ctrl`+`z` and virtual environment by typing `exit`

## FAQ
1. Q: How would a user know which version of python is installed as default?
    - A: Python version can be found by typing `python --version` in terminal. If X in `X.*.*` is 2, then python 2 is installed as default, and if it's 3, then python 3 is being used as default.