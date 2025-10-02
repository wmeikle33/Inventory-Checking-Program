from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Dict

Record = Dict[str, str]

class Source(ABC):
    @abstractmethod
    def read(self) -> Iterable[Record]:
        """Yield records. No business logic here."""

class Processor(ABC):
    @abstractmethod
    def process(self, rows: Iterable[Record]) -> Iterable[Record]:
        """Transform records (e.g., enrich, validate, aggregate)."""

class Sink(ABC):
    @abstractmethod
    def write(self, rows: Iterable[Record]) -> None:
        """Consume rows (e.g., store, publish)."""
