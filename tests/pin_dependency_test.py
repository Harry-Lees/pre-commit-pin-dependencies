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
        "tests/resources/less_than_equal.toml",
        "tests/resources/more_than_equal.toml",
        "tests/resources/multiple_unpinned.toml",
        "tests/resources/tilde.toml",
    ],
)
def test_unpinned_dependencies(filename) -> None:
    assert pin_poetry_dependencies.main([filename]) == 1


def test_allow_unpinned() -> None:
    assert pin_poetry_dependencies.main(["tests/resources/tilde.toml"]) == 1
    assert (
        pin_poetry_dependencies.main(
            ["--allow-unpinned=python", "tests/resources/tilde.toml"]
        )
        == 1
    )
    assert (
        pin_poetry_dependencies.main(
            ["--allow-unpinned=toml", "tests/resources/tilde.toml"]
        )
        == 0
    )


def test_allow_multiple_unpinned() -> None:
    assert pin_poetry_dependencies.main(["tests/resources/multiple_unpinned.toml"]) == 1
    assert (
        pin_poetry_dependencies.main(
            [
                "--allow-unpinned=python",
                "--allow-unpinned=toml",
                "--allow-unpinned=pytest",
                "tests/resources/multiple_unpinned.toml",
            ]
        )
        == 0
    )
