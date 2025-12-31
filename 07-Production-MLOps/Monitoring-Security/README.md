# Monitoring & Security

## Overview

This project covers **monitoring and security** for production AI systems. This is critical for maintaining reliable, secure, and cost-effective AI applications.

## Why This Matters for AI Engineers

Production AI systems need:
- **Monitoring:** Track performance, costs, and errors
- **Tracing:** Debug issues with LangSmith
- **Security:** Protect against attacks (prompt injection, jailbreak)
- **Cost Control:** Monitor and optimize spending
- **Performance:** Track latency and throughput

## Learning Objectives

By completing this project, you will:

1. Use LangSmith for tracing LLM calls
2. Monitor latency, tokens, and costs
3. Understand AI security threats
4. Implement defenses against prompt injection
5. Prevent jailbreak attacks
6. Protect against data leakage
7. Set up security monitoring

## Project Structure

```
Monitoring-Security/
├── README.md
├── requirements.txt
├── monitoring.py          # LangSmith, metrics, costs
└── ai_security.py        # Security threats and defenses
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up LangSmith (optional):**
   ```bash
   export LANGCHAIN_TRACING_V2=true
   export LANGCHAIN_API_KEY="your-key"
   ```

3. **Run examples:**
   ```bash
   python monitoring.py
   python ai_security.py
   ```

## Key Concepts

### LangSmith Tracing

**What it is:** Observability platform for LLM applications

**Tracks:**
- All LLM calls (inputs, outputs)
- Latency per call
- Token usage
- Costs
- Errors
- Chain/tool execution

**Benefits:**
- Debug issues quickly
- Optimize prompts
- Monitor costs
- Track performance
- A/B test prompts

### Latency Metrics

**Key metrics:**
- **P50 (median):** 50% of requests faster
- **P95:** 95% of requests faster
- **P99:** 99% of requests faster
- **Average:** Mean latency
- **Max:** Slowest request

**Optimization:**
- Use smaller models
- Limit max_tokens
- Use caching
- Optimize prompts

### Token Metrics

**Track:**
- Input tokens (prompt)
- Output tokens (response)
- Total tokens
- Cost per request
- Aggregated usage (daily/weekly/monthly)

**Why it matters:**
- Directly affects costs
- Helps optimize prompts
- Identifies expensive operations

### Cost Monitoring

**Track at multiple levels:**
- Per request
- Per user
- Per endpoint
- Per model
- Per time period

**Optimization:**
- Use cheaper models
- Shorter prompts
- Limit response length
- Cache responses
- Monitor and alert

### AI Security

#### Prompt Injection
**What it is:** Malicious input that manipulates LLM behavior

**Types:**
- Direct injection (user input)
- Indirect injection (retrieved documents)
- Code injection
- Instruction override

**Defense:**
- Input validation
- Separate system/user prompts
- Output filtering
- Monitoring

#### Jailbreak Attacks
**What it is:** Bypassing safety guardrails

**Techniques:**
- Role-playing
- Hypothetical scenarios
- Encoding/obfuscation
- Multi-step reasoning

**Defense:**
- Strong safety training
- Input filtering
- Output moderation
- Monitoring

#### Data Leakage
**What it is:** Unauthorized exposure of sensitive data

**Vectors:**
- Training data memorization
- Prompt exposure
- Retrieved documents
- Conversation history

**Prevention:**
- Don't include sensitive data in prompts
- Filter retrieved documents
- Sanitize outputs
- Access controls
- Encryption

## Common Pitfalls

1. **No monitoring:** Can't debug or optimize
2. **No cost tracking:** Unexpected bills
3. **No security:** Vulnerable to attacks
4. **No input validation:** Prompt injection attacks
5. **No output filtering:** Data leakage
6. **Ignoring alerts:** Issues go unnoticed

## Production Notes

- Set up LangSmith for all LLM calls
- Monitor latency (P50, P95, P99)
- Track token usage and costs
- Set up alerts for anomalies
- Validate and sanitize all inputs
- Filter outputs for sensitive content
- Implement rate limiting
- Regular security audits
- Have incident response plan

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

