# Demo REST API for testing purposes

Running with [Pipenv](https://pipenv.pypa.io/en/latest/):

```
pipenv shell
pipenv install
python manage.py migrate
python manage.py runserver

```
Explore endpoints defined in `django_ninja_demoapi/urls.py` via interactive OpenAPI/Swagger UI http://127.0.0.1:8000/api/docs.
