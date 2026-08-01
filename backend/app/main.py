from fastapi import FastAPI

app = FastAPI(
    title="DevFlow API",
    description="Enterprise Project Management Platform",
    version="1.0.0",
)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to DevFlow API 🚀"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "Running Successfully"}
