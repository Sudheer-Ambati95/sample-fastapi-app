from fastapi import FastAPI

from app.routers.health import router
from app.middleware.correlation import CorrelationIdMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="Sample FastAPI App"
)

app.add_middleware(CorrelationIdMiddleware)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "FastAPI Application Running"
    }

Instrumentator().instrument(app).expose(app)
