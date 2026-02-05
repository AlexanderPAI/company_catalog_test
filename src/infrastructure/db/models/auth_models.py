import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import Base
from src.infrastructure.db.models.mixins import TimestampedMixin, UUIDMixin

id: Mapped[uuid.UUID] = mapped_column(
    UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
)


class ApiKey(Base, TimestampedMixin, UUIDMixin):
    """Api key model"""

    __tablename__ = "api_keys"

    key: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4)
