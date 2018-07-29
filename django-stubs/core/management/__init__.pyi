# Stubs for django.core.management (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.core.management.base import BaseCommand
from typing import Dict, List, Optional, Union

def find_commands(management_dir: str) -> List[str]: ...
def load_command_class(app_name: str, name: str) -> BaseCommand: ...
def get_commands() -> Dict[str, str]: ...
def call_command(
    command_name: Union[str, BaseCommand], *args: Any, **options: Any
) -> Optional[str]: ...

class ManagementUtility:
    argv: Any = ...
    prog_name: Any = ...
    settings_exception: Any = ...
    def __init__(self, argv: List[str] = ...) -> None: ...
    def main_help_text(self, commands_only: bool = ...): ...
    def fetch_command(self, subcommand: str) -> BaseCommand: ...
    def autocomplete(self): ...
    def execute(self) -> None: ...

def execute_from_command_line(argv: Optional[Any] = ...) -> None: ...
