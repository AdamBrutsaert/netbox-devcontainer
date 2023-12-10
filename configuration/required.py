from os import environ
from .utils import read_secret, environ_get_and_map, AS_INT, AS_BOOL, AS_LIST, BASE_DIR

ALLOWED_HOSTS = environ_get_and_map("ALLOWED_HOSTS", "*", AS_LIST)
if '*' not in ALLOWED_HOSTS and 'localhost' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append('localhost')

DATABASE = {
    'NAME': environ.get('POSTGRES_DB', 'netbox'),
    'USER': environ.get('POSTGRES_USER', ''),
    'PASSWORD': read_secret('postgres_password', environ.get('POSTGRES_PASSWORD', '')),
    'HOST': environ.get('POSTGRES_HOST', 'localhost'),
    'PORT': environ_get_and_map('POSTGRES_PORT', '5432', AS_INT),
    'OPTIONS': { 'sslmode': environ.get('POSTGRES_SSLMODE', 'prefer') },
    'CONN_MAX_AGE': environ_get_and_map('POSTGRES_CONN_MAX_AGE', '300', AS_INT),
    'DISABLE_SERVER_SIDE_CURSORS': environ_get_and_map('POSTGRES_DISABLE_SERVER_SIDE_CURSORS', 'False', AS_BOOL),
}

REDIS = {
    'tasks': {
        'HOST': environ.get('REDIS_HOST', 'localhost'),
        'PORT': environ_get_and_map('REDIS_PORT', '6379', AS_INT),
        'PASSWORD': read_secret('redis_password', environ.get('REDIS_PASSWORD', '')),
        'DATABASE': environ_get_and_map('REDIS_DATABASE', '0', AS_INT),
        'SSL': environ_get_and_map('REDIS_SSL', 'False', AS_BOOL),
        'INSECURE_SKIP_TLS_VERIFY': environ_get_and_map('REDIS_INSECURE_SKIP_TLS_VERIFY', 'False', AS_BOOL),
    },
    'caching': {
        'HOST': environ.get('REDIS_CACHE_HOST', 'localhost'),
        'PORT': environ_get_and_map('REDIS_CACHE_PORT', '6379', AS_INT),
        'PASSWORD': read_secret('redis_cache_password', environ.get('REDIS_CACHE_PASSWORD', '')),
        'DATABASE': environ_get_and_map('REDIS_CACHE_DATABASE', '0', AS_INT),
        'SSL': environ_get_and_map('REDIS_CACHE_SSL', 'False', AS_BOOL),
        'INSECURE_SKIP_TLS_VERIFY': environ_get_and_map('REDIS_CACHE_INSECURE_SKIP_TLS_VERIFY', 'False', AS_BOOL),
    },
}

SECRET_KEY = read_secret('secret_key', environ.get('SECRET_KEY', ''))

CHANGELOG_RETENTION = 1800
