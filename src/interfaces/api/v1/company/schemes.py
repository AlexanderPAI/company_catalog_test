from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from src.interfaces.api.v1.activity.schemes import GeneralActivityScheme
from src.interfaces.api.v1.building.schemes import BuildingScheme


class Company(BaseModel):
    """Company scheme"""

    id: Optional[UUID] = Field(None, title="ID")
    name: str = Field(..., title="Company name")
    phone_number: List[str] = Field(..., title="Phone number")
    building: BuildingScheme = Field(..., title="Building")
    activities: List[GeneralActivityScheme] = Field(..., title="Activities")
