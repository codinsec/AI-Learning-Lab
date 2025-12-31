"""
ML Pipelines
Organizing preprocessing and modeling steps.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def create_sample_data():
    """Create sample data with mixed types."""
    np.random.seed(42)
    n = 100
    
    data = {
        'numeric1': np.random.randn(n) * 10,
        'numeric2': np.random.randn(n) * 5,
        'category': np.random.choice(['A', 'B', 'C'], n),
        'target': np.random.randn(n) * 2
    }
    
    return pd.DataFrame(data)


def pipeline_example():
    """Demonstrates ML pipeline concept."""
    print("=== ML Pipeline Example ===")
    
    df = create_sample_data()
    
    # Separate features and target
    X = df[['numeric1', 'numeric2', 'category']]
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create pipeline: preprocessing + model
    pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Step 1: Scale numeric features
        ('encoder', OneHotEncoder()),  # Step 2: Encode categorical (simplified)
        ('model', LinearRegression())  # Step 3: Train model
    ])
    
    # Fit pipeline (applies all steps)
    pipeline.fit(X_train, y_train)
    
    # Predict (applies preprocessing + prediction)
    y_pred = pipeline.predict(X_test)
    
    print(f"Pipeline steps: {[step[0] for step in pipeline.steps]}")
    print(f"Predictions shape: {y_pred.shape}")
    print("\nBenefit: All preprocessing is applied automatically")


def column_transformer_example():
    """Different preprocessing for different column types."""
    print("\n=== Column Transformer ===")
    
    df = create_sample_data()
    X = df[['numeric1', 'numeric2', 'category']]
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Different preprocessing for different columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['numeric1', 'numeric2']),
            ('cat', OneHotEncoder(), ['category'])
        ]
    )
    
    # Pipeline with preprocessor
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('model', LinearRegression())
    ])
    
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    print("Preprocessing:")
    print("  - Numeric columns: StandardScaler")
    print("  - Categorical columns: OneHotEncoder")
    print(f"Predictions: {y_pred[:5]}")


if __name__ == "__main__":
    pipeline_example()
    column_transformer_example()
    
    print("\n=== Pipeline Benefits ===")
    print("1. Organizes preprocessing steps")
    print("2. Prevents data leakage (fits only on training data)")
    print("3. Makes code reusable and maintainable")
    print("4. Ensures consistent preprocessing in production")

