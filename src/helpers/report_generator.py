from pathlib import Path
from typing import Dict, Any


def generate_report_md(
    knn_results: Dict[str, Any],
    class_metrics: Dict[str, Dict[str, Dict[str, float]]],
    output_path: str | Path = "classification_report.md",
) -> Path:
    """
    Generate a Polish Markdown report summarising k-NN classification
    results and per-class feature statistics.

    Args:
        knn_results: Output of `train_and_evaluate_knn()`
        class_metrics: Output of `compute_class_metrics()`
        output_path: Path to the output .md file

    Returns:
        Path to the written Markdown file
    """
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    lines = []

    # Header: overall results
    lines.append(f"# Wyniki klasyfikacji k-NN")
    lines.append("")

    # Parameters
    lines.append("## Parametry klasyfikatora")
    lines.append("")
    lines.append(f"- Liczba sąsiadów: {knn_results.get('n_neighbors')}")
    lines.append(f"- Udział zbioru testowego: {knn_results.get('test_size')}")
    lines.append(f"- Liczba foldów CV: {knn_results.get('cv_folds')}")
    lines.append("")

    # CV results
    lines.append("## Wyniki walidacji krzyżowej")
    lines.append("")
    train_mean = knn_results.get("train_scores_mean")
    train_std = knn_results.get("train_scores_std")
    fold_scores = knn_results.get("train_scores")
    if train_mean is not None:
        lines.append(f"- Średnia dokładność (CV): {train_mean:.4f}")
    if train_std is not None:
        lines.append(f"- Odchylenie standardowe (CV): {train_std:.4f}")
    if fold_scores is not None:
        lines.append(
            f"- Wyniki dla poszczególnych foldów: {', '.join([f'{s:.4f}' for s in fold_scores])}"
        )
    lines.append("")

    # Test results
    lines.append("## Wyniki na zbiorze testowym")
    lines.append("")
    test_score = knn_results.get("test_score")
    if test_score is not None:
        lines.append(f"- Dokładność: {test_score:.4f}")
    lines.append("")

    # Confusion matrix
    lines.append("## Macierz pomyłek")
    lines.append("")
    cm = knn_results.get("confusion_matrix")
    classes = knn_results.get("classes")
    if cm is not None and classes is not None:
        # Header row
        header = "| Klasa | " + " | ".join([str(c) for c in classes]) + " |"
        sep = "|---" + "|---" * len(classes) + "|"
        lines.append(header)
        lines.append(sep)
        for i, c in enumerate(classes):
            row = [str(int(x)) for x in cm[i]]
            lines.append(f"| {c} | " + " | ".join(row) + " |")
    else:
        lines.append("Brak macierzy pomyłek")
    lines.append("")

    # Classification report (per-class precision/recall/f1)
    lines.append("## Raport klasyfikacji (dokładność, precyzja, recall, F1)")
    lines.append("")
    class_report = knn_results.get("classification_report")
    if class_report:
        for cls, metrics in class_report.items():
            if cls in ["accuracy", "macro avg", "weighted avg"]:
                continue
            lines.append(f"### Klasa: {cls}")
            lines.append("")
            lines.append(f"- Precision: {metrics.get('precision', 0):.4f}")
            lines.append(f"- Recall:    {metrics.get('recall', 0):.4f}")
            lines.append(f"- F1-score:  {metrics.get('f1-score', 0):.4f}")
            lines.append("")
    else:
        lines.append("Brak raportu klasyfikacji")
    lines.append("")

    # Per-class characteristic sections
    if class_metrics:
        for cls_name, feats in class_metrics.items():
            lines.append(f"# {cls_name}")
            lines.append("")
            if not feats:
                lines.append("Brak danych dla tej klasy")
                lines.append("")
                continue

            # Table header
            lines.append("| Cecha | Min | Max | Std | Średnia | Mediana |")
            lines.append("|---|---:|---:|---:|---:|---:|")

            for feat_name, metrics in feats.items():
                min_v = metrics.get("min")
                max_v = metrics.get("max")
                std_v = metrics.get("std")
                avg_v = metrics.get("average")
                med_v = metrics.get("median")
                lines.append(
                    f"| {feat_name} | {min_v:.6g} | {max_v:.6g} | {std_v:.6g} | {avg_v:.6g} | {med_v:.6g} |"
                )

            lines.append("")
    else:
        lines.append("Brak statystyk per-klasa")

    out.write_text("\n".join(lines), encoding="utf-8")
    return out
