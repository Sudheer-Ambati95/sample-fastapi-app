import os

APP_NAME = os.getenv("APP_NAME", "sample-fastapi-app")

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")

VERSION = os.getenv("VERSION", "1.0.0")

BUILD = os.getenv("BUILD", "local")
