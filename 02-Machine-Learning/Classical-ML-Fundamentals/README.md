# Classical Machine Learning Fundamentals

## Overview

This project covers classical machine learning concepts essential for AI Engineers. The goal is **not** to become a data scientist, but to understand how ML models work so you can use them effectively in AI systems.

## Why This Matters for AI Engineers

Understanding ML fundamentals helps you:
- Choose the right model for the task
- Recognize overfitting and underfitting
- Build proper data pipelines
- Avoid data leakage
- Evaluate model performance correctly

## Learning Objectives

By completing this project, you will:

1. Understand basic ML algorithms (regression, trees, random forest)
2. Recognize overfitting vs underfitting
3. Build ML pipelines for preprocessing and modeling
4. Properly split data into train/validation/test sets
5. Avoid data leakage pitfalls
6. Evaluate model performance correctly

## Project Structure

```
Classical-ML-Fundamentals/
├── README.md
├── requirements.txt
├── ml_basics.py              # Basic ML algorithms
├── overfitting_underfitting.py  # Model complexity concepts
├── pipelines.py              # ML pipeline organization
└── train_validation_test.py # Data splitting and leakage
```

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run examples:**
   ```bash
   # Basic ML algorithms
   python ml_basics.py
   
   # Overfitting/underfitting
   python overfitting_underfitting.py
   
   # Pipelines
   python pipelines.py
   
   # Train/validation/test split
   python train_validation_test.py
   ```

## Key Concepts

### Basic ML Algorithms

#### Linear Regression
- Predicts continuous values
- Assumes linear relationship
- Fast and interpretable

#### Decision Tree
- Handles non-linear relationships
- Can overfit easily
- Interpretable (can visualize tree)

#### Random Forest
- Ensemble of decision trees
- More robust than single tree
- Less prone to overfitting

### Overfitting vs Underfitting

#### Overfitting
- **Sign:** Low training error, high test error
- **Cause:** Model too complex (memorizes training data)
- **Solution:** Reduce complexity (simpler model, regularization)

#### Underfitting
- **Sign:** High training error, high test error
- **Cause:** Model too simple (can't learn pattern)
- **Solution:** Increase complexity (more features, deeper model)

#### Good Fit
- **Sign:** Similar train/test error, both low
- **Balance:** Right model complexity for the data

### ML Pipelines

- **Purpose:** Organize preprocessing and modeling steps
- **Benefit:** Prevents data leakage, makes code reusable
- **Structure:** Preprocessing → Model → Prediction

### Train/Validation/Test Split

- **Train (60-80%):** Learn model parameters
- **Validation (10-20%):** Tune hyperparameters, choose best model
- **Test (10-20%):** Final evaluation (unbiased estimate)

**Critical Rule:** Test set should only be used once, at the very end!

### Data Leakage

**What it is:** Information from test set leaks into training

**Common causes:**
- Preprocessing before splitting data
- Using future information to predict past
- Target encoding with test data statistics

**Prevention:**
- Always split data FIRST
- Fit preprocessing only on training data
- Transform test data with fitted preprocessor

## Common Pitfalls

1. **Preprocessing before split:** Causes data leakage
2. **Using test set multiple times:** Biases performance estimate
3. **Ignoring validation set:** Can't tune hyperparameters properly
4. **Not recognizing overfitting:** Deploys model that fails in production
5. **Choosing wrong algorithm:** Linear model for non-linear data (or vice versa)

## Production Notes

- Always use pipelines in production (ensures consistent preprocessing)
- Monitor model performance over time (concept drift)
- Retrain models periodically with new data
- Use validation set for hyperparameter tuning
- Test set is for final evaluation only (use once!)
- Implement data validation before model input

---
**Created by:** [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)  
**Author:** Barbaros Kaymak

