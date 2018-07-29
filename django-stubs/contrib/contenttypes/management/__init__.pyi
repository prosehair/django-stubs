# Stubs for django.contrib.contenttypes.management (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db import migrations
from typing import Any, Optional

from django.apps.config import AppConfig
from django.apps.registry import Apps
from django.contrib.contenttypes.models import ContentType
from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from django.db.migrations.migration import Migration
from django.db.migrations.state import StateApps
from typing import Any, List, Tuple, Type, Union

class RenameContentType(migrations.RunPython):
    app_label: Any = ...
    old_model: Any = ...
    new_model: Any = ...
    def __init__(self, app_label: str, old_model: str, new_model: str) -> None: ...
    def _rename(
        self,
        apps: StateApps,
        schema_editor: DatabaseSchemaEditor,
        old_model: str,
        new_model: str,
    ) -> None: ...
    def rename_forward(
        self, apps: StateApps, schema_editor: DatabaseSchemaEditor
    ) -> None: ...
    def rename_backward(
        self, apps: StateApps, schema_editor: DatabaseSchemaEditor
    ) -> None: ...

def inject_rename_contenttypes_operations(
    plan: Union[List[Any], List[Tuple[Migration, bool]]] = ...,
    apps: StateApps = ...,
    using: str = ...,
    **kwargs: Any,
) -> None: ...
def get_contenttypes_and_models(
    app_config: AppConfig, using: str, ContentType: Type[ContentType]
) -> Any: ...
def create_contenttypes(
    app_config: AppConfig,
    verbosity: int = ...,
    interactive: bool = ...,
    using: str = ...,
    apps: Apps = ...,
    **kwargs: Any,
) -> None: ...
