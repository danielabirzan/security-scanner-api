"""Scans API endpoints."""

from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.scan_repository import ScanRepository
from app.schemas.scan import ScanCreate, ScanResponse
from app.services.scan_service import ScanService

router = APIRouter()


class Scan(BaseModel):
    """Scan model representing a security scan job."""

    id: int
    name: str
    status: str


def get_scan_service(db: Session = Depends(get_db)) -> ScanService:
    """Dependency to get scan service."""
    repo = ScanRepository(db)
    return ScanService(repo)


@router.post("/", response_model=ScanResponse, status_code=201)
def create_scan(
    scan_data: ScanCreate, service: ScanService = Depends(get_scan_service)
) -> ScanResponse:
    """Create a new scan."""
    return service.create_scan(str(scan_data.url))


@router.get("/{scan_id}", response_model=ScanResponse)
def get_scan(
    scan_id: int, service: ScanService = Depends(get_scan_service)
) -> ScanResponse:
    """Get scan by ID."""
    scan = service.get_scan(scan_id)
    if not scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    return scan


@router.get("/", response_model=list[ScanResponse])
def list_scans(
    skip: int = 0, limit: int = 100, service: ScanService = Depends(get_scan_service)
) -> Sequence[ScanResponse]:
    """List all scans."""
    return service.list_scans(skip, limit)
