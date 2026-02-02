from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models import models
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.schemes import Building

building_router = APIRouter(prefix="/building")


@building_router.post("/add", response_model=Building)
async def add_building(  # type: ignore
    building: Building, session: AsyncSession = Depends(get_session)
):
    db_repo = DBRepository(model=models.Building, session=session)
    result = await db_repo.add(building.model_dump())
    return result


@building_router.get("/list", response_model=List[Building])
async def get_buildings(session: AsyncSession = Depends(get_session)):  # type: ignore
    db_repo = DBRepository(model=models.Building, session=session)
    result = await db_repo.list()
    return result


@building_router.get("/get/{id}", response_model=Building)
async def get_building(building_id: UUID, session: AsyncSession = Depends(get_session)):  # type: ignore
    db_repo = DBRepository(model=models.Building, session=session)
    result = await db_repo.get(id=building_id)
    return result
