"""
NumPy: Understanding Tensors for AI
Tensors are multi-dimensional arrays - the foundation of all AI operations.
"""

import numpy as np


def demonstrate_tensors():
    """Shows different tensor dimensions used in AI."""
    
    # Scalar (0D tensor) - single number
    scalar = np.array(5)
    print(f"Scalar (0D): {scalar}, shape: {scalar.shape}")
    
    # Vector (1D tensor) - array of numbers
    vector = np.array([1, 2, 3, 4, 5])
    print(f"Vector (1D): {vector}, shape: {vector.shape}")
    
    # Matrix (2D tensor) - table of numbers
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Matrix (2D):\n{matrix}\nshape: {matrix.shape}")
    
    # 3D tensor - stack of matrices (e.g., batch of images)
    tensor_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f"3D Tensor:\n{tensor_3d}\nshape: {tensor_3d.shape}")
    
    # Higher dimensions - common in deep learning
    # 4D: (batch, height, width, channels) for images
    batch_images = np.random.rand(32, 224, 224, 3)  # 32 images, 224x224, RGB
    print(f"Batch of images (4D): shape {batch_images.shape}")


def broadcasting_example():
    """
    Broadcasting: How NumPy handles operations between arrays of different shapes.
    Essential for understanding embedding calculations.
    """
    print("\n=== Broadcasting Example ===")
    
    # Vector (1D)
    vector = np.array([1, 2, 3])
    
    # Scalar
    scalar = 10
    
    # Broadcasting: scalar is "broadcast" to match vector shape
    result = vector + scalar
    print(f"Vector: {vector}")
    print(f"Scalar: {scalar}")
    print(f"Result (broadcasted): {result}")
    
    # Matrix broadcasting
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    vector = np.array([10, 20, 30])
    
    # Broadcasting: vector is broadcast to each row
    result = matrix + vector
    print(f"\nMatrix:\n{matrix}")
    print(f"Vector: {vector}")
    print(f"Result (broadcasted):\n{result}")


def embedding_similarity():
    """
    Demonstrates embedding similarity calculation using dot product.
    This is the core of vector search in RAG systems.
    """
    print("\n=== Embedding Similarity ===")
    
    # Simulate embeddings (vectors of numbers)
    embedding1 = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    embedding2 = np.array([0.2, 0.3, 0.4, 0.5, 0.6])  # Similar to embedding1
    embedding3 = np.array([-0.1, -0.2, -0.3, -0.4, -0.5])  # Different from embedding1
    
    # Dot product = similarity measure
    similarity_12 = np.dot(embedding1, embedding2)
    similarity_13 = np.dot(embedding1, embedding3)
    
    print(f"Embedding 1: {embedding1}")
    print(f"Embedding 2: {embedding2}")
    print(f"Embedding 3: {embedding3}")
    print(f"\nSimilarity (1, 2): {similarity_12:.3f} (higher = more similar)")
    print(f"Similarity (1, 3): {similarity_13:.3f} (lower = less similar)")
    
    # Cosine similarity (normalized dot product)
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    cos_sim_12 = cosine_similarity(embedding1, embedding2)
    cos_sim_13 = cosine_similarity(embedding1, embedding3)
    
    print(f"\nCosine Similarity (1, 2): {cos_sim_12:.3f}")
    print(f"Cosine Similarity (1, 3): {cos_sim_13:.3f}")


def matrix_multiplication():
    """
    Matrix multiplication: Foundation of neural networks and attention mechanisms.
    """
    print("\n=== Matrix Multiplication ===")
    
    # Two matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    # Element-wise multiplication (NOT matrix multiplication)
    element_wise = A * B
    print(f"Element-wise:\n{element_wise}")
    
    # Matrix multiplication (dot product)
    matrix_mult = np.dot(A, B)
    print(f"Matrix multiplication:\n{matrix_mult}")
    
    # In neural networks: output = input @ weights + bias
    input_vector = np.array([1, 2, 3])
    weights = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
    bias = np.array([0.1, 0.2])
    
    output = np.dot(input_vector, weights) + bias
    print(f"\nNeural network layer:")
    print(f"Input: {input_vector}")
    print(f"Weights shape: {weights.shape}")
    print(f"Output: {output}")


if __name__ == "__main__":
    demonstrate_tensors()
    broadcasting_example()
    embedding_similarity()
    matrix_multiplication()

