############################
# Build Stage
############################

FROM python:3.11-slim AS builder

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-dev

COPY . .

############################
# Runtime Stage
############################

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder \
/usr/local/lib/python3.11/site-packages \
/usr/local/lib/python3.11/site-packages

COPY . .

CMD [
  "uvicorn",
  "app.main:app",
  "--host",
  "0.0.0.0",
  "--port",
  "8080"
]
