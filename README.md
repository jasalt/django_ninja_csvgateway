# Simple API receiving and serving (CSV) files with token authentication

*Status: code finished, testing in production*

Allows passing CSV files from private server behind firewall to public endpoint accessible by [Grafana Cloud Infinity Data Source](https://grafana.com/grafana/plugins/yesoreyeram-infinity-datasource/) to make it available on a dashboard.

There are probably better ways to do this but it was done partially as an exercise to learn [Django Ninja API Framework](https://django-ninja.dev/) and [Fly.io](https://fly.io/docs/django/getting-started/).

## Usage
Explore endpoints defined in `django_ninja_csvgateway/urls.py` via interactive OpenAPI/Swagger UI at http://127.0.0.1:8000/api/docs.

Data can be uploaded to POST endpoint `/api/upload` and downloaded via GET endpoint `/api/download?file=<FILENAME>`. Both require API_TOKEN header that corresponds to what is set in `.env` or environment. Deploy with HTTPS to keep plaintext token secure (Fly.io example included).

### Curl

Post data (adjust filetype declaration as needed):
```
curl -X 'POST' \
  'https://<YOUR_ADDRESS>/api/upload' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer <API_TOKEN>' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@<FILENAME>;type=text/csv'
```

Get data:
```
curl -X 'GET' \
  'https://<YOUR_ADDRESS>/api/download?file=<FILENAME>' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer <API_TOKEN>'
```

### Grafana Infinity Datasource config (GET)
Method GET, URL `https://<YOUR_ADDRESS>/api/download?file=<FILENAME>`. Filename could also be set as query parameter in UI.

HTTP auth header
- Key: `Authorization`
- Value: `Bearer <API_TOKEN>`

HTTP accept header
- Key: `accept`
- Value: `*/*`

![Screenshot_20231126_193757](https://github.com/jasalt/django_ninja_csvgateway/assets/2306521/0364ddc9-08be-485e-9c2b-1e7a8f7ce70d)


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

Copy `.env.example` to `.env` and customize setting `API_TOKEN` which will be used for authentication.


## Deploying to Fly.io

Using simplified Dockerfile without PDM, prepare `requirements.txt` with `pdm export > requirements.txt` [(doc)](https://pdm-project.org/latest/usage/advanced/#export-requirementstxt-or-setuppy). Requirements file includes artifact hashes and might not work on other platforms.

Create Fly.io application, deploy and set secrets:

```
fly auth login
fly launch
fly deploy
fly secrets set API_TOKEN=XXX
```

Then run migrations and create super user via fly shell.

```
fly ssh console
python manage.py migrate
python manage.py createsuperuser
```

## Notes

The `fly deploy` command guesses project to use Poetry (based on `pyproject.toml`?) and creates Poetry boilerplate `Dockerfile` which needs some editing to get it working without Poetry. Following basic `Dockerfile` example from [DjangoX](https://github.com/wsvincent/djangox/tree/main).


### TODO

- [x] File uploads 
- [x] Token authentication
- [x] Keep token secret
- [x] Deployment [(fly.io doc)](https://fly.io/django-beats/deploying-django-to-production/)
  - [x] Add persisting volume for uploads folder [(fly.io doc)](https://fly.io/docs/reference/volumes/)
  - [x] Hide `fly.toml` from repo, keep `fly.toml.example` and change app url to secret.
  - [x] Admin CSRF verification (allows all from *.fly.dev)
  - [x] Serve static files 

### Improvement ideas

Instead of setting API token as environment variable, it could have a database model, admin management view and read/write permission setting etc. to make this more flexible if needed. 


