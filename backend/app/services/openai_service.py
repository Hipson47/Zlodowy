"""OpenAI service for handling AI chat interactions."""

import logging
from typing import Optional
import openai
from openai import AsyncOpenAI

from app.config import settings

logger = logging.getLogger(__name__)


class OpenAIService:
    """Service for interacting with OpenAI API."""
    
    def __init__(self) -> None:
        """Initialize OpenAI client."""
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
    
    async def generate_response(self, message: str) -> str:
        """
        Generate AI response using OpenAI GPT-4.
        
        Args:
            message: User's input message
            
        Returns:
            AI generated response
            
        Raises:
            Exception: If OpenAI API call fails
        """
        try:
            logger.info("Generating AI response for message: %s", message[:50])
            
            response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant. Provide clear, concise, and accurate responses."
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                max_tokens=500,
                temperature=0.7,
            )
            
            ai_response = response.choices[0].message.content
            logger.info("AI response generated successfully")
            
            return ai_response or "I apologize, but I couldn't generate a response at this time."
            
        except openai.AuthenticationError as e:
            logger.error("OpenAI authentication error: %s", str(e))
            raise Exception("Authentication failed with OpenAI API")
            
        except openai.RateLimitError as e:
            logger.error("OpenAI rate limit error: %s", str(e))
            raise Exception("Rate limit exceeded for OpenAI API")
            
        except openai.APIError as e:
            logger.error("OpenAI API error: %s", str(e))
            raise Exception("OpenAI API error occurred")
            
        except Exception as e:
            logger.error("Unexpected error in OpenAI service: %s", str(e))
            raise Exception("Failed to generate AI response")


# Global service instance
openai_service = OpenAIService() 