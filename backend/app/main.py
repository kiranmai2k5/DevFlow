from fastapi import FastAPI

from app.api.auth import router as auth_router

app = FastAPI(
    title="DevFlow API",
    description="Enterprise Project Management Platform",
    version="1.0.0",
)

# Register API Routers
app.include_router(auth_router)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to DevFlow API 🚀"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "Running Successfully"}