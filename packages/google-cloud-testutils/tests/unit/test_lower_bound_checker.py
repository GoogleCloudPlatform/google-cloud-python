# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from contextlib import contextmanager
from pathlib import Path
import re
import tempfile
import sys
from typing import List

from click.testing import CliRunner
import pytest  # type: ignore

if sys.version_info >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    # For Python 3.7 compatibility
    import importlib_metadata

from test_utils.lower_bound_checker import lower_bound_checker

RUNNER = CliRunner()

PACKAGE_LIST_REGEX = re.compile(r"Error.*[\[\{](.+)[\]\}]")
DIFFERENT_VERSIONS_LIST_REGEX = re.compile("'(.*?)' lower bound is")

# These packages are installed into the environment by the nox session
# See 'resources/' for the setup.py files
GOOD_PACKAGE = "valid-package"
BAD_PACKAGE = "invalid-package"


def skip_test_if_not_installed(package_name: str):
    """Skips the current test if given package is not installed"""
    try:
        importlib_metadata.distribution(package_name)
    except importlib_metadata.PackageNotFoundError:
        pytest.skip(
            f"Skipping test which requires {package_name} in `tests/unit/resources/` to be installed"
        )


def parse_error_msg(msg: str) -> List[str]:
    """Get package names from the error message.

    Example:
        Error: setup.py is missing explicit lower bounds for the following packages: ["requests", "grpcio"]
    """
    match = PACKAGE_LIST_REGEX.search(msg)

    reqs: List[str] = []

    if match:
        reqs = match.groups(1)[0].split(",")  # type: ignore
        reqs = [r.strip().replace("'", "").replace('"', "") for r in reqs]

    return reqs


def parse_diff_versions_error_msg(msg: str) -> List[str]:
    """Get package names from the error message listing different versions

    Example:
        'requests' lower bound is 1.2.0 in setup.py but constraints file has 1.3.0
        'grpcio' lower bound is 1.0.0 in setup.py but constraints file has 1.10.0
    """
    pattern = re.compile(DIFFERENT_VERSIONS_LIST_REGEX)
    pkg_names = pattern.findall(msg)

    return pkg_names


@contextmanager
def constraints_file(requirements: List[str]):
    """Write the list of requirements into a temporary file"""

    tmpdir = tempfile.TemporaryDirectory()
    constraints_path = Path(tmpdir.name) / "constraints.txt"

    constraints_path.write_text("\n".join(requirements))
    yield constraints_path

    tmpdir.cleanup()


def test_update_constraints():
    skip_test_if_not_installed(GOOD_PACKAGE)

    with tempfile.TemporaryDirectory() as tmpdir:
        constraints_path = Path(tmpdir) / "constraints.txt"

        result = RUNNER.invoke(
            lower_bound_checker.update,
            [
                "--package-name",
                GOOD_PACKAGE,
                "--constraints-file",
                str(constraints_path),
            ],
        )

        assert result.exit_code == 0
        assert constraints_path.exists()

        output = constraints_path.read_text().split("\n")

        assert output == [
            "click==7.0.0",
            "grpcio==1.0.0",
            "packaging==14.0",
            "requests==1.0.0",
            "wheel==0.41.0",
        ]


def test_update_constraints_overwrites_existing_file():
    skip_test_if_not_installed(GOOD_PACKAGE)

    constraints = [
        "requests==1.0.0",
        "packaging==13.0",
        "wheel==0.42.0",
        "click==5.0.0",
    ]
    with constraints_file(constraints) as c:
        result = RUNNER.invoke(
            lower_bound_checker.update,
            ["--package-name", GOOD_PACKAGE, "--constraints-file", c],
        )

        assert result.exit_code == 0

        output = c.read_text().split("\n")
        assert output == [
            "click==7.0.0",
            "grpcio==1.0.0",
            "packaging==14.0",
            "requests==1.0.0",
            "wheel==0.41.0",
        ]


def test_update_constraints_with_setup_py_missing_lower_bounds():
    skip_test_if_not_installed(BAD_PACKAGE)

    constraints = [
        "requests==1.0.0",
        "packaging==14.0",
        "wheel==0.41.0",
        "click==7.0.0",
    ]
    with constraints_file(constraints) as c:
        result = RUNNER.invoke(
            lower_bound_checker.update,
            ["--package-name", BAD_PACKAGE, "--constraints-file", c],
        )

    assert result.exit_code == 2
    assert "setup.py is missing explicit lower bounds" in result.output

    invalid_pkg_list = parse_error_msg(result.output)
    assert set(invalid_pkg_list) == {"requests", "wheel"}


def test_check():
    skip_test_if_not_installed(GOOD_PACKAGE)

    constraints = [
        "requests==1.0.0",
        "packaging==14.0",
        "wheel==0.41.0",
        "click==7.0.0",
        "grpcio==1.0.0",
    ]
    with constraints_file(constraints) as c:
        result = RUNNER.invoke(
            lower_bound_checker.check,
            ["--package-name", GOOD_PACKAGE, "--constraints-file", c],
        )

    assert result.exit_code == 0


def test_update_constraints_with_extra_constraints():
    skip_test_if_not_installed(GOOD_PACKAGE)

    constraints = [
        "requests==1.0.0",
        "packaging==14.0",
        "wheel==0.41.0",
        "click==7.0.0",
        "grpcio==1.0.0",
        "pytest==6.0.0",  # additional requirement
    ]
    with constraints_file(constraints) as c:
        result = RUNNER.invoke(
            lower_bound_checker.check,
            ["--package-name", GOOD_PACKAGE, "--constraints-file", c],
        )

    assert result.exit_code == 0


def test_check_with_missing_constraints_file():
    skip_test_if_not_installed(GOOD_PACKAGE)

    result = RUNNER.invoke(
        lower_bound_checker.check,
        [
            "--package-name",
            GOOD_PACKAGE,
            "--constraints-file",
            "missing_constraints.txt",
        ],
    )

    assert result.exit_code == 1
    assert isinstance(result.exception, FileNotFoundError)


def test_check_with_constraints_file_invalid_pins():
    skip_test_if_not_installed(GOOD_PACKAGE)

    constraints = [
        "requests==1.0.0",
        "packaging==14.0",
        "wheel==1.0.0, <2.0.0dev",  # should be ==
        "click>=7.0.0",  # should be ==
    ]
    with constraints_file(constraints) as c:
        result = RUNNER.invoke(
            lower_bound_checker.check,
            ["--package-name", GOOD_PACKAGE, "--constraints-file", c],
        )

    assert result.exit_code == 2

    invalid_pkg_list = parse_error_msg(result.output)

    assert set(invalid_pkg_list) == {"wheel", "click"}


def test_check_with_constraints_file_missing_packages():
    skip_test_if_not_installed(GOOD_PACKAGE)

    constraints = [
        "requests==1.0.0",
        "packaging==14.0",
        # missing 'wheel' and 'click' and extra 'grpcio'
    ]
    with constraints_file(constraints) as c:
        result = RUNNER.invoke(
            lower_bound_checker.check,
            ["--package-name", GOOD_PACKAGE, "--constraints-file", c],
        )

    assert result.exit_code == 2

    invalid_pkg_list = parse_error_msg(result.output)
    assert set(invalid_pkg_list) == {"wheel", "click", "grpcio"}


def test_check_with_constraints_file_different_versions():
    skip_test_if_not_installed(GOOD_PACKAGE)

    constraints = [
        "requests==1.2.0",  # setup.py has 1.0.0
        "packaging==14.1",  # setup.py has 14.0
        "wheel==0.42.0",  # setup.py has 0.41.0
        "click==7.0.0",
        "grpcio==1.0.0",
    ]
    with constraints_file(constraints) as c:
        result = RUNNER.invoke(
            lower_bound_checker.check,
            ["--package-name", GOOD_PACKAGE, "--constraints-file", c],
        )

    assert result.exit_code == 2

    invalid_pkg_list = parse_diff_versions_error_msg(result.output)
    assert set(invalid_pkg_list) == {"requests", "packaging", "wheel"}


def test_check_with_setup_py_missing_lower_bounds():
    skip_test_if_not_installed(BAD_PACKAGE)

    constraints = [
        "requests==1.0.0",
        "packaging==14.0",
        "wheel==1.0.0",
        "click==7.0.0",
    ]
    with constraints_file(constraints) as c:
        result = RUNNER.invoke(
            lower_bound_checker.check,
            ["--package-name", BAD_PACKAGE, "--constraints-file", c],
        )

    assert result.exit_code == 2

    invalid_pkg_list = parse_error_msg(result.output)
    assert set(invalid_pkg_list) == {"requests", "wheel"}


def test_lower_bound_with_exclusion():
    from packaging.requirements import Requirement

    req = Requirement("google-auth>=1.25.0, !=2.24.0")
    assert lower_bound_checker._lower_bound(req) == "1.25.0"

    # Multiple exclusions
    req_multiple = Requirement("google-auth>=1.25.0, !=2.24.0, !=2.25.0")
    assert lower_bound_checker._lower_bound(req_multiple) == "1.25.0"

