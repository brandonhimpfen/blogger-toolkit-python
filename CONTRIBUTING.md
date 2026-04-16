# Contributing

Thanks for contributing to Blogger Toolkit.

## General guidelines

Please keep new tools practical, lightweight, and well documented.

A good contribution usually includes:

- a clear use case
- simple function signatures
- docstrings
- example usage when appropriate
- tests for core behavior

## Development setup

```bash
pip install -e .[dev]
pytest
```

## Style

- Prefer explicit, readable code
- Keep dependencies minimal
- Avoid heavy frameworks for simple tasks
- Treat metrics and scores as signals, not guarantees
