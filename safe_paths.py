import os

UPLOAD_DIR = os.path.realpath(os.environ.get('UPLOAD_DIR', os.path.join(os.getcwd(), 'uploads')))


def resolve_in_upload_dir(path, base=None):
    """Return the real path of `path` if it lies inside the upload dir, else raise ValueError."""
    base = os.path.realpath(base or UPLOAD_DIR)
    if not isinstance(path, str) or not path or '\0' in path:
        raise ValueError('invalid path')
    full = os.path.realpath(os.path.join(base, path))
    if os.path.commonpath([base, full]) != base:
        raise ValueError('path outside upload directory')
    return full
