# Copyright 2026 Google LLC
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

"""Script to group changed packages into balanced shards for CI testing.

This script identifies which packages have changed compared to a target branch
(or since the last commit) and groups them into a fixed number of shards.
It uses package weights (configured via environment variables) to balance the
execution time across shards while maintaining alphabetical order and
contiguous grouping. All directory variants of a package (e.g. packages/foo and
preview-packages/foo) are kept aligned in the exact same shard.
"""

import collections
import json
import math
import os
import subprocess
import sys

# CI infrastructure and workflow paths that affect test execution
CI_INFRASTRUCTURE_DIRS = {
    ".github",
    "ci",
}

# Core dependency packages whose changes affect all downstream handwritten packages
CORE_PACKAGES = {
    "google-api-core",
    "google-auth",
    "google-auth-httplib2",
    "google-auth-oauthlib",
    "google-cloud-core",
    "googleapis-common-protos",
    "grpc-google-iam-v1",
    "proto-plus",
    "google-crc32c",
}

# Packages temporarily excluded from CI test execution.
EXCLUDED_PACKAGES = set()


def get_package_directories():
    """Parses package directory roots from the PACKAGE_DIRS environment variable.

    Defaults to ['packages', 'preview-packages'] if not set.
    """
    env_dirs = os.environ.get("PACKAGE_DIRS", "")
    if env_dirs:
        dirs = [d.strip() for d in env_dirs.replace("\n", " ").split(" ") if d.strip()]
        if dirs:
            return dirs
    return ["packages", "preview-packages"]


def get_package_weights():
    """Parses package weights from the PACKAGE_WEIGHTS environment variable.
    Package weights represent the relative size of the test, where the weight
    approximately represents the minutes the test takes to run. This is used
    for distributing work properly across shards.

    The environment variable is expected to be a multiline string where each line
    is in the format 'package_name: weight'. Lines starting with '#' are ignored.

    Returns:
        dict: A mapping of package names to their integer weights.
    """
    weights = {}
    env_weights = os.environ.get("PACKAGE_WEIGHTS", "")
    for line in env_weights.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            try:
                pkg, weight = line.split(":", 1)
                weights[pkg.strip()] = int(weight.strip())
            except ValueError:
                continue
    return weights


def get_packages(handwritten_only=False):
    """Lists all package directory paths in the repository grouped by package name.

    If handwritten_only is True, includes only non-GAPIC_AUTO libraries.

    Returns:
        dict: A dictionary mapping package_name -> list of relative directory paths.
    """
    subdirs = get_package_directories()
    packages_map = collections.defaultdict(list)
    for subdir in subdirs:
        if not os.path.exists(subdir):
            continue
        for d in os.listdir(subdir):
            if d in EXCLUDED_PACKAGES:
                continue
            full_path = os.path.join(subdir, d) + "/"
            if not os.path.isdir(full_path):
                continue
            if handwritten_only:
                meta_file = os.path.join(full_path, ".repo-metadata.json")
                if os.path.exists(meta_file):
                    try:
                        with open(meta_file) as f:
                            data = json.load(f)
                            if (
                                isinstance(data, dict)
                                and data.get("library_type") == "GAPIC_AUTO"
                            ):
                                continue
                    except Exception:
                        pass
            packages_map[d].append(full_path)
    return packages_map


def get_packages_to_test():
    """Determines the dictionary of package names to directory paths that need to be tested.

    This is based on git diffs against the target branch (presubmit) or the
    previous commit (continuous). If TEST_ALL_PACKAGES is set to true,
    all packages are returned.

    Returns:
        dict: A dictionary mapping package_name -> list of relative directory paths to be tested.
    """
    build_type = os.environ.get("BUILD_TYPE", "presubmit")
    target_branch = os.environ.get("TARGET_BRANCH", "main")
    test_all_packages = os.environ.get("TEST_ALL_PACKAGES", "false").lower() == "true"
    handwritten_only = os.environ.get("HANDWRITTEN_ONLY", "false").lower() == "true"

    all_packages = get_packages(handwritten_only=handwritten_only)

    if test_all_packages:
        return all_packages

    if build_type == "presubmit":
        git_diff_arg = f"origin/{target_branch}..."
    elif build_type == "continuous":
        git_diff_arg = "HEAD~1.."
    else:
        return all_packages

    try:
        res = subprocess.check_output(
            ["git", "diff", "--name-only", git_diff_arg]
        ).decode("utf-8")
        changed_files = res.splitlines()
    except subprocess.CalledProcessError:
        # If change detection fails, fall back to all packages
        return all_packages

    package_dirs = set(get_package_directories())
    to_test_paths = collections.defaultdict(list)
    has_ci_change = False

    for f in changed_files:
        parts = os.path.normpath(f).split(os.sep)
        if parts and parts[0] in CI_INFRASTRUCTURE_DIRS:
            has_ci_change = True
        if len(parts) >= 2 and parts[0] in package_dirs:
            pkg_name = parts[1]
            full_path = f"{parts[0]}/{parts[1]}/"
            if pkg_name in all_packages and full_path in all_packages[pkg_name]:
                if full_path not in to_test_paths[pkg_name]:
                    to_test_paths[pkg_name].append(full_path)

    has_core_change = any(pkg in CORE_PACKAGES for pkg in to_test_paths)

    # If CI infrastructure or a core dependency was touched, merge all handwritten packages
    if has_ci_change or has_core_change:
        for pkg, paths in get_packages(handwritten_only=True).items():
            for path in paths:
                if path not in to_test_paths[pkg]:
                    to_test_paths[pkg].append(path)

    return dict(to_test_paths)


def group_packages(packages_map):
    """Groups packages by package name into balanced shards.

    All directory variants of a package (e.g. packages/foo and preview-packages/foo)
    are kept together in the exact same shard.

    Args:
        packages_map (dict): Dictionary mapping package_name -> list of directory paths.

    Returns:
        list: A list of dictionaries, each representing a shard with its name,
              index, description, and the space-separated list of packages.
    """
    if not packages_map:
        return []

    package_weights_map = get_package_weights()
    sorted_pkg_names = sorted(packages_map.keys())

    pkg_items = []
    total_weight = 0
    for name in sorted_pkg_names:
        paths = packages_map[name]
        # Multiply base weight by number of directory variants (e.g. standard + preview)
        weight = package_weights_map.get(name, 1) * len(paths)
        pkg_items.append((name, paths, weight))
        total_weight += weight

    # Dynamically determine target weight to balance across max shards.
    max_shards = int(os.environ.get("MAX_SHARDS", 16))
    min_shard_weight = int(os.environ.get("MIN_SHARD_WEIGHT", 10))
    target_weight = max(min_shard_weight, math.ceil(total_weight / max_shards))

    shards_list = []
    current_shard_items = []
    current_shard_weight = 0

    # Pack packages alphabetically by package name.
    for name, paths, weight in pkg_items:
        # If adding this package would exceed target weight AND we haven't reached the
        # shard limit, start a new shard. Otherwise, keep "stuffing" the current one.
        if (
            current_shard_items
            and (current_shard_weight + weight > target_weight)
            and len(shards_list) < max_shards - 1
        ):
            shards_list.append(current_shard_items)
            current_shard_items = [(name, paths, weight)]
            current_shard_weight = weight
        else:
            current_shard_items.append((name, paths, weight))
            current_shard_weight += weight

    if current_shard_items:
        shards_list.append(current_shard_items)

    # Construct the final shards output list
    shards = []
    for i, shard_items in enumerate(shards_list):
        index = i + 1
        name = f"Shard {index}"
        num_in_shard = len(shard_items)

        # Calculate contiguous range description using package names
        first_pkg_name = shard_items[0][0]
        last_pkg_name = shard_items[-1][0]
        if num_in_shard == 1:
            desc = first_pkg_name
        else:
            desc = f"{first_pkg_name}...{last_pkg_name} ({num_in_shard} packages)"

        all_paths = []
        for _, paths, _ in shard_items:
            all_paths.extend(paths)

        shards.append(
            {
                "name": name,
                "index": index,
                "description": desc,
                "packages": " ".join(all_paths),
                "is_sharded": True,
            }
        )

    # Set is_sharded dynamically based on the total number of shards
    total_shards = len(shards)
    for shard in shards:
        shard["is_sharded"] = total_shards > 1

    return shards


if __name__ == "__main__":
    packages = get_packages_to_test()
    shards = group_packages(packages)
    shards_json = json.dumps(shards)
    print(shards_json)

    all_paths = []
    for paths in packages.values():
        all_paths.extend(paths)
    packages_str = " ".join(all_paths)

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"matrix={shards_json}\n")
            f.write(f"packages={packages_str}\n")
