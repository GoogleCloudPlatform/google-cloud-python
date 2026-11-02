# -*- coding: utf-8 -*-
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
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.bigquery.logging.v1",
    manifest={
        "AuditData",
        "TableInsertRequest",
        "TableUpdateRequest",
        "TableInsertResponse",
        "TableUpdateResponse",
        "DatasetListRequest",
        "DatasetInsertRequest",
        "DatasetInsertResponse",
        "DatasetUpdateRequest",
        "DatasetUpdateResponse",
        "JobInsertRequest",
        "JobInsertResponse",
        "JobQueryRequest",
        "JobQueryResponse",
        "JobGetQueryResultsRequest",
        "JobGetQueryResultsResponse",
        "JobQueryDoneResponse",
        "JobCompletedEvent",
        "TableDataReadEvent",
        "TableDataListRequest",
        "Table",
        "TableInfo",
        "TableViewDefinition",
        "Dataset",
        "DatasetInfo",
        "BigQueryAcl",
        "Job",
        "JobConfiguration",
        "TableDefinition",
        "JobStatus",
        "JobStatistics",
        "DatasetName",
        "TableName",
        "JobName",
        "EncryptionInfo",
    },
)


class AuditData(proto.Message):
    r"""BigQuery request and response messages for audit log. Note:
    ``Table.schema`` has been deprecated in favor of
    ``Table.schemaJson``. ``Table.schema`` may continue to be present in
    your logs during this transition.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        table_insert_request (google.cloud.bigquery_logging_v1.types.TableInsertRequest):
            Table insert request.

            This field is a member of `oneof`_ ``request``.
        table_update_request (google.cloud.bigquery_logging_v1.types.TableUpdateRequest):
            Table update request.

            This field is a member of `oneof`_ ``request``.
        dataset_list_request (google.cloud.bigquery_logging_v1.types.DatasetListRequest):
            Dataset list request.

            This field is a member of `oneof`_ ``request``.
        dataset_insert_request (google.cloud.bigquery_logging_v1.types.DatasetInsertRequest):
            Dataset insert request.

            This field is a member of `oneof`_ ``request``.
        dataset_update_request (google.cloud.bigquery_logging_v1.types.DatasetUpdateRequest):
            Dataset update request.

            This field is a member of `oneof`_ ``request``.
        job_insert_request (google.cloud.bigquery_logging_v1.types.JobInsertRequest):
            Job insert request.

            This field is a member of `oneof`_ ``request``.
        job_query_request (google.cloud.bigquery_logging_v1.types.JobQueryRequest):
            Job query request.

            This field is a member of `oneof`_ ``request``.
        job_get_query_results_request (google.cloud.bigquery_logging_v1.types.JobGetQueryResultsRequest):
            Job get query results request.

            This field is a member of `oneof`_ ``request``.
        table_data_list_request (google.cloud.bigquery_logging_v1.types.TableDataListRequest):
            Table data-list request.

            This field is a member of `oneof`_ ``request``.
        set_iam_policy_request (google.iam.v1.iam_policy_pb2.SetIamPolicyRequest):
            Iam policy request.

            This field is a member of `oneof`_ ``request``.
        table_insert_response (google.cloud.bigquery_logging_v1.types.TableInsertResponse):
            Table insert response.

            This field is a member of `oneof`_ ``response``.
        table_update_response (google.cloud.bigquery_logging_v1.types.TableUpdateResponse):
            Table update response.

            This field is a member of `oneof`_ ``response``.
        dataset_insert_response (google.cloud.bigquery_logging_v1.types.DatasetInsertResponse):
            Dataset insert response.

            This field is a member of `oneof`_ ``response``.
        dataset_update_response (google.cloud.bigquery_logging_v1.types.DatasetUpdateResponse):
            Dataset update response.

            This field is a member of `oneof`_ ``response``.
        job_insert_response (google.cloud.bigquery_logging_v1.types.JobInsertResponse):
            Job insert response.

            This field is a member of `oneof`_ ``response``.
        job_query_response (google.cloud.bigquery_logging_v1.types.JobQueryResponse):
            Job query response.

            This field is a member of `oneof`_ ``response``.
        job_get_query_results_response (google.cloud.bigquery_logging_v1.types.JobGetQueryResultsResponse):
            Job get query results response.

            This field is a member of `oneof`_ ``response``.
        job_query_done_response (google.cloud.bigquery_logging_v1.types.JobQueryDoneResponse):
            Deprecated: Job query-done response. Use this
            information for usage analysis.

            This field is a member of `oneof`_ ``response``.
        policy_response (google.iam.v1.policy_pb2.Policy):
            Iam Policy.

            This field is a member of `oneof`_ ``response``.
        job_completed_event (google.cloud.bigquery_logging_v1.types.JobCompletedEvent):
            A job completion event.
        table_data_read_events (MutableSequence[google.cloud.bigquery_logging_v1.types.TableDataReadEvent]):
            Information about the table access events.
    """

    table_insert_request: "TableInsertRequest" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="request",
        message="TableInsertRequest",
    )
    table_update_request: "TableUpdateRequest" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="request",
        message="TableUpdateRequest",
    )
    dataset_list_request: "DatasetListRequest" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="request",
        message="DatasetListRequest",
    )
    dataset_insert_request: "DatasetInsertRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="request",
        message="DatasetInsertRequest",
    )
    dataset_update_request: "DatasetUpdateRequest" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="request",
        message="DatasetUpdateRequest",
    )
    job_insert_request: "JobInsertRequest" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="request",
        message="JobInsertRequest",
    )
    job_query_request: "JobQueryRequest" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="request",
        message="JobQueryRequest",
    )
    job_get_query_results_request: "JobGetQueryResultsRequest" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="request",
        message="JobGetQueryResultsRequest",
    )
    table_data_list_request: "TableDataListRequest" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="request",
        message="TableDataListRequest",
    )
    set_iam_policy_request: iam_policy_pb2.SetIamPolicyRequest = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="request",
        message=iam_policy_pb2.SetIamPolicyRequest,
    )
    table_insert_response: "TableInsertResponse" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="response",
        message="TableInsertResponse",
    )
    table_update_response: "TableUpdateResponse" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="response",
        message="TableUpdateResponse",
    )
    dataset_insert_response: "DatasetInsertResponse" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="response",
        message="DatasetInsertResponse",
    )
    dataset_update_response: "DatasetUpdateResponse" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="response",
        message="DatasetUpdateResponse",
    )
    job_insert_response: "JobInsertResponse" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="response",
        message="JobInsertResponse",
    )
    job_query_response: "JobQueryResponse" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="response",
        message="JobQueryResponse",
    )
    job_get_query_results_response: "JobGetQueryResultsResponse" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="response",
        message="JobGetQueryResultsResponse",
    )
    job_query_done_response: "JobQueryDoneResponse" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="response",
        message="JobQueryDoneResponse",
    )
    policy_response: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="response",
        message=policy_pb2.Policy,
    )
    job_completed_event: "JobCompletedEvent" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="JobCompletedEvent",
    )
    table_data_read_events: MutableSequence["TableDataReadEvent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message="TableDataReadEvent",
    )


class TableInsertRequest(proto.Message):
    r"""Table insert request.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Table):
            The new table.
    """

    resource: "Table" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Table",
    )


class TableUpdateRequest(proto.Message):
    r"""Table update request.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Table):
            The table to be updated.
    """

    resource: "Table" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Table",
    )


class TableInsertResponse(proto.Message):
    r"""Table insert response.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Table):
            Final state of the inserted table.
    """

    resource: "Table" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Table",
    )


class TableUpdateResponse(proto.Message):
    r"""Table update response.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Table):
            Final state of the updated table.
    """

    resource: "Table" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Table",
    )


class DatasetListRequest(proto.Message):
    r"""Dataset list request.

    Attributes:
        list_all (bool):
            Whether to list all datasets, including
            hidden ones.
    """

    list_all: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class DatasetInsertRequest(proto.Message):
    r"""Dataset insert request.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Dataset):
            The dataset to be inserted.
    """

    resource: "Dataset" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Dataset",
    )


class DatasetInsertResponse(proto.Message):
    r"""Dataset insert response.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Dataset):
            Final state of the inserted dataset.
    """

    resource: "Dataset" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Dataset",
    )


class DatasetUpdateRequest(proto.Message):
    r"""Dataset update request.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Dataset):
            The dataset to be updated.
    """

    resource: "Dataset" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Dataset",
    )


class DatasetUpdateResponse(proto.Message):
    r"""Dataset update response.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Dataset):
            Final state of the updated dataset.
    """

    resource: "Dataset" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Dataset",
    )


class JobInsertRequest(proto.Message):
    r"""Job insert request.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Job):
            Job insert request.
    """

    resource: "Job" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Job",
    )


class JobInsertResponse(proto.Message):
    r"""Job insert response.

    Attributes:
        resource (google.cloud.bigquery_logging_v1.types.Job):
            Job insert response.
    """

    resource: "Job" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Job",
    )


class JobQueryRequest(proto.Message):
    r"""Job query request.

    Attributes:
        query (str):
            The query.
        max_results (int):
            The maximum number of results.
        default_dataset (google.cloud.bigquery_logging_v1.types.DatasetName):
            The default dataset for tables that do not
            have a dataset specified.
        project_id (str):
            Project that the query should be charged to.
        dry_run (bool):
            If true, don't actually run the job. Just
            check that it would run.
    """

    query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_results: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    default_dataset: "DatasetName" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DatasetName",
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    dry_run: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class JobQueryResponse(proto.Message):
    r"""Job query response.

    Attributes:
        total_results (int):
            The total number of rows in the full query
            result set.
        job (google.cloud.bigquery_logging_v1.types.Job):
            Information about the queried job.
    """

    total_results: int = proto.Field(
        proto.UINT64,
        number=1,
    )
    job: "Job" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Job",
    )


class JobGetQueryResultsRequest(proto.Message):
    r"""Job getQueryResults request.

    Attributes:
        max_results (int):
            Maximum number of results to return.
        start_row (int):
            Zero-based row number at which to start.
    """

    max_results: int = proto.Field(
        proto.UINT32,
        number=1,
    )
    start_row: int = proto.Field(
        proto.UINT64,
        number=2,
    )


class JobGetQueryResultsResponse(proto.Message):
    r"""Job getQueryResults response.

    Attributes:
        total_results (int):
            Total number of results in query results.
        job (google.cloud.bigquery_logging_v1.types.Job):
            The job that was created to run the query. It completed if
            ``job.status.state`` is ``DONE``. It failed if
            ``job.status.errorResult`` is also present.
    """

    total_results: int = proto.Field(
        proto.UINT64,
        number=1,
    )
    job: "Job" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Job",
    )


class JobQueryDoneResponse(proto.Message):
    r"""Job getQueryDone response.

    Attributes:
        job (google.cloud.bigquery_logging_v1.types.Job):
            The job and status information. The job completed if
            ``job.status.state`` is ``DONE``.
    """

    job: "Job" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Job",
    )


class JobCompletedEvent(proto.Message):
    r"""Query job completed event.

    Attributes:
        event_name (str):
            Name of the event.
        job (google.cloud.bigquery_logging_v1.types.Job):
            Job information.
    """

    event_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job: "Job" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Job",
    )


class TableDataReadEvent(proto.Message):
    r"""Table data read event. Only present for tables, not views,
    and is only included in the log record for the project that owns
    the table.

    Attributes:
        table_name (google.cloud.bigquery_logging_v1.types.TableName):
            Name of the accessed table.
        referenced_fields (MutableSequence[str]):
            A list of referenced fields. This information
            is not included by default. To enable this in
            the logs, please contact BigQuery support or
            open a bug in the BigQuery issue tracker.
    """

    table_name: "TableName" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TableName",
    )
    referenced_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class TableDataListRequest(proto.Message):
    r"""Table data-list request.

    Attributes:
        start_row (int):
            Starting row offset.
        max_results (int):
            Maximum number of results to return.
    """

    start_row: int = proto.Field(
        proto.UINT64,
        number=1,
    )
    max_results: int = proto.Field(
        proto.UINT32,
        number=2,
    )


class Table(proto.Message):
    r"""Describes a BigQuery table. See the
    `Table </bigquery/docs/reference/v2/tables>`__ API resource for more
    details on individual fields. Note: ``Table.schema`` has been
    deprecated in favor of ``Table.schemaJson``. ``Table.schema`` may
    continue to be present in your logs during this transition.

    Attributes:
        table_name (google.cloud.bigquery_logging_v1.types.TableName):
            The name of the table.
        info (google.cloud.bigquery_logging_v1.types.TableInfo):
            User-provided metadata for the table.
        schema_json (str):
            A JSON representation of the table's schema.
        view (google.cloud.bigquery_logging_v1.types.TableViewDefinition):
            If present, this is a virtual table defined
            by a SQL query.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The expiration date for the table, after
            which the table is deleted and the storage
            reclaimed. If not present, the table persists
            indefinitely.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the table was created.
        truncate_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the table was last truncated by an operation with a
            ``writeDisposition`` of ``WRITE_TRUNCATE``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the table was last modified.
        encryption (google.cloud.bigquery_logging_v1.types.EncryptionInfo):
            The table encryption information. Set when
            non-default encryption is used.
    """

    table_name: "TableName" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TableName",
    )
    info: "TableInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TableInfo",
    )
    schema_json: str = proto.Field(
        proto.STRING,
        number=8,
    )
    view: "TableViewDefinition" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TableViewDefinition",
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    truncate_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    encryption: "EncryptionInfo" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="EncryptionInfo",
    )


class TableInfo(proto.Message):
    r"""User-provided metadata for a table.

    Attributes:
        friendly_name (str):
            A short name for the table, such
            as\ ``"Analytics Data - Jan 2011"``.
        description (str):
            A long description, perhaps several
            paragraphs, describing the table contents in
            detail.
        labels (MutableMapping[str, str]):
            Labels provided for the table.
    """

    friendly_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class TableViewDefinition(proto.Message):
    r"""Describes a virtual table defined by a SQL query.

    Attributes:
        query (str):
            SQL query defining the view.
    """

    query: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Dataset(proto.Message):
    r"""BigQuery dataset information. See the
    `Dataset </bigquery/docs/reference/v2/datasets>`__ API resource for
    more details on individual fields.

    Attributes:
        dataset_name (google.cloud.bigquery_logging_v1.types.DatasetName):
            The name of the dataset.
        info (google.cloud.bigquery_logging_v1.types.DatasetInfo):
            User-provided metadata for the dataset.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the dataset was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the dataset was last modified.
        acl (google.cloud.bigquery_logging_v1.types.BigQueryAcl):
            The access control list for the dataset.
        default_table_expire_duration (google.protobuf.duration_pb2.Duration):
            If this field is present, each table that does not specify
            an expiration time is assigned an expiration time by adding
            this duration to the table's ``createTime``. If this field
            is empty, there is no default table expiration time.
    """

    dataset_name: "DatasetName" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DatasetName",
    )
    info: "DatasetInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DatasetInfo",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    acl: "BigQueryAcl" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="BigQueryAcl",
    )
    default_table_expire_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )


class DatasetInfo(proto.Message):
    r"""User-provided metadata for a dataset.

    Attributes:
        friendly_name (str):
            A short name for the dataset, such
            as\ ``"Analytics Data 2011"``.
        description (str):
            A long description, perhaps several
            paragraphs, describing the dataset contents in
            detail.
        labels (MutableMapping[str, str]):
            Labels provided for the dataset.
    """

    friendly_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class BigQueryAcl(proto.Message):
    r"""An access control list.

    Attributes:
        entries (MutableSequence[google.cloud.bigquery_logging_v1.types.BigQueryAcl.Entry]):
            Access control entry list.
    """

    class Entry(proto.Message):
        r"""Access control entry.

        Attributes:
            role (str):
                The granted role, which can be ``READER``, ``WRITER``, or
                ``OWNER``.
            group_email (str):
                Grants access to a group identified by an
                email address.
            user_email (str):
                Grants access to a user identified by an
                email address.
            domain (str):
                Grants access to all members of a domain.
            special_group (str):
                Grants access to special groups. Valid groups are
                ``PROJECT_OWNERS``, ``PROJECT_READERS``, ``PROJECT_WRITERS``
                and ``ALL_AUTHENTICATED_USERS``.
            view_name (google.cloud.bigquery_logging_v1.types.TableName):
                Grants access to a BigQuery View.
        """

        role: str = proto.Field(
            proto.STRING,
            number=1,
        )
        group_email: str = proto.Field(
            proto.STRING,
            number=2,
        )
        user_email: str = proto.Field(
            proto.STRING,
            number=3,
        )
        domain: str = proto.Field(
            proto.STRING,
            number=4,
        )
        special_group: str = proto.Field(
            proto.STRING,
            number=5,
        )
        view_name: "TableName" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="TableName",
        )

    entries: MutableSequence[Entry] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Entry,
    )


class Job(proto.Message):
    r"""Describes a job.

    Attributes:
        job_name (google.cloud.bigquery_logging_v1.types.JobName):
            Job name.
        job_configuration (google.cloud.bigquery_logging_v1.types.JobConfiguration):
            Job configuration.
        job_status (google.cloud.bigquery_logging_v1.types.JobStatus):
            Job status.
        job_statistics (google.cloud.bigquery_logging_v1.types.JobStatistics):
            Job statistics.
    """

    job_name: "JobName" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="JobName",
    )
    job_configuration: "JobConfiguration" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="JobConfiguration",
    )
    job_status: "JobStatus" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="JobStatus",
    )
    job_statistics: "JobStatistics" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="JobStatistics",
    )


class JobConfiguration(proto.Message):
    r"""Job configuration information. See the
    `Jobs </bigquery/docs/reference/v2/jobs>`__ API resource for more
    details on individual fields.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query (google.cloud.bigquery_logging_v1.types.JobConfiguration.Query):
            Query job information.

            This field is a member of `oneof`_ ``configuration``.
        load (google.cloud.bigquery_logging_v1.types.JobConfiguration.Load):
            Load job information.

            This field is a member of `oneof`_ ``configuration``.
        extract (google.cloud.bigquery_logging_v1.types.JobConfiguration.Extract):
            Extract job information.

            This field is a member of `oneof`_ ``configuration``.
        table_copy (google.cloud.bigquery_logging_v1.types.JobConfiguration.TableCopy):
            TableCopy job information.

            This field is a member of `oneof`_ ``configuration``.
        dry_run (bool):
            If true, don't actually run the job. Just
            check that it would run.
        labels (MutableMapping[str, str]):
            Labels provided for the job.
    """

    class Query(proto.Message):
        r"""Describes a query job, which executes a SQL-like query.

        Attributes:
            query (str):
                The SQL query to run.
            destination_table (google.cloud.bigquery_logging_v1.types.TableName):
                The table where results are written.
            create_disposition (str):
                Describes when a job is allowed to create a table:
                ``CREATE_IF_NEEDED``, ``CREATE_NEVER``.
            write_disposition (str):
                Describes how writes affect existing tables:
                ``WRITE_TRUNCATE``, ``WRITE_APPEND``, ``WRITE_EMPTY``.
            default_dataset (google.cloud.bigquery_logging_v1.types.DatasetName):
                If a table name is specified without a
                dataset in a query, this dataset will be added
                to table name.
            table_definitions (MutableSequence[google.cloud.bigquery_logging_v1.types.TableDefinition]):
                Describes data sources outside BigQuery, if
                needed.
            query_priority (str):
                Describes the priority given to the query:
                ``QUERY_INTERACTIVE`` or ``QUERY_BATCH``.
            destination_table_encryption (google.cloud.bigquery_logging_v1.types.EncryptionInfo):
                Result table encryption information. Set when
                non-default encryption is used.
            statement_type (str):
                Type of the statement (e.g. SELECT, INSERT, CREATE_TABLE,
                CREATE_MODEL..)
        """

        query: str = proto.Field(
            proto.STRING,
            number=1,
        )
        destination_table: "TableName" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="TableName",
        )
        create_disposition: str = proto.Field(
            proto.STRING,
            number=3,
        )
        write_disposition: str = proto.Field(
            proto.STRING,
            number=4,
        )
        default_dataset: "DatasetName" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="DatasetName",
        )
        table_definitions: MutableSequence["TableDefinition"] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="TableDefinition",
        )
        query_priority: str = proto.Field(
            proto.STRING,
            number=7,
        )
        destination_table_encryption: "EncryptionInfo" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="EncryptionInfo",
        )
        statement_type: str = proto.Field(
            proto.STRING,
            number=9,
        )

    class Load(proto.Message):
        r"""Describes a load job, which loads data from an external
        source via the  import pipeline.

        Attributes:
            source_uris (MutableSequence[str]):
                URIs for the data to be imported. Only Google
                Cloud Storage URIs are supported.
            schema_json (str):
                The table schema in JSON format
                representation of a TableSchema.
            destination_table (google.cloud.bigquery_logging_v1.types.TableName):
                The table where the imported data is written.
            create_disposition (str):
                Describes when a job is allowed to create a table:
                ``CREATE_IF_NEEDED``, ``CREATE_NEVER``.
            write_disposition (str):
                Describes how writes affect existing tables:
                ``WRITE_TRUNCATE``, ``WRITE_APPEND``, ``WRITE_EMPTY``.
            destination_table_encryption (google.cloud.bigquery_logging_v1.types.EncryptionInfo):
                Result table encryption information. Set when
                non-default encryption is used.
        """

        source_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        schema_json: str = proto.Field(
            proto.STRING,
            number=6,
        )
        destination_table: "TableName" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="TableName",
        )
        create_disposition: str = proto.Field(
            proto.STRING,
            number=4,
        )
        write_disposition: str = proto.Field(
            proto.STRING,
            number=5,
        )
        destination_table_encryption: "EncryptionInfo" = proto.Field(
            proto.MESSAGE,
            number=7,
            message="EncryptionInfo",
        )

    class Extract(proto.Message):
        r"""Describes an extract job, which exports data to an external
        source via the  export pipeline.

        Attributes:
            destination_uris (MutableSequence[str]):
                Google Cloud Storage URIs where extracted
                data should be written.
            source_table (google.cloud.bigquery_logging_v1.types.TableName):
                The source table.
        """

        destination_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        source_table: "TableName" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="TableName",
        )

    class TableCopy(proto.Message):
        r"""Describes a copy job, which copies an existing table to
        another table.

        Attributes:
            source_tables (MutableSequence[google.cloud.bigquery_logging_v1.types.TableName]):
                Source tables.
            destination_table (google.cloud.bigquery_logging_v1.types.TableName):
                Destination table.
            create_disposition (str):
                Describes when a job is allowed to create a table:
                ``CREATE_IF_NEEDED``, ``CREATE_NEVER``.
            write_disposition (str):
                Describes how writes affect existing tables:
                ``WRITE_TRUNCATE``, ``WRITE_APPEND``, ``WRITE_EMPTY``.
            destination_table_encryption (google.cloud.bigquery_logging_v1.types.EncryptionInfo):
                Result table encryption information. Set when
                non-default encryption is used.
        """

        source_tables: MutableSequence["TableName"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="TableName",
        )
        destination_table: "TableName" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="TableName",
        )
        create_disposition: str = proto.Field(
            proto.STRING,
            number=3,
        )
        write_disposition: str = proto.Field(
            proto.STRING,
            number=4,
        )
        destination_table_encryption: "EncryptionInfo" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="EncryptionInfo",
        )

    query: Query = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="configuration",
        message=Query,
    )
    load: Load = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="configuration",
        message=Load,
    )
    extract: Extract = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="configuration",
        message=Extract,
    )
    table_copy: TableCopy = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="configuration",
        message=TableCopy,
    )
    dry_run: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class TableDefinition(proto.Message):
    r"""Describes an external data source used in a query.

    Attributes:
        name (str):
            Name of the table, used in queries.
        source_uris (MutableSequence[str]):
            Google Cloud Storage URIs for the data to be
            imported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class JobStatus(proto.Message):
    r"""Running state of a job.

    Attributes:
        state (str):
            State of a job: ``PENDING``, ``RUNNING``, or ``DONE``.
        error (google.rpc.status_pb2.Status):
            If the job did not complete successfully,
            this field describes why.
        additional_errors (MutableSequence[google.rpc.status_pb2.Status]):
            Errors encountered during the running of the
            job. Do not necessarily mean that the job has
            completed or was unsuccessful.
    """

    state: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    additional_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )


class JobStatistics(proto.Message):
    r"""Job statistics that may change after a job starts.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the job was created.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the job started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the job ended.
        total_processed_bytes (int):
            Total bytes processed for a job.
        total_billed_bytes (int):
            Processed bytes, adjusted by the job's CPU
            usage.
        billing_tier (int):
            The tier assigned by CPU-based billing.
        total_slot_ms (int):
            The total number of slot-ms consumed by the
            query job.
        reservation_usage (MutableSequence[google.cloud.bigquery_logging_v1.types.JobStatistics.ReservationResourceUsage]):
            Reservation usage. This field reported
            misleading information and will no longer be
            populated. Aggregate usage of all jobs submitted
            to a reservation should provide a more reliable
            indicator of reservation imbalance.
        reservation (str):
            Reservation name or "unreserved" for
            on-demand resource usage.
        referenced_tables (MutableSequence[google.cloud.bigquery_logging_v1.types.TableName]):
            The first N tables accessed by the query job. Older queries
            that reference a large number of tables may not have all of
            their tables in this list. You can use the
            total_tables_processed count to know how many total tables
            were read in the query. For new queries, there is currently
            no limit.
        total_tables_processed (int):
            Total number of unique tables referenced in
            the query.
        referenced_views (MutableSequence[google.cloud.bigquery_logging_v1.types.TableName]):
            The first N views accessed by the query job. Older queries
            that reference a large number of views may not have all of
            their views in this list. You can use the
            total_tables_processed count to know how many total tables
            were read in the query. For new queries, there is currently
            no limit.
        total_views_processed (int):
            Total number of unique views referenced in
            the query.
        query_output_row_count (int):
            Number of output rows produced by the query
            job.
        total_load_output_bytes (int):
            Total bytes loaded for an import job.
    """

    class ReservationResourceUsage(proto.Message):
        r"""Job resource usage breakdown by reservation.

        Attributes:
            name (str):
                Reservation name or "unreserved" for
                on-demand resources usage.
            slot_ms (int):
                Total slot milliseconds used by the
                reservation for a particular job.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        slot_ms: int = proto.Field(
            proto.INT64,
            number=2,
        )

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    total_processed_bytes: int = proto.Field(
        proto.INT64,
        number=4,
    )
    total_billed_bytes: int = proto.Field(
        proto.INT64,
        number=5,
    )
    billing_tier: int = proto.Field(
        proto.INT32,
        number=7,
    )
    total_slot_ms: int = proto.Field(
        proto.INT64,
        number=8,
    )
    reservation_usage: MutableSequence[ReservationResourceUsage] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=ReservationResourceUsage,
    )
    reservation: str = proto.Field(
        proto.STRING,
        number=16,
    )
    referenced_tables: MutableSequence["TableName"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="TableName",
    )
    total_tables_processed: int = proto.Field(
        proto.INT32,
        number=10,
    )
    referenced_views: MutableSequence["TableName"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="TableName",
    )
    total_views_processed: int = proto.Field(
        proto.INT32,
        number=12,
    )
    query_output_row_count: int = proto.Field(
        proto.INT64,
        number=15,
    )
    total_load_output_bytes: int = proto.Field(
        proto.INT64,
        number=13,
    )


class DatasetName(proto.Message):
    r"""The fully-qualified name for a dataset.

    Attributes:
        project_id (str):
            The project ID.
        dataset_id (str):
            The dataset ID within the project.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TableName(proto.Message):
    r"""The fully-qualified name for a table.

    Attributes:
        project_id (str):
            The project ID.
        dataset_id (str):
            The dataset ID within the project.
        table_id (str):
            The table ID of the table within the dataset.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    table_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class JobName(proto.Message):
    r"""The fully-qualified name for a job.

    Attributes:
        project_id (str):
            The project ID.
        job_id (str):
            The job ID within the project.
        location (str):
            The job location.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class EncryptionInfo(proto.Message):
    r"""Describes encryption properties for a table or a job

    Attributes:
        kms_key_name (str):
            unique identifier for cloud kms key
    """

    kms_key_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
