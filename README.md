# Searching_Application_using_algorithms
This project is developed using "Django Rest Framework". It's a searching application where the input list will be sorted in descending order using "Minheap" and then search element using "Binary Search" algorithm. 

# Token Based Authentication is used...
- Superadmin: admin
- password: admin
- Token: 607fe44c83bafbdc9fdc3fa4830f35eba4617771
#
- user: faria
- password: @/./+/-/_only.
- Token: 10a06a572bb31404bfa1786843d675494a9cc0c6
#
# Dockerized the application: https://github.com/noshinfaria/Searching_Application_using_algorithms/blob/main/Ami_Coding_Pari_Na/Dockerfile
# Requirement.txt file is included: https://github.com/noshinfaria/Searching_Application_using_algorithms/blob/main/Ami_Coding_Pari_Na/requirements.txt


# Operators:
- Sorting: Minheap
- Searching: Binary Search


## URLS:

- Signup: http://127.0.0.1:8000/account/signup/
- Login: http://127.0.0.1:8000/account/login/
- Search API: http://127.0.0.1:8000/searchapp/search/
- Get Data API: http://127.0.0.1:8000/searchapp/listview/

# Server run:

    - command: python manage.py runserver `127.0.0.1:8000`

## Commands
Without Docker file:
- python -m pip install -r requirements.txt
- python version: ```3.8.5```
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver


With Docker file:
- docker-compose build
- docker-compose up


```
Django==3.2.5
gunicorn==20.0.4
djangorestframework==3.14.0
tzdata==2022.7
urllib3==1.26.13
Werkzeug==2.2.2
wrapt==1.14.1
zipp==3.11.0

```
