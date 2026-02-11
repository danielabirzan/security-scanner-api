"""API information endpoints."""

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=dict, tags=["info"])
def api_info() -> dict:
    """Get API version and status information.

    Returns:
        dict: API metadata.
    """
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }
