from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.models import (  # ActivityType,; GeneralActivity,
    SubActivity,
)
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.activity.schemes import (  # ActivityTypeScheme,; GeneralActivityScheme,
    SubActivityScheme,
)

activity_router = APIRouter(prefix="/activity")


@activity_router.post("/sub_activity", response_model=SubActivityScheme)
async def create_sub_activity(  # type: ignore
    sub_activity: SubActivityScheme,
    session: AsyncSession = Depends(get_session),
):
    """Endpoint for creating a sub activity."""
    db_repo = DBRepository(model=SubActivity, session=session)
    result = await db_repo.add(sub_activity.model_dump())
    return result


@activity_router.get("/sub_activity/list", response_model=List[SubActivityScheme])
async def get_sub_activities(  # type: ignore
    session: AsyncSession = Depends(get_session),
):
    """Endpoint for getting a list of sub activities."""
    db_repo = DBRepository(model=SubActivity, session=session)
    result = await db_repo.list()
    return result


@activity_router.get("/sub_activity/{id}", response_model=SubActivityScheme)
async def get_sub_activity(  # type: ignore
    sub_activity_id: UUID, session: AsyncSession = Depends(get_session)
):
    """Endpoint for getting a sub activity by ID."""
    db_repo = DBRepository(model=SubActivity, session=session)
    result = await db_repo.get(id=sub_activity_id)
    return result
