from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.models import GeneralActivity
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.activity.schemes import GeneralActivityScheme

general_activity_router = APIRouter()


@general_activity_router.post("/general_activity", response_model=GeneralActivityScheme)
async def create_sub_activity(  # type: ignore
    general_activity: GeneralActivityScheme,
    session: AsyncSession = Depends(get_session),
):
    """Endpoint for creating a sub activity."""
    db_repo = DBRepository(model=GeneralActivity, session=session)
    result = await db_repo.add(general_activity.model_dump())
    return result


@general_activity_router.get(
    "/general_activity/list", response_model=List[GeneralActivityScheme]
)
async def get_general_activity_list(session: AsyncSession = Depends(get_session)):  # type: ignore
    """Endpoint for listing all general activity."""
    db_repo = DBRepository(model=GeneralActivity, session=session)
    result = await db_repo.list()
    return result


@general_activity_router.get(
    "/general_activity/{id}", response_model=GeneralActivityScheme
)
async def get_general_activity(  # type: ignore
    general_activity_id: UUID, session: AsyncSession = Depends(get_session)
):
    """Endpoint for getting a general activity."""
    db_repo = DBRepository(model=GeneralActivity, session=session)
    result = await db_repo.get(id=general_activity_id)
    return result
