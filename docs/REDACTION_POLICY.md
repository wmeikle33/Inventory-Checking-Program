# Redaction Policy (Public Sample)

This repository is intentionally **minimal** to avoid exposing proprietary details.

## DO share
- Interfaces (`interfaces.py`) and simple demo adapters.
- Trivial example logic (`SumByCategory`) that conveys *shape*, not domain IP.
- Generic tests, docs, and CI configuration.

## DO NOT share
- Any real data, schemas, proprietary algorithms, or secrets.
- Internal service URLs, credentials, or vendor names that aren't public.
- Business-specific constants, queries, or rules.

## How to extend privately
- In a private repo, implement your real `Source`/`Processor`/`Sink` against these interfaces.
- Keep environment variables and credentials in your private repo or a secrets manager.
