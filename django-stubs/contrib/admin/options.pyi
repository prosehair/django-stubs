# Stubs for django.contrib.admin.options (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.core.checks.messages import Error
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.base import Model
from django.db.models.fields import Field
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.query import QuerySet
from django.forms.fields import Field, TypedChoiceField
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.utils.safestring import SafeText
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

IS_POPUP_VAR: str
TO_FIELD_VAR: str
HORIZONTAL: Any
VERTICAL: Any

def get_content_type_for_model(obj: Any): ...
def get_ul_class(radio_style: Any): ...

class IncorrectLookupParameters(Exception): ...

FORMFIELD_FOR_DBFIELD_DEFAULTS: Any
csrf_protect_m: Any

class BaseModelAdmin:
    autocomplete_fields: Any = ...
    raw_id_fields: Any = ...
    fields: Any = ...
    exclude: Any = ...
    fieldsets: Any = ...
    form: Any = ...
    filter_vertical: Any = ...
    filter_horizontal: Any = ...
    radio_fields: Any = ...
    prepopulated_fields: Any = ...
    formfield_overrides: Any = ...
    readonly_fields: Any = ...
    ordering: Any = ...
    sortable_by: Any = ...
    view_on_site: bool = ...
    show_full_result_count: bool = ...
    checks_class: Any = ...
    def check(self, **kwargs: Any) -> List[Error]: ...
    def __init__(self) -> None: ...
    def formfield_for_dbfield(
        self, db_field: Field, request: object, **kwargs: Any
    ) -> Optional[Field]: ...
    def formfield_for_choice_field(
        self, db_field: Field, request: object, **kwargs: Any
    ) -> TypedChoiceField: ...
    def get_field_queryset(
        self, db: None, db_field: Union[ManyToManyField, ForeignKey], request: object
    ) -> Optional[QuerySet]: ...
    def formfield_for_foreignkey(
        self, db_field: ForeignKey, request: object, **kwargs: Any
    ) -> Optional[ModelChoiceField]: ...
    def formfield_for_manytomany(
        self, db_field: ManyToManyField, request: WSGIRequest, **kwargs: Any
    ) -> ModelMultipleChoiceField: ...
    def get_autocomplete_fields(self, request: object) -> Tuple: ...
    def get_view_on_site_url(self, obj: Optional[Model] = ...) -> Optional[str]: ...
    def get_empty_value_display(self) -> SafeText: ...
    def get_exclude(self, request: object, obj: Optional[Model] = ...) -> None: ...
    def get_fields(
        self, request: object, obj: Optional[Model] = ...
    ) -> Union[List[str], List[Union[str, Callable]]]: ...
    def get_fieldsets(self, request: WSGIRequest, obj: Optional[Model] = ...) -> Any: ...
    def get_ordering(self, request: WSGIRequest) -> Union[List[str], Tuple]: ...
    def get_readonly_fields(
        self, request: object, obj: Optional[Model] = ...
    ) -> Union[List[str], Tuple]: ...
    def get_prepopulated_fields(
        self, request: WSGIRequest, obj: Optional[Model] = ...
    ) -> Dict[str, Tuple[str]]: ...
    def get_queryset(self, request: object) -> QuerySet: ...
    def get_sortable_by(self, request: WSGIRequest) -> Union[List[str], Tuple]: ...
    def lookup_allowed(self, lookup: Any, value: Any): ...
    def to_field_allowed(self, request: Any, to_field: Any): ...
    def has_add_permission(self, request: WSGIRequest) -> bool: ...
    def has_change_permission(
        self, request: object, obj: Optional[Model] = ...
    ) -> bool: ...
    def has_delete_permission(
        self, request: object, obj: Optional[Model] = ...
    ) -> bool: ...
    def has_view_permission(
        self, request: WSGIRequest, obj: Optional[Model] = ...
    ) -> bool: ...
    def has_module_permission(self, request: object) -> bool: ...

class ModelAdmin(BaseModelAdmin):
    list_display: Any = ...
    list_display_links: Any = ...
    list_filter: Any = ...
    list_select_related: bool = ...
    list_per_page: int = ...
    list_max_show_all: int = ...
    list_editable: Any = ...
    search_fields: Any = ...
    date_hierarchy: Any = ...
    save_as: bool = ...
    save_as_continue: bool = ...
    save_on_top: bool = ...
    paginator: Any = ...
    preserve_filters: bool = ...
    inlines: Any = ...
    add_form_template: Any = ...
    change_form_template: Any = ...
    change_list_template: Any = ...
    delete_confirmation_template: Any = ...
    delete_selected_confirmation_template: Any = ...
    object_history_template: Any = ...
    popup_response_template: Any = ...
    actions: Any = ...
    action_form: Any = ...
    actions_on_top: bool = ...
    actions_on_bottom: bool = ...
    actions_selection_counter: bool = ...
    checks_class: Any = ...
    model: Any = ...
    opts: Any = ...
    admin_site: Any = ...
    def __init__(self, model: Any, admin_site: Any) -> None: ...
    def __str__(self): ...
    def get_inline_instances(self, request: Any, obj: Optional[Any] = ...): ...
    def get_urls(self): ...
    @property
    def urls(self): ...
    @property
    def media(self): ...
    def get_model_perms(self, request: Any): ...
    def _get_form_for_get_fields(self, request: Any, obj: Any): ...
    def get_form(
        self, request: Any, obj: Optional[Any] = ..., change: bool = ..., **kwargs: Any
    ): ...
    def get_changelist(self, request: Any, **kwargs: Any): ...
    def get_changelist_instance(self, request: Any): ...
    def get_object(self, request: Any, object_id: Any, from_field: Optional[Any] = ...): ...
    def get_changelist_form(self, request: Any, **kwargs: Any): ...
    def get_changelist_formset(self, request: Any, **kwargs: Any): ...
    def get_formsets_with_inlines(self, request: Any, obj: Optional[Any] = ...) -> None: ...
    def get_paginator(
        self,
        request: Any,
        queryset: Any,
        per_page: Any,
        orphans: int = ...,
        allow_empty_first_page: bool = ...,
    ): ...
    def log_addition(self, request: Any, object: Any, message: Any): ...
    def log_change(self, request: Any, object: Any, message: Any): ...
    def log_deletion(self, request: Any, object: Any, object_repr: Any): ...
    def action_checkbox(self, obj: Any): ...
    def _get_base_actions(self): ...
    def _filter_actions_by_permissions(self, request: Any, actions: Any): ...
    def get_actions(self, request: Any): ...
    def get_action_choices(self, request: Any, default_choices: Any = ...): ...
    def get_action(self, action: Any): ...
    def get_list_display(self, request: Any): ...
    def get_list_display_links(self, request: Any, list_display: Any): ...
    def get_list_filter(self, request: Any): ...
    def get_list_select_related(self, request: Any): ...
    def get_search_fields(self, request: Any): ...
    def get_search_results(self, request: Any, queryset: Any, search_term: Any): ...
    def get_preserved_filters(self, request: Any): ...
    def construct_change_message(
        self, request: Any, form: Any, formsets: Any, add: bool = ...
    ): ...
    def message_user(
        self,
        request: Any,
        message: Any,
        level: Any = ...,
        extra_tags: str = ...,
        fail_silently: bool = ...,
    ) -> None: ...
    def save_form(self, request: Any, form: Any, change: Any): ...
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None: ...
    def delete_model(self, request: Any, obj: Any) -> None: ...
    def delete_queryset(self, request: Any, queryset: Any) -> None: ...
    def save_formset(self, request: Any, form: Any, formset: Any, change: Any) -> None: ...
    def save_related(self, request: Any, form: Any, formsets: Any, change: Any) -> None: ...
    def render_change_form(
        self,
        request: Any,
        context: Any,
        add: bool = ...,
        change: bool = ...,
        form_url: str = ...,
        obj: Optional[Any] = ...,
    ): ...
    def response_add(
        self, request: Any, obj: Any, post_url_continue: Optional[Any] = ...
    ): ...
    def response_change(self, request: Any, obj: Any): ...
    def response_post_save_add(self, request: Any, obj: Any): ...
    def response_post_save_change(self, request: Any, obj: Any): ...
    def response_action(self, request: Any, queryset: Any): ...
    def response_delete(self, request: Any, obj_display: Any, obj_id: Any): ...
    def render_delete_form(self, request: Any, context: Any): ...
    def get_inline_formsets(
        self, request: Any, formsets: Any, inline_instances: Any, obj: Optional[Any] = ...
    ): ...
    def get_changeform_initial_data(self, request: Any): ...
    def _get_obj_does_not_exist_redirect(self, request: Any, opts: Any, object_id: Any): ...
    def changeform_view(
        self,
        request: Any,
        object_id: Optional[Any] = ...,
        form_url: str = ...,
        extra_context: Optional[Any] = ...,
    ): ...
    def _changeform_view(
        self, request: Any, object_id: Any, form_url: Any, extra_context: Any
    ): ...
    def autocomplete_view(self, request: Any): ...
    def add_view(
        self, request: Any, form_url: str = ..., extra_context: Optional[Any] = ...
    ): ...
    def change_view(
        self,
        request: Any,
        object_id: Any,
        form_url: str = ...,
        extra_context: Optional[Any] = ...,
    ): ...
    def _get_edited_object_pks(self, request: Any, prefix: Any): ...
    def _get_list_editable_queryset(self, request: Any, prefix: Any): ...
    def changelist_view(self, request: Any, extra_context: Optional[Any] = ...): ...
    def get_deleted_objects(self, objs: Any, request: Any): ...
    def delete_view(
        self, request: Any, object_id: Any, extra_context: Optional[Any] = ...
    ): ...
    def _delete_view(self, request: Any, object_id: Any, extra_context: Any): ...
    def history_view(
        self, request: Any, object_id: Any, extra_context: Optional[Any] = ...
    ): ...
    def _create_formsets(self, request: Any, obj: Any, change: Any): ...

class InlineModelAdmin(BaseModelAdmin):
    model: Any = ...
    fk_name: Any = ...
    formset: Any = ...
    extra: int = ...
    min_num: Any = ...
    max_num: Any = ...
    template: Any = ...
    verbose_name: Any = ...
    verbose_name_plural: Any = ...
    can_delete: bool = ...
    show_change_link: bool = ...
    checks_class: Any = ...
    classes: Any = ...
    admin_site: Any = ...
    parent_model: Any = ...
    opts: Any = ...
    has_registered_model: Any = ...
    def __init__(self, parent_model: Any, admin_site: Any) -> None: ...
    @property
    def media(self): ...
    def get_extra(self, request: Any, obj: Optional[Any] = ..., **kwargs: Any): ...
    def get_min_num(self, request: Any, obj: Optional[Any] = ..., **kwargs: Any): ...
    def get_max_num(self, request: Any, obj: Optional[Any] = ..., **kwargs: Any): ...
    fields: Any = ...
    def get_formset(self, request: Any, obj: Optional[Any] = ..., **kwargs: Any): ...
    def _get_form_for_get_fields(self, request: Any, obj: Optional[Any] = ...): ...
    def get_queryset(self, request: Any): ...
    def has_add_permission(self, request: Any, obj: Any): ...
    def has_change_permission(self, request: Any, obj: Optional[Any] = ...): ...
    def has_delete_permission(self, request: Any, obj: Optional[Any] = ...): ...
    def has_view_permission(self, request: Any, obj: Optional[Any] = ...): ...

class StackedInline(InlineModelAdmin):
    template: str = ...

class TabularInline(InlineModelAdmin):
    template: str = ...
