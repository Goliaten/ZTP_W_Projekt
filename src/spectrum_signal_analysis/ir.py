import numpy as np
import numpy.typing as npt
from typing import Any, Generator

from src.helpers.signal_cleaner import normalise_specter_signal, apply_window_function
from src.helpers.specter_helper import fourier_transform


def analyse(
    window_generator: Generator[npt.NDArray, None, None],
    freq: int,
) -> Any:
    """
    Analyze spectrum signal - IR (Spectral Irregularity).

    Calculates a measure of spectral irregularity (deviation from smooth spectrum),
    averaged across windowed segments.

    IR = Σ|S(f_i) - S(f_i-1)|

    Args:
        windows: Generator yielding signal windows from windower function
        raw_data: Raw time-domain signal
        freq: Sampling frequency in Hz

    Returns:
        Average spectral irregularity measure
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

        # Calculate IR (spectral irregularity)
        if len(normalized_spectrum) >= 2:
            # Calculate differences between consecutive bins
            differences = np.abs(np.diff(normalized_spectrum))
            ir = float(np.sum(differences))
        else:
            ir = 0.0

        results.append(ir)

    # Return average across all windows
    return float(np.mean(results)) if results else 0.0
