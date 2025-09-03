from __future__ import annotations
from datetime import timedelta
from devdummies.core.clock import FakeClock

def test_fake_clock_advances():
    c = FakeClock()
    t0 = c.now()
    c.sleep(timedelta(seconds=5))
    assert (c.now() - t0).total_seconds() == 5
