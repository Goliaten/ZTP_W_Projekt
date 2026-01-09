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
    main_param = Params.get("time_analysis").get("release_time")
    envelope = get_envelope(data)

    # Normalize envelope for easier thresholding
    envelope = envelope / np.max(envelope)

    # Detect sustain phase (plateau)
    # Simple approach: find where the envelope is above a threshold (e.g., 0.9)
    sustain_threshold = main_param.get("sustain_threshold")
    sustain_indices = np.where(envelope > sustain_threshold)[0]

    if len(sustain_indices) == 0:
        return {"release_time": 0.0, "release_start_sample": 0, "release_end_sample": 0}

    sustain_end = sustain_indices[-1]

    # Detect release phase: after sustain, envelope drops below sustain_threshold
    release_start = sustain_end
    release_end = len(envelope) - 1

    # Find where envelope drops below a release threshold (e.g., 0.05)
    release_threshold = main_param.get("release_threshold")
    for i in range(release_start, len(envelope)):
        if envelope[i] < release_threshold:
            release_end = i
            break

    data_len = len(data)
    start = float(release_start)
    end = float(release_end)

    return {
        "absolute": {
            "start": start,
            "end": end,
            "period": end - start,
        },
        "relative": {
            "start": start / data_len,
            "end": end / data_len,
            "period": (end - start) / data_len,
        },
        "timed": {
            "start": start / freq,
            "end": end / freq,
            "period": (end - start) / freq,
        },
    }
