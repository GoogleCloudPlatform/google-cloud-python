#!/bin/bash
# Copyright 2026 Google LLC
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

# Script to determine ad-hoc packages to test.
# This script is intended to be sourced from main test scripts.
#
# Precondition: This script assumes it is sourced from the project root (as set by system.sh).

ADHOC_DIR="ci/adhoc"
STANDALONE_LIST="${ADHOC_DIR}/.standalone_package_list.txt"
GROUPS_FILE="${ADHOC_DIR}/.package_groups.txt"

if [[ ! -f "$STANDALONE_LIST" ]]; then
    echo "Warning: $STANDALONE_LIST not found."
    return 0 2>/dev/null || exit 0
fi

if [[ ! -f "$GROUPS_FILE" ]]; then
    echo "Warning: $GROUPS_FILE not found."
    return 0 2>/dev/null || exit 0
fi

# Grab individual packages
adhoc_packages=$(grep "^package:" "$STANDALONE_LIST" | cut -d':' -f2 | tr -d '\r' | xargs || true)

# Grab requested groups
requested_groups=$(grep "^group:" "$STANDALONE_LIST" | cut -d':' -f2 | tr -d '\r' | xargs || true)

# Expand groups
for group in $requested_groups; do
    group_pkgs=$(grep "^$group:" "$GROUPS_FILE" | cut -d':' -f2 | tr -d '\r' | xargs || true)
    adhoc_packages="$adhoc_packages $group_pkgs"
done

# Convert to unique list (deduplicate our adhoc packages)
ADHOC_PACKAGES=$(echo "$adhoc_packages" | tr ' ' '\n' | sort -u | xargs)

export ADHOC_PACKAGES
