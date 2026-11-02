# Copyright 2026 Google LLC
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

"""Helper to turn string references into REST resources."""

# TODO(b/513204277): Consolidate these transformations with pandas-gbq and bigframes.

from __future__ import annotations

import re
from typing import TypedDict, Union


ParsedDatasetReference = TypedDict(
    "ParsedDatasetReference",
    {
        "projectId": str,
        "datasetId": str,
    },
)


ParsedTableReference = TypedDict(
    "ParsedTableReference",
    {
        "projectId": str,
        "datasetId": str,
        "tableId": str,
    },
)


_FULLY_QUALIFIED_DATASET_REFERENCE_PATTERN = re.compile(
    # In the past, organizations could prefix their project IDs with a domain
    # name. Such projects still exist, especially at Google.
    r"^(?P<legacy_project_domain>[^:]+:)?"
    r"(?P<project>[^.]+)\."
    # Match dataset or catalog + namespace.
    #
    # Namespace could be arbitrarily deeply nested in Iceberg/BigLake. Support
    # this without catastrophic backtracking by moving the trailing "." to the
    # table group.
    r"(?P<inner_parts>.*)"
)


_FULLY_QUALIFIED_TABLE_REFERENCE_PATTERN = re.compile(
    # In the past, organizations could prefix their project IDs with a domain
    # name. Such projects still exist, especially at Google.
    r"^(?P<legacy_project_domain>[^:]+:)?"
    r"(?P<project>[^.]+)\."
    # Match dataset or catalog + namespace.
    #
    # Namespace could be arbitrarily deeply nested in Iceberg/BigLake. Support
    # this without catastrophic backtracking by moving the trailing "." to the
    # table group.
    r"(?P<inner_parts>.*)"
    # Table names can't contain ".", as that's used as the separator.
    r"\.(?P<table>[^.]+)$"
)


_RELATIVE_TABLE_REFERENCE_PATTERN = re.compile(
    # Match dataset or catalog + namespace.
    #
    # Namespace could be arbitrarily deeply nested in Iceberg/BigLake. Support
    # this without catastrophic backtracking by moving the trailing "." to the
    # table group.
    r"(?P<inner_parts>.*)"
    # Table names can't contain ".", as that's used as the separator.
    r"\.(?P<table>[^.]+)$"
)


def parse_dataset_reference(
    dataset_id: str, *, default_project: Union[str, None]
) -> ParsedDatasetReference:
    """Parse a dataset ID string.

    Returns:
        ParsedDatasetReference: A typed dictionary (to avoid circular dependencies).

    Raises:
        ValueError: When a fully-qualified dataset ID can't be determined.
    """
    regex_match = _FULLY_QUALIFIED_DATASET_REFERENCE_PATTERN.match(dataset_id)
    if regex_match:
        legacy_project_domain = regex_match.group("legacy_project_domain")
        project = regex_match.group("project")

        if legacy_project_domain:
            output_project_id = f"{legacy_project_domain}{project}"
        else:
            output_project_id = project

        return {
            "projectId": output_project_id,
            "datasetId": regex_match.group("inner_parts"),
        }

    if not default_project:
        raise ValueError(
            "When default_project is not set, dataset_id must be a "
            "fully-qualified dataset ID in standard SQL format, "
            'e.g., "project.dataset_id" got {}'.format(dataset_id)
        )

    return {"datasetId": dataset_id, "projectId": default_project}


def parse_table_reference(
    table_id: str, *, default_project: Union[str, None]
) -> ParsedTableReference:
    """Parse a table ID string.

    Returns:
        ParsedTableReference: A typed dictionary (to avoid circular dependencies).

    Raises:
        ValueError: When a fully-qualified table ID can't be determined.
    """
    regex_match = _FULLY_QUALIFIED_TABLE_REFERENCE_PATTERN.match(table_id)
    if regex_match:
        legacy_project_domain = regex_match.group("legacy_project_domain")
        project = regex_match.group("project")

        if legacy_project_domain:
            output_project_id = f"{legacy_project_domain}{project}"
        else:
            output_project_id = project

        return {
            "projectId": output_project_id,
            "datasetId": regex_match.group("inner_parts"),
            "tableId": regex_match.group("table"),
        }

    if not default_project:
        raise ValueError(
            "Could not determine project ID. Supply a default project or a fully-qualified table ID, "
            f"such as 'project.dataset.table'. Got {table_id}."
        )

    regex_match = _RELATIVE_TABLE_REFERENCE_PATTERN.match(table_id)
    if not regex_match:
        raise ValueError(
            "Could not parse table_id. Expected a table ID"
            f"such as 'project.dataset.table', but got {table_id}."
        )

    return {
        "projectId": default_project,
        "datasetId": regex_match.group("inner_parts"),
        "tableId": regex_match.group("table"),
    }
