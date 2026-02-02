from fastapi import APIRouter

from src.interfaces.api.v1.endpoints import v1_router

main_router = APIRouter()
main_router.include_router(v1_router)
