import os
import redis
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

cache = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

Instrumentator().instrument(app).expose(app)


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

@app.get("/redis-health")
def read_redis_health() -> dict[str, str]:
    try:
        cache.ping()
        return {"redis_status": "ok"}
    except redis.RedisError:
        return {"redis_status": "error"}

@app.post("/notes/{note}")
def create_note(note: str) -> dict[str, str]:
    cache.rpush("notes", note)
    return {"message": f"Note '{note}' added successfully"}

@app.get("/notes")
def read_notes() -> dict[str, list[str]]:
    notes= cache.lrange("notes", 0, -1)
    return {"notes": notes}

@app.delete("/notes")
def delete_notes() -> dict[str, str]:
    cache.delete("notes")
    return {"message": "Notes deleted successfully"}