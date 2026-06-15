from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/readiness")
def readiness():
    return {
        "status": "ready"
    }


@router.get("/liveness")
def liveness():
    return {
        "status": "alive"
    }


@router.get("/info")
def info():
    return {
        "application": "sample-fastapi-app"
    }


@router.get("/version")
def version():
    return {
        "version": "1.0.0"
    }
