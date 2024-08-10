from _typeshed import Incomplete, StrPath
from abc import ABCMeta, abstractmethod
from collections.abc import MutableMapping
from typing import ClassVar, Literal, TypeVar

from .pytree import Base, Leaf, Node

_N = TypeVar("_N", bound=Base)

class BaseFix:
    PATTERN: ClassVar[str | None]
    pattern: Incomplete | None
    pattern_tree: Incomplete | None
    options: Incomplete | None
    filename: Incomplete | None
    numbers: Incomplete
    used_names: Incomplete
    order: ClassVar[Literal["post", "pre"]]
    explicit: ClassVar[bool]
    run_order: ClassVar[int]
    keep_line_order: ClassVar[bool]
    BM_compatible: ClassVar[bool]
    syms: Incomplete
    log: Incomplete
    def __init__(self, options: MutableMapping[str, Incomplete], log: list[str]) -> None: ...
    def compile_pattern(self) -> None: ...
    def set_filename(self, filename: StrPath) -> None: ...
    def match(self, node: _N) -> Literal[False] | dict[str, _N]: ...
    @abstractmethod
    def transform(self, node: Base, results: dict[str, Base]) -> Node | Leaf | None: ...
    def new_name(self, template: str = "xxx_todo_changeme") -> str: ...
    first_log: bool
    def log_message(self, message: str) -> None: ...
    def cannot_convert(self, node: Base, reason: str | None = None) -> None: ...
    def warning(self, node: Base, reason: str) -> None: ...
    def start_tree(self, tree: Node, filename: StrPath) -> None: ...
    def finish_tree(self, tree: Node, filename: StrPath) -> None: ...

class ConditionalFix(BaseFix, metaclass=ABCMeta):
    skip_on: ClassVar[str | None]
    def start_tree(self, tree: Node, filename: StrPath, /) -> None: ...
    def should_skip(self, node: Base) -> bool: ...
