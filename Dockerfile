FROM python:3.11-slim-bookworm

# Set env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code


### Start WIP section

# This came from `fly launch`
# RUN pip install poetry
# COPY pyproject.toml poetry.lock /code/
# RUN poetry config virtualenvs.create false
# RUN poetry install --only main --no-root --no-interaction

# This is WIP attempt to convert to pdm
# RUN pip install pdm
# COPY pyproject.toml pdm.lock /code/
# RUN pdm install

# TODO https://pdm-project.org/latest/usage/advanced/#use-pdm-in-a-multi-stage-dockerfile

### End WIP section


# Run simply using requirements.txt
# Created with `pdm export > requirements.txt`

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    apt update && \
    apt -y install git ffmpeg black && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code/

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "django_ninja_csvgateway.wsgi"]
