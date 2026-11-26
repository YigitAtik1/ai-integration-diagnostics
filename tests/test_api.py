from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_receive_valid_event():
    payload = {
        "service": "payment-api",
        "endpoint": "/payments",
        "status_code": 200,
        "response_time_ms": 150,
        "success": True,
        "retry_count": 0
    }

    response = client.post("/events", json=payload)

    assert response.status_code == 200
    assert response.json()["message"] == "Event Received"
    assert response.json()["event"] == payload


def test_receive_invalid_event():
    payload = {
            "service": "payment-api",
            "endpoint": "/payments",
            "status_code": "banana",
            "response_time_ms": 150,
            "success": True,
            "retry_count": 0
        }

    response = client.post("/events", json=payload)
    assert response.status_code == 422

    error = response.json()["detail"][0]

    assert error["type"] == "int_parsing"
    assert error["loc"] == ["body", "status_code"]
    assert error["input"] == "banana"

def test_receive_event_with_missing_field():
    payload = {
            "service": "payment-api",
            "endpoint": "/payments",
            "response_time_ms": 150,
            "success": True,
            "retry_count": 0
    }

    response = client.post("/events", json=payload)
    assert response.status_code == 422
    error = response.json()["detail"][0]
    assert error["type"] == "missing"
    assert error["loc"] == ["body", "status_code"]