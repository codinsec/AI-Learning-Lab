"""
Prompt Engineering: Getting the Best from LLMs
Understanding different prompting techniques.
"""


def zero_shot_prompting():
    """
    Zero-shot: No examples, just the task.
    LLM uses its pre-trained knowledge.
    """
    print("=== Zero-Shot Prompting ===")
    
    prompt = """
    Classify the sentiment of the following text as positive, negative, or neutral:
    
    Text: "I love this product! It works perfectly."
    Sentiment:
    """
    
    print(prompt)
    print("\nZero-shot: No examples provided, LLM uses general knowledge")
    print("Use case: Simple tasks, general knowledge questions")


def few_shot_prompting():
    """
    Few-shot: Provide examples to guide the LLM.
    Helps with specific formats or domain knowledge.
    """
    print("\n=== Few-Shot Prompting ===")
    
    prompt = """
    Classify the sentiment of the following text as positive, negative, or neutral.
    
    Examples:
    Text: "This is amazing!" → Sentiment: positive
    Text: "I hate this." → Sentiment: negative
    Text: "It's okay." → Sentiment: neutral
    
    Now classify:
    Text: "I love this product! It works perfectly."
    Sentiment:
    """
    
    print(prompt)
    print("\nFew-shot: Examples guide the LLM to desired format/behavior")
    print("Use case: Specific formats, domain-specific tasks, consistency")


def chain_of_thought():
    """
    Chain-of-Thought: Ask LLM to show its reasoning.
    Improves accuracy for complex problems.
    """
    print("\n=== Chain-of-Thought (CoT) ===")
    
    prompt = """
    Solve this math problem step by step:
    
    Problem: A store has 15 apples. They sell 6 apples in the morning and 4 apples in the afternoon. How many apples are left?
    
    Let's think step by step:
    1. Start with 15 apples
    2. Subtract 6 apples sold in the morning: 15 - 6 = 9
    3. Subtract 4 apples sold in the afternoon: 9 - 4 = 5
    4. Answer: 5 apples are left
    """
    
    print(prompt)
    print("\nChain-of-Thought: LLM shows reasoning process")
    print("Use case: Complex problems, math, logic, multi-step tasks")
    print("Benefit: More accurate results, easier to debug")


def role_prompting():
    """
    Role Prompting: Assign a role to the LLM.
    Helps LLM adopt specific perspective or expertise.
    """
    print("\n=== Role Prompting ===")
    
    prompt = """
    You are an expert Python developer with 10 years of experience.
    Your task is to review code and provide constructive feedback.
    
    Code:
    def add(a, b):
        return a + b
    
    Review:
    """
    
    print(prompt)
    print("\nRole Prompting: Assigns specific role/expertise to LLM")
    print("Use case: Domain-specific tasks, consistent tone, expert perspective")
    print("Benefit: More focused and relevant responses")


def system_vs_user_prompt():
    """
    System Prompt vs User Prompt: Understanding the difference.
    Critical for production LLM applications.
    """
    print("\n=== System Prompt vs User Prompt ===")
    
    system_prompt = """
    You are a helpful AI assistant specialized in Python programming.
    Always provide clear, concise explanations with code examples.
    """
    
    user_prompt = "Explain how decorators work in Python."
    
    print("System Prompt (instructions, behavior, constraints):")
    print(f'"{system_prompt}"')
    print("\nUser Prompt (actual question/task):")
    print(f'"{user_prompt}"')
    print("\nKey differences:")
    print("- System prompt: Sets behavior, tone, constraints (persistent)")
    print("- User prompt: Actual question/task (changes per request)")
    print("- System prompt: Usually not counted in token limits (depends on API)")
    print("- Best practice: Put instructions in system prompt, questions in user prompt")


def prompt_versioning():
    """
    Prompt Versioning: Managing prompt changes.
    Critical for production systems.
    """
    print("\n=== Prompt Versioning ===")
    
    # Version 1
    prompt_v1 = "Classify this text as positive or negative: {text}"
    
    # Version 2 (improved)
    prompt_v2 = """
    Classify the sentiment of the following text.
    Consider context and nuance.
    
    Text: {text}
    
    Sentiment (positive/negative/neutral):
    """
    
    print("Version 1:")
    print(f'"{prompt_v1}"')
    print("\nVersion 2 (improved):")
    print(f'"{prompt_v2}"')
    print("\nWhy versioning matters:")
    print("- Track which prompts perform best")
    print("- A/B test different versions")
    print("- Rollback if performance degrades")
    print("- Understand impact of prompt changes")
    print("\nBest practices:")
    print("- Store prompts in version control")
    print("- Log which version was used for each request")
    print("- Monitor performance metrics per version")


if __name__ == "__main__":
    zero_shot_prompting()
    few_shot_prompting()
    chain_of_thought()
    role_prompting()
    system_vs_user_prompt()
    prompt_versioning()
    
    print("\n=== Prompt Engineering Best Practices ===")
    print("1. Start with zero-shot, add examples if needed")
    print("2. Use CoT for complex reasoning tasks")
    print("3. Separate system and user prompts")
    print("4. Version your prompts for production")
    print("5. Test and iterate based on results")

