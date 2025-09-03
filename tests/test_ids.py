from __future__ import annotations
from devdummies.core.ids import IdFactory

def test_ids_monotonic():
    ids = IdFactory(prefix="x_", start=41)
    assert ids.next() == "x_41"
    assert ids.next() == "x_42"
