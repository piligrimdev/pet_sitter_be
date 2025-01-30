FROM python:3.12-slim AS builder
# Установка зависимостей

ENV PATH="/root/.local/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl && rm -rf /var/lib/apt/lists/*

# установка poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && poetry --version

WORKDIR /home/app

COPY poetry.lock pyproject.toml /home/app/

# установка зависимостей через poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

WORKDIR /home/app/web

COPY web ./
