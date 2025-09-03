from __future__ import annotations
from devdummies.fakes.mail_memory import InMemoryMailer

def test_mailer_outbox():
    m = InMemoryMailer()
    mid = m.send(to="t@example.com", subject="Hi", body="x")
    assert any(msg["id"] == mid for msg in m.outbox)
