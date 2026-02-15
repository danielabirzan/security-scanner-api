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

    def update_status(
        self, scan_id: int, status: ScanStatus, error_message: Optional[str] = None
    ) -> Optional[Scan]:
        """Update scan status."""
        scan = self.get_by_id(scan_id)
        if scan:
            scan.status = status
            if error_message:
                scan.error_message = error_message
            self.db.commit()
            self.db.refresh(scan)
        return scan
