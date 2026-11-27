from pydantic import BaseModel, Field


class IntegrationEvent(BaseModel):
    service: str = Field(min_length=1)
    endpoint: str = Field(min_length=1)
    status_code: int = Field(ge=100, le=599)
    response_time_ms: float = Field(ge=0)
    success: bool
    retry_count: int = Field(ge=0)


class DiagnosticResult(BaseModel):
    rule_id: str = Field(min_length=1)
    category: str = Field(min_length=1)
    severity: str = Field(min_length=1)
    probable_cause: str = Field(min_length=1)
    evidence: list[str] = Field(min_length=1)
    recommended_action: str = Field(min_length=1)
