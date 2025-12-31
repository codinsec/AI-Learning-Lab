"""
Embeddings and Retrieval
Understanding how embeddings enable semantic search.
"""

import numpy as np


def embedding_concept():
    """Understanding embeddings for RAG."""
    print("=== Embedding Concept ===")
    
    print("Embeddings convert text into numerical vectors.")
    print("Similar texts have similar embeddings (close in vector space).")
    
    # Simulated embeddings
    text1 = "Python programming"
    text2 = "Coding in Python"
    text3 = "Cooking recipes"
    
    # Mock embeddings (in practice, use embedding model)
    embedding1 = np.array([0.8, 0.6, 0.4, 0.2])
    embedding2 = np.array([0.7, 0.5, 0.5, 0.3])  # Similar to embedding1
    embedding3 = np.array([-0.2, -0.3, 0.1, 0.8])  # Different
    
    print(f"\nText 1: '{text1}'")
    print(f"Text 2: '{text2}'")
    print(f"Text 3: '{text3}'")
    
    # Cosine similarity
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    sim_12 = cosine_similarity(embedding1, embedding2)
    sim_13 = cosine_similarity(embedding1, embedding3)
    
    print(f"\nSimilarity (1, 2): {sim_12:.3f} (high - similar topics)")
    print(f"Similarity (1, 3): {sim_13:.3f} (low - different topics)")
    
    print("\nIn RAG:")
    print("1. Convert documents to embeddings (store in vector DB)")
    print("2. Convert query to embedding")
    print("3. Find most similar document embeddings")
    print("4. Retrieve corresponding text chunks")


def embedding_model_selection():
    """Choosing the right embedding model."""
    print("\n=== Embedding Model Selection ===")
    
    models = {
        "OpenAI text-embedding-ada-002": {
            "Dimensions": 1536,
            "Context": 8191 tokens,
            "Use case": "General purpose, good quality",
        },
        "sentence-transformers/all-MiniLM-L6-v2": {
            "Dimensions": 384,
            "Context": 256 tokens,
            "Use case": "Fast, local, smaller embeddings",
        },
        "sentence-transformers/all-mpnet-base-v2": {
            "Dimensions": 768,
            "Context": 384 tokens,
            "Use case": "Better quality, still local",
        },
    }
    
    print("Common embedding models:")
    for model, specs in models.items():
        print(f"\n{model}:")
        for key, value in specs.items():
            print(f"  {key}: {value}")
    
    print("\nSelection criteria:")
    print("  - Quality vs speed trade-off")
    print("  - Embedding dimensions (affects storage)")
    print("  - Context window size")
    print("  - Cost (API vs local)")
    print("  - Language support")


def vector_search():
    """How vector search works in RAG."""
    print("\n=== Vector Search ===")
    
    print("RAG Retrieval Process:")
    print("1. Query: 'What is Python?'")
    print("2. Convert query to embedding")
    print("3. Search vector database for similar embeddings")
    print("4. Retrieve top-k most similar chunks")
    print("5. Pass chunks + query to LLM for answer")
    
    # Simulated search
    query_embedding = np.array([0.8, 0.6, 0.4, 0.2])
    
    # Document embeddings (stored in vector DB)
    doc_embeddings = [
        (np.array([0.7, 0.5, 0.5, 0.3]), "Python is a programming language..."),
        (np.array([0.6, 0.4, 0.6, 0.2]), "Python syntax is simple..."),
        (np.array([-0.2, -0.3, 0.1, 0.8]), "Cooking recipes are..."),
    ]
    
    # Calculate similarities
    similarities = []
    for i, (doc_emb, text) in enumerate(doc_embeddings):
        sim = np.dot(query_embedding, doc_emb) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(doc_emb)
        )
        similarities.append((sim, text))
    
    # Sort by similarity
    similarities.sort(reverse=True, key=lambda x: x[0])
    
    print("\nTop results (by similarity):")
    for i, (sim, text) in enumerate(similarities[:2]):
        print(f"  {i+1}. Similarity: {sim:.3f}")
        print(f"     Text: {text[:50]}...")


def hybrid_search():
    """Hybrid search: Combining keyword and vector search."""
    print("\n=== Hybrid Search ===")
    
    print("Hybrid Search = BM25 (keyword) + Vector Search (semantic)")
    
    print("\nBM25 (Keyword Search):")
    print("  - Finds exact keyword matches")
    print("  - Good for specific terms, names, dates")
    print("  - Fast and efficient")
    
    print("\nVector Search (Semantic):")
    print("  - Finds semantically similar content")
    print("  - Good for concepts, synonyms, meaning")
    print("  - Captures intent")
    
    print("\nHybrid Approach:")
    print("  1. Run both BM25 and vector search")
    print("  2. Combine results (weighted or reciprocal rank fusion)")
    print("  3. Get best of both worlds")
    
    print("\nUse cases:")
    print("  - BM25: Specific product names, codes, dates")
    print("  - Vector: Conceptual questions, synonyms")
    print("  - Hybrid: Production systems (best results)")


def reranking():
    """Re-ranking for better retrieval quality."""
    print("\n=== Re-ranking ===")
    
    print("Re-ranking improves retrieval quality:")
    print("1. Initial retrieval: Get top-k candidates (e.g., 100)")
    print("2. Re-rank: Use cross-encoder to score query-document pairs")
    print("3. Final results: Return top-n re-ranked results (e.g., 5)")
    
    print("\nWhy re-ranking?")
    print("  - Initial retrieval is fast but approximate")
    print("  - Re-ranking is slower but more accurate")
    print("  - Best of both: Fast retrieval + accurate ranking")
    
    print("\nRe-ranking models:")
    print("  - Cross-encoders: More accurate, slower")
    print("  - Bi-encoders: Faster, less accurate")
    print("  - Use cross-encoders for final ranking")
    
    print("\nProduction tip:")
    print("  Retrieve 50-100 candidates, re-rank to top 5-10")


if __name__ == "__main__":
    embedding_concept()
    embedding_model_selection()
    vector_search()
    hybrid_search()
    reranking()
    
    print("\n=== Key Takeaways ===")
    print("1. Embeddings enable semantic search")
    print("2. Choose embedding model based on quality/speed needs")
    print("3. Hybrid search combines keyword + semantic")
    print("4. Re-ranking improves final results")
    print("5. Test different combinations for your use case")

