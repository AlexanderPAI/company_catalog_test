from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.models import Company
from src.infrastructure.repositories.db import DBRepository

router = APIRouter()


@router.get("/company/list")
async def get_company_list(  # type: ignore
    session: AsyncSession = Depends(get_session),
):
    """List all companies"""

    db_repo = DBRepository(model=Company, session=session)
    result = await db_repo.list()
    return result
