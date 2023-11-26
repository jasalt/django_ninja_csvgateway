# Simple API receiving and serving (CSV) files with token authentication

Allows passing CSV files from private server behind firewall to public endpoint accessible by [Grafana Cloud Infinity Data Source](https://grafana.com/grafana/plugins/yesoreyeram-infinity-datasource/) to make it available on a dashboard.

There are probably better ways to do this but it was done partially as an exercise to learn [Django Ninja API Framework](https://django-ninja.dev/) and [Fly.io](https://fly.io/docs/django/getting-started/).

## TODO

- [x] File uploads 
- [x] Token authentication
- [x] Keep token secret
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

Using simplified Dockerfile without PDM, prepare `requirements.txt` with `pdm export > requirements.txt` [(doc)](https://pdm-project.org/latest/usage/advanced/#export-requirementstxt-or-setuppy). Requirements file includes artifact hashes and might not work on other platforms.

Create Fly.io application, set secrets and deploy:

```
fly auth login
fly launch
fly secrets set CSVGATEWAY_TOKEN=XXX
fly secrets set CSVGATEWAY_SECRET_KEY=XXX
fly secrets unset SECRET_KEY  # this was unnecessarily set by launch script ?
fly deploy
```

Then run migrations and create super user via fly shell.

```
fly console --machine <machine_id> -C bash
python manage.py migrate
python manage.py createsuperuser
```


### TODO

- [x] Initial setup
- [x] Add persisting volume for uploads folder https://fly.io/docs/reference/volumes/
- [x] Hide `fly.toml` from repo, keep `fly.toml.example` and change app url to secret.
- [x] Admin CSRF verification fails (allows all from *.fly.dev)
- [ ] CSS fails loading from `/static/` [(see doc)](https://fly.io/django-beats/deploying-django-to-production/#static-files)

### Notes

Some Fly.io Python docs are bit outdated with mentions of `Procfile` etc. Generic `Dockerfile` method and `fly.toml` are used to get Django project running. 

The `fly deploy` command also guesses project to use Poetry (based on `pyproject.toml`?) and creates Poetry boilerplate `Dockerfile` which needs some editing to get it working without Poetry. Following basic `Dockerfile` example from [DjangoX](https://github.com/wsvincent/djangox/tree/main).
