"""Tests for the OpenAI service."""

import pytest
from unittest.mock import AsyncMock, patch
import openai

from app.services.openai_service import OpenAIService


@pytest.fixture
def openai_service():
    """Create OpenAI service instance for testing."""
    return OpenAIService()


@pytest.mark.asyncio
async def test_generate_response_success(openai_service):
    """Test successful response generation."""
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message.content = "Hello! How can I help you?"
    
    with patch.object(openai_service.client.chat.completions, 'create', return_value=mock_response):
        result = await openai_service.generate_response("Hello")
        assert result == "Hello! How can I help you?"


@pytest.mark.asyncio
async def test_generate_response_authentication_error(openai_service):
    """Test authentication error handling."""
    with patch.object(openai_service.client.chat.completions, 'create', side_effect=openai.AuthenticationError("Invalid API key")):
        with pytest.raises(Exception, match="Authentication failed with OpenAI API"):
            await openai_service.generate_response("Hello")


@pytest.mark.asyncio
async def test_generate_response_rate_limit_error(openai_service):
    """Test rate limit error handling."""
    with patch.object(openai_service.client.chat.completions, 'create', side_effect=openai.RateLimitError("Rate limit exceeded")):
        with pytest.raises(Exception, match="Rate limit exceeded for OpenAI API"):
            await openai_service.generate_response("Hello")


@pytest.mark.asyncio
async def test_generate_response_api_error(openai_service):
    """Test API error handling."""
    with patch.object(openai_service.client.chat.completions, 'create', side_effect=openai.APIError("API error")):
        with pytest.raises(Exception, match="OpenAI API error occurred"):
            await openai_service.generate_response("Hello")


@pytest.mark.asyncio
async def test_generate_response_empty_response(openai_service):
    """Test handling of empty response."""
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message.content = None
    
    with patch.object(openai_service.client.chat.completions, 'create', return_value=mock_response):
        result = await openai_service.generate_response("Hello")
        assert result == "I apologize, but I couldn't generate a response at this time." 