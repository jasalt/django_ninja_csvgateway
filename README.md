# Demo REST API for testing purposes

Running with [Pipenv](https://pipenv.pypa.io/en/latest/):

```
pipenv shell
pipenv install
python manage.py migrate
python manage.py runserver

```
Access endpoints (defined in `django_ninja_demoapi/urls.py`) via `http://127.0.0.1:8000/api/<route>`.
