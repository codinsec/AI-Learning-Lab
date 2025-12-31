# Data & Tensor Fundamentals

## Overview

This project covers data manipulation and tensor operations essential for AI Engineering. The goal is **not** to become a data scientist, but to understand how to prepare data in the format that AI models expect.

## Why This Matters for AI Engineers

AI models work with:
- **Tensors** (multi-dimensional arrays) - the fundamental data structure
- **Structured data** - models need clean, formatted inputs
- **Token-based preparation** - understanding context windows and chunking
- **Embedding calculations** - vector operations for similarity search

## Learning Objectives

By completing this project, you will:

1. Understand tensors as multi-dimensional arrays (0D to 4D+)
2. Master NumPy operations: broadcasting, dot product, matrix multiplication
3. Use Pandas for text cleaning and data transformation pipelines
4. Implement token-based data preparation for LLMs
5. Apply different chunking strategies for RAG systems
6. Calculate embedding similarities using vector operations

## Project Structure

```
Data-Tensor-Fundamentals/
├── README.md
├── requirements.txt
├── numpy_tensors.py              # Tensor fundamentals and operations
└── pandas_data_processing.py     # Data cleaning and preparation
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run examples:**
   ```bash
   # NumPy tensor operations
   python numpy_tensors.py
   
   # Pandas data processing
   python pandas_data_processing.py
   ```

## Key Concepts

### Tensors
- **0D (Scalar):** Single number
- **1D (Vector):** Array of numbers (e.g., embeddings)
- **2D (Matrix):** Table of numbers (e.g., weight matrices)
- **3D+ (Tensor):** Stack of matrices (e.g., batch of images, sequences)

### Broadcasting
- NumPy automatically handles operations between arrays of different shapes
- Essential for understanding how embedding calculations work
- Example: Adding a scalar to a vector broadcasts the scalar to all elements

### Embedding Similarity
- **Dot product:** Measures similarity between two vectors
- **Cosine similarity:** Normalized dot product (range: -1 to 1)
- Core of vector search in RAG systems

### Matrix Multiplication
- Foundation of neural networks and attention mechanisms
- Different from element-wise multiplication
- Formula: `output = input @ weights + bias`

### Data Cleaning Pipeline
- Remove whitespace, normalize case, handle special characters
- Convert unstructured text to structured format
- Essential preprocessing step before feeding data to models

### Token-based Preparation
- LLMs work with tokens, not characters
- 1 token ≈ 4 characters (English)
- Context windows limit token count (e.g., 512, 1024, 4096 tokens)

### Chunking Strategies
1. **Fixed-size:** Simple, but may split sentences
2. **Sentence-based:** Preserves sentence boundaries
3. **Sliding window:** Overlaps chunks to preserve context

## Common Pitfalls

1. **Confusing matrix multiplication with element-wise:** Use `np.dot()` or `@` for matrix multiplication
2. **Ignoring token limits:** Always check token count before sending to LLM
3. **Poor chunking:** Splitting in the middle of sentences loses context
4. **Not normalizing embeddings:** Always normalize before similarity calculations
5. **Forgetting to clean data:** Unclean data leads to poor model performance

## Production Notes

- Always normalize embeddings before similarity calculations (use cosine similarity)
- Use sliding window chunking with overlap for RAG systems
- Monitor token counts to stay within context windows
- Implement data validation pipelines before model input
- Cache cleaned/preprocessed data to avoid reprocessing

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

