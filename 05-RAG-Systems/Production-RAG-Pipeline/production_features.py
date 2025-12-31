"""
Production RAG Features
Advanced features for production RAG systems.
"""


def caching_strategy():
    """Caching for RAG systems."""
    print("=== Caching Strategy ===")
    
    print("Caching reduces costs and improves latency.")
    
    print("\nWhat to cache:")
    print("  1. Embeddings (expensive to compute)")
    print("  2. LLM responses (for common queries)")
    print("  3. Retrieved chunks (if query is similar)")
    
    print("\nCaching layers:")
    print("  - Embedding cache: Store document embeddings")
    print("  - Query cache: Store query-answer pairs")
    print("  - Chunk cache: Store retrieved chunks")
    
    print("\nImplementation:")
    print("  - Redis: Fast, in-memory cache")
    print("  - Key: Query hash or embedding hash")
    print("  - TTL: Set expiration based on data freshness needs")
    
    print("\nExample:")
    print("""
    import redis
    import hashlib
    
    redis_client = redis.Redis()
    
    def get_cached_response(query):
        query_hash = hashlib.md5(query.encode()).hexdigest()
        cached = redis_client.get(f"response:{query_hash}")
        if cached:
            return cached
        return None
    
    def cache_response(query, response):
        query_hash = hashlib.md5(query.encode()).hexdigest()
        redis_client.setex(f"response:{query_hash}", 3600, response)
    """)


def multi_tenant_rag():
    """Multi-tenant RAG systems."""
    print("\n=== Multi-Tenant RAG ===")
    
    print("Multi-tenant: Multiple users/orgs share infrastructure.")
    
    print("\nChallenges:")
    print("  1. Data isolation (users can't see each other's data)")
    print("  2. Performance (one tenant shouldn't affect others)")
    print("  3. Cost allocation (track usage per tenant)")
    print("  4. Customization (different models/configs per tenant)")
    
    print("\nSolutions:")
    print("  - Separate collections per tenant (ChromaDB)")
    print("  - Namespace/partition per tenant (Pinecone)")
    print("  - Metadata filtering (filter by tenant_id)")
    print("  - Rate limiting per tenant")
    
    print("\nImplementation:")
    print("""
    # Add tenant_id to metadata
    collection.add(
        embeddings=embeddings,
        documents=documents,
        metadatas=[{"tenant_id": "org_123", ...}],
        ids=ids
    )
    
    # Filter by tenant_id when querying
    results = collection.query(
        query_embeddings=query_emb,
        n_results=10,
        where={"tenant_id": "org_123"}  # Isolate data
    )
    """)


def permission_based_retrieval():
    """Permission-based retrieval."""
    print("\n=== Permission-Based Retrieval ===")
    
    print("Control access to documents based on user permissions.")
    
    print("\nUse cases:")
    print("  - User can only see their own documents")
    print("  - Role-based access (admin, user, guest)")
    print("  - Department-based access")
    print("  - Time-based access (expired documents)")
    
    print("\nImplementation:")
    print("  1. Store permissions in metadata")
    print("  2. Filter by permissions during retrieval")
    print("  3. Apply permissions before LLM generation")
    
    print("\nExample:")
    print("""
    # Store with permissions
    collection.add(
        embeddings=embeddings,
        documents=documents,
        metadatas=[
            {
                "user_id": "user_123",
                "department": "engineering",
                "access_level": "internal"
            }
        ],
        ids=ids
    )
    
    # Query with permission filter
    results = collection.query(
        query_embeddings=query_emb,
        n_results=10,
        where={
            "$or": [
                {"user_id": current_user_id},
                {"department": user_department},
                {"access_level": "public"}
            ]
        }
    )
    """)


def monitoring_rag():
    """Monitoring RAG systems."""
    print("\n=== Monitoring RAG Systems ===")
    
    print("Key metrics to monitor:")
    
    metrics = {
        "Retrieval metrics": [
            "Query latency",
            "Chunks retrieved",
            "Similarity scores",
            "Cache hit rate",
        ],
        "Generation metrics": [
            "LLM response time",
            "Tokens used",
            "Cost per query",
            "Error rate",
        ],
        "Quality metrics": [
            "User feedback (thumbs up/down)",
            "Answer relevance",
            "Source citation accuracy",
        ],
    }
    
    for category, items in metrics.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  - {item}")
    
    print("\nImplementation:")
    print("  - Log all queries and responses")
    print("  - Track metrics in time-series DB (e.g., Prometheus)")
    print("  - Set up alerts for anomalies")
    print("  - Dashboard for visualization")


def error_handling_rag():
    """Error handling in RAG systems."""
    print("\n=== Error Handling ===")
    
    print("Common errors and handling:")
    
    errors = {
        "Vector DB timeout": "Retry with exponential backoff",
        "LLM API error": "Fallback to simpler model or cached response",
        "No relevant chunks": "Return 'no information found' message",
        "Embedding failure": "Use keyword search as fallback",
        "Context too long": "Reduce chunk count or use summarization",
    }
    
    for error, solution in errors.items():
        print(f"  {error}: {solution}")
    
    print("\nBest practices:")
    print("  - Always have fallback strategies")
    print("  - Implement circuit breakers")
    print("  - Log errors for debugging")
    print("  - Return user-friendly error messages")
    print("  - Monitor error rates")


if __name__ == "__main__":
    caching_strategy()
    multi_tenant_rag()
    permission_based_retrieval()
    monitoring_rag()
    error_handling_rag()
    
    print("\n=== Production RAG Checklist ===")
    print("✓ Implement caching (embeddings, responses)")
    print("✓ Support multi-tenancy (data isolation)")
    print("✓ Add permission-based retrieval")
    print("✓ Set up monitoring and alerting")
    print("✓ Implement error handling and fallbacks")
    print("✓ Test at scale before production")

