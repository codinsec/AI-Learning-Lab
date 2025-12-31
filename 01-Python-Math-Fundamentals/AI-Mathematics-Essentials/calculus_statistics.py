"""
Calculus & Statistics for AI
Intuitive understanding of gradients, probability, and distributions.
"""

import numpy as np


def gradient_descent_intuition():
    """
    Gradient Descent: How models learn
    Intuitive explanation without heavy math.
    """
    print("=== Gradient Descent Intuition ===")
    
    # Simple function: f(x) = x^2 (we want to find minimum)
    def f(x):
        return x ** 2
    
    # Derivative: f'(x) = 2x (slope at point x)
    def gradient(x):
        return 2 * x
    
    # Starting point
    x = 5.0
    learning_rate = 0.1
    
    print(f"Finding minimum of f(x) = x²")
    print(f"Starting point: x = {x}, f(x) = {f(x):.3f}")
    
    # Gradient descent steps
    for step in range(10):
        grad = gradient(x)
        x = x - learning_rate * grad  # Move opposite to gradient
        print(f"Step {step + 1}: x = {x:.3f}, f(x) = {f(x):.3f}, gradient = {grad:.3f}")
    
    print("\nIntuition: Gradient points to steepest ascent, so we move opposite (descent)")
    print("Learning rate controls step size - too large = overshoot, too small = slow")


def chain_rule_backprop():
    """
    Chain Rule: Why backpropagation works
    Understanding how gradients flow through networks.
    """
    print("\n=== Chain Rule & Backpropagation ===")
    
    # Simple chain: y = g(f(x)) where f(x) = x², g(u) = u + 1
    def f(x):
        return x ** 2
    
    def g(u):
        return u + 1
    
    def f_prime(x):
        return 2 * x
    
    def g_prime(u):
        return 1
    
    x = 3.0
    
    # Forward pass
    u = f(x)
    y = g(u)
    
    # Backward pass (chain rule)
    # dy/dx = (dy/du) * (du/dx) = g'(u) * f'(x)
    dy_du = g_prime(u)
    du_dx = f_prime(x)
    dy_dx = dy_du * du_dx
    
    print(f"Forward: x = {x} → f(x) = {u} → g(f(x)) = {y}")
    print(f"Backward: dy/dx = (dy/du) * (du/dx) = {dy_du} * {du_dx} = {dy_dx}")
    print("\nIntuition: Chain rule lets us compute gradients layer by layer (backprop)")


def probability_distributions():
    """
    Probability Distributions: Understanding model outputs
    """
    print("\n=== Probability Distributions ===")
    
    # Simulated logits (raw model outputs before softmax)
    logits = np.array([2.0, 1.0, 0.1])
    
    # Softmax: Converts logits to probabilities
    def softmax(logits):
        exp_logits = np.exp(logits - np.max(logits))  # Numerical stability
        return exp_logits / np.sum(exp_logits)
    
    probabilities = softmax(logits)
    
    print(f"Logits (raw outputs): {logits}")
    print(f"Probabilities (after softmax): {probabilities}")
    print(f"Sum of probabilities: {np.sum(probabilities):.3f} (must be 1.0)")
    
    # Temperature: Controls randomness
    def softmax_with_temperature(logits, temperature=1.0):
        scaled_logits = logits / temperature
        exp_logits = np.exp(scaled_logits - np.max(scaled_logits))
        return exp_logits / np.sum(exp_logits)
    
    print("\nEffect of temperature:")
    for temp in [0.5, 1.0, 2.0]:
        probs = softmax_with_temperature(logits, temp)
        print(f"Temperature {temp}: {probs}")
    
    print("\nIntuition:")
    print("- Low temperature (0.5): More confident, less random")
    print("- High temperature (2.0): Less confident, more random")


def entropy_crossentropy():
    """
    Entropy & Cross-Entropy: Measuring uncertainty and loss
    """
    print("\n=== Entropy & Cross-Entropy ===")
    
    def entropy(probabilities):
        """Entropy: Measure of uncertainty."""
        # Avoid log(0)
        probabilities = probabilities[probabilities > 0]
        return -np.sum(probabilities * np.log(probabilities))
    
    # High entropy = high uncertainty (uniform distribution)
    uniform = np.array([0.25, 0.25, 0.25, 0.25])
    high_entropy = entropy(uniform)
    
    # Low entropy = low uncertainty (confident prediction)
    confident = np.array([0.9, 0.05, 0.03, 0.02])
    low_entropy = entropy(confident)
    
    print(f"Uniform distribution: {uniform}")
    print(f"Entropy: {high_entropy:.3f} (high uncertainty)")
    
    print(f"\nConfident distribution: {confident}")
    print(f"Entropy: {low_entropy:.3f} (low uncertainty)")
    
    # Cross-entropy: Loss function for classification
    def cross_entropy(y_true, y_pred):
        """Cross-entropy loss."""
        # Avoid log(0)
        y_pred = np.clip(y_pred, 1e-15, 1.0)
        return -np.sum(y_true * np.log(y_pred))
    
    # True label (one-hot encoded)
    true_label = np.array([1, 0, 0, 0])  # Class 0
    
    # Good prediction
    good_pred = np.array([0.9, 0.05, 0.03, 0.02])
    good_loss = cross_entropy(true_label, good_pred)
    
    # Bad prediction
    bad_pred = np.array([0.1, 0.3, 0.3, 0.3])
    bad_loss = cross_entropy(true_label, bad_pred)
    
    print(f"\nTrue label: {true_label}")
    print(f"Good prediction: {good_pred}, Loss: {good_loss:.3f}")
    print(f"Bad prediction: {bad_pred}, Loss: {bad_loss:.3f}")
    print("\nIntuition: Lower loss = better prediction")


if __name__ == "__main__":
    gradient_descent_intuition()
    chain_rule_backprop()
    probability_distributions()
    entropy_crossentropy()

