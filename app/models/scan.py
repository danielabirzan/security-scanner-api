"""Scan model."""

import enum
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import JSON, Enum, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class ScanStatus(str, enum.Enum):
    """Possible scan statuses."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Scan(Base):
    """Security scan record."""

    __tablename__ = "scans"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    url: Mapped[str] = mapped_column(String, nullable=False, index=True)
    status: Mapped[ScanStatus] = mapped_column(
        Enum(ScanStatus), default=ScanStatus.PENDING
    )
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    results: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
