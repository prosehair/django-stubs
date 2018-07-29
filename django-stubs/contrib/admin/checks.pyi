# Stubs for django.contrib.admin.checks (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from django.contrib.admin.options import InlineModelAdmin, ModelAdmin, TabularInline
from django.contrib.auth.models import Group, User
from django.core.checks.messages import Error
from django.db.models.base import Model
from typing import Any, List, Tuple, Type, Union

def check_admin_app(app_configs: Any, **kwargs: Any): ...
def check_dependencies(**kwargs: Any): ...

class BaseModelAdminChecks:
    def check(
        self, admin_obj: Union[ModelAdmin, InlineModelAdmin], **kwargs: Any
    ) -> List[Error]: ...
    def _check_autocomplete_fields(
        self, obj: Union[ModelAdmin, InlineModelAdmin]
    ) -> List[Any]: ...
    def _check_autocomplete_fields_item(
        self,
        obj: Union[ModelAdmin, InlineModelAdmin],
        model: Type[Model],
        field_name: str,
        label: str,
    ) -> List[Any]: ...
    def _check_raw_id_fields(
        self, obj: Union[ModelAdmin, InlineModelAdmin]
    ) -> List[Any]: ...
    def _check_raw_id_fields_item(
        self, obj: ModelAdmin, model: Type[Model], field_name: str, label: str
    ) -> List[Any]: ...
    def _check_fields(self, obj: Union[ModelAdmin, InlineModelAdmin]) -> List[Any]: ...
    def _check_fieldsets(self, obj: Union[ModelAdmin, InlineModelAdmin]) -> List[Any]: ...
    def _check_fieldsets_item(
        self,
        obj: Union[ModelAdmin, InlineModelAdmin],
        model: Type[Model],
        fieldset: Any,
        label: str,
        seen_fields: List[str],
    ) -> List[Any]: ...
    def _check_field_spec(
        self,
        obj: Union[ModelAdmin, InlineModelAdmin],
        model: Type[Model],
        fields: Union[str, Tuple[str, str, str, str], Tuple[str, str]],
        label: str,
    ) -> List[Any]: ...
    def _check_field_spec_item(
        self,
        obj: Union[ModelAdmin, TabularInline],
        model: Type[Model],
        field_name: str,
        label: str,
    ) -> List[Any]: ...
    def _check_exclude(self, obj: Union[ModelAdmin, InlineModelAdmin]) -> List[Any]: ...
    def _check_form(self, obj: Union[ModelAdmin, InlineModelAdmin]) -> List[Any]: ...
    def _check_filter_vertical(
        self, obj: Union[ModelAdmin, InlineModelAdmin]
    ) -> List[Any]: ...
    def _check_filter_horizontal(
        self, obj: Union[ModelAdmin, InlineModelAdmin]
    ) -> List[Any]: ...
    def _check_filter_item(
        self, obj: ModelAdmin, model: Type[Union[Group, User]], field_name: str, label: str
    ) -> List[Any]: ...
    def _check_radio_fields(
        self, obj: Union[ModelAdmin, InlineModelAdmin]
    ) -> List[Any]: ...
    def _check_radio_fields_key(
        self, obj: Any, model: Any, field_name: Any, label: Any
    ): ...
    def _check_radio_fields_value(self, obj: Any, val: Any, label: Any): ...
    def _check_view_on_site_url(
        self, obj: Union[ModelAdmin, InlineModelAdmin]
    ) -> List[Any]: ...
    def _check_prepopulated_fields(
        self, obj: Union[ModelAdmin, InlineModelAdmin]
    ) -> List[Any]: ...
    def _check_prepopulated_fields_key(
        self,
        obj: Union[ModelAdmin, InlineModelAdmin],
        model: Type[Model],
        field_name: str,
        label: str,
    ) -> List[Any]: ...
    def _check_prepopulated_fields_value(
        self,
        obj: Union[ModelAdmin, InlineModelAdmin],
        model: Type[Model],
        val: Union[List[str], Tuple[str]],
        label: str,
    ) -> List[Any]: ...
    def _check_prepopulated_fields_value_item(
        self,
        obj: Union[ModelAdmin, TabularInline],
        model: Type[Model],
        field_name: str,
        label: str,
    ) -> List[Any]: ...
    def _check_ordering(self, obj: Union[ModelAdmin, InlineModelAdmin]) -> List[Any]: ...
    def _check_ordering_item(
        self, obj: ModelAdmin, model: Type[Model], field_name: str, label: str
    ) -> List[Any]: ...
    def _check_readonly_fields(
        self, obj: Union[ModelAdmin, InlineModelAdmin]
    ) -> List[Any]: ...
    def _check_readonly_fields_item(
        self,
        obj: Union[ModelAdmin, TabularInline],
        model: Type[Model],
        field_name: str,
        label: str,
    ) -> List[Any]: ...

class ModelAdminChecks(BaseModelAdminChecks):
    def check(self, admin_obj: Any, **kwargs: Any): ...
    def _check_save_as(self, obj: Any): ...
    def _check_save_on_top(self, obj: Any): ...
    def _check_inlines(self, obj: Any): ...
    def _check_inlines_item(self, obj: Any, model: Any, inline: Any, label: Any): ...
    def _check_list_display(self, obj: Any): ...
    def _check_list_display_item(self, obj: Any, model: Any, item: Any, label: Any): ...
    def _check_list_display_links(self, obj: Any): ...
    def _check_list_display_links_item(self, obj: Any, field_name: Any, label: Any): ...
    def _check_list_filter(self, obj: Any): ...
    def _check_list_filter_item(self, obj: Any, model: Any, item: Any, label: Any): ...
    def _check_list_select_related(self, obj: Any): ...
    def _check_list_per_page(self, obj: Any): ...
    def _check_list_max_show_all(self, obj: Any): ...
    def _check_list_editable(self, obj: Any): ...
    def _check_list_editable_item(
        self, obj: Any, model: Any, field_name: Any, label: Any
    ): ...
    def _check_search_fields(self, obj: Any): ...
    def _check_date_hierarchy(self, obj: Any): ...
    def _check_action_permission_methods(self, obj: Any): ...

class InlineModelAdminChecks(BaseModelAdminChecks):
    def check(self, inline_obj: Any, **kwargs: Any): ...
    def _check_exclude_of_parent_model(
        self, obj: InlineModelAdmin, parent_model: Type[Model]
    ) -> List[Any]: ...
    def _check_relation(
        self, obj: InlineModelAdmin, parent_model: Type[Model]
    ) -> List[Any]: ...
    def _check_extra(self, obj: InlineModelAdmin) -> List[Any]: ...
    def _check_max_num(self, obj: InlineModelAdmin) -> List[Any]: ...
    def _check_min_num(self, obj: InlineModelAdmin) -> List[Any]: ...
    def _check_formset(self, obj: InlineModelAdmin) -> List[Any]: ...
    def _check_has_add_permission(self, obj: InlineModelAdmin) -> None: ...

def must_be(type: Any, option: Any, obj: Any, id: Any): ...
def must_inherit_from(parent: Any, option: Any, obj: Any, id: Any): ...
def refer_to_missing_field(field: Any, option: Any, model: Any, obj: Any, id: Any): ...
