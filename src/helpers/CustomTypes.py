from abc import abstractmethod
from types import ModuleType
from typing import Any, Dict

import numpy.typing as npt
import numpy as np


class AnalysisModule(ModuleType):
    @staticmethod
    @abstractmethod
    def analyse(
        *,
        data: npt.NDArray[np.integer],
        raw_data: npt.NDArray[np.integer],
        freq: int,
        **kwargs,
    ) -> Dict[str, Any]:
        pass
