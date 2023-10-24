FROM python:3.12-bookworm as python-run-stage

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ Europe/Warsaw
WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  make \
  tzdata \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY ./backend/pyproject.toml ./backend/poetry.lock* ${APP_HOME}/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install

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
CMD /start-prod.sh

FROM python-run-stage as python-run-as-user-stage

ARG USER_ID=0
ENV USER_ID=${USER_ID}

RUN addgroup --system --gid ${USER_ID} django \
    && adduser --system --home /home/django --uid ${USER_ID} --ingroup django django

RUN chown django:django /entrypoint.sh \
    && chown django:django /start-local.sh \
    && chown django:django /start-prod.sh \
    && chown django:django ${APP_HOME}

USER django
