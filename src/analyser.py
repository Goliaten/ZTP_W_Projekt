from typing import Any, Dict

from src.helpers.file_helper import open_file
from src.helpers.params_helper import Params
from src.helpers.signal_cleaner import (
    ommit_noise_in_time_signal,
)
from src.helpers.window_helper import windower
import src.time_signal_analysis as time_analysis
import src.spectrum_signal_analysis as spectrum_analysis


def analyse_soundfile(path_to_file: str) -> Dict[str, Any]:
    print(f"Analysing {path_to_file}")
    freq, raw_time_data = open_file(path_to_file)
    # clean time data
    cleaned_time_data = ommit_noise_in_time_signal(raw_time_data, freq)
    out: Dict[str, Any] = {"freq": freq}

    # analyse cleaned time data
    for name, mod in time_analysis.analyse_modules.items():
        res = mod.analyse(data=cleaned_time_data, raw_data=raw_time_data, freq=freq)
        out[name] = res

    window_len = int(Params.get("window_generator").get("length_sec") * freq)
    window_overlap = Params.get("window_generator").get("overlap")

    # spectral analysis
    for name, mod in spectrum_analysis.analyse_modules.items():
        window_generator = windower(
            cleaned_time_data, length=window_len, overlap=window_overlap
        )
        res = mod.analyse(window_generator=window_generator, freq=freq)
        out[name] = res

    return out
