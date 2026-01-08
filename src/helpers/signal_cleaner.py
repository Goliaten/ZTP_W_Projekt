import numpy.typing as npt
import numpy as np

from src.helpers.params_helper import Params


def normalise_specter_signal():
    # TODO
    raise NotImplementedError()


def apply_window_function():
    # hamming, hanning
    # TODO
    raise NotImplementedError()


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
