from __future__ import annotations
from ..core.featureflags import FeatureFlags

class InMemoryFlags(FeatureFlags):
    """[Fake] Feature flags stored in memory."""
    def __init__(self) -> None:
        self._flags: dict[str, bool] = {}

    def is_enabled(self, name: str) -> bool:
        return self._flags.get(name, False)

    def set(self, name: str, value: bool) -> None:
        self._flags[name] = value

    def all(self) -> dict[str, bool]:
        return dict(self._flags)
