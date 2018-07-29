from django.db.migrations.graph import MigrationGraph
from django.db.migrations.migration import Migration
from django.db.migrations.operations.fields import FieldOperation
from django.db.migrations.operations.models import (
    AddIndex,
    CreateModel,
    DeleteModel,
    FieldRelatedOptionOperation,
    ModelOperation,
    RemoveIndex,
)
from django.db.migrations.questioner import MigrationQuestioner
from django.db.migrations.state import ProjectState
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.fields.reverse_related import ManyToOneRel
from typing import Any, Dict, List, Optional, Set, Tuple, Type, Union

class MigrationAutodetector:
    def __init__(
        self,
        from_state: ProjectState,
        to_state: ProjectState,
        questioner: Optional[MigrationQuestioner] = ...,
    ) -> None: ...
    def _build_migration_list(self, graph: Optional[MigrationGraph] = ...) -> None: ...
    def _detect_changes(
        self, convert_apps: Optional[Set[str]] = ..., graph: Optional[MigrationGraph] = ...
    ) -> Dict[str, List[Migration]]: ...
    def _generate_added_field(
        self, app_label: str, model_name: str, field_name: str
    ) -> None: ...
    def _generate_altered_foo_together(
        self, operation: Type[FieldRelatedOptionOperation]
    ) -> None: ...
    def _generate_removed_field(
        self, app_label: str, model_name: str, field_name: str
    ) -> None: ...
    def _generate_through_model_map(self) -> None: ...
    def _get_dependencies_for_foreign_key(
        self, field: Union[ManyToOneRel, ManyToManyField, ForeignKey]
    ) -> List[Tuple[str, str, None, bool]]: ...
    def _optimize_migrations(self) -> None: ...
    def _prepare_field_lists(self) -> None: ...
    def _sort_migrations(self) -> None: ...
    def _trim_to_apps(
        self, changes: Dict[str, List[Migration]], app_labels: Set[str]
    ) -> Dict[str, List[Migration]]: ...
    def add_operation(
        self,
        app_label: str,
        operation: Union[FieldOperation, RemoveIndex, ModelOperation],
        dependencies: Any = ...,
        beginning: bool = ...,
    ) -> None: ...
    def arrange_for_graph(
        self,
        changes: Dict[str, List[Migration]],
        graph: MigrationGraph,
        migration_name: Optional[str] = ...,
    ) -> Dict[str, List[Migration]]: ...
    def changes(
        self,
        graph: MigrationGraph,
        trim_to_apps: Optional[Set[str]] = ...,
        convert_apps: Optional[Set[str]] = ...,
        migration_name: None = ...,
    ) -> Dict[str, List[Migration]]: ...
    def check_dependency(
        self,
        operation: Union[FieldOperation, AddIndex, ModelOperation],
        dependency: Union[
            Tuple[str, str, None, bool],
            Tuple[str, str, str, str],
            Tuple[str, str, str, bool],
        ],
    ) -> bool: ...
    def create_altered_indexes(self) -> None: ...
    def deep_deconstruct(self, obj: object) -> Any: ...
    def generate_added_fields(self) -> None: ...
    def generate_added_indexes(self) -> None: ...
    def generate_altered_db_table(self) -> None: ...
    def generate_altered_fields(self) -> None: ...
    def generate_altered_index_together(self) -> None: ...
    def generate_altered_managers(self) -> None: ...
    def generate_altered_options(self) -> None: ...
    def generate_altered_order_with_respect_to(self) -> None: ...
    def generate_altered_unique_together(self) -> None: ...
    def generate_created_models(self) -> None: ...
    def generate_created_proxies(self) -> None: ...
    def generate_deleted_models(self) -> None: ...
    def generate_deleted_proxies(self) -> None: ...
    def generate_removed_fields(self) -> None: ...
    def generate_removed_indexes(self) -> None: ...
    def generate_renamed_fields(self) -> None: ...
    def generate_renamed_models(self) -> None: ...
    def only_relation_agnostic_fields(self, fields: Any) -> Any: ...
    @classmethod
    def parse_number(cls, name: str) -> int: ...
    @classmethod
    def suggest_name(
        cls,
        ops: Union[
            List[Union[CreateModel, FieldOperation]],
            List[CreateModel],
            List[ModelOperation],
            List[DeleteModel],
        ],
    ) -> str: ...
    def swappable_first_key(self, item: Tuple[str, str]) -> Tuple[str, str]: ...
