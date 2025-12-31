# LLM & Generative AI Fundamentals

## Overview

This project covers Large Language Models (LLMs) and Generative AI from an AI Engineer's perspective. This is where **70% of what's called "AI Engineering" today** happens - working with LLMs effectively.

## Why This Matters for AI Engineers

LLMs are the foundation of modern AI applications:
- **Prompt Engineering:** Getting the best results from LLMs
- **Tokenization:** Understanding costs and limitations
- **Context Windows:** Managing input/output limits
- **API Integration:** Building production LLM applications

## Learning Objectives

By completing this project, you will:

1. Master prompt engineering techniques (zero-shot, few-shot, CoT, role prompting)
2. Understand tokenization and context windows
3. Calculate costs and optimize for latency
4. Differentiate between system and user prompts
5. Implement prompt versioning for production
6. Work with LLM APIs effectively

## Project Structure

```
LLM-Fundamentals/
├── README.md
├── requirements.txt
├── prompt_engineering.py    # Prompting techniques
├── tokenization.py          # Tokens, context windows, costs
└── llm_api_basics.py        # API integration basics
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API key (optional, for actual API calls):**
   ```bash
   export OPENAI_API_KEY="your-key-here"
   # Or create .env file with OPENAI_API_KEY=your-key-here
   ```

3. **Run examples:**
   ```bash
   # Prompt engineering techniques
   python prompt_engineering.py
   
   # Tokenization and costs
   python tokenization.py
   
   # API basics
   python llm_api_basics.py
   ```

## Key Concepts

### Prompt Engineering

#### Zero-Shot Prompting
- No examples provided
- LLM uses pre-trained knowledge
- Use for: Simple tasks, general knowledge

#### Few-Shot Prompting
- Provide examples to guide LLM
- Helps with specific formats
- Use for: Domain-specific tasks, consistent formatting

#### Chain-of-Thought (CoT)
- Ask LLM to show reasoning
- Improves accuracy for complex problems
- Use for: Math, logic, multi-step tasks

#### Role Prompting
- Assign specific role/expertise
- Helps LLM adopt perspective
- Use for: Domain expertise, consistent tone

### System vs User Prompt

**System Prompt:**
- Sets behavior, tone, constraints
- Usually persistent across conversation
- Not always counted in token limits (depends on API)

**User Prompt:**
- Actual question/task
- Changes per request
- Always counted in token limits

**Best Practice:** Put instructions in system prompt, questions in user prompt.

### Tokenization

- **Tokens:** Sub-word units (not characters or words)
- **Approximation:** 1 token ≈ 4 characters (English)
- **Context Window:** Maximum tokens model can handle
- **Cost:** Based on input + output tokens

### Context Windows

Common sizes:
- GPT-3.5-turbo: 4,096 tokens
- GPT-4: 8,192 tokens
- GPT-4-turbo: 128,000 tokens
- Claude-3: 200,000 tokens

**Includes:** System prompt + user prompt + response + conversation history

### Cost & Latency

**Cost factors:**
- Input tokens (prompt)
- Output tokens (response)
- Model pricing (varies by model)

**Latency factors:**
- Input token count
- Model size
- Output length
- API load
- Network distance

**Optimization:**
- Minimize prompt length
- Set max_tokens appropriately
- Use caching
- Consider streaming
- Choose right model for task

### Prompt Versioning

**Why it matters:**
- Track which prompts perform best
- A/B test different versions
- Rollback if performance degrades
- Understand impact of changes

**Best practices:**
- Store prompts in version control
- Log which version used per request
- Monitor performance metrics per version

## Common Pitfalls

1. **Not separating system and user prompts:** Harder to manage and optimize
2. **Ignoring token limits:** Requests fail or get truncated
3. **Not versioning prompts:** Can't track what works
4. **Wrong temperature:** Too high = random, too low = repetitive
5. **No error handling:** API failures break application
6. **Not monitoring costs:** Unexpected bills

## Production Notes

- Always use environment variables for API keys
- Implement retry logic with exponential backoff
- Monitor token usage and costs
- Version your prompts
- Use streaming for better UX
- Set appropriate timeouts
- Log requests/responses for debugging
- Cache common responses when possible
- Test different temperature settings

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

