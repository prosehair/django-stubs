# Stubs for django.template.backends.dummy (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import string
from .base import BaseEngine
from .utils import csrf_input_lazy, csrf_token_lazy
from typing import Any, Optional

from django.http.request import HttpRequest
from typing import Dict, Optional, Union

class TemplateStrings(BaseEngine):
    app_dirname: str = ...
    def __init__(self, params: Dict[str, Union[bool, str]]) -> None: ...
    def from_string(self, template_code: Any): ...
    def get_template(self, template_name: str) -> Template: ...

class Template(string.Template):
    def render(
        self, context: Optional[Dict[str, str]] = ..., request: Optional[HttpRequest] = ...
    ) -> str: ...
