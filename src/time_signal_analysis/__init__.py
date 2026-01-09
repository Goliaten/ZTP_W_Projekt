import importlib as il
import os
from typing import Dict
from src.helpers.CustomTypes import AnalysisModule

analyse_modules: Dict[str, AnalysisModule] = {}
exclude_entries = ["__init__", "__pycache__"]

for file in os.listdir(__path__[0]):
    file = os.path.splitext(file)[0]

    if file in exclude_entries:
        continue
    module_candidate = il.import_module(f".{file}", __package__)

    # validade module
    try:
        assert module_candidate.__dict__.get("analyse") is not None
        # TODO should also check signature of this function
        valid_module: AnalysisModule = module_candidate  # type: ignore
    except AssertionError:
        print(f"Module {file} is invalid. It's missing `analyse` method")
        continue

    analyse_modules[file] = valid_module

del file, module_candidate, valid_module, os, il, Dict, AnalysisModule
