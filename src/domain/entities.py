from typing import List

from pydantic import BaseModel


class Building(BaseModel):
    """Building entity"""

    address: str
    latitude: float
    longitude: float


class GeneralActivity(BaseModel):
    """Activity type entity"""

    title: str
    activity_types: List["ActivityType"]


class ActivityType(BaseModel):
    """Activity entity"""

    title: str
    sub_activities: List["SubActivity"]


class SubActivity(BaseModel):
    """Sub Activity entity"""

    title: str


class Company(BaseModel):
    """Company entity"""

    name: str
    phone_number: List[str]
    building: Building
    activity_type: List[ActivityType]
