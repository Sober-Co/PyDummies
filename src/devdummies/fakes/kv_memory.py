from __future__ import annotations
from typing import Any
from ..core.storage import KeyValue

class InMemoryKV(KeyValue):
    """[Fake] Simple in-memory key-value store."""
    def __init__(self) -> None:
        self._store: dict[str, Any] = {}

    def get(self, key: str, default: Any | None = None) -> Any | None:
        return self._store.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._store[key] = value

    def delete(self, key: str) -> None:
        self._store.pop(key, None)

    def keys(self, prefix: str = "") -> list[str]:
        return [k for k in self._store if k.startswith(prefix)]

    # observability
    def snapshot(self) -> dict[str, Any]:
        return dict(self._store)

    def clear(self) -> None:
        self._store.clear()
