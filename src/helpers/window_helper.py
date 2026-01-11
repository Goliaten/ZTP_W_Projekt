import numpy as np
import numpy.typing as npt
from typing import Generator, Union


def windower(
    signal: Union[npt.NDArray, list], length: int, overlap: float
) -> Generator[npt.NDArray, None, None]:
    """
    Create a generator that yields overlapping windows from a signal.

    Args:
        signal: Input signal (array-like or list)
        length: Length of each window in samples
        overlap: Overlap ratio between 0 and 1 (e.g., 0.5 for 50% overlap)

    Returns:
        Generator that yields windows of the signal with specified length and overlap

    Raises:
        ValueError: If length is larger than signal or overlap is not in valid range
    """
    # Convert to numpy array if needed
    if isinstance(signal, list):
        signal = np.array(signal)

    signal_len = len(signal)

    # Validate inputs
    if length > signal_len:
        raise ValueError(
            f"Window length ({length}) cannot be larger than signal length ({signal_len})"
        )
    if not (0 <= overlap < 1):
        raise ValueError(f"Overlap ratio must be between 0 and 1, got {overlap}")

    # Calculate step size based on overlap
    step = int(length * (1 - overlap))
    if step < 1:
        step = 1

    def _window_generator():
        """Inner generator function that yields windows."""
        pos = 0
        while pos + length <= signal_len:
            yield signal[pos : pos + length]
            pos += step

        # Yield final window if there are remaining samples
        if pos < signal_len:
            yield signal[pos:signal_len]

    return _window_generator()
