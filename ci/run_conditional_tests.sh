#!/bin/bash
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
# `BUILD_TYPE` should be one of ["presubmit", "continuous"]
# `TEST_TYPE` should be one of ["docs", "docfx", "prerelease", "unit"]
# or match the name of the nox session that you want to run.
# `PY_VERSION` should be one of ["3.10", "3.11", "3.12"]

# `TEST_TYPE` and `PY_VERSION` are required by the script `ci/run_single_test.sh`

# This script will determine which directories have changed
# under the `packages` folder. For `BUILD_TYPE=="presubmit"`,
# we'll compare against the `packages` folder in HEAD,
# whereas for `BUILD_TYPE=="continuous"` we'll compare changes
# with HEAD~1. For all directories that have changed files, we will
# run the script located at `${PROJECT_ROOT}/ci/run_single_test.sh`.

# `-e` enables the script to automatically fail when a command fails
# `-o pipefail` sets the exit code to non-zero if any command fails,
# or zero if all commands in the pipeline exit successfully.
set -eo pipefail

export PROJECT_ROOT=$(realpath $(dirname "${BASH_SOURCE[0]}")/..)
TARGET_BRANCH="${TARGET_BRANCH:-main}"

# Redirect git clones for core dependencies to the local repository.
# This serves two purposes:
# 1. Performance: Avoids repeated 100MB+ downloads of the monorepo for each dependency.
# 2. Correctness: Ensures that changes in core packages (like google-api-core) are
#    tested against downstream packages in the same Pull Request.
git config --global url."${PROJECT_ROOT}".insteadOf "https://github.com/googleapis/google-cloud-python"
git config --global url."${PROJECT_ROOT}".insteadOf "https://github.com/googleapis/google-cloud-python.git"

# A script file for running the test in a sub project.
test_script="${PROJECT_ROOT}/ci/run_single_test.sh"

if [ "${TEST_ALL_PACKAGES}" = "true" ]; then
    GIT_DIFF_ARG=""

elif [[ ${BUILD_TYPE} == "presubmit" ]]; then
    # For presubmit build, we want to know the difference from the
    # common commit in the target branch.
    if [ -n "${TARGET_BRANCH}" ]; then
        if [[ "${TEST_TYPE}" == "import_profile" ]]; then
            git fetch --no-tags --quiet origin "${TARGET_BRANCH}:refs/remotes/origin/${TARGET_BRANCH}" || true
        else
            git fetch --no-tags --quiet origin "${TARGET_BRANCH}:refs/remotes/origin/${TARGET_BRANCH}" --depth=200 || true
        fi
    fi
    GIT_DIFF_ARG="origin/${TARGET_BRANCH}..."

elif [[ ${BUILD_TYPE} == "continuous" ]]; then
    # For continuous build, we want to know the difference in the last
    # commit. This assumes we use squash commit when merging PRs.
    GIT_DIFF_ARG="HEAD~1.."

else
    # Run everything.
    GIT_DIFF_ARG=""
fi

run_test_in_dir() {
    local d=$1
    local pkg_name_clean=$(echo ${d} | sed 's|/$||' | sed 's|/|_|g')
    local log_file="/tmp/test_log_${PY_VERSION}_${pkg_name_clean}.log"
    export COVERAGE_FILE="${PROJECT_ROOT}/.coverage.${PY_VERSION}.${pkg_name_clean}"

    # Isolate setuptools build directories per worker to prevent parallel build collisions.
    local worker_build_dir="/tmp/build_${PY_VERSION}_${pkg_name_clean}"
    local dist_cfg="/tmp/dist_cfg_${PY_VERSION}_${pkg_name_clean}.cfg"
    mkdir -p "${worker_build_dir}"
    printf "[build]\nbuild_base = %s/build\n[bdist_wheel]\nbdist_dir = %s/bdist\n[egg_info]\negg_base = %s\n" \
        "${worker_build_dir}" "${worker_build_dir}" "${worker_build_dir}" > "${dist_cfg}"
    export DIST_EXTRA_CONFIG="${dist_cfg}"

    local div="============================================================"
    local header="\n${div}\nRunning tests in ${d}\n${div}"
    local footer

    pushd ${d} > /dev/null
    set +e
    if [ "${PARALLEL_WORKERS}" = "1" ]; then
        # When running with a single worker, stream output in real-time while capturing to log file
        echo -e "${header}"
        ${test_script} 2>&1 | tee "${log_file}"
        local ret=${PIPESTATUS[0]}
    else
        # When running multiple workers in parallel, buffer output to prevent interleaved log lines
        ${test_script} > "${log_file}" 2>&1
        local ret=$?
    fi
    set -e
    popd > /dev/null

    rm -rf "${worker_build_dir}" "${dist_cfg}"

    if [ ${ret} -ne 0 ]; then
        footer="❌ Tests failed in ${d} with exit code ${ret}"
    else
        footer="✅ Tests passed in ${d}"
    fi

    if [ "${PARALLEL_WORKERS}" != "1" ]; then
        (
            flock -x 9
            echo -e "${header}"
            cat "${log_file}"
            echo "${footer}"
        ) 9> "/tmp/ci_output_${PY_VERSION}.lock"
    else
        echo "${footer}"
    fi

    if [ ${ret} -ne 0 ] && [ -n "${FAILURE_LOG_DIR}" ]; then
        mkdir -p "${FAILURE_LOG_DIR}"
        local pkg_name=$(basename "${d}")
        if grep -q "short test summary info" "${log_file}" 2>/dev/null; then
            grep -A 35 -B 2 "short test summary info" "${log_file}" 2>/dev/null | sed $'s/\x1b\\[[0-9;]*[a-zA-Z]//g' > "${FAILURE_LOG_DIR}/${pkg_name}.log.txt" || true
        else
            tail -n 50 "${log_file}" 2>/dev/null | sed $'s/\x1b\\[[0-9;]*[a-zA-Z]//g' > "${FAILURE_LOG_DIR}/${pkg_name}.log.txt" || true
        fi
    fi

    rm -f "${log_file}"
    if [ ${ret} -ne 0 ]; then
        if [ "${CONTINUE_ON_ERROR}" = "true" ]; then
            exit 1
        fi
        exit 255  # Cancel xargs parallel jobs
    fi
}
export -f run_test_in_dir
export test_script PROJECT_ROOT PY_VERSION TEST_TYPE CONTINUE_ON_ERROR FAILURE_LOG_DIR

dirs_to_test=()

if [ -n "${PACKAGE_LIST}" ]; then
    echo "Using provided PACKAGE_LIST"
    dirs_to_test=(${PACKAGE_LIST})
else
    subdirs=(${PACKAGE_DIRS:-packages preview-packages})

    for subdir in ${subdirs[@]}; do
        if [ ! -d "${subdir}" ]; then continue; fi
        for d in `ls -d ${subdir}/*/ 2>/dev/null`; do
            should_test=false
            if [ -n "${GIT_DIFF_ARG}" ]; then
                set +e
                git diff --quiet ${GIT_DIFF_ARG} -- "${d}"
                changed=$?
                set -e
                if [[ "${changed}" -ne 0 ]]; then
                    should_test=true
                fi
            else
                # If GIT_DIFF_ARG is empty, run all the tests.
                should_test=true
            fi
            if [ "${should_test}" = true ]; then
                dirs_to_test+=("${d}")
            fi
        done
    done
fi

if [ ${#dirs_to_test[@]} -eq 0 ]; then
    echo "No packages to test."
    exit 0
fi

PARALLEL_WORKERS="${PARALLEL_WORKERS:-1}"
AVAIL_CORES=$(nproc 2>/dev/null || echo 4)
if [ "${PARALLEL_WORKERS}" -gt "${AVAIL_CORES}" ]; then
    PARALLEL_WORKERS="${AVAIL_CORES}"
fi

echo "Running tests across ${#dirs_to_test[@]} package(s) using ${PARALLEL_WORKERS} parallel worker(s)..."
printf "%s\0" "${dirs_to_test[@]}" | xargs -0 -P "${PARALLEL_WORKERS}" -I {} bash -c 'run_test_in_dir "$@"' _ {}
