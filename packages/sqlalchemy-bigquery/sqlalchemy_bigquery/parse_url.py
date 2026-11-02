# Copyright (c) 2017 The sqlalchemy-bigquery Authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import re

from google.cloud.bigquery import QueryJobConfig
from google.cloud.bigquery.dataset import DatasetReference
from google.cloud.bigquery.job import (
    CreateDisposition,
    QueryPriority,
    SchemaUpdateOption,
    WriteDisposition,
)
from google.cloud.bigquery.table import EncryptionConfiguration, TableReference

GROUP_DELIMITER = re.compile(r"\s*\,\s*")
KEY_VALUE_DELIMITER = re.compile(r"\s*\:\s*")


def parse_boolean(bool_string):
    bool_string = bool_string.lower()
    if bool_string == "true":
        return True
    elif bool_string == "false":
        return False
    else:
        raise ValueError()


def parse_url(url):  # noqa: C901
    query = dict(url.query)  # need mutable query.

    # use_legacy_sql (legacy)
    if "use_legacy_sql" in query:
        raise ValueError("legacy sql is not supported by this dialect")
    # allow_large_results (legacy)
    if "allow_large_results" in query:
        raise ValueError(
            "allow_large_results is only allowed for legacy sql, which is not supported by this dialect"
        )
    # flatten_results (legacy)
    if "flatten_results" in query:
        raise ValueError(
            "flatten_results is only allowed for legacy sql, which is not supported by this dialect"
        )
    # maximum_billing_tier (deprecated)
    if "maximum_billing_tier" in query:
        raise ValueError("maximum_billing_tier is a deprecated argument")

    project_id = url.host
    location = None
    dataset_id = url.database or None
    arraysize = None
    credentials_path = None
    credentials_base64 = None
    list_tables_page_size = None
    user_supplied_client = False

    # location
    if "location" in query:
        location = query.pop("location")

    # credentials_path
    if "credentials_path" in query:
        credentials_path = query.pop("credentials_path")

    # credentials_base64
    if "credentials_base64" in query:
        credentials_base64 = query.pop("credentials_base64")

    # arraysize
    if "arraysize" in query:
        str_arraysize = query.pop("arraysize")
        try:
            arraysize = int(str_arraysize)
        except ValueError:
            raise ValueError("invalid int in url query arraysize: " + str_arraysize)

    if "list_tables_page_size" in query:
        str_list_tables_page_size = query.pop("list_tables_page_size")
        try:
            list_tables_page_size = int(str_list_tables_page_size)
        except ValueError:
            raise ValueError(
                "invalid int in url query list_tables_page_size: "
                + str_list_tables_page_size
            )

    # user_supplied_client
    if "user_supplied_client" in query:
        user_supplied_client = query.pop("user_supplied_client").lower() == "true"

    # if only these "non-config" values were present, the dict will now be empty
    if not query:
        # if a dataset_id exists, we need to return a job_config that isn't None
        # so it can be updated with a dataset reference from the client
        if dataset_id:
            return (
                project_id,
                location,
                dataset_id,
                arraysize,
                credentials_path,
                credentials_base64,
                QueryJobConfig(),
                list_tables_page_size,
                user_supplied_client,
            )
        else:
            return (
                project_id,
                location,
                dataset_id,
                arraysize,
                credentials_path,
                credentials_base64,
                None,
                list_tables_page_size,
                user_supplied_client,
            )

    job_config = QueryJobConfig()

    # clustering_fields list(str)
    if "clustering_fields" in query:
        clustering_fields = GROUP_DELIMITER.split(query["clustering_fields"])
        job_config.clustering_fields = list(clustering_fields)

    # create_disposition
    if "create_disposition" in query:
        create_disposition = query["create_disposition"]
        try:
            job_config.create_disposition = getattr(
                CreateDisposition, create_disposition
            )
        except AttributeError:
            raise ValueError(
                "invalid create_disposition in url query: " + create_disposition
            )

    # default_dataset
    if "default_dataset" in query or "dataset_id" in query or "project_id" in query:
        raise ValueError(
            "don't pass default_dataset, dataset_id, project_id in url query, instead use the url host and database"
        )

    # destination
    if "destination" in query:
        dest_project = None
        dest_dataset = None
        dest_table = None

        try:
            dest_project, dest_dataset, dest_table = query["destination"].split(".")
        except ValueError:
            raise ValueError(
                "url query destination parameter should be fully qualified with project, dataset, and table"
            )

        job_config.destination = TableReference(
            DatasetReference(dest_project, dest_dataset), dest_table
        )

    # destination_encryption_configuration
    if "destination_encryption_configuration" in query:
        job_config.destination_encryption_configuration = EncryptionConfiguration(
            query["destination_encryption_configuration"]
        )

    # dry_run
    if "dry_run" in query:
        try:
            job_config.dry_run = parse_boolean(query["dry_run"])
        except ValueError:
            raise ValueError(
                "invalid boolean in url query for dry_run: " + query["dry_run"]
            )

    # labels
    if "labels" in query:
        label_groups = GROUP_DELIMITER.split(query["labels"])
        labels = {}
        for label_group in label_groups:
            try:
                key, value = KEY_VALUE_DELIMITER.split(label_group)
            except ValueError:
                raise ValueError("malformed url query in labels: " + label_group)
            labels[key] = value

        job_config.labels = labels

    # maximum_bytes_billed
    if "maximum_bytes_billed" in query:
        try:
            job_config.maximum_bytes_billed = int(query["maximum_bytes_billed"])
        except ValueError:
            raise ValueError(
                "invalid int in url query maximum_bytes_billed: "
                + query["maximum_bytes_billed"]
            )

    # priority
    if "priority" in query:
        try:
            job_config.priority = getattr(QueryPriority, query["priority"])
        except AttributeError:
            raise ValueError("invalid priority in url query: " + query["priority"])

    # query_parameters
    if "query_parameters" in query:
        raise NotImplementedError("url query query_parameters not implemented")

    # schema_update_options
    if "schema_update_options" in query:
        schema_update_options = GROUP_DELIMITER.split(query["schema_update_options"])
        try:
            job_config.schema_update_options = [
                getattr(SchemaUpdateOption, schema_update_option)
                for schema_update_option in schema_update_options
            ]
        except AttributeError:
            raise ValueError(
                "invalid schema_update_options in url query: "
                + query["schema_update_options"]
            )

    # table_definitions
    if "table_definitions" in query:
        raise NotImplementedError("url query table_definitions not implemented")

    # time_partitioning
    if "time_partitioning" in query:
        raise NotImplementedError("url query time_partitioning not implemented")

    # udf_resources
    if "udf_resources" in query:
        raise NotImplementedError("url query udf_resources not implemented")

    # use_query_cache
    if "use_query_cache" in query:
        try:
            job_config.use_query_cache = parse_boolean(query["use_query_cache"])
        except ValueError:
            raise ValueError(
                "invalid boolean in url query for use_query_cache: "
                + query["use_query_cache"]
            )

    # write_disposition
    if "write_disposition" in query:
        try:
            job_config.write_disposition = getattr(
                WriteDisposition, query["write_disposition"]
            )
        except AttributeError:
            raise ValueError(
                "invalid write_disposition in url query: " + query["write_disposition"]
            )

    return (
        project_id,
        location,
        dataset_id,
        arraysize,
        credentials_path,
        credentials_base64,
        job_config,
        list_tables_page_size,
        user_supplied_client,
    )
