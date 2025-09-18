from __future__ import annotations
from pathlib import Path
from ..core.storage import BlobStorage

class FSBlobStorage(BlobStorage):
    """[Fake/Emulator] Blob storage backed by local filesystem root."""
    def __init__(self, root: str) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str, *, create_parent: bool = False) -> Path:
        p = self.root / key
        if create_parent:
            p.parent.mkdir(parents=True, exist_ok=True)
        return p

    def put(self, key: str, data: bytes) -> None:
        self._path(key, create_parent=True).write_bytes(data)

    def get(self, key: str) -> bytes:
        return self._path(key).read_bytes()

    def delete(self, key: str) -> None:
        self._path(key).unlink(missing_ok=True)

    def exists(self, key: str) -> bool:
        return self._path(key).exists()

    def list(self, prefix: str = "") -> list[str]:
        out: list[str] = []
        for p in self.root.rglob("*"):
            if p.is_file():
                rel = p.relative_to(self.root).as_posix()
                if rel.startswith(prefix):
                    out.append(rel)
        out.sort()
        return out
