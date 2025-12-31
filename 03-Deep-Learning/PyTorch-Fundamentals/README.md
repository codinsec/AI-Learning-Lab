# PyTorch Fundamentals

## Overview

This project covers deep learning with PyTorch from an AI Engineer's perspective. You'll learn to work with tensors, understand autograd, write training loops, and grasp key architectures like CNNs and Transformers.

## Why This Matters for AI Engineers

Deep learning is the foundation of modern AI:
- **Tensors:** The data structure of AI (multi-dimensional arrays)
- **Autograd:** How models learn (automatic differentiation)
- **Training loops:** The core of model training
- **Architectures:** CNNs for vision, Transformers for everything else
- **Transfer learning:** Pretraining and fine-tuning for efficiency

## Learning Objectives

By completing this project, you will:

1. Understand tensor lifecycle (CPU ↔ GPU)
2. Grasp autograd and how backpropagation works
3. Write training loops from scratch
4. Understand CNN and Transformer architectures
5. Know when to use pretraining vs fine-tuning
6. Understand LoRA/PEFT for efficient adaptation
7. Recognize inference vs training differences

## Project Structure

```
PyTorch-Fundamentals/
├── README.md
├── requirements.txt
├── tensor_lifecycle.py      # CPU/GPU operations
├── autograd.py              # Automatic differentiation
├── training_loop.py         # Writing training loops
├── cnn_transformer.py       # Key architectures
└── pretraining_finetuning.py # Transfer learning
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run examples:**
   ```bash
   # Tensor operations
   python tensor_lifecycle.py
   
   # Autograd
   python autograd.py
   
   # Training loops
   python training_loop.py
   
   # Architectures
   python cnn_transformer.py
   
   # Transfer learning
   python pretraining_finetuning.py
   ```

## Key Concepts

### Tensor Lifecycle

- **Default:** Tensors created on CPU
- **GPU:** Use `.to(device)` to move tensors
- **Operations:** Happen on the device where tensor is located
- **Memory:** GPU memory is limited, manage carefully

### Autograd (Automatic Differentiation)

- **requires_grad=True:** Tracks operations for gradient computation
- **.backward():** Computes gradients automatically
- **Chain rule:** Applied automatically (backpropagation)
- **Gradient accumulation:** Gradients accumulate for multiple operations

### Training Loop

Essential steps:
1. **Forward pass:** `predictions = model(input)`
2. **Compute loss:** `loss = criterion(predictions, targets)`
3. **Backward pass:** `loss.backward()` (computes gradients)
4. **Update weights:** `optimizer.step()` (updates parameters)
5. **Zero gradients:** `optimizer.zero_grad()` (clear previous gradients)

**Critical:** Always call `optimizer.zero_grad()` before `loss.backward()`!

### Architectures

#### CNN (Convolutional Neural Network)
- **Use case:** Image classification, computer vision
- **Components:** Convolutional layers, pooling, fully connected layers
- **Key idea:** Detects patterns at different scales

#### Transformer
- **Use case:** NLP, LLMs, RAG, Agents (foundation of modern AI)
- **Components:** Embeddings, positional encoding, self-attention, feed-forward
- **Key idea:** Attention mechanism allows tokens to attend to each other

### Pretraining vs Fine-tuning

#### Pretraining
- Train model on large dataset (e.g., ImageNet, text corpus)
- Learns general features/representations
- Expensive, done once

#### Fine-tuning
- Adapt pretrained model to specific task
- Train on smaller, task-specific dataset
- Much faster and cheaper
- Strategies:
  - Freeze all, train only classifier
  - Unfreeze last layers
  - Full fine-tuning

### LoRA (Low-Rank Adaptation)

- **Problem:** Full fine-tuning is expensive for large models
- **Solution:** Add small trainable matrices instead of updating all weights
- **Benefits:** Fewer parameters, faster training, less memory
- **Use case:** Adapting large language models efficiently

### Inference ≠ Training

**Training mode:**
- `model.train()`
- Dropout active
- BatchNorm uses batch statistics
- Gradients computed

**Inference mode:**
- `model.eval()`
- Dropout inactive
- BatchNorm uses running statistics
- No gradients (`torch.no_grad()`)

## Common Pitfalls

1. **Forgetting optimizer.zero_grad():** Gradients accumulate incorrectly
2. **Using training mode for inference:** Dropout active, wrong statistics
3. **Not moving tensors to GPU:** Slow training on CPU
4. **Memory issues:** Not managing GPU memory properly
5. **Wrong fine-tuning strategy:** Overfitting or underfitting

## Production Notes

- Always use `model.eval()` and `torch.no_grad()` for inference
- Monitor GPU memory usage
- Use mixed precision training for large models
- Implement proper checkpointing for long training
- Use LoRA/PEFT for efficient fine-tuning
- Validate model in eval mode before deployment

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

