# Simple API receiving and serving (CSV) files with token authentication

Allows passing CSV files from private server behind firewall to public endpoint accessible by [Grafana Cloud Infinity Data Source](https://grafana.com/grafana/plugins/yesoreyeram-infinity-datasource/) to make it available on a dashboard.

There are probably better ways to do this but it was done partially as an exercise to learn [Django Ninja API Framework](https://django-ninja.dev/) and [Fly.io](https://fly.io/docs/django/getting-started/).

## TODO

- [x] File uploads 
- [x] Token authentication
- [ ] Keep token secret
- [ ] Deployment

## Local installation

### Pre-requisites

- Python 3.11 (`sudo apt install python`)
- [pipx](https://github.com/pypa/pipx) (`sudo apt install pipx`, `brew install pipx`)
- [PDM](https://pdm-project.org/) (`pipx install pdm`)

### Running with PDM

[PDM](https://pdm-project.org/) is a Python package and virtualenv manager quite similar to [Poetry](https://python-poetry.org/) and [Pipenv](https://pipenv.pypa.io/en/latest/) but has 50% less characters and some other differences.

Create `.venv`, install dependencies, run migrations and start development server with:
```
pdm install
pdm run manage.py migrate
pdm run manage.py runserver
```

Explore endpoints defined in `django_ninja_csvgateway/urls.py` via interactive OpenAPI/Swagger UI at http://127.0.0.1:8000/api/docs.

## Deploying to Fly.io

### TODO

- [ ] Basic setup https://fly.io/docs/django/getting-started/
- [ ] Add persisting volume for uploads folder https://fly.io/docs/reference/volumes/
