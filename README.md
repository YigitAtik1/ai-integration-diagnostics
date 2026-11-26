# AI-Powered Integration Diagnostics

A Python-based diagnostic platform designed to detect, investigate, and explain software integration failures through structured event collection, deterministic analysis, and AI-assisted reasoning.

**Status:** Active Development — Phase 1: API Foundation

## Motivation

Modern software integrations span multiple services, APIs, SDKs, and infrastructure layers. When failures occur, identifying the root cause requires structured evidence collection and systematic investigation.

This project aims to build an extensible diagnostic platform that combines traditional engineering methods with evidence-grounded AI capabilities.

## Current Capabilities

- REST API built with FastAPI
- Health monitoring endpoint
- Structured integration event ingestion
- Runtime data validation using Pydantic
- Automatic rejection of malformed requests
- Modular API and data model architecture
- Manual HTTP testing using curl
- Automated API testing using pytest and TestClient
- Domain-specific event validation
- Parametrized API testing
- Boundry value testing 

## Architecture

```text
External Systems
       |
       v
FastAPI — API Layer
       |
       v
Pydantic — Validation Layer
       |
       v
Validated Integration Events
       |
       v
Future Components
  |-- Event Persistence
  |-- Diagnostic Engine
  |-- Event Correlation
  |-- AI-Assisted Analysis
```

## Technology Stack

| Technology | Purpose | Status |
|---|---|---|
| Python 3.14 | Backend development | Implemented |
| FastAPI | REST API | Implemented |
| Pydantic | Data validation | Implemented |
| Uvicorn | ASGI server | Implemented |
| Pytest | Automated testing | Implemented |
| HTTPX2 | HTTP testing | Implemented |
| Linux / WSL 2 | Development environment | Implemented |
| PostgreSQL | Event persistence | Planned |
| Docker | Containerization | Planned |
| GitHub Actions | CI/CD | Planned |
| AWS | Cloud deployment | Planned |
| LLM API | AI-assisted diagnostics | Planned |

## Repository Structure

```text
ai-integration-diagnostics/
├── src/
│   ├── main.py
│   └── models.py
├── tests/
│   └── test_api.py
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.14
- Git
- Linux or WSL 2 recommended

### Installation

```bash
git clone https://github.com/YigitAtik1/ai-integration-diagnostics.git
cd ai-integration-diagnostics

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt
```

### Run the API

```bash
python -m uvicorn src.main:app --reload
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /health | Application health check |
| POST | /events | Receive and validate integration events |

### Example Integration Event

```json
{
  "service": "payment-api",
  "endpoint": "/payments",
  "status_code": 401,
  "response_time_ms": 125.5,
  "success": false,
  "retry_count": 1
}
```

A valid event returns HTTP 200. Invalid request data returns HTTP 422 with structured validation details.

The status code contained in an integration event represents the external system's response, not the diagnostic API's response.

## Testing

```bash
python -m pytest -v
```

### Current Verification Results

| Scenario | Expected Result | Status |
|---|---|---|
| Health endpoint | HTTP 200 | Automated — PASS |
| Valid integration event | HTTP 200 | Automated — PASS |
| Invalid status code type | HTTP 422 | Automated — PASS |
| Missing required field | HTTP 422 | Automated — PASS |
| Invalid domain values (6 cases) | HTTP 422 | Automated — PASS |
| Valid boundary values (2 cases) | HTTP 200 | Automated — PASS |

Latest automated test result: **12 passed, 0 warnings.**

## Development Roadmap

- [x] Development environment setup
- [x] FastAPI application foundation
- [x] Integration event data model
- [x] Event ingestion endpoint
- [x] Manual positive and negative API testing
- [x] Initial automated API test
- [x] Extended automated API validation tests
- [x] HTTP client dependency migration
- [x] Domain-specific validation
- [x] Parametrized validation tests
- [x] Boundary value testing
- [ ] Integration failure simulation
- [ ] Deterministic diagnostic engine
- [ ] PostgreSQL persistence
- [ ] Multi-service event correlation
- [ ] AI-assisted root cause analysis
- [ ] Docker and CI/CD
- [ ] Cloud deployment

## Engineering Principles

- Evidence-driven diagnostics
- Deterministic analysis before AI inference
- Separation of concerns
- Reproducible development environments
- Testable and maintainable architecture
- Incremental implementation

## Known Limitations

- Diagnostic reasoning and AI capabilities are not implemented yet.
- Events are validated but not persisted.
- Cross-field validation is not implemented yet.
- Multi-service event correlation is pending.

---

This repository is under active development and will evolve through incremental engineering milestones.