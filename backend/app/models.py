"""Pydantic models for request and response validation."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    
    message: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="User message to send to AI"
    )


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    
    message: str = Field(..., description="AI response message")
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