"""Scans API endpoints."""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

router = APIRouter()


class Scan(BaseModel):
    """Scan model representing a security scan job."""

    id: int
    name: str
    status: str


@router.get("/", response_model=list[Scan])
def list_scans(limit: int = Query(10, ge=1, le=100), offset: int = Query(0, ge=0)) -> list[Scan]:
    """Scan model representing a security scan job."""
    # TODO: replace with real data store access
    return []


@router.get("/{scan_id}", response_model=Scan)
def get_scan(scan_id: int) -> Scan:
    """Retrieve a specific scan by ID."""
    # TODO: fetch a scan from DB; placeholder raises 404
    raise HTTPException(status_code=404, detail="Scan not found")
