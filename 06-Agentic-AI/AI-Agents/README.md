# AI Agents

## Overview

This project covers building **AI Agents** - autonomous systems that can use tools, make decisions, and interact with the world. This is the future of AI: not just prompt engineering, but agents that actually do work.

## Why This Matters for AI Engineers

**"After 2026, those who build agents that do work will win, not those who write prompts."**

Agents represent the next evolution:
- **Tool Calling:** Agents can interact with external systems
- **Function Calling:** Structured, type-safe tool execution
- **Orchestration:** Coordinating multiple tools and APIs
- **Frameworks:** LangGraph, CrewAI, AutoGen for building agents
- **Production Concerns:** Determinism, retry, rollback, hallucinations

## Learning Objectives

By completing this project, you will:

1. Understand tool calling and function calling
2. Orchestrate multiple API calls in agents
3. Choose and use agent frameworks (LangGraph, CrewAI, AutoGen)
4. Balance determinism and autonomy
5. Implement retry and rollback mechanisms
6. Prevent tool hallucination
7. Build agent workflows with LangGraph

## Project Structure

```
AI-Agents/
├── README.md
├── requirements.txt
├── tool_calling.py          # Tool/function calling concepts
└── langgraph_basics.py     # LangGraph workflow building
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API keys (optional):**
   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

3. **Run examples:**
   ```bash
   # Tool calling concepts
   python tool_calling.py
   
   # LangGraph basics
   python langgraph_basics.py
   ```

## Key Concepts

### Tool Calling

**What it is:** LLMs can call external functions/tools to perform actions

**How it works:**
1. Define tools (functions agent can call)
2. LLM decides which tool to use
3. Execute tool with parameters
4. Return result to LLM
5. LLM generates response

**Use cases:**
- Search the web
- Execute code
- Call APIs
- Manipulate files
- Control devices

### Function Calling

**What it is:** Specific implementation of tool calling with structured output

**Benefits:**
- Structured output (JSON)
- Type-safe parameters
- Reliable execution
- Easy to validate

**Flow:**
1. User query
2. LLM decides to call function
3. LLM returns function call (JSON)
4. System executes function
5. System returns result
6. LLM generates final response

### API Orchestration

**Patterns:**
- **Sequential:** Call APIs one after another
- **Parallel:** Call multiple APIs simultaneously
- **Conditional:** Call APIs based on previous results
- **Retry:** Retry failed API calls

**Best practices:**
- Handle failures gracefully
- Set timeouts
- Cache results
- Rate limit

### Agent Frameworks

#### LangGraph
- **Type:** State machine for agents
- **Best for:** Complex workflows, production
- **Key feature:** Graph-based orchestration
- **Use case:** Production agent systems

#### CrewAI
- **Type:** Multi-agent framework
- **Best for:** Collaborative agents
- **Key feature:** Role-based agents
- **Use case:** Multi-agent systems

#### AutoGen
- **Type:** Conversational framework
- **Best for:** Agent-to-agent communication
- **Key feature:** Multi-agent conversations
- **Use case:** Research, complex problems

### Determinism vs Autonomy

**Determinism:**
- Predictable, controlled
- Fixed workflow
- More reliable
- Less flexible

**Autonomy:**
- Agent makes decisions
- Dynamic workflow
- More flexible
- Less predictable

**Balance:**
- High-stakes: More deterministic
- Creative tasks: More autonomous
- Production: Controlled autonomy

### Retry & Rollback

**Retry strategies:**
- Immediate retry (transient errors)
- Exponential backoff (rate limits)
- Max retries (avoid loops)
- Different approach (if first fails)

**Rollback:**
- Undo actions if later steps fail
- Transaction-like behavior
- State restoration
- Compensation actions

### Tool Hallucination

**What it is:** LLM calls non-existent tools or uses wrong parameters

**Prevention:**
- Validate tool calls
- Use structured schemas
- Clear tool descriptions
- Limit available tools
- Add validation layers

### LangGraph Basics

**Concepts:**
- **Nodes:** States in workflow
- **Edges:** Transitions between states
- **State:** Shared data
- **Conditional edges:** Dynamic routing

**Benefits:**
- Explicit control flow
- Easy to debug
- Production-ready
- Handles complex workflows

## Common Pitfalls

1. **No validation:** Tool hallucinations break agents
2. **No retry logic:** Transient failures crash agents
3. **Too much autonomy:** Unpredictable behavior
4. **No rollback:** Failed steps leave system in bad state
5. **Ignoring frameworks:** Reinventing the wheel
6. **No human oversight:** Critical actions need approval

## Production Notes

- Always validate tool calls before execution
- Implement retry with exponential backoff
- Add rollback mechanisms for critical actions
- Use LangGraph for production agent systems
- Balance determinism and autonomy
- Add human-in-the-loop for critical decisions
- Monitor agent behavior and tool usage
- Log all tool calls for debugging

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

