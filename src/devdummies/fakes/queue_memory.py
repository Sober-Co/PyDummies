from __future__ import annotations
from typing import Any
from ..core.storage import Queue

class InMemoryQueue(Queue):
    """[Fake] FIFO queue backed by a Python list."""
    def __init__(self) -> None:
        self._q: list[Any] = []

    def push(self, item: Any) -> None:
        self._q.append(item)

    def pop(self) -> Any | None:
        if not self._q:
            return None
        return self._q.pop(0)

    def size(self) -> int:
        return len(self._q)

    def clear(self) -> None:
        self._q.clear()

    def snapshot(self) -> list[Any]:
        return list(self._q)
