from django.core.management.base import CommandParser

class Command:
    def add_arguments(self, parser: CommandParser) -> None: ...
