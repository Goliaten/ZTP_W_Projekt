import importlib as il
import os
from types import ModuleType
from typing import Dict

analyse_modules: Dict[str, ModuleType] = {}
exclude_entries = ["__init__", "__pycache__"]

for file in os.listdir(__path__[0]):
    file = os.path.splitext(file)[0]
    print(file)
    if file in exclude_entries:
        continue
    module_candidate = il.import_module(f".{file}", __package__)

    try:
        # validade module
        assert module_candidate.__dict__.get("analyse") is not None
    except AssertionError:
        print(f"Module {file} is invalid. It's missing `analyse` method")
        continue

    analyse_modules[file] = module_candidate
