"""
Threading vs Multiprocessing for AI Tasks
Understanding when to use each for CPU-bound vs IO-bound operations.
"""

import threading
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def cpu_bound_task(n: int) -> int:
    """
    CPU-bound task: embedding computation, matrix multiplication.
    Use multiprocessing for this.
    """
    result = 0
    for i in range(n):
        result += i ** 2
    return result


def io_bound_task(delay: float = 0.1) -> str:
    """
    IO-bound task: API calls, file I/O, network requests.
    Use threading for this.
    """
    time.sleep(delay)  # Simulates network/disk I/O
    return f"IO task completed after {delay}s"


def demonstrate_threading():
    """Threading is good for IO-bound tasks (API calls, file I/O)."""
    print("=== Threading for IO-bound tasks ===")
    start = time.time()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(io_bound_task, 0.1) for _ in range(5)]
        results = [f.result() for f in futures]
    
    elapsed = time.time() - start
    print(f"Threading took: {elapsed:.3f}s (parallel IO operations)")
    print(f"Results: {results}")


def demonstrate_multiprocessing():
    """Multiprocessing is good for CPU-bound tasks (embeddings, computations)."""
    print("\n=== Multiprocessing for CPU-bound tasks ===")
    start = time.time()
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_bound_task, 1000000) for _ in range(4)]
        results = [f.result() for f in futures]
    
    elapsed = time.time() - start
    print(f"Multiprocessing took: {elapsed:.3f}s (parallel CPU operations)")
    print(f"Results sum: {sum(results)}")


def sequential_io_tasks():
    """Sequential approach - slow for IO-bound tasks."""
    print("\n=== Sequential IO tasks (for comparison) ===")
    start = time.time()
    results = [io_bound_task(0.1) for _ in range(5)]
    elapsed = time.time() - start
    print(f"Sequential took: {elapsed:.3f}s")


if __name__ == "__main__":
    sequential_io_tasks()
    demonstrate_threading()
    demonstrate_multiprocessing()
    
    print("\n=== Key Takeaways ===")
    print("Threading: Use for IO-bound tasks (API calls, file I/O)")
    print("Multiprocessing: Use for CPU-bound tasks (embeddings, computations)")
    print("Async/Await: Best for concurrent IO-bound tasks (LLM API calls)")

