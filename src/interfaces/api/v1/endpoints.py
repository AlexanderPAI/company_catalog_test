from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.models import Building, Company
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.schemes import CompanyScheme

router = APIRouter()


@router.get("/company/get_by_building", response_model=List[CompanyScheme])
async def get_company_by_building(  # type: ignore
    address: str,
    session: AsyncSession = Depends(get_session),
):
    building_db_repo = DBRepository(model=Building, session=session)
    building = await building_db_repo.get(address=address)
    if not building:
        raise HTTPException(status_code=404, detail="Building not found")

    company_db_repo = DBRepository(model=Company, session=session)
    companies = await company_db_repo.list(building_id=building.id)
    return companies


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
