from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.models import Company
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.company.schemes import CompanyScheme

company_router = APIRouter()


@company_router.post("/company", response_model=CompanyScheme)
async def create_company(  # type: ignore
    company: CompanyScheme,
    session: AsyncSession = Depends(get_session),
):
    """Create a new company"""
    db_repo = DBRepository(model=Company, session=session)
    result = await db_repo.add(company.model_dump())
    return result


@company_router.get("/company/list", response_model=List[CompanyScheme])
async def get_companies(  # type: ignore
    session: AsyncSession = Depends(get_session),
):
    """List all companies"""
    db_repo = DBRepository(model=Company, session=session)
    result = db_repo.list()
    return result


@company_router.get("/company/{id}", response_model=CompanyScheme)
async def get_company(company_id: UUID, session: AsyncSession = Depends(get_session)):  # type: ignore
    """Get a company"""
    db_repo = DBRepository(model=Company, session=session)
    result = await db_repo.get(id=company_id)
    return result
