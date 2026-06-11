from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI running successfully"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
