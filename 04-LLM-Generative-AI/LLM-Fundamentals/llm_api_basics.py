"""
LLM API Basics: Working with LLM APIs
Practical examples for production use.
"""

import os
from typing import Optional


def openai_api_example():
    """
    Example OpenAI API call structure.
    Note: Requires OPENAI_API_KEY environment variable.
    """
    print("=== OpenAI API Example ===")
    
    # API call structure (pseudo-code, actual implementation requires API key)
    api_call_structure = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain Python decorators."}
        ],
        "temperature": 0.7,
        "max_tokens": 500,
    }
    
    print("API Call Structure:")
    print(f"  Model: {api_call_structure['model']}")
    print(f"  Messages: {len(api_call_structure['messages'])} messages")
    print(f"  Temperature: {api_call_structure['temperature']}")
    print(f"  Max tokens: {api_call_structure['max_tokens']}")
    
    print("\nKey parameters:")
    print("- model: Which LLM to use")
    print("- messages: Conversation history (system, user, assistant)")
    print("- temperature: Controls randomness (0.0 = deterministic, 2.0 = very random)")
    print("- max_tokens: Maximum response length")
    
    print("\nTo use in production:")
    print("1. Set OPENAI_API_KEY environment variable")
    print("2. Install: pip install openai")
    print("3. Use OpenAI client library")


def error_handling():
    """Error handling for LLM API calls."""
    print("\n=== Error Handling ===")
    
    common_errors = {
        "Rate limit": "Too many requests - implement retry with exponential backoff",
        "Invalid API key": "Check API key configuration",
        "Context length exceeded": "Reduce prompt length or use model with larger context",
        "Timeout": "Request took too long - implement timeout handling",
        "Invalid request": "Check request format and parameters",
    }
    
    print("Common errors and solutions:")
    for error, solution in common_errors.items():
        print(f"  {error}: {solution}")
    
    print("\nBest practices:")
    print("- Always implement retry logic")
    print("- Use exponential backoff for rate limits")
    print("- Set appropriate timeouts")
    print("- Log errors for debugging")
    print("- Have fallback responses")


def streaming_responses():
    """Understanding streaming responses."""
    print("\n=== Streaming Responses ===")
    
    print("Standard response:")
    print("  - Wait for complete response")
    print("  - Higher perceived latency")
    print("  - Simpler implementation")
    
    print("\nStreaming response:")
    print("  - Receive tokens as they're generated")
    print("  - Lower perceived latency")
    print("  - Better user experience")
    print("  - More complex implementation")
    
    print("\nUse streaming when:")
    print("- Response time is important")
    print("- Building chat interfaces")
    print("- Long responses expected")
    
    print("\nImplementation:")
    print("- Set stream=True in API call")
    print("- Process chunks as they arrive")
    print("- Handle partial responses")


def temperature_guidelines():
    """Temperature settings for different tasks."""
    print("\n=== Temperature Guidelines ===")
    
    temperature_settings = {
        "0.0 - 0.3": "Deterministic, factual tasks (classification, extraction)",
        "0.4 - 0.7": "Balanced, creative but controlled (general Q&A, writing)",
        "0.8 - 1.2": "Creative tasks (storytelling, brainstorming)",
        "1.3 - 2.0": "Very creative, high randomness (experimental)",
    }
    
    print("Temperature ranges and use cases:")
    for temp_range, use_case in temperature_settings.items():
        print(f"  {temp_range}: {use_case}")
    
    print("\nProduction recommendations:")
    print("- Start with 0.7 for most tasks")
    print("- Use lower (0.2-0.5) for factual/structured outputs")
    print("- Use higher (0.8-1.0) for creative tasks")
    print("- Test different values and measure results")


if __name__ == "__main__":
    openai_api_example()
    error_handling()
    streaming_responses()
    temperature_guidelines()
    
    print("\n=== Production Checklist ===")
    print("✓ Set up API keys securely (environment variables)")
    print("✓ Implement error handling and retries")
    print("✓ Monitor token usage and costs")
    print("✓ Use appropriate temperature settings")
    print("✓ Consider streaming for better UX")
    print("✓ Version your prompts")
    print("✓ Log requests and responses for debugging")

