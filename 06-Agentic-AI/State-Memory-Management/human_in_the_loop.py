"""
Human-in-the-Loop: Approval Gates
Adding human oversight to agent systems.
"""


def human_approval_concept():
    """Understanding human-in-the-loop."""
    print("=== Human-in-the-Loop Concept ===")
    
    print("Human-in-the-loop: Pause agent for human input/approval")
    
    print("\nWhy it's needed:")
    print("  - Critical actions need approval")
    print("  - High-stakes decisions")
    print("  - Error handling")
    print("  - Quality control")
    print("  - Compliance requirements")
    
    print("\nWhen to use:")
    print("  - Financial transactions")
    print("  - Data deletion")
    print("  - External API calls (costly)")
    print("  - Unclear user intent")
    print("  - Error recovery")


def approval_gates():
    """Approval gates in agent workflows."""
    print("\n=== Approval Gates ===")
    
    print("Approval gates: Checkpoints requiring human approval")
    
    print("\nImplementation:")
    print("""
    def agent_workflow(state):
        # Step 1: Agent decides action
        action = agent.decide(state)
        
        # Step 2: Check if approval needed
        if requires_approval(action):
            # Pause and wait for approval
            approval = wait_for_human_approval(action)
            
            if approval == "approved":
                execute_action(action)
            else:
                return "Action cancelled"
        else:
            execute_action(action)
    """)
    
    print("\nApproval criteria:")
    print("  - Action type (e.g., delete, payment)")
    print("  - Cost threshold")
    print("  - Risk level")
    print("  - User preference")
    print("  - Compliance requirements")
    
    print("\nApproval flow:")
    print("  1. Agent proposes action")
    print("  2. System checks if approval needed")
    print("  3. If yes: Pause, notify human")
    print("  4. Human reviews and approves/rejects")
    print("  5. Agent continues or cancels")


def error_handling_with_human():
    """Error handling with human intervention."""
    print("\n=== Error Handling with Human ===")
    
    print("Human intervention for error recovery:")
    
    print("\nScenarios:")
    print("  1. Agent encounters error")
    print("  2. Automatic retry fails")
    print("  3. Escalate to human")
    print("  4. Human provides guidance")
    print("  5. Agent continues or adjusts")
    
    print("\nImplementation:")
    print("""
    try:
        result = agent.execute_action()
    except Error as e:
        if retry_count < max_retries:
            retry()
        else:
            # Escalate to human
            human_guidance = request_human_help(e)
            agent.adjust_strategy(human_guidance)
            retry()
    """)


def clarification_requests():
    """Requesting clarification from humans."""
    print("\n=== Clarification Requests ===")
    
    print("Agent requests clarification when intent is unclear:")
    
    print("\nWhen to request:")
    print("  - Ambiguous user query")
    print("  - Multiple possible interpretations")
    print("  - Missing required information")
    print("  - Conflicting requirements")
    
    print("\nExample:")
    print("""
    User: "Delete the file"
    
    Agent: "Which file? I found multiple files:")
    Agent: "  1. document.pdf"
    Agent: "  2. report.docx"
    Agent: "  3. notes.txt"
    Agent: "Please specify which file to delete."
    
    User: "document.pdf"
    
    Agent: [Deletes document.pdf]
    """)


def async_approval():
    """Asynchronous approval patterns."""
    print("\n=== Asynchronous Approval ===")
    
    print("Asynchronous: Agent continues, approval happens separately")
    
    print("\nPatterns:")
    print("  1. Agent pauses, waits for approval (synchronous)")
    print("  2. Agent continues, approval happens async (asynchronous)")
    print("  3. Agent proceeds with caution, approval retroactive")
    
    print("\nUse cases:")
    print("  - Synchronous: Critical, must wait")
    print("  - Asynchronous: Non-blocking, can continue")
    print("  - Retroactive: Low risk, can undo")
    
    print("\nImplementation:")
    print("""
    # Async approval
    def async_approval_flow(action):
        # Start approval process
        approval_request = create_approval_request(action)
        
        # Continue with low-risk steps
        agent.continue_workflow()
        
        # Check approval status later
        if approval_request.status == "approved":
            execute_action(action)
        elif approval_request.status == "rejected":
            rollback_or_cancel()
    """)


if __name__ == "__main__":
    human_approval_concept()
    approval_gates()
    error_handling_with_human()
    clarification_requests()
    async_approval()
    
    print("\n=== Best Practices ===")
    print("1. Use approval gates for critical actions")
    print("2. Escalate errors to humans when needed")
    print("3. Request clarification for ambiguous queries")
    print("4. Choose sync vs async based on risk")
    print("5. Make approval process clear and fast")
    print("6. Log all approvals for audit")

