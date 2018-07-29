# Stubs for django.db.backends.sqlite3.operations (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.operations import BaseDatabaseOperations
from typing import Any

from datetime import date, datetime, time, timedelta
from django.core.management.color import Style
from django.db.backends.sqlite3.base import DatabaseWrapper, SQLiteCursorWrapper
from django.db.backends.utils import CursorDebugWrapper
from django.db.models.aggregates import Aggregate, Max
from django.db.models.expressions import Col, CombinedExpression, Expression, F, OrderBy
from django.db.models.functions.comparison import Cast
from django.db.models.functions.datetime import TruncBase
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from uuid import UUID

class DatabaseOperations(BaseDatabaseOperations):
    cast_char_field_without_max_length: str = ...
    cast_data_types: Any = ...
    explain_prefix: str = ...
    def bulk_batch_size(self, fields: Any, objs: Any) -> int: ...
    def check_expression_support(self, expression: Union[OrderBy, Expression]) -> None: ...
    def date_extract_sql(self, lookup_type: str, field_name: str) -> str: ...
    def date_interval_sql(self, timedelta: timedelta) -> str: ...
    def format_for_duration_arithmetic(self, sql: str) -> str: ...
    def date_trunc_sql(self, lookup_type: str, field_name: str) -> str: ...
    def time_trunc_sql(self, lookup_type: str, field_name: str) -> str: ...
    def _convert_tzname_to_sql(self, tzname: Optional[str]) -> str: ...
    def datetime_cast_date_sql(self, field_name: str, tzname: str) -> str: ...
    def datetime_cast_time_sql(self, field_name: str, tzname: str) -> str: ...
    def datetime_extract_sql(
        self, lookup_type: str, field_name: str, tzname: Optional[str]
    ) -> str: ...
    def datetime_trunc_sql(
        self, lookup_type: str, field_name: str, tzname: Optional[str]
    ) -> str: ...
    def time_extract_sql(self, lookup_type: str, field_name: str) -> str: ...
    def pk_default_value(self) -> str: ...
    def _quote_params_for_last_executed_query(self, params: Any): ...
    def last_executed_query(
        self,
        cursor: Union[SQLiteCursorWrapper, CursorDebugWrapper],
        sql: str,
        params: Optional[Union[List[str], Tuple]],
    ) -> str: ...
    def quote_name(self, name: str) -> str: ...
    def no_limit_value(self) -> int: ...
    def sql_flush(
        self,
        style: Style,
        tables: List[str],
        sequences: Union[List[Dict[str, str]], Tuple],
        allow_cascade: bool = ...,
    ) -> List[str]: ...
    def execute_sql_flush(self, using: str, sql_list: List[str]) -> None: ...
    def adapt_datetimefield_value(
        self, value: Optional[Union[datetime, F]]
    ) -> Optional[Union[str, F]]: ...
    def adapt_timefield_value(self, value: Optional[time]) -> Optional[str]: ...
    def get_db_converters(self, expression: Expression) -> List[Callable]: ...
    def convert_datetimefield_value(
        self,
        value: Optional[Union[str, datetime]],
        expression: Expression,
        connection: DatabaseWrapper,
    ) -> Optional[datetime]: ...
    def convert_datefield_value(
        self,
        value: Optional[Union[str, date]],
        expression: Union[Col, Cast, Aggregate, django.db.models.functions.TruncBase],
        connection: DatabaseWrapper,
    ) -> Optional[date]: ...
    def convert_timefield_value(
        self,
        value: Optional[Union[str, time]],
        expression: Union[Col, Max, django.db.models.functions.TruncBase],
        connection: DatabaseWrapper,
    ) -> Optional[time]: ...
    def get_decimalfield_converter(
        self, expression: Union[Col, CombinedExpression, Aggregate]
    ) -> Callable: ...
    def convert_uuidfield_value(
        self, value: Optional[str], expression: Col, connection: DatabaseWrapper
    ) -> Optional[UUID]: ...
    def convert_booleanfield_value(
        self, value: Optional[int], expression: Expression, connection: DatabaseWrapper
    ) -> Optional[bool]: ...
    def bulk_insert_sql(self, fields: Any, placeholder_rows: Any) -> str: ...
    def combine_expression(self, connector: str, sub_expressions: List[str]) -> str: ...
    def combine_duration_expression(
        self, connector: str, sub_expressions: List[str]
    ) -> str: ...
    def integer_field_range(self, internal_type: str) -> Tuple[None, None]: ...
    def subtract_temporals(
        self,
        internal_type: str,
        lhs: Tuple[str, List[Any]],
        rhs: Union[Tuple[str, List[str]], Tuple[str, List[Any]]],
    ) -> Union[Tuple[str, List[str]], Tuple[str, List[Any]]]: ...
