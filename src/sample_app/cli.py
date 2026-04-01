from __future__ import annotations
from .inventory_checker import app

import json
from pathlib import Path

import typer

app = typer.Typer(add_completion=False, help="Inventory Checking Program CLI")

@app.command()
def run(
    input_dir: Path = typer.Option(Path("data/"), "--out-dir", help="Output file path"),
    columnA: str = typer.Option(..., "--Column A", help="Autohome section to scrape"),
    columnsB: str = typer.Option(1, "--Column B", min=1, help="Number of list pages to crawl"),
):

    print(f"Output: {out_dir.resolve()}")

    summary_path = out_dir.parent / "output.csv"
    summary_path.write_text(json.dumps(result.to_dict(), indent=2), encoding="utf-8")


def main():
    app()


if __name__ == "__main__":
    main()
