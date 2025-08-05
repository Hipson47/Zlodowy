"""Pydantic models for request and response validation."""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class RecipeRequest(BaseModel):
    """Request model for recipe endpoint."""
    
    ingredients: List[str] = Field(..., min_length=1, max_length=10, description="List of ingredients")
    preferences: Optional[str] = Field(None, max_length=500, description="User preferences for the recipe")


class Recipe(BaseModel):
    """Recipe model."""
    
    name: str = Field(..., description="Recipe name")
    ingredients: List[str] = Field(..., description="List of ingredients")
    steps: List[str] = Field(..., description="List of cooking steps")


class RecipeResponse(BaseModel):
    """Response model for recipe endpoint."""
    
    recipe: Recipe
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""
    
    status: str = Field(default="healthy", description="Service status")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    version: str = Field(..., description="Application version")


class ErrorResponse(BaseModel):
    """Error response model."""
    
    detail: str = Field(..., description="Error message")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    error_code: Optional[str] = Field(None, description="Error code")