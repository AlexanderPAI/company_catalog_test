from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.models import Building
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.building.schemes import BuildingScheme

building_router = APIRouter()


@building_router.post("/building", response_model=BuildingScheme)
async def add_building(  # type: ignore
    building: BuildingScheme, session: AsyncSession = Depends(get_session)
):
    """Endpoint for adding a building to the database."""
    db_repo = DBRepository(model=Building, session=session)
    result = await db_repo.add(building.model_dump())
    return result


@building_router.get("/building/list", response_model=List[BuildingScheme])
async def get_buildings(session: AsyncSession = Depends(get_session)):  # type: ignore
    """Endpoint for listing all buildings."""
    db_repo = DBRepository(model=Building, session=session)
    result = await db_repo.list()
    return result


@building_router.get("/building/{id}", response_model=BuildingScheme)
async def get_building(building_id: UUID, session: AsyncSession = Depends(get_session)):  # type: ignore
    """Endpoint for getting a building by ID."""
    db_repo = DBRepository(model=Building, session=session)
    result = await db_repo.get(id=building_id)
    return result
