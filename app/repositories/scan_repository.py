"""Scan repository for database operations."""

from typing import Optional

from sqlalchemy.orm import Session

from app.models.scan import Scan, ScanStatus


class ScanRepository:
    """Repository for Scan model CRUD operations."""

    def __init__(self, db: Session) -> None:
        """Initialize repository with database session."""
        self.db = db

    def create(self, url: str) -> Scan:
        """Create a new scan."""
        scan = Scan(url=url, status=ScanStatus.PENDING)
        self.db.add(scan)
        self.db.commit()
        self.db.refresh(scan)
        return scan

    def get_by_id(self, scan_id: int) -> Optional[Scan]:
        """Get scan by ID."""
        return self.db.query(Scan).filter(Scan.id == scan_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Scan]:
        """Get all scans with pagination."""
        return self.db.query(Scan).offset(skip).limit(limit).all()

    def update(
        self,
        scan_id: int,
        status: Optional[ScanStatus] = None,
        error_message: Optional[str] = None,
        results: Optional[dict] = None,
    ) -> Optional[Scan]:
        """Update scan details."""
        scan = self.get_by_id(scan_id)
        if scan:
            if status is not None:
                scan.status = status
            if error_message is not None:
                scan.error_message = error_message
            if results is not None:
                scan.results = results
            self.db.commit()
            self.db.refresh(scan)
        return scan

    def delete(self, scan_id: int) -> bool:
        """Delete scan by ID."""
        scan = self.get_by_id(scan_id)
        if scan:
            self.db.delete(scan)
            self.db.commit()
            return True
        return False
