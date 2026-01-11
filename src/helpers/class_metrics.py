import pandas as pd
from typing import Dict

from src.config import RESULT_CSV_FILENAME


def compute_class_metrics() -> Dict[str, Dict[str, Dict[str, float]]]:
    """
    Compute basic statistics per-class from the results CSV.

    Loads `RESULT_CSV_FILENAME` and for each class computes min, max,
    standard deviation, average (mean) and median for each feature column.

    Returns:
        Nested dict of the form {class: {feature: {metric: value}}}
    """
    df = pd.read_csv(RESULT_CSV_FILENAME)

    # Columns to ignore
    ignore_columns = {"row", "filename", "freq", "", "class"}

    feature_columns = [col for col in df.columns if col not in ignore_columns]

    results: Dict[str, Dict[str, Dict[str, float]]] = {}

    if "class" not in df.columns:
        return results

    grouped = df.groupby("class")

    for class_name, group in grouped:
        class_metrics: Dict[str, Dict[str, float]] = {}
        for col in feature_columns:
            # Attempt to coerce column to numeric; skip if entirely non-numeric
            series = pd.to_numeric(group[col], errors="coerce").dropna()
            if series.empty:
                continue

            class_metrics[col] = {
                "min": float(series.min()),
                "max": float(series.max()),
                "std": float(series.std(ddof=0)),
                "average": float(series.mean()),
                "median": float(series.median()),
            }

        results[str(class_name)] = class_metrics

    return results
