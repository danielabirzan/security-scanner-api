"""Tests for scan service."""

from app.models.scan import ScanStatus
from app.repositories.scan_repository import ScanRepository
from app.services.scan_service import ScanService


def test_create_scan(db):
    """Test creating a scan via service."""
    repo = ScanRepository(db)
    service = ScanService(repo)

    scan = service.create_scan(url="https://example.com")

    assert scan.id is not None
    assert scan.url == "https://example.com"
    assert scan.status == ScanStatus.PENDING


def test_get_scan(db):
    """Test getting scan via service."""
    repo = ScanRepository(db)
    service = ScanService(repo)

    # Create scan
    created = service.create_scan(url="https://test.com")

    # Get scan
    retrieved = service.get_scan(created.id)

    assert retrieved is not None
    assert retrieved.id == created.id


def test_get_scan_not_found(db):
    """Test getting non-existent scan."""
    repo = ScanRepository(db)
    service = ScanService(repo)

    scan = service.get_scan(999)

    assert scan is None


def test_list_scans(db):
    """Test listing scans via service."""
    repo = ScanRepository(db)
    service = ScanService(repo)

    # Create scans
    service.create_scan(url="https://test1.com")
    service.create_scan(url="https://test2.com")

    # List scans
    scans = service.list_scans()

    assert len(scans) == 2


def test_list_scans_pagination(db):
    """Test pagination."""
    repo = ScanRepository(db)
    service = ScanService(repo)

    # Create 5 scans
    for i in range(5):
        service.create_scan(url=f"https://test{i}.com")

    # Get page 1 (2 items)
    page1 = service.list_scans(skip=0, limit=2)
    assert len(page1) == 2

    # Get page 2 (2 items)
    page2 = service.list_scans(skip=2, limit=2)
    assert len(page2) == 2

    # Get page 3 (1 item)
    page3 = service.list_scans(skip=4, limit=2)
    assert len(page3) == 1


def test_update_scan_status(db):
    """Test updating scan via service."""
    repo = ScanRepository(db)
    service = ScanService(repo)

    # Create scan
    scan = service.create_scan(url="https://update-me.com")

    # Update
    updated = service.update_scan(
        scan.id, status=ScanStatus.COMPLETED, results={"vulnerabilities": []}
    )

    assert updated is not None
    assert updated.status == ScanStatus.COMPLETED
    assert updated.results == {"vulnerabilities": []}
