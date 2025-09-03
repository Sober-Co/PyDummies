from __future__ import annotations
from typing import Protocol, Mapping, Any, NamedTuple

class Request(NamedTuple):
    method: str
    path: str
    headers: Mapping[str, str] = {}
    body: bytes = b""

class Response(NamedTuple):
    status: int
    headers: Mapping[str, str]
    body: bytes

class HTTPService(Protocol):
    def request(self, req: Request) -> Response: ...
