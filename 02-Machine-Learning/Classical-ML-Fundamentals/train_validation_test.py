"""
Train / Validation / Test Split
Proper data splitting to evaluate model performance.
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


def demonstrate_splits():
    """Demonstrates train/validation/test split."""
    print("=== Train / Validation / Test Split ===")
    
    # Generate sample data
    np.random.seed(42)
    X = np.random.rand(1000, 5)
    y = X[:, 0] * 2 + np.random.randn(1000) * 0.5
    
    # Step 1: Split into train+val and test (80/20)
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Step 2: Split train+val into train and validation (80/20 of remaining = 64/16)
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=0.2, random_state=42
    )
    
    print(f"Total samples: {len(X)}")
    print(f"Train: {len(X_train)} ({len(X_train)/len(X)*100:.1f}%)")
    print(f"Validation: {len(X_val)} ({len(X_val)/len(X)*100:.1f}%)")
    print(f"Test: {len(X_test)} ({len(X_test)/len(X)*100:.1f}%)")
    
    # Train model
    model = DecisionTreeRegressor(max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate on validation set (for hyperparameter tuning)
    val_pred = model.predict(X_val)
    val_mse = mean_squared_error(y_val, val_pred)
    print(f"\nValidation MSE: {val_mse:.4f} (use for tuning)")
    
    # Evaluate on test set (final evaluation, only once!)
    test_pred = model.predict(X_test)
    test_mse = mean_squared_error(y_test, test_pred)
    print(f"Test MSE: {test_mse:.4f} (final performance estimate)")
    
    print("\nPurpose of each split:")
    print("Train: Learn model parameters")
    print("Validation: Tune hyperparameters, choose best model")
    print("Test: Final evaluation (unbiased estimate)")


def data_leakage_example():
    """Demonstrates data leakage - a common mistake."""
    print("\n=== Data Leakage ===")
    
    np.random.seed(42)
    X = np.random.rand(100, 3)
    y = X[:, 0] * 2 + np.random.randn(100) * 0.5
    
    # WRONG: Preprocessing before split (leakage!)
    print("WRONG Approach (Data Leakage):")
    from sklearn.preprocessing import StandardScaler
    
    # Don't do this!
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)  # Fits on ALL data
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    print("Problem: Scaler saw test data statistics!")
    
    # CORRECT: Preprocessing after split
    print("\nCORRECT Approach:")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)  # Fit only on train
    X_test_scaled = scaler.transform(X_test)  # Transform test (don't fit!)
    
    print("Solution: Fit scaler only on training data")
    print("Then transform both train and test with fitted scaler")


if __name__ == "__main__":
    demonstrate_splits()
    data_leakage_example()
    
    print("\n=== Key Rules ===")
    print("1. Always split data BEFORE any preprocessing")
    print("2. Fit preprocessing (scaler, encoder) only on training data")
    print("3. Use validation set for hyperparameter tuning")
    print("4. Test set: Only evaluate once, at the very end")
    print("5. Never let test data influence training or validation")

