from src.models import IntegrationEvent, DiagnosticResult


def diagnose_event(event: IntegrationEvent) -> DiagnosticResult | None:
    if event.status_code == 401:
        return DiagnosticResult(
            rule_id="HTTP-001",
            category="authentication_failure",
            severity="error",
            probable_cause="Invalid or missing authentication credentials",
            evidence=[f"Status code: {event.status_code}"],
            recommended_action="Verify authentication credentials and try again"
        )
    return None