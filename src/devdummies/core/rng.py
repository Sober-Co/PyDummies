from __future__ import annotations
import random
from typing import Iterable, TypeVar, Sequence

T = TypeVar("T")

class SeededRNG:
    """[Determinism] Wrapper around random.Random for reproducible tests."""
    def __init__(self, seed: int | str | bytes | bytearray) -> None:
        self._r = random.Random()
        self._r.seed(seed)

    def randint(self, a: int, b: int) -> int:
        return self._r.randint(a, b)

    def choice(self, seq: Sequence[T]) -> T:
        return self._r.choice(seq)

    def shuffle(self, x: list[T]) -> None:
        self._r.shuffle(x)

    def sample(self, population: Sequence[T] | set[T], k: int) -> list[T]:
        return self._r.sample(list(population), k)
