from __future__ import annotations
from typing import Iterable, Dict
from collections import defaultdict
from .interfaces import Source, Processor, Sink, Record

class SumByCategory(Processor):
    """Minimal processor: sum numeric 'value' per 'category'."""
    def process(self, rows: Iterable[Record]) -> Iterable[Record]:
        totals = defaultdict(float)
        for r in rows:
            try:
                v = float(r.get("value", 0))
            except ValueError:
                v = 0.0
            cat = r.get("category", "unknown")
            totals[cat] += v
        for cat, total in totals.items():
            yield {"category": cat, "total_value": f"{total:.2f}"}

def run_pipeline(source: Source, processor: Processor, sink: Sink) -> None:
    sink.write(processor.process(source.read()))
