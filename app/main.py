from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import scans, info

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json"
)

# Include routers
app.include_router(
    info.router,
    prefix=f"{settings.API_V1_PREFIX}",
    tags=["info"]
)

app.include_router(
    scans.router,
    prefix=f"{settings.API_V1_PREFIX}/scans",
    tags=["scans"]
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}