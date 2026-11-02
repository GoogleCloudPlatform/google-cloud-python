#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

import pytest

import google.cloud._helpers
from google.cloud import bigquery


@pytest.fixture
def target_class():
    from google.cloud.bigquery.routine import Routine

    return Routine


@pytest.fixture
def object_under_test(target_class):
    return target_class("project-id.dataset_id.routine_id")


def test_ctor(target_class):
    from google.cloud.bigquery.routine import RoutineReference

    ref = RoutineReference.from_string("my-proj.my_dset.my_routine")
    actual_routine = target_class(ref)
    assert actual_routine.reference == ref
    assert (
        actual_routine.path == "/projects/my-proj/datasets/my_dset/routines/my_routine"
    )


def test_ctor_w_string(target_class):
    from google.cloud.bigquery.routine import RoutineReference

    routine_id = "my-proj.my_dset.my_routine"
    ref = RoutineReference.from_string(routine_id)
    actual_routine = target_class(routine_id)
    assert actual_routine.reference == ref


def test_ctor_w_properties(target_class):
    from google.cloud.bigquery.routine import RoutineArgument
    from google.cloud.bigquery.routine import RoutineReference

    routine_id = "my-proj.my_dset.my_routine"
    arguments = [
        RoutineArgument(
            name="x",
            data_type=bigquery.standard_sql.StandardSqlDataType(
                type_kind=bigquery.StandardSqlTypeNames.INT64
            ),
        )
    ]
    body = "x * 3"
    language = "SQL"
    return_type = bigquery.standard_sql.StandardSqlDataType(
        type_kind=bigquery.StandardSqlTypeNames.INT64
    )
    type_ = "SCALAR_FUNCTION"
    description = "A routine description."
    determinism_level = bigquery.DeterminismLevel.NOT_DETERMINISTIC

    options = bigquery.RemoteFunctionOptions(
        endpoint="https://some.endpoint",
        connection="connection_string",
        max_batching_rows=99,
        user_defined_context={"foo": "bar"},
    )
    external_runtime_options = bigquery.ExternalRuntimeOptions(
        container_memory="1G",
        container_cpu=1,
        runtime_connection="projects/p/locations/l/connections/c",
        max_batching_rows=100,
        runtime_version="python-3.11",
    )

    actual_routine = target_class(
        routine_id,
        arguments=arguments,
        body=body,
        language=language,
        return_type=return_type,
        type_=type_,
        description=description,
        determinism_level=determinism_level,
        remote_function_options=options,
        external_runtime_options=external_runtime_options,
    )

    ref = RoutineReference.from_string(routine_id)
    assert actual_routine.reference == ref
    assert actual_routine.arguments == arguments
    assert actual_routine.body == body
    assert actual_routine.language == language
    assert actual_routine.return_type == return_type
    assert actual_routine.type_ == type_
    assert actual_routine.description == description
    assert (
        actual_routine.determinism_level == bigquery.DeterminismLevel.NOT_DETERMINISTIC
    )
    assert actual_routine.remote_function_options == options
    assert actual_routine.external_runtime_options == external_runtime_options


def test_ctor_invalid_remote_function_options(target_class):
    with pytest.raises(
        ValueError,
        match=".*must be google.cloud.bigquery.routine.RemoteFunctionOptions.*",
    ):
        target_class(
            "my-proj.my_dset.my_routine",
            remote_function_options=object(),
        )


def test_ctor_invalid_external_runtime_options(target_class):
    with pytest.raises(
        ValueError,
        match=".*must be google.cloud.bigquery.routine.ExternalRuntimeOptions.*",
    ):
        target_class(
            "my-proj.my_dset.my_routine",
            external_runtime_options=object(),
        )


def test_from_api_repr(target_class):
    from google.cloud.bigquery.routine import RoutineArgument
    from google.cloud.bigquery.routine import RoutineReference

    creation_time = datetime.datetime(
        2010, 5, 19, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    modified_time = datetime.datetime(
        2011, 10, 1, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    resource = {
        "routineReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "routineId": "my_routine",
        },
        "etag": "abcdefg",
        "creationTime": str(google.cloud._helpers._millis(creation_time)),
        "lastModifiedTime": str(google.cloud._helpers._millis(modified_time)),
        "definitionBody": "42",
        "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
        "language": "SQL",
        "returnType": {"typeKind": "INT64"},
        "routineType": "SCALAR_FUNCTION",
        "someNewField": "someValue",
        "description": "A routine description.",
        "determinismLevel": bigquery.DeterminismLevel.DETERMINISTIC,
        "remoteFunctionOptions": {
            "endpoint": "https://some.endpoint",
            "connection": "connection_string",
            "maxBatchingRows": 50,
            "userDefinedContext": {
                "foo": "bar",
            },
        },
        "dataGovernanceType": "DATA_MASKING",
        "externalRuntimeOptions": {
            "containerMemory": "1G",
            "containerCpu": 1,
            "runtimeConnection": "projects/p/locations/l/connections/c",
            "maxBatchingRows": 100,
            "runtimeVersion": "python-3.11",
        },
    }
    actual_routine = target_class.from_api_repr(resource)

    assert actual_routine.project == "my-project"
    assert actual_routine.dataset_id == "my_dataset"
    assert actual_routine.routine_id == "my_routine"
    assert (
        actual_routine.path
        == "/projects/my-project/datasets/my_dataset/routines/my_routine"
    )
    assert actual_routine.reference == RoutineReference.from_string(
        "my-project.my_dataset.my_routine"
    )
    assert actual_routine.etag == "abcdefg"
    assert actual_routine.created == creation_time
    assert actual_routine.modified == modified_time
    assert actual_routine.arguments == [
        RoutineArgument(
            name="x",
            data_type=bigquery.standard_sql.StandardSqlDataType(
                type_kind=bigquery.StandardSqlTypeNames.INT64
            ),
        )
    ]
    assert actual_routine.body == "42"
    assert actual_routine.language == "SQL"
    assert actual_routine.return_type == bigquery.standard_sql.StandardSqlDataType(
        type_kind=bigquery.StandardSqlTypeNames.INT64
    )
    assert actual_routine.return_table_type is None
    assert actual_routine.type_ == "SCALAR_FUNCTION"
    assert actual_routine._properties["someNewField"] == "someValue"
    assert actual_routine.description == "A routine description."
    assert actual_routine.determinism_level == "DETERMINISTIC"
    assert actual_routine.remote_function_options.endpoint == "https://some.endpoint"
    assert actual_routine.remote_function_options.connection == "connection_string"
    assert actual_routine.remote_function_options.max_batching_rows == 50
    assert actual_routine.remote_function_options.user_defined_context == {"foo": "bar"}
    assert actual_routine.data_governance_type == "DATA_MASKING"
    assert actual_routine.external_runtime_options.container_memory == "1G"
    assert actual_routine.external_runtime_options.container_cpu == 1
    assert (
        actual_routine.external_runtime_options.runtime_connection
        == "projects/p/locations/l/connections/c"
    )
    assert actual_routine.external_runtime_options.max_batching_rows == 100
    assert actual_routine.external_runtime_options.runtime_version == "python-3.11"


def test_from_api_repr_tvf_function(target_class):
    from google.cloud.bigquery.routine import RoutineArgument
    from google.cloud.bigquery.routine import RoutineReference
    from google.cloud.bigquery.routine import RoutineType

    StandardSqlDataType = bigquery.standard_sql.StandardSqlDataType
    StandardSqlField = bigquery.standard_sql.StandardSqlField
    StandardSqlTableType = bigquery.standard_sql.StandardSqlTableType

    creation_time = datetime.datetime(
        2010, 5, 19, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    modified_time = datetime.datetime(
        2011, 10, 1, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    resource = {
        "routineReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "routineId": "my_routine",
        },
        "etag": "abcdefg",
        "creationTime": str(google.cloud._helpers._millis(creation_time)),
        "lastModifiedTime": str(google.cloud._helpers._millis(modified_time)),
        "definitionBody": "SELECT x FROM UNNEST([1,2,3]) x WHERE x > a",
        "arguments": [{"name": "a", "dataType": {"typeKind": "INT64"}}],
        "language": "SQL",
        "returnTableType": {
            "columns": [{"name": "int_col", "type": {"typeKind": "INT64"}}]
        },
        "routineType": "TABLE_VALUED_FUNCTION",
        "someNewField": "someValue",
        "description": "A routine description.",
        "determinismLevel": bigquery.DeterminismLevel.DETERMINISTIC,
    }
    actual_routine = target_class.from_api_repr(resource)

    assert actual_routine.project == "my-project"
    assert actual_routine.dataset_id == "my_dataset"
    assert actual_routine.routine_id == "my_routine"
    assert (
        actual_routine.path
        == "/projects/my-project/datasets/my_dataset/routines/my_routine"
    )
    assert actual_routine.reference == RoutineReference.from_string(
        "my-project.my_dataset.my_routine"
    )
    assert actual_routine.etag == "abcdefg"
    assert actual_routine.created == creation_time
    assert actual_routine.modified == modified_time
    assert actual_routine.arguments == [
        RoutineArgument(
            name="a",
            data_type=StandardSqlDataType(
                type_kind=bigquery.StandardSqlTypeNames.INT64
            ),
        )
    ]
    assert actual_routine.body == "SELECT x FROM UNNEST([1,2,3]) x WHERE x > a"
    assert actual_routine.language == "SQL"
    assert actual_routine.return_type is None
    assert actual_routine.return_table_type == StandardSqlTableType(
        columns=[
            StandardSqlField(
                name="int_col",
                type=StandardSqlDataType(type_kind=bigquery.StandardSqlTypeNames.INT64),
            )
        ]
    )
    assert actual_routine.type_ == RoutineType.TABLE_VALUED_FUNCTION
    assert actual_routine._properties["someNewField"] == "someValue"
    assert actual_routine.description == "A routine description."
    assert actual_routine.determinism_level == "DETERMINISTIC"


def test_from_api_repr_w_minimal_resource(target_class):
    from google.cloud.bigquery.routine import RoutineReference

    resource = {
        "routineReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "routineId": "my_routine",
        }
    }
    actual_routine = target_class.from_api_repr(resource)
    assert actual_routine.reference == RoutineReference.from_string(
        "my-project.my_dataset.my_routine"
    )
    assert actual_routine.etag is None
    assert actual_routine.created is None
    assert actual_routine.modified is None
    assert actual_routine.arguments == []
    assert actual_routine.body is None
    assert actual_routine.language is None
    assert actual_routine.return_type is None
    assert actual_routine.type_ is None
    assert actual_routine.description is None
    assert actual_routine.determinism_level is None
    assert actual_routine.remote_function_options is None
    assert actual_routine.data_governance_type is None
    assert actual_routine.external_runtime_options is None


def test_from_api_repr_w_unknown_fields(target_class):
    from google.cloud.bigquery.routine import RoutineReference

    resource = {
        "routineReference": {
            "projectId": "my-project",
            "datasetId": "my_dataset",
            "routineId": "my_routine",
        },
        "thisFieldIsNotInTheProto": "just ignore me",
    }
    actual_routine = target_class.from_api_repr(resource)
    assert actual_routine.reference == RoutineReference.from_string(
        "my-project.my_dataset.my_routine"
    )
    assert actual_routine._properties is resource


@pytest.mark.parametrize(
    "resource,filter_fields,expected",
    [
        (
            {
                "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
                "definitionBody": "x * 3",
                "language": "SQL",
                "returnType": {"typeKind": "INT64"},
                "routineType": "SCALAR_FUNCTION",
                "description": "A routine description.",
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED,
            },
            ["arguments"],
            {"arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}]},
        ),
        (
            {
                "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
                "definitionBody": "x * 3",
                "language": "SQL",
                "returnType": {"typeKind": "INT64"},
                "routineType": "SCALAR_FUNCTION",
                "description": "A routine description.",
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED,
            },
            ["body"],
            {"definitionBody": "x * 3"},
        ),
        (
            {
                "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
                "definitionBody": "x * 3",
                "language": "SQL",
                "returnType": {"typeKind": "INT64"},
                "routineType": "SCALAR_FUNCTION",
                "description": "A routine description.",
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED,
            },
            ["language"],
            {"language": "SQL"},
        ),
        (
            {
                "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
                "definitionBody": "x * 3",
                "language": "SQL",
                "returnType": {"typeKind": "INT64"},
                "routineType": "SCALAR_FUNCTION",
                "description": "A routine description.",
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED,
            },
            ["return_type"],
            {"returnType": {"typeKind": "INT64"}},
        ),
        (
            {
                "definitionBody": "SELECT x FROM UNNEST([1,2,3]) x WHERE x > 1",
                "language": "SQL",
                "returnTableType": {
                    "columns": [{"name": "int_col", "type": {"typeKind": "INT64"}}]
                },
                "routineType": "TABLE_VALUED_FUNCTION",
                "description": "A routine description.",
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED,
            },
            ["return_table_type"],
            {
                "returnTableType": {
                    "columns": [{"name": "int_col", "type": {"typeKind": "INT64"}}]
                }
            },
        ),
        (
            {
                "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
                "definitionBody": "x * 3",
                "language": "SQL",
                "returnType": {"typeKind": "INT64"},
                "routineType": "SCALAR_FUNCTION",
                "description": "A routine description.",
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED,
            },
            ["type_"],
            {"routineType": "SCALAR_FUNCTION"},
        ),
        (
            {
                "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
                "definitionBody": "x * 3",
                "language": "SQL",
                "returnType": {"typeKind": "INT64"},
                "routineType": "SCALAR_FUNCTION",
                "description": "A routine description.",
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED,
            },
            ["description"],
            {"description": "A routine description."},
        ),
        (
            {
                "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
                "definitionBody": "x * 3",
                "language": "SQL",
                "returnType": {"typeKind": "INT64"},
                "routineType": "SCALAR_FUNCTION",
                "description": "A routine description.",
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED,
            },
            ["determinism_level"],
            {
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED
            },
        ),
        (
            {
                "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
                "definitionBody": "x * 3",
                "language": "SQL",
                "returnType": {"typeKind": "INT64"},
                "routineType": "SCALAR_FUNCTION",
                "description": "A routine description.",
                "determinismLevel": bigquery.DeterminismLevel.DETERMINISM_LEVEL_UNSPECIFIED,
                "dataGovernanceType": "DATA_MASKING",
            },
            ["data_governance_type"],
            {"dataGovernanceType": "DATA_MASKING"},
        ),
        (
            {},
            [
                "arguments",
                "language",
                "body",
                "type_",
                "return_type",
                "description",
                "determinism_level",
            ],
            {
                "arguments": None,
                "definitionBody": None,
                "language": None,
                "returnType": None,
                "routineType": None,
                "description": None,
                "determinismLevel": None,
            },
        ),
        (
            {"someNewField": "someValue"},
            ["someNewField"],
            {"someNewField": "someValue"},
        ),
        (
            {
                "routineType": "SCALAR_FUNCTION",
                "remoteFunctionOptions": {
                    "endpoint": "https://some_endpoint",
                    "connection": "connection_string",
                    "max_batching_rows": 101,
                },
            },
            ["remote_function_options"],
            {
                "remoteFunctionOptions": {
                    "endpoint": "https://some_endpoint",
                    "connection": "connection_string",
                    "max_batching_rows": 101,
                },
            },
        ),
    ],
)
def test_build_resource(object_under_test, resource, filter_fields, expected):
    object_under_test._properties = resource
    actual_routine = object_under_test._build_resource(filter_fields)
    assert actual_routine == expected


def test_set_arguments_w_none(object_under_test):
    object_under_test.arguments = None
    assert object_under_test.arguments == []
    assert object_under_test._properties["arguments"] == []


def test_set_imported_libraries(object_under_test):
    imported_libraries = ["gs://cloud-samples-data/bigquery/udfs/max-value.js"]
    object_under_test.imported_libraries = imported_libraries
    assert object_under_test.imported_libraries == imported_libraries
    assert object_under_test._properties["importedLibraries"] == imported_libraries


def test_set_imported_libraries_w_none(object_under_test):
    object_under_test.imported_libraries = None
    assert object_under_test.imported_libraries == []
    assert object_under_test._properties["importedLibraries"] == []


def test_set_return_type_w_none(object_under_test):
    object_under_test.return_type = None
    assert object_under_test.return_type is None
    assert object_under_test._properties["returnType"] is None


def test_set_return_table_type_w_none(object_under_test):
    object_under_test.return_table_type = None
    assert object_under_test.return_table_type is None
    assert object_under_test._properties["returnTableType"] is None


def test_set_return_table_type_w_not_none(object_under_test):
    StandardSqlDataType = bigquery.standard_sql.StandardSqlDataType
    StandardSqlField = bigquery.standard_sql.StandardSqlField
    StandardSqlTableType = bigquery.standard_sql.StandardSqlTableType

    table_type = StandardSqlTableType(
        columns=[
            StandardSqlField(
                name="int_col",
                type=StandardSqlDataType(type_kind=bigquery.StandardSqlTypeNames.INT64),
            ),
            StandardSqlField(
                name="str_col",
                type=StandardSqlDataType(
                    type_kind=bigquery.StandardSqlTypeNames.STRING
                ),
            ),
        ]
    )

    object_under_test.return_table_type = table_type

    assert object_under_test.return_table_type == table_type
    assert object_under_test._properties["returnTableType"] == {
        "columns": [
            {"name": "int_col", "type": {"typeKind": "INT64"}},
            {"name": "str_col", "type": {"typeKind": "STRING"}},
        ]
    }


def test_set_description_w_none(object_under_test):
    object_under_test.description = None
    assert object_under_test.description is None
    assert object_under_test._properties["description"] is None


def test_set_remote_function_options_w_none(object_under_test):
    object_under_test.remote_function_options = None
    assert object_under_test.remote_function_options is None
    assert object_under_test._properties["remoteFunctionOptions"] is None


def test_set_external_runtime_options_w_none(object_under_test):
    object_under_test.external_runtime_options = None
    assert object_under_test.external_runtime_options is None
    assert object_under_test._properties["externalRuntimeOptions"] is None


def test_set_data_governance_type_w_none(object_under_test):
    object_under_test.data_governance_type = None
    assert object_under_test.data_governance_type is None
    assert object_under_test._properties["dataGovernanceType"] is None


def test_set_data_governance_type_valid(object_under_test):
    object_under_test.data_governance_type = "DATA_MASKING"
    assert object_under_test.data_governance_type == "DATA_MASKING"
    assert object_under_test._properties["dataGovernanceType"] == "DATA_MASKING"


def test_set_data_governance_type_wrong_type(object_under_test):
    with pytest.raises(ValueError) as exp:
        object_under_test.data_governance_type = 1
    assert "invalid data_governance_type" in str(exp)
    assert object_under_test.data_governance_type is None
    assert object_under_test._properties.get("dataGovernanceType") is None


def test_set_data_governance_type_wrong_str(object_under_test):
    """Client does not verify the content of data_governance_type string to be
    compatible with future upgrades. If the value is not supported, BigQuery
    itself will report an error.
    """
    object_under_test.data_governance_type = "RANDOM_STRING"
    assert object_under_test.data_governance_type == "RANDOM_STRING"
    assert object_under_test._properties["dataGovernanceType"] == "RANDOM_STRING"


def test_repr(target_class):
    model = target_class("my-proj.my_dset.my_routine")
    actual_routine = repr(model)
    assert actual_routine == "Routine('my-proj.my_dset.my_routine')"
