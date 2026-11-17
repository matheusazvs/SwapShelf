
from fastapi.testclient import TestClient

from services.catalog.app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "catalog",
    }


def test_list_items():
    response = client.get("/items")

    assert response.status_code == 200
    assert response.json() == {"items": []}
