"""Tests for the main FastAPI application."""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "docs" in data


def test_health_endpoint():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data


@pytest.mark.asyncio
async def test_chat_endpoint_success():
    """Test the chat endpoint with successful response."""
    with patch('app.services.openai_service.openai_service.generate_response') as mock_generate:
        mock_generate.return_value = "Hello! How can I help you today?"
        
        response = client.post("/chat", json={"message": "Hello"})
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "timestamp" in data
        assert data["message"] == "Hello! How can I help you today?"


def test_chat_endpoint_invalid_request():
    """Test the chat endpoint with invalid request."""
    response = client.post("/chat", json={"message": ""})
    assert response.status_code == 422


def test_chat_endpoint_missing_message():
    """Test the chat endpoint with missing message."""
    response = client.post("/chat", json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_chat_endpoint_openai_error():
    """Test the chat endpoint with OpenAI API error."""
    with patch('app.services.openai_service.openai_service.generate_response') as mock_generate:
        mock_generate.side_effect = Exception("OpenAI API error")
        
        response = client.post("/chat", json={"message": "Hello"})
        assert response.status_code == 500
        data = response.json()
        assert "detail" in data 