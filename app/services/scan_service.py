"""Scan service for business logic."""

from typing import Optional

from app.models.scan import Scan, ScanStatus
from app.repositories.scan_repository import ScanRepository


class ScanService:
    """Service layer for scan operations."""

    def __init__(self, scan_repo: ScanRepository):
        """Initialize service with repository."""
        self.scan_repo = scan_repo

    def create_scan(self, url: str) -> Scan:
        """Create a new scan."""
        # Business logic aici (validări, transformări)
        return self.scan_repo.create(url)

    def get_scan(self, scan_id: int) -> Optional[Scan]:
        """Get scan by ID."""
        return self.scan_repo.get_by_id(scan_id)

    def list_scans(self, skip: int = 0, limit: int = 100) -> list[Scan]:
        """List all scans with pagination."""
        return self.scan_repo.get_all(skip, limit)

    def update_scan(
        self,
        scan_id: int,
        status: Optional[ScanStatus] = None,
        error_message: Optional[str] = None,
        results: Optional[dict] = None,
    ) -> Optional[Scan]:
        """Update scan details."""
        return self.scan_repo.update(
            scan_id, status=status, error_message=error_message, results=results
        )

    def delete_scan(self, scan_id: int) -> bool:
        """Delete scan by ID."""
        return self.scan_repo.delete(scan_id)
