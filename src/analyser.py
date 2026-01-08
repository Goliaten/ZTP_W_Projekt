from typing import Any, Dict

from src.helpers.file_helper import open_file
from src.helpers.signal_cleaner import ommit_noise_in_time_signal
import src.time_signal_analysis as time_analysis


def analyse_soundfile(path_to_file: str) -> Dict[str, Any]:
    print(f"Analysing {path_to_file}")
    freq, raw_time_data = open_file(path_to_file)
    # clean time data
    cleaned_time_data = ommit_noise_in_time_signal(raw_time_data, freq)
    for name, mod in time_analysis.analyse_modules.items():
        # mod.analyse(data=cleaned_time_data, raw_data=raw_time_data, freq=freq)
        from src.time_signal_analysis.attack_time import analyse

        out = analyse(data=cleaned_time_data, raw_data=raw_time_data, freq=freq)
        print(out)
        exit()
    # analyse cleaned time data
    # convert time data to spectrum data
    # get window function
    # TODO
    raise NotImplementedError()
