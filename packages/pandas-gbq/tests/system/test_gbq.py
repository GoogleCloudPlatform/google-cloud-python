# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import datetime
import sys
import zoneinfo

import numpy as np
import packaging.version
import pandas
import pandas.api.types
import pandas.testing as tm
import pytest
from pandas import DataFrame

import pandas_gbq.schema
from pandas_gbq import gbq

TABLE_ID = "new_test"
PANDAS_VERSION = packaging.version.parse(pandas.__version__)


def test_imports():
    gbq._test_google_api_imports()


def make_mixed_dataframe_v1():
    # Re-implementation of private pandas.util.testing.makeMixedDataFrame
    return pandas.DataFrame(
        {
            "A": [0.0, 1.0, 2.0, 3.0, 4.0],
            "B": [0.0, 1.0, 0.0, 1.0, 0.0],
            "C": ["foo1", "foo2", "foo3", "foo4", "foo5"],
            "D": pandas.bdate_range("1/1/2009", periods=5),
        }
    )


def make_mixed_dataframe_v2(test_size):
    # create df to test for all BQ datatypes except RECORD
    bools = np.random.randint(2, size=(1, test_size)).astype(bool)
    flts = np.random.randn(1, test_size)
    ints = np.random.randint(1, 10, size=(1, test_size))
    strs = np.random.randint(1, 10, size=(1, test_size)).astype(str)
    times = [datetime.datetime.now(zoneinfo.ZoneInfo("UTC")) for t in range(test_size)]
    return DataFrame(
        {
            "bools": bools[0],
            "flts": flts[0],
            "ints": ints[0],
            "strs": strs[0],
            "times": times[0],
        },
        index=range(test_size),
    )


def get_schema(gbq_connector: gbq.GbqConnector, dataset_id: str, table_id: str):
    """Retrieve the schema of the table

    Obtain from BigQuery the field names and field types
    for the table defined by the parameters

    Parameters
    ----------
    dataset_id : str
        Name of the BigQuery dataset for the table
    table_id : str
        Name of the BigQuery table

    Returns
    -------
    list of dicts
        Fields representing the schema
    """
    from google.cloud import bigquery

    bqclient = gbq_connector.client
    table_ref = bigquery.TableReference(
        bigquery.DatasetReference(bqclient.project, dataset_id),
        table_id,
    )

    try:
        table = bqclient.get_table(table_ref)
        remote_schema = table.schema

        remote_fields = [field_remote.to_api_repr() for field_remote in remote_schema]
        for field in remote_fields:
            field["type"] = field["type"].upper()
            field["mode"] = field["mode"].upper()

        return remote_fields
    except gbq_connector.http_error as ex:
        gbq_connector.process_http_error(ex)


def verify_schema(gbq_connector, dataset_id, table_id, schema):
    """Indicate whether schemas match exactly

    Compare the BigQuery table identified in the parameters with
    the schema passed in and indicate whether all fields in the former
    are present in the latter. Order is not considered.

    Parameters
    ----------
    dataset_id :str
        Name of the BigQuery dataset for the table
    table_id : str
        Name of the BigQuery table
    schema : list(dict)
        Schema for comparison. Each item should have
        a 'name' and a 'type'

    Returns
    -------
    bool
        Whether the schemas match
    """

    fields_remote = pandas_gbq.schema._clean_schema_fields(
        get_schema(gbq_connector, dataset_id, table_id)
    )
    fields_local = pandas_gbq.schema._clean_schema_fields(schema["fields"])
    return fields_remote == fields_local


class TestGBQConnectorIntegration(object):
    def test_should_be_able_to_make_a_connector(self, gbq_connector):
        assert gbq_connector is not None, "Could not create a GbqConnector"

    def test_should_be_able_to_get_a_bigquery_client(self, gbq_connector):
        bigquery_client = gbq_connector.get_client()
        assert bigquery_client is not None


class TestReadGBQIntegration(object):
    @pytest.fixture(autouse=True)
    def setup(self, project, credentials):
        # - PER-TEST FIXTURES -
        # put here any instruction you want to be run *BEFORE* *EVERY* test is
        # executed.
        self.gbq_connector = gbq.GbqConnector(project, credentials=credentials)
        self.credentials = credentials

    def test_unicode_string_conversion_and_normalization(self, project_id):
        correct_test_datatype = DataFrame({"unicode_string": ["éü"]})
        unicode_string = "éü"
        query = 'SELECT "{0}" AS unicode_string'.format(unicode_string)

        df = gbq.read_gbq(
            query,
            project_id=project_id,
            credentials=self.credentials,
            dialect="legacy",
        )
        tm.assert_frame_equal(df, correct_test_datatype)

    def test_index_column(self, project_id):
        query = "SELECT 'a' AS string_1, 'b' AS string_2"
        result_frame = gbq.read_gbq(
            query,
            project_id=project_id,
            index_col="string_1",
            credentials=self.credentials,
            dialect="legacy",
        )
        correct_frame = DataFrame({"string_1": ["a"], "string_2": ["b"]}).set_index(
            "string_1"
        )
        assert result_frame.index.name == correct_frame.index.name

    def test_column_order(self, project_id):
        query = "SELECT 'a' AS string_1, 'b' AS string_2, 'c' AS string_3"
        col_order = ["string_3", "string_1", "string_2"]
        result_frame = gbq.read_gbq(
            query,
            project_id=project_id,
            col_order=col_order,
            credentials=self.credentials,
            dialect="legacy",
        )
        correct_frame = DataFrame(
            {"string_1": ["a"], "string_2": ["b"], "string_3": ["c"]}
        )[col_order]
        tm.assert_frame_equal(result_frame, correct_frame)

    def test_read_gbq_raises_invalid_column_order(self, project_id):
        query = "SELECT 'a' AS string_1, 'b' AS string_2, 'c' AS string_3"
        col_order = ["string_aaa", "string_1", "string_2"]

        # Column string_aaa does not exist. Should raise InvalidColumnOrder
        with pytest.raises(gbq.InvalidColumnOrder):
            gbq.read_gbq(
                query,
                project_id=project_id,
                col_order=col_order,
                credentials=self.credentials,
                dialect="legacy",
            )

    def test_column_order_plus_index(self, project_id):
        query = "SELECT 'a' AS string_1, 'b' AS string_2, 'c' AS string_3"
        col_order = ["string_3", "string_2"]
        result_frame = gbq.read_gbq(
            query,
            project_id=project_id,
            index_col="string_1",
            col_order=col_order,
            credentials=self.credentials,
            dialect="legacy",
        )
        correct_frame = DataFrame(
            {"string_1": ["a"], "string_2": ["b"], "string_3": ["c"]}
        )
        correct_frame.set_index("string_1", inplace=True)
        correct_frame = correct_frame[col_order]
        tm.assert_frame_equal(result_frame, correct_frame)

    def test_read_gbq_raises_invalid_index_column(self, project_id):
        query = "SELECT 'a' AS string_1, 'b' AS string_2, 'c' AS string_3"
        col_order = ["string_3", "string_2"]

        # Column string_bbb does not exist. Should raise InvalidIndexColumn
        with pytest.raises(gbq.InvalidIndexColumn):
            gbq.read_gbq(
                query,
                project_id=project_id,
                index_col="string_bbb",
                col_order=col_order,
                credentials=self.credentials,
                dialect="legacy",
            )

    def test_malformed_query(self, project_id):
        with pytest.raises(gbq.GenericGBQException):
            gbq.read_gbq(
                "SELCET * FORM [publicdata:samples.shakespeare]",
                project_id=project_id,
                credentials=self.credentials,
                dialect="legacy",
            )

    def test_bad_project_id(self):
        with pytest.raises(gbq.GenericGBQException):
            gbq.read_gbq(
                "SELCET * FROM [publicdata:samples.shakespeare]",
                project_id="not-my-project",
                credentials=self.credentials,
                dialect="legacy",
            )

    def test_bad_table_name(self, project_id):
        with pytest.raises(gbq.GenericGBQException):
            gbq.read_gbq(
                "SELECT * FROM [publicdata:samples.nope]",
                project_id=project_id,
                credentials=self.credentials,
                dialect="legacy",
            )

    def test_download_dataset_larger_than_200k_rows(self, project_id):
        test_size = 200005
        # Test for known BigQuery bug in datasets larger than 100k rows
        # http://stackoverflow.com/questions/19145587/bq-py-not-paging-results
        df = gbq.read_gbq(
            "SELECT id FROM [publicdata:samples.wikipedia] "
            "GROUP EACH BY id ORDER BY id ASC LIMIT {0}".format(test_size),
            project_id=project_id,
            credentials=self.credentials,
            dialect="legacy",
        )
        assert len(df.drop_duplicates()) == test_size

    def test_ddl(self, random_dataset, project_id):
        # Bug fix for https://github.com/pydata/pandas-gbq/issues/45
        df = gbq.read_gbq(
            "CREATE OR REPLACE TABLE {}.test_ddl (x INT64)".format(
                random_dataset.dataset_id
            )
        )
        assert len(df) == 0

    def test_ddl_w_max_results(self, random_dataset, project_id):
        df = gbq.read_gbq(
            "CREATE OR REPLACE TABLE {}.test_ddl (x INT64)".format(
                random_dataset.dataset_id
            ),
            max_results=0,
        )
        assert df is None

    def test_max_results(self, random_dataset, project_id):
        df = gbq.read_gbq(
            "SELECT * FROM UNNEST(GENERATE_ARRAY(1, 100))", max_results=10
        )
        assert len(df) == 10

    def test_one_row_one_column(self, project_id):
        df = gbq.read_gbq(
            "SELECT 3 as v",
            project_id=project_id,
            credentials=self.credentials,
            dialect="standard",
        )
        expected_result = DataFrame(dict(v=[3]), dtype="Int64")
        tm.assert_frame_equal(df, expected_result)

    def test_legacy_sql(self, project_id):
        legacy_sql = "SELECT id FROM [publicdata.samples.wikipedia] LIMIT 10"

        # Test that a legacy sql statement fails when
        # setting dialect='standard'
        with pytest.raises(gbq.GenericGBQException):
            gbq.read_gbq(
                legacy_sql,
                project_id=project_id,
                dialect="standard",
                credentials=self.credentials,
            )

        # Test that a legacy sql statement succeeds when
        # setting dialect='legacy'
        df = gbq.read_gbq(
            legacy_sql,
            project_id=project_id,
            dialect="legacy",
            credentials=self.credentials,
        )
        assert len(df.drop_duplicates()) == 10

    def test_standard_sql(self, project_id):
        standard_sql = "SELECT DISTINCT id FROM `publicdata.samples.wikipedia` LIMIT 10"

        # Test that a standard sql statement fails when using
        # the legacy SQL dialect.
        with pytest.raises(gbq.GenericGBQException):
            gbq.read_gbq(
                standard_sql,
                project_id=project_id,
                credentials=self.credentials,
                dialect="legacy",
            )

        # Test that a standard sql statement succeeds when
        # setting dialect='standard'
        df = gbq.read_gbq(
            standard_sql,
            project_id=project_id,
            dialect="standard",
            credentials=self.credentials,
        )
        assert len(df.drop_duplicates()) == 10

    def test_query_with_parameters(self, project_id):
        sql_statement = "SELECT @param1 + @param2 AS valid_result"
        config = {
            "query": {
                "useLegacySql": False,
                "parameterMode": "named",
                "queryParameters": [
                    {
                        "name": "param1",
                        "parameterType": {"type": "INTEGER"},
                        "parameterValue": {"value": 1},
                    },
                    {
                        "name": "param2",
                        "parameterType": {"type": "INTEGER"},
                        "parameterValue": {"value": 2},
                    },
                ],
            }
        }
        # Test that a query that relies on parameters fails
        # when parameters are not supplied via configuration
        with pytest.raises(ValueError):
            gbq.read_gbq(
                sql_statement,
                project_id=project_id,
                credentials=self.credentials,
                dialect="legacy",
            )

        # Test that the query is successful because we have supplied
        # the correct query parameters via the 'config' option
        df = gbq.read_gbq(
            sql_statement,
            project_id=project_id,
            credentials=self.credentials,
            configuration=config,
            dialect="legacy",
        )
        tm.assert_frame_equal(df, DataFrame({"valid_result": [3]}, dtype="Int64"))

    def test_query_inside_configuration(self, project_id):
        query_no_use = 'SELECT "PI_WRONG" AS valid_string'
        query = 'SELECT "PI" AS valid_string'
        config = {"query": {"query": query, "useQueryCache": False}}
        # Test that it can't pass query both
        # inside config and as parameter
        with pytest.raises(ValueError):
            gbq.read_gbq(
                query_no_use,
                project_id=project_id,
                credentials=self.credentials,
                configuration=config,
                dialect="legacy",
            )

        df = gbq.read_gbq(
            None,
            project_id=project_id,
            credentials=self.credentials,
            configuration=config,
            dialect="legacy",
        )
        tm.assert_frame_equal(df, DataFrame({"valid_string": ["PI"]}))

    def test_configuration_without_query(self, project_id):
        sql_statement = "SELECT 1"
        config = {
            "copy": {
                "sourceTable": {
                    "projectId": project_id,
                    "datasetId": "publicdata:samples",
                    "tableId": "wikipedia",
                },
                "destinationTable": {
                    "projectId": project_id,
                    "datasetId": "publicdata:samples",
                    "tableId": "wikipedia_copied",
                },
            }
        }
        # Test that only 'query' configurations are supported
        # nor 'copy','load','extract'
        with pytest.raises(ValueError):
            gbq.read_gbq(
                sql_statement,
                project_id=project_id,
                credentials=self.credentials,
                configuration=config,
                dialect="legacy",
            )

    def test_configuration_raises_value_error_with_multiple_config(self, project_id):
        sql_statement = "SELECT 1"
        config = {
            "query": {"query": sql_statement, "useQueryCache": False},
            "load": {"query": sql_statement, "useQueryCache": False},
        }
        # Test that only ValueError is raised with multiple configurations
        with pytest.raises(ValueError):
            gbq.read_gbq(
                sql_statement,
                project_id=project_id,
                credentials=self.credentials,
                configuration=config,
                dialect="legacy",
            )

    def test_timeout_configuration(self, project_id):
        sql_statement = """
        select count(*) from unnest(generate_array(1,1000000)), unnest(generate_array(1, 10000))
        """

        # This first test confirms that we get a timeout error if we exceed the timeout limit.
        # The above query is expected to take a long time and exceed the limit.
        configs = [
            # we have a minimum limit on the timeout_ms being 400 milliseconds
            # see pandas-gbq/gbq.py/GbqConnector/run_query docstring
            # for more details.
            # pandas-gbq timeout configuration. Transformed to REST API compatible version.
            {"query": {"useQueryCache": False, "timeoutMs": 401}},
            # REST API job timeout. See:
            # https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfiguration.FIELDS.job_timeout_ms
            {"query": {"useQueryCache": False}, "jobTimeoutMs": 401},
        ]
        for config in configs:
            with pytest.raises(gbq.QueryTimeout):
                gbq.read_gbq(
                    sql_statement,
                    project_id=project_id,
                    credentials=self.credentials,
                    configuration=config,
                )

        # This second test confirms out our validation logic won't allow a
        # value less than or equal to 400 be used as a timeout value.
        # by exercising the system for various edge cases to ensure we catch
        # invalid values less than or equal to 400.
        configs = [
            {"query": {"useQueryCache": False, "timeoutMs": 399}},
            {"query": {"useQueryCache": False, "timeoutMs": 400}},
            {"query": {"useQueryCache": False, "timeoutMs": 1}},
            {"query": {"useQueryCache": False}, "jobTimeoutMs": 399},
            {"query": {"useQueryCache": False}, "jobTimeoutMs": 400},
            {"query": {"useQueryCache": False}, "jobTimeoutMs": 1},
        ]

        for config in configs:
            with pytest.raises(gbq.QueryTimeout):
                gbq.read_gbq(
                    sql_statement,
                    project_id=project_id,
                    credentials=self.credentials,
                    configuration=config,
                )

    def test_struct(self, project_id):
        query = """SELECT 1 int_field,
                   STRUCT("a" as letter, 1 as num) struct_field"""
        df = gbq.read_gbq(
            query,
            project_id=project_id,
            credentials=self.credentials,
            dialect="standard",
        )
        expected = DataFrame(
            {
                "int_field": pandas.Series([1], dtype="Int64"),
                "struct_field": [{"letter": "a", "num": 1}],
            },
            columns=["int_field", "struct_field"],
        )
        tm.assert_frame_equal(df, expected)

    def test_array(self, project_id):
        query = """select ["a","x","b","y","c","z"] as letters"""
        df = gbq.read_gbq(
            query,
            project_id=project_id,
            credentials=self.credentials,
            dialect="standard",
        )
        tm.assert_frame_equal(
            df,
            DataFrame([[["a", "x", "b", "y", "c", "z"]]], columns=["letters"]),
        )

    def test_array_length_zero(self, project_id):
        query = """WITH t as (
                   SELECT "a" letter, [""] as array_field
                   UNION ALL
                   SELECT "b" letter, [] as array_field)

                   select letter, array_field, array_length(array_field) len
                   from t
                   order by letter ASC"""
        df = gbq.read_gbq(
            query,
            project_id=project_id,
            credentials=self.credentials,
            dialect="standard",
        )
        expected = DataFrame(
            {
                "letter": ["a", "b"],
                "array_field": [[""], []],
                "len": pandas.Series([1, 0], dtype="Int64"),
            },
            columns=["letter", "array_field", "len"],
        )
        tm.assert_frame_equal(df, expected)

    def test_array_agg(self, project_id):
        query = """WITH t as (
                SELECT "a" letter, 1 num
                UNION ALL
                SELECT "b" letter, 2 num
                UNION ALL
                SELECT "a" letter, 3 num)

                select letter, array_agg(num order by num ASC) numbers
                from t
                group by letter
                order by letter ASC"""
        df = gbq.read_gbq(
            query,
            project_id=project_id,
            credentials=self.credentials,
            dialect="standard",
        )
        tm.assert_frame_equal(
            df,
            DataFrame([["a", [1, 3]], ["b", [2]]], columns=["letter", "numbers"]),
        )

    def test_array_of_floats(self, project_id):
        query = """select [1.1, 2.2, 3.3] as a, 4 as b"""
        df = gbq.read_gbq(
            query,
            project_id=project_id,
            credentials=self.credentials,
            dialect="standard",
        )
        tm.assert_frame_equal(
            df,
            DataFrame(
                {"a": [[1.1, 2.2, 3.3]], "b": pandas.Series([4], dtype="Int64")},
                columns=["a", "b"],
            ),
        )

    def test_tokyo(self, tokyo_dataset, tokyo_table, project_id):
        df = gbq.read_gbq(
            "SELECT MAX(year) AS max_year FROM {}.{}".format(
                tokyo_dataset, tokyo_table
            ),
            dialect="standard",
            location="asia-northeast1",
            project_id=project_id,
            credentials=self.credentials,
        )
        assert df["max_year"][0] >= 2000

    def test_columns_as_alias(self, project_id):
        query = "SELECT 'a' AS string_1, 'b' AS string_2, 'c' AS string_3"
        columns = ["string_2", "string_1", "string_3"]

        df = gbq.read_gbq(
            query,
            project_id=project_id,
            columns=columns,
            credentials=self.credentials,
            dialect="standard",
        )

        expected = DataFrame({"string_1": ["a"], "string_2": ["b"], "string_3": ["c"]})[
            columns
        ]

        # Verify that the result_frame matches the expected DataFrame
        tm.assert_frame_equal(df, expected)

    def test_columns_and_col_order_raises_error(self, project_id):
        query = "SELECT 'a' AS string_1, 'b' AS string_2, 'c' AS string_3"
        columns = ["string_2", "string_1"]
        col_order = ["string_3", "string_1", "string_2"]

        with pytest.raises(ValueError):
            gbq.read_gbq(
                query,
                project_id=project_id,
                columns=columns,
                col_order=col_order,
                credentials=self.credentials,
                dialect="standard",
            )

    def test_read_gbq_with_dry_run(self, project_id):
        query = "SELECT 1"
        result = gbq.read_gbq(
            query,
            project_id=project_id,
            credentials=self.credentials,
            dialect="standard",
            dry_run=True,
        )
        assert isinstance(result, pandas.Series)
        assert result["totalBytesProcessed"] >= 0


class TestToGBQIntegration(object):
    @pytest.fixture(autouse=True, scope="function")
    def setup(self, project, credentials, random_dataset_id):
        # - PER-TEST FIXTURES -
        # put here any instruction you want to be run *BEFORE* *EVERY* test is
        # executed.
        self.credentials = credentials
        self.gbq_connector = gbq.GbqConnector(project, credentials=credentials)
        self.bqclient = self.gbq_connector.client
        self.table = gbq._Table(project, random_dataset_id, credentials=credentials)
        self.destination_table = "{}.{}".format(random_dataset_id, TABLE_ID)

    def test_upload_data(self, project_id):
        test_id = "1"
        test_size = 20001
        df = make_mixed_dataframe_v2(test_size)

        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id,
            chunksize=10000,
            credentials=self.credentials,
        )

        result = gbq.read_gbq(
            "SELECT COUNT(*) AS num_rows FROM {0}".format(
                self.destination_table + test_id
            ),
            project_id=project_id,
            credentials=self.credentials,
            dialect="legacy",
        )
        assert result["num_rows"][0] == test_size

    def test_upload_empty_data(self, project_id):
        test_id = "data_with_0_rows"
        df = DataFrame()

        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id,
            credentials=self.credentials,
        )

        table = self.bqclient.get_table(self.destination_table + test_id)
        assert table.num_rows == 0
        assert len(table.schema) == 0

    def test_upload_empty_data_with_schema(self, project_id):
        test_id = "data_with_0_rows"
        df = DataFrame(
            {"a": pandas.Series(dtype="int64"), "b": pandas.Series(dtype="object")}
        )

        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id,
            credentials=self.credentials,
        )

        table = self.bqclient.get_table(self.destination_table + test_id)
        assert table.num_rows == 0
        schema = table.schema
        assert schema[0].field_type == "INTEGER"
        assert schema[1].field_type == "STRING"

    def test_upload_data_if_table_exists_fail(self, project_id):
        test_id = "2"
        test_size = 10
        df = make_mixed_dataframe_v2(test_size)

        # Initialize table with sample data
        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id,
            chunksize=10000,
            credentials=self.credentials,
        )

        # Test the default value of if_exists == 'fail'
        with pytest.raises(gbq.TableCreationError):
            gbq.to_gbq(
                df,
                self.destination_table + test_id,
                project_id,
                credentials=self.credentials,
            )

        # Test the if_exists parameter with value 'fail'
        with pytest.raises(gbq.TableCreationError):
            gbq.to_gbq(
                df,
                self.destination_table + test_id,
                project_id,
                if_exists="fail",
                credentials=self.credentials,
            )

    def test_upload_data_if_table_exists_append(self, project_id):
        test_id = "3"
        test_size = 10
        df = make_mixed_dataframe_v2(test_size)
        df_different_schema = make_mixed_dataframe_v1()

        # Initialize table with sample data
        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id,
            chunksize=10000,
            credentials=self.credentials,
        )

        # Test the if_exists parameter with value 'append'
        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id,
            if_exists="append",
            credentials=self.credentials,
        )

        result = gbq.read_gbq(
            "SELECT COUNT(*) AS num_rows FROM {0}".format(
                self.destination_table + test_id
            ),
            project_id=project_id,
            credentials=self.credentials,
            dialect="legacy",
        )
        assert result["num_rows"][0] == test_size * 2

        # Try inserting with a different schema, confirm failure
        with pytest.raises(gbq.InvalidSchema):
            gbq.to_gbq(
                df_different_schema,
                self.destination_table + test_id,
                project_id,
                if_exists="append",
                credentials=self.credentials,
            )

    def test_upload_subset_columns_if_table_exists_append(self, project_id):
        # Issue 24: Upload is succesful if dataframe has columns
        # which are a subset of the current schema
        test_id = "16"
        test_size = 10
        df = make_mixed_dataframe_v2(test_size)
        df_subset_cols = df.iloc[:, :2]

        # Initialize table with sample data
        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id,
            chunksize=10000,
            credentials=self.credentials,
        )

        # Test the if_exists parameter with value 'append'
        gbq.to_gbq(
            df_subset_cols,
            self.destination_table + test_id,
            project_id,
            if_exists="append",
            credentials=self.credentials,
        )

        result = gbq.read_gbq(
            "SELECT COUNT(*) AS num_rows FROM {0}".format(
                self.destination_table + test_id
            ),
            project_id=project_id,
            credentials=self.credentials,
            dialect="legacy",
        )
        assert result["num_rows"][0] == test_size * 2

    def test_upload_data_if_table_exists_replace(self, project_id):
        test_id = "4"
        test_size = 10
        df = make_mixed_dataframe_v2(test_size)
        df_different_schema = make_mixed_dataframe_v1()
        schema_new = gbq.generate_bq_schema(df_different_schema)

        # Initialize table with sample data
        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id,
            chunksize=10000,
            credentials=self.credentials,
        )

        # When if_exists == 'replace', table schema should change too.
        gbq.to_gbq(
            df_different_schema,
            self.destination_table + test_id,
            project_id,
            if_exists="replace",
            credentials=self.credentials,
        )

        df_new = gbq.read_gbq(
            "SELECT * FROM {0}".format(self.destination_table + test_id),
            project_id=project_id,
            credentials=self.credentials,
            dialect="legacy",
        )

        schema_returned = gbq.generate_bq_schema(df_new)
        assert schema_new == schema_returned
        assert df_new.shape[0] == 5

    def test_upload_data_if_table_exists_raises_value_error(self, project_id):
        test_id = "4"
        test_size = 10
        df = make_mixed_dataframe_v2(test_size)

        # Test invalid value for if_exists parameter raises value error
        with pytest.raises(ValueError):
            gbq.to_gbq(
                df,
                self.destination_table + test_id,
                project_id,
                if_exists="xxxxx",
                credentials=self.credentials,
            )

    def test_google_upload_errors_should_raise_exception(self, project_id):
        raise pytest.skip("buggy test")

        test_id = "5"
        test_timestamp = datetime.datetime.now(zoneinfo.ZoneInfo("UTC"))
        bad_df = DataFrame(
            {
                "bools": [False, False],
                "flts": [0.0, 1.0],
                "ints": [0, "1"],
                "strs": ["a", 1],
                "times": [test_timestamp, test_timestamp],
            },
            index=range(2),
        )

        with pytest.raises(gbq.StreamingInsertError):
            gbq.to_gbq(
                bad_df,
                self.destination_table + test_id,
                project_id,
                credentials=self.credentials,
            )

    def test_upload_mixed_float_and_int(self, project_id):
        """Test that we can upload a dataframe containing an int64 and float64 column.
        See: https://github.com/pydata/pandas-gbq/issues/116
        """
        test_id = "mixed_float_and_int"
        test_size = 2
        df = DataFrame(
            [[1, 1.1], [2, 2.2]],
            index=["row 1", "row 2"],
            columns=["intColumn", "floatColumn"],
        )

        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id=project_id,
            credentials=self.credentials,
        )

        result_df = gbq.read_gbq(
            "SELECT * FROM {0}".format(self.destination_table + test_id),
            project_id=project_id,
            credentials=self.credentials,
            dialect="legacy",
        )

        assert len(result_df) == test_size

    def test_upload_data_with_newlines(self, project_id):
        test_id = "data_with_newlines"
        test_size = 2
        df = DataFrame({"s": ["abcd", "ef\ngh"]})

        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id=project_id,
            credentials=self.credentials,
        )

        result_df = gbq.read_gbq(
            "SELECT * FROM {0}".format(self.destination_table + test_id),
            project_id=project_id,
            credentials=self.credentials,
            dialect="legacy",
        )

        assert len(result_df) == test_size

        if sys.version_info.major < 3:
            pytest.skip(msg="Unicode comparison in Py2 not working")

        result = result_df["s"].sort_values()
        expected = df["s"].sort_values()

        tm.assert_series_equal(expected, result)

    def test_upload_data_flexible_column_order(self, project_id):
        test_id = "13"
        test_size = 10
        df = make_mixed_dataframe_v2(test_size)

        # Initialize table with sample data
        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id,
            chunksize=10000,
            credentials=self.credentials,
        )

        df_columns_reversed = df[df.columns[::-1]]

        gbq.to_gbq(
            df_columns_reversed,
            self.destination_table + test_id,
            project_id,
            if_exists="append",
            credentials=self.credentials,
        )

    def test_upload_data_with_valid_user_schema(self, project_id):
        # Issue #46; tests test scenarios with user-provided
        # schemas
        df = make_mixed_dataframe_v1()
        test_id = "18"
        test_schema = [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
        destination_table = self.destination_table + test_id
        gbq.to_gbq(
            df,
            destination_table,
            project_id,
            credentials=self.credentials,
            table_schema=test_schema,
        )
        dataset, table = destination_table.split(".")
        assert verify_schema(
            self.gbq_connector, dataset, table, dict(fields=test_schema)
        )

    def test_upload_data_with_invalid_user_schema_raises_error(self, project_id):
        df = make_mixed_dataframe_v1()
        test_id = "19"
        test_schema = [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "FLOAT"},
            {"name": "D", "type": "FLOAT"},
        ]
        destination_table = self.destination_table + test_id
        with pytest.raises(gbq.GenericGBQException):
            gbq.to_gbq(
                df,
                destination_table,
                project_id,
                credentials=self.credentials,
                table_schema=test_schema,
            )

    def test_upload_data_with_missing_schema_fields_raises_error(self, project_id):
        df = make_mixed_dataframe_v1()
        test_id = "20"
        test_schema = [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "FLOAT"},
        ]
        destination_table = self.destination_table + test_id
        with pytest.raises(gbq.GenericGBQException):
            gbq.to_gbq(
                df,
                destination_table,
                project_id,
                credentials=self.credentials,
                table_schema=test_schema,
            )

    @pytest.mark.skipif(
        packaging.version.parse(pandas.__version__).release >= (2, 0), reason=""
    )
    def test_upload_data_with_timestamp(self, project_id):
        test_id = "21"
        test_size = 6
        df = DataFrame(
            np.random.randn(test_size, 4),
            index=range(test_size),
            columns=list("ABCD"),
        )
        df["times"] = pandas.Series(
            [
                "2018-03-13T05:40:45.348318",
                "2018-04-13T05:40:45.348318",
                "2018-05-13T05:40:45.348318",
                "2018-06-13T05:40:45.348318",
                "2018-07-13T05:40:45.348318",
                "2018-08-13T05:40:45.348318",
            ],
            dtype="datetime64[ns]",
        ).dt.tz_localize("UTC")

        gbq.to_gbq(
            df,
            self.destination_table + test_id,
            project_id=project_id,
            credentials=self.credentials,
        )

        result_df = gbq.read_gbq(
            "SELECT * FROM {0}".format(self.destination_table + test_id),
            project_id=project_id,
            credentials=self.credentials,
            dialect="legacy",
        )

        assert len(result_df) == test_size

        expected = df["times"].sort_values()
        result = result_df["times"].sort_values()
        tm.assert_series_equal(expected, result)

    def test_upload_data_with_different_df_and_user_schema(self, project_id):
        df = make_mixed_dataframe_v1()
        df["A"] = df["A"].astype(str)
        df["B"] = df["B"].astype(str)
        test_id = "22"
        test_schema = [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
        destination_table = self.destination_table + test_id
        gbq.to_gbq(
            df,
            destination_table,
            project_id,
            credentials=self.credentials,
            table_schema=test_schema,
            # Loading string pandas series to FLOAT column not supported with
            # Parquet.
            api_method="load_csv",
        )
        dataset, table = destination_table.split(".")
        assert verify_schema(
            self.gbq_connector, dataset, table, dict(fields=test_schema)
        )

    def test_upload_data_tokyo(self, project_id, tokyo_dataset, bigquery_client):
        from google.cloud import bigquery

        test_size = 10
        df = make_mixed_dataframe_v2(test_size)
        tokyo_destination = "{}.to_gbq_test".format(tokyo_dataset)

        # Initialize table with sample data
        gbq.to_gbq(
            df,
            tokyo_destination,
            project_id,
            credentials=self.credentials,
            location="asia-northeast1",
        )

        table = bigquery_client.get_table(
            bigquery.TableReference(
                bigquery.DatasetReference(project_id, tokyo_dataset),
                "to_gbq_test",
            )
        )
        assert table.num_rows > 0

    def test_upload_data_tokyo_non_existing_dataset(
        self, project_id, random_dataset_id, bigquery_client
    ):
        from google.cloud import bigquery

        test_size = 10
        df = make_mixed_dataframe_v2(test_size)
        non_existing_tokyo_dataset = random_dataset_id
        non_existing_tokyo_destination = "{}.to_gbq_test".format(
            non_existing_tokyo_dataset
        )

        # Initialize table with sample data
        gbq.to_gbq(
            df,
            non_existing_tokyo_destination,
            project_id,
            credentials=self.credentials,
            location="asia-northeast1",
        )

        table = bigquery_client.get_table(
            bigquery.TableReference(
                bigquery.DatasetReference(project_id, non_existing_tokyo_dataset),
                "to_gbq_test",
            )
        )
        assert table.num_rows > 0


# _Dataset tests


def test_create_dataset(bigquery_client, gbq_dataset, random_dataset_id, project_id):
    from google.cloud import bigquery

    gbq_dataset.create(random_dataset_id)
    dataset_reference = bigquery.DatasetReference(project_id, random_dataset_id)
    assert bigquery_client.get_dataset(dataset_reference) is not None


def test_create_dataset_already_exists(gbq_dataset, random_dataset_id):
    gbq_dataset.create(random_dataset_id)
    with pytest.raises(gbq.DatasetCreationError):
        gbq_dataset.create(random_dataset_id)


def test_dataset_exists(gbq_dataset, random_dataset_id):
    gbq_dataset.create(random_dataset_id)
    assert gbq_dataset.exists(random_dataset_id)


def test_dataset_does_not_exist(gbq_dataset, random_dataset_id):
    assert not gbq_dataset.exists(random_dataset_id)


# _Table tests


def test_create_table(gbq_table):
    schema = gbq._generate_bq_schema(make_mixed_dataframe_v1())
    gbq_table.create("test_create_table", schema)
    assert gbq_table.exists("test_create_table")


def test_create_table_already_exists(gbq_table):
    schema = gbq._generate_bq_schema(make_mixed_dataframe_v1())
    gbq_table.create("test_create_table_exists", schema)
    with pytest.raises(gbq.TableCreationError):
        gbq_table.create("test_create_table_exists", schema)


def test_table_does_not_exist(gbq_table):
    assert not gbq_table.exists("test_table_does_not_exist")


def test_delete_table(gbq_table):
    test_schema = {
        "fields": [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
    }
    gbq_table.create("test_delete_table", test_schema)
    gbq_table.delete("test_delete_table")
    assert not gbq_table.exists("test_delete_table")


def test_create_table_data_dataset_does_not_exist(
    project, credentials, gbq_dataset, random_dataset_id
):
    table_id = "test_create_table_data_dataset_does_not_exist"
    table_with_new_dataset = gbq._Table(
        project, random_dataset_id, credentials=credentials
    )
    df = make_mixed_dataframe_v2(10)
    table_with_new_dataset.create(table_id, gbq._generate_bq_schema(df))
    assert gbq_dataset.exists(random_dataset_id)
    assert table_with_new_dataset.exists(table_id)


def test_verify_schema_allows_flexible_column_order(gbq_table, gbq_connector):
    table_id = "test_verify_schema_allows_flexible_column_order"
    test_schema_1 = {
        "fields": [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
    }
    test_schema_2 = {
        "fields": [
            {"name": "A", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
            {"name": "B", "type": "FLOAT"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
    }

    gbq_table.create(table_id, test_schema_1)
    assert verify_schema(gbq_connector, gbq_table.dataset_id, table_id, test_schema_2)


def test_verify_schema_fails_different_data_type(gbq_table, gbq_connector):
    table_id = "test_verify_schema_fails_different_data_type"
    test_schema_1 = {
        "fields": [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
    }
    test_schema_2 = {
        "fields": [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "STRING"},
            {"name": "C", "type": "STRING"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
    }

    gbq_table.create(table_id, test_schema_1)
    assert not verify_schema(
        gbq_connector, gbq_table.dataset_id, table_id, test_schema_2
    )


def test_verify_schema_fails_different_structure(gbq_table, gbq_connector):
    table_id = "test_verify_schema_fails_different_structure"
    test_schema_1 = {
        "fields": [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
    }
    test_schema_2 = {
        "fields": [
            {"name": "A", "type": "FLOAT"},
            {"name": "B2", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
    }

    gbq_table.create(table_id, test_schema_1)
    assert not verify_schema(
        gbq_connector, gbq_table.dataset_id, table_id, test_schema_2
    )


def test_verify_schema_ignores_field_mode(gbq_table, gbq_connector):
    table_id = "test_verify_schema_ignores_field_mode"
    test_schema_1 = {
        "fields": [
            {"name": "A", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "B", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "C", "type": "STRING", "mode": "NULLABLE"},
            {"name": "D", "type": "TIMESTAMP", "mode": "REQUIRED"},
        ]
    }
    test_schema_2 = {
        "fields": [
            {"name": "A", "type": "FLOAT"},
            {"name": "B", "type": "FLOAT"},
            {"name": "C", "type": "STRING"},
            {"name": "D", "type": "TIMESTAMP"},
        ]
    }

    gbq_table.create(table_id, test_schema_1)
    assert verify_schema(gbq_connector, gbq_table.dataset_id, table_id, test_schema_2)


def test_retrieve_schema(gbq_table, gbq_connector):
    # Issue #24 schema function returns the schema in biquery
    table_id = "test_retrieve_schema"
    test_schema = {
        "fields": [
            {"name": "A", "type": "FLOAT", "mode": "NULLABLE", "description": None},
            {"name": "B", "type": "FLOAT", "mode": "NULLABLE", "description": None},
            {"name": "C", "type": "STRING", "mode": "NULLABLE", "description": None},
            {
                "name": "D",
                "type": "TIMESTAMP",
                "mode": "NULLABLE",
                "description": None,
            },
        ]
    }

    gbq_table.create(table_id, test_schema)
    expected = [
        {"name": "A", "type": "FLOAT"},
        {"name": "B", "type": "FLOAT"},
        {"name": "C", "type": "STRING"},
        {"name": "D", "type": "TIMESTAMP"},
    ]
    assert verify_schema(
        gbq_connector, gbq_table.dataset_id, table_id, {"fields": expected}
    )


def test_to_gbq_does_not_override_mode(gbq_table, gbq_connector):
    # See: https://github.com/pydata/pandas-gbq/issues/315
    table_id = "test_to_gbq_does_not_override_mode"
    table_schema = {
        "fields": [
            {"mode": "REQUIRED", "name": "A", "type": "FLOAT", "description": "A"},
            {"mode": "NULLABLE", "name": "B", "type": "FLOAT", "description": "B"},
            {"mode": "NULLABLE", "name": "C", "type": "STRING", "description": "C"},
        ]
    }

    gbq_table.create(table_id, table_schema)
    gbq.to_gbq(
        pandas.DataFrame({"A": [1.0], "B": [2.0], "C": ["a"]}),
        "{0}.{1}".format(gbq_table.dataset_id, table_id),
        project_id=gbq_connector.project_id,
        if_exists="append",
    )

    assert verify_schema(gbq_connector, gbq_table.dataset_id, table_id, table_schema)


def test_gbqconnector_init_with_bq_client(bigquery_client):
    gbq_connector = gbq.GbqConnector(
        project_id="project_id", credentials=None, bigquery_client=bigquery_client
    )

    assert gbq_connector.project_id == bigquery_client.project
    assert gbq_connector.credentials is bigquery_client._credentials
    assert gbq_connector.client is bigquery_client
