"""OpenAI service for handling AI recipe generation."""

import logging
import json
from typing import Dict, Any, List, Optional
import openai
from openai import AsyncOpenAI

from app.config import settings
from app.models import Recipe

logger = logging.getLogger(__name__)


class OpenAIService:
    """Service for interacting with OpenAI API."""
    
    def __init__(self) -> None:
        """Initialize OpenAI client."""
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
    
    async def generate_recipe(self, ingredients: List[str], preferences: Optional[str] = None) -> Recipe:
        """
        Generate a recipe using OpenAI GPT-4.
        
        Args:
            ingredients: List of ingredients
            preferences: User preferences
            
        Returns:
            A Recipe object
            
        Raises:
            Exception: If OpenAI API call fails or response is invalid
        """
        try:
            prompt = self._build_prompt(ingredients, preferences)
            logger.info("Generating recipe for ingredients: %s", ingredients)
            
            response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self._get_system_message()},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1024,
                temperature=0.7,
                response_format={"type": "json_object"}
            )
            
            raw_response = response.choices[0].message.content
            if not raw_response:
                raise ValueError("Received an empty response from OpenAI.")
                
            recipe_data = self._parse_recipe(raw_response)
            logger.info("Recipe generated successfully: %s", recipe_data.get('name'))
            
            return Recipe(**recipe_data)
            
        except (openai.APIError, ValueError) as e:
            logger.error("Error generating recipe: %s", str(e))
            raise Exception("Failed to generate recipe from OpenAI")
            
        except Exception as e:
            logger.error("Unexpected error in OpenAI service: %s", str(e))
            raise Exception("An unexpected error occurred while generating the recipe")

    def _build_prompt(self, ingredients: List[str], preferences: Optional[str]) -> str:
        """Build the prompt for the OpenAI API."""
        prompt = f"Ingredients: {', '.join(ingredients)}."
        if preferences:
            prompt += f"\nPreferences: {preferences}."
        return prompt

    def _get_system_message(self) -> str:
        """Get the system message for the OpenAI API."""
        return (
            "You are a master chef. Based on the ingredients and preferences provided, "
            "generate a recipe with a creative name, a list of ingredients, and cooking steps. "
            "Provide the output in a JSON object with keys 'name', 'ingredients', and 'steps'."
        )

    def _parse_recipe(self, response: str) -> Dict[str, Any]:
        """Parse the JSON response from OpenAI."""
        try:
            recipe_dict = json.loads(response)
            if not all(k in recipe_dict for k in ['name', 'ingredients', 'steps']):
                raise ValueError("Invalid JSON structure from OpenAI.")
            return recipe_dict
        except json.JSONDecodeError:
            raise ValueError("Failed to decode JSON from OpenAI response.")


# Global service instance
openai_service = OpenAIService()
