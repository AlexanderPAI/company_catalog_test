import uuid
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from src.infrastructure.db.models.mixins import TimestampedMixin, UUIDMixin


class Base(AsyncAttrs, DeclarativeBase):
    """Base model"""

    __abstract__ = True


class Building(Base, UUIDMixin, TimestampedMixin):
    """Building entity"""

    __tablename__ = "buildings"
    address: Mapped[str] = mapped_column("address", nullable=False)
    latitude: Mapped[float] = mapped_column("latitude", nullable=False)
    longitude: Mapped[float] = mapped_column("longitude", nullable=False)
    companies: Mapped[List["Company"]] = relationship(
        "Company", back_populates="building"
    )


class Phone(Base, UUIDMixin):
    """Phone entity"""

    __tablename__ = "phones"
    phone: Mapped[str] = mapped_column("phone", nullable=False)
    company_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("companies.id"))
    company: Mapped["Company"] = relationship("Company", back_populates="phones")


class Company(Base, UUIDMixin, TimestampedMixin):
    """Company entity"""

    __tablename__ = "companies"
    name: Mapped[str] = mapped_column("name", nullable=False)
    building_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("buildings.id"))
    building: Mapped["Building"] = relationship(
        "Building", back_populates="companies", lazy="selectin"
    )
    phones: Mapped[List["Phone"]] = relationship(
        "Phone", back_populates="company", cascade="all, delete-orphan", lazy="selectin"
    )
    company_activities: Mapped[List["CompanyActivity"]] = relationship(
        "CompanyActivity", back_populates="company", lazy="selectin"
    )
    company_sub_activities: Mapped[List["CompanySubActivity"]] = relationship(
        "CompanySubActivity", back_populates="company", lazy="selectin"
    )
    company_double_sub_activities: Mapped[List["CompanyDoubleSubActivity"]] = (
        relationship(
            "CompanyDoubleSubActivity", back_populates="company", lazy="selectin"
        )
    )


class Activity(Base, UUIDMixin):
    """Activity entity"""

    __tablename__ = "activities"
    title: Mapped[str] = mapped_column("title", nullable=False)
    sub_activities: Mapped[List["SubActivity"]] = relationship(
        "SubActivity",
        back_populates="activity",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
    company_activities: Mapped[List["CompanyActivity"]] = relationship(
        "CompanyActivity", back_populates="activity", lazy="selectin"
    )


class SubActivity(Base, UUIDMixin):
    """Sub activity entity"""

    __tablename__ = "sub_activities"
    title: Mapped[str] = mapped_column("title", nullable=False)
    activity_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("activities.id"))
    activity: Mapped["Activity"] = relationship(
        "Activity", back_populates="sub_activities"
    )
    double_sub_activities: Mapped[List["DoubleSubActivity"]] = relationship(
        "DoubleSubActivity",
        back_populates="sub_activity",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    company_sub_activities: Mapped[List["CompanySubActivity"]] = relationship(
        "CompanySubActivity",
        back_populates="sub_activity",
        lazy="selectin",
    )


class DoubleSubActivity(Base, UUIDMixin):
    """Double sub activity entity"""

    __tablename__ = "double_sub_activities"
    title: Mapped[str] = mapped_column("title", nullable=False)
    sub_activity_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sub_activities.id"))
    sub_activity: Mapped["SubActivity"] = relationship(
        "SubActivity", back_populates="double_sub_activities"
    )
    company_double_sub_activities: Mapped[List["CompanyDoubleSubActivity"]] = (
        relationship(
            "CompanyDoubleSubActivity",
            back_populates="double_sub_activity",
            lazy="selectin",
        )
    )


class CompanyActivity(Base, UUIDMixin):
    """Company activity for m2m relationship"""

    __tablename__ = "company_activities"
    company_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("companies.id"), primary_key=True
    )
    activity_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("activities.id"), primary_key=True
    )
    company: Mapped["Company"] = relationship(
        "Company", back_populates="company_activities", lazy="selectin"
    )
    activity: Mapped["Activity"] = relationship(
        "Activity", back_populates="company_activities", lazy="selectin"
    )


class CompanySubActivity(Base, UUIDMixin):
    """Company sub_activity for m2m relationship"""

    __tablename__ = "company_sub_activities"
    company_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("companies.id"), primary_key=True
    )
    sub_activity_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("sub_activities.id"), primary_key=True
    )
    company: Mapped["Company"] = relationship(
        "Company", back_populates="company_sub_activities", lazy="selectin"
    )
    sub_activity: Mapped["SubActivity"] = relationship(
        "SubActivity", back_populates="company_sub_activities", lazy="selectin"
    )


class CompanyDoubleSubActivity(Base, UUIDMixin):
    """Company double_sub_activity for m2m relationship"""

    __tablename__ = "company_double_sub_activities"
    company_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("companies.id"), primary_key=True
    )
    double_sub_activity_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("double_sub_activities.id"), primary_key=True
    )
    company: Mapped["Company"] = relationship(
        "Company", back_populates="company_double_sub_activities", lazy="selectin"
    )
    double_sub_activity: Mapped["DoubleSubActivity"] = relationship(
        "DoubleSubActivity",
        back_populates="company_double_sub_activities",
        lazy="selectin",
    )
