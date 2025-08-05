"""Chat API endpoints."""

import logging
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.models import ChatRequest, ChatResponse, ErrorResponse
from app.services.openai_service import openai_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post(
    "/",
    response_model=ChatResponse,
    responses={
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
    summary="Send a message to AI",
    description="Send a message to the AI assistant and receive a response"
)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Send a message to the AI assistant.
    
    Args:
        request: Chat request containing the user message
        
    Returns:
        ChatResponse: AI response with timestamp
        
    Raises:
        HTTPException: If message processing fails
    """
    try:
        logger.info("Processing chat request: %s", request.message[:50])
        
        # Generate AI response
        ai_response = await openai_service.generate_response(request.message)
        
        # Create response
        response = ChatResponse(message=ai_response)
        
        logger.info("Chat request processed successfully")
        return response
        
    except Exception as e:
        logger.error("Error processing chat request: %s", str(e))
        
        error_response = ErrorResponse(
            detail="Failed to process chat request",
            error_code="CHAT_ERROR"
        )
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error_response.detail
        ) 