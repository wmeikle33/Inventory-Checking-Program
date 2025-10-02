from __future__ import annotations
import argparse
from .adapters import LocalCSVSource, LocalCSVSink
from .pipeline import SumByCategory, run_pipeline

def main() -> None:
    p = argparse.ArgumentParser(description="Sample pipeline (redaction-safe).")
    p.add_argument("--input", required=True, help="Path to input CSV with columns: category,value")
    p.add_argument("--output", required=True, help="Path to write aggregated CSV")
    args = p.parse_args()

    run_pipeline(
        source=LocalCSVSource(args.input),
        processor=SumByCategory(),
        sink=LocalCSVSink(args.output),
    )

if __name__ == "__main__":
    main()
