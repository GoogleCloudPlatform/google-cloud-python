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

# ci/adhoc/setup_adhoc.sh
# This script is sourced by system.sh to check for ad-hoc status and update PACKAGES_TO_TEST.
# It fails open and is isolated to minimize impact on production.

TRIGGER_ADHOC="false"

echo "Checking for adhoc test label on PR #${KOKORO_GITHUB_PULL_REQUEST_NUMBER}..."
# Simple, unauthenticated call to check labels (capturing headers for rate limit debugging)
CURL_OUTPUT=$(curl -s -i -H "User-Agent: Kokoro-AdHoc-Checker" "https://api.github.com/repos/googleapis/google-cloud-python/issues/${KOKORO_GITHUB_PULL_REQUEST_NUMBER}/labels" || true)

# Separate headers and body
# Using awk to find the blank line separating headers from body
HEADERS=$(echo "$CURL_OUTPUT" | awk 'BEGIN{RS="\r\n\r\n"} NR==1' || true)
LABELS_JSON=$(echo "$CURL_OUTPUT" | awk 'BEGIN{RS="\r\n\r\n"} NR==2' || true)

# --- DEBUGGING: Extract and print Rate Limit Headers ---
echo "---------------------------------------------------------------"
echo "DEBUG: GitHub API Rate Limit Status:"
echo "$HEADERS" | grep -i "^x-ratelimit-limit:" | tr -d '\r' || true
echo "$HEADERS" | grep -i "^x-ratelimit-remaining:" | tr -d '\r' || true
echo "$HEADERS" | grep -i "^x-ratelimit-used:" | tr -d '\r' || true

# Convert reset time to human-readable if date is available, otherwise show raw
RESET_EPOCH=$(echo "$HEADERS" | grep -i "^x-ratelimit-reset:" | awk '{print $2}' | tr -d '\r' || true)
if [[ -n "$RESET_EPOCH" ]]; then
    if date -d "@$RESET_EPOCH" >/dev/null 2>&1; then
        RESET_HUMAN=$(date -d "@$RESET_EPOCH" "+%Y-%m-%d %H:%M:%S UTC")
        echo "x-ratelimit-reset: $RESET_HUMAN ($RESET_EPOCH)" 
    else
        echo "x-ratelimit-reset: $RESET_EPOCH"
    fi
fi
echo "---------------------------------------------------------------"

if [[ -z "$LABELS_JSON" ]] || [[ "$HEADERS" == *"HTTP/1.1 4"* ]] || [[ "$HEADERS" == *"HTTP/1.1 5"* ]]; then
    echo "==============================================================="
    echo "WARNING: Failed to fetch labels or received error from GitHub API!"
    echo "Ad-hoc tests will NOT be triggered."
    echo "==============================================================="
else
    # Use jq to parse github labels (works as long as jq is available in python-multi image).
    IS_ADHOC=$(echo "$LABELS_JSON" | jq -r 'if type == "array" then any(.name == "test:adhoc") else false end' 2>/dev/null || echo "false")

    if [[ "$IS_ADHOC" == "true" ]]; then
        TRIGGER_ADHOC="true"
        echo "Adhoc test label 'test:adhoc' found!"
    else
        if [[ "$LABELS_JSON" != "["* ]]; then
            API_ERR_MSG=$(echo "$LABELS_JSON" | jq -r '.message // "Unknown error"' 2>/dev/null || echo "Unknown error")
            echo "==============================================================="
            echo "WARNING: Failed to fetch PR labels from GitHub API!"
            echo "Error Message: $API_ERR_MSG"
            echo "This might be due to API Rate Limiting."
            echo "Ad-hoc tests will NOT be triggered."
            echo "==============================================================="
        else
            echo "Adhoc test label 'test:adhoc' not found."
        fi
    fi
fi

if [[ "$TRIGGER_ADHOC" == "true" ]]; then
    echo "Running ad-hoc package selection..."
    # Ensure the runner script exists before sourcing
    if [[ -f "ci/adhoc/adhoc_test_runner.sh" ]]; then
        source ci/adhoc/adhoc_test_runner.sh

        echo "Deduplicating packages..."
        # Deduplication using Associative Arrays (Requires Bash 4+)
        declare -A unique_packages
        for pkg in "${PACKAGES_TO_TEST[@]}"; do
            [[ -n "$pkg" ]] && unique_packages["$pkg"]=1
        done
        for pkg in $ADHOC_PACKAGES; do
            [[ -n "$pkg" ]] && unique_packages["$pkg"]=1
        done

        PACKAGES_TO_TEST=("${!unique_packages[@]}")

        echo "Combined packages to test: ${PACKAGES_TO_TEST[*]}"
    else
        echo "==============================================================="
        echo "WARNING: ci/adhoc/adhoc_test_runner.sh not found!"
        echo "Ad-hoc packages will NOT be added."
        echo "==============================================================="
    fi
fi
