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

# Sample usage:
#
# git-migrate-history.sh \
# "googleapis/python-speech" \
# "~/temp/google-cloud-python" \
# "" \
# "" \
# ".github/.OwlBot.yaml"
#
# This invocation runs migration script on python-speech, where the source path is root directory,
# nothing is ignored, and .OwlBot.yaml is being kept.

set -ex

[[ "${BASH_SOURCE[0]}" != "${0}" ]] && EXIT=return || EXIT=exit

if [ $# -lt 3 ]
then
  echo "Usage: $0 <source-repo> <target-repo> <source-path> [folders,to,skip] [files,to,keep] [branch-name] [issue-number]"
  $EXIT 1
fi

# source GitHub repository. format: <owner>/<repo>
SOURCE_REPO=$1

# destination GitHub repository. format: <owner>/<repo>
TARGET_REPO=$2  # Path to google-cloud-python

# path in the source repo to copy code from. Defaults to the root directory
SOURCE_PATH=$3

# comma-separated list of files/folders to skip
IGNORE_FOLDERS=$4

# keep these specific files that would otherwise be deleted by IGNORE_FOLDERS
KEEP_FILES=$5

# override the HEAD branch name for the migration PR
BRANCH=$6

# GitHub issue number
ISSUE_NUMBER=$7

if [[ -z "${BRANCH}" ]]
then
  # default the branch name to be generated from the source repo name
  BRANCH=$(basename ${SOURCE_REPO})-migration
fi
export FILTER_BRANCH_SQUELCH_WARNING=1

# create a working directory
WORKDIR="$(mktemp -d -t code-migration-XXXXXXXXXX)"
echo "Created working directory: ${WORKDIR}"

pushd "${WORKDIR}"  # cd into workdir

echo "Cloning source repository: ${SOURCE_REPO}"
git clone --recurse-submodules "git@github.com:${SOURCE_REPO}.git" source-repo

pushd source-repo

DISTRIBUTION_NAME=$(jq -r '.distribution_name' .repo-metadata.json) # -r removes quotes around the name.
TARGET_PATH="packages/${DISTRIBUTION_NAME}"

git remote remove origin

# prune only files within the specified directory
if [[ ! -z "${SOURCE_PATH}" ]]
then
  echo "Pruning commits only including path: ${SOURCE_PATH}"
  git filter-branch \  # rewrites history... unsafe
    --prune-empty \
    --subdirectory-filter "${SOURCE_PATH}"
fi

if [[ ! -z "${IGNORE_FOLDERS}" ]]
then
  echo "Ignoring folder: ${IGNORE_FOLDERS}"
  mkdir -p "${WORKDIR}/filtered-source"
  FOLDERS=$(echo ${IGNORE_FOLDERS} | tr "," " ")
  # remove files/folders we don't want
  FILTER="(rm -rf ${FOLDERS} || true)"
  if [[ ! -z "${KEEP_FILES}" ]]
  then
    KEEP_FILES_SPACES=($(echo ${KEEP_FILES} | tr "," " "))
    LAST_ELEMENT=$(( ${#KEEP_FILES_SPACES[@]} - 1 ))
    KEEP_FILE_COMMANDS=""
    for file in "${KEEP_FILES_SPACES[@]}"
    do
      if [[ $file == "${KEEP_FILES_SPACES[$LAST_ELEMENT]}" ]]
      then
        KEEP_FILE_COMMANDS+="git checkout -- ${file} 2>/dev/null || true"
      else 
        KEEP_FILE_COMMANDS+="git checkout -- ${file} 2>/dev/null || true; "
      fi   
    done
    # restore files to keep, silence errors if the file doesn't exist
    FILTER="${FILTER}; ${KEEP_FILE_COMMANDS}"
  fi
  git filter-branch \
    --force \
    --prune-empty \
    --tree-filter "${FILTER}"
fi

# reorganize the filtered code into the desired target locations
echo "Moving files to destination path: ${TARGET_PATH}"
git filter-branch \
  --force \
  --prune-empty \
  --tree-filter \
    "git submodule update --init --recursive; find . -mindepth 2 -name .git -exec rm -rf {} +; git submodule update --init --recursive; find . -mindepth 2 -name .git -exec rm -rf {} +; shopt -s dotglob; mkdir -p ${WORKDIR}/migrated-source; mv * ${WORKDIR}/migrated-source; mkdir -p ${TARGET_PATH}; { mv ${WORKDIR}/migrated-source/* ${TARGET_PATH} || echo 'No files to move' ; }"

# back to workdir
popd

# merge histories
pushd $TARGET_REPO

REMOTE="remote.${SOURCE_REPO}"
git remote add --fetch ${REMOTE} ${WORKDIR}/source-repo
git checkout -B "${BRANCH}"
git merge --allow-unrelated-histories ${REMOTE}/main --no-edit

echo "Success"

popd # back to workdir

# Do a diff between source code split repo and migrated code.
git clone --recurse-submodules "git@github.com:${SOURCE_REPO}.git" source-repo-validation  # Not ideal to clone again.
find source-repo-validation -name .git -exec rm -rf {} +  # That folder is not needed for validation.

DIFF_FILE="${WORKDIR}/diff.txt"
if diff -r "${TARGET_REPO}/${TARGET_PATH}" source-repo-validation > "${DIFF_FILE}" ; then
  echo "No diff"
else
  echo "Diff non-empty. See ${DIFF_FILE}"
  $EXIT 1
fi

pushd "${TARGET_REPO}" >& /dev/null  # To target repo

# For postprocessing of the batch migration script.
mkdir -p owl-bot-staging/${DISTRIBUTION_NAME}/${DISTRIBUTION_NAME}
touch owl-bot-staging/${DISTRIBUTION_NAME}/${DISTRIBUTION_NAME}/${DISTRIBUTION_NAME}.txt
git add owl-bot-staging
git commit -m "Trigger owlbot post-processor"

git push -u origin "${BRANCH}" --force

# create pull request
if which gh > /dev/null
then
  while ! gh pr create --draft --title "chore(migration): Migrate code from ${SOURCE_REPO} into ${TARGET_PATH}" --body "$(echo -e "See #${ISSUE_NUMBER}. \n\nThis PR should be merged with a merge-commit, not a squash-commit, in order to preserve the git history.")" ; do
    echo "** PR creation command FAILED (${SOURCE_REPO} --> ${TARGET_PATH}) : sleeping & retrying"
    sleep 30s
  done
else
  hub pull-request --draft -m "migrate code from ${SOURCE_REPO}"
fi

popd >& /dev/null

# Some of the post-processing scripts require the ${DISTRIBUTION_NAME}. We
# output it here so they can use the same value we derived, rather than risking
# diverging computations of the value.
echo "${DISTRIBUTION_NAME}"
