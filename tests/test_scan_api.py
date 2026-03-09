"""Tests for scan API endpoints."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Get test client."""
    return TestClient(app)


def test_create_scan(client):
    """Test POST /scans endpoint."""
    response = client.post("/api/v1/scans/", json={"url": "https://example.com"})

    assert response.status_code == 201
    data = response.json()
    assert data["url"] == "https://example.com/"
    assert data["status"] == "pending"
    assert "id" in data
    assert "created_at" in data


def test_create_scan_invalid_url(client):
    """Test creating scan with invalid URL."""
    response = client.post("/api/v1/scans/", json={"url": "not-a-url"})

    assert response.status_code == 422


def test_get_scan(client):
    """Test GET /scans/{id} endpoint."""
    create_response = client.post("/api/v1/scans/", json={"url": "https://test.com"})
    scan_id = create_response.json()["id"]

    response = client.get(f"/api/v1/scans/{scan_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == scan_id
    assert data["url"] == "https://test.com/"


def test_get_scan_not_found(client):
    """Test getting non-existent scan."""
    response = client.get("/api/v1/scans/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Scan not found"


def test_list_scans(client):
    """Test GET /scans endpoint."""
    # Create scans
    client.post("/api/v1/scans/", json={"url": "https://test1.com"})
    client.post("/api/v1/scans/", json={"url": "https://test2.com"})

    # List scans
    response = client.get("/api/v1/scans/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_list_scans_pagination(client):
    """Test pagination."""
    for i in range(5):
        client.post("/api/v1/scans/", json={"url": f"https://test{i}.com"})

    response = client.get("/api/v1/scans/?skip=0&limit=2")
    assert response.status_code == 200
    assert len(response.json()) == 2

    response = client.get("/api/v1/scans/?skip=2&limit=2")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_delete_scan(client):
    """Test DELETE /scans/{id} endpoint."""
    create_response = client.post(
        "/api/v1/scans/", json={"url": "https://delete-me.com"}
    )
    scan_id = create_response.json()["id"]

    response = client.delete(f"/api/v1/scans/{scan_id}")

    assert response.status_code == 204

    get_response = client.get(f"/api/v1/scans/{scan_id}")
    assert get_response.status_code == 404


def test_delete_scan_not_found(client):
    """Test deleting non-existent scan."""
    response = client.delete("/api/v1/scans/999")

    assert response.status_code == 404


def test_update_scan(client):
    """Test PATCH /scans/{id} endpoint."""
    create_response = client.post(
        "/api/v1/scans/", json={"url": "https://update-me.com"}
    )
    scan_id = create_response.json()["id"]

    response = client.patch(
        f"/api/v1/scans/{scan_id}",
        json={"status": "completed", "results": {"ports": [80, 443]}},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "completed"
    assert data["results"] == {"ports": [80, 443]}


def test_update_scan_not_found(client):
    """Test updating non-existent scan."""
    response = client.patch("/api/v1/scans/999", json={"status": "completed"})

    assert response.status_code == 404
