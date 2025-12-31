"""
Tokenization: Understanding LLM Input/Output
Critical for cost and latency management.
"""

import tiktoken


def understand_tokens():
    """Understanding what tokens are."""
    print("=== Understanding Tokens ===")
    
    # Tokens are not characters or words
    text = "Hello, how are you?"
    
    # Count characters
    char_count = len(text)
    print(f"Text: '{text}'")
    print(f"Characters: {char_count}")
    
    # Count words
    word_count = len(text.split())
    print(f"Words: {word_count}")
    
    # Count tokens (approximate)
    # 1 token ≈ 4 characters for English
    approx_tokens = char_count / 4
    print(f"Approximate tokens: {approx_tokens:.1f}")
    
    print("\nKey points:")
    print("- Tokens are sub-word units (not characters or words)")
    print("- Different models use different tokenizers")
    print("- Token count determines cost and context window limits")


def context_window():
    """Understanding context windows."""
    print("\n=== Context Window ===")
    
    # Common context window sizes
    context_windows = {
        "GPT-3.5-turbo": 4096,
        "GPT-4": 8192,
        "GPT-4-turbo": 128000,
        "Claude-3": 200000,
    }
    
    print("Context Window Sizes (tokens):")
    for model, size in context_windows.items():
        print(f"  {model}: {size:,} tokens")
    
    # Calculate what fits
    example_text = "This is a sample text. " * 100
    approx_tokens = len(example_text) / 4
    
    print(f"\nExample text length: {len(example_text)} characters")
    print(f"Approximate tokens: {approx_tokens:.1f}")
    
    for model, size in context_windows.items():
        fits = "✓" if approx_tokens < size else "✗"
        print(f"  {model}: {fits} ({size - approx_tokens:.1f} tokens remaining)")
    
    print("\nContext window includes:")
    print("- System prompt")
    print("- User prompt")
    print("- Assistant response")
    print("- Conversation history (in chat mode)")


def cost_calculation():
    """Calculating LLM API costs."""
    print("\n=== Cost Calculation ===")
    
    # Example pricing (hypothetical, check actual API pricing)
    pricing = {
        "input": 0.0015,  # $ per 1K tokens
        "output": 0.002,   # $ per 1K tokens
    }
    
    # Example request
    system_prompt = "You are a helpful assistant." * 10
    user_prompt = "Explain quantum computing." * 20
    response = "Quantum computing is..." * 30
    
    # Approximate token counts
    input_tokens = (len(system_prompt) + len(user_prompt)) / 4
    output_tokens = len(response) / 4
    
    # Calculate cost
    input_cost = (input_tokens / 1000) * pricing["input"]
    output_cost = (output_tokens / 1000) * pricing["output"]
    total_cost = input_cost + output_cost
    
    print(f"Input tokens: {input_tokens:.0f}")
    print(f"Output tokens: {output_tokens:.0f}")
    print(f"Total tokens: {input_tokens + output_tokens:.0f}")
    print(f"\nCost:")
    print(f"  Input: ${input_cost:.6f}")
    print(f"  Output: ${output_cost:.6f}")
    print(f"  Total: ${total_cost:.6f}")
    
    print("\nCost optimization tips:")
    print("- Minimize system prompt length")
    print("- Use shorter user prompts when possible")
    print("- Set max_tokens to limit response length")
    print("- Cache common responses")
    print("- Use cheaper models when appropriate")


def latency_considerations():
    """Understanding latency factors."""
    print("\n=== Latency Considerations ===")
    
    factors = {
        "Input tokens": "More tokens = longer processing time",
        "Model size": "Larger models = slower inference",
        "Output length": "Longer responses = more time",
        "API load": "High traffic = slower responses",
        "Network": "Distance to API = network latency",
    }
    
    print("Factors affecting latency:")
    for factor, explanation in factors.items():
        print(f"  {factor}: {explanation}")
    
    print("\nLatency optimization:")
    print("- Use smaller models for faster responses")
    print("- Limit max_tokens for shorter outputs")
    print("- Implement caching for repeated queries")
    print("- Use streaming for better perceived latency")
    print("- Consider local models for very low latency")


def token_counting_example():
    """Practical token counting example."""
    print("\n=== Token Counting Example ===")
    
    try:
        # Use tiktoken for accurate token counting (OpenAI models)
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        
        text = "Hello, how are you? I'm learning about LLMs."
        tokens = encoding.encode(text)
        
        print(f"Text: '{text}'")
        print(f"Character count: {len(text)}")
        print(f"Word count: {len(text.split())}")
        print(f"Token count: {len(tokens)}")
        print(f"Tokens: {tokens}")
        
        print("\nToken breakdown:")
        for i, token_id in enumerate(tokens):
            token_str = encoding.decode([token_id])
            print(f"  Token {i+1}: {token_id} → '{token_str}'")
        
    except Exception as e:
        print(f"Note: tiktoken example (install with: pip install tiktoken)")
        print(f"Error: {e}")


if __name__ == "__main__":
    understand_tokens()
    context_window()
    cost_calculation()
    latency_considerations()
    token_counting_example()
    
    print("\n=== Key Takeaways ===")
    print("1. Tokens determine cost and context limits")
    print("2. Always check context window size")
    print("3. Monitor token usage for cost control")
    print("4. Optimize prompts to reduce tokens")
    print("5. Consider latency when choosing models")

