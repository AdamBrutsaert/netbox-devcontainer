from .utils import environ_get_and_map, AS_BOOL

DEBUG = environ_get_and_map("DEBUG", "False", AS_BOOL)
DEVELOPER = environ_get_and_map("DEVELOPER", "False", AS_BOOL)
