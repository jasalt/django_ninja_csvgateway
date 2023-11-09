# Demo REST API for testing purposes

Running with [PDM](https://pdm-project.org/) (install with eg. `pipx install pdm`):

```
pdm install
pdm run manage.py migrate
pdm run manage.py runserver
```

Explore endpoints defined in `django_ninja_demoapi/urls.py` via interactive OpenAPI/Swagger UI http://127.0.0.1:8000/api/docs.
