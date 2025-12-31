"""
Overfitting and Underfitting
Critical concepts for understanding model performance.
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def generate_data():
    """Generate data with some noise."""
    np.random.seed(42)
    X = np.linspace(0, 10, 100).reshape(-1, 1)
    y = np.sin(X.flatten()) + np.random.randn(100) * 0.3
    return X, y


def demonstrate_overfitting():
    """Overfitting: Model learns training data too well, fails on new data."""
    print("=== Overfitting ===")
    
    X, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Overfitted model (too complex)
    overfitted = DecisionTreeRegressor(max_depth=20, min_samples_split=2)
    overfitted.fit(X_train, y_train)
    
    train_pred = overfitted.predict(X_train)
    test_pred = overfitted.predict(X_test)
    
    train_mse = mean_squared_error(y_train, train_pred)
    test_mse = mean_squared_error(y_test, test_pred)
    
    print(f"Training MSE: {train_mse:.4f} (very low)")
    print(f"Test MSE: {test_mse:.4f} (much higher)")
    print("Sign: Large gap between train and test performance")
    print("Problem: Model memorized training data, can't generalize")


def demonstrate_underfitting():
    """Underfitting: Model too simple, can't capture patterns."""
    print("\n=== Underfitting ===")
    
    X, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Underfitted model (too simple)
    underfitted = LinearRegression()  # Linear model for non-linear data
    underfitted.fit(X_train, y_train)
    
    train_pred = underfitted.predict(X_train)
    test_pred = underfitted.predict(X_test)
    
    train_mse = mean_squared_error(y_train, train_pred)
    test_mse = mean_squared_error(y_test, test_pred)
    
    print(f"Training MSE: {train_mse:.4f} (high)")
    print(f"Test MSE: {test_mse:.4f} (also high)")
    print("Sign: Both train and test performance are poor")
    print("Problem: Model too simple, can't learn the pattern")


def demonstrate_good_fit():
    """Good fit: Balanced model complexity."""
    print("\n=== Good Fit ===")
    
    X, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Well-fitted model (balanced complexity)
    good_fit = DecisionTreeRegressor(max_depth=5, min_samples_split=10)
    good_fit.fit(X_train, y_train)
    
    train_pred = good_fit.predict(X_train)
    test_pred = good_fit.predict(X_test)
    
    train_mse = mean_squared_error(y_train, train_pred)
    test_mse = mean_squared_error(y_test, test_pred)
    
    print(f"Training MSE: {train_mse:.4f}")
    print(f"Test MSE: {test_mse:.4f}")
    print("Sign: Train and test performance are similar and good")
    print("Solution: Balanced model complexity")


if __name__ == "__main__":
    demonstrate_overfitting()
    demonstrate_underfitting()
    demonstrate_good_fit()
    
    print("\n=== Key Takeaways ===")
    print("Overfitting: Low train error, high test error → Reduce complexity")
    print("Underfitting: High train error, high test error → Increase complexity")
    print("Good fit: Similar train/test error, both low → Right complexity")

