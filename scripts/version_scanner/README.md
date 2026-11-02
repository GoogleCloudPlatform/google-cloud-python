# Automated Dependency Version Scanner

This tool scans the repository for hardcoded references to specific dependency versions (like Python 3.7) that need to be upgraded or removed.

## Usage

Run the script from the repository root:

```bash
python3 scripts/version_scanner/version_scanner.py -d <dependency> -v <version> [options]
```

### Options

*   `-d`, `--dependency`: Name of the dependency (e.g., python, protobuf)
*   `-v`, `--version`: Specific version to search for (e.g., 3.7, 4.25.8)
*   `-p`, `--path`: Root directory to scan (defaults to current directory)
*   `--package`: Specific subdirectory filter (useful for monorepos)
*   `--package-file`: Path to a file containing a list of package directories to scan (e.g., `scripts/version_scanner/small_package_list.txt`)
*   `--config`: Path to the regex configuration file (defaults to scripts/version_scanner/regex_pattern_config.yaml)
*   `-o`, `--output`: Path to the output CSV file (defaults to <dependency>-<version>-<timestamp>.csv)
*   `--github-repo`: GitHub repository URL base (defaults to https://github.com/googleapis/google-cloud-python)
*   `--branch`: GitHub branch for links (defaults to main)

## Installation & Setup

By default, the core scanner only depends on Python's standard library and **`pyyaml`** to read the configuration file.

If you want to use the Google Drive upload feature (`--upload`), you must install the optional Google API client dependencies:
```bash
pip install -r scripts/version_scanner/requirements.txt
```

## Scope: Handwritten vs. Generated Code

> [!NOTE]
> **This scanner is primarily intended for auditing handwritten code, configuration files, CI scripts, and documentation.**
> You do **not** need to scan or manually edit auto-generated GAPIC libraries. Any dependency updates for generated code are handled upstream by editing the generator templates in the `gapic-generator-python` repository. When the templates are updated, the changes naturally trickle downstream to correct all generated client libraries upon the next regeneration.

## Limitations

*   **Single-Line Matching Only**: The scanner processes files line-by-line to ensure high performance and simplicity. Consequently, version declarations or dependency lists that span across multiple lines (such as multiline lists in a `setup.py` file) will not be caught by the regex patterns.

## Configuration

The scanner uses a YAML configuration file (`regex_pattern_config.yaml`) to define rules and regex patterns.

## Matrix File Format

When using `--matrix-file`, you must provide a YAML file specifying dependencies and versions.

### Example
```yaml
python:
  - "3.10"
  - "3.11"
protobuf: "4.25.8"
```

> [!IMPORTANT]
> **Versions must be specified as quoted strings** (e.g., `"3.10"`, not `3.10`). This prevents YAML parsers from converting them to floats (which would truncate `3.10` to `3.1`).

## Ignoring Directories and Files

In order to ignore files OR entire directories, you can add ignore patterns to the `.scannerignore` file located in the same directory as the script (`scripts/version_scanner/.scannerignore`). Ignore patterns should be added one per line.

### Features
- **Case-insensitive**: All patterns are matched case-insensitively.
- **Globbing**: Supports standard shell globbing patterns (e.g., `*.jpg`, `test_*`).
- **Subpaths**: You can specify subpaths (e.g., `packages/pkg_a/.nox`).
- **Root Anchoring**: Patterns starting with a slash `/` are anchored to the root of the scan (e.g., `/packages` ignores the `packages` directory at root, but not `some/other/packages`).

---

---

## Universal Prompt for EOL Runtime & Dependency Migration

### Context & Overview

#### Overview
This prompt is provided as an example and outlines the approach to update Python packages to drop support for end-of-life Python runtimes (3.7, 3.8, 3.9) OR for deprecated dependencies, and ensure the packages are configured for modern Python. This may help speed up your ability to resolve version mismatches. This prompt is provided with no guarantees, your mileage may vary. LLMs may make mistakes, always double check the LLM's work and test thoroughly.

#### High-Level Strategy
- **One Branch Per Package**: To keep PRs manageable and isolated, we suggest a dedicated worktree and branch for each package (e.g., `feat/drop-<dependency>-<version>-<package-name>` i.e. `feat/drop-protobuf-4.25.8-google-cloud-bigquery`).
- **Small & Reversible Commits**: Group changes into logical commits (Metadata, Nox, Docs, Cleanup, Tests) following Conventional Commits.

---

### Per-Package Workflow

Follow these steps for each package in the target list. Context and warnings are provided inline before the steps where they apply.

#### Step 1: Sync & Branch
1. Ensure `main` branch is up to date.
2. Create the feature branch: `git checkout -b feat/drop-<dependency>-<version>-<package-name>`.

#### Step 2: Scan (Baseline)
1. Run the `version_scanner` for the package to get a list of all occurrences of the dependency and version.
   > [!TIP]
   > Use `# version-scanner: ignore` or `ignore-next-line` in code to silence true false-positives and maintain clean reports.

---

#### 💡 Context for Step 3: Standards & Cleanup
*Before applying changes, review these standards to ensure consistency:*

##### Runtime Version Checks
- **Standard**: Use `sys.version_info < (X, Y)`.
- **Rationale**: Python compares tuples lexicographically, making this robust.
- **Avoid**: `sys.version_info.minor < Y` or string conversions.

##### Pytest Skips
- **Standard**: `@pytest.mark.skipif(sys.version_info < (X, Y), reason="Requires Python X.Y+")`.
- **Avoid**: String-based conditions like `@pytest.mark.skipif("sys.version_info < ...")`.

##### Noxfile Version Matches
- **Standard**: `session.python == "X.Y"` (Nox uses strings).
- **Avoid**: `float(session.python) < X.Y` (fails for `3.10`).

##### Cleanup Rules
- **Polyfills**: Remove dead `try/except` blocks guarding polyfills for features now standard in 3.10+.
- **Obsolete Skips**: Remove pytest skips for features now universally available.

##### Dependency Specific rules
- Use idiomatic python references to detect dependency versions and to compare against the target version.

---

#### 💡 Context for Step 3: Disposition Rules
*Every reference to the dependency version found by the scanner must be dispositioned in one of these ways:*

1. **Update**: Update the reference if still necessary (e.g., changing `3.9` to `3.10` in support files).
2. **Delete**: Delete if no longer relevant (dead code, obsolete comments).
3. **Pragma Ignore**: Use `# version-scanner: ignore` or `# version-scanner: ignore-next-line` but ONLY for immutable historical facts or true false positives. Do NOT use for things that might change in future upgrades.

#### Step 3: Apply Changes
1. Update `setup.py` or `pyproject.toml` metadata and `requires-python`.
2. Update `noxfile.py` to remove old versions from sessions.
3. Update `README.rst` and `CONTRIBUTING.rst` documentation.
4. Remove compatibility code and skips based on the standards above.
5. **Sync Documentation**: If the package has a `docs` folder containing a `README.rst`, copy the updated top-level `README.rst` to overwrite it (unless it is a symlink).
6. Continue with the update process until all rows from the scan have been properly dispositioned.

---

#### Step 4: Verify (Post-Scan)
1. Run the `version_scanner` again. The result should be 0 matches (or only valid ignores).

---

#### 💡 Context for Step 5: Constraints & Conflicts
*Review these lessons learned when dealing with constraints:*

- **Lowest Runtime Constraints**: The file for the lowest accepted runtime (e.g., `constraints-3.10.txt`) must have pins matching the lowest acceptable versions in `setup.py` or `pyproject.toml`.
- **Philosophy on Warnings**: Do not simply block warnings (like `six` or `pkg_resources`) to make tests pass. **Bump the lower bounds** of dependencies to versions that don't trigger warnings on the current lowest acceptable runtime. This protects customers who use strict warning filters.
- **SQLAlchemy Transition**: For libraries supporting both 1.4 and 2.0, use `SQLALCHEMY_SILENCE_UBER_WARNING=1` in specific legacy Nox sessions rather than silencing globally.

---

#### Step 5: Local Test
1. Run unit tests using Nox (e.g., `nox -s unit`).
   > [!TIP]
   > Use `nox -s unit-3.10` to save time when debugging specific runtime failures.
2. Run `blacken` and `lint` sessions.

#### Step 6: Push & PR
1. Push the branch and create the PR using the template in the Appendix.

---

## Appendix

### PR Template [^1]
```text
This PR updates `<dependency>` to establish version x.y.z as the minimum supported version.

### Changes
* Configuration: Updated `setup.py` and `noxfile.py` to require <dependency> <version> and remove references to older versions.
* Cleanup: Removed dead code and polyfills no longer needed.

Fixes internal issue: http://b/482126936 🦕
```

---

## Candidates for `.conductor` or `gemini.md`

*The following guidelines are universal for AI assistants workin' in this repo and should be moved to `.conductor` files or Gemini memories:*

1. **AI & LLM Guidelines for Verification**:
   - Use Git Worktrees to scan branches without switching.
   - Run scanner from main branch pointing to worktree.
   - Bypass env artifacts by worktree only checking out tracked files.
2. **Automated Bisection**:
   - Use `version_bisector.py` to find lowest workable versions.
   - Abort tests early as soon as collection succeeds to save time.

[^1]: Adapted from the standard PR template used in this repository.
