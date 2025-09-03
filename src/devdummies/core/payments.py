from __future__ import annotations
from typing import Protocol, TypedDict

class Authorisation(TypedDict):
    id: str
    amount: int  # in minor units
    currency: str
    approved: bool

class Charge(TypedDict):
    id: str
    amount: int
    currency: str
    captured: bool

class PaymentGateway(Protocol):
    def authorise(self, *, amount: int, currency: str, card_token: str) -> Authorisation: ...
    def capture(self, *, auth_id: str, amount: int | None = None) -> Charge: ...
    def charge(self, *, amount: int, currency: str, card_token: str) -> Charge: ...
