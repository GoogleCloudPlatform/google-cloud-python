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
# This script will update the various metadata files migrated from the split
# repo into formats and locations suitable for the mono-repo. This script deals
# with common (shared) files, and thus CANNOT be called in parallel for
# individual APIs, since each run touches shared files and would thus lead to
# merge conflicts.
#
# Pre-condition: the split repo has been copied to the path indicated when
# calling this function.
#
# **** NOTE: You would typically not call this directly unless debugging. Use
# multiple-library.post-process.common-files.sh instead. ****
#
# INVOCATION from the mono-repo root directory:
#   single-library.post-process.common-files.sh PACKAGE_PATH
# where PACKAGE_PATH is the path (absolute or relative) from pwd to the
# directory in google-cloud-python holding the copied split repo. Typically, if
# running from the top level of google-cloud-python, this is something like
# "packages/google-cloud-APINAME"
# EXAMPLE from the root directory of the monorepo:
#   ./scripts/split_repo_migration/single-library.post-process.common-files.sh packages/google-cloud-speech
#
# For debugging/developing this script, you can have additional parameters:
#  ./single-library.post-process.common-files.sh SPLIT_REPO_DIR MONOREPO_DIR MONOREPO_PACKAGE_NAME
# Example from this script's directory:
#  ./single-library.post-process.common-files.sh ../../../python-speech ../../ google-cloud-speech

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

# We require executing the script so that an early exit (explicitly or via -e)
# does not kill the user's shell.
                                     
# `-e` enables the script to automatically fail when a command fails
set -e


NOP="echo -n"
DEBUG=""  # "yes"  # set to blank for a real run, or non-blank to prevent modifying the split-repo
MESSAGE=""

# Use indent of 4 when formatting json for readability
INDENT_JSON="--indent 4"

[[ -n ${DEBUG} ]] && {
  # Comment out some commands for development/debugging
  RM='echo "*** would run:" rm'
  GIT='echo "*** would run:" git'

  # It's easier to debug if keys don't get reordered
  SORT_JSON_KEYS="" 
} || {
  # Real commands for actual runs
  RM='rm'
  GIT='git'

  # Sort keys for easier look-up.
  SORT_JSON_KEYS="--sort-keys"
}

if [ $# -lt 1 ]
then
  echo "Usage: $0 PATH/TO/PACKAGE_NAME"
  exit 1
fi

# variable naming convention
#   PATH_* are absolute system paths
#   MONOREPO_PATH_* are paths relative to the root of the monorepo
#   MONOREPO_* are values used in the monorepo

# In a real run for a split repo already copied to the mono-repo, $1 would be
# specified as `packages/PACKAGE_NAME`. For developing this script, it's useful
# to specify $1 as the name of a completely separate split repo, in which case
# specifying $2 and $3 is also useful (see below).
PATH_PACKAGE="$(realpath "$1")"

# The optional second argument is useful for development: it specifies a different
# directory for the monorepo (rather than deriving it from $1).
PATH_MONOREPO="${2:-$(dirname $(dirname $PATH_PACKAGE))}"
PATH_MONOREPO="$(realpath "${PATH_MONOREPO}")"

# The optional third argument is useful for development: it specifies what the the
# package name should be for this API once migrated to the monorepo. This can be
# inferred if we've already migrated the split repo to the correct location, but
# otherwise needs to be specified, since it differs from the split repo name
# (for example, the repo "python-speech" defines a package
# "google-cloud-speech").
MONOREPO_PACKAGE_NAME="${3:-$(basename ${PATH_PACKAGE})}"

MONOREPO_PATH_PACKAGE="packages/${MONOREPO_PACKAGE_NAME}"

cat <<EOF
Post-processing ${MONOREPO_PACKAGE_NAME}
  PATH_PACKAGE:          ${PATH_PACKAGE}
  PATH_MONOREPO:         ${PATH_MONOREPO}
  MONOREPO_PACKAGE_NAME: ${MONOREPO_PACKAGE_NAME}
  MONOREPO_PATH_PACKAGE: ${MONOREPO_PATH_PACKAGE}
EOF

pushd "${PATH_MONOREPO}" >& /dev/null

## START release-please config migration ########################################
# variable prefix: RPC_*

RPC_MONO_PATH="release-please-config.json"
echo "Migrating: ${RPC_MONO_PATH}"

# enable this if we want sorted keys. Keep it disabled to append new entries at
# the end (useful for debugging):
RPC_SORT_KEYS="${SORT_JSON_KEYS}"

RPC_SPLIT_PATH="${PATH_PACKAGE}/release-please-config.json"
jq ${INDENT_JSON} ".packages.\".\" += {component: \"${MONOREPO_PACKAGE_NAME}\"}" "${RPC_SPLIT_PATH}" | sponge "${RPC_SPLIT_PATH}"
RPC_NEW_OBJECT="$(jq '.packages."."' "${RPC_SPLIT_PATH}")"

jq ${INDENT_JSON} ${RPC_SORT_KEYS} --argjson newObject "${RPC_NEW_OBJECT}" ". * {\"packages\": {\"${MONOREPO_PATH_PACKAGE}\": \$newObject}}" ${RPC_MONO_PATH} | sponge ${RPC_MONO_PATH}
$RM ${RPC_SPLIT_PATH}
## END release-please config migration

## START release-please manifest migration ########################################
# variable prefix: RPM_*
RPM_MONO_PATH=".release-please-manifest.json"
echo "Migrating: ${RPM_MONO_PATH}"

# enable this if we want sorted keys. Keep it disabled to append new entries at
# the end (useful for debugging):
RPM_SORT_KEYS="${SORT_JSON_KEYS}"

RPM_SPLIT_PATH="${PATH_PACKAGE}/.release-please-manifest.json"
RPM_VERSION="$(jq '."."' "${RPM_SPLIT_PATH}")"
jq ${INDENT_JSON} ${RPM_SORT_KEYS}  ". * {\"${MONOREPO_PATH_PACKAGE}\": ${RPM_VERSION}}" ${RPM_MONO_PATH} | sponge ${RPM_MONO_PATH}
$RM ${RPM_SPLIT_PATH}
## END release-please manifest migration

## START migrate release tags ########################################
# We need to migrate the release tags since that is what release-please uses to
# get the next release number.We use ${RPM_VERSION} from the previous section
# variable prefix: LRT_*
echo "Replicating latest release tag"

LRT_VERSION="${RPM_VERSION//\"/}"

# any of the gapic_version.py files will do: they all match
LRT_VERSION_FILE="$(find ${MONOREPO_PATH_PACKAGE} -name "gapic_version.py" | head -n 1)"
LRT_SHA=$(git log --format=oneline ${LRT_VERSION_FILE} | grep release | head -n 1 | awk '{ print $1 }')
$GIT tag -f ${MONOREPO_PACKAGE_NAME}-v${LRT_VERSION} ${LRT_SHA}
$GIT push --tags
## END migrate release tags




## START .repo-metadata.json migration ########################################
# variable prefix: RMJ_*
RMJ_MONO_PATH="${MONOREPO_PATH_PACKAGE}/.repo-metadata.json"
echo "Migrating: ${RMJ_MONO_PATH}"

[[ -z ${DEBUG} ]] || { \
RMJ_SPLIT_PATH="${PATH_PACKAGE}/.repo-metadata.json"
cp ${RMJ_SPLIT_PATH} ${RMJ_MONO_PATH}
}

jq ${INDENT_JSON} '.repo = "googleapis/google-cloud-python"' ${RMJ_MONO_PATH} | sponge ${RMJ_MONO_PATH}
jq -r ".issue_tracker" "${RMJ_MONO_PATH}" | grep -q "github.com"  && {
  jq ${INDENT_JSON} '.issue_tracker = "https://github.com/googleapis/google-cloud-python/issues"' ${RMJ_MONO_PATH} | sponge ${RMJ_MONO_PATH}
} || { $NOP ; }
## END .repo-metadata.json migration


## START .pre-commit-config migration ########################################
# variable prefix: PCC_*
PCC_MONO_PATH=".pre-commit-config.yaml"
echo "Migrating: ${PCC_MONO_PATH}"

PCC_SPLIT_PATH="${PATH_PACKAGE}/.pre-commit-config.yaml"

# We only copy this if it doesn't already exist in the mono-repo.
[[ ! -f "${PCC_MONO_PATH}" ]] && [[ -f "${PCC_SPLIT_PATH}" ]] && {
  cp ${PCC_SPLIT_PATH} ${PCC_MONO_PATH}
} || { $NOP ; }
$RM -f ${PCC_SPLIT_PATH}
## END .pre-commit-config migration

### Delete file that was copied over from owlbot-staging/
${RM} -f "${PATH_PACKAGE}/${MONOREPO_PACKAGE_NAME}.txt"


## START commit changes #############################################
echo "Committing changes locally"
${GIT} add .
${GIT} commit -am "migration(${MONOREPO_PACKAGE_NAME}): adjust metadata and automation configs"
## END commit changes

popd >& /dev/null # "${PATH_MONOREPO}"

[[ -z ${MESSAGE} ]] && echo "Done." || echo -e "Done, with a message:\n\n${MESSAGE}\n"



