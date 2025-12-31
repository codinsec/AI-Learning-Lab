"""
Pandas: Data Processing for AI
Converting unstructured data to structured format for AI models.
"""

import pandas as pd
import numpy as np


def text_cleaning_pipeline():
    """
    Text cleaning pipeline: Preparing unstructured text for AI models.
    """
    print("=== Text Cleaning Pipeline ===")
    
    # Sample unstructured data
    data = {
        'text': [
            '  Hello World!!!  ',
            'This is a TEST.',
            '  Multiple   spaces   here  ',
            'UPPERCASE TEXT',
            'Mixed Case Text'
        ]
    }
    
    df = pd.DataFrame(data)
    print("Original data:")
    print(df)
    
    # Cleaning pipeline
    df['cleaned'] = df['text'].str.strip()  # Remove leading/trailing whitespace
    df['cleaned'] = df['cleaned'].str.lower()  # Convert to lowercase
    df['cleaned'] = df['cleaned'].str.replace(r'\s+', ' ', regex=True)  # Multiple spaces to single
    
    print("\nCleaned data:")
    print(df[['text', 'cleaned']])


def unstructured_to_structured():
    """
    Converting unstructured data to structured format.
    Essential for preparing data for AI models.
    """
    print("\n=== Unstructured to Structured Conversion ===")
    
    # Unstructured text data
    unstructured_texts = [
        "Name: John, Age: 30, City: New York",
        "Name: Jane, Age: 25, City: London",
        "Name: Bob, Age: 35, City: Paris"
    ]
    
    # Convert to structured DataFrame
    structured_data = []
    for text in unstructured_texts:
        parts = text.split(', ')
        record = {}
        for part in parts:
            key, value = part.split(': ')
            record[key] = value
        structured_data.append(record)
    
    df = pd.DataFrame(structured_data)
    print("Structured DataFrame:")
    print(df)
    print(f"\nDataFrame shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")


def token_based_preparation():
    """
    Token-based data preparation for LLMs.
    Understanding tokenization and context windows.
    """
    print("\n=== Token-based Data Preparation ===")
    
    # Sample texts of different lengths
    texts = [
        "Short text.",
        "This is a medium length text that contains more words and information.",
        "This is a very long text that contains many words and sentences. " * 10
    ]
    
    df = pd.DataFrame({'text': texts})
    
    # Approximate token count (1 token ≈ 4 characters for English)
    df['approx_tokens'] = df['text'].str.len() / 4
    
    # Chunking strategy: Split long texts into chunks
    max_tokens = 512  # Common context window size
    
    def chunk_text(text, max_tokens):
        """Split text into chunks of max_tokens."""
        approx_chars = max_tokens * 4
        chunks = []
        for i in range(0, len(text), approx_chars):
            chunks.append(text[i:i + approx_chars])
        return chunks
    
    df['chunks'] = df['text'].apply(lambda x: chunk_text(x, max_tokens))
    df['num_chunks'] = df['chunks'].apply(len)
    
    print("Token-based preparation:")
    print(df[['text', 'approx_tokens', 'num_chunks']])
    
    # Show chunks for long text
    print(f"\nChunks for long text (max {max_tokens} tokens each):")
    for i, chunk in enumerate(df.iloc[2]['chunks']):
        print(f"Chunk {i+1}: {chunk[:50]}...")


def chunking_strategies():
    """
    Different chunking strategies for RAG systems.
    """
    print("\n=== Chunking Strategies ===")
    
    # Sample document
    document = "This is sentence one. This is sentence two. This is sentence three. " * 5
    
    # Strategy 1: Fixed-size chunks (512 tokens)
    def fixed_size_chunk(text, chunk_size=512):
        """Fixed-size chunking (sliding window approach)."""
        approx_chars = chunk_size * 4
        chunks = []
        for i in range(0, len(text), approx_chars):
            chunks.append(text[i:i + approx_chars])
        return chunks
    
    # Strategy 2: Sentence-based chunking
    def sentence_chunk(text, max_sentences=3):
        """Chunk by sentences."""
        sentences = text.split('. ')
        chunks = []
        for i in range(0, len(sentences), max_sentences):
            chunk = '. '.join(sentences[i:i + max_sentences])
            chunks.append(chunk)
        return chunks
    
    # Strategy 3: Sliding window with overlap
    def sliding_window_chunk(text, chunk_size=512, overlap=128):
        """Sliding window with overlap to preserve context."""
        approx_chars = chunk_size * 4
        overlap_chars = overlap * 4
        chunks = []
        i = 0
        while i < len(text):
            chunks.append(text[i:i + approx_chars])
            i += approx_chars - overlap_chars
        return chunks
    
    fixed_chunks = fixed_size_chunk(document)
    sentence_chunks = sentence_chunk(document)
    sliding_chunks = sliding_window_chunk(document)
    
    print(f"Document length: {len(document)} characters")
    print(f"Fixed-size chunks: {len(fixed_chunks)}")
    print(f"Sentence-based chunks: {len(sentence_chunks)}")
    print(f"Sliding window chunks: {len(sliding_chunks)}")
    
    print("\nFixed-size chunk example:")
    print(f"  {fixed_chunks[0][:100]}...")


if __name__ == "__main__":
    text_cleaning_pipeline()
    unstructured_to_structured()
    token_based_preparation()
    chunking_strategies()

