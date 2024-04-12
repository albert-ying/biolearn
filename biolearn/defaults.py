import appdirs
from biolearn.cache import LocalFolderCache


def default_cache():
    app_name = "biolearn"
    cache_path = appdirs.user_cache_dir(app_name)
    return LocalFolderCache(cache_path, 50)
