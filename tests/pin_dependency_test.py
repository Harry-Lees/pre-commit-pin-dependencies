import pytest

import entry


def test_no_dependencies() -> None:
    assert entry.main(["tests/resources/no_deps.toml"]) == 1

def test_pinned_dependencies() -> None:
    assert entry.main(["tests/resources/pinned_deps.toml"]) == 0

@pytest.mark.parametrize(
    "filename",
    [
        "tests/resources/caret.toml",
        "tests/resources/tilde.toml",
        "tests/resources/less_than_equal.toml",
        "tests/resources/more_than_equal.toml",
    ]
)
def test_unpinned_dependencies(filename) -> None:
    assert entry.main([filename]) == 1