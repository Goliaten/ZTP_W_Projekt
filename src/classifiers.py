import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from typing import Dict, Any

from src import config
from src.config import RESULT_CSV_FILENAME


def train_and_evaluate_knn(
    n_neighbors: int = config.KNN_NEIGHBOUR_COUNT,
    test_size: float = config.KNN_TEST_SPLIT,
    random_state: int = config.KNN_RANDOM_STATE,
    cv_folds: int = config.KNN_CROSS_VALIDATION_COUNT,
) -> Dict[str, Any]:
    """
    Train a k-NN classifier on analysis results with cross-validation and confusion matrix.

    Args:
        n_neighbors: Number of neighbors for k-NN classifier
        test_size: Fraction of data to use for testing (0.0-1.0)
        random_state: Seed for reproducibility
        cv_folds: Number of cross-validation folds

    Returns:
        Dictionary containing:
        - model: Trained KNeighborsClassifier
        - train_scores: Cross-validation scores
        - test_score: Accuracy on test set
        - confusion_matrix: Confusion matrix array
        - classification_report: Classification metrics report
        - feature_names: List of feature column names used
    """
    # Load data
    df = pd.read_csv(RESULT_CSV_FILENAME)

    # Columns to ignore
    ignore_columns = {"filename", "freq", "", "row"}

    # Extract features and target
    feature_columns = [
        col for col in df.columns if col not in ignore_columns and col != "class"
    ]

    X = df[feature_columns].values
    y = df["class"].values

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,  # type: ignore
    )

    # Create and train model
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)

    # Cross-validation
    cv_scores = cross_val_score(
        model, X_train, y_train, cv=cv_folds, scoring="accuracy"
    )

    # Evaluate on test set
    test_score = model.score(X_test, y_test)

    # Predictions and confusion matrix
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    # Classification report
    class_report = classification_report(y_test, y_pred, output_dict=True)

    return {
        "model": model,
        "train_scores": cv_scores,
        "train_scores_mean": float(np.mean(cv_scores)),
        "train_scores_std": float(np.std(cv_scores)),
        "test_score": float(test_score),
        "confusion_matrix": cm,
        "classification_report": class_report,
        "feature_names": feature_columns,
        "classes": sorted(list(set(y))),
        "n_neighbors": n_neighbors,
        "test_size": test_size,
        "cv_folds": cv_folds,
    }


def print_results(results: Dict[str, Any]) -> None:
    """
    Pretty-print k-NN training and evaluation results.

    Args:
        results: Dictionary returned from train_and_evaluate_knn()
    """
    print("\n" + "=" * 60)
    print("k-NN Classifier Results")
    print("=" * 60)

    print("\nModel Configuration:")
    print(f"  Number of neighbors: {results['n_neighbors']}")
    print(f"  Test set size: {results['test_size']:.1%}")
    print(f"  Cross-validation folds: {results['cv_folds']}")
    print(f"  Number of features: {len(results['feature_names'])}")

    print("\nCross-Validation Scores:")
    print(f"  Mean: {results['train_scores_mean']:.4f}")
    print(f"  Std:  {results['train_scores_std']:.4f}")
    print(f"  Fold scores: {[f'{s:.4f}' for s in results['train_scores']]}")

    print("\nTest Set Performance:")
    print(f"  Accuracy: {results['test_score']:.4f}")

    print("\nConfusion Matrix:")
    cm = results["confusion_matrix"]
    classes = results["classes"]
    print(f"  Classes: {classes}")
    print(cm)

    print("\nClassification Report:")
    report = results["classification_report"]
    for class_name, metrics in report.items():
        if class_name not in ["accuracy", "macro avg", "weighted avg"]:
            print(f"  {class_name}:")
            print(f"    Precision: {metrics.get('precision', 0):.4f}")
            print(f"    Recall:    {metrics.get('recall', 0):.4f}")
            print(f"    F1-Score:  {metrics.get('f1-score', 0):.4f}")

    print("=" * 60 + "\n")
