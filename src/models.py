from pydantic import BaseModel, Field


class IntegrationEvent(BaseModel):
    service: str = Field(min_length=1)
    endpoint: str = Field(min_length=1)
    status_code: int = Field(ge=100, le=599)
    response_time_ms: float = Field(ge=0)
    success: bool
    retry_count: int = Field(ge=0)