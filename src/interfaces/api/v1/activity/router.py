from fastapi import APIRouter

from src.interfaces.api.v1.activity.endpoints.activity_type import activity_type_router
from src.interfaces.api.v1.activity.endpoints.sub_activity import sub_activity_router

activity_router = APIRouter(prefix="/activity")
activity_router.include_router(activity_type_router)
activity_router.include_router(sub_activity_router)
