"""
Tool Calling: Enabling AI Agents to Interact with the World
Understanding how agents use tools to perform actions.
"""


def tool_calling_concept():
    """Understanding tool calling."""
    print("=== Tool Calling Concept ===")
    
    print("Tool calling allows LLMs to interact with external systems:")
    print("  - Search the web")
    print("  - Execute code")
    print("  - Call APIs")
    print("  - Manipulate files")
    print("  - Control devices")
    
    print("\nHow it works:")
    print("1. Define tools (functions the agent can call)")
    print("2. LLM decides which tool to use based on user query")
    print("3. Execute tool with parameters")
    print("4. Return result to LLM")
    print("5. LLM uses result to generate response")
    
    print("\nExample tool definition:")
    print("""
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get current weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City name"
                        }
                    },
                    "required": ["location"]
                }
            }
        }
    ]
    """)


def function_calling():
    """Function calling vs tool calling."""
    print("\n=== Function Calling ===")
    
    print("Function calling is a specific implementation of tool calling.")
    print("LLM is given function definitions and can 'call' them.")
    
    print("\nFunction calling flow:")
    print("1. User: 'What's the weather in Istanbul?'")
    print("2. LLM: Decides to call get_weather function")
    print("3. LLM: Returns function call with parameters")
    print("   {")
    print('     "name": "get_weather",')
    print('     "arguments": {"location": "Istanbul"}')
    print("   }")
    print("4. System: Executes function")
    print("5. System: Returns result to LLM")
    print("6. LLM: Generates final response using result")
    
    print("\nBenefits:")
    print("  - Structured output (JSON)")
    print("  - Type-safe parameters")
    print("  - Reliable execution")
    print("  - Easy to validate")


def api_orchestration():
    """API orchestration in agents."""
    print("\n=== API Orchestration ===")
    
    print("Agents often need to orchestrate multiple API calls:")
    
    print("\nExample: Travel planning agent")
    print("1. Search flights API")
    print("2. Search hotels API")
    print("3. Get weather API")
    print("4. Combine results")
    print("5. Generate recommendation")
    
    print("\nOrchestration patterns:")
    print("  - Sequential: Call APIs one after another")
    print("  - Parallel: Call multiple APIs simultaneously")
    print("  - Conditional: Call APIs based on previous results")
    print("  - Retry: Retry failed API calls")
    
    print("\nBest practices:")
    print("  - Handle API failures gracefully")
    print("  - Set timeouts for API calls")
    print("  - Cache results when possible")
    print("  - Rate limit to avoid overwhelming APIs")


def agent_frameworks():
    """Overview of agent frameworks."""
    print("\n=== Agent Frameworks ===")
    
    frameworks = {
        "LangGraph": {
            "Type": "State machine for agents",
            "Best for": "Complex workflows, multi-step agents",
            "Key feature": "Graph-based agent orchestration",
            "Use case": "Production agent systems",
        },
        "CrewAI": {
            "Type": "Multi-agent framework",
            "Best for": "Collaborative agents, team workflows",
            "Key feature": "Role-based agents working together",
            "Use case": "Multi-agent systems",
        },
        "AutoGen": {
            "Type": "Conversational agent framework",
            "Best for": "Agent-to-agent communication",
            "Key feature": "Multi-agent conversations",
            "Use case": "Research, complex problem solving",
        },
    }
    
    print("Popular agent frameworks:")
    for framework, details in frameworks.items():
        print(f"\n{framework}:")
        for key, value in details.items():
            print(f"  {key}: {value}")
    
    print("\nSelection guide:")
    print("  - LangGraph: Complex workflows, production")
    print("  - CrewAI: Multi-agent collaboration")
    print("  - AutoGen: Research, agent conversations")


def determinism_vs_autonomy():
    """Balancing determinism and autonomy."""
    print("\n=== Determinism vs Autonomy ===")
    
    print("Determinism: Predictable, controlled behavior")
    print("  - Fixed workflow")
    print("  - Limited choices")
    print("  - More reliable")
    print("  - Less flexible")
    
    print("\nAutonomy: Agent makes its own decisions")
    print("  - Dynamic workflow")
    print("  - Many choices")
    print("  - More flexible")
    print("  - Less predictable")
    
    print("\nBalance:")
    print("  - High-stakes actions: More deterministic")
    print("  - Creative tasks: More autonomous")
    print("  - Production systems: Controlled autonomy")
    print("  - Research/experimentation: Full autonomy")
    
    print("\nImplementation:")
    print("  - Approval gates for critical actions")
    print("  - Constrained action spaces")
    print("  - Validation before execution")
    print("  - Human-in-the-loop for important decisions")


def retry_rollback():
    """Retry and rollback mechanisms."""
    print("\n=== Retry & Rollback ===")
    
    print("Agents need to handle failures gracefully:")
    
    print("\nRetry strategies:")
    print("  1. Immediate retry (transient errors)")
    print("  2. Exponential backoff (rate limits)")
    print("  3. Max retries (avoid infinite loops)")
    print("  4. Different approach (if first fails)")
    
    print("\nRollback mechanisms:")
    print("  - Undo actions if later steps fail")
    print("  - Transaction-like behavior")
    print("  - State restoration")
    print("  - Compensation actions")
    
    print("\nExample:")
    print("""
    try:
        result = call_api()
    except APIError:
        if retry_count < max_retries:
            wait(exponential_backoff(retry_count))
            retry()
        else:
            rollback_previous_actions()
            notify_user()
    """)


def tool_hallucination():
    """Tool hallucination risks."""
    print("\n=== Tool Hallucination Risks ===")
    
    print("Tool hallucination: LLM 'calls' non-existent tools or uses wrong parameters")
    
    print("\nCommon issues:")
    print("  1. Calling tools that don't exist")
    print("  2. Using wrong parameter names")
    print("  3. Invalid parameter values")
    print("  4. Calling tools in wrong order")
    
    print("\nPrevention:")
    print("  - Validate tool calls before execution")
    print("  - Use structured schemas (JSON Schema)")
    print("  - Provide clear tool descriptions")
    print("  - Limit available tools per step")
    print("  - Add validation layers")
    
    print("\nExample validation:")
    print("""
    def validate_tool_call(tool_call):
        # Check tool exists
        if tool_call.name not in available_tools:
            raise ValueError(f"Tool {tool_call.name} not found")
        
        # Validate parameters
        schema = get_tool_schema(tool_call.name)
        validate_against_schema(tool_call.parameters, schema)
        
        # Check parameter types
        for param, value in tool_call.parameters.items():
            expected_type = schema['properties'][param]['type']
            if not isinstance(value, expected_type):
                raise TypeError(f"{param} must be {expected_type}")
    """)


if __name__ == "__main__":
    tool_calling_concept()
    function_calling()
    api_orchestration()
    agent_frameworks()
    determinism_vs_autonomy()
    retry_rollback()
    tool_hallucination()
    
    print("\n=== Key Takeaways ===")
    print("1. Tool calling enables agents to interact with the world")
    print("2. Function calling provides structured, type-safe tool execution")
    print("3. Choose framework based on use case (LangGraph for production)")
    print("4. Balance determinism and autonomy based on task")
    print("5. Always implement retry and rollback mechanisms")
    print("6. Validate tool calls to prevent hallucinations")

