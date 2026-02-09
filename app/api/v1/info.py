from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/", tags=["info"])
def api_info():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }