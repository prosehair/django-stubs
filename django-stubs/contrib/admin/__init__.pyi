# Stubs for django.contrib.admin (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.contrib.admin.decorators import register as register
from django.contrib.admin.filters import (
    AllValuesFieldListFilter as AllValuesFieldListFilter,
    BooleanFieldListFilter as BooleanFieldListFilter,
    ChoicesFieldListFilter as ChoicesFieldListFilter,
    DateFieldListFilter as DateFieldListFilter,
    FieldListFilter as FieldListFilter,
    ListFilter as ListFilter,
    RelatedFieldListFilter as RelatedFieldListFilter,
    RelatedOnlyFieldListFilter as RelatedOnlyFieldListFilter,
    SimpleListFilter as SimpleListFilter,
)
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME as ACTION_CHECKBOX_NAME
from django.contrib.admin.options import (
    HORIZONTAL as HORIZONTAL,
    ModelAdmin as ModelAdmin,
    StackedInline as StackedInline,
    TabularInline as TabularInline,
    VERTICAL as VERTICAL,
)
from django.contrib.admin.sites import AdminSite as AdminSite, site as site

def autodiscover() -> None: ...
