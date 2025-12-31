"""
Linear Algebra for AI
Intuitive understanding of vectors, matrices, and operations used in AI.
"""

import numpy as np


def dot_product_similarity():
    """
    Dot Product = Similarity Measure
    Core concept for embedding search and attention mechanisms.
    """
    print("=== Dot Product as Similarity ===")
    
    # Two vectors representing embeddings
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([2, 3, 4])  # Similar direction
    vec3 = np.array([-1, -2, -3])  # Opposite direction
    
    # Dot product
    similarity_12 = np.dot(vec1, vec2)
    similarity_13 = np.dot(vec1, vec3)
    
    print(f"Vector 1: {vec1}")
    print(f"Vector 2: {vec2} (similar direction)")
    print(f"Vector 3: {vec3} (opposite direction)")
    print(f"\nDot product (1, 2): {similarity_12} (higher = more similar)")
    print(f"Dot product (1, 3): {similarity_13} (lower = less similar)")
    
    # Intuition: Dot product is high when vectors point in similar directions


def cosine_similarity_embeddings():
    """
    Cosine Similarity = Normalized Dot Product
    The heart of embedding search in RAG systems.
    """
    print("\n=== Cosine Similarity for Embeddings ===")
    
    def cosine_similarity(a, b):
        """Calculate cosine similarity between two vectors."""
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    # Embeddings for different texts
    embedding_ai = np.array([0.8, 0.6, 0.4, 0.2])
    embedding_machine_learning = np.array([0.7, 0.5, 0.5, 0.3])  # Similar topic
    embedding_cooking = np.array([-0.2, -0.3, 0.1, 0.8])  # Different topic
    
    sim_ai_ml = cosine_similarity(embedding_ai, embedding_machine_learning)
    sim_ai_cooking = cosine_similarity(embedding_ai, embedding_cooking)
    
    print(f"AI embedding: {embedding_ai}")
    print(f"ML embedding: {embedding_machine_learning}")
    print(f"Cooking embedding: {embedding_cooking}")
    print(f"\nCosine similarity (AI, ML): {sim_ai_ml:.3f}")
    print(f"Cosine similarity (AI, Cooking): {sim_ai_cooking:.3f}")
    print("\nIntuition: Values close to 1 = very similar, close to -1 = very different")


def matrix_multiplication_attention():
    """
    Matrix Multiplication = Attention Mechanism Foundation
    Understanding how attention works at a fundamental level.
    """
    print("\n=== Matrix Multiplication for Attention ===")
    
    # Simplified attention mechanism
    # Query, Key, Value matrices (simplified)
    query = np.array([[1, 0], [0, 1]])  # What we're looking for
    key = np.array([[1, 0.5], [0.5, 1]])  # What's available
    value = np.array([[10, 20], [30, 40]])  # Actual content
    
    # Attention score = Query @ Key^T
    attention_scores = np.dot(query, key.T)
    print(f"Query:\n{query}")
    print(f"Key:\n{key}")
    print(f"Attention scores (Query @ Key^T):\n{attention_scores}")
    
    # Apply softmax (normalize to probabilities)
    def softmax(x):
        exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
    
    attention_weights = softmax(attention_scores)
    print(f"Attention weights (after softmax):\n{attention_weights}")
    
    # Final output = Attention weights @ Value
    output = np.dot(attention_weights, value)
    print(f"Output (Attention @ Value):\n{output}")
    
    print("\nIntuition: Attention determines which parts of Value to focus on")


def vector_operations():
    """
    Essential vector operations used throughout AI.
    """
    print("\n=== Essential Vector Operations ===")
    
    vec1 = np.array([3, 4])
    vec2 = np.array([1, 2])
    
    # Addition
    addition = vec1 + vec2
    print(f"Addition: {vec1} + {vec2} = {addition}")
    
    # Scalar multiplication
    scaled = 2 * vec1
    print(f"Scalar multiplication: 2 * {vec1} = {scaled}")
    
    # Dot product
    dot = np.dot(vec1, vec2)
    print(f"Dot product: {vec1} · {vec2} = {dot}")
    
    # Norm (magnitude/length)
    norm = np.linalg.norm(vec1)
    print(f"Norm (magnitude) of {vec1}: {norm:.3f}")
    
    # Normalization (unit vector)
    normalized = vec1 / np.linalg.norm(vec1)
    print(f"Normalized {vec1}: {normalized}")


if __name__ == "__main__":
    dot_product_similarity()
    cosine_similarity_embeddings()
    matrix_multiplication_attention()
    vector_operations()

