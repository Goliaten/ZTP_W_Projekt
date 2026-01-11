import numpy as np
import numpy.typing as npt
from typing import Any, Generator

from src.helpers.signal_cleaner import normalise_specter_signal, apply_window_function
from src.helpers.specter_helper import fourier_transform


def analyse(
    windows: Generator[npt.NDArray, None, None],
    freq: int,
) -> Any:
    """
    Analyze spectrum signal - even-indexed components.

    Calculates the sum of spectrum components at even indices (0, 2, 4, ...),
    averaged across windowed segments.

    Args:
        windows: Generator yielding signal windows from windower function
        raw_data: Raw time-domain signal
        freq: Sampling frequency in Hz

    Returns:
        Average sum of even-indexed spectrum components
    """
    results = []

    # Analyze each window from the generator
    for window in windows:
        # Apply Hamming window to reduce spectral leakage
        windowed_signal = apply_window_function(window, window_type="hamming")

        # Transform to frequency domain
        spectrum, _ = fourier_transform(windowed_signal, freq)

        # Normalize spectrum
        normalized_spectrum = normalise_specter_signal(spectrum)

        # Calculate even components
        even_indices = np.arange(0, len(normalized_spectrum), 2)
        even_sum = float(np.sum(normalized_spectrum[even_indices]))

        results.append(even_sum)

    # Return average across all windows
    return float(np.mean(results)) if results else 0.0
