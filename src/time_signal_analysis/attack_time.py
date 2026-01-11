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
) -> Dict[str, Any]:
    main_param = Params.get("time_analysis").get("attack_time")
    envelope = get_envelope(data)
    thresh = main_param.get("threshold")

    max_amp = np.max(envelope)
    threshold_amp = thresh * max_amp

    # Peak (end of attack) is the max amplitude index
    peak_idx = int(np.argmax(envelope))

    # Find first crossing of threshold before or at the peak
    pre_peak_idx = envelope[: peak_idx + 1]
    cross = np.where(pre_peak_idx > threshold_amp)[0]
    if cross.size > 0:
        start_idx = int(cross[0])
    else:
        # fallback: first crossing anywhere
        all_cross = np.where(envelope > threshold_amp)[0]
        if all_cross.size > 0:
            start_idx = int(all_cross[0])
        else:
            return {}

    start = float(start_idx)
    peak = float(peak_idx)

    data_len = len(data)

    data_out = {
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
    return {"attack_time": data_out["relative"]["period"]}
    # return (peak - start) / sr  # in seconds
