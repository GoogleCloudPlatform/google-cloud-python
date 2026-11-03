# Copyright 2017, Google LLC
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

# Helpful notes for local usage:
#   unset PYENV_VERSION
#   pyenv local 3.14.1 3.13.10 3.12.11 3.11.4 3.10.12
#   PIP_INDEX_URL=https://pypi.org/simple nox

from __future__ import absolute_import

import os
import shutil
import sys
import tempfile
import typing
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from os import path
from pathlib import Path

import nox  # type: ignore

nox.options.error_on_missing_interpreters = True


showcase_version = os.environ.get("SHOWCASE_VERSION", "0.44.2")
ADS_TEMPLATES = path.join(path.dirname(__file__), "gapic", "ads-templates")
CURRENT_DIRECTORY = Path(__file__).parent.absolute()
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
LINT_PATHS = ["docs", "gapic", "tests", "test_utils", "noxfile.py", "setup.py"]
# Ruff uses globs for excludes (different from Black's regex)
# .*golden.* -> *golden*
# .*pb2.py -> *pb2.py
RUFF_EXCLUDES = "*golden*,*pb2.py,*pb2.pyi"

ALL_PYTHON = (
    "3.10",
    "3.11",
    "3.12",
    "3.13",
    "3.14",
    "3.15",
)

NEWEST_PYTHON = ALL_PYTHON[-2]


@nox.session(python=ALL_PYTHON)
def unit(session):
    """Run the unit test suite."""
    session.install(
        # TODO(https://github.com/googleapis/gapic-generator-python/issues/2478):
        # Temporarily pin coverage to 7.11.0
        # See https://github.com/nedbat/coveragepy/issues/2077
        "coverage<=7.11.0",
        "pytest-cov",
        "pytest",
        "pytest-xdist",
        "pyfakefs",
        "grpcio-status",
        "proto-plus",
    )
    session.install("-e", ".")
    session.run(
        "py.test",
        *(
            session.posargs
            or [
                "-vv",
                "-n=auto",
                "--cov=gapic",
                "--cov-append",
                "--cov-config=.coveragerc",
                "--cov-report=term",
                "--cov-fail-under=0",
                path.join("tests", "unit"),
            ]
        ),
    )


FRAG_DIR = Path("tests") / "fragments"
FRAGMENT_FILES = tuple(
    Path(dirname).relative_to(FRAG_DIR) / f
    for dirname, _, files in os.walk(FRAG_DIR)
    for f in files
    if os.path.splitext(f)[1] == ".proto" and f.startswith("test_")
)


# Note: this class lives outside 'fragment'
# so that, if necessary, it can be pickled for a ProcessPoolExecutor
# A callable class is necessary so that the session can be closed over
# instead of passed in, which simplifies the invocation via map.
class FragTester:
    def __init__(self, session, use_ads_templates):
        self.session = session
        self.use_ads_templates = use_ads_templates

    def __call__(self, frag):
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Generate the fragment GAPIC.
            outputs = []
            templates = (
                path.join(path.dirname(__file__), "gapic", "ads-templates")
                if self.use_ads_templates
                else "DEFAULT"
            )
            maybe_old_naming = ",old-naming" if self.use_ads_templates else ""

            session_args = [
                "python",
                "-m",
                "grpc_tools.protoc",
                f"--proto_path={str(FRAG_DIR)}",
                f"--python_gapic_out={tmp_dir}",
                f"--python_gapic_opt=transport=grpc+rest,python-gapic-templates={templates}{maybe_old_naming}",
            ]

            outputs.append(
                self.session.run(
                    *session_args,
                    str(frag),
                    external=True,
                    silent=True,
                )
            )

            # Install the generated fragment library.
            if self.use_ads_templates:
                self.session.install(tmp_dir, "-e", ".", "-qqq")
            else:
                # Use the constraints file for the specific python runtime version.
                # We do this to make sure that we're testing against the lowest
                # supported version of a dependency.
                # This is needed to recreate the issue reported in
                # https://github.com/googleapis/gapic-generator-python/issues/1748
                # The ads templates do not have constraints files.
                constraints_path = str(
                    f"{tmp_dir}/testing/constraints-{self.session.python}.txt"
                )
                self.session.install(tmp_dir, "-e", ".", "-qqq", "-r", constraints_path)

            # Run the fragment's generated unit tests.
            # Don't bother parallelizing them: we already parallelize
            # the fragments, and there usually aren't too many tests per fragment.
            outputs.append(
                self.session.run(
                    "py.test",
                    "--quiet",
                    f"--cov-config={str(Path(tmp_dir) / '.coveragerc')}",
                    "--cov-report=term",
                    "--cov-fail-under=100",
                    str(Path(tmp_dir) / "tests" / "unit"),
                    silent=True,
                )
            )

            return "".join(outputs)


@nox.session(python=ALL_PYTHON)
def fragment(session, use_ads_templates=False):
    session.install(
        "coverage",
        "pytest",
        "pytest-cov",
        "pytest-xdist",
        "pytest-asyncio",
        "grpcio-tools",
    )
    session.install("-e", ".")

    frag_files = (
        [Path(f) for f in session.posargs] if session.posargs else FRAGMENT_FILES
    )

    if os.environ.get("PARALLEL_FRAGMENT_TESTS", "false").lower() == "true":
        with ThreadPoolExecutor() as p:
            all_outs = p.map(FragTester(session, use_ads_templates), frag_files)

        output = "".join(all_outs)
        session.log(output)
    else:
        tester = FragTester(session, use_ads_templates)
        for frag in frag_files:
            session.log(tester(frag))


@nox.session(python=ALL_PYTHON)
def fragment_alternative_templates(session):
    fragment(session, use_ads_templates=True)


# `_add_python_settings` consumes a path to a temporary directory (str; i.e. tmp_dir) and
# python settings (Dict; i.e. python settings) and modifies the service yaml within
# tmp_dir to include python settings. The primary purpose of this function is to modify
# the service yaml and include `rest_async_io_enabled=True` to test the async rest
# optional feature.
def _add_python_settings(tmp_dir, python_settings):
    return f"""
import yaml
from pathlib import Path
temp_file_path = Path(f"{tmp_dir}/showcase_v1beta1.yaml")
with temp_file_path.open('r') as file:
    data = yaml.safe_load(file)
    data['publishing']['library_settings'] = {python_settings}

with temp_file_path.open('w') as file:
    yaml.safe_dump(data, file, default_flow_style=False, sort_keys=False)
"""


# TODO(https://github.com/googleapis/gapic-generator-python/issues/2121): `rest_async_io_enabled` must be removed once async rest is GA.
@contextmanager
def showcase_library(
    session,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
    include_service_yaml=True,
    retry_config=True,
    rest_async_io_enabled=False,
    install_async_rest_extra=False,
):
    """Install the generated library into the session for showcase tests.

    Args:
        session: The nox session object.
        templates (str): The template directory to use for code generation.
            Defaults to "DEFAULT".
        other_opts (typing.Iterable[str]): Additional options passed to
            `--python_gapic_opt` during code generation.
        include_service_yaml (bool): Whether to download and pass
            `showcase_v1beta1.yaml` to the generator.
        retry_config (bool): Whether to download and pass
            `showcase_grpc_service_config.json` to the generator.
        rest_async_io_enabled (bool): Whether to enable the experimental
            `rest_async_io_enabled` setting in `showcase_v1beta1.yaml` so
            `rest_asyncio` transports are generated for all services. When True,
            the `[async_rest]` extra is also installed.
        install_async_rest_extra (bool): Whether to install the generated
            library with the `[async_rest]` extra and its corresponding
            `constraints-{python}-async-rest.txt` file even when
            `rest_async_io_enabled` is False in `showcase_v1beta1.yaml` (e.g.,
            for services with resumable upload methods).
    """

    session.log("-" * 70)
    session.log("Note: Showcase must be running for these tests to work.")
    session.log("See https://github.com/googleapis/gapic-showcase")
    session.log("-" * 70)

    # Install gapic-generator-python
    session.install("-e", ".")

    # Install grpcio-tools for protoc
    session.install("grpcio-tools")

    # TODO(https://github.com/googleapis/gapic-generator-python/issues/2473):
    # Warnings emitted from google-api-core starting in 2.28
    # appear to cause issues when running protoc.
    # The specific failure is `Plugin output is unparseable`
    if session.python == "3.10":
        session.install("google-api-core<2.28")

    # Install a client library for Showcase.
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Download the Showcase descriptor.
        session.run(
            "curl",
            "https://github.com/googleapis/gapic-showcase/releases/"
            f"download/v{showcase_version}/"
            f"gapic-showcase-{showcase_version}.desc",
            "-L",
            "--output",
            path.join(tmp_dir, "showcase.desc"),
            external=True,
            silent=True,
        )
        if include_service_yaml:
            session.run(
                "curl",
                "https://github.com/googleapis/gapic-showcase/releases/"
                f"download/v{showcase_version}/"
                f"showcase_v1beta1.yaml",
                "-L",
                "--output",
                path.join(tmp_dir, "showcase_v1beta1.yaml"),
                external=True,
                silent=True,
            )
            # TODO(https://github.com/googleapis/gapic-generator-python/issues/2121): The section below updates the showcase service yaml
            # to test experimental async rest transport. It must be removed once support for async rest is GA.
            if rest_async_io_enabled:
                # Install pyYAML for yaml.
                session.install("pyYAML")

                python_settings = [
                    {
                        "version": "google.showcase.v1beta1",
                        "python_settings": {
                            "experimental_features": {"rest_async_io_enabled": True}
                        },
                    }
                ]
                update_service_yaml = _add_python_settings(tmp_dir, python_settings)
                session.run("python", "-c", f"{update_service_yaml}")
            # END TODO section to remove.
        if retry_config:
            session.run(
                "curl",
                "https://github.com/googleapis/gapic-showcase/releases/"
                f"download/v{showcase_version}/"
                f"showcase_grpc_service_config.json",
                "-L",
                "--output",
                path.join(tmp_dir, "showcase_grpc_service_config.json"),
                external=True,
                silent=True,
            )
        # Write out a client library for Showcase.
        template_opt = f"python-gapic-templates={templates}"
        opts = "--python_gapic_opt="
        if include_service_yaml and retry_config:
            opts += ",".join(
                other_opts
                + (
                    f"{template_opt}",
                    "transport=grpc+rest",
                    f"service-yaml={tmp_dir}/showcase_v1beta1.yaml",
                    f"retry-config={tmp_dir}/showcase_grpc_service_config.json",
                )
            )
        else:
            opts += ",".join(
                other_opts
                + (
                    f"{template_opt}",
                    "transport=grpc+rest",
                )
            )
        # TODO(https://github.com/googleapis/google-cloud-python/issues/16312):
        # Add compliance.proto once this bug is fixed
        # We should use `"google/showcase/v1beta1/*.proto",`
        protos = (
            "google/showcase/v1beta1/echo.proto",
            "google/showcase/v1beta1/identity.proto",
            "google/showcase/v1beta1/messaging.proto",
            "google/showcase/v1beta1/rest_error.proto",
            "google/showcase/v1beta1/sequence.proto",
            "google/showcase/v1beta1/testing.proto",
        )
        if templates == "DEFAULT":
            protos += ("google/showcase/v1beta1/resumable_upload.proto",)
        cmd_tup = (
            "python",
            "-m",
            "grpc_tools.protoc",
            "--experimental_allow_proto3_optional",
            f"--descriptor_set_in={tmp_dir}{path.sep}showcase.desc",
            opts,
            f"--python_gapic_out={tmp_dir}",
            *protos,
        )

        session.run(
            *cmd_tup,
            external=True,
        )

        # Install the generated showcase library.
        if templates == "DEFAULT":
            # Use the constraints file for the specific python runtime version.
            # We do this to make sure that we're testing against the lowest
            # supported version of a dependency.
            # This is needed to recreate the issue reported in
            # https://github.com/googleapis/google-cloud-python/issues/12254
            constraints_path = str(
                f"{tmp_dir}/testing/constraints-{session.python}.txt"
            )
            extras = ""
            if rest_async_io_enabled or install_async_rest_extra:
                extras = "[async_rest]"
                async_rest_constraints_path = str(
                    f"{tmp_dir}/testing/constraints-{session.python}-async-rest.txt"
                )
                if os.path.exists(async_rest_constraints_path):
                    # use async-rest constraints if available
                    constraints_path = async_rest_constraints_path
                else:
                    session.log(
                        f"{async_rest_constraints_path} not found. Using base constraints file"
                    )
            session.install("-e", f"{tmp_dir}{extras}", "-r", constraints_path)
        else:
            # The ads templates do not have constraints files.
            # See https://github.com/googleapis/gapic-generator-python/issues/1788
            # Install the library without a constraints file.
            session.install("-e", tmp_dir)

        yield tmp_dir


@nox.session(python=ALL_PYTHON)
@nox.parametrize("install_async_rest_extra", [False, True])
def showcase(
    session,
    install_async_rest_extra=False,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
    env: typing.Optional[typing.Dict[str, str]] = {},
):
    """Run the Showcase test suite.

    Set INSTALL_LOCAL_CORE=true to install packages/google-api-core from source
    (useful for local testing and canary validation).
    """

    with showcase_library(
        session,
        templates=templates,
        other_opts=other_opts,
        install_async_rest_extra=install_async_rest_extra,
    ):
        # When opt-in environment variable is set (e.g. in canary CI or local testing),
        # install the local google-api-core package from source.
        if os.getenv("INSTALL_LOCAL_CORE") == "true":
            local_core = Path(__file__).resolve().parent.parent / "google-api-core"
            if not local_core.is_dir():
                session.error(
                    f"INSTALL_LOCAL_CORE is set to 'true' but {local_core} does not exist."
                )
            session.install("-e", str(local_core))

        # Use pytest-asyncio<1.0.0 while we investigate the recent failure described in
        # https://github.com/googleapis/gapic-generator-python/issues/2399
        session.install("pytest", "pytest-asyncio<1.0.0")
        session.install(
            "opentelemetry-api",
            "opentelemetry-sdk",
            "opentelemetry-instrumentation-grpc",
        )
        test_directory = Path("tests", "system")
        ignore_file = env.get("IGNORE_FILE")
        pytest_command = [
            "py.test",
            "--quiet",
            *(session.posargs or [str(test_directory)]),
        ]
        if ignore_file:
            ignore_path = test_directory / ignore_file
            pytest_command.extend(["--ignore", str(ignore_path)])

        session.run(
            *pytest_command,
            env=env,
        )


@nox.session(python=ALL_PYTHON)
def showcase_w_rest_async(
    session,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
    env: typing.Optional[typing.Dict[str, str]] = {},
):
    """Run the Showcase test suite with async rest transport.

    Set INSTALL_LOCAL_CORE=true to install packages/google-api-core from source
    (useful for local testing and canary validation).
    """

    with showcase_library(
        session, templates=templates, other_opts=other_opts, rest_async_io_enabled=True
    ):
        # When opt-in environment variable is set (e.g. in canary CI or local testing),
        # install the local google-api-core package from source.
        if os.getenv("INSTALL_LOCAL_CORE") == "true":
            local_core = Path(__file__).resolve().parent.parent / "google-api-core"
            if not local_core.is_dir():
                session.error(
                    f"INSTALL_LOCAL_CORE is set to 'true' but {local_core} does not exist."
                )
            session.install("-e", str(local_core))

        # Use pytest-asyncio<1.0.0 while we investigate the recent failure described in
        # https://github.com/googleapis/gapic-generator-python/issues/2399
        session.install("pytest", "pytest-asyncio<1.0.0")
        session.install(
            "opentelemetry-api",
            "opentelemetry-sdk",
            "opentelemetry-instrumentation-grpc",
        )
        test_directory = Path("tests", "system")
        ignore_file = env.get("IGNORE_FILE")
        pytest_command = [
            "py.test",
            "--quiet",
            *(session.posargs or [str(test_directory)]),
        ]
        if ignore_file:
            ignore_path = test_directory / ignore_file
            pytest_command.extend(["--ignore", str(ignore_path)])

        session.run(
            *pytest_command,
            env=env,
        )


@nox.session(python=NEWEST_PYTHON)
def showcase_mtls(
    session,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
    env: typing.Optional[typing.Dict[str, str]] = {},
):
    """Run the Showcase mtls test suite."""

    with showcase_library(session, templates=templates, other_opts=other_opts):
        session.install("pytest", "pytest-asyncio")
        test_directory = Path("tests", "system")
        ignore_file = env.get("IGNORE_FILE")
        pytest_command = [
            "py.test",
            "--quiet",
            "--mtls",
            *(session.posargs or [str(test_directory)]),
        ]
        if ignore_file:
            ignore_path = test_directory / ignore_file
            pytest_command.extend(["--ignore", str(ignore_path)])

        session.run(
            *pytest_command,
            env=env,
        )


# TODO(https://github.com/googleapis/google-cloud-python/issues/17752):
# Remove showcase_pqc once grpcio >= 1.83.0 is enforced by default.
@nox.session(python=NEWEST_PYTHON)
def showcase_pqc(
    session,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
    env: typing.Optional[typing.Dict[str, str]] = {},
):
    """Run the Showcase PQC verification test suite against grpcio 1.83+ over standard TLS."""
    with showcase_library(session, templates=templates, other_opts=other_opts):
        session.install("pytest", "pytest-asyncio")
        session.install("--upgrade", "grpcio>=1.83.0", "grpcio-status>=1.83.0")
        session.run(
            "py.test",
            "--quiet",
            "--tls",
            *(session.posargs or ["tests/system/test_pqc.py"]),
            env=env,
        )


def run_showcase_unit_tests(
    session,
    fail_under=100,
    rest_async_io_enabled=False,
    install_async_rest_extra=False,
):
    """Run the generated Showcase unit test suite with coverage verification.

    Args:
        session: The nox session object.
        fail_under (int): Minimum required test coverage percentage.
            Defaults to 100.
        rest_async_io_enabled (bool): Whether `rest_async_io_enabled` was enabled
            in `showcase_v1beta1.yaml` during code generation.
        install_async_rest_extra (bool): Whether the library was installed with
            the `[async_rest]` extra. When both `rest_async_io_enabled` and
            `install_async_rest_extra` are False, `**/rest_asyncio.py` is omitted
            from coverage since optional `async_rest` dependencies are not
            installed.
    """
    session.install(
        "coverage",
        "pytest",
        "pytest-cov",
        "pytest-xdist",
        "pytest-asyncio",
        "opentelemetry-api",
        "opentelemetry-sdk",
    )
    # Freeze and print python environment package versions
    session.run("python", "-m", "pip", "freeze")

    if (
        not rest_async_io_enabled
        and not install_async_rest_extra
        and path.exists(".coveragerc")
    ):
        with open(".coveragerc", "r") as f:
            coveragerc = f.read()
        if "**/rest_asyncio.py" not in coveragerc:
            coveragerc = coveragerc.replace(
                "omit =\n", "omit =\n    **/rest_asyncio.py\n"
            )
            with open(".coveragerc", "w") as f:
                f.write(coveragerc)

    # Run the tests.
    session.run(
        "py.test",
        *(
            session.posargs
            or [
                "-n=auto",
                "--quiet",
                "--cov=google",
                "--cov-append",
                f"--cov-fail-under={str(fail_under)}",
                path.join("tests", "unit"),
            ]
        ),
    )


@nox.session(python=ALL_PYTHON)
@nox.parametrize("install_async_rest_extra", [False, True])
def showcase_unit(
    session,
    install_async_rest_extra=False,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
):
    """Run the generated unit tests against the Showcase library."""
    with showcase_library(
        session,
        templates=templates,
        other_opts=other_opts,
        install_async_rest_extra=install_async_rest_extra,
    ) as lib:
        session.chdir(lib)
        run_showcase_unit_tests(
            session, install_async_rest_extra=install_async_rest_extra
        )


# TODO: `showcase_unit_w_rest_async` nox session runs showcase unit tests with the
# experimental async rest transport and must be removed once support for async rest is GA.
# See related issue: https://github.com/googleapis/gapic-generator-python/issues/2121.
@nox.session(python=ALL_PYTHON)
def showcase_unit_w_rest_async(
    session,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
):
    """Run the generated unit tests with async rest transport against the Showcase library."""
    with showcase_library(
        session, templates=templates, other_opts=other_opts, rest_async_io_enabled=True
    ) as lib:
        session.chdir(lib)
        run_showcase_unit_tests(session, rest_async_io_enabled=True)


@nox.session(python=ALL_PYTHON)
def showcase_unit_alternative_templates(session):
    with showcase_library(
        session, templates=ADS_TEMPLATES, other_opts=("old-naming",)
    ) as lib:
        session.chdir(lib)
        run_showcase_unit_tests(session)


@nox.session(python=NEWEST_PYTHON)
def showcase_unit_add_iam_methods(session):
    with showcase_library(session, other_opts=("add-iam-methods",)) as lib:
        session.chdir(lib)
        run_showcase_unit_tests(session, fail_under=100)


@nox.session(python=ALL_PYTHON)
def showcase_unit_mixins(session):
    with showcase_library(session, include_service_yaml=True) as lib:
        session.chdir(lib)
        run_showcase_unit_tests(session)


@nox.session(python=ALL_PYTHON)
def showcase_unit_alternative_templates_mixins(session):
    with showcase_library(
        session,
        templates=ADS_TEMPLATES,
        other_opts=("old-naming",),
        include_service_yaml=True,
    ) as lib:
        session.chdir(lib)
        run_showcase_unit_tests(session)


@nox.session(python=NEWEST_PYTHON)
def showcase_mypy(
    session,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
):
    """Perform typecheck analysis on the generated Showcase library.

    Set INSTALL_LOCAL_CORE=true to install packages/google-api-core from source
    (useful for local testing and canary validation).
    """

    session.install(
        "mypy",
        "types-setuptools",
        "types-protobuf",
        "types-requests",
        "types-dataclasses",
    )

    with showcase_library(session, templates=templates, other_opts=other_opts) as lib:
        # When opt-in environment variable is set (e.g. in canary CI or local testing),
        # install the local google-api-core package from source.
        if os.getenv("INSTALL_LOCAL_CORE") == "true":
            local_core = Path(__file__).resolve().parent.parent / "google-api-core"
            if not local_core.is_dir():
                session.error(
                    f"INSTALL_LOCAL_CORE is set to 'true' but {local_core} does not exist."
                )
            session.install(str(local_core))

        session.chdir(lib)

        # Run the tests.
        session.run("mypy", "-p", "google", "--check-untyped-defs")


@nox.session(python=NEWEST_PYTHON)
def showcase_mypy_alternative_templates(session):
    showcase_mypy(session, templates=ADS_TEMPLATES, other_opts=("old-naming",))


@nox.session(python=NEWEST_PYTHON)
def snippetgen(session):
    # Clone googleapis/api-common-protos which are referenced by the snippet
    # protos
    api_common_protos = "api-common-protos"
    try:
        session.run("git", "-C", api_common_protos, "pull", external=True)
    except nox.command.CommandFailed:
        session.run(
            "git",
            "clone",
            "--single-branch",
            f"https://github.com/googleapis/{api_common_protos}",
            external=True,
        )

    # Install gapic-generator-python
    session.install("-e", ".")

    session.install("grpcio-tools", "pytest", "pytest-asyncio")

    session.run("py.test", "-vv", "tests/snippetgen")


@nox.session(python="3.10")
def docs(session):
    """Build the docs for this generator."""

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
        "sphinx-rtd-theme",
    )

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    session.run(
        "sphinx-build",
        "-W",  # warnings as errors
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
        "sphinx-rtd-theme",
    )

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    session.run(
        "sphinx-build",
        "-T",  # show full traceback on exception
        "-N",  # no colors
        "-D",  # Override configuration values set in the conf.py file
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
        "html",  # builder
        "-d",
        os.path.join("docs", "_build", "doctrees", ""),  # cache directory
        # paths to build:
        os.path.join("docs", ""),
        os.path.join("docs", "_build", "html", ""),
    )


@nox.session(python=ALL_PYTHON)
def mypy(session):
    """Perform typecheck analysis."""
    # Pin to click==8.1.3 to workaround https://github.com/pallets/click/issues/2558
    session.install(
        "mypy",
        "types-protobuf<=3.19.7",
        "types-PyYAML",
        "types-dataclasses",
        "click==8.1.3",
    )
    session.install(".")
    session.run("mypy", f"--config-file={MYPY_CONFIG_FILE}", "-p", "gapic")


@nox.session(python=NEWEST_PYTHON)
def lint(session):
    """Run linters.

    Returns a failure if the linters find linting errors or sufficiently
    serious code quality issues.
    """

    # TODO(https://github.com/googleapis/google-cloud-python/issues/16186):
    # SKIP: This session was not enforced in the standalone (split) repo
    # and is disabled here to ensure a "move-only" migration.
    session.skip(
        "Linting was not enforced in the split repo. "
        "Skipping now to avoid changing code during migration. See Issue #16186"
    )

    session.install("flake8", RUFF_VERSION)

    # 1. Check imports
    session.run(
        "ruff",
        "check",
        "--select",
        "I",
        *LINT_PATHS,
        "--exclude",
        RUFF_EXCLUDES,
    )

    # 2. Check formatting
    session.run(
        "ruff",
        "format",
        "--check",
        *LINT_PATHS,
        "--exclude",
        RUFF_EXCLUDES,
    )

    # 3. Run Flake8
    session.run(
        "flake8",
        "gapic",
        "tests",
    )


@nox.session(python=NEWEST_PYTHON)
def lint_setup_py(session):
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16186):
    # SKIP: This session was not enforced in the standalone (split) repo
    # and is disabled here to ensure a "move-only" migration.
    session.skip(
        "Skipping now to avoid changing code during migration. See Issue #16186"
    )


@nox.session(python="3.10")
def blacken(session):
    """Run ruff format.

    DEPRECATED: This session now uses Ruff instead of Black.
    It formats code style only (indentation, quotes, etc).
    """
    session.log(
        "WARNING: The 'blacken' session is deprecated and will be removed in the next release. Please use 'nox -s format' in the future."
    )

    session.install(RUFF_VERSION)

    # 1. Format Code (Replaces black)
    # We do NOT run 'ruff check --select I' here, preserving strict parity.
    session.run(
        "ruff",
        "format",
        "--line-length=88",  # Standard Black line length
        *LINT_PATHS,
        "--exclude",
        RUFF_EXCLUDES,
    )


@nox.session(python=NEWEST_PYTHON)
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
        "--line-length=88",  # Standard Black line length
        *LINT_PATHS,
    )

    # 3. Run Ruff to format code
    session.run(
        "ruff",
        "format",
        "--line-length=88",  # Standard Black line length
        *LINT_PATHS,
    )


@contextmanager
def google_ads_library(session):
    """Generate and install the Google Ads GAPIC library for live system tests."""
    session.install("-e", ".")
    session.install("grpcio-tools", "pyYAML", "pypandoc-binary==1.16.2")

    with tempfile.TemporaryDirectory() as tmp_dir:
        googleapis_dir = path.join(tmp_dir, "googleapis")
        sdk_dir = path.join(tmp_dir, "sdk")
        os.makedirs(sdk_dir, exist_ok=True)

        session.run(
            "git",
            "clone",
            "--depth",
            "1",
            "--filter=blob:none",
            "--sparse",
            "https://github.com/googleapis/googleapis.git",
            googleapis_dir,
            external=True,
            silent=True,
        )
        session.run(
            "git",
            "-C",
            googleapis_dir,
            "sparse-checkout",
            "set",
            "google/ads/googleads/v23",
            "google/api",
            "google/rpc",
            "google/longrunning",
            "google/type",
            external=True,
            silent=True,
        )

        src_yaml = path.join(
            googleapis_dir, "google", "ads", "googleads", "v23", "googleads_v23.yaml"
        )
        dst_yaml = path.join(sdk_dir, "googleads_v23.yaml")
        shutil.copyfile(src_yaml, dst_yaml)
        session.run(
            "python",
            "-c",
            (
                "import yaml; "
                f"p = {dst_yaml!r}; "
                "data = yaml.safe_load(open(p, encoding='utf-8')); "
                "data['apis'] = [{'name': 'google.ads.googleads.v23.services.YouTubeVideoUploadService'}]; "
                "data.setdefault('publishing', {})['library_settings'] = ["
                "{'version': 'google.ads.googleads.v23', "
                "'python_settings': {'experimental_features': {'rest_async_io_enabled': True}}}"
                "]; "
                "yaml.safe_dump(data, open(p, 'w', encoding='utf-8'), default_flow_style=False, sort_keys=False)"
            ),
        )

        ads_protos = (
            "google/ads/googleads/v23/services/youtube_video_upload_service.proto",
            "google/ads/googleads/v23/resources/youtube_video_upload.proto",
            "google/ads/googleads/v23/enums/youtube_video_privacy.proto",
        )
        desc_path = path.join(sdk_dir, "googleads.desc")
        session.run(
            "python",
            "-m",
            "grpc_tools.protoc",
            "--experimental_allow_proto3_optional",
            f"--proto_path={googleapis_dir}",
            "--include_imports",
            "--include_source_info",
            f"-o{desc_path}",
            *(path.join(googleapis_dir, p) for p in ads_protos),
            external=True,
        )

        retry_config = path.join(
            googleapis_dir,
            "google",
            "ads",
            "googleads",
            "v23",
            "googleads_grpc_service_config.json",
        )
        session.run(
            "python",
            "-m",
            "grpc_tools.protoc",
            "--experimental_allow_proto3_optional",
            f"--descriptor_set_in={desc_path}",
            (
                "--python_gapic_opt="
                f"transport=grpc+rest,autogen-snippets=False,service-yaml={dst_yaml},retry-config={retry_config}"
            ),
            f"--python_gapic_out={sdk_dir}",
            *ads_protos,
            external=True,
        )

        session.install("-e", f"{sdk_dir}[async_rest]")
        yield sdk_dir


@nox.session(python=ALL_PYTHON)
def system(session):
    """Run the system test suite."""
    with google_ads_library(session):
        session.install("pytest", "pytest-asyncio")
        session.run(
            "py.test",
            *(session.posargs or ["-vv", path.join("tests", "system_live")]),
        )


@nox.session(python=NEWEST_PYTHON)
@nox.parametrize(
    "protobuf_implementation",
    ["python", "upb"],
)
def prerelease_deps(session, protobuf_implementation):
    """
    Run all tests with pre-release versions of dependencies installed.
    """
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16184):
    # Implement pre-release dependency logic to test against upcoming runtime changes.
    session.skip(
        "prerelease_deps session is not yet implemented for gapic-generator-python."
    )


@nox.session(python=NEWEST_PYTHON)
@nox.parametrize(
    "protobuf_implementation",
    ["python", "upb"],
)
def core_deps_from_source(session, protobuf_implementation):
    """Run all tests with core dependencies installed from source."""
    # TODO(https://github.com/googleapis/google-cloud-python/issues/16185):
    # Implement logic to install core packages directly from the mono-repo directories.
    session.skip(
        "core_deps_from_source session is not yet implemented for gapic-generator-python."
    )
