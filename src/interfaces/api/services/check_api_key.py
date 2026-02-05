import uuid
from http import HTTPStatus

from fastapi import HTTPException

from src.infrastructure.db.models.auth_models import ApiKey
from src.infrastructure.repositories.db import DBRepository


async def check_api_key(api_repo: DBRepository[ApiKey], api_key: uuid.UUID) -> None:
    """Check if an API key is valid."""
    result = await api_repo.get(key=api_key)
    if result is None:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN)
