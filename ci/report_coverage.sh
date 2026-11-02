#!/bin/bash
# Copyright 2026 Google LLC
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

set -eo pipefail

# This script generates coverage reports for modified packages.
# It assumes coverage databases have been downloaded to RESULTS_DIR.
# It uses /dev/shm for high-performance processing.

RESULTS_DIR="${RESULTS_DIR:-/dev/shm/.coverage-results}"
LOG_DIR="/dev/shm/coverage-logs"
DEFAULT_FAIL_UNDER="${DEFAULT_FAIL_UNDER:-99}"
MAX_JOBS=$(nproc)

mkdir -p "${LOG_DIR}"

# Identify modified packages
BUILD_TYPE="${BUILD_TYPE:-presubmit}"
TARGET_BRANCH="${TARGET_BRANCH:-main}"
PACKAGE_DIRS="${PACKAGE_DIRS:-packages preview-packages}"

if [ "${PACKAGE_LIST+set}" = "set" ]; then
    # If pre-determined package list is set, use it
    modified_packages="${PACKAGE_LIST}"
elif [[ "${TEST_ALL_PACKAGES}" == "true" ]]; then
    # Test all packages mode: evaluate coverage for every package in the repository
    modified_packages=$(for dir in ${PACKAGE_DIRS}; do ls -d ${dir}/*/ 2>/dev/null; done | cut -d/ -f1,2 | sort -u)
elif [[ "${BUILD_TYPE}" == "presubmit" ]]; then
    # Presubmit build: evaluate coverage only for packages modified relative to the target branch
    modified_packages=$(git diff --name-only "origin/${TARGET_BRANCH}..." -- ${PACKAGE_DIRS} 2>/dev/null | cut -d/ -f1,2 | sort -u)
else
    # Continuous build (post-merge on main): evaluate coverage for packages modified in the last commit
    modified_packages=$(git diff --name-only HEAD~1 -- ${PACKAGE_DIRS} 2>/dev/null | cut -d/ -f1,2 | sort -u)
fi

if [ -z "${modified_packages}" ]; then
    echo "============================================================"
    echo "No modified packages to evaluate coverage for."
    echo "============================================================"
    exit 0
fi
# Check if any modified package requires coverage
requires_coverage=false
for pkg in ${modified_packages}; do
    if [ -f "${pkg}/.coveragerc" ] && grep -Eq "fail_under\s*=\s*0" "${pkg}/.coveragerc"; then
        continue
    fi
    requires_coverage=true
    break
done
if [ ! -d "${RESULTS_DIR}" ] || [ -z "$(ls -A "${RESULTS_DIR}" 2>/dev/null)" ]; then
    if [ "${requires_coverage}" = "true" ]; then
        echo "Error: No coverage results found in ${RESULTS_DIR}, but some modified packages require coverage."
        exit 1
    else
        echo "No coverage results found, but no modified packages require coverage."
        exit 0
    fi
fi

# Unzip any zipped coverage results
find "$RESULTS_DIR" -type f -name '*.zip' -print0 | xargs -0 -P "${MAX_JOBS}" -I {} unzip -q -o {} -d "$RESULTS_DIR"

# Function to report coverage for a single package
report_package_coverage() {
    local pkg=$1
    local pkg_name_clean=$(echo "${pkg}" | sed 's|/$||' | sed 's|/|_|g')
    local pkg_log="${LOG_DIR}/${pkg_name_clean}.log"
    local pkg_status="${LOG_DIR}/${pkg_name_clean}.status"

    # Use /dev/shm for the combined coverage file to reduce disk I/O
    local pkg_coverage_db="/dev/shm/.coverage.${pkg_name_clean}"

    set +e
    (
        # Find coverage databases belonging specifically to this package
        shopt -s nullglob
        local pkg_files=(
            "${RESULTS_DIR}/.coverage."*"."${pkg_name_clean}
            "${RESULTS_DIR}/.coverage."*"."${pkg_name_clean}"."*
            "${RESULTS_DIR}"/*/".coverage."*"."${pkg_name_clean}
            "${RESULTS_DIR}"/*/".coverage."*"."${pkg_name_clean}"."*
        )
        shopt -u nullglob

        # Handle explicit skip via .coveragerc
        if [ -f "${pkg}/.coveragerc" ] && grep -Eq "fail_under\s*=\s*0" "${pkg}/.coveragerc"; then
            echo "Package has fail_under = 0, passing instantly with 100% success (even without coverage files)" > "${pkg_log}"
            echo 0 > "${pkg_status}"
            return
        fi

        if [ ${#pkg_files[@]} -eq 0 ]; then
            echo "Warning: No coverage results found for ${pkg}" > "${pkg_log}"
            echo 1 > "${pkg_status}"
            return
        fi

        pushd "${pkg}" > /dev/null

        # Combine databases
        COVERAGE_FILE="${pkg_coverage_db}" coverage combine "${pkg_files[@]}" >> "${pkg_log}" 2>&1

        # Generate report
        if [ -f ".coveragerc" ]; then
            echo "Using package-specific configuration: ${pkg}/.coveragerc" >> "${pkg_log}"
            if grep -q "fail_under" ".coveragerc"; then
                COVERAGE_FILE="${pkg_coverage_db}" coverage report --rcfile=".coveragerc" --include="$PWD/**" >> "${pkg_log}" 2>&1
            else
                echo "No fail_under specified in ${pkg}/.coveragerc, enforcing default" >> "${pkg_log}"
                COVERAGE_FILE="${pkg_coverage_db}" coverage report --rcfile=".coveragerc" --include="$PWD/**" --fail-under="${DEFAULT_FAIL_UNDER}" >> "${pkg_log}" 2>&1
            fi
        else
            echo "No .coveragerc found for ${pkg}, enforcing default" >> "${pkg_log}"
            COVERAGE_FILE="${pkg_coverage_db}" coverage report --include="$PWD/**" --fail-under="${DEFAULT_FAIL_UNDER}" >> "${pkg_log}" 2>&1
        fi

        echo $? > "${pkg_status}"
        popd > /dev/null
    )
    set -e
}

# Run coverage reporting in parallel
for pkg in ${modified_packages}; do
    if [ -d "${pkg}" ]; then
        # Limit concurrent jobs
        while [ $(jobs -r | wc -l) -ge "${MAX_JOBS}" ]; do
            sleep 0.1
        done
        report_package_coverage "${pkg}" &
    fi
done

wait

# Summary and exit
failed_packages=()
passed_packages=()

for pkg in ${modified_packages}; do
    if [ -d "${pkg}" ]; then
        pkg_name_clean=$(echo "${pkg}" | sed 's|/$||' | sed 's|/|_|g')
        pkg_log="${LOG_DIR}/${pkg_name_clean}.log"
        pkg_status="${LOG_DIR}/${pkg_name_clean}.status"

        echo "============================================================"
        echo "Evaluating coverage for package: ${pkg}"
        echo "============================================================"
        [ -f "${pkg_log}" ] && cat "${pkg_log}"

        status=$(cat "${pkg_status}" 2>/dev/null || echo 1)
        if [ "${status}" -ne 0 ]; then
            failed_packages+=("${pkg}")
        else
            passed_packages+=("${pkg}")
        fi
    fi
done

echo "============================================================"
echo "Coverage Evaluation Summary"
echo "============================================================"
if [ ${#passed_packages[@]} -gt 0 ]; then
    echo "✅ Passed: ${#passed_packages[@]} packages"
fi

if [ ${#failed_packages[@]} -gt 0 ]; then
    echo "❌ Failed: ${#failed_packages[@]} packages"
    for pkg in "${failed_packages[@]}"; do
        echo "  - ${pkg}"
    done
    exit 1
fi
