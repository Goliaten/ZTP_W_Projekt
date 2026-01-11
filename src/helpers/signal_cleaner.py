from typing import Optional
import numpy.typing as npt
import numpy as np

from src.helpers.params_helper import Params


def normalise_specter_signal(
    spectrum: npt.NDArray[np.complexfloating],
) -> npt.NDArray[np.floating]:
    # Calculate magnitude spectrum
    magnitude = np.abs(spectrum)

    # Normalize by maximum value
    max_magnitude = np.max(magnitude)
    if max_magnitude > 0:
        normalized = magnitude / max_magnitude
    else:
        normalized = magnitude

    return normalized


def apply_window_function(
    signal: npt.NDArray[np.floating], window_type: Optional[str] = None
) -> npt.NDArray[np.floating]:
    if not window_type:
        main_param = Params.get("spectrum_analysis").get("window_function")
        window_type = main_param.get("window_type")

    signal_len = len(signal)
    windows = {
        "hamming": np.hamming,
        "hanning": np.hanning,
        "blackman": np.blackman,
        "bartlett": np.bartlett,
    }

    # Create window based on type
    if window_type in windows:
        window = windows[window_type](signal_len)
    else:
        raise ValueError(
            f"Unknown window type: {window_type}. "
            f"Supported types: {', '.join(list(windows.keys()))}"
        )

    # Apply window to signal
    windowed_signal = signal * window

    return windowed_signal


def ommit_noise_in_time_signal(
    data: npt.NDArray[np.integer], freq: int
) -> npt.NDArray[np.integer]:
    main_param = Params.get("time_analysis").get("signal_cleaning")

    # Convert ratio to actual indexes from max value of signal
    min_left = main_param.get("min_value_ratio_left") * max(data)
    min_right = main_param.get("min_value_ratio_right") * max(data)

    # Find the first values with at least given values
    left_index = np.argmax(data > min_left)
    right_index = len(data) - np.argmax(data[::-1] > min_right)

    # Slice the input with found indexes
    out_data = data[left_index:right_index]
    print(
        f"Cleaned time signal. Returned signal from index {left_index}({left_index / len(data):2.2%}) to index {right_index}({right_index / len(data):2.2%})"
    )
    return out_data
