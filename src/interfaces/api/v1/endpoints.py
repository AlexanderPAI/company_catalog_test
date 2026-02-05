import logging
import uuid
from typing import List

from fastapi import APIRouter, Depends, Header
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.db_connector import get_session
from src.infrastructure.db.models.app_models import (
    Activity,
    Building,
    Company,
    CompanyActivity,
    CompanyDoubleSubActivity,
    CompanySubActivity,
)
from src.infrastructure.db.models.auth_models import ApiKey
from src.infrastructure.repositories.db import DBRepository
from src.interfaces.api.services.check_api_key import check_api_key
from src.interfaces.api.v1.schemes import CompanyScheme

router = APIRouter()


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


@router.get("/company/get_by_area", response_model=List[CompanyScheme])
async def get_company_by_area(  # type: ignore
    map_lat: float,
    map_lng: float,
    radius: float,
    session: AsyncSession = Depends(get_session),
    api_key: uuid.UUID = Header(...),
):
    """Get_companies_by_radius"""
    api_repo = DBRepository(model=ApiKey, session=session)
    await check_api_key(api_repo, api_key)

    # честно - подсмотрел как делается
    db_repo = DBRepository(model=Company, session=session)

    Building = Company.building.property.mapper.class_

    EARTH_RADIUS = 6371

    distance_expr = EARTH_RADIUS * func.acos(
        func.cos(func.radians(map_lat))
        * func.cos(func.radians(Building.latitude))
        * func.cos(func.radians(Building.longitude) - func.radians(map_lng))
        + func.sin(func.radians(map_lat)) * func.sin(func.radians(Building.latitude))
    )

    building_subquery = select(Building.id).where(distance_expr <= radius).subquery()

    result = await db_repo.list(Company.building_id.in_(select(building_subquery.c.id)))

    return result


@router.get("/company/get_by_activity", response_model=List[CompanyScheme])
async def get_company_activity_all(  # type: ignore
    activity: str,
    session: AsyncSession = Depends(get_session),
    api_key: uuid.UUID = Header(...),
):
    """Get all companies activities (subactivities, double subactivities)"""
    api_repo = DBRepository(model=ApiKey, session=session)
    await check_api_key(api_repo, api_key)

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
    api_key: uuid.UUID = Header(...),
):
    """Get company by activity"""
    api_repo = DBRepository(model=ApiKey, session=session)
    await check_api_key(api_repo, api_key)

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
    api_key: uuid.UUID = Header(...),
):
    """Get Company by Building"""
    api_repo = DBRepository(model=ApiKey, session=session)
    await check_api_key(api_repo, api_key)

    db_repo = DBRepository(model=Company, session=session)
    companies = await db_repo.list(Company.building.has(Building.address == address))
    return companies


@router.get("/company/get_by_id", response_model=CompanyScheme)
async def get_company_by_uuid(  # type: ignore
    company_id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
    api_key: uuid.UUID = Header(...),
):
    """Get Company by ID"""
    api_repo = DBRepository(model=ApiKey, session=session)
    await check_api_key(api_repo, api_key)

    db_repo = DBRepository(model=Company, session=session)
    company = await db_repo.get(id=company_id)
    return company


@router.get("/company/get_by_name", response_model=CompanyScheme)
async def get_company_by_name(  # type: ignore
    name: str,
    session: AsyncSession = Depends(get_session),
    api_key: uuid.UUID = Header(...),
):
    """Get Company by Name"""
    api_repo = DBRepository(model=ApiKey, session=session)
    await check_api_key(api_repo, api_key)

    db_repo = DBRepository(model=Company, session=session)
    company = await db_repo.get(name=name)
    return company


@router.get(
    "/company/list",
    response_model=List[CompanyScheme],
)
async def get_company_list(  # type: ignore
    session: AsyncSession = Depends(get_session),
    api_key: uuid.UUID = Header(...),
):
    """List all companies"""
    api_repo = DBRepository(model=ApiKey, session=session)
    await check_api_key(api_repo, api_key)

    db_repo = DBRepository(model=Company, session=session)
    result = await db_repo.list()
    return result
