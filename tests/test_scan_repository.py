"""Tests for scan repository."""

from app.models.scan import ScanStatus
from app.repositories.scan_repository import ScanRepository


def test_create_scan(db):
    """Test creating a scan."""
    repo = ScanRepository(db)

    scan = repo.create(url="https://example.com")

    assert scan.id is not None
    assert scan.url == "https://example.com"
    assert scan.status == ScanStatus.PENDING
    assert scan.created_at is not None


def test_get_scan_by_id(db):
    """Test getting scan by ID."""
    repo = ScanRepository(db)

    created_scan = repo.create(url="https://test.com")

    retrieved_scan = repo.get_by_id(created_scan.id)

    assert retrieved_scan is not None
    assert retrieved_scan.id == created_scan.id
    assert retrieved_scan.url == "https://test.com"


def test_get_scan_by_id_not_found(db):
    """Test getting non-existent scan."""
    repo = ScanRepository(db)

    scan = repo.get_by_id(999)

    assert scan is None


def test_get_all_scans(db):
    """Test getting all scans."""
    repo = ScanRepository(db)

    # Create multiple scans
    repo.create(url="https://test1.com")
    repo.create(url="https://test2.com")
    repo.create(url="https://test3.com")

    # Get all
    scans = repo.get_all()

    assert len(scans) == 3


def test_delete_scan(db):
    """Test deleting a scan."""
    repo = ScanRepository(db)

    scan = repo.create(url="https://delete-me.com")
    scan_id = scan.id

    result = repo.delete(scan_id)

    assert result is True
    assert repo.get_by_id(scan_id) is None


def test_delete_scan_not_found(db):
    """Test deleting non-existent scan."""
    repo = ScanRepository(db)

    result = repo.delete(999)

    assert result is False


def test_update_scan(db):
    """Test updating scan."""
    repo = ScanRepository(db)

    scan = repo.create(url="https://update-me.com")

    updated = repo.update(
        scan.id, status=ScanStatus.COMPLETED, results={"ports": [80, 443]}
    )

    assert updated is not None
    assert updated.status == ScanStatus.COMPLETED
    assert updated.results == {"ports": [80, 443]}
