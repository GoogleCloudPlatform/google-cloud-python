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

# `-e` enables the script to automatically fail when a command fails
# `-o pipefail` sets the exit code to non-zero if any command fails,
# or zero if all commands in the pipeline exit successfully.
set -eo pipefail

pwd

# If NOX_SESSION is set, it only runs the specified session,
# otherwise run all the sessions.
NOX_SESSION_ARG=""

# IF NOX_FILE is set, it runs the specific nox file,
# otherwise it runs noxfile.py in the package directory.
NOX_FILE_ARG=""

[[ -z "${NOX_SESSION}" ]] || NOX_SESSION_ARG="-s ${NOX_SESSION}"

[[ -z "${NOX_FILE}" ]] || NOX_FILE_ARG="-f ${NOX_FILE}"

python3 -m nox ${NOX_SESSION_ARG} $NOX_FILE_ARG
