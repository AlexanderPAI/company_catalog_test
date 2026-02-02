from fastapi import APIRouter

from src.interfaces.api.v1.activity.router import activity_router
from src.interfaces.api.v1.building.endpoints import building_router
from src.interfaces.api.v1.company.endpoints import company_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(building_router)
v1_router.include_router(activity_router)
v1_router.include_router(company_router)
