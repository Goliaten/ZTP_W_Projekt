from typing import Any, Dict
import numpy.typing as npt
import numpy as np

from src.helpers.params_helper import Params
from src.helpers.time_signal_helper import get_envelope


def analyse(
    *,
    data: npt.NDArray[np.integer],
    raw_data: npt.NDArray[np.integer],
    freq: int,
    **kwargs,
) -> Dict[str, Dict[str, Any]]:
    main_param = Params.get("time_analysis").get("attack_time")
    envelope = get_envelope(data)
    thresh = main_param.get("threshold")

    max_amp = np.max(envelope)
    threshold_amp = thresh * max_amp
    above_threshold = np.where(envelope > threshold_amp)[0]

    if len(above_threshold) == 0:
        return {}

    start = above_threshold[0]
    peak = np.argmax(envelope)

    data_len = len(data)

    return {
        "absolute": {"start": start, "end": peak, "period": peak - start},
        "relative": {
            "start": start / data_len,
            "end": peak / data_len,
            "period": (peak - start) / data_len,
        },
        "timed": {
            "start": start / freq,
            "end": peak / freq,
            "period": (peak - start) / freq,
        },
    }
    # return (peak - start) / sr  # in seconds
