# Modern Python for AI Engineering

## Overview

This project covers essential Python concepts at an **AI Engineer level**, not just basic Python. These skills are critical for building production-ready AI systems that interact with LLMs, manage resources efficiently, and handle concurrent operations.

## Why This Matters for AI Engineers

Traditional Python tutorials teach syntax, but AI Engineering requires:
- **Async/await** for handling multiple LLM API calls efficiently
- **Decorators** for retry logic, rate limiting, and logging
- **Context managers** for proper model lifecycle management (loading/unloading)
- **Pydantic** for validating LLM inputs/outputs and preventing hallucinations
- **Type hints** for maintainability in large AI codebases
- **Threading vs Multiprocessing** for CPU-bound vs IO-bound operations

## Learning Objectives

By completing this project, you will:

1. Understand when and why to use `async/await` for LLM API calls
2. Implement decorators for retry mechanisms and logging
3. Use context managers for proper resource management
4. Validate LLM inputs/outputs with Pydantic to prevent errors
5. Write type-safe code with type hints
6. Choose between threading and multiprocessing for different task types

## Project Structure

```
Modern-Python-AI-Engineering/
├── README.md
├── requirements.txt
├── async_llm_calls.py          # Async/await for concurrent API calls
├── decorators_retry.py          # Decorators for retry and logging
├── context_managers.py          # Resource management for models
├── pydantic_validation.py       # Input/output validation
├── threading_multiprocessing.py # When to use threading vs multiprocessing
└── type_hints.py                # Type safety for AI projects
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run individual examples:**
   ```bash
   # Async/await example
   python async_llm_calls.py
   
   # Decorators example
   python decorators_retry.py
   
   # Context managers example
   python context_managers.py
   
   # Pydantic validation example
   python pydantic_validation.py
   
   # Threading vs Multiprocessing
   python threading_multiprocessing.py
   
   # Type hints example
   python type_hints.py
   ```

## Key Concepts

### Async/Await
- **Why:** LLM API calls are IO-bound (waiting for network responses)
- **Benefit:** Can handle multiple API calls concurrently instead of sequentially
- **Example:** Making 10 API calls sequentially takes 5 seconds, concurrently takes 0.5 seconds

### Decorators
- **Why:** Reusable patterns for retry logic, rate limiting, logging
- **Benefit:** Clean separation of concerns, DRY principle
- **Example:** `@retry(max_attempts=3)` automatically retries failed API calls

### Context Managers
- **Why:** Models consume significant memory; must be loaded/unloaded properly
- **Benefit:** Automatic cleanup, exception-safe resource management
- **Example:** `with ModelManager("GPT-4") as model:` ensures model is unloaded even if an error occurs

### Pydantic Validation
- **Why:** LLMs can hallucinate or return unexpected formats
- **Benefit:** Type-safe validation prevents runtime errors
- **Example:** Validates that LLM response has required fields with correct types

### Type Hints
- **Why:** Large AI projects become unmaintainable without type information
- **Benefit:** IDE autocomplete, early error detection, self-documenting code
- **Example:** `def process_text(text: str) -> str:` makes function contract clear

### Threading vs Multiprocessing
- **Threading:** For IO-bound tasks (API calls, file I/O)
- **Multiprocessing:** For CPU-bound tasks (embedding computation, matrix multiplication)
- **Rule of thumb:** If it waits (IO), use threading. If it computes (CPU), use multiprocessing.

## Common Pitfalls

1. **Using sequential calls instead of async:** Wastes time waiting for API responses
2. **Not using context managers for models:** Memory leaks when models aren't unloaded
3. **Skipping validation:** LLM outputs can be unpredictable; always validate
4. **Ignoring type hints:** Makes code harder to maintain as projects grow
5. **Wrong concurrency model:** Using threading for CPU-bound tasks (or vice versa) wastes resources

## Production Notes

- Always use async/await for LLM API calls in production
- Implement retry logic with exponential backoff for API calls
- Use context managers for any resource that needs cleanup (models, connections, files)
- Validate all LLM inputs and outputs with Pydantic schemas
- Add type hints to all functions in production code
- Profile your code to identify bottlenecks before optimizing

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

