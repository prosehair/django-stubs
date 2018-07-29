from django.db import DefaultConnectionProxy
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models.query import QuerySet
from typing import Optional, Set, Tuple, Union

class MigrationRecorder:
    def __init__(
        self,
        connection: Optional[
            Union[DefaultConnectionProxy, backends.base.base.BaseDatabaseWrapper]
        ],
    ) -> None: ...
    def applied_migrations(self) -> Set[Tuple[str, str]]: ...
    def ensure_schema(self) -> None: ...
    def flush(self) -> None: ...
    def has_table(self) -> bool: ...
    @property
    def migration_qs(self) -> QuerySet: ...
    def record_applied(self, app: str, name: str) -> None: ...
    def record_unapplied(self, app: str, name: str) -> None: ...
