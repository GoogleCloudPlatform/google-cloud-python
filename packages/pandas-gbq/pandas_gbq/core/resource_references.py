# Copyright (c) 2026 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

import dataclasses
import re
from typing import Union

_TABLE_REFEREENCE_PATTERN = re.compile(
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


@dataclasses.dataclass(frozen=True)
class BigLakeTableId:
    project: str
    catalog: str
    namespace: tuple[str, ...]
    table: str


@dataclasses.dataclass(frozen=True)
class BigQueryTableId:
    project_id: str
    dataset_id: str
    table_id: str


def parse_table_id(table_id: str) -> Union[BigLakeTableId, BigQueryTableId]:
    """Turn a string into a BigLakeTableId or BigQueryTableId.

    Raises:
        ValueError: If the table ID is invalid.
    """
    regex_match = _TABLE_REFEREENCE_PATTERN.match(table_id)
    if not regex_match:
        raise ValueError(f"Invalid table ID: {table_id}")

    inner_parts = regex_match.group("inner_parts").split(".")
    if any(part == "" for part in inner_parts):
        raise ValueError(f"Invalid table ID: {table_id}")

    # The parsed parts are interpolated into backtick-quoted table references in
    # generated SQL (see core/biglake.py and core/sample.py). A backtick can't
    # appear in a real project/dataset/table name, and one here would close the
    # identifier quoting and let the rest of the string run as SQL, so reject it
    # while we're validating the table ID rather than downstream.
    if "`" in table_id:
        raise ValueError(f"Invalid table ID: {table_id}")

    if len(inner_parts) == 1:
        return BigQueryTableId(
            project_id=regex_match.group("project"),
            dataset_id=inner_parts[0],
            table_id=regex_match.group("table"),
        )

    return BigLakeTableId(
        project=regex_match.group("project"),
        catalog=inner_parts[0],
        namespace=tuple(inner_parts[1:]),
        table=regex_match.group("table"),
    )
