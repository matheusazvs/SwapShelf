
from fastapi.testclient import TestClient

from services.exchange.app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "exchange",
    }


def test_list_exchanges():
    response = client.get("/exchanges")

    assert response.status_code == 200
    assert response.json() == {"exchanges": []}
