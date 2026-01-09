import numpy as np
import numpy.typing as npt
from typing import Dict, Any


def analyse(
    *,
    data: npt.NDArray[np.integer],
    raw_data: npt.NDArray[np.integer],
    freq: int,
    **kwargs,
) -> Dict[str, Any]:
    # TODO verify if this is correct

    zero_crossings = np.where(np.diff(np.sign(data)))[0]

    zcr = len(zero_crossings) / (len(data) / freq)

    return {"zcr": zcr}
