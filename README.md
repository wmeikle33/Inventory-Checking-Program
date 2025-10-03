# Inventory Checking Program (Sample/Redacted)

This repository provides a **minimal, redaction‑safe sample** of a larger internal program.
It demonstrates sample code without exposing any proprietary logic.

> ✅ You can share this repo publicly. All domain details are generic; any sensitive components are stubbed.

## What's included
- **Sample Code** that aggregates demo CSV (sum by category).
- **Redaction policy** to guide what *can/can't* be shared.

## Quickstart
```bash
# (optional) create venv
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
pip install -r requirements-dev.txt

# run the demo pipeline
python -m sample_app.cli --input sample_data/input.csv --output sample_data/output.csv

# run tests
pytest -q
```

## Architecture (minimal, extensible)
```
src/sample_app
├── sample code.py  
```
- Replace or extend adapters with your internal implementations (kept private).
- Keep interfaces stable to demonstrate design without revealing details.

## How to bring your private code without leaking IP
1. **Keep this repo public** with only the sample code.
2. In your private repo, implement adapters/processors that import these public interfaces.
3. Show reviewers *just* the public repo and, if needed, a **screen share** for private parts.

See: [docs/REDACTION_POLICY.md](docs/REDACTION_POLICY.md).

## Why this is intentionally small
- Hiring teams want to see **how** you structure/think, not full IP.
- This repo shows tests, CI, docs, and clean seams—enough to evaluate engineering quality.

## License
MIT (see `LICENSE`).
