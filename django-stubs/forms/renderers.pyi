# Stubs for django.forms.renderers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.template.backends.django import DjangoTemplates, Template
from typing import Any, Dict

ROOT: Any

def get_default_renderer() -> DjangoTemplates: ...

class BaseRenderer:
    def get_template(self, template_name: Any) -> None: ...
    def render(
        self, template_name: str, context: Dict[str, Any], request: None = ...
    ) -> str: ...

class EngineMixin:
    def get_template(self, template_name: str) -> Template: ...
    def engine(self) -> DjangoTemplates: ...

class DjangoTemplates(EngineMixin, BaseRenderer):
    backend: Any = ...

class Jinja2(EngineMixin, BaseRenderer):
    backend: Any = ...

class TemplatesSetting(BaseRenderer):
    def get_template(self, template_name: Any): ...
