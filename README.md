# PyDummies

Deterministic **test doubles** and **service emulators** for Python 3.13.

- Deterministic: seedable clocks/IDs/RNG
- Drop-in: `typing.Protocol` interfaces
- Fast: in-memory by default
- Observable: inspect state, counters, mailboxes, queues

## Install

```bash
pip install -e .
# or build
pipx run build
```

Optional extras:
```bash
pip install .[http]       # ASGI emulator helpers (Starlette)
pip install .[vcr]        # record/replay
```

## Quickstart

```python
from devdummies.core.clock import FakeClock
from devdummies.fakes.mail_memory import InMemoryMailer

clock = FakeClock()
mailer = InMemoryMailer()
mid = mailer.send(to="user@example.com", subject="Welcome", body="Hello")
assert mailer.outbox[-1]["id"] == mid
```

## License
MIT
