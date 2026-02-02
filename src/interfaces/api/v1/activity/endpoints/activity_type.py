from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.models import ActivityType
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.activity.schemes import ActivityTypeScheme

activity_type_router = APIRouter()


@activity_type_router.post("/activity_type", response_model=ActivityTypeScheme)
async def create_activity_types(  # type: ignore
    activity_type: ActivityTypeScheme,
    session: AsyncSession = Depends(get_session),
):
    """Create a new activity type."""
    db_repo = DBRepository(model=ActivityType, session=session)
    result = await db_repo.add(activity_type.model_dump())
    return result


@activity_type_router.get(
    "/activity_type/list", response_model=List[ActivityTypeScheme]
)
async def get_activity_types(  # type: ignore
    session: AsyncSession = Depends(get_session),
):
    """Get all activity types."""
    db_repo = DBRepository(model=ActivityType, session=session)
    result = await db_repo.list()
    return result


@activity_type_router.get("/activity_type/{id}", response_model=ActivityTypeScheme)
async def get_activity_type_by_id(  # type: ignore
    activity_type_id: UUID,
    session: AsyncSession = Depends(get_session),
):
    """Get activity type by ID."""
    db_repo = DBRepository(model=ActivityType, session=session)
    result = await db_repo.get(activity_type_id=activity_type_id)
    return result
