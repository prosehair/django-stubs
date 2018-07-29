# Stubs for django.contrib.admin.widgets (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django import forms
from typing import Any, Optional

from datetime import datetime
from django.contrib.admin.sites import AdminSite
from django.db.models.fields.reverse_related import ForeignObjectRel, ManyToOneRel
from django.forms.widgets import Media, Select
from django.http.request import QueryDict
from django.utils.datastructures import MultiValueDict
from typing import Any, Dict, List, Optional, Set, Tuple, Union

class FilteredSelectMultiple(forms.SelectMultiple):
    @property
    def media(self) -> Media: ...
    verbose_name: Any = ...
    is_stacked: Any = ...
    def __init__(
        self, verbose_name: str, is_stacked: bool, attrs: None = ..., choices: Tuple = ...
    ) -> None: ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...

class AdminDateWidget(forms.DateInput):
    @property
    def media(self) -> Media: ...
    def __init__(self, attrs: None = ..., format: None = ...) -> None: ...

class AdminTimeWidget(forms.TimeInput):
    @property
    def media(self) -> Media: ...
    def __init__(self, attrs: None = ..., format: None = ...) -> None: ...

class AdminSplitDateTime(forms.SplitDateTimeWidget):
    template_name: str = ...
    def __init__(self, attrs: None = ...) -> None: ...
    def get_context(
        self, name: str, value: Optional[datetime], attrs: Dict[str, Union[bool, str]]
    ) -> Dict[
        str,
        Union[
            Dict[str, Any],
            str,
            Dict[
                str,
                Union[
                    str,
                    bool,
                    Dict[str, Union[bool, str]],
                    List[Dict[str, Union[str, bool, Dict[str, Union[bool, str]]]]],
                ],
            ],
            Dict[
                str,
                Union[
                    str,
                    bool,
                    Dict[str, str],
                    List[Dict[str, Union[str, bool, Dict[str, str]]]],
                ],
            ],
        ],
    ]: ...

class AdminRadioSelect(forms.RadioSelect):
    template_name: str = ...

class AdminFileWidget(forms.ClearableFileInput):
    template_name: str = ...

def url_params_from_lookup_dict(lookups: Dict[str, Union[str, int]]) -> Dict[str, str]: ...

class ForeignKeyRawIdWidget(forms.TextInput):
    template_name: str = ...
    rel: Any = ...
    admin_site: Any = ...
    db: Any = ...
    def __init__(
        self, rel: ManyToOneRel, admin_site: AdminSite, attrs: None = ..., using: None = ...
    ) -> None: ...
    def get_context(
        self, name: str, value: None, attrs: Dict[str, Union[bool, str]]
    ) -> Dict[
        str, Union[Dict[str, Union[str, bool, None, Dict[str, Union[bool, str]]]], str]
    ]: ...
    def base_url_parameters(self) -> Dict[str, str]: ...
    def url_parameters(self) -> Dict[str, str]: ...
    def label_and_url_for_value(self, value: Any): ...

class ManyToManyRawIdWidget(ForeignKeyRawIdWidget):
    template_name: str = ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    def url_parameters(self): ...
    def label_and_url_for_value(self, value: Any): ...
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...
    def format_value(self, value: Any): ...

class RelatedFieldWidgetWrapper(forms.Widget):
    template_name: str = ...
    needs_multipart_form: Any = ...
    attrs: Any = ...
    choices: Any = ...
    widget: Any = ...
    rel: Any = ...
    can_add_related: Any = ...
    can_change_related: Any = ...
    can_delete_related: Any = ...
    can_view_related: Any = ...
    admin_site: Any = ...
    def __init__(
        self,
        widget: Union[Select, AdminRadioSelect],
        rel: ForeignObjectRel,
        admin_site: AdminSite,
        can_add_related: Optional[bool] = ...,
        can_change_related: bool = ...,
        can_delete_related: bool = ...,
        can_view_related: bool = ...,
    ) -> None: ...
    def __deepcopy__(self, memo: Dict[int, Any]) -> RelatedFieldWidgetWrapper: ...
    @property
    def is_hidden(self) -> bool: ...
    @property
    def media(self) -> Media: ...
    def get_related_url(self, info: Tuple[str, str], action: str, *args: Any) -> str: ...
    def get_context(
        self, name: str, value: Optional[Union[str, int]], attrs: Dict[str, str]
    ) -> Dict[str, Union[bool, str]]: ...
    def value_from_datadict(
        self, data: QueryDict, files: MultiValueDict, name: str
    ) -> Optional[str]: ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...
    def id_for_label(self, id_: str) -> str: ...

class AdminTextareaWidget(forms.Textarea):
    def __init__(self, attrs: None = ...) -> None: ...

class AdminTextInputWidget(forms.TextInput):
    def __init__(self, attrs: None = ...) -> None: ...

class AdminEmailInputWidget(forms.EmailInput):
    def __init__(self, attrs: None = ...) -> None: ...

class AdminURLFieldWidget(forms.URLInput):
    template_name: str = ...
    def __init__(self, attrs: None = ...) -> None: ...
    def get_context(
        self, name: str, value: None, attrs: Dict[str, str]
    ) -> Dict[str, Union[Dict[str, Union[str, bool, None, Dict[str, str]]], str]]: ...

class AdminIntegerFieldWidget(forms.NumberInput):
    class_name: str = ...
    def __init__(self, attrs: None = ...) -> None: ...

class AdminBigIntegerFieldWidget(AdminIntegerFieldWidget):
    class_name: str = ...

SELECT2_TRANSLATIONS: Any

class AutocompleteMixin:
    url_name: str = ...
    rel: Any = ...
    admin_site: Any = ...
    db: Any = ...
    choices: Any = ...
    attrs: Any = ...
    def __init__(
        self,
        rel: ManyToOneRel,
        admin_site: AdminSite,
        attrs: None = ...,
        choices: Tuple = ...,
        using: None = ...,
    ) -> None: ...
    def get_url(self) -> str: ...
    def build_attrs(
        self, base_attrs: Dict[Any, Any], extra_attrs: Dict[str, str] = ...
    ) -> Dict[str, str]: ...
    def optgroups(
        self, name: str, value: List[str], attr: Dict[str, str] = ...
    ) -> Union[
        List[Tuple[None, List[Dict[str, Union[str, int, Set[str], Dict[str, bool]]]], int]],
        List[Tuple[None, List[Dict[str, Union[bool, str]]], int]],
    ]: ...
    @property
    def media(self) -> Media: ...

class AutocompleteSelect(AutocompleteMixin, forms.Select): ...
class AutocompleteSelectMultiple(AutocompleteMixin, forms.SelectMultiple): ...
