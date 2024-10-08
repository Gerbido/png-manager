from collections.abc import Callable, Collection
from decimal import Decimal
from re import Pattern, RegexFlag
from typing import Any

from django.core.files.base import File

EMPTY_VALUES: Any

_Regex = str | Pattern[str]
_ErrorMessage = str | Any

def _lazy_re_compile(regex: _Regex, flags: int = ...) -> Any: ...

class RegexValidator:
    regex: _Regex = ...
    message: str = ...
    code: str = ...
    inverse_match: bool = ...
    flags: int = ...
    def __init__(
        self,
        regex: _Regex | None = ...,
        message: _ErrorMessage | None = ...,
        code: str | None = ...,
        inverse_match: bool | None = ...,
        flags: RegexFlag | None = ...,
    ) -> None: ...
    def __call__(self, value: str | None) -> None: ...

class URLValidator(RegexValidator):
    ul: str = ...
    ipv4_re: str = ...
    ipv6_re: str = ...
    hostname_re: str = ...
    domain_re: str = ...
    tld_re: str = ...
    host_re: str = ...
    schemes: list[str] = ...
    def __init__(
        self, schemes: Collection[str] | None = ..., **kwargs: Any
    ) -> None: ...

integer_validator: RegexValidator = ...

def validate_integer(value: float | str | None) -> None: ...

class EmailValidator:
    message: str = ...
    code: str = ...
    user_regex: Pattern[str] = ...
    domain_regex: Pattern[str] = ...
    literal_regex: Pattern[str] = ...
    domain_whitelist: list[str] = ...
    def __init__(
        self,
        message: _ErrorMessage | None = ...,
        code: str | None = ...,
        whitelist: Collection[str] | None = ...,
    ) -> None: ...
    def __call__(self, value: str | None) -> None: ...
    def validate_domain_part(self, domain_part: str) -> bool: ...

validate_email: EmailValidator = ...
slug_re: Pattern[str] = ...
validate_slug: RegexValidator = ...
slug_unicode_re: Pattern[str] = ...
validate_unicode_slug: RegexValidator = ...

def validate_ipv4_address(value: str) -> None: ...
def validate_ipv6_address(value: str) -> None: ...
def validate_ipv46_address(value: str) -> None: ...

_IPValidator = tuple[Callable[[Any], None], str]
ip_address_validator_map: dict[str, _IPValidator]

def ip_address_validators(protocol: str, unpack_ipv4: bool) -> _IPValidator: ...
def int_list_validator(
    sep: str = ...,
    message: _ErrorMessage | None = ...,
    code: str = ...,
    allow_negative: bool = ...,
) -> RegexValidator: ...

validate_comma_separated_integer_list: Any

class BaseValidator:
    message: str = ...
    code: str = ...
    limit_value: Any = ...
    def __init__(
        self, limit_value: Any, message: _ErrorMessage | None = ...
    ) -> None: ...
    def __call__(self, value: Any) -> None: ...
    def compare(self, a: Any, b: Any) -> bool: ...
    def clean(self, x: Any) -> Any: ...

class MaxValueValidator(BaseValidator): ...
class MinValueValidator(BaseValidator): ...
class MinLengthValidator(BaseValidator): ...
class MaxLengthValidator(BaseValidator): ...

class DecimalValidator:
    messages: dict[str, str] = ...
    max_digits: int = ...
    decimal_places: int = ...
    def __init__(
        self,
        max_digits: int | str | None,
        decimal_places: int | str | None,
    ) -> None: ...
    def __call__(self, value: Decimal) -> None: ...

class FileExtensionValidator:
    message: str = ...
    code: str = ...
    allowed_extensions: list[str] = ...
    def __init__(
        self,
        allowed_extensions: Collection[str] | None = ...,
        message: _ErrorMessage | None = ...,
        code: str | None = ...,
    ) -> None: ...
    def __call__(self, value: File) -> None: ...

def get_available_image_extensions() -> list[str]: ...
def validate_image_file_extension(value: File) -> None: ...

class ProhibitNullCharactersValidator:
    message: str = ...
    code: str = ...
    def __init__(
        self, message: _ErrorMessage | None = ..., code: str | None = ...
    ) -> None: ...
    def __call__(self, value: Any) -> None: ...
