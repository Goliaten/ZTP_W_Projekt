import csv
from typing import Dict, Union
from pathlib import Path


def save_dict_to_csv(
    data: Dict[str, Dict[str, Union[float, str]]],
    filepath: str | Path,
) -> None:
    """
    Save a nested dictionary to a CSV file.

    Args:
        data: Dictionary where first level keys are row names,
              second level keys are column names, and values are floats or strings
        filepath: Path where the CSV file will be saved

    Example:
        data = {
            "row1": {"col1": 1.5, "col2": "text"},
            "row2": {"col1": 2.5, "col2": "more"}
        }
        save_dict_to_csv(data, "output.csv")
    """
    if not data:
        return

    # Convert to Path object for easier handling
    filepath = Path(filepath)

    # Get all unique column names (keys from inner dicts)
    all_columns = set()
    for row_dict in data.values():
        all_columns.update(row_dict.keys())

    columns = ["row"] + sorted(list(all_columns))

    # Write to CSV
    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns, extrasaction="ignore")

        # Write header
        writer.writerow(dict(zip(columns, columns)))

        # Write rows
        for row_name, row_data in data.items():
            row_dict: Dict[str, Union[str, float]] = {"row": row_name}
            row_dict.update(row_data)  # type: ignore
            writer.writerow(row_dict)
