# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
#
import os
import pathlib
import re
import shutil
import sys
import warnings
from typing import Dict, List

import nox

RUFF_VERSION = "ruff==0.14.14"
LINT_PATHS = ["google", "tests", "noxfile.py", "setup.py"]

DEFAULT_PYTHON_VERSION = "3.14"

# Default to Python 3.12 for local development if available. If Python 3.12 is
# not installed (such as in CI environments where a different Python version
# is provisioned), fall back to the currently running Python interpreter to
# avoid InterpreterNotFound errors. Can also be overridden via the
# MOCK_SERVER_TESTS_PYTHON_VERSION environment variable.
DEFAULT_MOCK_SERVER_TESTS_PYTHON_VERSION = os.environ.get(
    "MOCK_SERVER_TESTS_PYTHON_VERSION",
    "3.12"
    if shutil.which("python3.12")
    else f"{sys.version_info.major}.{sys.version_info.minor}",
)
SYSTEM_TEST_PYTHON_VERSIONS: List[str] = ["3.12"]

ALL_PYTHON: List[str] = [
    "3.10",
    "3.11",
    "3.12",
    "3.13",
    "3.14",
    "3.15",
]
UNIT_TEST_STANDARD_DEPENDENCIES = [
    "mock",
    "asyncmock",
    "pytest",
    "pytest-cov",
    "pytest-asyncio",
    "pytest-xdist",
]
MOCK_SERVER_ADDITIONAL_DEPENDENCIES = [
    "google-cloud-testutils",
]
UNIT_TEST_EXTERNAL_DEPENDENCIES: List[str] = []
UNIT_TEST_LOCAL_DEPENDENCIES: List[str] = []
UNIT_TEST_DEPENDENCIES: List[str] = []
UNIT_TEST_EXTRAS: List[str] = [
    "omni",
]
UNIT_TEST_EXTRAS_BY_PYTHON: Dict[str, List[str]] = {}

SYSTEM_TEST_STANDARD_DEPENDENCIES: List[str] = [
    "mock",
    "pytest",
    "pytest-asyncio",
    "google-cloud-testutils",
]
SYSTEM_TEST_EXTERNAL_DEPENDENCIES: List[str] = []
SYSTEM_TEST_LOCAL_DEPENDENCIES: List[str] = []
SYSTEM_TEST_DEPENDENCIES: List[str] = []
SYSTEM_TEST_EXTRAS: List[str] = [
    "tracing",
    "omni",
]
SYSTEM_TEST_EXTRAS_BY_PYTHON: Dict[str, List[str]] = {}

CURRENT_DIRECTORY = pathlib.Path(__file__).parent.absolute()

nox.options.sessions = [
    "unit-3.10",
    "unit-3.11",
    "unit-3.12",
    "unit-3.13",
    "unit-3.14",
    "system",
    "cover",
    "lint",
    "lint_setup_py",
    "blacken",
    "docs",
    "docfx",
    "format",
    "prerelease_deps",
    "core_deps_from_source",
    "mypy",
]

# Error if a python version is missing
nox.options.error_on_missing_interpreters = True


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
        *LINT_PATHS,
    )

    # 2. Check formatting
    session.run(
        "ruff",
        "format",
        "--check",
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",
        *LINT_PATHS,
    )

    session.run("flake8", "google", "tests")


# Use a python runtime which is available in the owlbot post processor here
# https://github.com/googleapis/synthtool/blob/master/docker/owlbot/python/Dockerfile
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
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",
        *LINT_PATHS,
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
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",  # Standard Black line length
        *LINT_PATHS,
    )

    # 3. Run Ruff to format code
    session.run(
        "ruff",
        "format",
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",  # Standard Black line length
        *LINT_PATHS,
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint_setup_py(session):
    """Verify that setup.py is valid (including RST check)."""
    session.install("setuptools", "docutils", "pygments")
    session.run("python", "setup.py", "check", "--restructuredtext", "--strict")


def install_unittest_dependencies(session, *constraints):
    standard_deps = UNIT_TEST_STANDARD_DEPENDENCIES + UNIT_TEST_DEPENDENCIES
    session.install(*standard_deps, *constraints)

    if UNIT_TEST_EXTERNAL_DEPENDENCIES:
        warnings.warn(
            "'unit_test_external_dependencies' is deprecated. Instead, please "
            "use 'unit_test_dependencies' or 'unit_test_local_dependencies'.",
            DeprecationWarning,
        )
        session.install(*UNIT_TEST_EXTERNAL_DEPENDENCIES, *constraints)

    if UNIT_TEST_LOCAL_DEPENDENCIES:
        session.install(*UNIT_TEST_LOCAL_DEPENDENCIES, *constraints)

    if UNIT_TEST_EXTRAS_BY_PYTHON:
        extras = UNIT_TEST_EXTRAS_BY_PYTHON.get(session.python, [])
    elif UNIT_TEST_EXTRAS:
        extras = UNIT_TEST_EXTRAS
    else:
        extras = []

    if extras:
        session.install("-e", f".[{','.join(extras)}]", *constraints)
    else:
        session.install("-e", ".", *constraints)

    # XXX Work around Kokoro image's older pip, which borks the OT install.
    session.run("pip", "install", "--upgrade", "pip")
    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )
    session.install("-e", ".[tracing]", "-c", constraints_path)
    # XXX: Dump installed versions to debug OT issue
    session.run("pip", "list")


@nox.session(python=ALL_PYTHON)
@nox.parametrize(
    "protobuf_implementation",
    ["python", "upb"],
)
def unit(session, protobuf_implementation):
    # Install all test dependencies, then install this package in-place.

    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )
    install_unittest_dependencies(session, "-c", constraints_path)

    # Run py.test against the unit tests.
    args = [
        "py.test",
        "-n",
        "auto",
        "-s",
        f"--junitxml=unit_{session.python}_sponge_log.xml",
        "--cov=google",
        "--cov=tests/unit",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",
        "--cov-fail-under=0",
    ]
    if not session.posargs:
        args.append(os.path.join("tests", "unit"))
    args.extend(session.posargs)

    session.run(
        *args,
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
        },
    )


@nox.session(python=DEFAULT_MOCK_SERVER_TESTS_PYTHON_VERSION)
def mockserver(session):
    # Install all test dependencies, then install this package in-place.

    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )
    standard_deps = (
        UNIT_TEST_STANDARD_DEPENDENCIES
        + UNIT_TEST_DEPENDENCIES
        + MOCK_SERVER_ADDITIONAL_DEPENDENCIES
    )
    session.install(*standard_deps, "-c", constraints_path)
    session.install("-e", ".", "-c", constraints_path)

    # Run py.test against the mockserver tests.
    session.run(
        "py.test",
        "--quiet",
        f"--junitxml=unit_{session.python}_sponge_log.xml",
        "--cov=google",
        "--cov=tests/unit",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",
        "--cov-fail-under=0",
        os.path.join("tests", "mockserver_tests"),
        *session.posargs,
    )


def install_systemtest_dependencies(session, *constraints):
    # Use pre-release gRPC for system tests.
    # Exclude version 1.52.0rc1 which has a known issue.
    # See https://github.com/grpc/grpc/issues/32163
    session.install("--pre", "grpcio!=1.52.0rc1")

    session.install(*SYSTEM_TEST_STANDARD_DEPENDENCIES, *constraints)

    if SYSTEM_TEST_EXTERNAL_DEPENDENCIES:
        session.install(*SYSTEM_TEST_EXTERNAL_DEPENDENCIES, *constraints)

    if SYSTEM_TEST_LOCAL_DEPENDENCIES:
        session.install("-e", *SYSTEM_TEST_LOCAL_DEPENDENCIES, *constraints)

    if SYSTEM_TEST_DEPENDENCIES:
        session.install("-e", *SYSTEM_TEST_DEPENDENCIES, *constraints)

    if SYSTEM_TEST_EXTRAS_BY_PYTHON:
        extras = SYSTEM_TEST_EXTRAS_BY_PYTHON.get(session.python, [])
    elif SYSTEM_TEST_EXTRAS:
        extras = SYSTEM_TEST_EXTRAS
    else:
        extras = []

    if extras:
        session.install("-e", f".[{','.join(extras)}]", *constraints)
    else:
        session.install("-e", ".", *constraints)


@nox.session(python=SYSTEM_TEST_PYTHON_VERSIONS)
@nox.parametrize(
    "protobuf_implementation,database_dialect",
    [
        ("python", "GOOGLE_STANDARD_SQL"),
        ("python", "POSTGRESQL"),
        ("upb", "GOOGLE_STANDARD_SQL"),
        ("upb", "POSTGRESQL"),
    ],
)
def system(session, protobuf_implementation, database_dialect):
    """Run the system test suite."""
    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )
    system_test_path = os.path.join("tests", "system.py")
    system_test_folder_path = os.path.join("tests", "system")

    # Check the value of `RUN_SYSTEM_TESTS` env var. It defaults to true.
    if os.environ.get("RUN_SYSTEM_TESTS", "true") == "false":
        session.skip("RUN_SYSTEM_TESTS is set to false, skipping")
    # Sanity check: Only run tests if the environment variable is set.
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "") and not os.environ.get(
        "SPANNER_EMULATOR_HOST", ""
    ):
        session.skip(
            "Credentials or emulator host must be set via environment variable"
        )
    if not (
        os.environ.get("SPANNER_EMULATOR_HOST") or protobuf_implementation == "python"
    ):
        session.skip(
            "Only run system tests on real Spanner with one protobuf implementation to speed up the build"
        )

    # Install pyopenssl for mTLS testing.
    if os.environ.get("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false") == "true":
        session.install("pyopenssl")

    system_test_exists = os.path.exists(system_test_path)
    system_test_folder_exists = os.path.exists(system_test_folder_path)
    # Sanity check: only run tests if found.
    if not system_test_exists and not system_test_folder_exists:
        session.skip("System tests were not found")

    install_systemtest_dependencies(session, "-c", constraints_path)

    # Run py.test against the system tests.
    if system_test_exists:
        args = [
            "py.test",
            "--quiet",
            "-o",
            "asyncio_mode=auto",
            f"--junitxml=system_{session.python}_sponge_log.xml",
        ]
        if not session.posargs:
            args.append(system_test_path)
        args.extend(session.posargs)

        session.run(
            *args,
            env={
                "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
                "SPANNER_DATABASE_DIALECT": database_dialect,
                "SKIP_BACKUP_TESTS": "true",
            },
        )
    elif system_test_folder_exists:
        # Run sync tests
        sync_args = [
            "py.test",
            "--quiet",
            "-o",
            "asyncio_mode=auto",
            f"--junitxml=system_{session.python}_sync_sponge_log.xml",
        ]
        if not session.posargs:
            sync_args.append(os.path.join("tests", "system"))
            sync_args.append("--ignore=tests/system/_async")
        else:
            sync_args.extend(session.posargs)

        session.run(
            *sync_args,
            env={
                "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
                "SPANNER_DATABASE_DIALECT": database_dialect,
                "SKIP_BACKUP_TESTS": "true",
            },
        )

        # Run async tests
        async_args = [
            "py.test",
            "--quiet",
            "-o",
            "asyncio_mode=auto",
            f"--junitxml=system_{session.python}_async_sponge_log.xml",
        ]
        if not session.posargs:
            async_args.append(os.path.join("tests", "system", "_async"))
        else:
            # If posargs are provided, only run if they match async tests
            # or just skip if they were already run in sync.
            # For simplicity, we only run async folder if no posargs.
            return

        session.run(
            *async_args,
            env={
                "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
                "SPANNER_DATABASE_DIALECT": database_dialect,
                "SKIP_BACKUP_TESTS": "true",
            },
        )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def cover(session):
    """Run the final coverage report.

    This outputs the coverage report aggregating coverage from the unit
    test runs (not system test runs), and then erases coverage data.
    """
    session.install("coverage", "pytest-cov")
    session.run("coverage", "report", "--show-missing", "--fail-under=98")

    session.run("coverage", "erase")


@nox.session(python="3.10")
def docs(session):
    """Build the docs for this library."""

    session.install("-e", ".[tracing]")
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

    session.install("-e", ".[tracing]")
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


@nox.session(python="3.14")
@nox.parametrize(
    "protobuf_implementation,database_dialect",
    [
        ("python", "GOOGLE_STANDARD_SQL"),
        ("python", "POSTGRESQL"),
        ("upb", "GOOGLE_STANDARD_SQL"),
        ("upb", "POSTGRESQL"),
    ],
)
def prerelease_deps(session, protobuf_implementation, database_dialect):
    """Run all tests with prerelease versions of dependencies installed."""

    # Install all dependencies
    session.install("-e", ".[all, tests, tracing]")
    unit_deps_all = UNIT_TEST_STANDARD_DEPENDENCIES + UNIT_TEST_EXTERNAL_DEPENDENCIES
    session.install(*unit_deps_all)
    system_deps_all = (
        SYSTEM_TEST_STANDARD_DEPENDENCIES + SYSTEM_TEST_EXTERNAL_DEPENDENCIES
    )
    session.install(*system_deps_all)

    # Because we test minimum dependency versions on the minimum Python
    # version, the first version we test with in the unit tests sessions has a
    # constraints file containing all dependencies and extras.
    with open(
        CURRENT_DIRECTORY / "testing" / f"constraints-{ALL_PYTHON[0]}.txt",
        encoding="utf-8",
    ) as constraints_file:
        constraints_text = constraints_file.read()

    # Ignore leading whitespace and comment lines.
    constraints_deps = [
        match.group(1)
        for match in re.finditer(
            r"^\s*([a-zA-Z0-9._-]+)", constraints_text, flags=re.MULTILINE
        )
    ]

    if constraints_deps:
        session.install(*constraints_deps)

    prerel_deps = [
        "protobuf",
        # dependency of grpc
        "six",
        "grpc-google-iam-v1",
        "googleapis-common-protos",
        "grpcio",
        "grpcio-status",
        "google-api-core",
        "google-auth",
        "proto-plus",
        "google-cloud-testutils",
        # dependencies of google-cloud-testutils"
        "click",
        # dependency of google-auth
        "cffi",
        "cryptography",
        "cachetools",
    ]

    for dep in prerel_deps:
        session.install("--pre", "--no-deps", "--upgrade", dep)

    # Remaining dependencies
    other_deps = [
        "requests",
    ]
    session.install(*other_deps)

    # Print out prerelease package versions
    session.run(
        "python", "-c", "import google.protobuf; print(google.protobuf.__version__)"
    )
    session.run("python", "-c", "import grpc; print(grpc.__version__)")
    session.run("python", "-c", "import google.auth; print(google.auth.__version__)")

    session.run(
        "py.test",
        "tests/unit",
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
            "SPANNER_DATABASE_DIALECT": database_dialect,
            "SKIP_BACKUP_TESTS": "true",
        },
    )

    system_test_path = os.path.join("tests", "system.py")
    system_test_folder_path = os.path.join("tests", "system")

    system_test_exists = os.path.exists(system_test_path)
    system_test_folder_exists = os.path.exists(system_test_folder_path)
    # Sanity check: only run tests if found.
    if not system_test_exists and not system_test_folder_exists:
        session.skip("System tests were not found")

    if os.environ.get("SPANNER_EMULATOR_HOST"):
        # Run tests against the emulator
        run_system = True
    elif protobuf_implementation == "python":
        # Run tests against real Spanner, but check creds first
        if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
            run_system = True
        else:
            session.log(
                "Skipping system tests because GOOGLE_APPLICATION_CREDENTIALS is not set"
            )
            run_system = False
    else:
        # Skip to speed up build (only run python implementation on real Spanner)
        session.log(
            f"Skipping system tests for protobuf={protobuf_implementation} on real Spanner to speed up build"
        )
        run_system = False

    if run_system:
        # Run py.test against the system tests.
        if system_test_exists:
            args = [
                "py.test",
                "--quiet",
                "-o",
                "asyncio_mode=auto",
                f"--junitxml=system_{session.python}_sponge_log.xml",
            ]
            if not session.posargs:
                args.append(system_test_path)
            args.extend(session.posargs)

            session.run(
                *args,
                env={
                    "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
                    "SPANNER_DATABASE_DIALECT": database_dialect,
                    "SKIP_BACKUP_TESTS": "true",
                },
            )
        elif system_test_folder_exists:
            # Run sync tests
            sync_args = [
                "py.test",
                "--quiet",
                "-o",
                "asyncio_mode=auto",
                f"--junitxml=system_{session.python}_sync_sponge_log.xml",
            ]
            if not session.posargs:
                sync_args.append(system_test_folder_path)
                sync_args.append(
                    f"--ignore={os.path.join(system_test_folder_path, '_async')}"
                )
            else:
                sync_args.extend(session.posargs)

            session.run(
                *sync_args,
                env={
                    "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
                    "SPANNER_DATABASE_DIALECT": database_dialect,
                    "SKIP_BACKUP_TESTS": "true",
                },
            )

            # Run async tests
            async_args = [
                "py.test",
                "--quiet",
                "-o",
                "asyncio_mode=auto",
                f"--junitxml=system_{session.python}_async_sponge_log.xml",
            ]
            if not session.posargs:
                async_args.append(os.path.join(system_test_folder_path, "_async"))
            else:
                # If posargs are provided, only run if they match async tests
                # or just skip if they were already run in sync.
                # For simplicity, we only run async folder if no posargs.
                return

            session.run(
                *async_args,
                env={
                    "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
                    "SPANNER_DATABASE_DIALECT": database_dialect,
                    "SKIP_BACKUP_TESTS": "true",
                },
            )


@nox.session(python=ALL_PYTHON)
def mypy(session):
    """Run the type checker."""
    session.skip("Mypy is not yet supported")
    # TODO(https://github.com/googleapis/gapic-generator-python/issues/2579):
    # use the latest version of mypy
    session.install(
        "mypy<1.16.0",
        "types-requests",
        "types-protobuf",
    )
    session.install(".")
    session.run(
        "mypy",
        "-p",
        "google",
        # "--check-untyped-defs",
        *session.posargs,
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
@nox.parametrize(
    "protobuf_implementation",
    ["python", "upb"],
)
def core_deps_from_source(session, protobuf_implementation):
    """Run all tests with core dependencies installed from source,
    rather than pulling the dependencies from PyPI.
    """

    # Install all dependencies
    session.install("-e", ".[omni]")

    # Install dependencies for the unit test environment
    unit_deps_all = (
        UNIT_TEST_STANDARD_DEPENDENCIES
        + UNIT_TEST_DEPENDENCIES
        + UNIT_TEST_EXTERNAL_DEPENDENCIES
    )
    session.install(*unit_deps_all)

    # Because we test minimum dependency versions on the minimum Python
    # version, the first version we test with in the unit tests sessions has a
    # constraints file containing all dependencies and extras.
    with open(
        CURRENT_DIRECTORY / "testing" / f"constraints-{ALL_PYTHON[0]}.txt",
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

    # TODO(https://github.com/googleapis/gapic-generator-python/issues/2358): `grpcio` and
    # `grpcio-status` should be added to the list below so that they are installed from source,
    # rather than PyPI.
    # TODO(https://github.com/googleapis/gapic-generator-python/issues/2357): `protobuf` should be
    # added to the list below so that it is installed from source, rather than PyPI
    # Note: If a dependency is added to the `core_dependencies_from_source` list,
    # the `prerel_deps` list in the `prerelease_deps` nox session should also be updated.
    core_dependencies_from_source = [
        "googleapis-common-protos",
        "google-api-core",
        "google-auth",
        "grpc-google-iam-v1",
        "proto-plus",
    ]

    # Locate the monorepo 'packages' directory containing core dependencies
    deps_dir = next(
        p / "packages" for p in CURRENT_DIRECTORY.parents if (p / "packages").is_dir()
    )

    # Batch the pip installation to avoid sequential overhead
    dep_paths = [str(deps_dir / dep) for dep in core_dependencies_from_source]

    session.install(*dep_paths, "--no-deps", "--ignore-installed")
    session.install("pytest-xdist")
    print(
        f"Installed {', '.join(core_dependencies_from_source)} locally from {deps_dir}"
    )

    session.run(
        "py.test",
        "-n",
        "auto",
        "tests/unit",
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
        },
    )
