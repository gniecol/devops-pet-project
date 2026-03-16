from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DevOps pet project is running"}

def test_read_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

def test_read_hello() -> None:
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI"}

def test_read_version() -> None:
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}