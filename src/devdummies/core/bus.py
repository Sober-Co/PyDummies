from __future__ import annotations
from typing import Protocol, Callable, Any

Handler = Callable[[str, Any], None]

class MessageBus(Protocol):
    def publish(self, topic: str, message: Any) -> None: ...
    def subscribe(self, topic: str, handler: Handler) -> None: ...

class EventBus(MessageBus, Protocol):
    pass
