from src.models import IntegrationEvent
from src.diagnostics import diagnose_event


def test_diagnose_authentication_failure():
    event = IntegrationEvent(
        service="payment-api",
        endpoint="/payments",
        status_code=401,
        response_time_ms=125.5,
        success=False,
        retry_count=1
    )

    result = diagnose_event(event)

    assert result is not None
    assert result.rule_id == "HTTP-001"
    assert result.category == "authentication_failure"
    assert result.severity == "error"
    assert "Status code: 401" in result.evidence
    assert result.probable_cause == "Invalid or missing authentication credentials"
    assert result.recommended_action == "Verify authentication credentials and try again"


def test_diagnose_event_without_matching_rule():
    event = IntegrationEvent(
        service="payment-api",
        endpoint="/payments",
        status_code=200,
        response_time_ms=125.5,
        success=True,
        retry_count=0
    )

    result = diagnose_event(event)

    assert result is None