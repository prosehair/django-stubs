# Stubs for django.core.cache.backends.dummy (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.cache.backends.base import BaseCache
from typing import Any, Optional

from typing import Any, Dict, Optional, Union

class DummyCache(BaseCache):
    def __init__(self, host: str, *args: Any, **kwargs: Any) -> None: ...
    def add(
        self, key: str, value: str, timeout: object = ..., version: None = ...
    ) -> bool: ...
    def get(
        self, key: str, default: Optional[str] = ..., version: Optional[int] = ...
    ) -> Optional[str]: ...
    def set(
        self,
        key: str,
        value: Union[str, Dict[str, Any], int],
        timeout: object = ...,
        version: Optional[str] = ...,
    ) -> None: ...
    def touch(self, key: Any, timeout: Any = ..., version: Optional[Any] = ...): ...
    def delete(self, key: Any, version: Optional[Any] = ...) -> None: ...
    def has_key(self, key: str, version: None = ...) -> bool: ...
    def clear(self) -> None: ...
