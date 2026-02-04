from typing import List, Optional

from pydantic import BaseModel


class Building(BaseModel):
    """Building entity"""

    address: str
    latitude: float
    longitude: float


class Activity(BaseModel):
    """Activity entity"""

    title: str
    sub_activities: List["SubActivity"]


class SubActivity(BaseModel):
    """SubActivity entity"""

    title: str
    double_sub_activities: List["DoubleSubActivity"]


class DoubleSubActivity(BaseModel):
    """Sub Activity entity"""

    title: str


class Phone(BaseModel):
    """Phone entity"""

    phone: str


class Company(BaseModel):
    """Company entity"""

    name: str
    phones: Optional[List[Phone]] = []
    building: Building
    activities: Optional[List[Activity]] = []
    sub_activities: Optional[List[SubActivity]] = []
    double_sub_activities: Optional[List[DoubleSubActivity]] = []
