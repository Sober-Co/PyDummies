from __future__ import annotations
from typing import Protocol
from datetime import datetime, timedelta, timezone


_DEFAULT_FAKE_CLOCK_START = datetime(2000, 1, 1, tzinfo=timezone.utc)

class Clock(Protocol):
    def now(self) -> datetime: ...
    def sleep(self, delta: timedelta) -> None: ...

class FakeClock:
    """[Test Double: Fake] Deterministic clock you can advance manually.

    When ``start`` is omitted the clock begins at a fixed UTC timestamp so that
    repeated instantiations remain deterministic.
    """

    def __init__(self, start: datetime | None = None) -> None:
        self._t = (start or _DEFAULT_FAKE_CLOCK_START).astimezone(timezone.utc)

    def now(self) -> datetime:
        return self._t

    def sleep(self, delta: timedelta) -> None:
        self._t += delta

    def set(self, t: datetime) -> None:
        self._t = t.astimezone(timezone.utc)
