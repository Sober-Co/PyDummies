from __future__ import annotations
import itertools

class IdFactory:
    """[Determinism] Monotonic ID generator with optional prefix."""
    def __init__(self, prefix: str = "id_", start: int = 1) -> None:
        self._c = itertools.count(start)
        self.prefix = prefix

    def next(self) -> str:
        return f"{self.prefix}{next(self._c)}"
