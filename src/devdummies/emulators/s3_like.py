from __future__ import annotations
from pathlib import Path
import hashlib

class S3Like:
    """[Emulator] Very small S3-like interface on local filesystem.

    Buckets are directories under `root`, objects are files.
    """
    def __init__(self, root: str):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _bucket(self, bucket: str) -> Path:
        b = self.root / bucket
        b.mkdir(parents=True, exist_ok=True)
        return b

    def put_object(self, bucket: str, key: str, data: bytes) -> dict:
        b = self._bucket(bucket)
        obj = b / key
        obj.parent.mkdir(parents=True, exist_ok=True)
        obj.write_bytes(data)
        etag = hashlib.md5(data, usedforsecurity=False).hexdigest()
        return {"ETag": etag, "ContentLength": len(data)}

    def get_object(self, bucket: str, key: str) -> bytes:
        return (self._bucket(bucket) / key).read_bytes()

    def list_objects(self, bucket: str, prefix: str = "") -> list[str]:
        base = self._bucket(bucket)
        return [str(p.relative_to(base)).replace("\\", "/")
                for p in base.rglob("*")
                if p.is_file() and str(p.relative_to(base)).replace("\\", "/").startswith(prefix)]

    def delete_object(self, bucket: str, key: str) -> None:
        (self._bucket(bucket) / key).unlink(missing_ok=True)
