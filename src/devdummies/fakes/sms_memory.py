from __future__ import annotations
from ..core.sms import SMS, SMSMessage
from ..core.ids import IdFactory

class InMemorySMS(SMS):
    """[Fake] Captures SMS in memory."""
    def __init__(self, id_factory: IdFactory | None = None) -> None:
        self._ids = id_factory or IdFactory("sms_")
        self.outbox: list[SMSMessage] = []

    def send(self, *, to: str, body: str, sender: str | None = None) -> str:
        sid = self._ids.next()
        self.outbox.append(SMSMessage(id=sid, to=to, body=body, sender=sender))
        return sid
