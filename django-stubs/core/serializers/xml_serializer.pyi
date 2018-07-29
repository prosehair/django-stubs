# Stubs for django.core.serializers.xml_serializer (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.serializers import base
from typing import Any
from xml.sax.expatreader import ExpatParser as _ExpatParser

from io import BufferedReader, TextIOWrapper
from django.core.serializers.base import DeserializedObject
from django.db.models.base import Model
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey, ManyToManyField
from typing import List, Optional, Type, Union
from xml.dom.minidom import Element

class Serializer(base.Serializer):
    def indent(self, level: int) -> None: ...
    xml: Any = ...
    def start_serialization(self) -> None: ...
    def end_serialization(self) -> None: ...
    def start_object(self, obj: Model) -> None: ...
    def end_object(self, obj: Model) -> None: ...
    def handle_field(self, obj: Model, field: Field) -> None: ...
    def handle_fk_field(self, obj: Model, field: ForeignKey) -> None: ...
    def handle_m2m_field(self, obj: Model, field: ManyToManyField) -> None: ...
    def _start_relational_field(
        self, field: Union[ManyToManyField, ForeignKey]
    ) -> None: ...

class Deserializer(base.Deserializer):
    event_stream: Any = ...
    db: Any = ...
    ignore: Any = ...
    def __init__(
        self,
        stream_or_string: Union[str, TextIOWrapper, BufferedReader],
        *,
        using: Any = ...,
        ignorenonexistent: bool = ...,
        **options: Any,
    ) -> None: ...
    def _make_parser(self) -> DefusedExpatParser: ...
    def __next__(self) -> DeserializedObject: ...
    def _handle_object(self, node: Element) -> DeserializedObject: ...
    def _handle_fk_field_node(self, node: Element, field: ForeignKey) -> Optional[int]: ...
    def _handle_m2m_field_node(
        self, node: Element, field: ManyToManyField
    ) -> List[int]: ...
    def _get_model_from_node(self, node: Element, attr: str) -> Type[Model]: ...

def getInnerText(node: Element) -> str: ...

class DefusedExpatParser(_ExpatParser):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def start_doctype_decl(
        self, name: Any, sysid: Any, pubid: Any, has_internal_subset: Any
    ) -> None: ...
    def entity_decl(
        self,
        name: Any,
        is_parameter_entity: Any,
        value: Any,
        base: Any,
        sysid: Any,
        pubid: Any,
        notation_name: Any,
    ) -> None: ...
    def unparsed_entity_decl(
        self, name: Any, base: Any, sysid: Any, pubid: Any, notation_name: Any
    ) -> None: ...
    def external_entity_ref_handler(
        self, context: Any, base: Any, sysid: Any, pubid: Any
    ) -> None: ...
    def reset(self) -> None: ...

class DefusedXmlException(ValueError):
    def __repr__(self): ...

class DTDForbidden(DefusedXmlException):
    name: Any = ...
    sysid: Any = ...
    pubid: Any = ...
    def __init__(self, name: Any, sysid: Any, pubid: Any) -> None: ...
    def __str__(self): ...

class EntitiesForbidden(DefusedXmlException):
    name: Any = ...
    value: Any = ...
    base: Any = ...
    sysid: Any = ...
    pubid: Any = ...
    notation_name: Any = ...
    def __init__(
        self, name: Any, value: Any, base: Any, sysid: Any, pubid: Any, notation_name: Any
    ) -> None: ...
    def __str__(self): ...

class ExternalReferenceForbidden(DefusedXmlException):
    context: Any = ...
    base: Any = ...
    sysid: Any = ...
    pubid: Any = ...
    def __init__(self, context: Any, base: Any, sysid: Any, pubid: Any) -> None: ...
    def __str__(self): ...
