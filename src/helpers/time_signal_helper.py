from scipy.signal import hilbert
import numpy.typing as npt
import numpy as np


def get_envelope(signal: npt.NDArray[np.integer]) -> npt.NDArray[np.integer]:
    analytic_signal = hilbert(signal)
    return np.abs(analytic_signal)
