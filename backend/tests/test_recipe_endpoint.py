"""Tests for the recipe API endpoint."""

import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient

from app.main import app
from app.models import Recipe

client = TestClient(app)


@pytest.fixture
def mock_openai_service():
    """Fixture to mock the OpenAI service."""
    with patch("app.api.chat.openai_service", new_callable=AsyncMock) as mock_service:
        yield mock_service


def test_generate_recipe_success(mock_openai_service):
    """Test successful recipe generation."""
    # Arrange
    mock_recipe = Recipe(
        name="Spaghetti Carbonara",
        ingredients=["Spaghetti", "Eggs", "Pancetta", "Parmesan Cheese", "Black Pepper"],
        steps=["Boil spaghetti.", "Fry pancetta.", "Mix eggs and cheese.", "Combine everything."]
    )
    mock_openai_service.generate_recipe.return_value = mock_recipe
    
    # Act
    response = client.post("/recipe/", json={
        "ingredients": ["Spaghetti", "Eggs", "Pancetta"],
        "preferences": "classic italian"
    })
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["recipe"]["name"] == "Spaghetti Carbonara"
    assert "timestamp" in data


def test_generate_recipe_openai_error(mock_openai_service):
    """Test handling of OpenAI service error."""
    # Arrange
    mock_openai_service.generate_recipe.side_effect = Exception("OpenAI API is down")
    
    # Act
    response = client.post("/recipe/", json={
        "ingredients": ["Chicken", "Broccoli"]
    })
    
    # Assert
    assert response.status_code == 500
    assert response.json() == {"detail": "Failed to generate recipe"}


def test_generate_recipe_invalid_payload(mock_openai_service):
    """Test with invalid request payload."""
    # Act
    response = client.post("/recipe/", json={"ingredients": []})  # Empty ingredients list
    
    # Assert
    assert response.status_code == 422  # Unprocessable Entity
