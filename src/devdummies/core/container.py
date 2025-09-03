from __future__ import annotations
import os
from ..fakes.kv_memory import InMemoryKV
from ..fakes.mail_memory import InMemoryMailer
from ..fakes.queue_memory import InMemoryQueue
from ..fakes.flags_memory import InMemoryFlags
from ..fakes.secrets_memory import InMemorySecrets
from ..fakes.bus_memory import InMemoryBus

def build_services() -> dict[str, object]:
    """[IoC] Build default fake services when DEV_DUMMIES=1 (default)."""
    if os.getenv("DEV_DUMMIES", "1") == "1":
        return {
            "kv": InMemoryKV(),
            "mailer": InMemoryMailer(),
            "queue": InMemoryQueue(),
            "flags": InMemoryFlags(),
            "secrets": InMemorySecrets(),
            "bus": InMemoryBus(),
        }
    raise NotImplementedError("Real adapters live in your app.")
