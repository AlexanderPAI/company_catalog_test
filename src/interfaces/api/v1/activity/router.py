from fastapi import APIRouter

from src.interfaces.api.v1.activity.sub_activity.endpoints import sub_activity_router

activity_router = APIRouter()
activity_router.include_router(sub_activity_router)
