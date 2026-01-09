from typing import Any, Dict
import numpy.typing as npt
import numpy as np

from src.helpers.params_helper import Params
import src.time_signal_analysis as tsa


def analyse(
    *,
    data: npt.NDArray[np.integer],
    raw_data: npt.NDArray[np.integer],
    freq: int,
    **kwargs,
) -> Dict[str, Dict[str, Any]]:
    at = tsa.analyse_modules.get("attack_time")
    rt = tsa.analyse_modules.get("release_time")
    if not at or not rt:
        return {}

    at_out = at.analyse(data=data, raw_data=raw_data, freq=freq, **kwargs)
    rt_out = rt.analyse(data=data, raw_data=raw_data, freq=freq, **kwargs)
    attack_time = at_out.get("absolute", {}).get("period")
    release_time = rt_out.get("absolute", {}).get("period")

    return {
        "ar_ratio": attack_time / release_time,
        "ra_ratio": release_time / attack_time,
    }
