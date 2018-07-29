# Stubs for django.contrib.auth.hashers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from collections import OrderedDict
from typing import Callable, Dict, List, Optional, Union

UNUSABLE_PASSWORD_PREFIX: str
UNUSABLE_PASSWORD_SUFFIX_LENGTH: int

def is_password_usable(encoded: Optional[str]) -> bool: ...
def check_password(
    password: str, encoded: str, setter: Optional[Callable] = ..., preferred: str = ...
) -> bool: ...
def make_password(
    password: Optional[str], salt: Optional[str] = ..., hasher: str = ...
) -> str: ...
def get_hashers() -> Union[
    List[UnsaltedMD5PasswordHasher],
    List[MD5PasswordHasher],
    List[BasePasswordHasher],
    List[PBKDF2PasswordHasher],
]: ...
def get_hashers_by_algorithm() -> Dict[str, BasePasswordHasher]: ...
def reset_hashers(**kwargs: Any) -> None: ...
def get_hasher(algorithm: str = ...) -> BasePasswordHasher: ...
def identify_hasher(encoded: str) -> BasePasswordHasher: ...
def mask_hash(hash: str, show: int = ..., char: str = ...) -> str: ...

class BasePasswordHasher:
    algorithm: Any = ...
    library: Any = ...
    def _load_library(self): ...
    def salt(self) -> str: ...
    def verify(self, password: Any, encoded: Any) -> None: ...
    def encode(self, password: Any, salt: Any) -> None: ...
    def safe_summary(self, encoded: str) -> None: ...
    def must_update(self, encoded: str) -> bool: ...
    def harden_runtime(self, password: str, encoded: str) -> None: ...

class PBKDF2PasswordHasher(BasePasswordHasher):
    algorithm: str = ...
    iterations: int = ...
    digest: Any = ...
    def encode(self, password: str, salt: str, iterations: Optional[int] = ...) -> str: ...
    def verify(self, password: str, encoded: str) -> bool: ...
    def safe_summary(self, encoded: Any): ...
    def must_update(self, encoded: str) -> bool: ...
    def harden_runtime(self, password: Any, encoded: Any) -> None: ...

class PBKDF2SHA1PasswordHasher(PBKDF2PasswordHasher):
    algorithm: str = ...
    digest: Any = ...

class Argon2PasswordHasher(BasePasswordHasher):
    algorithm: str = ...
    library: str = ...
    time_cost: int = ...
    memory_cost: int = ...
    parallelism: int = ...
    def encode(self, password: Any, salt: Any): ...
    def verify(self, password: Any, encoded: Any): ...
    def safe_summary(self, encoded: Any): ...
    def must_update(self, encoded: Any): ...
    def harden_runtime(self, password: Any, encoded: Any) -> None: ...
    def _decode(self, encoded: Any): ...

class BCryptSHA256PasswordHasher(BasePasswordHasher):
    algorithm: str = ...
    digest: Any = ...
    library: Any = ...
    rounds: int = ...
    def salt(self): ...
    def encode(self, password: Any, salt: Any): ...
    def verify(self, password: Any, encoded: Any): ...
    def safe_summary(self, encoded: Any): ...
    def must_update(self, encoded: Any): ...
    def harden_runtime(self, password: Any, encoded: Any) -> None: ...

class BCryptPasswordHasher(BCryptSHA256PasswordHasher):
    algorithm: str = ...
    digest: Any = ...

class SHA1PasswordHasher(BasePasswordHasher):
    algorithm: str = ...
    def encode(self, password: str, salt: str) -> str: ...
    def verify(self, password: str, encoded: str) -> bool: ...
    def safe_summary(self, encoded: Any): ...
    def harden_runtime(self, password: Any, encoded: Any) -> None: ...

class MD5PasswordHasher(BasePasswordHasher):
    algorithm: str = ...
    def encode(self, password: str, salt: str) -> str: ...
    def verify(self, password: str, encoded: str) -> bool: ...
    def safe_summary(self, encoded: str) -> OrderedDict: ...
    def harden_runtime(self, password: Any, encoded: Any) -> None: ...

class UnsaltedSHA1PasswordHasher(BasePasswordHasher):
    algorithm: str = ...
    def salt(self) -> str: ...
    def encode(self, password: str, salt: str) -> str: ...
    def verify(self, password: str, encoded: str) -> bool: ...
    def safe_summary(self, encoded: Any): ...
    def harden_runtime(self, password: Any, encoded: Any) -> None: ...

class UnsaltedMD5PasswordHasher(BasePasswordHasher):
    algorithm: str = ...
    def salt(self): ...
    def encode(self, password: str, salt: str) -> str: ...
    def verify(self, password: str, encoded: str) -> bool: ...
    def safe_summary(self, encoded: Any): ...
    def harden_runtime(self, password: Any, encoded: Any) -> None: ...

class CryptPasswordHasher(BasePasswordHasher):
    algorithm: str = ...
    library: str = ...
    def salt(self): ...
    def encode(self, password: Any, salt: Any): ...
    def verify(self, password: Any, encoded: Any): ...
    def safe_summary(self, encoded: Any): ...
    def harden_runtime(self, password: Any, encoded: Any) -> None: ...
