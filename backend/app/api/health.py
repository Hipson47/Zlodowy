"""Health check API endpoints."""

import logging
from fastapi import APIRouter

from app.models import HealthResponse
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/health", tags=["health"])


@router.get(
    "/",
    response_model=HealthResponse,
    summary="Health check",
    description="Check the health status of the API"
)
async def health_check() -> HealthResponse:
    """
    Check the health status of the API.
    
    Returns:
        HealthResponse: Health status with timestamp and version
    """
    logger.debug("Health check requested")
    
    return HealthResponse(
        status="healthy",
        version=settings.app_version
    ) 