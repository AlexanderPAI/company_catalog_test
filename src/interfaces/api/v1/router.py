from fastapi import APIRouter

from src.interfaces.api.v1.building.endpoints import building_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(building_router)
