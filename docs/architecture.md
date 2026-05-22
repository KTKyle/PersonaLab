Flow:
    Next.js UI
    ↓
    FastAPI Backend
    ↓
    PostgreSQL ← stores personas, experiments, responses
    ↓
    Qdrant ← stores embedded persona memory
    ↓
    LLM API ← generates structured responses
    ↓
    MLflow / eval logs ← tracks quality, latency, cost