"""
Async/Await for LLM API Calls
Demonstrates why async is essential for IO-bound LLM operations.
"""

import asyncio
import time
from typing import List


async def mock_llm_api_call(prompt: str, delay: float = 0.5) -> str:
    """
    Simulates an LLM API call (IO-bound operation).
    In production, this would be an actual API call to OpenAI, Anthropic, etc.
    """
    await asyncio.sleep(delay)  # Simulates network latency
    return f"Response to: {prompt[:50]}..."


async def sequential_calls(prompts: List[str]) -> List[str]:
    """Sequential approach - slow for multiple calls."""
    results = []
    for prompt in prompts:
        result = await mock_llm_api_call(prompt)
        results.append(result)
    return results


async def concurrent_calls(prompts: List[str]) -> List[str]:
    """Concurrent approach - much faster for multiple calls."""
    tasks = [mock_llm_api_call(prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks)
    return results


async def main():
    prompts = [f"Prompt {i}" for i in range(5)]
    
    # Sequential approach
    start = time.time()
    sequential_results = await sequential_calls(prompts)
    sequential_time = time.time() - start
    print(f"Sequential calls took: {sequential_time:.2f} seconds")
    
    # Concurrent approach
    start = time.time()
    concurrent_results = await concurrent_calls(prompts)
    concurrent_time = time.time() - start
    print(f"Concurrent calls took: {concurrent_time:.2f} seconds")
    
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x faster")


if __name__ == "__main__":
    asyncio.run(main())

