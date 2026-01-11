import numpy as np
import numpy.typing as npt
from typing import Dict, Any

from src.helpers.params_helper import Params


def analyse(
    *,
    data: npt.NDArray[np.integer],
    raw_data: npt.NDArray[np.integer],
    freq: int,
    **kwargs,
) -> Dict[str, Any]:
    main_param = Params.get("time_analysis").get("zcr")
    num_of_samples = main_param.get("samples_to_analyse")

    max_val = data.argmax()
    data_ = data[max_val : max_val + min(num_of_samples, len(data))]

    zero_crossings = np.where(np.diff(np.sign(data_)))[0]

    zcr = len(zero_crossings) / (len(data_) / freq)

    return {"zcr": zcr}
