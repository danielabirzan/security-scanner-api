"""Pytest configuration and fixtures."""

from collections.abc import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings
from app.database import Base

# Create test engine
engine = create_engine(settings.DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function", autouse=True)
def reset_db() -> Generator[None, None, None]:
    """Reset database before each test."""
    # Drop all tables
    Base.metadata.drop_all(bind=engine)
    # Recreate all tables
    Base.metadata.create_all(bind=engine)
    yield
    # Cleanup after test (optional, next test will drop anyway)
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db() -> Generator[Session, None, None]:
    """Get test database session."""
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
