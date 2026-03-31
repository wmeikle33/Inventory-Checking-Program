from __future__ import annotations

import json
from pathlib import Path

import typer

app = typer.Typer(add_completion=False, help="Thesis Webscraper CLI")

@app.command("sections")
def sections():
    for name in SECTION_URLS:
        print(name)

@app.command()
def run(
    columnA: str = typer.Option(..., "--Column A", help="Autohome section to scrape"),
    columnsB: str = typer.Option(1, "--Column B", min=1, help="Number of list pages to crawl"),
):
    cfg = ScrapeConfig(
        columnA=columnA,
        columnB=columnB,
        out_dir=out_dir,
        headless=headless,
        delay_ms=delay_ms,
    )

    result = scrape(cfg)

    print("[bold green]Done![/bold green]")
    print(f"Posts: {result.posts_count}")
    print(f"Comments: {result.comments_count}")
    print(f"Output: {out_dir.resolve()}")

    summary_path = out_dir.parent / "run_summary.json"
    summary_path.write_text(json.dumps(result.to_dict(), indent=2), encoding="utf-8")


def main():
    app()


if __name__ == "__main__":
    main()
