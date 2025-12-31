"""
Pydantic for LLM Input/Output Validation
Prevents hallucinations and ensures type safety in AI systems.
"""

from pydantic import BaseModel, Field, validator
from typing import List, Optional
from enum import Enum


class Sentiment(str, Enum):
    """Sentiment classification enum."""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class LLMResponse(BaseModel):
    """
    Validates LLM output structure.
    Prevents hallucination by enforcing schema.
    """
    text: str = Field(..., min_length=1, max_length=1000)
    sentiment: Sentiment
    confidence: float = Field(..., ge=0.0, le=1.0)
    entities: List[str] = Field(default_factory=list)
    
    @validator('text')
    def text_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Text cannot be empty or whitespace')
        return v.strip()
    
    @validator('entities')
    def entities_must_be_unique(cls, v):
        if len(v) != len(set(v)):
            raise ValueError('Entities must be unique')
        return list(set(v))


class LLMRequest(BaseModel):
    """Validates LLM input before sending to API."""
    prompt: str = Field(..., min_length=1, max_length=2000)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=100, ge=1, le=4000)
    
    @validator('prompt')
    def prompt_must_be_safe(cls, v):
        # Basic safety check - in production, add more validation
        if len(v) < 1:
            raise ValueError('Prompt cannot be empty')
        return v


def validate_llm_output(raw_output: dict) -> LLMResponse:
    """
    Validates LLM output against schema.
    Raises ValidationError if output doesn't match expected structure.
    """
    try:
        return LLMResponse(**raw_output)
    except Exception as e:
        print(f"Validation failed: {e}")
        raise


def validate_llm_input(prompt: str, temperature: float = 0.7) -> LLMRequest:
    """Validates LLM input before API call."""
    return LLMRequest(prompt=prompt, temperature=temperature)


if __name__ == "__main__":
    # Valid input
    request = validate_llm_input("Analyze this text", temperature=0.8)
    print(f"Valid request: {request}")
    
    # Valid output
    valid_output = {
        "text": "This is a positive review",
        "sentiment": "positive",
        "confidence": 0.95,
        "entities": ["review", "product"]
    }
    response = validate_llm_output(valid_output)
    print(f"Valid response: {response}")
    
    # Invalid output (will raise ValidationError)
    try:
        invalid_output = {
            "text": "",  # Empty text
            "sentiment": "positive",
            "confidence": 1.5  # Invalid confidence (> 1.0)
        }
        validate_llm_output(invalid_output)
    except Exception as e:
        print(f"Caught validation error: {e}")

