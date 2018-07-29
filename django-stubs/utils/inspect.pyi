# Stubs for django.utils.inspect (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from typing import Callable, List

def get_func_args(func: Callable) -> List[str]: ...
def get_func_full_args(func: Any): ...
def func_accepts_kwargs(func: Callable) -> bool: ...
def func_accepts_var_args(func: Callable) -> bool: ...
def func_has_no_args(func: Any): ...
def func_supports_parameter(func: Callable, parameter: str) -> bool: ...
