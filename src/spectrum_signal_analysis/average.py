import numpy as np
import numpy.typing as npt
from typing import Any, Generator

from src.helpers.signal_cleaner import normalise_specter_signal, apply_window_function
from src.helpers.specter_helper import fourier_transform


def analyse_(
    window_generator: Generator[npt.NDArray, None, None],
    freq: int,
) -> Any:
    """
    Analyze spectrum signal - average magnitude.

    Calculates the average magnitude across all frequency bins,
    averaged across windowed segments.

    Args:
        windows: Generator yielding signal windows from windower function
        raw_data: Raw time-domain signal
        freq: Sampling frequency in Hz

    Returns:
        Average spectrum magnitude
    """
    results = []

    # Analyze each window from the generator
    for window in window_generator:
        # Apply Hamming window to reduce spectral leakage
        windowed_signal = apply_window_function(window, window_type="hamming")

        # Transform to frequency domain
        spectrum, _ = fourier_transform(windowed_signal, freq)

        # Normalize spectrum
        normalized_spectrum = normalise_specter_signal(spectrum)

        # Calculate average magnitude
        avg_magnitude = float(np.mean(normalized_spectrum))

        results.append(avg_magnitude)

    # Return average across all windows
    return float(np.mean(results)) if results else 0.0
