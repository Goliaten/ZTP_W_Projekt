# from typing import Any, Dict
# import numpy.typing as npt
# import numpy as np

# from src.helpers.params_helper import Params
# import src.time_signal_analysis as tsa


# def analyse_(
#     *,
#     data: npt.NDArray[np.integer],
#     raw_data: npt.NDArray[np.integer],
#     freq: int,
#     **kwargs,
# ) -> Dict[str, Dict[str, Any]]:
#     at = tsa.analyse_modules.get("attack_time")
#     rt = tsa.analyse_modules.get("release_time")
#     if not at or not rt:
#         return {}

#     at_out = at.analyse(data=data, raw_data=raw_data, freq=freq, **kwargs)
#     rt_out = rt.analyse(data=data, raw_data=raw_data, freq=freq, **kwargs)
#     attack_time = at_out.get("absolute", {}).get("period")
#     release_time = rt_out.get("absolute", {}).get("period")

#     # Guard against missing or zero values
#     try:
#         if not attack_time or not release_time:
#             return {"ar_ratio": None, "ra_ratio": None}

#         ar = float(attack_time) / float(release_time)
#         ra = float(release_time) / float(attack_time)
#     except Exception:
#         return {"ar_ratio": None, "ra_ratio": None}

#     return {"ar_ratio": ar, "ra_ratio": ra}
