from __future__ import annotations
from typing import Protocol, TypedDict

class SMSMessage(TypedDict):
    id: str
    to: str
    body: str
    sender: str | None

class SMS(Protocol):
    def send(self, *, to: str, body: str, sender: str | None = None) -> str: ...
