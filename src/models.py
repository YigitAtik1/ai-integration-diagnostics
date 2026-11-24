from pydantic import BaseModel


class IntegrationEvent(BaseModel):
    service: str
    endpoint: str
    status_code: int
    response_time_ms: float
    success: bool
    retry_count: int
