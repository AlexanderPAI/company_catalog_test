import uuid
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class CompanyScheme(BaseModel):
    """Company scheme"""

    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID = Field(..., title="ID")
    name: str = Field(..., title="Company Name")
    building: "BuildingScheme" = Field(..., title="Company Building")
    phones: Optional[List["PhoneScheme"]] = Field(None, title="Company Phones")
    company_activities: Optional[List["CompanyDoubleSubActivityScheme"]] = Field(
        ..., title="Company Activities"
    )


class PhoneScheme(BaseModel):
    """Phone scheme"""

    model_config = ConfigDict(from_attributes=True)
    phone: str = Field(..., title="Phone number")


class BuildingScheme(BaseModel):
    """Building scheme"""

    model_config = ConfigDict(from_attributes=True)
    address: str = Field(..., title="Building address")
    latitude: float = Field(..., title="Building latitude")
    longitude: float = Field(..., title="Building longitude")


class DoubleSubActivityScheme(BaseModel):
    """Double sub activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    title: str = Field(..., title="Double sub activity title")


class SubActivityScheme(BaseModel):
    """Sub activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    title: str = Field(..., title="Sub activity title")
    double_sub_activities: List[DoubleSubActivityScheme] = Field(
        ..., title="Double Sub activities", alias="double_sub_activities"
    )


class ActivityScheme(BaseModel):
    """Activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    title: str = Field(..., title="Activity title")
    sub_activities: List[SubActivityScheme] = Field(
        ..., title="Sub activities", alias="sub_activities"
    )


class CompanyDoubleSubActivityScheme(BaseModel):
    """Company activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    double_sub_activity: DoubleSubActivityScheme = Field(..., title="Activity")
