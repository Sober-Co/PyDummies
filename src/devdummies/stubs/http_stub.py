from __future__ import annotations
from typing import Callable, Mapping, Tuple

RequestKey = Tuple[str, str]  # (method, path)

class HttpStub:
    """[Stub] Route table mapping (METHOD, PATH) -> handler() -> (status, headers, body)."""
    def __init__(self, routes: Mapping[RequestKey, Callable[[], tuple[int, dict, str]]]):
        self.routes = dict(routes)
        self.calls: list[RequestKey] = []

    def request(self, method: str, path: str) -> tuple[int, dict, str]:
        key = (method.upper(), path)
        self.calls.append(key)
        handler = self.routes.get(key)
        if not handler:
            return 404, {}, "Not Found"
        return handler()
