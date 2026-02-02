from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Building(BaseModel):
    """Building entity"""

    id: Optional[UUID] = Field(None, title="Building ID")
    address: str = Field(..., title="Building address")
    latitude: float = Field(..., title="Building latitude")
    longitude: float = Field(..., title="Building longitude")
