from __future__ import annotations
import pytest
from ..core.clock import FakeClock
from ..core.ids import IdFactory
from ..fakes.kv_memory import InMemoryKV
from ..fakes.mail_memory import InMemoryMailer

@pytest.fixture
def fake_clock():
    return FakeClock()

@pytest.fixture
def id_factory():
    return IdFactory()

@pytest.fixture
def kv():
    return InMemoryKV()

@pytest.fixture
def mailer(id_factory):
    return InMemoryMailer(id_factory=id_factory)
