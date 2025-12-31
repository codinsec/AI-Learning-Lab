"""
Context Managers for Model Lifecycle
Demonstrates proper resource management for AI models.
"""

from contextlib import contextmanager
from typing import Generator


class ModelManager:
    """Manages model loading and unloading lifecycle."""
    
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = None
        self.loaded = False
    
    def load(self):
        """Simulates model loading (memory-intensive operation)."""
        print(f"Loading {self.model_name}...")
        self.model = f"Loaded model: {self.model_name}"
        self.loaded = True
        print(f"{self.model_name} loaded successfully")
    
    def unload(self):
        """Simulates model unloading (frees memory)."""
        if self.loaded:
            print(f"Unloading {self.model_name}...")
            self.model = None
            self.loaded = False
            print(f"{self.model_name} unloaded")
    
    def __enter__(self):
        """Context manager entry."""
        self.load()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - always unloads model."""
        self.unload()
        return False  # Don't suppress exceptions


@contextmanager
def model_context(model_name: str) -> Generator[str, None, None]:
    """
    Context manager using @contextmanager decorator.
    More Pythonic for simple cases.
    """
    print(f"Loading {model_name}...")
    model = f"Loaded: {model_name}"
    try:
        yield model
    finally:
        print(f"Unloading {model_name}...")


def demonstrate_model_lifecycle():
    """Shows proper model lifecycle management."""
    
    # Method 1: Class-based context manager
    print("=== Method 1: Class-based Context Manager ===")
    with ModelManager("GPT-4") as manager:
        print(f"Using model: {manager.model}")
        # Model is automatically unloaded when exiting
    
    print("\n=== Method 2: Decorator-based Context Manager ===")
    with model_context("Claude-3") as model:
        print(f"Using model: {model}")
        # Model is automatically unloaded when exiting
    
    print("\n=== Without context manager (BAD PRACTICE) ===")
    manager = ModelManager("Mistral")
    manager.load()
    # If an exception occurs here, model might not be unloaded!
    # Always use context managers for resource management


if __name__ == "__main__":
    demonstrate_model_lifecycle()

