"""
Autograd: Automatic Differentiation
Understanding how PyTorch computes gradients automatically.
"""

import torch


def simple_autograd_example():
    """Basic autograd demonstration."""
    print("=== Simple Autograd Example ===")
    
    # Create tensor with gradient tracking
    x = torch.tensor(2.0, requires_grad=True)
    
    # Define function: y = x²
    y = x ** 2
    
    print(f"x = {x.item()}")
    print(f"y = x² = {y.item()}")
    
    # Compute gradient: dy/dx = 2x
    y.backward()
    
    print(f"dy/dx = {x.grad.item()} (should be 2x = 4)")
    print("Autograd computed this automatically!")


def chain_rule_example():
    """Chain rule in autograd (backpropagation)."""
    print("\n=== Chain Rule (Backpropagation) ===")
    
    # y = g(f(x)) where f(x) = x², g(u) = u + 1
    x = torch.tensor(3.0, requires_grad=True)
    
    # Forward pass
    u = x ** 2  # f(x)
    y = u + 1   # g(u)
    
    print(f"Forward: x = {x.item()} → u = x² = {u.item()} → y = u + 1 = {y.item()}")
    
    # Backward pass (chain rule)
    y.backward()
    
    # dy/dx = (dy/du) * (du/dx) = 1 * 2x = 2x
    print(f"dy/dx = {x.grad.item()} (should be 2x = 6)")
    print("Autograd applied chain rule automatically!")


def neural_network_gradients():
    """Gradients in a simple neural network."""
    print("\n=== Neural Network Gradients ===")
    
    # Simple network: y = Wx + b
    x = torch.tensor([1.0, 2.0], requires_grad=False)  # Input (no grad needed)
    W = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)  # Weights
    b = torch.tensor([0.5, 0.5], requires_grad=True)  # Bias
    
    # Forward pass
    y = torch.matmul(W, x) + b
    loss = y.sum()  # Simple loss (sum of outputs)
    
    print(f"Input x: {x}")
    print(f"Weights W:\n{W}")
    print(f"Bias b: {b}")
    print(f"Output y: {y}")
    print(f"Loss: {loss.item()}")
    
    # Backward pass
    loss.backward()
    
    print(f"\nGradient w.r.t. W:\n{W.grad}")
    print(f"Gradient w.r.t. b: {b.grad}")
    print("These gradients are used to update weights during training!")


def gradient_accumulation():
    """Understanding gradient accumulation."""
    print("\n=== Gradient Accumulation ===")
    
    x = torch.tensor(2.0, requires_grad=True)
    
    # Multiple forward passes
    y1 = x ** 2
    y2 = x ** 3
    
    # Sum and backward
    total = y1 + y2
    total.backward()
    
    print(f"x = {x.item()}")
    print(f"y1 = x² = {y1.item()}")
    print(f"y2 = x³ = {y2.item()}")
    print(f"total = y1 + y2 = {total.item()}")
    print(f"dy1/dx = 2x = 4")
    print(f"dy2/dx = 3x² = 12")
    print(f"d(total)/dx = {x.grad.item()} (should be 4 + 12 = 16)")
    print("Gradients accumulate automatically!")


if __name__ == "__main__":
    simple_autograd_example()
    chain_rule_example()
    neural_network_gradients()
    gradient_accumulation()
    
    print("\n=== Key Takeaways ===")
    print("1. Set requires_grad=True to track gradients")
    print("2. Call .backward() to compute gradients")
    print("3. Gradients are stored in .grad attribute")
    print("4. Chain rule is applied automatically (backpropagation)")
    print("5. Gradients accumulate for multiple operations")

