"""
LangGraph: Building Agent Workflows
Understanding LangGraph for production agent systems.
"""


def langgraph_concept():
    """Understanding LangGraph."""
    print("=== LangGraph Concept ===")
    
    print("LangGraph: State machine for building agent workflows")
    
    print("\nKey concepts:")
    print("  - Nodes: States in the workflow")
    print("  - Edges: Transitions between states")
    print("  - State: Shared data across nodes")
    print("  - Conditional edges: Dynamic routing")
    
    print("\nWhy LangGraph?")
    print("  - Explicit control flow")
    print("  - Easy to debug")
    print("  - Production-ready")
    print("  - Handles complex workflows")
    
    print("\nBasic structure:")
    print("""
    from langgraph.graph import StateGraph
    
    # Define state
    class AgentState(TypedDict):
        messages: list
        tools: list
    
    # Create graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", tools_node)
    
    # Add edges
    workflow.add_edge("agent", "tools")
    workflow.add_conditional_edges("tools", should_continue)
    
    # Compile
    app = workflow.compile()
    """)


def agent_workflow_example():
    """Example agent workflow."""
    print("\n=== Agent Workflow Example ===")
    
    print("Simple agent workflow:")
    print("""
    1. User Input
       ↓
    2. Agent Node (LLM decides action)
       ↓
    3. Tool Node? (if tool needed)
       ↓
    4. Continue or End?
       ↓
    5. Final Response
    """)
    
    print("\nState flow:")
    print("  - Start: User query")
    print("  - Agent: LLM processes query")
    print("  - Tools: Execute if needed")
    print("  - Check: More actions needed?")
    print("  - End: Return final answer")
    
    print("\nBenefits:")
    print("  - Clear execution path")
    print("  - Easy to add logging")
    print("  - Can pause/resume")
    print("  - Human-in-the-loop support")


def conditional_routing():
    """Conditional routing in LangGraph."""
    print("\n=== Conditional Routing ===")
    
    print("Conditional edges allow dynamic routing based on state:")
    
    print("\nExample:")
    print("""
    def should_continue(state):
        last_message = state["messages"][-1]
        
        if hasattr(last_message, "tool_calls"):
            return "tools"  # Go to tools node
        else:
            return "end"  # Finish
    
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "tools": "tools",
            "end": END
        }
    )
    """)
    
    print("\nUse cases:")
    print("  - Route based on tool calls")
    print("  - Handle errors differently")
    print("  - Multi-step workflows")
    print("  - Human approval gates")


def human_in_the_loop():
    """Human-in-the-loop with LangGraph."""
    print("\n=== Human-in-the-Loop ===")
    
    print("LangGraph supports pausing for human input:")
    
    print("\nImplementation:")
    print("""
    # Add interrupt point
    workflow.add_node("human_approval", human_approval_node)
    
    # Interrupt before critical action
    workflow.add_edge("agent", "human_approval")
    workflow.add_edge("human_approval", "tools")
    
    # In human_approval_node:
    def human_approval_node(state):
        # Pause and wait for human input
        return interrupt("human_approval")
    """)
    
    print("\nUse cases:")
    print("  - Approval for critical actions")
    print("  - Clarification needed")
    print("  - Error handling")
    print("  - Quality control")


def state_management():
    """State management in LangGraph."""
    print("\n=== State Management ===")
    
    print("State is shared across all nodes:")
    
    print("\nState structure:")
    print("""
    class AgentState(TypedDict):
        messages: list  # Conversation history
        tools: list     # Available tools
        user_id: str    # User identifier
        session_id: str # Session identifier
        metadata: dict  # Additional data
    """)
    
    print("\nState updates:")
    print("  - Nodes read from state")
    print("  - Nodes update state")
    print("  - State persists across nodes")
    print("  - Can checkpoint state")
    
    print("\nBest practices:")
    print("  - Keep state minimal")
    print("  - Use typed state (TypedDict)")
    print("  - Don't mutate state directly")
    print("  - Return updated state")


if __name__ == "__main__":
    langgraph_concept()
    agent_workflow_example()
    conditional_routing()
    human_in_the_loop()
    state_management()
    
    print("\n=== LangGraph Best Practices ===")
    print("1. Start simple, add complexity gradually")
    print("2. Use typed state for clarity")
    print("3. Add logging at each node")
    print("4. Handle errors gracefully")
    print("5. Test workflows thoroughly")
    print("6. Use interrupts for human approval")

