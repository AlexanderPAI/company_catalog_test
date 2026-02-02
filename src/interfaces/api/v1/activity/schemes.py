from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class GeneralActivityScheme(BaseModel):
    """General activity scheme"""

    id: Optional[UUID] = Field(None, title="ID")
    title: str = Field(..., title="Activity title")
    activity_types: List["ActivityTypeScheme"] = Field(..., title="Activity types")


class ActivityTypeScheme(BaseModel):
    """Activity type scheme"""

    id: Optional[UUID] = Field(None, title="ID")
    title: str = Field(..., title="Activity title")
    sub_activities: List["SubActivityScheme"] = Field(..., title="Sub Activities")


class SubActivityScheme(BaseModel):
    """Sub Activity scheme"""

    id: Optional[UUID] = Field(None, title="ID")
    title: str = Field(..., title="Activity title")
