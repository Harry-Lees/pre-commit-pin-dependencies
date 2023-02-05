import pytest

import pin_poetry_dependencies


def test_no_dependencies() -> None:
    assert pin_poetry_dependencies.main(["tests/resources/no_deps.toml"]) == 1

def test_pinned_dependencies() -> None:
    assert pin_poetry_dependencies.main(["tests/resources/pinned_deps.toml"]) == 0

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
    assert pin_poetry_dependencies.main([filename]) == 1