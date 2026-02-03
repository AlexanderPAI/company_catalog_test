from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.models import Company
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.schemes import CompanyScheme

router = APIRouter()


@router.get(
    "/company/list", response_model=List[CompanyScheme], response_model_by_alias=True
)
async def get_company_list(  # type: ignore
    session: AsyncSession = Depends(get_session),
):
    """List all companies"""

    db_repo = DBRepository(model=Company, session=session)
    result = await db_repo.list()
    return result
