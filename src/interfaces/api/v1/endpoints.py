import logging
import uuid
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.models import (
    Activity,
    Building,
    Company,
    CompanyActivity,
    CompanyDoubleSubActivity,
    CompanySubActivity,
)
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.v1.schemes import CompanyScheme

router = APIRouter()


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


@router.get("/company/get_by_activity", response_model=List[CompanyScheme])
async def get_company_activity_all(  # type: ignore
    activity: str,
    session: AsyncSession = Depends(get_session),
):
    """Get all companies activities (subactivities, double subactivities)"""
    act_repo = DBRepository(model=Activity, session=session)
    db_repo = DBRepository(model=Company, session=session)

    activity = await act_repo.get(title=activity)  # type: ignore

    sub_activity_ids = [sub_activity.id for sub_activity in activity.sub_activities]  # type: ignore
    double_sub_activities_ids = []

    for sub_activity in activity.sub_activities:  # type: ignore
        double_sub_activities_ids += [
            double_sub_activity.id
            for double_sub_activity in sub_activity.double_sub_activities
        ]

    result = await db_repo.list(
        Company.company_activities.any(
            CompanyActivity.activity.has(title=activity.title)
        )
    )

    result += await db_repo.list(  # type: ignore
        Company.company_sub_activities.any(
            CompanySubActivity.sub_activity_id.in_(sub_activity_ids)
        )
    )

    result += await db_repo.list(
        Company.company_double_sub_activities.any(
            CompanyDoubleSubActivity.double_sub_activity_id.in_(
                double_sub_activities_ids
            )
        )
    )
    result = set(result)  # type: ignore
    return result


@router.get("/company/get_by_specific_activity", response_model=List[CompanyScheme])
async def get_company_by_activity(  # type: ignore
    activity: str,
    session: AsyncSession = Depends(get_session),
):
    """Get company by activity"""
    db_repo = DBRepository(model=Company, session=session)
    result = await db_repo.list(
        Company.company_activities.any(CompanyActivity.activity.has(title=activity))
    )
    result += await db_repo.list(  # type: ignore
        Company.company_sub_activities.any(
            CompanySubActivity.sub_activity.has(title=activity)
        )
    )
    result += await db_repo.list(
        Company.company_double_sub_activities.any(
            CompanyDoubleSubActivity.double_sub_activity.has(title=activity)
        )
    )
    return result


@router.get("/company/get_by_building", response_model=List[CompanyScheme])
async def get_company_by_building(  # type: ignore
    address: str,
    session: AsyncSession = Depends(get_session),
):
    """Get Company by Building"""
    db_repo = DBRepository(model=Company, session=session)
    companies = await db_repo.list(Company.building.has(Building.address == address))
    return companies


@router.get("/company/get_by_id", response_model=CompanyScheme)
async def get_company_by_uuid(  # type: ignore
    company_id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
):
    """Get Company by ID"""
    db_repo = DBRepository(model=Company, session=session)
    company = await db_repo.get(id=company_id)
    return company


@router.get("/company/get_by_name", response_model=CompanyScheme)
async def get_company_by_name(  # type: ignore
    name: str,
    session: AsyncSession = Depends(get_session),
):
    """Get Company by Name"""
    db_repo = DBRepository(model=Company, session=session)
    company = await db_repo.get(name=name)
    return company


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
