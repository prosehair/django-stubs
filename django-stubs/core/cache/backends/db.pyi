# Stubs for django.core.cache.backends.db (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.cache.backends.base import BaseCache
from typing import Any, Optional

from datetime import datetime
from django.db.backends.utils import CursorWrapper
from typing import Any, Callable, Dict, Optional, Union

class Options:
    db_table: Any = ...
    app_label: str = ...
    model_name: str = ...
    verbose_name: str = ...
    verbose_name_plural: str = ...
    object_name: str = ...
    abstract: bool = ...
    managed: bool = ...
    proxy: bool = ...
    swapped: bool = ...
    def __init__(self, table: str) -> None: ...

class BaseDatabaseCache(BaseCache):
    _table: Any = ...
    cache_model_class: Any = ...
    def __init__(
        self, table: str, params: Dict[str, Union[Callable, Dict[str, int], str, int]]
    ) -> None: ...

class DatabaseCache(BaseDatabaseCache):
    def get(
        self,
        key: str,
        default: Optional[Union[str, int]] = ...,
        version: Optional[int] = ...,
    ) -> Any: ...
    def set(
        self, key: str, value: Any, timeout: object = ..., version: Optional[int] = ...
    ) -> None: ...
    def add(
        self,
        key: str,
        value: Union[str, bytes, Dict[str, int], int],
        timeout: object = ...,
        version: Optional[int] = ...,
    ) -> bool: ...
    def touch(
        self, key: str, timeout: Optional[int] = ..., version: None = ...
    ) -> bool: ...
    def _base_set(self, mode: str, key: str, value: object, timeout: object = ...): ...
    def delete(self, key: str, version: Optional[int] = ...) -> None: ...
    def has_key(self, key: str, version: Optional[int] = ...): ...
    def _cull(self, db: str, cursor: CursorWrapper, now: datetime) -> None: ...
    def clear(self) -> None: ...
