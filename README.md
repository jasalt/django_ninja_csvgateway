# Demo REST API for testing purposes

## Pre-requirements
Mainly tested on Debian, Mac instructions may not be up to date.

- Python 3.11 `sudo apt install python` / `brew install python`
- [pipx](https://github.com/pypa/pipx) `sudo apt install pipx` / `brew install pipx`
- [PDM](https://pdm-project.org/) `pipx install pdm`

## Running
PDM manages virtualenv at .venv and installs dependencies via Pip. Difference from poetry, pipenv or using plain virtualenv is that it does not require activating the virtualenv as a subshell every time. If subshell is needed it [can be activated](https://pdm-project.org/latest/usage/venv/#activate-a-virtualenv) via `eval $(pdm venv activate)` (bash) or `pdm venv activate` (zsh).

```
pdm install
pdm run manage.py migrate
pdm run manage.py runserver
```

Explore endpoints defined in `django_ninja_demoapi/urls.py` via interactive OpenAPI/Swagger UI http://127.0.0.1:8000/api/docs.
