from __future__ import annotations
from devdummies.stubs.http_stub import HttpStub

def test_http_stub_routes_and_calls():
    stub = HttpStub({
        ("GET", "/ping"): lambda: (200, {"X-Test": "1"}, "pong")
    })
    status, headers, body = stub.request("GET", "/ping")
    assert status == 200 and body == "pong"
    assert stub.calls == [("GET", "/ping")]
    status, _, _ = stub.request("GET", "/missing")
    assert status == 404


def test_http_stub_normalizes_registered_methods():
    stub = HttpStub({
        ("post", "/submit"): lambda: (201, {}, "created")
    })

    status, _, body = stub.request("POST", "/submit")

    assert status == 201 and body == "created"
    assert stub.calls == [("POST", "/submit")]
