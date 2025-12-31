"""
Chunking Strategies for RAG
Different approaches to splitting documents for retrieval.
"""


def fixed_size_chunking():
    """Fixed-size chunking with optional overlap."""
    print("=== Fixed-Size Chunking ===")
    
    document = """
    This is a long document that needs to be split into chunks.
    Fixed-size chunking splits the document into equal-sized pieces.
    This is simple but may split sentences or paragraphs in the middle.
    Overlap can be added to preserve context between chunks.
    """
    
    chunk_size = 50  # characters
    chunk_overlap = 10  # characters
    
    chunks = []
    start = 0
    while start < len(document):
        end = start + chunk_size
        chunk = document[start:end]
        chunks.append(chunk.strip())
        start = end - chunk_overlap  # Overlap
    
    print(f"Document length: {len(document)} characters")
    print(f"Chunk size: {chunk_size} characters")
    print(f"Overlap: {chunk_overlap} characters")
    print(f"Number of chunks: {len(chunks)}")
    print("\nChunks:")
    for i, chunk in enumerate(chunks):
        print(f"  Chunk {i+1}: {chunk[:50]}...")
    
    print("\nPros: Simple, predictable size")
    print("Cons: May split sentences/paragraphs")


def sentence_based_chunking():
    """Chunk by sentences to preserve meaning."""
    print("\n=== Sentence-Based Chunking ===")
    
    document = """
    This is sentence one. This is sentence two. This is sentence three.
    This is sentence four. This is sentence five. This is sentence six.
    """
    
    # Split by sentences
    sentences = document.split('. ')
    
    # Group sentences into chunks
    max_sentences_per_chunk = 2
    chunks = []
    for i in range(0, len(sentences), max_sentences_per_chunk):
        chunk = '. '.join(sentences[i:i + max_sentences_per_chunk])
        chunks.append(chunk)
    
    print(f"Total sentences: {len(sentences)}")
    print(f"Sentences per chunk: {max_sentences_per_chunk}")
    print(f"Number of chunks: {len(chunks)}")
    print("\nChunks:")
    for i, chunk in enumerate(chunks):
        print(f"  Chunk {i+1}: {chunk}")
    
    print("\nPros: Preserves sentence boundaries")
    print("Cons: Variable chunk sizes")


def semantic_chunking():
    """Chunk by semantic similarity (advanced)."""
    print("\n=== Semantic Chunking ===")
    
    print("Semantic chunking groups text by meaning/similarity.")
    print("Uses embeddings to find natural breakpoints.")
    
    print("\nProcess:")
    print("1. Split into small segments (e.g., sentences)")
    print("2. Compute embeddings for each segment")
    print("3. Group segments with similar embeddings")
    print("4. Create chunks from grouped segments")
    
    print("\nPros: Preserves semantic coherence")
    print("Cons: More complex, requires embedding model")
    print("Use case: Documents with varying topics")


def recursive_chunking():
    """Recursive chunking: Try different strategies."""
    print("\n=== Recursive Chunking ===")
    
    print("Recursive approach:")
    print("1. Try splitting by paragraphs")
    print("2. If chunks too large, split by sentences")
    print("3. If still too large, split by words")
    print("4. Ensures chunks fit within size limits")
    
    print("\nPros: Adapts to document structure")
    print("Cons: More complex implementation")


def chunking_best_practices():
    """Best practices for chunking."""
    print("\n=== Chunking Best Practices ===")
    
    practices = {
        "Chunk size": "512-1024 tokens (depends on embedding model)",
        "Overlap": "10-20% of chunk size (preserves context)",
        "Boundaries": "Prefer sentence/paragraph boundaries",
        "Metadata": "Store chunk metadata (source, position)",
        "Testing": "Test different strategies and measure retrieval quality",
    }
    
    print("Recommendations:")
    for practice, recommendation in practices.items():
        print(f"  {practice}: {recommendation}")
    
    print("\nCommon chunk sizes:")
    print("  - Small (128-256 tokens): Fine-grained retrieval")
    print("  - Medium (512-1024 tokens): Balanced (most common)")
    print("  - Large (2048+ tokens): Coarse-grained retrieval")
    
    print("\nConsiderations:")
    print("  - Embedding model context window")
    print("  - Query complexity")
    print("  - Retrieval accuracy vs context")


if __name__ == "__main__":
    fixed_size_chunking()
    sentence_based_chunking()
    semantic_chunking()
    recursive_chunking()
    chunking_best_practices()
    
    print("\n=== Key Takeaways ===")
    print("1. Choose chunking strategy based on document type")
    print("2. Preserve sentence/paragraph boundaries when possible")
    print("3. Use overlap to maintain context")
    print("4. Test and measure retrieval quality")
    print("5. Store metadata with chunks")

