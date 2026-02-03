import uuid
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


# Company
class CompanyScheme(BaseModel):
    """Company scheme"""

    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID = Field(..., title="ID")
    name: str = Field(..., title="Company Name")
    building: "BuildingScheme" = Field(..., title="Company Building")
    phones: Optional[List["PhoneScheme"]] = Field(None, title="Company Phones")
    company_activities: Optional[List["CompanyDoubleSubActivityScheme"]] = Field(
        None, title="Company Activities"
    )
    company_sub_activities: Optional[List["CompanySubActivityScheme"]] = Field(
        None, title="Company Sub Activities"
    )
    company_double_sub_activities: Optional[List["CompanyDoubleSubActivityScheme"]] = (
        Field(None, title="Company Double Sub Activities")
    )


class PhoneScheme(BaseModel):
    """Phone scheme"""

    model_config = ConfigDict(from_attributes=True)
    phone: str = Field(..., title="Phone number")


# Building
class BuildingScheme(BaseModel):
    """Building scheme"""

    model_config = ConfigDict(from_attributes=True)
    address: str = Field(..., title="Building address")
    latitude: float = Field(..., title="Building latitude")
    longitude: float = Field(..., title="Building longitude")


# Activities
class ActivityScheme(BaseModel):
    """Activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    title: str = Field(..., title="Activity title")


class SubActivityScheme(BaseModel):
    """Sub activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    title: str = Field(..., title="Sub activity title")


class DoubleSubActivityScheme(BaseModel):
    """Double sub activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    title: str = Field(..., title="Double sub activity title")


class CompanyActivityScheme(BaseModel):
    """Company activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    activity: ActivityScheme = Field(..., title="Company activity scheme")


class CompanySubActivityScheme(BaseModel):
    """Company sub activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    sub_activity: SubActivityScheme = Field(..., title="Sub activity")


class CompanyDoubleSubActivityScheme(BaseModel):
    """Company double sub activity scheme"""

    model_config = ConfigDict(from_attributes=True)
    double_sub_activity: DoubleSubActivityScheme = Field(..., title="Activity")
