from __future__ import annotations
from typing import Protocol
from datetime import datetime, timedelta, timezone

class Clock(Protocol):
    def now(self) -> datetime: ...
    def sleep(self, delta: timedelta) -> None: ...

class FakeClock:
    """[Test Double: Fake] Deterministic clock you can advance manually."""
    def __init__(self, start: datetime | None = None) -> None:
        self._t = (start or datetime.now(timezone.utc)).astimezone(timezone.utc)

    def now(self) -> datetime:
        return self._t

    def sleep(self, delta: timedelta) -> None:
        self._t += delta

    def set(self, t: datetime) -> None:
        self._t = t.astimezone(timezone.utc)
