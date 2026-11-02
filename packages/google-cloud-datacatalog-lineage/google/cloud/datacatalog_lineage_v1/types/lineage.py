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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.lineage.v1",
    manifest={
        "DependencyType",
        "Process",
        "Run",
        "LineageEvent",
        "EventLink",
        "DependencyInfo",
        "EntityReference",
        "OperationMetadata",
        "ProcessOpenLineageRunEventRequest",
        "ProcessOpenLineageRunEventResponse",
        "CreateProcessRequest",
        "UpdateProcessRequest",
        "GetProcessRequest",
        "ListProcessesRequest",
        "ListProcessesResponse",
        "DeleteProcessRequest",
        "CreateRunRequest",
        "UpdateRunRequest",
        "GetRunRequest",
        "ListRunsRequest",
        "ListRunsResponse",
        "DeleteRunRequest",
        "CreateLineageEventRequest",
        "GetLineageEventRequest",
        "ListLineageEventsRequest",
        "ListLineageEventsResponse",
        "DeleteLineageEventRequest",
        "SearchLinksRequest",
        "MultipleEntityReference",
        "SearchLinksResponse",
        "Link",
        "BatchSearchLinkProcessesRequest",
        "BatchSearchLinkProcessesResponse",
        "ProcessLinks",
        "ProcessLinkInfo",
        "Origin",
        "LineageLink",
        "SearchLineageStreamingRequest",
        "SearchLineageStreamingResponse",
    },
)


class DependencyType(proto.Enum):
    r"""Type of dependency between entities.

    Values:
        DEPENDENCY_TYPE_UNSPECIFIED (0):
            Dependency type unspecified.
        EXACT_COPY (1):
            Exact data copy without any change.
        OTHER (3):
            Other types of dependencies like filtering or
            grouping.
    """

    DEPENDENCY_TYPE_UNSPECIFIED = 0
    EXACT_COPY = 1
    OTHER = 3


class Process(proto.Message):
    r"""A process is the definition of a data transformation
    operation.

    Attributes:
        name (str):
            Immutable. The resource name of the lineage process. Format:
            ``projects/{project}/locations/{location}/processes/{process}``.
            Can be specified or auto-assigned. {process} must be not
            longer than 200 characters and only contain characters in a
            set: ``a-zA-Z0-9_-:.``
        display_name (str):
            Optional. A human-readable name you can set to display in a
            user interface. Must be not longer than 200 characters and
            only contain UTF-8 letters or numbers, spaces or characters
            like ``_-:&.``
        attributes (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Optional. The attributes of the process.
            Should only be used for the purpose of
            non-semantic management (classifying, describing
            or labeling the process).

            Up to 100 attributes are allowed.
        origin (google.cloud.datacatalog_lineage_v1.types.Origin):
            Optional. The origin of this process and its
            runs and lineage events.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    attributes: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Value,
    )
    origin: "Origin" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Origin",
    )


class Run(proto.Message):
    r"""A lineage run represents an execution of a process that
    creates lineage events.

    Attributes:
        name (str):
            Immutable. The resource name of the run. Format:
            ``projects/{project}/locations/{location}/processes/{process}/runs/{run}``.
            Can be specified or auto-assigned. {run} must be not longer
            than 200 characters and only contain characters in a set:
            ``a-zA-Z0-9_-:.``
        display_name (str):
            Optional. A human-readable name you can set to display in a
            user interface. Must be not longer than 200 characters and
            only contain UTF-8 letters or numbers, spaces or characters
            like ``_-:&.``
        attributes (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Optional. The attributes of the run. Should
            only be used for the purpose of non-semantic
            management (classifying, describing or labeling
            the run).

            Up to 100 attributes are allowed.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp of the start of the
            run.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The timestamp of the end of the
            run.
        state (google.cloud.datacatalog_lineage_v1.types.Run.State):
            Required. The state of the run.
    """

    class State(proto.Enum):
        r"""The current state of the run.

        Values:
            UNKNOWN (0):
                The state is unknown. The true state may be
                any of the below or a different state that is
                not supported here explicitly.
            STARTED (1):
                The run is still executing.
            COMPLETED (2):
                The run completed.
            FAILED (3):
                The run failed.
            ABORTED (4):
                The run aborted.
        """

        UNKNOWN = 0
        STARTED = 1
        COMPLETED = 2
        FAILED = 3
        ABORTED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    attributes: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Value,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )


class LineageEvent(proto.Message):
    r"""A lineage event represents an operation on assets. Within the
    operation, the data flows from the source to the target defined
    in the links field.

    Attributes:
        name (str):
            Immutable. The resource name of the lineage event. Format:
            ``projects/{project}/locations/{location}/processes/{process}/runs/{run}/lineageEvents/{lineage_event}``.
            Can be specified or auto-assigned. {lineage_event} must be
            not longer than 200 characters and only contain characters
            in a set: ``a-zA-Z0-9_-:.``
        links (MutableSequence[google.cloud.datacatalog_lineage_v1.types.EventLink]):
            Optional. List of source-target pairs. Can't
            contain more than 100 tuples.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The beginning of the transformation
            which resulted in this lineage event. For
            streaming scenarios, it should be the beginning
            of the period from which the lineage is being
            reported.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The end of the transformation which
            resulted in this lineage event.  For streaming
            scenarios, it should be the end of the period
            from which the lineage is being reported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    links: MutableSequence["EventLink"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="EventLink",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class EventLink(proto.Message):
    r"""A lineage between source and target entities.

    Attributes:
        source (google.cloud.datacatalog_lineage_v1.types.EntityReference):
            Required. Reference to the source entity
        target (google.cloud.datacatalog_lineage_v1.types.EntityReference):
            Required. Reference to the target entity
        dependency_info (google.cloud.datacatalog_lineage_v1.types.DependencyInfo):
            Optional. Describes how the target depends on
            the source.
    """

    source: "EntityReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EntityReference",
    )
    target: "EntityReference" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EntityReference",
    )
    dependency_info: "DependencyInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DependencyInfo",
    )


class DependencyInfo(proto.Message):
    r"""Dependency info describes how one entity depends on another.

    Attributes:
        dependency_type (google.cloud.datacatalog_lineage_v1.types.DependencyType):
            Required. Type of dependency.
    """

    dependency_type: "DependencyType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DependencyType",
    )


class EntityReference(proto.Message):
    r"""The soft reference to everything you can attach a lineage
    event to.

    Attributes:
        fully_qualified_name (str):
            Required. `Fully Qualified Name
            (FQN) <https://cloud.google.com/dataplex/docs/fully-qualified-names>`__
            of the entity.
        field (MutableSequence[str]):
            Optional. Field path within the entity. Each nesting level
            should be a separate value in the repeated field. The order
            matters. Must be empty for asset level lineage

            For example to address "salary.net" subfield where "salary"
            is a column and "net" is a proto field two values in the
            ``field`` should be reported, the first is "salary" and the
            second is "net".

            Each field length is limited to 500 characters. Maximum
            supported nesting level is 20.
    """

    fully_qualified_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    field: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class OperationMetadata(proto.Message):
    r"""Metadata describing the operation.

    Attributes:
        state (google.cloud.datacatalog_lineage_v1.types.OperationMetadata.State):
            Output only. The current operation state.
        operation_type (google.cloud.datacatalog_lineage_v1.types.OperationMetadata.Type):
            Output only. The type of the operation being
            performed.
        resource (str):
            Output only. The [relative name]
            (https://cloud.google.com//apis/design/resource_names#relative_resource_name)
            of the resource being operated on.
        resource_uuid (str):
            Output only. The UUID of the resource being
            operated on.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of the operation
            submission to the server.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of the operation
            termination, regardless of its success. This
            field is unset if the operation is still
            ongoing.
    """

    class State(proto.Enum):
        r"""An enum with the state of the operation.

        Values:
            STATE_UNSPECIFIED (0):
                Unused.
            PENDING (1):
                The operation has been created but is not yet
                started.
            RUNNING (2):
                The operation is underway.
            SUCCEEDED (3):
                The operation completed successfully.
            FAILED (4):
                The operation is no longer running and did
                not succeed.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        RUNNING = 2
        SUCCEEDED = 3
        FAILED = 4

    class Type(proto.Enum):
        r"""Type of the long running operation.

        Values:
            TYPE_UNSPECIFIED (0):
                Unused.
            DELETE (1):
                The resource deletion operation.
            CREATE (2):
                The resource creation operation.
        """

        TYPE_UNSPECIFIED = 0
        DELETE = 1
        CREATE = 2

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    operation_type: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    resource_uuid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class ProcessOpenLineageRunEventRequest(proto.Message):
    r"""Request message for
    [ProcessOpenLineageRunEvent][google.cloud.datacatalog.lineage.v1.Lineage.ProcessOpenLineageRunEvent].

    Attributes:
        parent (str):
            Required. The name of the project and its
            location that should own the process, run, and
            lineage event.
        open_lineage (google.protobuf.struct_pb2.Struct):
            Required. OpenLineage message following
            OpenLineage format:
            https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json
        request_id (str):
            Optional. A unique identifier for this request. Restricted
            to 36 ASCII characters. A random UUID is recommended. This
            request is idempotent only if a ``request_id`` is provided.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    open_lineage: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ProcessOpenLineageRunEventResponse(proto.Message):
    r"""Response message for
    [ProcessOpenLineageRunEvent][google.cloud.datacatalog.lineage.v1.Lineage.ProcessOpenLineageRunEvent].

    Attributes:
        process (str):
            Created process name. Format:
            ``projects/{project}/locations/{location}/processes/{process}``.
        run (str):
            Created run name. Format:
            ``projects/{project}/locations/{location}/processes/{process}/runs/{run}``.
        lineage_events (MutableSequence[str]):
            Created lineage event names. Format:
            ``projects/{project}/locations/{location}/processes/{process}/runs/{run}/lineageEvents/{lineage_event}``.
    """

    process: str = proto.Field(
        proto.STRING,
        number=1,
    )
    run: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lineage_events: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateProcessRequest(proto.Message):
    r"""Request message for
    [CreateProcess][google.cloud.datacatalog.lineage.v1.Lineage.CreateProcess].

    Attributes:
        parent (str):
            Required. The name of the project and its
            location that should own the process.
        process (google.cloud.datacatalog_lineage_v1.types.Process):
            Required. The process to create.
        request_id (str):
            Optional. A unique identifier for this request. Restricted
            to 36 ASCII characters. A random UUID is recommended. This
            request is idempotent only if a ``request_id`` is provided.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    process: "Process" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Process",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateProcessRequest(proto.Message):
    r"""Request message for
    [UpdateProcess][google.cloud.datacatalog.lineage.v1.Lineage.UpdateProcess].

    Attributes:
        process (google.cloud.datacatalog_lineage_v1.types.Process):
            Required. The lineage process to update.

            The process's ``name`` field is used to identify the process
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
            Currently not used. The whole message is
            updated.
        allow_missing (bool):
            Optional. If set to true and the process is
            not found, the request inserts it.
        request_id (str):
            Optional. A unique identifier for this request. Restricted
            to 36 ASCII characters. A random UUID is recommended. This
            request is idempotent only if a ``request_id`` is provided.
    """

    process: "Process" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Process",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetProcessRequest(proto.Message):
    r"""Request message for
    [GetProcess][google.cloud.datacatalog.lineage.v1.Lineage.GetProcess].

    Attributes:
        name (str):
            Required. The name of the process to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListProcessesRequest(proto.Message):
    r"""Request message for
    [ListProcesses][google.cloud.datacatalog.lineage.v1.Lineage.ListProcesses].

    Attributes:
        parent (str):
            Required. The name of the project and its
            location that owns this collection of processes.
        page_size (int):
            Optional. The maximum number of processes to
            return. The service may return fewer than this
            value. If unspecified, at most 50 processes are
            returned. The maximum value is 100; values
            greater than 100 are cut to 100.
        page_token (str):
            Optional. The page token received from a previous
            ``ListProcesses`` call. Specify it to get the next page.

            When paginating, all other parameters specified in this call
            must match the parameters of the call that provided the page
            token.
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


class ListProcessesResponse(proto.Message):
    r"""Response message for
    [ListProcesses][google.cloud.datacatalog.lineage.v1.Lineage.ListProcesses].

    Attributes:
        processes (MutableSequence[google.cloud.datacatalog_lineage_v1.types.Process]):
            The processes from the specified project and
            location.
        next_page_token (str):
            The token to specify as ``page_token`` in the next call to
            get the next page. If this field is omitted, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    processes: MutableSequence["Process"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Process",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteProcessRequest(proto.Message):
    r"""Request message for
    [DeleteProcess][google.cloud.datacatalog.lineage.v1.Lineage.DeleteProcess].

    Attributes:
        name (str):
            Required. The name of the process to delete.
        allow_missing (bool):
            Optional. If set to true and the process is
            not found, the request succeeds but the server
            doesn't perform any actions.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateRunRequest(proto.Message):
    r"""Request message for
    [CreateRun][google.cloud.datacatalog.lineage.v1.Lineage.CreateRun].

    Attributes:
        parent (str):
            Required. The name of the process that should
            own the run.
        run (google.cloud.datacatalog_lineage_v1.types.Run):
            Required. The run to create.
        request_id (str):
            Optional. A unique identifier for this request. Restricted
            to 36 ASCII characters. A random UUID is recommended. This
            request is idempotent only if a ``request_id`` is provided.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    run: "Run" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Run",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateRunRequest(proto.Message):
    r"""Request message for
    [UpdateRun][google.cloud.datacatalog.lineage.v1.Lineage.UpdateRun].

    Attributes:
        run (google.cloud.datacatalog_lineage_v1.types.Run):
            Required. The lineage run to update.

            The run's ``name`` field is used to identify the run to
            update.

            Format:
            ``projects/{project}/locations/{location}/processes/{process}/runs/{run}``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
            Currently not used. The whole message is
            updated.
        allow_missing (bool):
            Optional. If set to true and the run is not
            found, the request creates it.
    """

    run: "Run" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Run",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetRunRequest(proto.Message):
    r"""Request message for
    [GetRun][google.cloud.datacatalog.lineage.v1.Lineage.GetRun].

    Attributes:
        name (str):
            Required. The name of the run to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRunsRequest(proto.Message):
    r"""Request message for
    [ListRuns][google.cloud.datacatalog.lineage.v1.Lineage.ListRuns].

    Attributes:
        parent (str):
            Required. The name of process that owns this
            collection of runs.
        page_size (int):
            Optional. The maximum number of runs to
            return. The service may return fewer than this
            value. If unspecified, at most 50 runs are
            returned. The maximum value is 100; values
            greater than 100 are cut to 100.
        page_token (str):
            Optional. The page token received from a previous
            ``ListRuns`` call. Specify it to get the next page.

            When paginating, all other parameters specified in this call
            must match the parameters of the call that provided the page
            token.
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


class ListRunsResponse(proto.Message):
    r"""Response message for
    [ListRuns][google.cloud.datacatalog.lineage.v1.Lineage.ListRuns].

    Attributes:
        runs (MutableSequence[google.cloud.datacatalog_lineage_v1.types.Run]):
            The runs from the specified project and
            location.
        next_page_token (str):
            The token to specify as ``page_token`` in the next call to
            get the next page. If this field is omitted, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    runs: MutableSequence["Run"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Run",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteRunRequest(proto.Message):
    r"""Request message for
    [DeleteRun][google.cloud.datacatalog.lineage.v1.Lineage.DeleteRun].

    Attributes:
        name (str):
            Required. The name of the run to delete.
        allow_missing (bool):
            Optional. If set to true and the run is not
            found, the request succeeds but the server
            doesn't perform any actions.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateLineageEventRequest(proto.Message):
    r"""Request message for
    [CreateLineageEvent][google.cloud.datacatalog.lineage.v1.Lineage.CreateLineageEvent].

    Attributes:
        parent (str):
            Required. The name of the run that should own
            the lineage event.
        lineage_event (google.cloud.datacatalog_lineage_v1.types.LineageEvent):
            Required. The lineage event to create.
        request_id (str):
            Optional. A unique identifier for this request. Restricted
            to 36 ASCII characters. A random UUID is recommended. This
            request is idempotent only if a ``request_id`` is provided.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lineage_event: "LineageEvent" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LineageEvent",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetLineageEventRequest(proto.Message):
    r"""Request message for
    [GetLineageEvent][google.cloud.datacatalog.lineage.v1.Lineage.GetLineageEvent].

    Attributes:
        name (str):
            Required. The name of the lineage event to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLineageEventsRequest(proto.Message):
    r"""Request message for
    [ListLineageEvents][google.cloud.datacatalog.lineage.v1.Lineage.ListLineageEvents].

    Attributes:
        parent (str):
            Required. The name of the run that owns the
            collection of lineage events to get.
        page_size (int):
            Optional. The maximum number of lineage
            events to return.
            The service may return fewer events than this
            value. If unspecified, at most 50 events are
            returned. The maximum value is 100; values
            greater than 100 are cut to 100.
        page_token (str):
            Optional. The page token received from a previous
            ``ListLineageEvents`` call. Specify it to get the next page.

            When paginating, all other parameters specified in this call
            must match the parameters of the call that provided the page
            token.
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


class ListLineageEventsResponse(proto.Message):
    r"""Response message for
    [ListLineageEvents][google.cloud.datacatalog.lineage.v1.Lineage.ListLineageEvents].

    Attributes:
        lineage_events (MutableSequence[google.cloud.datacatalog_lineage_v1.types.LineageEvent]):
            Lineage events from the specified project and
            location.
        next_page_token (str):
            The token to specify as ``page_token`` in the next call to
            get the next page. If this field is omitted, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    lineage_events: MutableSequence["LineageEvent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LineageEvent",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteLineageEventRequest(proto.Message):
    r"""Request message for
    [DeleteLineageEvent][google.cloud.datacatalog.lineage.v1.Lineage.DeleteLineageEvent].

    Attributes:
        name (str):
            Required. The name of the lineage event to
            delete.
        allow_missing (bool):
            Optional. If set to true and the lineage
            event is not found, the request succeeds but the
            server doesn't perform any actions.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class SearchLinksRequest(proto.Message):
    r"""Request message for
    [SearchLinks][google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The project and location you want
            search in.
        source (google.cloud.datacatalog_lineage_v1.types.EntityReference):
            Optional. Send asset information in the **source** field to
            retrieve all links that lead from the specified asset to
            downstream assets.

            This field is a member of `oneof`_ ``criteria``.
        target (google.cloud.datacatalog_lineage_v1.types.EntityReference):
            Optional. Send asset information in the **target** field to
            retrieve all links that lead from upstream assets to the
            specified asset.

            This field is a member of `oneof`_ ``criteria``.
        sources (google.cloud.datacatalog_lineage_v1.types.MultipleEntityReference):
            Optional. Send a list of asset information in the
            **sources** field to retrieve all links that lead from the
            specified assets to downstream assets. This field is similar
            to the ``source``
            [source][google.cloud.datacatalog.lineage.v1.SearchLinksRequest.source]
            field but allows providing multiple entities. All entities
            within the ``MultipleEntityReference`` must have the same
            ``fully_qualified_name``.

            This field is a member of `oneof`_ ``criteria``.
        targets (google.cloud.datacatalog_lineage_v1.types.MultipleEntityReference):
            Optional. Send a list of asset information in the
            **targets** field to retrieve all links that lead from
            upstream assets to the specified assets. This field is
            similar to the ``target``
            [target][google.cloud.datacatalog.lineage.v1.SearchLinksRequest.target]
            field but allows providing multiple entities. All entities
            within the ``MultipleEntityReference`` must have the same
            ``fully_qualified_name``.

            This field is a member of `oneof`_ ``criteria``.
        page_size (int):
            Optional. The maximum number of links to
            return in a single page of the response. A page
            may contain fewer links than this value. If
            unspecified, at most 10 links are returned.

            Maximum value is 100; values greater than 100
            are reduced to 100.
        page_token (str):
            Optional. The page token received from a previous
            ``SearchLinksRequest`` call. Use it to get the next page.

            When requesting subsequent pages of a response, remember
            that all parameters must match the values you provided in
            the original request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: "EntityReference" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="criteria",
        message="EntityReference",
    )
    target: "EntityReference" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="criteria",
        message="EntityReference",
    )
    sources: "MultipleEntityReference" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="criteria",
        message="MultipleEntityReference",
    )
    targets: "MultipleEntityReference" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="criteria",
        message="MultipleEntityReference",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MultipleEntityReference(proto.Message):
    r"""Multiple entity reference for SearchLinksRequest.

    Attributes:
        entities (MutableSequence[google.cloud.datacatalog_lineage_v1.types.EntityReference]):
            Optional. The list of entities to search for
            links. The maximum number of entities is 20.
    """

    entities: MutableSequence["EntityReference"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EntityReference",
    )


class SearchLinksResponse(proto.Message):
    r"""Response message for
    [SearchLinks][google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks].

    Attributes:
        links (MutableSequence[google.cloud.datacatalog_lineage_v1.types.Link]):
            The list of links for a given asset. Can be
            empty if the asset has no relations of requested
            type (source or target).
        next_page_token (str):
            The token to specify as ``page_token`` in the subsequent
            call to get the next page. Omitted if there are no more
            pages in the response.
    """

    @property
    def raw_page(self):
        return self

    links: MutableSequence["Link"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Link",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Link(proto.Message):
    r"""Links represent the data flow between **source** (upstream) and
    **target** (downstream) assets in transformation pipelines.

    Links are created when LineageEvents record data transformation
    between related assets.

    Attributes:
        name (str):
            Output only. Immutable. The name of the link. Format:
            ``projects/{project}/locations/{location}/links/{link}``.
        source (google.cloud.datacatalog_lineage_v1.types.EntityReference):
            The pointer to the entity that is the **source** of this
            link.
        target (google.cloud.datacatalog_lineage_v1.types.EntityReference):
            The pointer to the entity that is the **target** of this
            link.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start of the first event establishing
            this link.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The end of the last event establishing this
            link.
        dependency_info (MutableSequence[google.cloud.datacatalog_lineage_v1.types.Link.DependencyInfo]):
            Optional. The dependency info of the link
            (applies only to column level links).
    """

    class DependencyInfo(proto.Message):
        r"""Dependency info describes how one entity depends on another.

        Attributes:
            dependency_type (google.cloud.datacatalog_lineage_v1.types.DependencyType):
                The type of dependency.
        """

        dependency_type: "DependencyType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DependencyType",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: "EntityReference" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EntityReference",
    )
    target: "EntityReference" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EntityReference",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    dependency_info: MutableSequence[DependencyInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=DependencyInfo,
    )


class BatchSearchLinkProcessesRequest(proto.Message):
    r"""Request message for
    [BatchSearchLinkProcesses][google.cloud.datacatalog.lineage.v1.Lineage.BatchSearchLinkProcesses].

    Attributes:
        parent (str):
            Required. The project and location where you
            want to search.
        links (MutableSequence[str]):
            Required. An array of links to check for their associated
            LineageProcesses.

            The maximum number of items in this array is 100. If the
            request contains more than 100 links, it returns the
            ``INVALID_ARGUMENT`` error.

            Format:
            ``projects/{project}/locations/{location}/links/{link}``.
        page_size (int):
            Optional. The maximum number of processes to
            return in a single page of the response. A page
            may contain fewer results than this value.
        page_token (str):
            Optional. The page token received from a previous
            ``BatchSearchLinkProcesses`` call. Use it to get the next
            page.

            When requesting subsequent pages of a response, remember
            that all parameters must match the values you provided in
            the original request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    links: MutableSequence[str] = proto.RepeatedField(
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


class BatchSearchLinkProcessesResponse(proto.Message):
    r"""Response message for
    [BatchSearchLinkProcesses][google.cloud.datacatalog.lineage.v1.Lineage.BatchSearchLinkProcesses].

    Attributes:
        process_links (MutableSequence[google.cloud.datacatalog_lineage_v1.types.ProcessLinks]):
            An array of processes associated with the
            specified links.
        next_page_token (str):
            The token to specify as ``page_token`` in the subsequent
            call to get the next page. Omitted if there are no more
            pages in the response.
    """

    @property
    def raw_page(self):
        return self

    process_links: MutableSequence["ProcessLinks"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ProcessLinks",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ProcessLinks(proto.Message):
    r"""Links associated with a specific process.

    Attributes:
        process (str):
            The process name in the format of
            ``projects/{project}/locations/{location}/processes/{process}``.
        links (MutableSequence[google.cloud.datacatalog_lineage_v1.types.ProcessLinkInfo]):
            An array containing link details objects of
            the links provided in the original request.

            A single process can result in creating multiple
            links. If any of the links you provide in the
            request are created by the same process, they
            all are included in this array.
    """

    process: str = proto.Field(
        proto.STRING,
        number=1,
    )
    links: MutableSequence["ProcessLinkInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ProcessLinkInfo",
    )


class ProcessLinkInfo(proto.Message):
    r"""Link details.

    Attributes:
        link (str):
            The name of the link in the format of
            ``projects/{project}/locations/{location}/links/{link}``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start of the first event establishing
            this link-process tuple.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The end of the last event establishing this
            link-process tuple.
    """

    link: str = proto.Field(
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


class Origin(proto.Message):
    r"""Origin of a process.

    Attributes:
        source_type (google.cloud.datacatalog_lineage_v1.types.Origin.SourceType):
            Type of the source.

            Use of a source_type other than ``CUSTOM`` for process
            creation or updating is highly discouraged. It might be
            restricted in the future without notice. There will be
            increase in cost if you use any of the source types other
            than ``CUSTOM``.
        name (str):
            If the source_type isn't CUSTOM, the value of this field
            should be a Google Cloud resource name of the system, which
            reports lineage. The project and location parts of the
            resource name must match the project and location of the
            lineage resource being created. Examples:

            - ``{source_type: COMPOSER, name: "projects/foo/locations/us/environments/bar"}``
            - ``{source_type: BIGQUERY, name: "projects/foo/locations/eu"}``
            - ``{source_type: CUSTOM,   name: "myCustomIntegration"}``
    """

    class SourceType(proto.Enum):
        r"""Type of the source of a process.

        Values:
            SOURCE_TYPE_UNSPECIFIED (0):
                Source is Unspecified
            CUSTOM (1):
                A custom source
            BIGQUERY (2):
                BigQuery
            DATA_FUSION (3):
                Data Fusion
            COMPOSER (4):
                Composer
            LOOKER_STUDIO (5):
                Looker Studio
            DATAPROC (6):
                Dataproc
            VERTEX_AI (7):
                Vertex AI
            DATAFLOW (8):
                Dataflow
            LOOKER_CORE (9):
                Looker Core
        """

        SOURCE_TYPE_UNSPECIFIED = 0
        CUSTOM = 1
        BIGQUERY = 2
        DATA_FUSION = 3
        COMPOSER = 4
        LOOKER_STUDIO = 5
        DATAPROC = 6
        VERTEX_AI = 7
        DATAFLOW = 8
        LOOKER_CORE = 9

    source_type: SourceType = proto.Field(
        proto.ENUM,
        number=1,
        enum=SourceType,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LineageLink(proto.Message):
    r"""Lineage link between two entities.

    Attributes:
        source (google.cloud.datacatalog_lineage_v1.types.EntityReference):
            The entity that is the **source** of this link.
        target (google.cloud.datacatalog_lineage_v1.types.EntityReference):
            The entity that is the **target** of this link.
        processes (MutableSequence[google.cloud.datacatalog_lineage_v1.types.LineageLink.LineageProcess]):
            Processes metadata associated with the link.
        dependency_info (MutableSequence[google.cloud.datacatalog_lineage_v1.types.LineageLink.DependencyInfo]):
            Describes how the target entity is dependent
            on the source entity.
        depth (int):
            Depth of the current link in the graph
            starting from 1.
        location (str):
            The location where the LineageEvent that
            created the link is stored.
    """

    class LineageProcess(proto.Message):
        r"""Process metadata for the link.

        Attributes:
            process (google.cloud.datacatalog_lineage_v1.types.Process):
                Process that created the link.
        """

        process: "Process" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Process",
        )

    class DependencyInfo(proto.Message):
        r"""Dependency info describes how one entity is dependent on
        another.

        Attributes:
            dependency_type (google.cloud.datacatalog_lineage_v1.types.DependencyType):
                The type of dependency.
        """

        dependency_type: "DependencyType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DependencyType",
        )

    source: "EntityReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EntityReference",
    )
    target: "EntityReference" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EntityReference",
    )
    processes: MutableSequence[LineageProcess] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=LineageProcess,
    )
    dependency_info: MutableSequence[DependencyInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=DependencyInfo,
    )
    depth: int = proto.Field(
        proto.INT32,
        number=5,
    )
    location: str = proto.Field(
        proto.STRING,
        number=7,
    )


class SearchLineageStreamingRequest(proto.Message):
    r"""Request message for
    [SearchLineageStreaming][google.cloud.datacatalog.lineage.v1.Lineage.SearchLineageStreaming].

    Attributes:
        parent (str):
            Required. The project and location to
            initiate the search from.
        locations (MutableSequence[str]):
            Required. The locations to search in.
        root_criteria (google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest.RootCriteria):
            Required. Criteria for the root of the
            search.
        direction (google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest.SearchDirection):
            Required. Direction of the search.
        filters (google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest.SearchFilters):
            Optional. Filters for the search.
        limits (google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest.SearchLimits):
            Optional. Limits for the search.
    """

    class SearchDirection(proto.Enum):
        r"""Direction of the search.

        Values:
            SEARCH_DIRECTION_UNSPECIFIED (0):
                Direction is unspecified.
            DOWNSTREAM (1):
                Retrieve links that lead from the specified
                asset to downstream assets.
            UPSTREAM (2):
                Retrieve links that lead from upstream assets
                to the specified asset.
        """

        SEARCH_DIRECTION_UNSPECIFIED = 0
        DOWNSTREAM = 1
        UPSTREAM = 2

    class EntitySet(proto.Enum):
        r"""Entity set restriction.

        Values:
            ENTITY_SET_UNSPECIFIED (0):
                The entity set is unspecified. Returns all
                the data.
            ENTITIES (1):
                Returns entities with only FQN specified. For example,
                entities with the ``field`` field set are not returned.
        """

        ENTITY_SET_UNSPECIFIED = 0
        ENTITIES = 1

    class SearchFilters(proto.Message):
        r"""Filters for the search.

        Attributes:
            dependency_types (MutableSequence[google.cloud.datacatalog_lineage_v1.types.DependencyType]):
                Optional. Types of dependencies between
                entities to retrieve. If unspecified, all
                dependency types are returned.
            entity_set (google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest.EntitySet):
                Optional. Entity set restriction. If
                unspecified, the method returns all entities.
            time_range (google.type.interval_pb2.Interval):
                Optional. Time interval to search for lineage. If
                unspecified, all lineage is returned. Currently, at most one
                of ``start_time`` and ``end_time`` can be set.
        """

        dependency_types: MutableSequence["DependencyType"] = proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum="DependencyType",
        )
        entity_set: "SearchLineageStreamingRequest.EntitySet" = proto.Field(
            proto.ENUM,
            number=2,
            enum="SearchLineageStreamingRequest.EntitySet",
        )
        time_range: interval_pb2.Interval = proto.Field(
            proto.MESSAGE,
            number=3,
            message=interval_pb2.Interval,
        )

    class SearchLimits(proto.Message):
        r"""Limits for the search results.

        Attributes:
            max_depth (int):
                Optional. The maximum depth of the search.
                The default value is 5 and maximum value is 100.
            max_results (int):
                Optional. The maximum number of links to return in the
                response. The default value is 1_000 and the maximum value
                is 10_000.
            max_process_per_link (int):
                Optional. The maximum number of processes to return per
                link. The default value is 0 and the maximum value is 100.
                If this value is non-zero, the response will contain process
                names for the links. To retrieve full process details in the
                response, include ``links.processes.process`` in the
                `FieldMask <https://developers.google.com/workspace/docs/api/how-tos/field-masks#read_with_a_field_mask>`__.
        """

        max_depth: int = proto.Field(
            proto.INT32,
            number=1,
        )
        max_results: int = proto.Field(
            proto.INT32,
            number=2,
        )
        max_process_per_link: int = proto.Field(
            proto.INT32,
            number=3,
        )

    class RootCriteria(proto.Message):
        r"""Criteria for the root of the search.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            entities (google.cloud.datacatalog_lineage_v1.types.MultipleEntityReference):
                Optional. The entities to initiate the search from. Entities
                can be specified by FQN only, or by FQN and field. To search
                by FQN and all available fields for that FQN, use the
                wildcard ``*`` as the field value.

                This field is a member of `oneof`_ ``criteria``.
        """

        entities: "MultipleEntityReference" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="criteria",
            message="MultipleEntityReference",
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    root_criteria: RootCriteria = proto.Field(
        proto.MESSAGE,
        number=3,
        message=RootCriteria,
    )
    direction: SearchDirection = proto.Field(
        proto.ENUM,
        number=4,
        enum=SearchDirection,
    )
    filters: SearchFilters = proto.Field(
        proto.MESSAGE,
        number=5,
        message=SearchFilters,
    )
    limits: SearchLimits = proto.Field(
        proto.MESSAGE,
        number=6,
        message=SearchLimits,
    )


class SearchLineageStreamingResponse(proto.Message):
    r"""Response message for
    [SearchLineageStreaming][google.cloud.datacatalog.lineage.v1.Lineage.SearchLineageStreaming].

    Attributes:
        links (MutableSequence[google.cloud.datacatalog_lineage_v1.types.LineageLink]):
            Output only. The lineage links that match the
            search criteria. Can be empty if no links match.
        unreachable (MutableSequence[str]):
            Unordered list. Unreachable resources. If non-empty, the
            result set might be incomplete.

            Currently, only locations are supported.

            Format: ``projects/[PROJECT_NUMBER]/locations/[LOCATION]``
            Example: projects/123456789/locations/us-east1
    """

    links: MutableSequence["LineageLink"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LineageLink",
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
