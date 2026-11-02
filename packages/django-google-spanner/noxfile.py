# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from __future__ import absolute_import

import os
import pathlib
import re
import shutil

import nox

RUFF_VERSION = "ruff==0.14.14"
LINT_PATHS = [
    "docs",
    "django_spanner",
    "tests",
    "noxfile.py",
    "setup.py",
]

MOCKSERVER_TEST_PYTHON_VERSION = "3.12"
DEFAULT_PYTHON_VERSION = "3.14"

UNIT_TEST_PYTHON_VERSIONS = [
    "3.10",
    "3.11",
    "3.12",
    "3.13",
    "3.14",
    "3.15",
]
ALL_PYTHON = list(UNIT_TEST_PYTHON_VERSIONS)

SYSTEM_TEST_PYTHON_VERSIONS = ALL_PYTHON

DJANGO_VERSIONS = ["5.2", "6.0"]

UNIT_TEST_STANDARD_DEPENDENCIES = [
    "mock",
    "pytest",
    "pytest-cov",
    "coverage",
]

UNIT_TEST_EXTERNAL_DEPENDENCIES = [
    "setuptools",
    "mock-import",
    "opentelemetry-api",
    "opentelemetry-sdk",
    "opentelemetry-instrumentation",
]

UNIT_TEST_DEPENDENCIES = [
    "django>=5.2,<6.1",
    "sqlparse>=0.3.1",
]

UNIT_TEST_MOCKSERVER_DEPENDENCIES = [
    "google-cloud-spanner>=3.70.0",
    "sqlparse>=0.4.4",
]

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

    session.run("flake8", "django_spanner", "tests")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def blacken(session):
    """(Deprecated) Legacy session. Please use 'nox -s format'."""
    session.log(
        "WARNING: The 'blacken' session is deprecated and will be removed in a future release. Please use 'nox -s format' in the future."
    )
    session.install(RUFF_VERSION)
    session.run(
        "ruff",
        "format",
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",
        *LINT_PATHS,
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint_setup_py(session):
    """Verify that setup.py is valid (including RST check)."""
    session.install("docutils", "pygments", "setuptools")
    session.run("python", "setup.py", "check", "--restructuredtext", "--strict")


def default(session, django_version="5.2"):
    # Django 6.0 dropped support for Python 3.10 and 3.11 (requires Python >= 3.12)
    if django_version == "6.0" and session.python in ("3.10", "3.11"):
        session.skip(f"Django {django_version} requires Python >= 3.12")

    # Target specific Django version
    django_dep = (
        f"django~={django_version}.0" if django_version == "6.0" else "django~=5.2.0"
    )

    # Install all test dependencies, then install this package in-place.
    session.install(
        *UNIT_TEST_STANDARD_DEPENDENCIES,
        *UNIT_TEST_EXTERNAL_DEPENDENCIES,
        *UNIT_TEST_MOCKSERVER_DEPENDENCIES,
        django_dep,
    )
    session.install("-e", ".")

    # Run py.test against unit and mockserver tests.
    session.run(
        "py.test",
        "--quiet",
        "--cov=django_spanner",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",
        "--cov-fail-under=0",
        os.path.join("tests", "unit"),
        os.path.join("tests", "mockserver_tests"),
        *session.posargs,
    )


@nox.session(python=ALL_PYTHON)
@nox.parametrize("django", DJANGO_VERSIONS)
def unit(session, django):
    """Run the unit test suite across Django versions."""
    default(session, django_version=django)


@nox.session(python=MOCKSERVER_TEST_PYTHON_VERSION)
@nox.parametrize("django", DJANGO_VERSIONS)
def mockserver(session, django):
    """Run mockserver tests across Django versions."""
    default(session, django_version=django)


def system_test(session):
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

    system_test_exists = os.path.exists(system_test_path)
    system_test_folder_exists = os.path.exists(system_test_folder_path)
    # Sanity check: only run tests if found.
    if not system_test_exists and not system_test_folder_exists:
        session.skip("System tests were not found")

    # Use pre-release gRPC for system tests.
    session.install("--pre", "grpcio")

    # Install all test dependencies, then install this package into the
    # virtualenv's dist-packages.
    session.install(
        "django~=5.2",
        "mock",
        "pytest",
        "google-cloud-testutils",
        "-c",
        constraints_path,
    )
    session.install("-e", ".[tracing]", "-c", constraints_path)
    # Run py.test against the system tests.
    if system_test_exists:
        session.run("py.test", "--quiet", system_test_path, *session.posargs)
    if system_test_folder_exists:
        session.run("py.test", "--quiet", system_test_folder_path, *session.posargs)


@nox.session(python=SYSTEM_TEST_PYTHON_VERSIONS)
def system(session):
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16099):
    # System tests were disabled in the split repo to speed up the build process.
    # See: https://github.com/googleapis/python-spanner-django/pull/929.
    session.skip("System tests are temporarily disabled.")

    print("System tests with django 5.2")
    system_test(session)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def cover(session):
    """Run the final coverage report.

    This outputs the coverage report aggregating coverage from the unit
    test runs (not system test runs), and then erases coverage data.
    """
    session.install("coverage", "pytest-cov")
    session.run("coverage", "report", "--show-missing")

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
        "django==5.2",
    )

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    # Warnings as errors is disabled for `sphinx-build` because django module
    # has warnings.
    session.run(
        "sphinx-build",
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
        "django==5.2",
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
def mypy(session):
    """Run the type checker."""
    # TODO(https://github.com/googleapis/google-cloud-python/issues/17047):
    # Add typehints to this package.
    session.skip("Typehints and thus mypy are not yet supported.")

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
        "django_spanner",
        *session.posargs,
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
@nox.parametrize(
    "protobuf_implementation",
    ["python", "upb"],
)
def core_deps_from_source(session, protobuf_implementation):
    """Run all tests with core dependencies installed from source
    rather than pulling the dependencies from PyPI.
    """
    session.install(
        *UNIT_TEST_STANDARD_DEPENDENCIES,
        *UNIT_TEST_EXTERNAL_DEPENDENCIES,
        *UNIT_TEST_DEPENDENCIES,
    )
    session.install("-e", ".")

    core_dependencies_from_source = [
        "googleapis-common-protos",
        "google-api-core",
        "google-auth",
        "grpc-google-iam-v1",
        "proto-plus",
        "google-cloud-spanner",
    ]

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
        "--quiet",
        "--cov=django_spanner",
        "--cov=tests.unit",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",
        "--cov-fail-under=0",
        os.path.join("tests", "unit"),
        *session.posargs,
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
        },
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
@nox.parametrize(
    "protobuf_implementation",
    ["python", "upb"],
)
def prerelease_deps(session, protobuf_implementation):
    """Run all tests with prerelease versions of dependencies installed."""
    session.install(
        *UNIT_TEST_STANDARD_DEPENDENCIES,
        *UNIT_TEST_EXTERNAL_DEPENDENCIES,
        *UNIT_TEST_DEPENDENCIES,
    )
    session.install("-e", ".")

    prerel_deps = [
        "googleapis-common-protos",
        "google-api-core",
        "google-auth",
        "grpc-google-iam-v1",
        "grpcio>=1.75.1" if session.python >= "3.12" else "grpcio<=1.62.2",
        "grpcio-status",
        "protobuf",
        "proto-plus",
        "google-cloud-spanner",
    ]

    deps_dir = next(
        p / "packages" for p in CURRENT_DIRECTORY.parents if (p / "packages").is_dir()
    )

    parsed_deps = {
        dep: re.match(r"^([a-zA-Z0-9_-]+)", dep).group(1) for dep in prerel_deps
    }

    local_paths = []
    pypi_deps = []

    for dep, pkg_name in parsed_deps.items():
        if (deps_dir / pkg_name).exists():
            local_paths.append(str(deps_dir / pkg_name))
        else:
            pypi_deps.append(dep)

    if local_paths:
        session.install(*local_paths, "--no-deps", "--ignore-installed")
    if pypi_deps:
        session.install(*pypi_deps, "--pre", "--no-deps", "--ignore-installed")

    package_namespaces = {
        "google-api-core": "google.api_core",
        "google-auth": "google.auth",
        "grpcio": "grpc",
        "protobuf": "google.protobuf",
        "proto-plus": "proto",
        "google-cloud-spanner": "google.cloud.spanner",
    }

    for dep, pkg_name in parsed_deps.items():
        print(f"Installed {dep}")
        version_namespace = package_namespaces.get(pkg_name)

        if version_namespace:
            session.run(
                "python",
                "-c",
                f"import {version_namespace}; print({version_namespace}.__version__)",
            )

    session.run(
        "py.test",
        "--quiet",
        "--cov=django_spanner",
        "--cov=tests.unit",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",
        "--cov-fail-under=0",
        os.path.join("tests", "unit"),
        *session.posargs,
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
        },
    )


@nox.session
def format(session: nox.sessions.Session) -> None:
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
