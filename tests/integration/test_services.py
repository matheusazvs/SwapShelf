
import time

import httpx

CATALOG_URL = "http://localhost:8001"
EXCHANGE_URL = "http://localhost:8002"


def wait_for_service(url):
    for _ in range(15):
        try:
            response = httpx.get(f"{url}/health", timeout=2)
            if response.status_code == 200:
                return
        except httpx.RequestError:
            pass

        time.sleep(2)

    raise RuntimeError(f"Service unavailable: {url}")


def test_catalog_integration():
    wait_for_service(CATALOG_URL)

    response = httpx.get(f"{CATALOG_URL}/items")

    assert response.status_code == 200
    assert response.json() == {"items": []}


def test_exchange_integration():
    wait_for_service(EXCHANGE_URL)

    response = httpx.get(f"{EXCHANGE_URL}/exchanges")

    assert response.status_code == 200
    assert response.json() == {"exchanges": []}
