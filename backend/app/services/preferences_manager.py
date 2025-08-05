"""Service for managing user preferences."""

import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

# In-memory database for mock testing
MOCK_DB: Dict[str, Dict[str, str]] = {}


class PreferencesManager:
    """Manages user preferences."""

    def get(self, user_id: str) -> Optional[Dict[str, str]]:
        """
        Get preferences for a user.
        
        Args:
            user_id: The ID of the user.
        
        Returns:
            A dictionary of preferences or None if not found.
        """
        logger.info("Getting preferences for user %s", user_id)
        return MOCK_DB.get(user_id)

    def set(self, user_id: str, preferences: Dict[str, str]) -> None:
        """
        Set preferences for a user.
        
        Args:
            user_id: The ID of the user.
            preferences: A dictionary of preferences to set.
        """
        logger.info("Setting preferences for user %s", user_id)
        MOCK_DB[user_id] = preferences

    def clear(self, user_id: str) -> None:
        """
        Clear preferences for a user.
        
        Args:
            user_id: The ID of the user.
        """
        if user_id in MOCK_DB:
            logger.info("Clearing preferences for user %s", user_id)
            del MOCK_DB[user_id]


preferences_manager = PreferencesManager()
