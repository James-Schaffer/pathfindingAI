# dynamic runtime test loader
#
# import importlib
# import os
# import sys
#
# tests = []
#
# _tests_dir = os.path.dirname(__file__)
# _this_module = sys.modules[__name__]
#
# for filename in os.listdir(_tests_dir):
# 	if filename.endswith(".py") and filename != "__init__.py":
# 		module_name = filename[:-3] # strip .py
# 		module = importlib.import_module(f".{module_name}", package=__name__)
#
# 		setattr(_this_module, module_name, module)

from .Test00 import *
from .Test01 import *
from .Test02 import *
from .Test03 import *
from .Test04 import *
from .Test05 import *
from .Test06 import *
from .Test07 import *
from .Test08 import *
from .Test09 import *

class test:
	env_size: tuple[int, int]
	env_data: list[str]
	start: tuple[int, int]
	end: tuple[int, int]