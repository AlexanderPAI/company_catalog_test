from sqlalchemy import UUID, Column, Float, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, relationship

from src.infrastructure.db.models.mixins import TimestampedMixin, UUIDMixin


class Base(DeclarativeBase):
    pass


class Building(UUIDMixin, TimestampedMixin, Base):
    """Building table"""

    __tablename__ = "building"

    address = Column(String(255), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class GeneralActivity(UUIDMixin, TimestampedMixin, Base):
    """General activity table"""

    __tablename__ = "general_activity"

    title = Column(String(255), nullable=False)

    activity_types = relationship("ActivityType", backref="general_activity")


class ActivityType(UUIDMixin, TimestampedMixin, Base):
    """Activity type table"""

    __tablename__ = "activity_type"

    title = Column(String(255), nullable=False)
    sub_activities = relationship("SubActivity", backref="activity_type")

    general_activity_id = Column(UUID(as_uuid=True), ForeignKey("general_activity.id"))
    general_activity = relationship("GeneralActivity", back_populates="activity_types")


class SubActivity(UUIDMixin, TimestampedMixin, Base):
    """Sub activity table"""

    __tablename__ = "sub_activity"
    title = Column(String(255), nullable=False)

    activity_type_id = Column(UUID(as_uuid=True), ForeignKey("activity_type.id"))
    activity_type = relationship("ActivityType", backref="sub_activities")


class Company(UUIDMixin, TimestampedMixin, Base):
    """Company table"""

    __tablename__ = "companies"
    name = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    # building
    # activities
