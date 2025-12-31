"""
Training Loop: Writing Your Own
Understanding the training process from scratch.
"""

import torch
import torch.nn as nn
import torch.optim as optim


class SimpleModel(nn.Module):
    """Simple neural network for demonstration."""
    
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x


def create_dummy_data():
    """Create dummy data for training."""
    # Simple regression problem
    X = torch.randn(100, 3)  # 100 samples, 3 features
    y = X[:, 0] * 2 + X[:, 1] * 1.5 - X[:, 2] * 0.5 + torch.randn(100) * 0.1
    y = y.unsqueeze(1)  # Reshape to (100, 1)
    return X, y


def training_loop_example():
    """Complete training loop from scratch."""
    print("=== Training Loop Example ===")
    
    # Create model
    model = SimpleModel(input_size=3, hidden_size=10, output_size=1)
    
    # Loss function
    criterion = nn.MSELoss()
    
    # Optimizer (updates weights)
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    
    # Get data
    X, y = create_dummy_data()
    
    # Training loop
    num_epochs = 100
    
    print("Training...")
    for epoch in range(num_epochs):
        # Forward pass
        predictions = model(X)
        loss = criterion(predictions, y)
        
        # Backward pass
        optimizer.zero_grad()  # Clear previous gradients
        loss.backward()  # Compute gradients
        optimizer.step()  # Update weights
        
        # Print progress
        if (epoch + 1) % 20 == 0:
            print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item():.4f}")
    
    print("\nTraining complete!")
    print("Key steps in training loop:")
    print("1. Forward pass: model(input) → predictions")
    print("2. Compute loss: criterion(predictions, targets)")
    print("3. Backward pass: loss.backward() → computes gradients")
    print("4. Update weights: optimizer.step() → updates model parameters")


def optimizer_zero_grad_importance():
    """Why optimizer.zero_grad() is crucial."""
    print("\n=== Why optimizer.zero_grad()? ===")
    
    x = torch.tensor(2.0, requires_grad=True)
    optimizer = optim.SGD([x], lr=0.1)
    
    # Without zero_grad (WRONG)
    print("Without zero_grad (gradients accumulate):")
    for i in range(3):
        y = x ** 2
        y.backward()
        print(f"Step {i+1}: grad = {x.grad.item()}")
        # Don't call zero_grad - gradients accumulate!
    
    # Reset
    x = torch.tensor(2.0, requires_grad=True)
    optimizer = optim.SGD([x], lr=0.1)
    
    # With zero_grad (CORRECT)
    print("\nWith zero_grad (gradients reset each step):")
    for i in range(3):
        optimizer.zero_grad()  # Clear previous gradients
        y = x ** 2
        y.backward()
        print(f"Step {i+1}: grad = {x.grad.item()}")
        optimizer.step()


def inference_mode():
    """Inference vs Training mode."""
    print("\n=== Inference vs Training Mode ===")
    
    model = SimpleModel(3, 10, 1)
    X, _ = create_dummy_data()
    
    # Training mode (default)
    model.train()
    print("Training mode:")
    print(f"  model.training = {model.training}")
    
    # Inference mode
    model.eval()
    print("\nEvaluation/Inference mode:")
    print(f"  model.training = {model.training}")
    
    # During inference, use torch.no_grad() to save memory
    with torch.no_grad():
        predictions = model(X)
        print(f"Predictions shape: {predictions.shape}")
        print("No gradients computed (saves memory and speed)")
    
    print("\nKey difference:")
    print("- Training: model.train(), gradients computed")
    print("- Inference: model.eval(), torch.no_grad(), no gradients")


if __name__ == "__main__":
    training_loop_example()
    optimizer_zero_grad_importance()
    inference_mode()

