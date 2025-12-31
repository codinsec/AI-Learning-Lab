"""
Tensor Lifecycle: CPU ↔ GPU
Understanding how tensors move between devices.
"""

import torch
import numpy as np


def demonstrate_tensor_creation():
    """Creating tensors in PyTorch."""
    print("=== Tensor Creation ===")
    
    # From Python list
    tensor1 = torch.tensor([1, 2, 3, 4, 5])
    print(f"From list: {tensor1}")
    
    # From NumPy array
    np_array = np.array([1, 2, 3])
    tensor2 = torch.from_numpy(np_array)
    print(f"From NumPy: {tensor2}")
    
    # Random tensor
    tensor3 = torch.randn(3, 4)  # 3x4 random values
    print(f"Random tensor:\n{tensor3}")
    
    # Zeros and ones
    zeros = torch.zeros(2, 3)
    ones = torch.ones(2, 3)
    print(f"Zeros:\n{zeros}")
    print(f"Ones:\n{ones}")


def cpu_gpu_operations():
    """Moving tensors between CPU and GPU."""
    print("\n=== CPU ↔ GPU Operations ===")
    
    # Check if GPU is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Create tensor on CPU (default)
    tensor_cpu = torch.randn(3, 3)
    print(f"Tensor on CPU: {tensor_cpu.device}")
    
    if torch.cuda.is_available():
        # Move to GPU
        tensor_gpu = tensor_cpu.to(device)
        print(f"Tensor on GPU: {tensor_gpu.device}")
        
        # Operations on GPU
        result_gpu = tensor_gpu @ tensor_gpu.T  # Matrix multiplication
        print(f"Result on GPU: {result_gpu.device}")
        
        # Move back to CPU
        result_cpu = result_gpu.cpu()
        print(f"Result back on CPU: {result_cpu.device}")
    else:
        print("GPU not available, using CPU only")
    
    print("\nKey points:")
    print("- Default: tensors created on CPU")
    print("- Use .to(device) to move tensors")
    print("- Operations happen on the device where tensor is located")
    print("- Move back to CPU for NumPy conversion")


def tensor_operations():
    """Basic tensor operations."""
    print("\n=== Tensor Operations ===")
    
    a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
    b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
    
    # Element-wise operations
    add = a + b
    multiply = a * b
    
    # Matrix multiplication
    matmul = torch.matmul(a, b)
    matmul_alt = a @ b  # Alternative syntax
    
    print(f"Matrix A:\n{a}")
    print(f"Matrix B:\n{b}")
    print(f"A + B (element-wise):\n{add}")
    print(f"A * B (element-wise):\n{multiply}")
    print(f"A @ B (matrix multiplication):\n{matmul}")


def gradient_tracking():
    """Understanding requires_grad for automatic differentiation."""
    print("\n=== Gradient Tracking ===")
    
    # Tensor without gradient tracking
    x = torch.tensor([1.0, 2.0, 3.0])
    print(f"x without grad: requires_grad={x.requires_grad}")
    
    # Tensor with gradient tracking (needed for training)
    x_grad = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
    print(f"x with grad: requires_grad={x_grad.requires_grad}")
    
    # Compute function
    y = (x_grad ** 2).sum()
    print(f"y = sum(x²) = {y.item()}")
    
    # Compute gradients
    y.backward()
    print(f"Gradient of y w.r.t. x: {x_grad.grad}")
    print("Gradient = 2x (as expected from calculus)")


if __name__ == "__main__":
    demonstrate_tensor_creation()
    cpu_gpu_operations()
    tensor_operations()
    gradient_tracking()

