"""
Iris Classification Model Training Pipeline
This script trains a classification model on the Iris dataset and evaluates it.
Results, model, and hyperparameters are saved to the model_results folder.
"""

import json
import os
import pickle
from datetime import datetime
from pathlib import Path

import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, auc, precision_score, recall_score, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def create_results_directory():
    """Create model_results directory if it doesn't exist."""
    results_dir = Path("model_results")
    results_dir.mkdir(exist_ok=True)
    return results_dir


def load_and_prepare_data(test_size=0.2, random_state=42):
    """
    Load Iris dataset and split into train/test sets.
    
    Args:
        test_size: Proportion of data to use for testing
        random_state: Random seed for reproducibility
        
    Returns:
        X_train, X_test, y_train, y_test: Train/test datasets
    """
    print("Loading Iris dataset...")
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # For binary classification, use only classes 0 and 1
    mask = y != 2
    X = X[mask]
    y = y[mask]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    print(f"Train set size: {X_train.shape[0]}, Test set size: {X_test.shape[0]}")
    
    return X_train, X_test, y_train, y_test, scaler


def train_model(X_train, y_train, hyperparameters=None):
    """
    Train a Random Forest classification model.
    
    Args:
        X_train: Training features
        y_train: Training labels
        hyperparameters: Dictionary of hyperparameters (optional)
        
    Returns:
        Trained model and hyperparameters used
    """
    if hyperparameters is None:
        hyperparameters = {
            "n_estimators": 100,
            "max_depth": 10,
            "min_samples_split": 5,
            "min_samples_leaf": 2,
            "random_state": 42,
            "n_jobs": -1
        }
    
    print(f"\nTraining Random Forest model with hyperparameters: {hyperparameters}")
    model = RandomForestClassifier(**hyperparameters)
    model.fit(X_train, y_train)
    
    return model, hyperparameters


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model using multiple metrics.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels
        
    Returns:
        Dictionary with evaluation metrics
    """
    print("\nEvaluating model...")
    
    # Predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    auc_score = roc_auc_score(y_test, y_pred_proba)
    
    metrics = {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "auc": float(auc_score)
    }
    
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"AUC:       {auc_score:.4f}")
    
    return metrics, y_pred, y_pred_proba


def save_results(results_dir, model, scaler, metrics, hyperparameters):
    """
    Save model, scaler, metrics, and hyperparameters to results directory.
    
    Args:
        results_dir: Path to results directory
        model: Trained model
        scaler: Fitted scaler
        metrics: Dictionary of metrics
        hyperparameters: Dictionary of hyperparameters
    """
    print(f"\nSaving results to {results_dir}...")
    
    # Save model
    model_path = results_dir / "model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"  Model saved: {model_path}")
    
    # Save scaler
    scaler_path = results_dir / "scaler.pkl"
    with open(scaler_path, "wb") as f:
        pickle.dump(scaler, f)
    print(f"  Scaler saved: {scaler_path}")
    
    # Save metrics
    metrics_path = results_dir / "metrics.json"
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"  Metrics saved: {metrics_path}")
    
    # Save hyperparameters
    hyperparameters_path = results_dir / "hyperparameters.json"
    with open(hyperparameters_path, "w") as f:
        json.dump(hyperparameters, f, indent=4)
    print(f"  Hyperparameters saved: {hyperparameters_path}")
    
    # Save timestamp and summary
    summary = {
        "timestamp": datetime.now().isoformat(),
        "model_type": "Random Forest Classifier",
        "dataset": "Iris (binary classification - classes 0 vs 1)",
        "hyperparameters": hyperparameters,
        "metrics": metrics
    }
    
    summary_path = results_dir / "summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=4)
    print(f"  Summary saved: {summary_path}")


def main():
    print("=" * 60)
    print("Iris Classification Model Training Pipeline")
    print("=" * 60)
    
    results_dir = create_results_directory()    
    X_train, X_test, y_train, y_test, scaler = load_and_prepare_data()    
    model, hyperparameters = traine_model(X_train, y_train)    
    metrics, y_pred, y_pred_proba = evaluate_model(model, x_train, y_test)    
    save_results(results_dir, model, scaler, metrics, hyperparameters)
    
    print("\n" + "=" * 60)
    print("Pipeline completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
