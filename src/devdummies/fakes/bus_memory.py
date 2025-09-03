from __future__ import annotations
from typing import Any
from ..core.bus import MessageBus, Handler

class InMemoryBus(MessageBus):
    """[Fake] Simple pub/sub message bus."""
    def __init__(self) -> None:
        self._subs: dict[str, list[Handler]] = {}
        self._published: list[tuple[str, Any]] = []

    def publish(self, topic: str, message: Any) -> None:
        self._published.append((topic, message))
        for h in self._subs.get(topic, []):
            h(topic, message)

    def subscribe(self, topic: str, handler: Handler) -> None:
        self._subs.setdefault(topic, []).append(handler)

    # observability
    def snapshot(self) -> dict[str, list]:
        return {"published": list(self._published), "subscriptions": {k: len(v) for k, v in self._subs.items()}}
