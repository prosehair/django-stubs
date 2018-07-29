# Stubs for django.forms.forms (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.forms.widgets import MediaDefiningClass
from typing import Any, Optional

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms.boundfield import BoundField
from django.forms.utils import ErrorDict, ErrorList
from django.utils.datastructures import MultiValueDict
from django.utils.safestring import SafeText
from typing import Any, Dict, Iterator, List, Optional, Type, Union

class DeclarativeFieldsMetaclass(MediaDefiningClass):
    def __new__(mcs: Any, name: Any, bases: Any, attrs: Any): ...
    @classmethod
    def __prepare__(metacls: Any, name: Any, bases: Any, **kwds: Any): ...

class BaseForm:
    default_renderer: Any = ...
    field_order: Any = ...
    prefix: Any = ...
    use_required_attribute: bool = ...
    is_bound: Any = ...
    data: Any = ...
    files: Any = ...
    auto_id: Any = ...
    initial: Any = ...
    error_class: Any = ...
    label_suffix: Any = ...
    empty_permitted: Any = ...
    _errors: Any = ...
    fields: Any = ...
    _bound_fields_cache: Any = ...
    renderer: Any = ...
    def __init__(
        self,
        data: Any = ...,
        files: Optional[Union[MultiValueDict, Dict[str, SimpleUploadedFile]]] = ...,
        auto_id: Optional[Union[str, bool]] = ...,
        prefix: Optional[str] = ...,
        initial: Any = ...,
        error_class: Type[ErrorList] = ...,
        label_suffix: None = ...,
        empty_permitted: bool = ...,
        field_order: None = ...,
        use_required_attribute: Optional[bool] = ...,
        renderer: object = ...,
    ) -> None: ...
    def order_fields(self, field_order: Any): ...
    def __str__(self): ...
    def __repr__(self) -> str: ...
    def __iter__(self) -> Iterator[BoundField]: ...
    def __getitem__(self, name: str) -> BoundField: ...
    @property
    def errors(self) -> ErrorDict: ...
    def is_valid(self): ...
    def add_prefix(self, field_name: str) -> str: ...
    def add_initial_prefix(self, field_name: str) -> str: ...
    def _html_output(
        self,
        normal_row: str,
        error_row: str,
        row_ender: str,
        help_text_html: str,
        errors_on_separate_row: bool,
    ) -> SafeText: ...
    def as_table(self) -> SafeText: ...
    def as_ul(self) -> SafeText: ...
    def as_p(self) -> SafeText: ...
    def non_field_errors(self): ...
    def add_error(
        self, field: Optional[str], error: Union[str, ValidationError]
    ) -> None: ...
    def has_error(self, field: Any, code: Optional[Any] = ...): ...
    cleaned_data: Any = ...
    def full_clean(self) -> None: ...
    def _clean_fields(self) -> None: ...
    def _clean_form(self) -> None: ...
    def _post_clean(self) -> None: ...
    def clean(self) -> Dict[str, Any]: ...
    def has_changed(self): ...
    def changed_data(self) -> List[str]: ...
    @property
    def media(self): ...
    def is_multipart(self): ...
    def hidden_fields(self): ...
    def visible_fields(self): ...
    def get_initial_for_field(self, field: Any, field_name: Any): ...

class Form(BaseForm): ...
