from fastapi import FastAPI

from src.config import settings
from src.api.frete import router as frete_router
from src.models.health import HealthResponse


app = FastAPI(title=settings.app_name)


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        environment=settings.environment,
    )


app.include_router(frete_router)