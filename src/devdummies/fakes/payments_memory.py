from __future__ import annotations
from ..core.payments import PaymentGateway, Authorisation, Charge
from ..core.ids import IdFactory

class InMemoryPayments(PaymentGateway):
    """[Fake] Minimal payment gateway with authorise/capture/charge flows."""
    def __init__(self, id_factory: IdFactory | None = None) -> None:
        self._ids = id_factory or IdFactory("pay_")
        self._auths: dict[str, Authorisation] = {}
        self._charges: dict[str, Charge] = {}

    def authorise(self, *, amount: int, currency: str, card_token: str) -> Authorisation:
        aid = self._ids.next()
        auth = Authorisation(id=aid, amount=amount, currency=currency, approved=True)
        self._auths[aid] = auth
        return auth

    def capture(self, *, auth_id: str, amount: int | None = None) -> Charge:
        base = self._auths.get(auth_id)
        if not base:
            raise KeyError(f"Unknown auth_id: {auth_id}")
        cid = self._ids.next()
        amt = amount if amount is not None else base["amount"]
        ch = Charge(id=cid, amount=amt, currency=base["currency"], captured=True)
        self._charges[cid] = ch
        return ch

    def charge(self, *, amount: int, currency: str, card_token: str) -> Charge:
        cid = self._ids.next()
        ch = Charge(id=cid, amount=amount, currency=currency, captured=True)
        self._charges[cid] = ch
        return ch

    # observability
    def snapshot(self) -> dict[str, dict[str, dict]]:
        return {"authorisations": dict(self._auths), "charges": dict(self._charges)}
