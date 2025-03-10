from fastapi.testclient import TestClient

from app import crud
from app.main import app

client = TestClient(app)


def test_fetch_wallet_info():
    """Тестирует получение информации о кошельке через POST-запрос."""
    response = client.post(
        "/wallet", json={"address": "TE2RzoSV3wFK99w6J9UnnZ4vLfXYoxvRwP"}
    )
    assert response.status_code == 200
    assert "balance" in response.json()


def test_create_wallet_request(db):
    """Тестирует создание нового запроса на кошелек в базе данных."""
    wallet = crud.create_wallet_request(db, "TEST_ADDRESS")
    assert wallet.wallet_address == "TEST_ADDRESS"
