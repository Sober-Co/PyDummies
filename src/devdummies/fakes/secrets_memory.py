from __future__ import annotations
from ..core.secrets import SecretsVault

class InMemorySecrets(SecretsVault):
    """[Fake] In-memory secret vault."""
    def __init__(self) -> None:
        self._data: dict[str, str] = {}

    def put(self, name: str, value: str) -> None:
        self._data[name] = value

    def get(self, name: str) -> str | None:
        return self._data.get(name)

    def delete(self, name: str) -> None:
        self._data.pop(name, None)

    def list(self, prefix: str = "") -> list[str]:
        return [k for k in self._data if k.startswith(prefix)]
