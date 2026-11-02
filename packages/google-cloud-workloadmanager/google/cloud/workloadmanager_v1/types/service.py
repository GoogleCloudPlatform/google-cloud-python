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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.workloadmanager.v1",
    manifest={
        "Evaluation",
        "ResourceFilter",
        "GceInstanceFilter",
        "ResourceStatus",
        "BigQueryDestination",
        "ListEvaluationsRequest",
        "ListEvaluationsResponse",
        "GetEvaluationRequest",
        "CreateEvaluationRequest",
        "UpdateEvaluationRequest",
        "DeleteEvaluationRequest",
        "Execution",
        "RuleExecutionResult",
        "ListExecutionsRequest",
        "ListExecutionsResponse",
        "GetExecutionRequest",
        "RunEvaluationRequest",
        "DeleteExecutionRequest",
        "ListExecutionResultsRequest",
        "ListExecutionResultsResponse",
        "ExecutionResult",
        "Command",
        "AgentCommand",
        "ShellCommand",
        "RuleOutput",
        "ViolationDetails",
        "Resource",
        "OperationMetadata",
        "Rule",
        "ListRulesRequest",
        "ListRulesResponse",
        "ListScannedResourcesRequest",
        "ListScannedResourcesResponse",
        "ScannedResource",
    },
)


class Evaluation(proto.Message):
    r"""Represents a Workload Manager Evaluation configuration.
    An Evaluation defines a set of rules to be validated against a
    scope of Cloud resources.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Name of resource that has the form
            ``projects/{project_id}/locations/{location_id}/evaluations/{evaluation_id}``.
        description (str):
            Description of the Evaluation.
        resource_filter (google.cloud.workloadmanager_v1.types.ResourceFilter):
            Resource filter for an evaluation defining
            the scope of resources to be evaluated.
        rule_names (MutableSequence[str]):
            The names of the rules used for this
            evaluation.
        resource_status (google.cloud.workloadmanager_v1.types.ResourceStatus):
            Output only. [Output only] The current lifecycle state of
            the evaluation resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        schedule (str):
            Crontab format schedule for scheduled evaluation, currently
            only supports the following fixed schedules:

            - ``0 */1 * * *`` # Hourly
            - ``0 */6 * * *`` # Every 6 hours
            - ``0 */12 * * *`` # Every 12 hours
            - ``0 0 */1 * *`` # Daily
            - ``0 0 */7 * *`` # Weekly
            - ``0 0 */14 * *`` # Every 14 days
            - ``0 0 1 */1 *`` # Monthly

            This field is a member of `oneof`_ ``_schedule``.
        custom_rules_bucket (str):
            The Cloud Storage bucket name for custom
            rules.
        evaluation_type (google.cloud.workloadmanager_v1.types.Evaluation.EvaluationType):
            Evaluation type.
        big_query_destination (google.cloud.workloadmanager_v1.types.BigQueryDestination):
            Optional. The BigQuery destination for
            detailed evaluation results. If this field is
            specified, the results of each evaluation
            execution are exported to BigQuery.
        kms_key (str):
            Optional. Immutable. Customer-managed encryption key name,
            in the format
            projects/*/locations/*/keyRings/*/cryptoKeys/*. The key will
            be used for CMEK encryption of the evaluation resource.
    """

    class EvaluationType(proto.Enum):
        r"""Possible types of workload evaluations like SAP, SQL Server,
        etc.

        Values:
            EVALUATION_TYPE_UNSPECIFIED (0):
                Not specified.
            SAP (1):
                SAP best practices.
            SQL_SERVER (2):
                SQL best practices.
            OTHER (3):
                Customized best practices.
        """

        EVALUATION_TYPE_UNSPECIFIED = 0
        SAP = 1
        SQL_SERVER = 2
        OTHER = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_filter: "ResourceFilter" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ResourceFilter",
    )
    rule_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    resource_status: "ResourceStatus" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ResourceStatus",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    schedule: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    custom_rules_bucket: str = proto.Field(
        proto.STRING,
        number=11,
    )
    evaluation_type: EvaluationType = proto.Field(
        proto.ENUM,
        number=12,
        enum=EvaluationType,
    )
    big_query_destination: "BigQueryDestination" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="BigQueryDestination",
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=15,
    )


class ResourceFilter(proto.Message):
    r"""Resource filter for an evaluation defining the scope of
    resources to be evaluated.

    Attributes:
        scopes (MutableSequence[str]):
            The scopes of evaluation resource. Format:

            - ``projects/{project_id}``
            - ``folders/{folder_id}``
            - ``organizations/{organization_id}``
        resource_id_patterns (MutableSequence[str]):
            The pattern to filter resources by their id For example, a
            pattern of ".\ *prod-cluster.*" will match all resources
            that contain "prod-cluster" in their ID.
        inclusion_labels (MutableMapping[str, str]):
            Labels to filter resources by. Each key-value pair in the
            map must exist on the resource for it to be included (e.g.
            VM instance labels). For example, specifying
            ``{ "env": "prod", "database": "nosql" }`` will only include
            resources that have labels ``env=prod`` and
            ``database=nosql``.
        gce_instance_filter (google.cloud.workloadmanager_v1.types.GceInstanceFilter):
            Filter compute engine resources.
    """

    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    resource_id_patterns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    inclusion_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    gce_instance_filter: "GceInstanceFilter" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="GceInstanceFilter",
    )


class GceInstanceFilter(proto.Message):
    r"""A filter for matching Compute Engine instances.

    Attributes:
        service_accounts (MutableSequence[str]):
            If non-empty, only Compute Engine instances
            associated with at least one of the provided
            service accounts will be included in the
            evaluation.
    """

    service_accounts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class ResourceStatus(proto.Message):
    r"""The lifecycle status of an Evaluation resource.

    Attributes:
        state (google.cloud.workloadmanager_v1.types.ResourceStatus.State):
            State of the Evaluation resource.
    """

    class State(proto.Enum):
        r"""Possible states of an evaluation, such as CREATING, ACTIVE,
        and DELETING.

        Values:
            STATE_UNSPECIFIED (0):
                The state has not been populated in this
                message.
            CREATING (1):
                Resource has an active Create operation.
            ACTIVE (2):
                Resource has no outstanding operations on it
                or has active Update operations.
            DELETING (3):
                Resource has an active Delete operation.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3

    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )


class BigQueryDestination(proto.Message):
    r"""BigQuery destination for evaluation results.

    Attributes:
        destination_dataset (str):
            Optional. Destination dataset to save
            evaluation results.
        create_new_results_table (bool):
            Optional. Determines if a new results table
            will be created when an Execution is created.
    """

    destination_dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_new_results_table: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListEvaluationsRequest(proto.Message):
    r"""Request message for the ListEvaluations RPC.

    Attributes:
        parent (str):
            Required. Parent value for
            ListEvaluationsRequest.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filter to be applied when listing the
            evaluation results.
        order_by (str):
            Hint for how to order the results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListEvaluationsResponse(proto.Message):
    r"""Response message for the ListEvaluations RPC.

    Attributes:
        evaluations (MutableSequence[google.cloud.workloadmanager_v1.types.Evaluation]):
            The list of evaluations.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    evaluations: MutableSequence["Evaluation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Evaluation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEvaluationRequest(proto.Message):
    r"""Request message for the GetEvaluation RPC.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEvaluationRequest(proto.Message):
    r"""Request message for the CreateEvaluation RPC.

    Attributes:
        parent (str):
            Required. The resource prefix of the evaluation location
            using the form:
            ``projects/{project_id}/locations/{location_id}``.
        evaluation_id (str):
            Required. Id of the requesting object.
        evaluation (google.cloud.workloadmanager_v1.types.Evaluation):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    evaluation_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    evaluation: "Evaluation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Evaluation",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateEvaluationRequest(proto.Message):
    r"""Request message for the UpdateEvaluation RPC.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Evaluation resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.
        evaluation (google.cloud.workloadmanager_v1.types.Evaluation):
            Required. The resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    evaluation: "Evaluation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Evaluation",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteEvaluationRequest(proto.Message):
    r"""Request message for the DeleteEvaluation RPC.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. Followed the best practice from
            https://aip.dev/135#cascading-delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class Execution(proto.Message):
    r"""Execution that represents a single run of an Evaluation.

    Attributes:
        name (str):
            The name of execution resource. The format is
            projects/{project}/locations/{location}/evaluations/{evaluation}/executions/{execution}.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Start time stamp.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] End time stamp.
        inventory_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Inventory time stamp.
        state (google.cloud.workloadmanager_v1.types.Execution.State):
            Output only. [Output only] State.
        evaluation_id (str):
            Output only. [Output only] Evaluation ID.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        run_type (google.cloud.workloadmanager_v1.types.Execution.Type):
            Type which represents whether the execution executed
            directly by user or scheduled according to the
            ``Evaluation.schedule`` field.
        rule_results (MutableSequence[google.cloud.workloadmanager_v1.types.RuleExecutionResult]):
            Output only. Execution result summary per
            rule.
        external_data_sources (MutableSequence[google.cloud.workloadmanager_v1.types.Execution.ExternalDataSources]):
            Optional. External data sources.
        notices (MutableSequence[google.cloud.workloadmanager_v1.types.Execution.Notice]):
            Output only. Additional information generated
            by the execution.
        engine (google.cloud.workloadmanager_v1.types.Execution.Engine):
            Optional. Engine.
        result_summary (google.cloud.workloadmanager_v1.types.Execution.Summary):
            Output only. [Output only] Result summary for the execution.
    """

    class State(proto.Enum):
        r"""The possible states of an execution like RUNNING, SUCCEEDED,
        FAILED, etc.

        Values:
            STATE_UNSPECIFIED (0):
                State of execution is unspecified.
            RUNNING (1):
                The execution is running in backend service.
            SUCCEEDED (2):
                The execution run succeeded.
            FAILED (3):
                The execution run failed.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        FAILED = 3

    class Type(proto.Enum):
        r"""The type of execution, could be on demand execute or
        scheduled execute.

        Values:
            TYPE_UNSPECIFIED (0):
                Type of execution is unspecified.
            ONE_TIME (1):
                Type of execution is one time.
            SCHEDULED (2):
                Type of execution is scheduled.
        """

        TYPE_UNSPECIFIED = 0
        ONE_TIME = 1
        SCHEDULED = 2

    class Engine(proto.Enum):
        r"""The engine used for the execution.

        Values:
            ENGINE_UNSPECIFIED (0):
                The original CG.
            ENGINE_SCANNER (1):
                SlimCG / Scanner.
            V2 (2):
                Evaluation Engine V2.
        """

        ENGINE_UNSPECIFIED = 0
        ENGINE_SCANNER = 1
        V2 = 2

    class ExternalDataSources(proto.Message):
        r"""External data sources for an execution.

        Attributes:
            name (str):
                Optional. Name of external data source. The
                name will be used inside the rego/sql to refer
                the external data.
            uri (str):
                Required. URI of external data source. example of bq table
                {project_ID}.{dataset_ID}.{table_ID}.
            type_ (google.cloud.workloadmanager_v1.types.Execution.ExternalDataSources.Type):
                Required. Type of external data source.
            asset_type (str):
                Required. The asset type of the external data
                source. This can be a supported Cloud Asset
                Inventory asset type (see
                https://cloud.google.com/asset-inventory/docs/supported-asset-types)
                to override the default asset type, or it can be
                a custom type defined by the user.
        """

        class Type(proto.Enum):
            r"""Possible types of external data sources like BigQuery table,
            etc.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unknown type.
                BIG_QUERY_TABLE (1):
                    BigQuery table.
            """

            TYPE_UNSPECIFIED = 0
            BIG_QUERY_TABLE = 1

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        uri: str = proto.Field(
            proto.STRING,
            number=2,
        )
        type_: "Execution.ExternalDataSources.Type" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Execution.ExternalDataSources.Type",
        )
        asset_type: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class Notice(proto.Message):
        r"""Additional information generated by an execution.

        Attributes:
            message (str):
                Output only. Message of the notice.
        """

        message: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Summary(proto.Message):
        r"""Execution summary.

        Attributes:
            failures (int):
                Output only. Number of failures.
            new_failures (int):
                Output only. Number of new failures compared
                to the previous execution.
            new_fixes (int):
                Output only. Number of new fixes compared to
                the previous execution.
        """

        failures: int = proto.Field(
            proto.INT64,
            number=1,
        )
        new_failures: int = proto.Field(
            proto.INT64,
            number=2,
        )
        new_fixes: int = proto.Field(
            proto.INT64,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
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
    inventory_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    evaluation_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    run_type: Type = proto.Field(
        proto.ENUM,
        number=8,
        enum=Type,
    )
    rule_results: MutableSequence["RuleExecutionResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="RuleExecutionResult",
    )
    external_data_sources: MutableSequence[ExternalDataSources] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=ExternalDataSources,
    )
    notices: MutableSequence[Notice] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=Notice,
    )
    engine: Engine = proto.Field(
        proto.ENUM,
        number=12,
        enum=Engine,
    )
    result_summary: Summary = proto.Field(
        proto.MESSAGE,
        number=13,
        message=Summary,
    )


class RuleExecutionResult(proto.Message):
    r"""Execution result summary per rule.

    Attributes:
        rule (str):
            Rule name as plain text like ``sap-hana-configured``.
        state (google.cloud.workloadmanager_v1.types.RuleExecutionResult.State):
            Output only. The execution status.
        message (str):
            Execution message, if any.
        result_count (int):
            Number of violations.
        scanned_resource_count (int):
            Number of total scanned resources.
    """

    class State(proto.Enum):
        r"""Possible states of a rule execution like SUCCESS, FAILURE,
        etc.

        Values:
            STATE_UNSPECIFIED (0):
                Unknown state
            STATE_SUCCESS (1):
                Execution completed successfully
            STATE_FAILURE (2):
                Execution completed with failures
            STATE_SKIPPED (3):
                Execution was not executed
        """

        STATE_UNSPECIFIED = 0
        STATE_SUCCESS = 1
        STATE_FAILURE = 2
        STATE_SKIPPED = 3

    rule: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    result_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    scanned_resource_count: int = proto.Field(
        proto.INT64,
        number=5,
    )


class ListExecutionsRequest(proto.Message):
    r"""Request message for the ListExecutions RPC.

    Attributes:
        parent (str):
            Required. The resource prefix of the Execution using the
            form:
            ``projects/{project}/locations/{location}/evaluations/{evaluation}``.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListExecutionsResponse(proto.Message):
    r"""Response message for the ListExecutions RPC.

    Attributes:
        executions (MutableSequence[google.cloud.workloadmanager_v1.types.Execution]):
            The list of Execution.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    executions: MutableSequence["Execution"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Execution",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetExecutionRequest(proto.Message):
    r"""Request message for the GetExecution RPC.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunEvaluationRequest(proto.Message):
    r"""Request message for the RunEvaluation RPC.

    Attributes:
        name (str):
            Required. The resource name of the Evaluation using the
            form:
            ``projects/{project}/locations/{location}/evaluations/{evaluation}``.
        execution_id (str):
            Required. ID of the execution which will be
            created.
        execution (google.cloud.workloadmanager_v1.types.Execution):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    execution_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    execution: "Execution" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Execution",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteExecutionRequest(proto.Message):
    r"""Request message for the DeleteExecution RPC.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListExecutionResultsRequest(proto.Message):
    r"""Request message for the ListExecutionResults RPC.

    Attributes:
        parent (str):
            Required. The execution results. Format:
            {parent}/evaluations/*/executions/*/results.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListExecutionResultsResponse(proto.Message):
    r"""Response message for the ListExecutionResults RPC.

    Attributes:
        execution_results (MutableSequence[google.cloud.workloadmanager_v1.types.ExecutionResult]):
            The versions from the specified publisher.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    execution_results: MutableSequence["ExecutionResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ExecutionResult",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExecutionResult(proto.Message):
    r"""The result of an execution.

    Attributes:
        violation_message (str):
            The violation message of an execution.
        severity (str):
            The severity of violation.
        rule (str):
            The rule that is violated in an evaluation.
        documentation_url (str):
            The URL for the documentation of the rule.
        resource (google.cloud.workloadmanager_v1.types.Resource):
            The resource that violates the rule.
        violation_details (google.cloud.workloadmanager_v1.types.ViolationDetails):
            The details of violation in an evaluation
            result.
        commands (MutableSequence[google.cloud.workloadmanager_v1.types.Command]):
            The commands to remediate the violation.
        type_ (google.cloud.workloadmanager_v1.types.ExecutionResult.Type):
            Execution result type of the scanned
            resource.
    """

    class Type(proto.Enum):
        r"""Enum of execution result type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unknown state.
            TYPE_PASSED (1):
                Resource successfully passed the rule.
            TYPE_VIOLATED (2):
                Resource violated the rule.
        """

        TYPE_UNSPECIFIED = 0
        TYPE_PASSED = 1
        TYPE_VIOLATED = 2

    violation_message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    severity: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rule: str = proto.Field(
        proto.STRING,
        number=3,
    )
    documentation_url: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resource: "Resource" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Resource",
    )
    violation_details: "ViolationDetails" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ViolationDetails",
    )
    commands: MutableSequence["Command"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="Command",
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=8,
        enum=Type,
    )


class Command(proto.Message):
    r"""Command specifies the type of command to execute.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        agent_command (google.cloud.workloadmanager_v1.types.AgentCommand):
            AgentCommand specifies a one-time executable
            program for the agent to run.

            This field is a member of `oneof`_ ``command_type``.
        shell_command (google.cloud.workloadmanager_v1.types.ShellCommand):
            ShellCommand is invoked via the agent's
            command line executor.

            This field is a member of `oneof`_ ``command_type``.
    """

    agent_command: "AgentCommand" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="command_type",
        message="AgentCommand",
    )
    shell_command: "ShellCommand" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="command_type",
        message="ShellCommand",
    )


class AgentCommand(proto.Message):
    r"""An AgentCommand specifies a one-time executable program for
    the agent to run.

    Attributes:
        command (str):
            The name of the agent one-time executable
            that will be invoked.
        parameters (MutableMapping[str, str]):
            A map of key/value pairs that can be used to
            specify additional one-time executable settings.
    """

    command: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class ShellCommand(proto.Message):
    r"""A ShellCommand is invoked via the agent's command line
    executor.

    Attributes:
        command (str):
            The name of the command to be executed.
        args (str):
            Arguments to be passed to the command.
        timeout_seconds (int):
            Optional. If not specified, the default
            timeout is 60 seconds.
    """

    command: str = proto.Field(
        proto.STRING,
        number=1,
    )
    args: str = proto.Field(
        proto.STRING,
        number=2,
    )
    timeout_seconds: int = proto.Field(
        proto.INT32,
        number=3,
    )


class RuleOutput(proto.Message):
    r"""The rule output of the violation.

    Attributes:
        details (MutableMapping[str, str]):
            Output only. Violation details generated by
            rule.
        message (str):
            Output only. The message generated by rule.
    """

    details: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ViolationDetails(proto.Message):
    r"""The violation in an evaluation result.

    Attributes:
        asset (str):
            The name of the asset.
        service_account (str):
            The service account associated with the
            resource.
        observed (MutableMapping[str, str]):
            Details of the violation.
        rule_output (MutableSequence[google.cloud.workloadmanager_v1.types.RuleOutput]):
            Output only. The rule output of the
            violation.
    """

    asset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    observed: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    rule_output: MutableSequence["RuleOutput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="RuleOutput",
    )


class Resource(proto.Message):
    r"""Resource in execution result.

    Attributes:
        type_ (str):
            The type of resource.
        name (str):
            The name of the resource.
        service_account (str):
            The service account associated with the
            resource.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Rule(proto.Message):
    r"""A rule to be evaluated.

    Attributes:
        name (str):
            Rule name.
        revision_id (str):
            Output only. The version of the rule.
        display_name (str):
            The name display in UI.
        description (str):
            Describe rule in plain language.
        severity (str):
            The severity of the rule.
        primary_category (str):
            The primary category.
        secondary_category (str):
            The secondary category.
        error_message (str):
            The message template for rule.
        uri (str):
            The document url for the rule.
        remediation (str):
            The remediation for the rule.
        tags (MutableSequence[str]):
            List of user-defined tags.
        rule_type (google.cloud.workloadmanager_v1.types.Rule.RuleType):
            The type of the rule.
        asset_type (str):
            The CAI asset type of the rule is evaluating,
            for joined asset types, it will be the
            corresponding primary asset types.
    """

    class RuleType(proto.Enum):
        r"""The type of the rule.

        Values:
            RULE_TYPE_UNSPECIFIED (0):
                Not specified.
            BASELINE (1):
                Baseline rules.
            CUSTOM (2):
                Custom rules.
        """

        RULE_TYPE_UNSPECIFIED = 0
        BASELINE = 1
        CUSTOM = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    severity: str = proto.Field(
        proto.STRING,
        number=5,
    )
    primary_category: str = proto.Field(
        proto.STRING,
        number=6,
    )
    secondary_category: str = proto.Field(
        proto.STRING,
        number=7,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=8,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    remediation: str = proto.Field(
        proto.STRING,
        number=10,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    rule_type: RuleType = proto.Field(
        proto.ENUM,
        number=12,
        enum=RuleType,
    )
    asset_type: str = proto.Field(
        proto.STRING,
        number=13,
    )


class ListRulesRequest(proto.Message):
    r"""Request message for the ListRules RPC.

    Attributes:
        parent (str):
            Required. The [project] on which to execute the request. The
            format is: projects/{project_id}/locations/{location}
            Currently, the pre-defined rules are global available to all
            projects and all regions.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filter based on primary_category, secondary_category.
        custom_rules_bucket (str):
            The Cloud Storage bucket name for custom
            rules.
        evaluation_type (google.cloud.workloadmanager_v1.types.Evaluation.EvaluationType):
            Optional. The evaluation type of the rules
            will be applied to. The Cloud Storage bucket
            name for custom rules.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    custom_rules_bucket: str = proto.Field(
        proto.STRING,
        number=5,
    )
    evaluation_type: "Evaluation.EvaluationType" = proto.Field(
        proto.ENUM,
        number=6,
        enum="Evaluation.EvaluationType",
    )


class ListRulesResponse(proto.Message):
    r"""Response message for the ListRules RPC.

    Attributes:
        rules (MutableSequence[google.cloud.workloadmanager_v1.types.Rule]):
            All rules in response.
    """

    rules: MutableSequence["Rule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Rule",
    )


class ListScannedResourcesRequest(proto.Message):
    r"""Request message for the ListScannedResources RPC.

    Attributes:
        parent (str):
            Required. Parent for
            ListScannedResourcesRequest.
        rule (str):
            Rule name.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Field to sort by. See
            https://google.aip.dev/132#ordering for more
            details.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListScannedResourcesResponse(proto.Message):
    r"""Response message for the ListScannedResources RPC.

    Attributes:
        scanned_resources (MutableSequence[google.cloud.workloadmanager_v1.types.ScannedResource]):
            All scanned resources in response.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    scanned_resources: MutableSequence["ScannedResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ScannedResource",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ScannedResource(proto.Message):
    r"""A scanned resource.

    Attributes:
        resource (str):
            Resource name.
        type_ (str):
            Resource type.
    """

    resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
