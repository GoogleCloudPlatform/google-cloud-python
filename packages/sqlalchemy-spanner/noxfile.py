# -*- coding: utf-8 -*-
#
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import configparser
import os
import pathlib
import re
import shutil
import uuid

import nox

ALEMBIC_CONF = """
[alembic]
script_location = test_migration
prepend_sys_path = .
sqlalchemy.url = {}
[post_write_hooks]
[loggers]
keys = root,sqlalchemy,alembic
[handlers]
keys = console
[formatters]
keys = generic
[logger_root]
level = WARN
handlers = console
qualname =
[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine
[logger_alembic]
level = INFO
handlers =
qualname = alembic
[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic
[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
"""

UPGRADE_CODE = """def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )
    op.alter_column(
        'account',
        'name',
        existing_type=sa.String(70),
    )
    op.alter_column(
        'account',
        'description',
        existing_type=sa.Unicode(200),
        nullable=False,
    )
    """


RUFF_VERSION = "ruff==0.14.14"
LINT_PATHS = ["google", "tests", "noxfile.py", "setup.py", "samples"]
CURRENT_DIRECTORY = pathlib.Path(__file__).parent.absolute()
UNIT_TEST_STANDARD_DEPENDENCIES = [
    "mock",
    "pytest",
    "pytest-cov",
]

UNIT_TEST_EXTERNAL_DEPENDENCIES = [
    "setuptools",
    "opentelemetry-api",
    "opentelemetry-sdk",
    "opentelemetry-instrumentation",
]

UNIT_TEST_DEPENDENCIES = [
    "sqlalchemy>=2.0",
]

SYSTEM_TEST_STANDARD_DEPENDENCIES = [
    "mock",
    "pytest",
    "pytest-cov",
    "pytest-asyncio",
]

SYSTEM_TEST_EXTERNAL_DEPENDENCIES = [
    "opentelemetry-api",
    "opentelemetry-sdk",
    "opentelemetry-instrumentation",
]

MIGRATION_TEST_DEPENDENCIES = [
    "pytest",
    "alembic",
]

SQLALCHEMY_14_DEPENDENCIES = [
    "sqlalchemy>=1.4,<2.0",
    "alembic<1.20.0",
]

SQLALCHEMY_20_DEPENDENCIES = [
    "sqlalchemy>=2.0",
]

UNIT_TEST_PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13", "3.14", "3.15"]
ALL_PYTHON = list(UNIT_TEST_PYTHON_VERSIONS)
SYSTEM_TEST_PYTHON_VERSIONS = ["3.12"]
SYSTEM_COMPLIANCE_MIGRATION_TEST_PYTHON_VERSIONS = ["3.12", "3.14"]
DEFAULT_PYTHON_VERSION = "3.14"
DEFAULT_PYTHON_VERSION_FOR_SQLALCHEMY_20 = "3.15"


nox.options.sessions = [
    "system",
    "compliance_test_14",
    "compliance_test_20",
    "migration_test",
    "mockserver",
]


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
    session.run(
        "flake8",
        "google",
        "tests",
        "--max-line-length=88",
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint_setup_py(session):
    """Verify that setup.py is valid (including RST check)."""
    session.install("docutils", "pygments", "setuptools")
    session.run("python", "setup.py", "check", "--restructuredtext", "--strict")


@nox.session(python=SYSTEM_COMPLIANCE_MIGRATION_TEST_PYTHON_VERSIONS[0])
def compliance_test_14(session):
    """Run SQLAlchemy dialect compliance test suite."""
    config_file = f"test_compliance_14_{session.python}_{uuid.uuid4().hex[:6]}.cfg"

    # Check the value of `RUN_COMPLIANCE_TESTS` env var. It defaults to true.
    if os.environ.get("RUN_COMPLIANCE_TESTS", "true") == "false":
        session.skip("RUN_COMPLIANCE_TESTS is set to false, skipping")
    # Sanity check: Only run tests if the environment variable is set.
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "") and not os.environ.get(
        "SPANNER_EMULATOR_HOST", ""
    ):
        session.skip(
            "Credentials or emulator host must be set via environment variable"
        )

    try:
        session.install(*SYSTEM_TEST_STANDARD_DEPENDENCIES)
        session.install(".[tracing]", *SQLALCHEMY_14_DEPENDENCIES)
        session.run(
            "python",
            "create_test_database.py",
            config_file,
        )
        config = configparser.ConfigParser()
        config.read(config_file)
        db_url = config.get("db", "default")
        session.run(
            "py.test",
            f"--dburi={db_url}",
            "--cov=google.cloud.sqlalchemy_spanner",
            "--cov=tests",
            "--cov-append",
            "--cov-config=.coveragerc",
            "--cov-report=",
            "--cov-fail-under=0",
            "--asyncio-mode=auto",
            "tests/test_suite_14.py",
            *session.posargs,
            # Explicitly pass SQLALCHEMY_SPANNER_CONFIG in the subprocess environment
            # to ensure test workers read the session-specific config file rather than
            # falling back to a shared default test.cfg.
            env={
                "SQLALCHEMY_SILENCE_UBER_WARNING": "1",
                "SQLALCHEMY_SPANNER_CONFIG": config_file,
            },
        )
    finally:
        if pathlib.Path(config_file).exists():
            session.run(
                "python",
                "drop_test_database.py",
                config_file,
                success_codes=[0, 1],
            )


@nox.session(python=DEFAULT_PYTHON_VERSION_FOR_SQLALCHEMY_20)
def compliance_test_20(session):
    """Run SQLAlchemy dialect compliance test suite."""
    config_file = f"test_compliance_20_{session.python}_{uuid.uuid4().hex[:6]}.cfg"

    # Check the value of `RUN_COMPLIANCE_TESTS` env var. It defaults to true.
    if os.environ.get("RUN_COMPLIANCE_TESTS", "true") == "false":
        session.skip("RUN_COMPLIANCE_TESTS is set to false, skipping")

    # Sanity check: Only run tests if the environment variable is set.
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "") and not os.environ.get(
        "SPANNER_EMULATOR_HOST", ""
    ):
        session.skip(
            "Credentials or emulator host must be set via environment variable"
        )

    try:
        session.install(*SYSTEM_TEST_STANDARD_DEPENDENCIES)
        session.install("-e", ".", "--force-reinstall")
        session.run(
            "python",
            "create_test_database.py",
            config_file,
        )
        config = configparser.ConfigParser()
        config.read(config_file)
        db_url = config.get("db", "default")

        session.install(*SQLALCHEMY_20_DEPENDENCIES)

        session.run(
            "py.test",
            f"--dburi={db_url}",
            "--cov=google.cloud.sqlalchemy_spanner",
            "--cov=tests",
            "--cov-append",
            "--cov-config=.coveragerc",
            "--cov-report=",
            "--cov-fail-under=0",
            "--asyncio-mode=auto",
            "tests/test_suite_20.py",
            *session.posargs,
            env={"SQLALCHEMY_SPANNER_CONFIG": config_file},
        )
    finally:
        if pathlib.Path(config_file).exists():
            session.run(
                "python",
                "drop_test_database.py",
                config_file,
                success_codes=[0, 1],
            )


@nox.session(python=DEFAULT_PYTHON_VERSION_FOR_SQLALCHEMY_20)
def mockserver(session):
    """Run mockserver tests."""
    # Run SQLAlchemy dialect tests using an in-mem mocked Spanner server.
    session.install(
        *UNIT_TEST_STANDARD_DEPENDENCIES,
        *UNIT_TEST_EXTERNAL_DEPENDENCIES,
        *UNIT_TEST_DEPENDENCIES,
    )
    session.install(".")
    session.run(
        "python",
        "create_test_config.py",
        "my-project",
        "my-instance",
        "my-database",
        "none",
        "AnonymousCredentials",
        "localhost",
        "9999",
    )
    session.run(
        "py.test",
        "--quiet",
        os.path.join("tests", "mockserver_tests"),
        *session.posargs,
    )


@nox.session
@nox.parametrize(
    ("python", "extra_dependencies"),
    [
        (
            SYSTEM_COMPLIANCE_MIGRATION_TEST_PYTHON_VERSIONS[0],
            SQLALCHEMY_14_DEPENDENCIES,
        ),
        (
            DEFAULT_PYTHON_VERSION_FOR_SQLALCHEMY_20,
            SQLALCHEMY_20_DEPENDENCIES,
        ),
    ],
    ids=["14", "20"],
)
def migration_test(session, extra_dependencies):
    """Test migrations with SQLAlchemy and Alembic."""
    _run_migration_test(session, extra_dependencies=extra_dependencies)


def _run_migration_test(session, extra_dependencies=()):
    """Migrate with SQLAlchemy and Alembic and check the result."""
    import glob
    import os
    import shutil

    config_file = f"test_migration_{session.python}_{uuid.uuid4().hex[:6]}.cfg"

    session.install(*MIGRATION_TEST_DEPENDENCIES, *extra_dependencies, ".")

    try:
        session.run(
            "python",
            "create_test_database.py",
            config_file,
        )

        config = configparser.ConfigParser()
        config_path = pathlib.Path(config_file)
        if config_path.exists():
            config.read(config_path)
        else:
            config.read("setup.cfg")
        db_url = config.get("db", "default")

        session.run("alembic", "init", "test_migration")

        # setting testing configurations
        alembic_ini = pathlib.Path("alembic.ini")
        if alembic_ini.exists():
            alembic_ini.unlink()
        alembic_ini.write_text(ALEMBIC_CONF.format(db_url))

        session.run("alembic", "revision", "-m", "migration_for_test")
        files = glob.glob("test_migration/versions/*.py")

        # updating the upgrade-script code
        with open(files[0], "rb") as f:
            script_code = f.read().decode()

        script_code = script_code.replace(
            """def upgrade() -> None:\n    pass""", UPGRADE_CODE
        )
        with open(files[0], "wb") as f:
            f.write(script_code.encode())

        env_py = pathlib.Path("test_migration/env.py")
        if env_py.exists():
            env_py.unlink()
        shutil.copyfile("test_migration_env.py", env_py)

        # running the test migration
        session.run("alembic", "upgrade", "head")

    finally:
        # clearing the migration data
        if alembic_ini.exists():
            alembic_ini.unlink()
        test_migration_dir = pathlib.Path("test_migration")
        if test_migration_dir.exists():
            shutil.rmtree(test_migration_dir)

        if config_path.exists():
            session.run(
                "python",
                "drop_test_database.py",
                config_file,
                success_codes=[0, 1],
            )


@nox.session(python=ALL_PYTHON)
@nox.parametrize("test_type", ["unit", "mockserver"])
def unit(session, test_type):
    """Run unit tests."""

    if (
        test_type == "mockserver"
        and session.python != DEFAULT_PYTHON_VERSION_FOR_SQLALCHEMY_20
    ):
        session.skip(
            f"mockserver tests only run on python {DEFAULT_PYTHON_VERSION_FOR_SQLALCHEMY_20}"
        )

    if test_type == "mockserver":
        mockserver(session)
        return

    if test_type == "unit":
        # Run SQLAlchemy dialect unit tests with pytest-cov if COVERAGE_FILE is set.
        session.install(
            *UNIT_TEST_STANDARD_DEPENDENCIES,
            *UNIT_TEST_EXTERNAL_DEPENDENCIES,
            *UNIT_TEST_DEPENDENCIES,
        )
        session.install(".")
        pytest_args = ["--quiet", os.path.join("tests/unit")]
        if "COVERAGE_FILE" in os.environ:
            pytest_args.extend(
                [
                    "--cov=google.cloud.sqlalchemy_spanner",
                    "--cov-config=.coveragerc",
                ]
            )
        session.run("py.test", *pytest_args, *session.posargs)
        return


@nox.session(python=SYSTEM_COMPLIANCE_MIGRATION_TEST_PYTHON_VERSIONS)
@nox.parametrize(
    "test_type",
    ["system", "compliance_14", "compliance_20", "migration_14", "migration_20"],
)
def system(session, test_type):
    """Run SQLAlchemy dialect system test suite."""
    if (
        test_type in ["compliance_14", "migration_14"]
        and session.python != SYSTEM_COMPLIANCE_MIGRATION_TEST_PYTHON_VERSIONS[0]
    ):
        session.skip(
            f"SQLAlchemy 1.4-based tests configured to run exclusively on {SYSTEM_COMPLIANCE_MIGRATION_TEST_PYTHON_VERSIONS[0]}"
        )
    if (
        test_type in ["compliance_20", "migration_20"]
        and session.python != DEFAULT_PYTHON_VERSION_FOR_SQLALCHEMY_20
    ):
        session.skip(
            f"SQLAlchemy 2.0-based tests configured to run exclusively on {DEFAULT_PYTHON_VERSION_FOR_SQLALCHEMY_20}"
        )

    if test_type == "compliance_14":
        return compliance_test_14(session)
    elif test_type == "compliance_20":
        return compliance_test_20(session)
    elif test_type == "migration_14":
        return _run_migration_test(
            session, extra_dependencies=SQLALCHEMY_14_DEPENDENCIES
        )
    elif test_type == "migration_20":
        return _run_migration_test(
            session, extra_dependencies=SQLALCHEMY_20_DEPENDENCIES
        )

    config_file = f"test_{test_type}_{session.python}_{uuid.uuid4().hex[:6]}.cfg"

    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "") and not os.environ.get(
        "SPANNER_EMULATOR_HOST", ""
    ):
        session.skip(
            "Credentials or emulator host must be set via environment variable"
        )

    if os.environ.get("RUN_SYSTEM_TESTS", "true") == "false" and not os.environ.get(
        "SPANNER_EMULATOR_HOST", ""
    ):
        session.skip("RUN_SYSTEM_TESTS is set to false, skipping")

    if test_type == "system" and session.python not in SYSTEM_TEST_PYTHON_VERSIONS:
        session.skip("Standard system tests configured to run exclusively on 3.12")

    try:
        if test_type == "system":
            session.install(*SYSTEM_TEST_STANDARD_DEPENDENCIES)
            session.install(".[tracing]")
            session.install(*SYSTEM_TEST_EXTERNAL_DEPENDENCIES)
            session.run(
                "python",
                "create_test_database.py",
                config_file,
            )
            config = configparser.ConfigParser()
            config.read(config_file)
            db_url = config.get("db", "default")
            session.install(*SQLALCHEMY_20_DEPENDENCIES)
            session.run(
                "py.test",
                f"--dburi={db_url}",
                "--quiet",
                os.path.join("tests", "system"),
                *session.posargs,
                env={"SQLALCHEMY_SPANNER_CONFIG": config_file},
            )
    finally:
        if pathlib.Path(config_file).exists():
            session.run(
                "python",
                "drop_test_database.py",
                config_file,
                success_codes=[0, 1],
            )


@nox.session(python=SYSTEM_COMPLIANCE_MIGRATION_TEST_PYTHON_VERSIONS)
@nox.parametrize(
    "test_type",
    ["compliance_14", "compliance_20"],
)
def compliance(session, test_type):
    """Run SQLAlchemy dialect compliance test suite."""
    system(session, test_type=test_type)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def mypy(session):
    """Run the type checker."""
    # TODO(https://github.com/googleapis/google-cloud-python/issues/17047):
    # Add typehints to this package.
    session.skip("mypy tests are not yet supported")


@nox.session(python=DEFAULT_PYTHON_VERSION)
@nox.parametrize(
    "protobuf_implementation",
    ["python", "upb"],
)
def core_deps_from_source(session, protobuf_implementation):
    """Run all tests with core dependencies installed from source"""
    session.install(
        *UNIT_TEST_STANDARD_DEPENDENCIES,
        *UNIT_TEST_EXTERNAL_DEPENDENCIES,
        *UNIT_TEST_DEPENDENCIES,
    )
    session.install(".")

    core_dependencies_from_source = [
        "googleapis-common-protos",
        "google-api-core",
        "google-auth",
        "grpc-google-iam-v1",
        "proto-plus",
    ]

    deps_dir = next(
        p / "packages" for p in CURRENT_DIRECTORY.parents if (p / "packages").is_dir()
    )

    local_paths = [
        str(deps_dir / dep)
        for dep in core_dependencies_from_source
        if (deps_dir / dep).exists()
    ]
    if local_paths:
        session.install(*local_paths, "--no-deps", "--ignore-installed")
        print(
            f"Installed {', '.join(core_dependencies_from_source)} locally from {deps_dir}"
        )

    tests_path = os.path.join("tests", "unit")
    session.run(
        "py.test",
        "--quiet",
        tests_path,
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
    session.install(".")

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
        os.path.join("tests", "unit"),
        *session.posargs,
        env={
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION": protobuf_implementation,
        },
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def cover(session):
    """Run the final coverage report."""
    session.install("coverage", "pytest-cov")
    if not pathlib.Path(".coverage").exists():
        session.skip("No coverage data found to report.")
    session.run("coverage", "report", "--show-missing", "--fail-under=0")
    session.run("coverage", "erase")


@nox.session(python="3.10")
def docs(session):
    """Build the docs for this library."""
    session.skip("There is no docs directory, thus docs builds do not run")


@nox.session(python="3.10")
def docfx(session):
    """Build the docfx yaml files for this library."""
    session.skip("There is no docs directory, thus docfx builds do not run")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def format(session):
    """Run ruff to sort imports and format code."""
    session.install(RUFF_VERSION)

    # Run Ruff to fix imports
    session.run(
        "ruff",
        "check",
        "--select",
        "I",
        "--fix",
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",
        *LINT_PATHS,
    )

    # Run Ruff to format code
    session.run(
        "ruff",
        "format",
        f"--target-version=py{ALL_PYTHON[0].replace('.', '')}",
        "--line-length=88",
        *LINT_PATHS,
    )
