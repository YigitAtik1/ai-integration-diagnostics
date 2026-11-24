from fastapi import FastAPI
from src.models import IntegrationEvent

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/events")
async def receive_event(event: IntegrationEvent):
    return {"message": "Event Received", "event": event.model_dump()}
