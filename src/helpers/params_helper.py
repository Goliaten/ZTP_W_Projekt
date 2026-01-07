from typing import Any, Dict, Type, TypeVar
import json

from src import config


class Singleton(type):
    _instances: Dict[Type[Any], Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Params(metaclass=Singleton):
    _type_var = TypeVar("T")  # type:ignore
    params: Dict[str, Any] = {}

    def __init__(self):
        with open(config.PARAMS_FILE, "r") as file:
            Params.params = json.load(file)
        super().__init__()

    @staticmethod
    def get(key: str, default: _type_var = None) -> Any | _type_var:  # type:ignore
        return Params.params.get(key, default)


Params()
