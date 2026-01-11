from typing import Tuple
from scipy.fft import fft, fftfreq
import numpy.typing as npt
import numpy as np


def fourier_transform(
    data: npt.NDArray[np.number], freq: int
) -> Tuple[npt.NDArray[np.complexfloating], npt.NDArray[np.floating]]:
    transformed = fft(data)
    fft_freq = fftfreq(len(data), 1 / freq)
    return transformed, fft_freq
