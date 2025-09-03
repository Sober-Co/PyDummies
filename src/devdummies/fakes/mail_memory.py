from __future__ import annotations
from ..core.mail import Mailer, MailMessage
from ..core.ids import IdFactory

class InMemoryMailer(Mailer):
    """[Fake] Captures emails in memory for assertions."""
    def __init__(self, id_factory: IdFactory | None = None) -> None:
        self._ids = id_factory or IdFactory("mail_")
        self.outbox: list[MailMessage] = []

    def send(self, *, to: str, subject: str, body: str, from_: str | None = None) -> str:
        mid = self._ids.next()
        self.outbox.append(MailMessage(id=mid, to=to, subject=subject, body=body, from_=from_))
        return mid
