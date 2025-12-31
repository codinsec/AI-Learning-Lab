# Agentic AI

## Overview

This section covers **Agentic AI** - autonomous AI systems that can use tools, make decisions, and interact with the world. This is the future: **"After 2026, those who build agents that do work will win, not those who write prompts."**

## Section Structure

This section contains two projects:

### AI Agents
**Location:** `AI-Agents/`

Covers building autonomous agents:
- Tool calling and function calling
- API orchestration
- Agent frameworks (LangGraph, CrewAI, AutoGen)
- Determinism vs autonomy
- Retry and rollback mechanisms
- Tool hallucination prevention
- LangGraph workflows

### State & Memory Management
**Location:** `State-Memory-Management/`

Covers agent memory and state:
- Short-term memory (conversation context)
- Long-term memory (persistent storage)
- Vector-based memory (semantic search)
- SQL-based state (structured data)
- Human-in-the-loop (approvals, clarification)

## Learning Path

1. **Start with AI Agents** - Learn tool calling and frameworks
2. **Master LangGraph** - Build production agent workflows
3. **Understand Memory** - Implement different memory types
4. **Add Human Oversight** - Approval gates and error handling

## Prerequisites

- Section 01 completed (Python & Math Fundamentals)
- Section 02 completed (Machine Learning Basics)
- Section 03 completed (Deep Learning & PyTorch)
- Section 04 completed (LLM & Generative AI)
- Section 05 completed (RAG Systems)

## Time Estimate

**7-9 months** for thorough understanding and practice.

## Key Learning Principles

1. **Agents do work:** Not just prompts, but actual actions
2. **Balance autonomy:** Determinism vs autonomy based on task
3. **Handle failures:** Retry, rollback, human escalation
4. **Memory matters:** Agents need to remember and learn
5. **Human oversight:** Critical actions need approval

## Common Questions

**Q: Do I need to learn all frameworks?**  
A: Start with LangGraph for production. Others are useful for specific use cases.

**Q: How much autonomy should agents have?**  
A: Depends on task. High-stakes = more control, creative = more autonomy.

**Q: Is human-in-the-loop necessary?**  
A: For critical actions, yes. For low-risk tasks, optional.

**Q: How do I prevent tool hallucinations?**  
A: Validate tool calls, use structured schemas, limit available tools.

## Next Steps

After completing this section, you'll move to:
- **Section 07:** Production, MLOps & AI Security (deploying agents to production)

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

