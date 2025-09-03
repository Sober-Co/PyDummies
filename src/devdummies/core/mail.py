from __future__ import annotations
from typing import Protocol, TypedDict

class MailMessage(TypedDict):
    id: str
    to: str
    subject: str
    body: str
    from_: str | None

class Mailer(Protocol):
    def send(self, *, to: str, subject: str, body: str, from_: str | None = None) -> str: ...
