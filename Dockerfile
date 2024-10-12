FROM python:3.12-slim

WORKDIR /app

RUN apt-get upgrade\
    && apt-get -y update\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH="./src"

RUN adduser --disabled-password --gecos '' user\
    && chmod -R 777 /app

USER user

HEALTHCHECK CMD "/bin/sh -c python --version"

CMD ["sh"]