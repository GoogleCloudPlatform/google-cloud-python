The directory contains scripts which can be used to migrate client library code
from split repositories located at http://github.com/googleapis/python-* into
this mono repository. Each such split repo becomes a "package" (under
`packages/`) in this repo.

These two scripts should be called one after the other for each split repo being
migrated, but this process can be done for multiple repos at once. In other
words, the order in which the PRs are created or merged does not matter:
  - [single-library.git-migrate-history.sh](single-library.git-migrate-history.sh)
    imports the files in the split repo into a package in this repo. In doing
    so, it also imports the associated git history. This script opens a PR, which
    must be merge-committed once approved, in order to preserve that history.
  - [single-library.post-process.api-files.sh](single-library.post-process.api-files.sh)
    applies needed package-specific migration changes that only touch files
    specific to the repo being migrated. It locally commits the changes to this
    repo but does not open a new PR. Typically this commit is included in the PR
    created by the previous script.
    
The output of this script should be merged before this script is called again,
as it modifies shared files:
  - [multiple-library.post-process.sh](multiple-library.post-process.sh), for a
    given list of migrated packages, applies package-specific migration changes
    that touch files shared among all packages in this repo. It does this by
    first calling the script below for each specified package, and then invoking
    OwlBot locally to post-process all the specified packages at once. It
    locally commits the changes to this repo but does not open a PR.
    - [single-library.post-process.common-files.sh](single-library.post-process.common-files.sh)
      applies package-specific migration changes that touch files shared among
      multiple packages. It locally commits the changes to this repo but does
      not open a PR.

The following script cleans up the now-migrated split repo:
- [delete-everything-split-repo.sh](delete-everything-split-repo.sh) will remove
  almost all files from a split repository and update the README.rst file to
  indicate that the repository is archived.

