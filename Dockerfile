# Official python image
FROM python:3.10-alpine3.17 AS builder

# Labels
LABEL maintainer="andrei.torres@ontariotechu.net"

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Define GEN's home directory
# If you change this value you will also need to update nginx default.conf
ENV GEN_HOME=/gen

# Copy project requirements file
COPY app/requirements.txt $GEN_HOME/app/requirements.txt

## Install packages, create virtualenv, and install dependencies
RUN set -ex \
    && apk add --no-cache ffmpeg libmagic gettext \
    && apk add --no-cache --virtual .build-deps python3-dev postgresql-dev gcc make libc-dev zlib-dev jpeg-dev libffi-dev freetype-dev \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip setuptools wheel\
    && /env/bin/pip install --no-cache-dir -r $GEN_HOME/app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

# Copy project
ADD app $GEN_HOME/app

FROM python:3.10-alpine3.17

# Create user that will run the project
RUN addgroup -S gen --gid 1000 \
    && adduser -S -G gen -h /gen --uid 1000 -D gen

RUN set -ex \
    && apk update \
    && apk add --no-cache ffmpeg libmagic gettext libpq \
    && apk upgrade

USER gen

ENV GEN_HOME=/gen

COPY --chown=gen:gen --from=builder ${GEN_HOME} ${GEN_HOME}

COPY --chown=gen:gen --from=builder /env /env

# Create django's static and media directories
RUN install -d -o gen -g gen $GEN_HOME/media
RUN install -d -o gen -g gen $GEN_HOME/static

# Change to the directory containing manage.py for running Django commands
WORKDIR $GEN_HOME/app

# Add virtualenv to path
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Create volumes
# VOLUME [ "/gen/static", "/gen/media" ]

# Compile language files
#RUN python manage.py compilemessages

# Set communication port
EXPOSE 8000

CMD gunicorn GEN.asgi:application --bind :8000 --workers $GUNICORN_WORKERS --worker-class uvicorn.workers.UvicornWorker --worker-tmp-dir /dev/shm --timeout $GUNICORN_TIMEOUT --log-level $GUNICORN_LOGLEVEL
