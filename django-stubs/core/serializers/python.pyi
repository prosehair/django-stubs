# Stubs for django.core.serializers.python (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.serializers import base
from typing import Any

from collections import OrderedDict
from datetime import datetime
from django.core.serializers.base import DeserializedObject
from django.db.models.base import Model
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey, ManyToManyField
from typing import Any, Iterator, List, Optional, Type, Union

class Serializer(base.Serializer):
    internal_use_only: bool = ...
    _current: Any = ...
    objects: Any = ...
    def start_serialization(self) -> None: ...
    def end_serialization(self) -> None: ...
    def start_object(self, obj: Model) -> None: ...
    def end_object(self, obj: Model) -> None: ...
    def get_dump_object(self, obj: Model) -> OrderedDict: ...
    def _value_from_field(
        self, obj: Model, field: Field
    ) -> Optional[Union[str, float, datetime]]: ...
    def handle_field(self, obj: Model, field: Field) -> None: ...
    def handle_fk_field(self, obj: Model, field: ForeignKey) -> None: ...
    def handle_m2m_field(self, obj: Model, field: ManyToManyField) -> None: ...
    def getvalue(self) -> List[OrderedDict]: ...

def Deserializer(
    object_list: Any, *, using: Any = ..., ignorenonexistent: bool = ..., **options: Any
) -> Iterator[DeserializedObject]: ...
def _get_model(model_identifier: str) -> Type[Model]: ...
