# Copyright 2017 Google Inc.
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

from __future__ import absolute_import
import os
import pathlib
import re
import shutil

import nox

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


SYSTEM_TEST_ENV_VARS = ("GOOGLE_APPLICATION_CREDENTIALS",)
RUFF_VERSION = "ruff==0.14.14"

DEFAULT_PYTHON_VERSION = "3.14"
UNIT_TEST_PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13", "3.14", "3.15"]
SYSTEM_TEST_PYTHON_VERSIONS = UNIT_TEST_PYTHON_VERSIONS

# Error if a python version is missing
nox.options.error_on_missing_interpreters = True

nox.options.sessions = [
    "system",
    "blacken",
    "format",
    "mypy",
    "doctest",
]


@nox.session(python=UNIT_TEST_PYTHON_VERSIONS)
def unit(session):
    """Run the unit test suite."""

    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )

    # Install all test dependencies, then install this package in-place.
    session.install("mock", "pytest", "pytest-cov", "pytest-asyncio<=0.14.0", "brotli")
    session.install("-e", ".[requests,aiohttp]", "-c", constraints_path)

    # Run py.test against the unit tests.
    # NOTE: We don't require 100% line coverage for unit test runs since
    #       some have branches that are Py2/Py3 specific.
    line_coverage = "--cov-fail-under=0"
    session.run(
        "py.test",
        "--cov=google.resumable_media",
        "--cov=google._async_resumable_media",
        "--cov=tests.unit",
        "--cov=tests_async.unit",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",
        line_coverage,
        os.path.join("tests", "unit"),
        os.path.join("tests_async", "unit"),
        *session.posargs,
    )


@nox.session(python="3.10")
def docs(session):
    """Build the docs for this library."""

    session.install("-e", ".")
    session.install(
        # We need to pin to specific versions of the `sphinxcontrib-*` packages
        # which still support sphinx 4.x.
        # See https://github.com/googleapis/sphinx-docfx-yaml/issues/344
        # and https://github.com/googleapis/sphinx-docfx-yaml/issues/345.
        "sphinxcontrib-applehelp==1.0.4",
        "sphinxcontrib-devhelp==1.0.2",
        "sphinxcontrib-htmlhelp==2.0.1",
        "sphinxcontrib-qthelp==1.0.3",
        "sphinxcontrib-serializinghtml==1.1.5",
        "sphinx==4.5.0",
        "alabaster",
        "recommonmark",
    )

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    session.run(
        "sphinx-build",
        "-W",  # warnings as errors
        "-T",  # show full traceback on exception
        "-N",  # no colors
        "-b",
        "html",
        "-d",
        os.path.join("docs", "_build", "doctrees", ""),
        os.path.join("docs", ""),
        os.path.join("docs", "_build", "html", ""),
    )


@nox.session(python="3.10")
def docfx(session):
    """Build the docfx yaml files for this library."""

    session.install("-e", ".")
    session.install(
        # We need to pin to specific versions of the `sphinxcontrib-*` packages
        # which still support sphinx 4.x.
        # See https://github.com/googleapis/sphinx-docfx-yaml/issues/344
        # and https://github.com/googleapis/sphinx-docfx-yaml/issues/345.
        "sphinxcontrib-applehelp==1.0.4",
        "sphinxcontrib-devhelp==1.0.2",
        "sphinxcontrib-htmlhelp==2.0.1",
        "sphinxcontrib-qthelp==1.0.3",
        "sphinxcontrib-serializinghtml==1.1.5",
        "gcp-sphinx-docfx-yaml",
        "alabaster",
        "recommonmark",
    )

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    session.run(
        "sphinx-build",
        "-T",  # show full traceback on exception
        "-N",  # no colors
        "-D",
        (
            "extensions=sphinx.ext.autodoc,"
            "sphinx.ext.autosummary,"
            "docfx_yaml.extension,"
            "sphinx.ext.intersphinx,"
            "sphinx.ext.coverage,"
            "sphinx.ext.napoleon,"
            "sphinx.ext.todo,"
            "sphinx.ext.viewcode,"
            "recommonmark"
        ),
        "-b",
        "html",
        "-d",
        os.path.join("docs", "_build", "doctrees", ""),
        os.path.join("docs", ""),
        os.path.join("docs", "_build", "html", ""),
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def doctest(session):
    """Run the doctests."""
    session.install("-e", ".[requests,aiohttp]")
    session.install("sphinx==4.0.1", "alabaster", "recommonmark")
    session.install(
        "sphinxcontrib-applehelp==1.0.4",
        "sphinxcontrib-devhelp==1.0.2",
        "sphinxcontrib-htmlhelp==2.0.1",
        "sphinxcontrib-qthelp==1.0.3",
        "sphinxcontrib-serializinghtml==1.1.5",
        "sphinx==4.5.0",
        "sphinx_rtd_theme",
        "sphinx-docstring-typing >= 0.0.3",
        "mock",
    )

    # Run the doctests with Sphinx.
    session.run(
        "sphinx-build",
        "-W",
        "-b",
        "doctest",
        "-d",
        os.path.join("docs", "_build", "doctrees"),
        os.path.join("docs", ""),
        os.path.join("docs", "_build", "doctest"),
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint(session):
    """Run flake8.

    Returns a failure if flake8 finds linting errors or sufficiently
    serious code quality issues.
    """
    session.install("flake8", RUFF_VERSION)
    session.install("-e", ".")
    session.run(
        "flake8",
        os.path.join("google", "resumable_media"),
        "tests",
        os.path.join("google", "_async_resumable_media"),
        "tests_async",
    )

    # 1. Check imports
    session.run(
        "ruff",
        "check",
        "--select",
        "I",
        f"--target-version=py{UNIT_TEST_PYTHON_VERSIONS[0].replace('.', '')}",
        "--line-length=88",
        os.path.join("google", "resumable_media"),
        "tests",
        os.path.join("google", "_async_resumable_media"),
        "tests_async",
    )

    # 2. Check formatting
    session.run(
        "ruff",
        "format",
        "--check",
        f"--target-version=py{UNIT_TEST_PYTHON_VERSIONS[0].replace('.', '')}",
        "--line-length=88",
        os.path.join("google", "resumable_media"),
        "tests",
        os.path.join("google", "_async_resumable_media"),
        "tests_async",
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint_setup_py(session):
    """Verify that setup.py is valid (including RST check)."""
    session.install("setuptools", "docutils", "Pygments")
    session.run("python", "setup.py", "check", "--restructuredtext", "--strict")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def blacken(session):
    """(Deprecated) Legacy session. Please use 'nox -s format'."""
    session.log(
        "WARNING: The 'blacken' session is deprecated and will be removed in a future release. Please use 'nox -s format' in the future."
    )

    # Just run the ruff formatter (keeping legacy behavior of only formatting, not sorting imports)
    session.install(RUFF_VERSION)
    session.run(
        "ruff",
        "format",
        f"--target-version=py{UNIT_TEST_PYTHON_VERSIONS[0].replace('.', '')}",
        "--line-length=88",
        os.path.join("google", "resumable_media"),
        "tests",
        os.path.join("google", "_async_resumable_media"),
        "tests_async",
    )


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
        f"--target-version=py{UNIT_TEST_PYTHON_VERSIONS[0].replace('.', '')}",
        "--line-length=88",  # Standard Black line length
        os.path.join("google", "resumable_media"),
        "tests",
        os.path.join("google", "_async_resumable_media"),
        "tests_async",
    )

    # 3. Run Ruff to format code
    session.run(
        "ruff",
        "format",
        f"--target-version=py{UNIT_TEST_PYTHON_VERSIONS[0].replace('.', '')}",
        "--line-length=88",  # Standard Black line length
        os.path.join("google", "resumable_media"),
        "tests",
        os.path.join("google", "_async_resumable_media"),
        "tests_async",
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def mypy(session):
    """Verify type hints are mypy compatible."""
    session.install("-e", ".")
    session.install(
        "mypy",
        "types-setuptools",
        "types-requests",
        "types-mock",
    )
    session.run(
        "mypy",
        f"--config-file={MYPY_CONFIG_FILE}",
        "-p",
        "google",
        "-p",
        "tests",
        "-p",
        "tests_async",
    )


@nox.session(python=SYSTEM_TEST_PYTHON_VERSIONS)
def system(session):
    """Run the system test suite."""

    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )

    # Environment check: environment variables are set.
    missing = []
    for env_var in SYSTEM_TEST_ENV_VARS:
        if env_var not in os.environ:
            missing.append(env_var)

    # Only run system tests if the environment variables are set.
    if missing:
        all_vars = ", ".join(missing)
        msg = "Environment variable(s) unset: {}".format(all_vars)
        session.skip(msg)

    # Install all test dependencies, then install this package into the
    # virtualenv's dist-packages.
    session.install("mock", "pytest", "google-cloud-testutils", "brotli")
    session.install("-e", ".[requests,aiohttp]", "-c", constraints_path)

    # Run py.test against the async system tests.
    if session.python.startswith("3"):
        session.install("pytest-asyncio<=0.14.0")
        session.run(
            "py.test", "-s", os.path.join("tests_async", "system"), *session.posargs
        )

    # Run py.test against the system tests.
    session.run("py.test", "-s", os.path.join("tests", "system"), *session.posargs)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def cover(session):
    """Run the final coverage report.

    This outputs the coverage report aggregating coverage from the unit
    test runs (not system test runs), and then erases coverage data.
    """
    session.install("coverage", "pytest-cov")
    session.run("coverage", "report", "--show-missing", "--fail-under=100")
    session.run("coverage", "erase")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def prerelease_deps(session):
    """
    Run all tests with pre-release versions of dependencies installed
    rather than the standard non pre-release versions.
    Pre-release versions can be installed using
    `pip install --pre <package>`.
    """

    # Install standard test dependencies, then install local packages in-place.
    session.install("mock", "pytest", "pytest-cov", "pytest-asyncio<=0.14.0", "brotli")
    session.install("-e", ".[requests,aiohttp]")

    # Because we test minimum dependency versions on the minimum Python
    # version, the first version we test with in the unit tests sessions has a
    # constraints file containing all dependencies and extras.
    with open(
        CURRENT_DIRECTORY
        / "testing"
        / f"constraints-{UNIT_TEST_PYTHON_VERSIONS[0]}.txt",
        encoding="utf-8",
    ) as constraints_file:
        constraints_text = constraints_file.read()

    # Ignore leading whitespace and comment lines.
    constraints_deps = [
        match.group(1)
        for match in re.finditer(
            r"^\s*(\S+)(?===\S+)", constraints_text, flags=re.MULTILINE
        )
    ]

    # Install dependencies specified in `testing/constraints-X.txt`.
    session.install(*constraints_deps)

    # Note: If a dependency is added to the `prerel_deps` list,
    # the `core_dependencies_from_source` list in the `core_deps_from_source`
    # nox session should also be updated.
    prerel_deps = [
        "google-crc32c",
        "google-auth",
        "cryptography",
        "cffi",
        "cachetools",
        "rsa",
        "pyasn1",
    ]

    deps_dir = CURRENT_DIRECTORY.parent
    while deps_dir.name != "packages" and deps_dir.parent != deps_dir:
        deps_dir = deps_dir.parent

    # Extract the base package name, safely ignoring version bounds and spaces
    # (e.g., "grpcio>=1.75.1" becomes "grpcio")
    parsed_deps = {
        dep: re.match(r"^([a-zA-Z0-9_-]+)", dep).group(1) for dep in prerel_deps
    }

    # Dynamically sort local packages vs PyPI dependencies
    local_paths = []
    pypi_deps = []

    for dep, pkg_name in parsed_deps.items():
        if (deps_dir / pkg_name).exists():
            local_paths.append(str(deps_dir / pkg_name))
        else:
            pypi_deps.append(dep)

    # Batch pip installations to avoid sequential overhead
    if local_paths:
        session.install(*local_paths, "--no-deps", "--ignore-installed")
    if pypi_deps:
        session.install(*pypi_deps, "--pre", "--no-deps", "--ignore-installed")

    # Reuse the parsed names for logging and version verification
    for dep, pkg_name in parsed_deps.items():
        print(f"Installed {dep}")

    session.run(
        "py.test",
        os.path.join("tests", "unit"),
        os.path.join("tests_async", "unit"),
        *session.posargs,
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def core_deps_from_source(session):
    """Run all tests with core dependencies installed from source
    rather than pulling the dependencies from PyPI.
    """

    # Install standard test dependencies, then install local packages in-place.
    session.install("mock", "pytest", "pytest-cov", "pytest-asyncio<=0.14.0", "brotli")
    session.install("-e", ".[requests,aiohttp]")

    # Because we test minimum dependency versions on the minimum Python
    # version, the first version we test with in the unit tests sessions has a
    # constraints file containing all dependencies and extras.
    with open(
        CURRENT_DIRECTORY
        / "testing"
        / f"constraints-{UNIT_TEST_PYTHON_VERSIONS[0]}.txt",
        encoding="utf-8",
    ) as constraints_file:
        constraints_text = constraints_file.read()

    # Ignore leading whitespace and comment lines.
    constraints_deps = [
        match.group(1)
        for match in re.finditer(
            r"^\s*(\S+)(?===\S+)", constraints_text, flags=re.MULTILINE
        )
    ]

    # Install dependencies specified in `testing/constraints-X.txt`.
    session.install(*constraints_deps)

    # Note: If a dependency is added to the `core_dependencies_from_source` list,
    # the `prerel_deps` list in the `prerelease_deps` nox session should also be updated.
    core_dependencies_from_source = [
        "google-crc32c",
        "google-auth",
    ]

    deps_dir = CURRENT_DIRECTORY.parent
    while deps_dir.name != "packages" and deps_dir.parent != deps_dir:
        deps_dir = deps_dir.parent

    # Batch the pip installation to avoid sequential overhead
    dep_paths = [str(deps_dir / dep) for dep in core_dependencies_from_source]

    session.install(*dep_paths, "--no-deps", "--ignore-installed")
    print(
        f"Installed {', '.join(core_dependencies_from_source)} locally from {deps_dir}"
    )

    other_deps = [
        "cryptography",
        "cffi",
        "cachetools",
        "rsa",
        "pyasn1",
    ]
    session.install(*other_deps)

    session.run(
        "py.test",
        os.path.join("tests", "unit"),
        os.path.join("tests_async", "unit"),
        *session.posargs,
    )
