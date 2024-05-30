from os import environ
from typing import Any, Callable


def environ_get_and_map(key: str, default: str | None = None, mapper: Callable[[str], Any] | None = None) -> Any | None:
    value = environ.get(key, default)

    if not mapper:
        return value

    return mapper(value)


AS_BOOL = lambda value: value.lower() in ('true', '1', 'yes', 'y', 'on')
AS_INT = lambda value: int(value)
AS_LIST = lambda value: list(filter(None, value.split(',')))
