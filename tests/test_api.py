from fastapi.testclient import TestClient
from src.main import app
import pytest

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

@pytest.mark.parametrize(
    "field, value, expected_error",
    [
        ("status_code", 99, "greater_than_equal"),
        ("status_code", 600, "less_than_equal"),
        ("response_time_ms", -150.0, "greater_than_equal"),
        ("retry_count", -1, "greater_than_equal"),
        ("service", "", "string_too_short"),
        ("endpoint", "", "string_too_short"),
    ]
)
def test_receive_event_with_invalid_domain_value(
    field, value, expected_error
):
    payload = {
        "service": "payment-api",
        "endpoint": "/payments",
        "status_code": 200,
        "response_time_ms": 150.0,
        "success": True,
        "retry_count": 0
    }

    payload[field] = value

    response = client.post("/events", json=payload)

    assert response.status_code == 422

    error = response.json()["detail"][0]

    assert error["type"] == expected_error
    assert error["loc"] == ["body", field]
    assert error["input"] == value


@pytest.mark.parametrize(
    "status_code, response_time_ms, retry_count",
    [
        (100, 0.0, 0),
        (599, 0.0, 0),
    ]
)
def test_receive_event_with_valid_boundary_values(
    status_code, response_time_ms, retry_count
):
    payload = {
        "service": "payment-api",
        "endpoint": "/payments",
        "status_code": status_code,
        "response_time_ms": response_time_ms,
        "success": False,
        "retry_count": retry_count
    }

    response = client.post("/events", json=payload)

    assert response.status_code == 200
    assert response.json()["event"] == payload