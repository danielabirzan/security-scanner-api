"""Main FastAPI application entry point."""

from fastapi import FastAPI

from app.api.v1 import info, scans
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
)

# Include routers
app.include_router(info.router, prefix=f"{settings.API_V1_PREFIX}", tags=["info"])

app.include_router(
    scans.router, prefix=f"{settings.API_V1_PREFIX}/scans", tags=["scans"]
)


@app.get("/health")
def health_check() -> dict:
    """Check application health status."""
    return {"status": "healthy"}
