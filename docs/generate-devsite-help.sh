#!/bin/bash

set -e
REPOROOT=$(git rev-parse --show-toplevel)

if [[ -z "$1" ]]
then
  declare -r VERSION="1.0.0"
else
  declare -r VERSION=$1
fi

DEVSITE_STAGING_BUCKET=docs-staging-v2

rm -rf $REPOROOT/docs/output
mkdir -p $REPOROOT/docs/output

cp $REPOROOT/docs/devsite-help/* $REPOROOT/docs/output
cd $REPOROOT/docs/output

# Create the docs metadata.
docuploader create-metadata \
  --name help \
  --version $VERSION \
  --language python

# Upload the
docuploader upload . \
  --staging-bucket="$DEVSITE_STAGING_BUCKET" \
  --destination-prefix="docfx-" \
  --metadata-file="docs.metadata"

echo 'Done'