from glob import glob
import os
from typing import Any, List, Tuple
import scipy.io as io

from src import config
import numpy.typing as npt
import numpy as np


def get_files(
    dir: str = config.INPUT_PATH,
    extensions: List[str] = config.ACCEPTED_FILE_EXTENSIONS,
) -> List[str]:
    out: List[str] = []
    for ext in extensions:
        out += glob(f"{dir}/**/*.{ext}", recursive=True)
    return out


def open_file(filepath: str) -> Tuple[int, npt.NDArray[np.integer]]:
    root, ext = os.path.splitext(filepath)
    match ext:
        case ".wav":
            return open_wav(filepath)
        case _:
            raise ValueError(f"Unknown file extension: {ext}")


def open_wav(filepath: str) -> Tuple[int, npt.NDArray[np.integer]]:
    fs, x = io.wavfile.read(filepath)
    return fs, x


def open_mp3(filepath: str):
    # TODO implement
    raise NotImplementedError()
