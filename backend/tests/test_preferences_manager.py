"""Tests for the PreferencesManager service."""

import pytest
from app.services.preferences_manager import PreferencesManager, MOCK_DB


@pytest.fixture(autouse=True)
def clear_mock_db():
    """Clear the mock database before each test."""
    MOCK_DB.clear()


def test_set_and_get_preferences():
    """Test setting and getting user preferences."""
    # Arrange
    manager = PreferencesManager()
    user_id = "user123"
    prefs = {"diet": "vegetarian", "allergies": "nuts"}
    
    # Act
    manager.set(user_id, prefs)
    retrieved_prefs = manager.get(user_id)
    
    # Assert
    assert retrieved_prefs == prefs


def test_get_non_existent_preferences():
    """Test getting preferences for a user that does not exist."""
    # Arrange
    manager = PreferencesManager()
    
    # Act
    retrieved_prefs = manager.get("nonexistent_user")
    
    # Assert
    assert retrieved_prefs is None


def test_clear_preferences():
    """Test clearing preferences for a user."""
    # Arrange
    manager = PreferencesManager()
    user_id = "user123"
    prefs = {"diet": "vegan"}
    manager.set(user_id, prefs)
    
    # Act
    manager.clear(user_id)
    retrieved_prefs = manager.get(user_id)
    
    # Assert
    assert retrieved_prefs is None


def test_clear_non_existent_preferences():
    """Test clearing preferences for a user that does not exist."""
    # Arrange
    manager = PreferencesManager()
    
    # Act
    manager.clear("nonexistent_user")
    
    # Assert
    assert "nonexistent_user" not in MOCK_DB
