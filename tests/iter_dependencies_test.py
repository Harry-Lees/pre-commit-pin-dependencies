import pytest

from pin_poetry_dependencies import iter_dependencies


def test_iter_dependencies() -> None:
    dependencies = iter_dependencies({
        "tool": {
            "poetry": {
                "dependencies": {
                    "requests": "^2.25.1",
                    "toml": {"version": "^0.10.2"},
                    "torch": [
                        {"version": "^2.2.2"},
                        {"version": "^2.2.2+cpu"},
                    ],
                }
            }
        }
    })
    assert list(dependencies) == [
        ("requests", "^2.25.1"),
        ("toml", "^0.10.2"),
        ("torch", "^2.2.2"),
        ("torch", "^2.2.2+cpu"),
    ]

def test_iter_dependencies_no_dependencies() -> None:
    with pytest.raises(ValueError, match="No dependencies found"):
        list(iter_dependencies({}))

def test_iter_dependencies_unexpected_version_type() -> None:
    with pytest.raises(ValueError, match="Unexpected version type: <class 'int'>"):
        list(iter_dependencies({
            "tool": {
                "poetry": {
                    "dependencies": {
                        "requests": 42,
                    }
                }
            }
        })
    )