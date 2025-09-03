from __future__ import annotations
from tempfile import TemporaryDirectory
from devdummies.emulators.s3_like import S3Like

def test_s3_like_put_get_list_delete():
    with TemporaryDirectory() as d:
        s3 = S3Like(d)
        meta = s3.put_object("bkt", "a/b.txt", b"hello")
        assert meta["ContentLength"] == 5
        assert s3.get_object("bkt", "a/b.txt") == b"hello"
        assert "a/b.txt" in s3.list_objects("bkt", prefix="a/")
        s3.delete_object("bkt", "a/b.txt")
        assert "a/b.txt" not in s3.list_objects("bkt")
