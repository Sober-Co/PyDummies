from __future__ import annotations

from tempfile import TemporaryDirectory

from devdummies.fakes.blob_fs import FSBlobStorage


def test_fs_blob_storage_roundtrip_and_listing() -> None:
    with TemporaryDirectory() as tmp:
        storage = FSBlobStorage(tmp)

        storage.put("docs/a.txt", b"hello")
        storage.put("docs/b.txt", b"world")
        storage.put("logs/a.txt", b"log")

        assert storage.exists("docs/a.txt")
        assert storage.get("docs/a.txt") == b"hello"

        listed = storage.list(prefix="docs/")
        assert listed == ["docs/a.txt", "docs/b.txt"]

        storage.delete("docs/a.txt")
        assert not storage.exists("docs/a.txt")

        # Ensure we didn't create any directories on reads
        assert not (storage.root / "missing").exists()
