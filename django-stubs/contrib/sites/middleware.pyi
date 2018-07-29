# Stubs for django.contrib.sites.middleware (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .shortcuts import get_current_site
from django.utils.deprecation import MiddlewareMixin
from typing import Any

from django.http.request import HttpRequest

class CurrentSiteMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest) -> None: ...
