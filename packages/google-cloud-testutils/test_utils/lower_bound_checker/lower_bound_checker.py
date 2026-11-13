# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib.metadata as metadata
from pathlib import Path
from typing import List, Set, Tuple

import click
from packaging.requirements import Requirement
from packaging.version import Version


def _get_package_requirements(package_name: str) -> List[Requirement]:
    """
    Get a list of all requirements and extras declared by this package.
    The package must already be installed in the environment.

    Args:
        package_name (str): The name of the package.

    Returns:
        List[packaging.requirements.Requirement]: A list of package requirements and extras.
    """
    requirements = []
    distribution = metadata.distribution(package_name)
    if distribution.requires:
        requirements = [Requirement(str(r)) for r in distribution.requires]
    return requirements


def _parse_requirements_file(requirements_file: str) -> List[Requirement]:
    """
    Get a list of requirements found in a requirements file.

    Args:
        requirements_file (str): Path to a requirements file.

    Returns:
        List[Requirement]: A list of requirements.
    """
    requirements = []

    with Path(requirements_file).open() as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                requirements.append(Requirement(line))

    return requirements


def _get_pinned_versions(
    ctx: click.Context, requirements: List[Requirement]
) -> Set[Tuple[str, Version]]:
    """Turn a list of requirements into a set of (package name, Version) tuples.

    The requirements are all expected to pin explicitly to one version.
    Other formats will result in an error.

        {("requests", Version("1.25.0"), ("google-auth", Version("1.0.0")}

    Args:
        ctx (click.Context): The current click context.
        requirements (List[Requirement]): A list of requirements.

    Returns:
        Set[Tuple[str, Version]]: Tuples of the package name and Version.
    """
    constraints = set()

    invalid_requirements = []

    for constraint in requirements:
        spec_set = list(constraint.specifier)
        if len(spec_set) != 1:
            invalid_requirements.append(constraint.name)
        else:
            if spec_set[0].operator != "==":
                invalid_requirements.append(constraint.name)
            else:
                constraints.add((constraint.name, Version(spec_set[0].version)))

    if invalid_requirements:
        ctx.fail(
            f"These requirements are not pinned to one version: {invalid_requirements}"
        )

    return constraints


class IndeterminableLowerBound(Exception):
    pass


def _lower_bound(requirement: Requirement) -> str:
    """
    Given a requirement, determine the lowest version that fulfills the requirement.
    The lower bound can be determined for a requirement only if it is one of these
    formats:

        foo==1.2.0
        foo>=1.2.0
        foo>=1.2.0, <2.0.0dev
        foo<2.0.0dev, >=1.2.0

    Args:
        requirement (Requirement): A requirement to parse

    Returns:
        str: The lower bound for the requirement.
    """
    spec_set = [s for s in requirement.specifier if s.operator != "!="]

    # sort by operator: <, then >=
    spec_set.sort(key=lambda x: x.operator)

    if len(spec_set) == 1:
        # foo==1.2.0
        if spec_set[0].operator == "==":
            return spec_set[0].version
        # foo>=1.2.0
        elif spec_set[0].operator == ">=":
            return spec_set[0].version
    # foo<2.0.0, >=1.2.0 or foo>=1.2.0, <2.0.0
    elif len(spec_set) == 2:
        if spec_set[0].operator == "<" and spec_set[1].operator == ">=":
            return spec_set[1].version

    raise IndeterminableLowerBound(
        f"Lower bound could not be determined for {requirement.name}"
    )


def _get_package_lower_bounds(
    ctx: click.Context, requirements: List[Requirement]
) -> Set[Tuple[str, Version]]:
    """Get a set of tuples ('package_name', Version('1.0.0')) from a
    list of Requirements.

    Args:
        ctx (click.Context): The current click context.
        requirements (List[Requirement]): A list of requirements.

    Returns:
        Set[Tuple[str, Version]]: A set of (package_name, lower_bound)
            tuples.
    """
    bad_package_lower_bounds = []
    package_lower_bounds = set()

    for req in requirements:
        try:
            version = _lower_bound(req)
            package_lower_bounds.add((req.name, Version(version)))
        except IndeterminableLowerBound:
            bad_package_lower_bounds.append(req.name)

    if bad_package_lower_bounds:
        ctx.fail(
            f"setup.py is missing explicit lower bounds for the following packages: {str(bad_package_lower_bounds)}"
        )
    else:
        return package_lower_bounds


@click.group()
def main():
    pass


@main.command()
@click.option("--package-name", required=True, help="Name of the package.")
@click.option("--constraints-file", required=True, help="Path to constraints file.")
@click.pass_context
def update(ctx: click.Context, package_name: str, constraints_file: str) -> None:
    """Create a constraints file with lower bounds for package-name.

    If the constraints file already exists the contents will be overwritten.
    """
    requirements = _get_package_requirements(package_name)
    requirements.sort(key=lambda x: x.name)

    package_lower_bounds = list(_get_package_lower_bounds(ctx, requirements))
    package_lower_bounds.sort(key=lambda x: x[0])

    constraints = [f"{name}=={version}" for name, version in package_lower_bounds]
    Path(constraints_file).write_text("\n".join(constraints))


@main.command()
@click.option("--package-name", required=True, help="Name of the package.")
@click.option("--constraints-file", required=True, help="Path to constraints file.")
@click.pass_context
def check(ctx: click.Context, package_name: str, constraints_file: str):
    """Check that the constraints-file pins to the lower bound specified in package-name's
    setup.py for each requirement.

    Requirements:

    1. The setup.py pins every requirement in one of the following formats:

        * foo==1.2.0

        * foo>=1.2.0

        * foo>=1.2.0, <2.0.0dev

        * foo<2.0.0dev, >=1.2.0

    2. The constraints file pins every requirement to a single version:

        * foo==1.2.0

    3. package-name is already installed in the environment.
    """

    package_requirements = _get_package_requirements(package_name)
    constraints = _parse_requirements_file(constraints_file)

    package_lower_bounds = _get_package_lower_bounds(ctx, package_requirements)
    constraints_file_versions = _get_pinned_versions(ctx, constraints)

    # Look for dependencies in setup.py that are missing from constraints.txt
    package_names = {x[0] for x in package_lower_bounds}
    constraint_names = {x[0] for x in constraints_file_versions}
    missing_from_constraints = package_names - constraint_names

    if missing_from_constraints:
        ctx.fail(
            (
                f"The following packages are declared as a requirement or extra"
                f"in setup.py but were not found in {constraints_file}: {str(missing_from_constraints)}"
            )
        )

    # We use .issuperset() instead of == because there may be additional entries
    # in constraints.txt (e.g., test only requirements)
    if not constraints_file_versions.issuperset(package_lower_bounds):
        first_line = f"The following packages have different versions {package_name}'s setup.py and {constraints_file}"
        error_msg = [first_line, "-" * (7 + len(first_line))]

        difference = package_lower_bounds - constraints_file_versions
        constraints_dict = dict(constraints_file_versions)

        for req, setup_py_version in difference:
            error_msg.append(
                f"'{req}' lower bound is {setup_py_version} in setup.py but constraints file has {constraints_dict[req]}"
            )
        ctx.fail("\n".join(error_msg))

    click.secho("All good!", fg="green")


if __name__ == "__main__":
    main()
