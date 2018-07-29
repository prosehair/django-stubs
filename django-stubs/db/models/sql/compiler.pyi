# Stubs for django.db.models.sql.compiler (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.backends.utils import CursorWrapper
from django.db.models.base import Model
from django.db.models.expressions import Col, CombinedExpression, Expression, OrderBy
from django.db.models.functions.datetime import Trunc
from django.db.models.options import Options
from django.db.models.sql.query import Query, RawQuery
from itertools import chain
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple, Type, Union

FORCE: Any

class SQLCompiler:
    query: Any = ...
    connection: Any = ...
    using: Any = ...
    quote_cache: Any = ...
    select: Any = ...
    annotation_col_map: Any = ...
    klass_info: Any = ...
    ordering_parts: Any = ...
    def __init__(
        self,
        query: Union[Query, RawQuery],
        connection: DatabaseWrapper,
        using: Optional[str],
    ) -> None: ...
    col_count: Any = ...
    def setup_query(self) -> None: ...
    has_extra_select: Any = ...
    def pre_sql_setup(self) -> Any: ...
    def get_group_by(
        self, select: Any, order_by: Any
    ) -> Union[
        List[Tuple[str, List[Any]]],
        List[Union[Tuple[str, List[Any]], Tuple[str, List[str]]]],
        List[Union[Tuple[str, List[Any]], Tuple[str, List[int]]]],
    ]: ...
    def collapse_group_by(
        self,
        expressions: Union[
            List[Union[Col, CombinedExpression]],
            List[Expression],
            List[Col],
            List[Union[Col, Trunc]],
        ],
        having: Union[List[CombinedExpression], List[Col], Tuple],
    ) -> Union[
        List[Union[Col, CombinedExpression]],
        List[Expression],
        List[Col],
        List[Union[Col, Trunc]],
    ]: ...
    def get_select(self) -> Any: ...
    def get_order_by(self) -> Any: ...
    def get_extra_select(
        self,
        order_by: Union[
            List[Tuple[OrderBy, Tuple[str, List[Any], bool]]],
            List[Tuple[OrderBy, Tuple[str, Tuple, bool]]],
            List[
                Union[
                    Tuple[OrderBy, Tuple[str, List[int], bool]],
                    Tuple[OrderBy, Tuple[str, List[Any], bool]],
                ]
            ],
        ],
        select: Any,
    ) -> List[Tuple[OrderBy, Tuple[str, List[Any]], None]]: ...
    def quote_name_unless_alias(self, name: str) -> str: ...
    def compile(self, node: Any, select_format: object = ...) -> Any: ...
    def get_combinator_sql(
        self, combinator: str, all: bool
    ) -> Union[
        Tuple[List[str], List[Any]],
        Tuple[List[str], List[int]],
        Tuple[List[str], List[str]],
    ]: ...
    def as_sql(self, with_limits: bool = ..., with_col_aliases: bool = ...): ...
    def get_default_columns(
        self,
        start_alias: Optional[str] = ...,
        opts: Optional[Options] = ...,
        from_parent: Optional[Type[Model]] = ...,
    ) -> List[Col]: ...
    def get_distinct(self) -> Tuple[List[Any], List[Any]]: ...
    def find_ordering_name(
        self,
        name: str,
        opts: Options,
        alias: Optional[str] = ...,
        default_order: str = ...,
        already_seen: Optional[
            Union[
                Set[Tuple[None, Tuple[Tuple[str, str]]]],
                Set[
                    Union[
                        Tuple[None, Tuple[Tuple[str, str]]],
                        Tuple[Tuple[Tuple[str, str]], Tuple[Tuple[str, str]]],
                    ]
                ],
                Set[
                    Tuple[
                        None,
                        Tuple[Tuple[str, str]],
                        Tuple[Tuple[str, str]],
                        Tuple[Tuple[str, str]],
                    ]
                ],
            ]
        ] = ...,
    ) -> List[Tuple[OrderBy, bool]]: ...
    def _setup_joins(
        self, pieces: List[str], opts: Options, alias: Optional[str]
    ) -> Any: ...
    def get_from_clause(
        self
    ) -> Union[
        Tuple[List[str], List[Any]],
        Tuple[List[str], List[Union[int, str]]],
        Tuple[List[str], List[int]],
        Tuple[List[str], List[str]],
    ]: ...
    def get_related_selections(
        self,
        select: Any,
        opts: Optional[Options] = ...,
        root_alias: Optional[str] = ...,
        cur_depth: int = ...,
        requested: Any = ...,
        restricted: Optional[bool] = ...,
    ) -> List[Dict[str, Any]]: ...
    def get_select_for_update_of_arguments(self): ...
    def deferred_to_columns(self) -> Dict[Type[Model], Set[str]]: ...
    def get_converters(self, expressions: Any) -> Dict[int, Any]: ...
    def apply_converters(
        self, rows: chain, converters: Dict[int, Any]
    ) -> Iterator[Any]: ...
    def results_iter(
        self,
        results: Any = ...,
        tuple_expected: bool = ...,
        chunked_fetch: bool = ...,
        chunk_size: int = ...,
    ) -> chain: ...
    def has_results(self) -> bool: ...
    def execute_sql(
        self, result_type: str = ..., chunked_fetch: bool = ..., chunk_size: int = ...
    ) -> Optional[CursorWrapper]: ...
    def as_subquery_condition(
        self, alias: str, columns: List[str], compiler: SQLCompiler
    ) -> Union[Tuple[str, Tuple], Tuple[str, Tuple[str]]]: ...
    def explain_query(self) -> Iterator[str]: ...

class SQLInsertCompiler(SQLCompiler):
    return_id: bool = ...
    def field_as_sql(self, field: Any, val: Any): ...
    def prepare_value(self, field: Any, value: Any): ...
    def pre_save_val(self, field: Any, obj: Any): ...
    def assemble_as_sql(self, fields: Any, value_rows: Any): ...
    def as_sql(self): ...
    def execute_sql(self, return_id: bool = ...): ...

class SQLDeleteCompiler(SQLCompiler):
    def as_sql(self): ...

class SQLUpdateCompiler(SQLCompiler):
    def as_sql(self): ...
    def execute_sql(self, result_type: Any): ...
    def pre_sql_setup(self): ...

class SQLAggregateCompiler(SQLCompiler):
    col_count: Any = ...
    def as_sql(self) -> Any: ...

def cursor_iter(cursor: Any, sentinel: Any, col_count: Any, itersize: Any): ...
