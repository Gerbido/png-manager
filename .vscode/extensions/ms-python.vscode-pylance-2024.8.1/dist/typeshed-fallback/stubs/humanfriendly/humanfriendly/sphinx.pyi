from typing import Any

logger: Any

def deprecation_note_callback(app, what, name, obj, options, lines) -> None: ...
def enable_deprecation_notes(app) -> None: ...
def enable_man_role(app) -> None: ...
def enable_pypi_role(app) -> None: ...
def enable_special_methods(app) -> None: ...
def enable_usage_formatting(app) -> None: ...
def man_role(role, rawtext, text, lineno, inliner, options={}, content=[]): ...
def pypi_role(role, rawtext, text, lineno, inliner, options={}, content=[]): ...
def setup(app): ...
def special_methods_callback(app, what, name, obj, skip, options): ...
def usage_message_callback(app, what, name, obj, options, lines) -> None: ...
