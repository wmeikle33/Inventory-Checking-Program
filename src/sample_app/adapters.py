from __future__ import annotations
import csv
from typing import Iterable, Dict, List
from .interfaces import Source, Sink, Record

class LocalCSVSource(Source):
    """Tiny demo source that reads a CSV with headers."""
    def __init__(self, path: str, encoding: str = "utf-8") -> None:
        self.path = path
        self.encoding = encoding

    def read(self) -> Iterable[Record]:
        with open(self.path, newline="", encoding=self.encoding) as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield dict(row)

class LocalCSVSink(Sink):
    """Tiny demo sink that writes a CSV with headers from the first row."""
    def __init__(self, path: str, encoding: str = "utf-8") -> None:
        self.path = path
        self.encoding = encoding

    def write(self, rows: Iterable[Record]) -> None:
        rows = list(rows)
        if not rows:
            # create empty file with headers: none
            open(self.path, "w", encoding=self.encoding).close()
            return
        fieldnames = list(rows[0].keys())
        with open(self.path, "w", newline="", encoding=self.encoding) as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            for r in rows:
                w.writerow(r)

class InMemorySink(Sink):
    """Testing sink that just captures rows in memory."""
    def __init__(self) -> None:
        self.data: List[Record] = []

    def write(self, rows: Iterable[Record]) -> None:
        self.data = list(rows)
