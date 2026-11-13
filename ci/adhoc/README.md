# Ad-Hoc Package Testing

## Overview
Ad-hoc package testing allows you to run CI tests for a specific subset of packages or predefined package groups without the need for intrusive and/or temporary mods to the package code to trigger a CI job run. Key use cases include:

* **Downstream Dependency Smoke Tests:** If you update a core library (like `google-api-core`), the diff detector only sees the core library. Ad-hoc lets you explicitly include major downstream consumers (like `storage`) to verify compatibility.
* **Debugging specific package failures:** If you want to look at just one OR two failing packages out of a larger group of failing packages, it can be helpful to run them in isolation in a separate PR (so that your prospective changes don't have to wait on all the other packages). This allows you to easily flag which packages you want to investigate by potentially starting with a baseline test with no changes (i.e. does this fail due to an externality OR due to a change in the code)?
* **Testing CI infrastructure updates:** If you are changing `.kokoro/system.sh` or root scripts, the standard diff detector won't trigger tests because no package folders changed. Ad-hoc allows you to test your CI scripts using a single lightweight package without polluting package code with dummy comments.

## How It Works
The ad-hoc testing system reads configuration files in the `ci/adhoc/` directory to determine which packages to test. It is triggered via the `test:adhoc` GitHub label on Pull Requests.

When triggered, the ad-hoc selected packages are **merged** with any packages automatically detected by the CI system (e.g., packages modified in the current PR). The final combined list is automatically deduplicated, ensuring each package is tested only once.

## Configuration Files

These files are located in the `ci/adhoc/` directory.

### 1. `.standalone_package_list.txt`
This file lists the specific packages or groups you want to test.

*   **To test an individual package:** Add a line starting with `package: ` (be sure to include the colon and space) followed by the package directory name.
    *   *Example:* `package: google-cloud-dns`
*   **To test a group of packages:** Add a line starting with `group: ` (be sure to include the colon and space) followed by the group name. NOTE: groups are defined in the file: `.package_groups.txt`
    *   *Example:* `group: handwritten`

### 2. `.package_groups.txt`
This file defines groups of commonly tested packages for convenience of the team. Groups such as all handwritten, all core, all hybrids, most widely used, etc. can be defined here.

*   **Format:** Each package in a group should be on its own line, prefixed by the group name, colon, and a space.
    *   *Example:*
        ```text
        handwritten: google-cloud-translate
        handwritten: google-cloud-logging
        core: google-api-core
        ```

#### 💡 Pro Tip
You can mix packages and groups in `.standalone_package_list.txt`. The system will automatically expand groups and deduplicate the list!

## Usage

1.  **Edit Configuration:** Open `ci/adhoc/.standalone_package_list.txt` and add the packages or groups you want to test.
2.  **Trigger Tests:**
    *   **New PR:** Commit the changes and open a Pull Request form.
    *   **Activate Label:** Add the `test:adhoc` label to your PR form in the GitHub UI. If you miss this step, simply applying the label won't magically launch the tests the way `kokoro-force-run` does. The label is only checked when a commit is detected.
    *   **Existing PR:** Commit and push the changes to your branch. If the label is already present, pushing a new commit will trigger the tests.
