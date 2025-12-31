"""
Type Hints for AI Engineering
Essential for maintainability in large AI projects.
"""

from typing import List, Dict, Optional, Union, Callable, Tuple
from pydantic import BaseModel


# Basic type hints
def process_text(text: str) -> str:
    """Simple function with type hints."""
    return text.lower().strip()


def calculate_embedding(text: str, model_name: str = "text-embedding-ada-002") -> List[float]:
    """Returns embedding vector for text."""
    # In production, this would call an actual embedding API
    return [0.1, 0.2, 0.3]  # Mock embedding


# Complex type hints
def batch_process_texts(
    texts: List[str],
    processor: Callable[[str], str]
) -> List[str]:
    """Process multiple texts with a processor function."""
    return [processor(text) for text in texts]


def create_embedding_dict(
    texts: List[str],
    model: str = "default"
) -> Dict[str, List[float]]:
    """Create dictionary mapping text to embeddings."""
    return {text: calculate_embedding(text, model) for text in texts}


# Optional and Union types
def find_entity(
    text: str,
    entity_type: Optional[str] = None
) -> Union[str, None]:
    """Find entity in text, optionally filtered by type."""
    if entity_type:
        return f"Found {entity_type} in {text}"
    return None


# Tuple return types
def split_text_and_metadata(text: str) -> Tuple[str, Dict[str, str]]:
    """Split text and return with metadata."""
    metadata = {"length": len(text), "words": len(text.split())}
    return text, metadata


# Using Pydantic models (best practice for complex data)
class EmbeddingResult(BaseModel):
    """Type-safe embedding result."""
    text: str
    embedding: List[float]
    model: str
    dimensions: int


def get_typed_embedding(text: str) -> EmbeddingResult:
    """Returns type-safe embedding result."""
    embedding = calculate_embedding(text)
    return EmbeddingResult(
        text=text,
        embedding=embedding,
        model="text-embedding-ada-002",
        dimensions=len(embedding)
    )


if __name__ == "__main__":
    # Type hints help with IDE autocomplete and error detection
    result = process_text("  HELLO WORLD  ")
    print(f"Processed: {result}")
    
    embedding = calculate_embedding("sample text")
    print(f"Embedding dimensions: {len(embedding)}")
    
    texts = ["text1", "text2", "text3"]
    processed = batch_process_texts(texts, process_text)
    print(f"Batch processed: {processed}")
    
    typed_result = get_typed_embedding("example")
    print(f"Typed result: {typed_result}")

