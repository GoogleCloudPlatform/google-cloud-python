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
import warnings
from typing import Dict, List

import nox

RUFF_VERSION = "ruff==0.14.14"

LINT_PATHS = ["docs", "google", "tests", "noxfile.py", "setup.py"]

# Add samples to the list of directories to format if the directory exists.
if os.path.isdir("samples"):
    LINT_PATHS.append("samples")

ALL_PYTHON = [
    "3.10",
    "3.11",
    "3.12",
    "3.13",
    "3.14",
    "3.15",
]

DEFAULT_PYTHON_VERSION = "3.14"

PREVIEW_PYTHON_VERSION = "3.15"

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

if (CURRENT_DIRECTORY / "testing").exists():
    LOWER_BOUND_CONSTRAINTS_FILE = (
        CURRENT_DIRECTORY / "testing" / f"constraints-{ALL_PYTHON[0]}.txt"
    )
else:
    LOWER_BOUND_CONSTRAINTS_FILE = CURRENT_DIRECTORY / "constraints.txt"
PACKAGE_NAME = "google-cloud-storage"

UNIT_TEST_STANDARD_DEPENDENCIES = [
    "mock",
    "asyncmock",
    "pytest",
    "pytest-cov",
    "pytest-asyncio",
]
UNIT_TEST_EXTERNAL_DEPENDENCIES: List[str] = []
UNIT_TEST_LOCAL_DEPENDENCIES: List[str] = []
UNIT_TEST_DEPENDENCIES: List[str] = [
    "brotli",
    "grpcio",
    "grpc-google-iam-v1",
    "opentelemetry-api",
    "opentelemetry-sdk",
]
UNIT_TEST_EXTRAS: List[str] = []
UNIT_TEST_EXTRAS_BY_PYTHON: Dict[str, List[str]] = {}

SYSTEM_TEST_PYTHON_VERSIONS: List[str] = ALL_PYTHON
SYSTEM_TEST_STANDARD_DEPENDENCIES = [
    "mock",
    "pytest",
    "google-cloud-testutils",
]
SYSTEM_TEST_EXTERNAL_DEPENDENCIES: List[str] = []
SYSTEM_TEST_LOCAL_DEPENDENCIES: List[str] = []
SYSTEM_TEST_DEPENDENCIES: List[str] = []
SYSTEM_TEST_EXTRAS: List[str] = []
SYSTEM_TEST_EXTRAS_BY_PYTHON: Dict[str, List[str]] = {}

nox.options.sessions = [
    "unit",
    "system",
    "cover",
    "lint",
    "lint_setup_py",
    "blacken",
    "docs",
]

# Error if a python version is missing
nox.options.error_on_missing_interpreters = True


@nox.session(python=ALL_PYTHON)
def mypy(session):
    """Run the type checker."""

    # TODO(https://github.com/googleapis/google-cloud-python/issues/13362):
    # Enable mypy once this repo has been updated for mypy evaluation.
    session.skip("Skip mypy since this library is not yet updated for mypy evaluation")

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
        "google",
        *session.posargs,
    )


@nox.session
def update_lower_bounds(session):
    """Update lower bounds in constraints.txt to match setup.py"""
    session.install("google-cloud-testutils")
    session.install(".")

    session.run(
        "lower-bound-checker",
        "update",
        "--package-name",
        PACKAGE_NAME,
        "--constraints-file",
        str(LOWER_BOUND_CONSTRAINTS_FILE),
    )


@nox.session
def check_lower_bounds(session):
    """Check lower bounds in setup.py are reflected in constraints file"""
    session.install("google-cloud-testutils")
    session.install(".")

    session.run(
        "lower-bound-checker",
        "check",
        "--package-name",
        PACKAGE_NAME,
        "--constraints-file",
        str(LOWER_BOUND_CONSTRAINTS_FILE),
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
        os.path.join("tests", "unit"),
        os.path.join("tests", "resumable_media", "unit"),
        *session.posargs,
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
        },
    )


def install_systemtest_dependencies(session, *constraints):
    if session.python >= "3.12":
        session.install("--pre", "grpcio>=1.75.1")
    else:
        session.install("--pre", "grpcio<=1.62.2")

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
    "test_type",
    ["system", "conformance", "conformance_bidi"],
)
def system(session, test_type):
    if test_type == "conformance":
        conftest_retry(session)
        return
    if test_type == "conformance_bidi":
        conftest_retry_bidi(session)
        return

    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )
    """Run the system test suite."""
    rerun_count = 0

    # Check the value of `RUN_SYSTEM_TESTS` env var. It defaults to true.
    if os.environ.get("RUN_SYSTEM_TESTS", "true") == "false":
        session.skip("RUN_SYSTEM_TESTS is set to false, skipping")
    # Environment check: Only run tests if the environment variable is set.
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""):
        session.skip(
            "Credentials must be set via environment variable GOOGLE_APPLICATION_CREDENTIALS"
        )
    # mTLS tests requires pyopenssl.
    if os.environ.get("GOOGLE_API_USE_CLIENT_CERTIFICATE", "") == "true":
        session.install("pyopenssl")
    # Check if endpoint is being overriden for rerun_count
    if (
        os.getenv("API_ENDPOINT_OVERRIDE", "https://storage.googleapis.com")
        != "https://storage.googleapis.com"
    ):
        rerun_count = 3

    # Use pre-release gRPC for system tests.
    # TODO: Remove ban of 1.52.0rc1 once grpc/grpc#31885 is resolved.
    session.install("--pre", "grpcio!=1.52.0rc1")

    # Install all test dependencies, then install this package into the
    # virtualenv's dist-packages.
    # 2021-05-06: defer installing 'google-cloud-*' to after this package,
    #             in order to work around Python 2.7 googolapis-common-protos
    #             issue.
    session.install(
        "mock",
        "pytest",
        "pytest-rerunfailures",
        "pytest-asyncio",
        "-c",
        constraints_path,
    )
    session.install("-e", ".", "-c", constraints_path)
    session.install(
        "google-cloud-testutils",
        "google-cloud-iam",
        "google-cloud-pubsub",
        "google-cloud-kms",
        "brotli",
        "-c",
        constraints_path,
    )

    # Run py.test against the system tests.
    session.run(
        "py.test",
        "--quiet",
        f"--junitxml=system_{session.python}_sponge_log.xml",
        "--reruns={}".format(rerun_count),
        os.path.join("tests", "system"),
        os.path.join("tests", "resumable_media", "system"),
        *session.posargs,
    )


@nox.session(python=SYSTEM_TEST_PYTHON_VERSIONS)
def conftest_retry(session):
    """Run the retry conformance test suite."""
    json_conformance_tests = "tests/conformance/test_conformance.py"
    # Environment check: only run tests if found.
    if not os.path.exists(json_conformance_tests):
        session.skip("Conformance tests were not found")

    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )

    # Install all test dependencies and pytest plugin to run tests in parallel.
    # Then install this package in-place.
    session.install(
        "pytest",
        "pytest-xdist",
        "-c",
        constraints_path,
    )
    session.install("-e", ".", "-c", constraints_path)

    # Run #CPU processes in parallel if no test session arguments are passed in.
    if session.posargs:
        test_cmd = [
            "pytest",
            "-vv",
            "-s",
            json_conformance_tests,
            *session.posargs,
        ]
    else:
        test_cmd = ["pytest", "-vv", "-s", "-n", "auto", json_conformance_tests]

    # Run pytest against the conformance tests.
    session.run(*test_cmd, env={"DOCKER_API_VERSION": "1.39"})


@nox.session(python=SYSTEM_TEST_PYTHON_VERSIONS)
def conftest_retry_bidi(session):
    """Run the retry conformance test suite."""

    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )

    # Install all test dependencies and pytest plugin to run tests in parallel.
    # Then install this package in-place.
    session.install(
        "pytest",
        "pytest-xdist",
        "pytest-asyncio",
        "grpcio",
        "grpcio-status",
        "grpc-google-iam-v1",
        "-c",
        constraints_path,
    )
    session.install("-e", ".", "-c", constraints_path)

    bidi_tests = [
        "tests/conformance/test_bidi_reads.py",
        "tests/conformance/test_bidi_writes.py",
    ]
    for test_file in bidi_tests:
        session.run(
            "pytest",
            "-vv",
            "-s",
            test_file,
            env={"DOCKER_API_VERSION": "1.39"},
        )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def cover(session):
    """Run the final coverage report.

    This outputs the coverage report aggregating coverage from the unit
    test runs (not system test runs), and then erases coverage data.
    """
    session.install("coverage", "pytest-cov")
    session.run("coverage", "report", "--show-missing", "--fail-under=100")

    session.run("coverage", "erase")


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
        "-T",  # show full traceback on exception
        "-N",  # no colors
        "-b",
        "html",  # builder
        "-d",
        os.path.join("docs", "_build", "doctrees", ""),  # cache directory
        # paths to build:
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


@nox.session(python=PREVIEW_PYTHON_VERSION)
@nox.parametrize(
    "protobuf_implementation",
    ["python", "upb"],
)
def prerelease_deps(session, protobuf_implementation):
    """Run all tests with prerelease versions of dependencies installed."""

    # Environment check: Only run tests if the environment variable is set.
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""):
        session.skip(
            "Credentials must be set via environment variable GOOGLE_APPLICATION_CREDENTIALS"
        )

    # Install dependencies for the unit test environment
    unit_deps_all = UNIT_TEST_STANDARD_DEPENDENCIES + UNIT_TEST_EXTERNAL_DEPENDENCIES
    session.install(*unit_deps_all)

    # Install dependencies needed for system tests
    session.install(
        "google-cloud-pubsub",
        "google-cloud-kms",
        "google-cloud-testutils",
        "google-cloud-iam",
    )

    # Install all dependencies
    session.install("-e", ".[protobuf, tracing]")

    prerel_deps = [
        "google-api-core",
        # Exclude google-auth 3.0.0.dev0 which was yanked
        "google-auth!=3.0.0.dev0",
        "google-cloud-core",
        "google-crc32c",
        "google-resumable-media",
        "opentelemetry-api",
        "protobuf",
    ]

    package_namespaces = {
        "google-api-core": "google.api_core",
        "google-auth": "google.auth",
        "google-cloud-core": "google.cloud.version",
        "opentelemetry-api": "opentelemetry.version",
        "protobuf": "google.protobuf",
    }

    for dep in prerel_deps:
        session.install("--pre", "--no-deps", "--upgrade", dep)
        print(f"Installed {dep}")

        version_namespace = package_namespaces.get(dep)

        if version_namespace:
            session.run(
                "python",
                "-c",
                f"import {version_namespace}; print({version_namespace}.__version__)",
            )
    # Remaining dependencies
    other_deps = ["requests", "pyopenssl"]
    session.install(*other_deps)

    session.run(
        "py.test",
        "tests/unit",
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
        },
    )

    session.run(
        "py.test",
        "--verbose",
        f"--junitxml=system_{session.python}_sponge_log.xml",
        os.path.join("tests", "system"),
        *session.posargs,
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
        },
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
@nox.session(python=DEFAULT_PYTHON_VERSION)
@nox.parametrize(
    "protobuf_implementation",
    ["python", "upb"],
)
def core_deps_from_source(session, protobuf_implementation):
    """Run all tests with core dependencies installed from source
    rather than pulling the dependencies from PyPI.
    """

    # Install all dependencies
    session.install("-e", ".")

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
    print(
        f"Installed {', '.join(core_dependencies_from_source)} locally from {deps_dir}"
    )

    session.run(
        "py.test",
        "tests/unit",
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
        },
    )
