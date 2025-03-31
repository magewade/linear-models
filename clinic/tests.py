from fastapi.testclient import TestClient
from main import app
import time


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_post():
    response = client.post("/post")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and data["id"] == 1
    assert "timestamp" in data and isinstance(data["timestamp"], int)
    assert data["timestamp"] <= int(time.time())


def test_create_dog():
    response = client.post("/dog", json={"name": "Buddy", "kind": "terrier", "pk": 0})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Buddy"
    assert data["kind"] == "terrier"
    assert "pk" in data


def test_get_dogs():
    response = client.get("/dog")
    assert response.status_code == 200
    dogs = response.json()
    assert isinstance(dogs, list)
    assert len(dogs) > 0


def test_get_dog_by_pk():
    response = client.get("/dog/1")
    assert response.status_code == 200
    data = response.json()
    assert data["pk"] == 1
    assert data["name"] == "Buddy"


def test_update_dog():
    response = client.patch(
        "/dog/1", json={"name": "Charlie", "kind": "bulldog", "pk": 1}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["pk"] == 1
    assert data["name"] == "Charlie"
    assert data["kind"] == "bulldog"
