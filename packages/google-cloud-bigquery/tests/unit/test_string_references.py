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

import pytest

from google.cloud import bigquery


@pytest.mark.parametrize(
    ("value", "default_project", "expected_project_id", "expected_dataset_id"),
    (
        (
            "string-project.string_dataset",
            None,
            "string-project",
            "string_dataset",
        ),
        (
            "google.com:string-project.string_dataset",
            None,
            "google.com:string-project",
            "string_dataset",
        ),
        (
            "string_dataset",
            "default-project",
            "default-project",
            "string_dataset",
        ),
        (
            "string-project.string_dataset",
            "default-project",
            "string-project",
            "string_dataset",
        ),
        (
            "my-biglake-project.biglake_catalog.namespace_a.namespace_b",
            "ignored-default-project",
            "my-biglake-project",
            # BigLake tables are usable from the BigQuery metadata APIs by
            # combining catalog and namespace into the datasetId field. See
            # internal issue b/512823729.
            "biglake_catalog.namespace_a.namespace_b",
        ),
        (
            "example.com:my-biglake-project.biglake_catalog.namespace_a.namespace_b",
            "ignored-default-project",
            # BigLake tables should be usable from legacy domain-scoped project IDs.
            "example.com:my-biglake-project",
            "biglake_catalog.namespace_a.namespace_b",
        ),
    ),
)
def test_dataset_reference(
    value, default_project, expected_project_id, expected_dataset_id
):
    got = bigquery.DatasetReference.from_string(value, default_project=default_project)
    assert got.project == expected_project_id
    assert got.dataset_id == expected_dataset_id


@pytest.mark.parametrize(
    ("value", "expected_error_message"),
    (
        (
            "string_dataset",
            "dataset_id must be a fully-qualified dataset ID",
        ),
        (
            "string-project:string_dataset",
            "dataset_id must be a fully-qualified dataset ID",
        ),
    ),
)
@pytest.mark.parametrize(
    ("default_project",),
    (
        (None,),
        ("",),
    ),
)
def test_dataset_reference_without_default_project_value_error(
    value, expected_error_message, default_project
):
    with pytest.raises(ValueError, match=expected_error_message):
        bigquery.DatasetReference.from_string(value, default_project=default_project)


@pytest.mark.parametrize(
    (
        "value",
        "default_project",
        "expected_project_id",
        "expected_dataset_id",
        "expected_table_id",
    ),
    (
        (
            "string-project.string_dataset.string_table",
            None,
            "string-project",
            "string_dataset",
            "string_table",
        ),
        (
            "google.com:string-project.string_dataset.string_table",
            None,
            "google.com:string-project",
            "string_dataset",
            "string_table",
        ),
        (
            "string_dataset.string_table",
            "default-project",
            "default-project",
            "string_dataset",
            "string_table",
        ),
        (
            "my-project.string_dataset.string_table",
            "ignored-default-project",
            "my-project",
            "string_dataset",
            "string_table",
        ),
        (
            "my-biglake-project.biglake_catalog.namespace_a.namespace_b.biglake_table",
            "ignored-default-project",
            "my-biglake-project",
            # BigLake tables are usable from the BigQuery metadata APIs by
            # combining catalog and namespace into the datasetId field. See
            # internal issue b/512823729.
            "biglake_catalog.namespace_a.namespace_b",
            "biglake_table",
        ),
        (
            "example.com:my-biglake-project.biglake_catalog.namespace_a.namespace_b.biglake_table",
            "ignored-default-project",
            # BigLake tables should be usable from legacy domain-scoped project IDs.
            "example.com:my-biglake-project",
            "biglake_catalog.namespace_a.namespace_b",
            "biglake_table",
        ),
    ),
)
def test_table_reference(
    value, default_project, expected_project_id, expected_dataset_id, expected_table_id
):
    got = bigquery.TableReference.from_string(value, default_project=default_project)
    assert got.project == expected_project_id
    assert got.dataset_id == expected_dataset_id
    assert got.table_id == expected_table_id


@pytest.mark.parametrize(
    ("value",),
    (
        ("string_table",),
        ("string_dataset.string_table",),
        ("string-project:string_dataset.string_table",),
    ),
)
@pytest.mark.parametrize(
    ("default_project",),
    (
        (None,),
        ("",),
    ),
)
def test_table_reference_without_default_project_value_error(value, default_project):
    with pytest.raises(ValueError, match="Supply a default project"):
        bigquery.TableReference.from_string(value, default_project=default_project)
