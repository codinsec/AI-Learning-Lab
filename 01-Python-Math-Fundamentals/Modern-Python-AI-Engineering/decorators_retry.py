"""
Decorators for AI Engineering
Demonstrates decorators for logging, rate limiting, and retry mechanisms.
"""

import time
import functools
from typing import Callable, Any


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Retry decorator for unreliable operations (e.g., API calls).
    Essential for production AI systems.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed.")
            raise last_exception
        return wrapper
    return decorator


def log_execution(func: Callable) -> Callable:
    """Log decorator for tracking function execution."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        print(f"Executing {func.__name__}...")
        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"{func.__name__} completed in {elapsed:.3f}s")
            return result
        except Exception as e:
            elapsed = time.time() - start
            print(f"{func.__name__} failed after {elapsed:.3f}s: {e}")
            raise
    return wrapper


@retry(max_attempts=3, delay=0.5)
@log_execution
def unreliable_api_call(success_on_attempt: int = 3) -> str:
    """Simulates an unreliable API call."""
    import random
    attempt = random.randint(1, 5)
    if attempt >= success_on_attempt:
        return "API call successful!"
    else:
        raise ConnectionError(f"API call failed (attempt {attempt})")


if __name__ == "__main__":
    # This will retry until successful
    result = unreliable_api_call(success_on_attempt=3)
    print(f"Result: {result}")

