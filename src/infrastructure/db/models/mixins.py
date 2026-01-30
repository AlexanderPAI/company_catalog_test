import uuid

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


class UUIDMixin:
    """UUID mixin for ID-models"""

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)


class TimestampedMixin:
    """Mixin created_at and updated_at"""

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
