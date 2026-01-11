import numpy as np
import numpy.typing as npt
from typing import Any, Generator

from src.helpers.signal_cleaner import normalise_specter_signal, apply_window_function
from src.helpers.specter_helper import fourier_transform


def analyse(windows: Generator[npt.NDArray, None, None], freq: int) -> Any:
    """
    Analyze spectrum signal - BR (Spectral Centroid).

    Calculates the center of gravity of the spectrum (spectral centroid),
    averaged across windowed segments.

    BR = Σ(f_i * |S(f_i)|) / Σ|S(f_i)|

    Args:
        windows: Generator yielding signal windows from windower function
        raw_data: Raw time-domain signal
        freq: Sampling frequency in Hz

    Returns:
        Average spectral centroid in Hz
    """
    results = []

    # Analyze each window from the generator
    for window in windows:
        # Apply Hamming window to reduce spectral leakage
        windowed_signal = apply_window_function(window, window_type="hamming")

        # Transform to frequency domain
        spectrum, spectrum_freq = fourier_transform(windowed_signal, freq)

        # Normalize spectrum
        normalized_spectrum = normalise_specter_signal(spectrum)

        # Calculate BR (spectral centroid)
        # Consider only positive frequencies
        positive_freq_idx = spectrum_freq >= 0
        positive_freq = spectrum_freq[positive_freq_idx]
        positive_spectrum = normalized_spectrum[positive_freq_idx]

        # Calculate centroid
        numerator = np.sum(positive_freq * positive_spectrum)
        denominator = np.sum(positive_spectrum)

        if denominator > 0:
            br = float(numerator / denominator)
        else:
            br = 0.0

        results.append(br)

    # Return average across all windows
    return float(np.mean(results)) if results else 0.0
