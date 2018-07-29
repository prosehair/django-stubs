from django.core.management.base import CommandParser
from typing import List, Tuple

def check_programs(*programs) -> None: ...
def normalize_eols(raw_contents: str) -> str: ...
def write_pot_file(potfile: str, msgs: str) -> None: ...

class BuildFile:
    def __init__(
        self, command: Command, domain: str, translatable: TranslatableFile
    ) -> None: ...
    def cleanup(self) -> None: ...
    @cached_property
    def is_templatized(self) -> bool: ...
    @cached_property
    def path(self) -> str: ...
    def postprocess_messages(self, msgs: str) -> str: ...
    def preprocess(self) -> None: ...
    @cached_property
    def work_path(self) -> str: ...

class Command:
    def add_arguments(self, parser: CommandParser) -> None: ...
    def build_potfiles(self) -> List[str]: ...
    def copy_plural_forms(self, msgs: str, locale: str) -> str: ...
    def find_files(self, root: str) -> List[TranslatableFile]: ...
    @cached_property
    def gettext_version(self) -> Tuple[int, int, int]: ...
    def handle(self, *args, **options) -> None: ...
    def process_files(self, file_list: List[TranslatableFile]) -> None: ...
    def process_locale_dir(
        self, locale_dir: str, files: List[TranslatableFile]
    ) -> None: ...
    def remove_potfiles(self) -> None: ...
    @cached_property
    def settings_available(self) -> bool: ...
    def write_po_file(self, potfile: str, locale: str) -> None: ...

class TranslatableFile:
    def __eq__(self, other: TranslatableFile) -> bool: ...
    def __init__(self, dirpath: str, file_name: str, locale_dir: object) -> None: ...
    def __lt__(self, other: TranslatableFile) -> bool: ...
    @property
    def path(self) -> str: ...
