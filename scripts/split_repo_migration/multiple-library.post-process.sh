#!/bin/bash
# Copyright 2023 Google LLC
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

# This script was written as part of a project to migrate
# split repositories to the mono-repository google-cloud-python.
#
# This script takes a list of packages. It will first call
# single-library.post-process.common-files.sh on each package to update the
# various metadata files migrated from the split repo. It will then cause the
# OwlBot post-processor to run once (via Docker) for all the repos together to
# update the appropriate files.
#
# This script deals with common (shared) files, and thus CANNOT be called in
# parallel for individual APIs, since each run touches shared files and would
# thus lead to merge conflicts.
#
# Pre-condition: the split repo has been copied to the path indicated when
# calling this function.
#
# INVOCATION 
#   multiple-library.post-process.common-files.sh DIR PACKAGE [PACKAGE...]
# where dir is the path to the monorepo (relative dirs, like "." are fine) and
# PACKAGE is the name of a (newly migrated) package in the monorepo.
# EXAMPLE from the root directory of the monorepo:
#   ./scripts/split_repo_migration/multiple-library.post-process.common-files.sh . google-cloud-speech
#

# sourced vs execution detection obtained from https://stackoverflow.com/a/28776166
SOURCED=0
if [ -n "$ZSH_VERSION" ]; then 
  case $ZSH_EVAL_CONTEXT in *:file) SOURCED=1;; esac
elif [ -n "$KSH_VERSION" ]; then
  [ "$(cd -- "$(dirname -- "$0")" && pwd -P)/$(basename -- "$0")" != "$(cd -- "$(dirname -- "${.sh.file}")" && pwd -P)/$(basename -- "${.sh.file}")" ] && SOURCED=1
elif [ -n "$BASH_VERSION" ]; then
  (return 0 2>/dev/null) && SOURCED=1 
else # All other shells: examine $0 for known shell binary filenames.
     # Detects `sh` and `dash`; add additional shell filenames as needed.
  case ${0##*/} in sh|-sh|dash|-dash) SOURCED=1;; esac
fi

(( ${SOURCED} != 1 )) || { \
  echo "Please do not source this script, but execute it directly."
  return -10
}

# to allow echoing commands for debugging, precede the following with something
# like "echo"
GIT="git"

# We require executing the script so that an early exit (explicitly or via -e)
# does not kill the user's shell.
                                     
# `-e` enables the script to automatically fail when a command fails
set -e

MESSAGE=""

if [ $# -lt 2 ]
then
  echo "Usage: $0 REPO_ROOT PACKAGE...."
  exit 1
fi

PATH_MONOREPO="$(realpath "$1")"
cat <<EOF
Post-processing multiple pacakges
  PATH_MONOREPO:         ${PATH_MONOREPO}
EOF
shift

pushd "${PATH_MONOREPO}" >& /dev/null

BRANCH="migration-batch-${USER}-$$"
${GIT} checkout -b "${BRANCH}"

# variable naming convention
#   PATH_* are absolute system paths
#   MONOREPO_PATH_* are paths relative to the root of the monorepo
#   MONOREPO_* are values used in the monorepo

for MONOREPO_PACKAGE_NAME in "$@"
do
  PATH_PACKAGE="$(realpath "packages/${MONOREPO_PACKAGE_NAME}")"
  MONOREPO_PATH_PACKAGE="packages/${MONOREPO_PACKAGE_NAME}"
  cat <<EOF
  MONOREPO_PACKAGE_NAME: ${MONOREPO_PACKAGE_NAME}
EOF
  ./scripts/split_repo_migration/single-library.post-process.common-files.sh "${MONOREPO_PATH_PACKAGE}"

  # we need the following directory present so OwlBot will include it in its
  # processing below.
  mkdir -p owl-bot-staging/${MONOREPO_PACKAGE_NAME}
done


## START invoke OwlBot post-processor ########################################
echo -e "\nInvoking owl-bot post-processor locally. PLEASE WAIT...."
docker pull gcr.io/cloud-devrel-public-resources/owlbot-python-mono-repo:latest
docker run --user $(id -u):$(id -g) --rm --mount type=bind,source=${PATH_MONOREPO},destination=/repo -w /repo gcr.io/cloud-devrel-public-resources/owlbot-python-mono-repo:latest
## END invoke OwlBot post-processor

## START commit changes #############################################
echo "Committing changes locally"
${GIT} add .
${GIT} commit -am "$(echo -e "migration: post-process\n\nThis includes post processing for:\n${*//\"/}")"
${GIT} push -u origin "${BRANCH}" --force
gh pr create --draft --title "chore(migration): Update common files for batch migration" --body "This updates the common files for the migration batch that contains ${*//\"/}"
${GIT} checkout main # to restore to a known state and allow reruns
## END commit changes

popd >& /dev/null # "${PATH_MONOREPO}"

[[ -z ${MESSAGE} ]] && echo "Done." || echo -e "Done, with a message:\n\n${MESSAGE}\n"
