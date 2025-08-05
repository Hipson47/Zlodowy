"""Recipe API endpoints."""

import logging
from fastapi import APIRouter, HTTPException, status, Body

from app.models import RecipeRequest, RecipeResponse, ErrorResponse
from app.services.openai_service import openai_service
from app.services.preferences_manager import preferences_manager

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/recipe", tags=["recipe"])


@router.post(
    "/",
    response_model=RecipeResponse,
    responses={
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
    summary="Generate a new recipe",
    description="Generate a new recipe based on a list of ingredients and user preferences"
)
async def generate_recipe(request: RecipeRequest) -> RecipeResponse:
    """
    Generate a new recipe from a list of ingredients.
    
    Args:
        request: Recipe request with ingredients and optional preferences.
        
    Returns:
        The generated recipe.
        
    Raises:
        HTTPException: If recipe generation fails.
    """
    try:
        user_id = "static_user"  # In a real app, this would be dynamic
        user_prefs = preferences_manager.get(user_id)
        
        # Combine request preferences with stored preferences
        combined_prefs = user_prefs.get('dietary', '') if user_prefs else ''
        if request.preferences:
            combined_prefs += f", {request.preferences}"
            
        recipe = await openai_service.generate_recipe(
            ingredients=request.ingredients,
            preferences=combined_prefs.strip(', ')
        )
        return RecipeResponse(recipe=recipe)
        
    except Exception as e:
        logger.error("Error generating recipe: %s", str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate recipe"
        )
