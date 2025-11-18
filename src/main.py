from fastapi import FastAPI

from src.config import settings
from src.api.frete import router as frete_router


app = FastAPI(title=settings.app_name)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment,
    }


# Registra as rotas de frete
app.include_router(frete_router)