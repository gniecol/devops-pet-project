from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "DevOps pet project is running"}

@app.get("/hello")
def read_hello() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}

@app.get("/health")
def read_health() -> dict[str, str]:
    return {"message": "OK"}

@app.get("/version")
def read_version() -> dict[str, str]:
    return {"version": "1.0.0"}