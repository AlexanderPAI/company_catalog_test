from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models import models
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.schemes import Building

v1_router = APIRouter(prefix="/v1")


@v1_router.post("/add_building", response_model=Building)
async def add_building(  # type: ignore
    building: Building, session: AsyncSession = Depends(get_session)
):
    db_repo = DBRepository(model=models.Building, session=session)
    result = await db_repo.add(building.model_dump())
    return result


@v1_router.get("/get_buildings", response_model=List[Building])
async def get_buildings(session: AsyncSession = Depends(get_session)):  # type: ignore
    db_repo = DBRepository(model=models.Building, session=session)
    result = await db_repo.list()
    return result


@v1_router.get("/")
def root() -> dict[str, str | int | float]:
    return {"message": "working"}
