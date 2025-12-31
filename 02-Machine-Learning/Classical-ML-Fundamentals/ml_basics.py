"""
Classical Machine Learning Basics
Understanding ML models without becoming a data scientist.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def load_sample_data():
    """Create sample data for demonstration."""
    np.random.seed(42)
    n_samples = 100
    
    # Simple regression problem
    X = np.random.rand(n_samples, 3) * 10
    y = X[:, 0] * 2 + X[:, 1] * 1.5 + X[:, 2] * 0.5 + np.random.randn(n_samples) * 2
    
    return X, y


def demonstrate_regression():
    """Linear Regression: Predicting continuous values."""
    print("=== Linear Regression ===")
    
    X, y = load_sample_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Squared Error: {mse:.3f}")
    print(f"R² Score: {r2:.3f}")
    print(f"Coefficients: {model.coef_}")
    print(f"Intercept: {model.intercept_:.3f}")


def demonstrate_tree():
    """Decision Tree: Non-linear relationships."""
    print("\n=== Decision Tree ===")
    
    X, y = load_sample_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = DecisionTreeRegressor(max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Squared Error: {mse:.3f}")
    print(f"R² Score: {r2:.3f}")
    print(f"Tree depth: {model.get_depth()}")


def demonstrate_random_forest():
    """Random Forest: Ensemble of trees."""
    print("\n=== Random Forest ===")
    
    X, y = load_sample_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Squared Error: {mse:.3f}")
    print(f"R² Score: {r2:.3f}")
    print(f"Number of trees: {model.n_estimators}")


if __name__ == "__main__":
    demonstrate_regression()
    demonstrate_tree()
    demonstrate_random_forest()

