"""Pydantic schemas for Scan API validation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl

from app.models.scan import ScanStatus


class ScanCreate(BaseModel):
    """Schema for creating a new scan."""

    url: HttpUrl


class ScanResponse(BaseModel):
    """Schema for scan response."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    url: str
    status: ScanStatus
    error_message: Optional[str] = None
    results: Optional[dict] = None
    created_at: datetime


class ScanUpdate(BaseModel):
    """Schema for updating scan."""

    status: Optional[ScanStatus] = None
    error_message: Optional[str] = None
    results: Optional[dict] = None
