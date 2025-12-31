"""
Memory Types for AI Agents
Understanding different memory strategies.
"""


def short_term_memory():
    """Short-term memory: Conversation context."""
    print("=== Short-Term Memory ===")
    
    print("Short-term memory: Current conversation context")
    
    print("\nCharacteristics:")
    print("  - Limited to current session")
    print("  - Stored in conversation history")
    print("  - Lost when session ends")
    print("  - Fast access")
    
    print("\nImplementation:")
    print("""
    # Store messages in conversation
    conversation_history = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi! How can I help?"},
        {"role": "user", "content": "What's the weather?"},
    ]
    
    # Pass to LLM as context
    response = llm(conversation_history)
    """)
    
    print("\nUse cases:")
    print("  - Current conversation flow")
    print("  - Immediate context")
    print("  - Session-specific information")
    
    print("\nLimitations:")
    print("  - Context window limits")
    print("  - Lost between sessions")
    print("  - Can't recall past sessions")


def long_term_memory():
    """Long-term memory: Persistent storage."""
    print("\n=== Long-Term Memory ===")
    
    print("Long-term memory: Persistent storage across sessions")
    
    print("\nCharacteristics:")
    print("  - Persists across sessions")
    print("  - Stored in database")
    print("  - Can be retrieved later")
    print("  - Slower access")
    
    print("\nImplementation:")
    print("""
    # Store in database
    def save_memory(user_id, content, metadata):
        db.insert({
            "user_id": user_id,
            "content": content,
            "metadata": metadata,
            "timestamp": now()
        })
    
    # Retrieve later
    def get_memories(user_id, query):
        return db.search(user_id, query)
    """)
    
    print("\nUse cases:")
    print("  - User preferences")
    print("  - Past conversations")
    print("  - Learned facts")
    print("  - Personalization")
    
    print("\nBenefits:")
    print("  - Remembers across sessions")
    print("  - Builds user profile")
    print("  - Personalized responses")


def vector_based_memory():
    """Vector-based memory: Semantic search."""
    print("\n=== Vector-Based Memory ===")
    
    print("Vector-based memory: Store memories as embeddings")
    
    print("\nHow it works:")
    print("  1. Convert memories to embeddings")
    print("  2. Store in vector database")
    print("  3. Query by semantic similarity")
    print("  4. Retrieve relevant memories")
    
    print("\nImplementation:")
    print("""
    # Store memory
    memory_embedding = embedding_model.encode("User likes Python")
    vector_db.add(
        embedding=memory_embedding,
        text="User likes Python",
        metadata={"user_id": "123", "type": "preference"}
    )
    
    # Retrieve relevant memories
    query_embedding = embedding_model.encode("What does user like?")
    relevant = vector_db.search(query_embedding, top_k=5)
    """)
    
    print("\nBenefits:")
    print("  - Semantic search (finds related memories)")
    print("  - Handles synonyms and variations")
    print("  - Scales to many memories")
    print("  - Efficient retrieval")
    
    print("\nUse cases:")
    print("  - Finding relevant past conversations")
    print("  - User preference retrieval")
    print("  - Knowledge base search")


def sql_based_state():
    """SQL-based state: Structured data storage."""
    print("\n=== SQL-Based State ===")
    
    print("SQL-based state: Store structured state in database")
    
    print("\nUse cases:")
    print("  - User sessions")
    print("  - Agent state")
    print("  - Workflow state")
    print("  - Transaction data")
    
    print("\nImplementation:")
    print("""
    # State table
    CREATE TABLE agent_state (
        session_id VARCHAR PRIMARY KEY,
        user_id VARCHAR,
        current_step VARCHAR,
        state_data JSON,
        updated_at TIMESTAMP
    );
    
    # Save state
    def save_state(session_id, step, data):
        db.execute(
            "INSERT OR UPDATE agent_state SET current_step=?, state_data=?",
            (step, json.dumps(data))
        )
    
    # Load state
    def load_state(session_id):
        return db.query("SELECT * FROM agent_state WHERE session_id=?", (session_id,))
    """)
    
    print("\nBenefits:")
    print("  - Structured queries")
    print("  - ACID transactions")
    print("  - Easy to query")
    print("  - Reliable persistence")
    
    print("\nWhen to use:")
    print("  - Structured data")
    print("  - Need for queries")
    print("  - Transaction requirements")
    print("  - Relational data")


def memory_architecture():
    """Combining memory types."""
    print("\n=== Memory Architecture ===")
    
    print("Production systems often combine memory types:")
    
    print("\nArchitecture:")
    print("""
    ┌─────────────────┐
    │  Short-term     │  Current conversation
    │  (In-memory)    │  Fast, limited
    └─────────────────┘
           ↓
    ┌─────────────────┐
    │  Long-term      │  Past conversations
    │  (SQL DB)       │  Structured queries
    └─────────────────┘
           ↓
    ┌─────────────────┐
    │  Vector Memory  │  Semantic search
    │  (Vector DB)    │  Related memories
    └─────────────────┘
    """)
    
    print("\nFlow:")
    print("  1. Check short-term memory (conversation)")
    print("  2. If needed, query long-term memory (SQL)")
    print("  3. For semantic search, use vector memory")
    print("  4. Combine all memories for context")
    
    print("\nBest practices:")
    print("  - Use short-term for immediate context")
    print("  - Use SQL for structured queries")
    print("  - Use vector for semantic search")
    print("  - Combine based on query type")


if __name__ == "__main__":
    short_term_memory()
    long_term_memory()
    vector_based_memory()
    sql_based_state()
    memory_architecture()
    
    print("\n=== Key Takeaways ===")
    print("1. Short-term: Current conversation (fast, limited)")
    print("2. Long-term: Persistent storage (SQL, structured)")
    print("3. Vector: Semantic search (embeddings, related memories)")
    print("4. Combine types for production systems")
    print("5. Choose based on access patterns and query needs")

