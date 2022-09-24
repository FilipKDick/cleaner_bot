ARG PYTHON_VERSION=3.9-slim-bullseye

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

# Python build stage
FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=local

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

# Requirements are installed here to ensure they will be cached.
COPY ./backend/requirements .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt


# Python 'run' stage
FROM python as python-run-stage

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  make \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
	&& rm -rf /wheels/

COPY ./.devops/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./.devops/django/start-local.sh /start-local.sh
RUN sed -i 's/\r$//g' /start-local.sh
RUN chmod +x /start-local.sh

COPY ./.devops/django/start-prod.sh /start-prod.sh
RUN sed -i 's/\r$//g' /start-prod.sh
RUN chmod +x /start-prod.sh


# copy application code to WORKDIR
COPY ./backend ${APP_HOME}

ENTRYPOINT ["/entrypoint.sh"]

FROM python-run-stage as python-run-as-user-stage

ARG USER_ID=0
ENV USER_ID=${USER_ID}

RUN addgroup --system --gid ${USER_ID} django \
    && adduser --system --uid ${USER_ID} --ingroup django django

RUN chown django:django /entrypoint.sh \
    && chown django:django /start-local.sh \
    && chown django:django /start-prod.sh \
    && chown django:django ${APP_HOME}

USER django
