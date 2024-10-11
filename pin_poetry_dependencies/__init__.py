import argparse
from typing import Any, Mapping, Sequence, Union

import toml


def path_exists(obj: Mapping[Any, Any], path: Sequence[str]) -> bool:
    """
    Test if a given path exists in a nested mapping.
    """
    if path[0] in obj:
        if len(path) == 1:
            return True
        return path_exists(obj[path[0]], path[1:])
    return False


def iter_dependencies(obj: Mapping[Any, Any]):
    """
    Iterate over all poetry dependencies in a nested mapping.
    """

    if not path_exists(obj, ("tool", "poetry", "dependencies")):
        raise ValueError("No dependencies found")

    for dep, version in obj["tool"]["poetry"]["dependencies"].items():
        if isinstance(version, str):
            yield dep, version
        elif isinstance(version, Mapping):
            if "version" in version:
                yield dep, version["version"]
        else:
            raise ValueError(f"Unexpected version type: {type(version)}")


def main(argv: Union[Sequence[str], None] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="+")
    parser.add_argument(
        "--allow-unpinned-python",
        default=False,
        action="store_true",
        help="Allow the `python` dependency to be unpinned.",
        )
    args = parser.parse_args(argv)

    failed = []
    for filename in args.filenames:
        try:
            with open(filename, "r") as f:
                pyproject = toml.load(f)
                for dep, version in iter_dependencies(pyproject):
                    if dep == "python" and args.allow_unpinned_python:
                        continue
                    if version.startswith(("^", "~", ">", "<")) or "*" in version:
                        failed.append(f"{filename}: {dep} {version}")
        except Exception as error:
            print(f"An unexpected error occurred while parsing {filename}: {error}")
            return 1
    if len(failed) > 0:
        print("The following dependencies are not pinned:")
        print(*failed, sep="\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
