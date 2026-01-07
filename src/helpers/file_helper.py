from glob import glob
import os
from typing import Any, List, Tuple
import scipy.io as io

from src import config


def get_files(
    dir: str = config.INPUT_PATH,
    extensions: List[str] = config.ACCEPTED_FILE_EXTENSIONS,
) -> List[str]:
    out: List[str] = []
    for ext in extensions:
        out += glob(f"{dir}/**/*.{ext}", recursive=True)
    return out


def open_file(filename: str):
    # TODO implement
    raise NotImplementedError()


def open_wav(filename: str) -> Tuple[int, List[Any]]:
    fs, x = io.wavfile.read(os.path.join(config.INPUT_PATH, filename))
    return fs, x


def open_mp3(filename: str):
    # TODO implement
    raise NotImplementedError()
