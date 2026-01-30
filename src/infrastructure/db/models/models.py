from sqlalchemy import Column, Float, String
from sqlalchemy.orm import DeclarativeBase

from src.infrastructure.db.models.mixins import TimestampedMixin, UUIDMixin

# from sqlalchemy.orm import relationship


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
    # activity types


class ActivityType(UUIDMixin, TimestampedMixin, Base):
    """Activity type table"""

    __tablename__ = "activity_type"
    title = Column(String(255), nullable=False)
    # sub activities


class SubActivity(UUIDMixin, TimestampedMixin, Base):
    """Sub activity table"""

    __tablename__ = "sub_activity"
    title = Column(String(255), nullable=False)


class Company(UUIDMixin, TimestampedMixin, Base):
    """Company table"""

    __tablename__ = "companies"
    name = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    # building
    # activities
