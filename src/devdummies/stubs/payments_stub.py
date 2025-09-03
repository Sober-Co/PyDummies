from __future__ import annotations
from ..core.payments import PaymentGateway, Authorisation, Charge
from ..core.ids import IdFactory

class PaymentsStub(PaymentGateway):
    """[Stub] Canned responses for payment flows."""
    def __init__(self, approved: bool = True, id_factory: IdFactory | None = None) -> None:
        self.approved = approved
        self._ids = id_factory or IdFactory("stubpay_")

    def authorise(self, *, amount: int, currency: str, card_token: str) -> Authorisation:
        return Authorisation(id=self._ids.next(), amount=amount, currency=currency, approved=self.approved)

    def capture(self, *, auth_id: str, amount: int | None = None) -> Charge:
        return Charge(id=self._ids.next(), amount=amount or 0, currency="XXX", captured=self.approved)

    def charge(self, *, amount: int, currency: str, card_token: str) -> Charge:
        return Charge(id=self._ids.next(), amount=amount, currency=currency, captured=self.approved)
