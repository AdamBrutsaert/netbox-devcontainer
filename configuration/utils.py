from os import environ
from os.path import abspath, dirname
from typing import Any, Callable


def read_secret(secret: str, default: str | None = None) -> str | None:
    try:
        f = open('/run/secrets/' + secret, 'r', encoding='utf-8')
    except EnvironmentError:
        return default
    else:
        with f:
            return f.read().strip()


def environ_get_and_map(key: str, default: str | None = None, mapper: Callable[[str], Any] | None = None) -> Any | None:
    value = environ.get(key, default)

    if not mapper:
        return value

    return mapper(value)


AS_BOOL = lambda value: value.lower() in ('true', '1', 'yes', 'y', 'on')
AS_INT = lambda value: int(value)
AS_LIST = lambda value: list(filter(None, value.split(',')))

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
