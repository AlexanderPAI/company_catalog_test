from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.domain import entities
from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models import models
from src.infrastructure.repositories.db import DBRepository

app = FastAPI()


@app.post("/add_building")
async def add_building(
    building: entities.Building, session: AsyncSession = Depends(get_session)
) -> entities.Building:
    db_repo = DBRepository(model=models.Building, session=session)
    result = await db_repo.add(building.model_dump())
    return result  # type: ignore


@app.get("/")
def root() -> dict[str, str | int | float]:
    return {"message": "working"}
