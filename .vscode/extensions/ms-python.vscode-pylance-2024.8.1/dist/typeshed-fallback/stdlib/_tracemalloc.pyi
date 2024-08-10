import sys
from collections.abc import Sequence
from tracemalloc import _FrameTuple, _TraceTuple

def _get_object_traceback(obj: object, /) -> Sequence[_FrameTuple] | None: ...
def _get_traces() -> Sequence[_TraceTuple]: ...
def clear_traces() -> None: ...
def get_traceback_limit() -> int: ...
def get_traced_memory() -> tuple[int, int]: ...
def get_tracemalloc_memory() -> int: ...
def is_tracing() -> bool: ...

if sys.version_info >= (3, 9):
    def reset_peak() -> None: ...

def start(nframe: int = 1, /) -> None: ...
def stop() -> None: ...
