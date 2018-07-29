# Stubs for django.db.migrations.utils (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from django.utils.functional import SimpleLazyObject

COMPILED_REGEX_TYPE: Any

class RegexObject:
    pattern: Any = ...
    flags: Any = ...
    def __init__(self, obj: SimpleLazyObject) -> None: ...
    def __eq__(self, other: RegexObject) -> bool: ...

def get_migration_name_timestamp() -> str: ...
