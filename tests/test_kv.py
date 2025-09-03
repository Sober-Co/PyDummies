from __future__ import annotations
from devdummies.fakes.kv_memory import InMemoryKV

def test_kv_basic():
    kv = InMemoryKV()
    kv.set("a", 1)
    assert kv.get("a") == 1
    assert kv.keys("a") == ["a"]
    kv.delete("a")
    assert kv.get("a") is None
