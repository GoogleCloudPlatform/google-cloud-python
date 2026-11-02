# Copyright (c) 2026 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import pytest

from pandas_gbq.core import resource_references


@pytest.mark.parametrize(
    ["table_id", "expected"],
    [
        (
            "my-project.my_dataset.my_table",
            resource_references.BigQueryTableId(
                project_id="my-project",
                dataset_id="my_dataset",
                table_id="my_table",
            ),
        ),
        (
            "google.com:my-project.my_dataset.my_table",
            resource_references.BigQueryTableId(
                project_id="my-project",
                dataset_id="my_dataset",
                table_id="my_table",
            ),
        ),
        (
            "my-project.my_catalog.my_table",
            resource_references.BigQueryTableId(
                project_id="my-project",
                dataset_id="my_catalog",
                table_id="my_table",
            ),
        ),
        (
            "my-project.my_catalog.my_namespace.my_table",
            resource_references.BigLakeTableId(
                project="my-project",
                catalog="my_catalog",
                namespace=("my_namespace",),
                table="my_table",
            ),
        ),
        (
            "my-project.my_catalog.my_namespace1.my_namespace2.my_table",
            resource_references.BigLakeTableId(
                project="my-project",
                catalog="my_catalog",
                namespace=("my_namespace1", "my_namespace2"),
                table="my_table",
            ),
        ),
    ],
)
def test_parse_table_id_valid(table_id, expected):
    result = resource_references.parse_table_id(table_id)
    assert result == expected


@pytest.mark.parametrize(
    "table_id",
    [
        "my-project",
        "my-project.my_dataset",
        ".my_dataset.my_table",
        "my-project.my_dataset.",
        "my-project..my_table",
        # A backtick would close the identifier quoting in the generated SQL and
        # let the rest of the string run as SQL, so it must be rejected here.
        "my-project.my_dataset.my_table` ORDER BY (SELECT 1) -- ",
        "my-project.my_catalog.my_namespace.evil` UNION ALL SELECT 1 -- ",
        "my-project.my_dataset.`",
    ],
)
def test_parse_table_id_invalid(table_id):
    with pytest.raises(ValueError):
        resource_references.parse_table_id(table_id)
