#!/bin/bash
#
# Copyright 2022 Google LLC
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

# This script requires the following environment variables to be set:
# `TEST_TYPE` should be one of ["lint", "lint_setup_py", "docs", "docfx", "prerelease"]
# `PY_VERSION` should be one of ["3.10", "3.11", "3.12", "3.13"]

# This script is called by the `ci/run_conditional_tests.sh` script.
# A specific `nox` session will be run, depending on the value of
# `TEST_TYPE` and `PY_VERSION`. For example, if `TEST_TYPE` is
# `lint`, the `nox -s lint` session will be run.


set -e

if [ -z "${TEST_TYPE}" ]; then
    echo "missing TEST_TYPE env var"
    exit 1
fi

if [ -z "${PY_VERSION}" ]; then
    echo "missing PY_VERSION env var"
    exit 1
fi

# Don't fail on errors so we can capture all of the output
set +e

case ${TEST_TYPE} in
    docs)
        nox -s docs
        # This line needs to be directly after `nox -s docs` in order
        # for the failure to appear in Github presubmits
        retval=$?
        # Clean up built docs and python cache after the build process to avoid
        # `[Errno 28] No space left on device`
        # See https://github.com/googleapis/google-cloud-python/issues/12271
        rm -rf docs/_build
        ;;
    docfx)
        nox -s docfx
        # This line needs to be directly after `nox -s docfx` in order
        # for the failure to appear in Github presubmits
        retval=$?
        # Clean up built docs and python cache after the build process to avoid
        # `[Errno 28] No space left on device`
        # See https://github.com/googleapis/google-cloud-python/issues/12271
        rm -rf docs/_build
        ;;
    mypy)
        nox -s mypy-3.14
        retval=$?
        ;;
    prerelease)
        if [[ "$(pwd)" == */preview-packages/* ]]; then
            echo "Skipping prerelease for preview package $(pwd)"
            exit 0
        fi
        nox --stop-on-first-error -s prerelease_deps
        retval=$?
        ;;
    core_deps_from_source)
        if [[ "$(pwd)" == */preview-packages/* ]]; then
            echo "Skipping core_deps_from_source for preview package $(pwd)"
            exit 0
        fi
        nox --stop-on-first-error -s core_deps_from_source
        retval=$?
        ;;
    unit)
        case ${PY_VERSION} in
        "3.10")
            nox --stop-on-first-error -s unit-3.10
            retval=$?
            ;;
        "3.11")
            nox --stop-on-first-error -s unit-3.11
            retval=$?
            ;;
        "3.12")
            nox --stop-on-first-error -s unit-3.12
            retval=$?
            ;;
        "3.13")
            nox --stop-on-first-error -s unit-3.13
            retval=$?
            ;;
        "3.14")
            nox --stop-on-first-error -s unit-3.14
            retval=$?
            ;;
        "3.15")
            # This is needed to speed up builds
            nox --stop-on-first-error --force-venv-backend uv -s unit-3.15
            retval=$?
            ;;
        *)
            echo "unsupported PY_VERSION"
            exit 1
            ;;
        esac
        ;;
    import_profile)
        if [ -f setup.py ] || [ -f pyproject.toml ]; then
            PACKAGE_NAME=$(basename $(pwd))

            # TODO(https://github.com/googleapis/google-cloud-python/issues/18035):
            # Remove this skip once Python 3.15 is officially released and upstream binary wheels
            # (e.g. numpy, pyarrow, pandas, geopandas, pikepdf) are published on PyPI.
            # Packages with heavy C/Rust dependencies attempt full source compilation on pre-release Python,
            # taking 5-10+ minutes before failing due to unreleased CPython 3.15 C-API changes.
            if [[ "${PY_VERSION}" == "3.15"* ]]; then
                UNSUPPORTED_PRE_RELEASE_PACKAGES=(
                    "bigframes"
                    "pandas-gbq"
                    "google-cloud-documentai-toolbox"
                    "db-dtypes"
                    "bigquery-magics"
                )
                for unsupported in "${UNSUPPORTED_PRE_RELEASE_PACKAGES[@]}"; do
                    if [ "${PACKAGE_NAME}" = "${unsupported}" ]; then
                        echo "WARNING: Skipping import_profile for ${PACKAGE_NAME}: package has heavy C/Rust dependencies not yet supported on pre-release Python ${PY_VERSION}."
                        exit 0
                    fi
                done
            fi

            echo "Creating temporary virtualenv for import profile..."
            python3 -m venv .venv-profiler
            source .venv-profiler/bin/activate
            export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
            python -m pip install --upgrade pip setuptools

            PROFILER_TEMP_DIR=$(mktemp -d)
            cp ../../scripts/import_profiler/profiler.py "${PROFILER_TEMP_DIR}/profiler.py"
            PROFILER_SCRIPT="${PROFILER_TEMP_DIR}/profiler.py"
            BASELINE_CSV="${PROFILER_TEMP_DIR}/baseline_${PACKAGE_NAME}.csv"

            if [ -n "${TARGET_BRANCH}" ]; then
                # Fetch history for the target branch without --depth=1 in case it was shallowly fetched
                if [ -f "$(git rev-parse --git-dir)/shallow" ]; then
                    git fetch origin "${TARGET_BRANCH}:refs/remotes/origin/${TARGET_BRANCH}" --unshallow 2>/dev/null || \
                    git fetch origin "${TARGET_BRANCH}:refs/remotes/origin/${TARGET_BRANCH}" 2>/dev/null || true
                fi
                # Try origin first, then fallback to HEAD if everything else fails
                BASELINE_COMMIT=$(git merge-base HEAD "origin/${TARGET_BRANCH}" 2>/dev/null || \
                                 git rev-parse HEAD)
                if [ -n "${BASELINE_COMMIT}" ]; then
                    echo "Checking out baseline commit ${BASELINE_COMMIT} in a temporary worktree..."
                    REPO_PREFIX=$(git rev-parse --show-prefix)
                    WORKTREE_DIR=$(mktemp -d)
                    rmdir "${WORKTREE_DIR}"
                    if git worktree add "${WORKTREE_DIR}" "${BASELINE_COMMIT}" 2>/dev/null; then
                        if ! (
                            cd "${WORKTREE_DIR}/${REPO_PREFIX}"
                            if [ -f setup.py ] || [ -f pyproject.toml ]; then
                                if pip install -e . ; then
                                    echo "INFO: Successfully installed baseline dependencies for ${PACKAGE_NAME}."
                                    python "${PROFILER_SCRIPT}" --package "${PACKAGE_NAME}" --iterations 11 --csv "${BASELINE_CSV}"
                                    if [ $? -eq 0 ]; then
                                        echo "INFO: Successfully ran baseline profiler for ${PACKAGE_NAME}."
                                    fi
                                elif [[ "${PY_VERSION}" != "3.15"* ]]; then
                                    exit 1
                                fi
                            fi
                        ); then
                            git worktree remove -f "${WORKTREE_DIR}"
                            deactivate
                            rm -rf .venv-profiler
                            rm -rf "${PROFILER_TEMP_DIR}"
                            exit 1
                        fi
                        git worktree remove -f "${WORKTREE_DIR}"
                    else
                        echo "Failed to create git worktree for baseline. Skipping baseline generation."
                    fi
                else
                    echo "Could not find baseline commit for ${TARGET_BRANCH:-main}. Skipping baseline generation."
                fi
            fi

            # TODO(https://github.com/googleapis/google-cloud-python/issues/18035):
            # Clean up this fallback once Python 3.15 is officially released and upstream binary wheels are available on PyPI.
            # On pre-release Python versions, packages with complex C/Rust dependencies (e.g. bigframes) fail during pip install due to missing pre-built wheels.
            if ! pip install -e . ; then
                if [[ "${PY_VERSION}" == "3.15"* ]]; then
                    echo "WARNING: Could not install dependencies for ${PACKAGE_NAME} on Python ${PY_VERSION} (missing pre-built binary wheels for pre-release Python). Skipping import_profile."
                    retval=0
                else
                    retval=1
                fi
            else
                echo "INFO: Successfully installed dependencies for ${PACKAGE_NAME} on Python ${PY_VERSION}."
                if [ -f "${BASELINE_CSV}" ]; then
                    python ${PROFILER_SCRIPT} --package ${PACKAGE_NAME} --iterations 11 --fail-threshold 5000 --diff-baseline "${BASELINE_CSV}" --diff-threshold 100
                else
                    python ${PROFILER_SCRIPT} --package ${PACKAGE_NAME} --iterations 11 --fail-threshold 5000
                fi
                retval=$?
                if [ $retval -eq 0 ]; then
                    echo "INFO: Successfully completed import_profile for ${PACKAGE_NAME}."
                fi
            fi
            deactivate
            rm -rf .venv-profiler
            rm -rf "${PROFILER_TEMP_DIR}"
        else
            echo "Skipping import_profile as this does not appear to be a Python package (no setup.py or pyproject.toml)."
            retval=0
        fi
        ;;
    twine_check)
        if [ -f setup.py ] || [ -f pyproject.toml ]; then
            echo "Running twine_check for $(basename $(pwd))..."
            rm -rf dist
            # TODO(https://github.com/googleapis/google-cloud-python/issues/18339): Re-enable `--strict` once `long_description_content_type` is set in setup.py across all packages.
            if python3 -m build --sdist --no-isolation --outdir dist . && twine check dist/*; then
                retval=0
            else
                retval=1
            fi
            rm -rf dist
        else
            echo "Skipping twine_check as this does not appear to be a Python package (no setup.py or pyproject.toml)."
            retval=0
        fi
        ;;
    *)
        nox --stop-on-first-error -s ${TEST_TYPE}
        retval=$?
        ;;
    esac

if [ ${retval} -ne 0 ] && [ -n "${FAILURE_LOG_DIR}" ]; then
    mkdir -p "${FAILURE_LOG_DIR}"
    pkg_name=$(basename "$(pwd)")
    for pip_bin in "${NOX_ENVDIR:-.nox}"/*/bin/pip; do
        if [ -x "$pip_bin" ]; then
            pip_out=$("$pip_bin" list 2>/dev/null || true)
            if echo "$pip_out" | grep -qvE "^(Package|-+|pip|setuptools|wheel)[[:space:]]"; then
                echo "$pip_out" > "${FAILURE_LOG_DIR}/${pkg_name}.pip.txt"
            fi
            break
        fi
    done
fi

# Clean up `__pycache__`, `.nox`, and build artifact directories to avoid error
# `No space left on device` and prevent leftover build/ files from polluting
# downstream local dependency builds.
find . | grep -E "(__pycache__)" | xargs rm -rf
rm -rf .nox build *.egg-info

exit ${retval}
