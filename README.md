# pre-commit pin Poetry dependencies

A pre-commit hook to ensure Poetry dependencies are pinned.

## Installation

```yaml
- repo: https://github.com/Harry-Lees/pre-commit-pin-dependencies
  rev: main  # or specific git tag
  hooks:
    - id: poetry-dependencies-pinned
```

## Example

The following pyproject.toml will raise an error as the Python dependency is not pinned.

```toml
# pyproject.toml
[tool.poetry.dependencies]
python = ">=3.7"
toml = "0.10.2"
```

## Motivation

When writing application code, it is important to ensure dependencies are pinned
in order to ensure reproducable builds.

By default, poetry will use [caret requirements](https://python-poetry.org/docs/dependency-specification/#caret-requirements) which will allow a range of possible versions. This can be misleading and cause hard to spot bugs in CI.
