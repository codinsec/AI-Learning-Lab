"""
CNN and Transformer Architectures
Understanding key architectures in deep learning.
"""

import torch
import torch.nn as nn


def simple_cnn():
    """Convolutional Neural Network for images."""
    print("=== CNN Architecture ===")
    
    class SimpleCNN(nn.Module):
        def __init__(self):
            super(SimpleCNN, self).__init__()
            # Convolutional layers
            self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)  # 3 channels → 16
            self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)  # 16 → 32
            # Pooling
            self.pool = nn.MaxPool2d(2, 2)  # Reduces size by 2
            # Fully connected
            self.fc1 = nn.Linear(32 * 8 * 8, 128)
            self.fc2 = nn.Linear(128, 10)  # 10 classes
            self.relu = nn.ReLU()
        
        def forward(self, x):
            # x shape: (batch, 3, 32, 32)
            x = self.pool(self.relu(self.conv1(x)))  # (batch, 16, 16, 16)
            x = self.pool(self.relu(self.conv2(x)))   # (batch, 32, 8, 8)
            x = x.view(-1, 32 * 8 * 8)  # Flatten
            x = self.relu(self.fc1(x))
            x = self.fc2(x)
            return x
    
    model = SimpleCNN()
    
    # Example input (batch of 4 images, 3 channels, 32x32)
    x = torch.randn(4, 3, 32, 32)
    output = model(x)
    
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape} (batch, num_classes)")
    print("\nCNN components:")
    print("- Conv2d: Detects patterns (edges, shapes)")
    print("- MaxPool: Reduces spatial dimensions")
    print("- Fully connected: Final classification")


def simple_transformer():
    """Transformer architecture (simplified)."""
    print("\n=== Transformer Architecture ===")
    
    class SimpleTransformer(nn.Module):
        def __init__(self, vocab_size, d_model, nhead, num_layers):
            super(SimpleTransformer, self).__init__()
            # Embedding
            self.embedding = nn.Embedding(vocab_size, d_model)
            # Positional encoding (simplified - usually learned)
            self.pos_encoding = nn.Parameter(torch.randn(1000, d_model))
            # Transformer encoder
            encoder_layer = nn.TransformerEncoderLayer(
                d_model=d_model,
                nhead=nhead,
                dim_feedforward=d_model * 4,
                batch_first=True
            )
            self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
            # Output projection
            self.fc = nn.Linear(d_model, vocab_size)
        
        def forward(self, x):
            # x shape: (batch, seq_len) - token indices
            x = self.embedding(x)  # (batch, seq_len, d_model)
            x = x + self.pos_encoding[:x.size(1), :]  # Add positional encoding
            x = self.transformer(x)  # Self-attention layers
            x = self.fc(x)  # (batch, seq_len, vocab_size)
            return x
    
    model = SimpleTransformer(vocab_size=1000, d_model=128, nhead=4, num_layers=2)
    
    # Example input (batch of 2 sequences, length 10)
    x = torch.randint(0, 1000, (2, 10))
    output = model(x)
    
    print(f"Input shape: {x.shape} (batch, sequence_length)")
    print(f"Output shape: {output.shape} (batch, sequence_length, vocab_size)")
    print("\nTransformer components:")
    print("- Embedding: Converts tokens to vectors")
    print("- Positional encoding: Adds position information")
    print("- Self-attention: Allows tokens to attend to each other")
    print("- Feed-forward: Non-linear transformation")


def attention_mechanism():
    """Understanding attention mechanism (simplified)."""
    print("\n=== Attention Mechanism ===")
    
    # Simplified attention
    batch_size, seq_len, d_model = 2, 5, 8
    
    # Query, Key, Value
    Q = torch.randn(batch_size, seq_len, d_model)
    K = torch.randn(batch_size, seq_len, d_model)
    V = torch.randn(batch_size, seq_len, d_model)
    
    # Attention scores: Q @ K^T
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_model ** 0.5)  # Scaled
    attention_weights = torch.softmax(scores, dim=-1)
    
    # Apply attention to values
    output = torch.matmul(attention_weights, V)
    
    print(f"Query shape: {Q.shape}")
    print(f"Key shape: {K.shape}")
    print(f"Value shape: {V.shape}")
    print(f"Attention weights shape: {attention_weights.shape}")
    print(f"Output shape: {output.shape}")
    print("\nAttention process:")
    print("1. Compute similarity: Q @ K^T (how similar are queries to keys)")
    print("2. Softmax: Convert to probabilities (attention weights)")
    print("3. Weighted sum: Attention @ V (combine values based on attention)")


if __name__ == "__main__":
    simple_cnn()
    simple_transformer()
    attention_mechanism()
    
    print("\n=== Architecture Use Cases ===")
    print("CNN: Image classification, object detection, computer vision")
    print("Transformer: NLP, LLMs, RAG, Agents (foundation of modern AI)")

