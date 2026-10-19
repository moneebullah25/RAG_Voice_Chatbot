import os
import tempfile
import pytest
from safe_paths import resolve_in_upload_dir


def test_resolve_in_upload_dir():
    with tempfile.TemporaryDirectory() as d:
        base = os.path.realpath(d)
        assert resolve_in_upload_dir('a.pdf', base) == os.path.join(base, 'a.pdf')
        assert resolve_in_upload_dir('sub/a.wav', base) == os.path.join(base, 'sub', 'a.wav')
        for bad in ['../x.pdf', '/etc/passwd', 'sub/../../x', '', None, 5, 'a\0b']:
            with pytest.raises(ValueError):
                resolve_in_upload_dir(bad, base)
