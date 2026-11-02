# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pathlib

import nox

DEFAULT_PYTHON_VERSION = "3.14"
UNIT_TEST_PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13", "3.14", "3.15"]
CURRENT_DIRECTORY = pathlib.Path(__file__).parent.absolute()
# Path to the centralized mypy configuration file at the repository root.
# Search upwards to support running nox from both monorepo packages and integration test goldens.
MYPY_CONFIG_FILE = next(
    (
        str(p / "mypy.ini")
        for p in CURRENT_DIRECTORY.parents
        if (p / "mypy.ini").exists()
    ),
    str(CURRENT_DIRECTORY.parent.parent / "mypy.ini"),
)

RUFF_VERSION = "ruff==0.14.14"

ALL_PYTHON = list(UNIT_TEST_PYTHON_VERSIONS)
# ALL_PYTHON.extend(["3.7"]) # User said NOT to include 3.7

nox.options.sessions = [
    "format",
    "lint",
    "lint_setup_py",
    "mypy",
    "unit",
    "docs",
    "prerelease_deps",
    "core_deps_from_source",
]


def _skip_python_session(session, versions):
    if session.python in versions:
        session.skip(
            f"Python {session.python} is either not supported or the tests are disabled temporarily."
        )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def mypy(session):
    """Run the type checker."""
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16014):
    # Add mypy tests
    session.skip("mypy tests are not yet supported")

    session.install("-e", ".")
    session.install(
        "mypy",
        "types-setuptools",
        "types-protobuf",
        "types-requests",
    )
    session.run(
        "mypy",
        f"--config-file={MYPY_CONFIG_FILE}",
        "-p",
        "docfx_yaml",
        *session.posargs,
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def core_deps_from_source(session):
    """Run all tests with core dependencies installed from source
    rather than pulling the dependencies from PyPI.
    """
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16014):
    # Add core deps from source tests
    session.skip("Core deps from source tests are not yet supported")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def prerelease_deps(session):
    """Run all tests with prerelease versions of dependencies installed."""
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16014):
    # Add prerelease deps tests
    session.skip("prerelease deps tests are not yet supported")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def format(session):
    """
    Run ruff to sort imports and format code.
    """

    # 1. Install ruff (skipped automatically if you run with --no-venv)
    session.install(RUFF_VERSION)

    # 2. Run Ruff to fix imports
    # check --select I: Enables strict import sorting
    # --fix: Applies the changes automatically
    session.run(
        "ruff",
        "check",
        "--select",
        "I",
        "--fix",
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",  # Standard Black line length
        ".",
    )

    # 3. Run Ruff to format code
    session.run(
        "ruff",
        "format",
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",  # Standard Black line length
        ".",
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint(session):
    """Run linters.

    Returns a failure if the linters find linting errors or sufficiently
    serious code quality issues.
    """
    session.install("flake8", RUFF_VERSION)

    # 1. Check imports
    session.run(
        "ruff",
        "check",
        "--select",
        "I",
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",
        ".",
    )

    # 2. Check formatting
    session.run(
        "ruff",
        "format",
        "--check",
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",
        ".",
    )

    # TODO(https://github.com/googleapis/google-cloud-python/issues/16179):
    # Resolve existing lint errors and remove success_codes=[0, 1] to enforce strict pass/fail.
    session.run("flake8", ".", success_codes=[0, 1])


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint_setup_py(session):
    """Lint setup.py."""
    session.install("setuptools", "flake8")
    session.run("flake8", "setup.py")


# Use virtualenv backend to prevent modern uv build isolation from failing on
# legacy sdist dependencies (unify/untokenize)
@nox.session(python=UNIT_TEST_PYTHON_VERSIONS, venv_backend="virtualenv")
def unit(session):
    """Run unit tests."""
    # Re-enable 3.11, 3.12, and 3.13 after environment verification.
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16176):
    # Track 3.14 compatibility as upstream dependencies stabilize.
    _skip_python_session(session, ["3.11", "3.12", "3.13", "3.14", "3.15"])
    session.install("-r", "requirements.txt")
    session.install("pytest", "pytest-cov")
    session.run(
        "pytest",
        "--cov=docfx_yaml",
        "--cov=tests",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",
        "--cov-fail-under=0",
        "tests",
    )


@nox.session(python="3.10")
def docs(session):
    """Build documentation (POSTPONED)."""
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16177):
    # investigate and implement docs session if needed.
    session.skip(
        "Docs build postponed during migration. "
        "Requires resolution of Sphinx 1.5.5 / Jinja2 compatibility."
    )


@nox.session(python="3.10")
def docfx(session):
    """Build documentation (POSTPONED)."""
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16178):
    # investigate and implement docs session if needed.
    session.skip(
        "DocFX build postponed during migration. "
        "Requires resolution of Sphinx 1.5.5 / Jinja2 compatibility."
    )
