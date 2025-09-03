from __future__ import annotations
from pathlib import Path
from datetime import datetime

class SmtpCapture:
    """[Emulator-ish] File-based SMTP capture: writes RFC822-ish files.

    This does not run an SMTP server; it captures messages to disk via a send() API,
    useful when you want file artifacts rather than in-memory outbox.
    """
    def __init__(self, out_dir: str) -> None:
        self.out = Path(out_dir)
        self.out.mkdir(parents=True, exist_ok=True)

    def send(self, *, to: str, subject: str, body: str, from_: str | None = None) -> str:
        ts = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
        mid = f"mail_{ts}"
        p = self.out / f"{mid}.eml"
        p.write_text(f"From: {from_ or 'noreply@example.com'}\nTo: {to}\nSubject: {subject}\n\n{body}\n", encoding="utf-8")
        return mid
