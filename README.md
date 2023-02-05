# pre-commit pin Poetry dependencies

A pre-commit hook to ensure Poetry dependencies are pinned.

## Motivation

When writing application code, it is important to ensure dependencies are pinned
in order to ensure reproducable builds.

By default, poetry will use [caret requirements](https://python-poetry.org/docs/dependency-specification/#caret-requirements) which will allow a range of possible versions. This can be misleading and cause hard to spot bugs in CI.
