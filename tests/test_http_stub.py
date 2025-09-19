from devdummies.stubs.http_stub import HttpStub


def test_http_stub_routes_and_calls():
    headers = {"X-Test": "1"}

    stub = HttpStub({
        ("GET", "/ping"): lambda: (200, headers, "pong")
    })

    status, returned_headers, body = stub.request("GET", "/ping")
    assert status == 200 and body == "pong"
    assert returned_headers is headers
    assert stub.calls == [("GET", "/ping")]

    status, _, _ = stub.request("GET", "/missing")
    assert status == 404



def test_http_stub_routes_allow_lowercase_methods():
    stub = HttpStub({
        ("post", "/lower"): lambda: (201, {"X-Test": "lower"}, "lowercase")
    })

    status, headers, body = stub.request("POST", "/lower")

    assert status == 201
    assert headers == {"X-Test": "lower"}
    assert body == "lowercase"

def test_http_stub_normalizes_registered_methods():
    stub = HttpStub({
        ("post", "/submit"): lambda: (201, {}, "created")
    })

    status, _, body = stub.request("POST", "/submit")

    assert status == 201 and body == "created"
    assert stub.calls == [("POST", "/submit")]

