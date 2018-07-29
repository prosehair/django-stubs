# Stubs for django.utils.timesince (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from datetime import date

TIME_STRINGS: Any
TIMESINCE_CHUNKS: Any

def timesince(
    d: date, now: Optional[date] = ..., reversed: bool = ..., time_strings: None = ...
) -> str: ...
def timeuntil(d: date, now: Optional[date] = ..., time_strings: None = ...) -> str: ...
