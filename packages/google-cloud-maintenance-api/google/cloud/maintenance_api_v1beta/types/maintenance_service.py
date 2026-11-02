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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.maintenance.api.v1beta",
    manifest={
        "MaintenanceCategory",
        "SummarizeMaintenancesRequest",
        "SummarizeMaintenancesResponse",
        "MaintenanceSummary",
        "ResourceMaintenance",
        "MaintenanceControl",
        "ListResourceMaintenancesRequest",
        "ListResourceMaintenancesResponse",
        "GetResourceMaintenanceRequest",
    },
)


class MaintenanceCategory(proto.Enum):
    r"""The Category of the maintenance.

    Values:
        MAINTENANCE_CATEGORY_UNSPECIFIED (0):
            Unspecified category.
        INFRASTRUCTURE (1):
            Infrastructure maintenance events are times
            that Google Cloud performs regular maintenance
            on network equipment e.g. Google Cloud
            Interconnect These events are usually scheduled
            in advance and we provide notification, when
            possible, so that users can plan for the
            infrastructure maintenance event and prevent
            downtime. Infrastructure maintenance events
            don't have a set interval between occurrences,
            but generally occur several times a year.
        SERVICE_UPDATE (3):
            Updates that can include bug fixes, changes,
            or new features that are backward compatible
            with existing versions (including patches). Some
            SPs allow users to control the scheduling of
            these maintenance events using maintenance
            windows and/or deny maintenance features.
    """

    MAINTENANCE_CATEGORY_UNSPECIFIED = 0
    INFRASTRUCTURE = 1
    SERVICE_UPDATE = 3


class SummarizeMaintenancesRequest(proto.Message):
    r"""Request message for SummarizeMaintenances custom method.

    Attributes:
        parent (str):
            Required. The parent of the resource maintenance. eg.
            ``projects/123/locations/*``
        page_size (int):
            The maximum number of resource maintenances
            to send per page. The default page size is 20
            and the maximum is 1000.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in https://google.aip.dev/160.
            Supported fields include:

            - state
            - resource.location
            - resource.resourceName
            - resource.type
            - maintenance.maintenanceName
            - maintenanceStartTime
            - maintenanceCompleteTime Examples:
            - state="SCHEDULED"
            - resource.location="us-central1-c"
            - resource.resourceName=~"\*/instance-20241212-211259"
            - maintenanceStartTime>"2000-10-11T20:44:51Z"
            - state="SCHEDULED" OR
              resource.type="compute.googleapis.com/Instance"
            - maintenance.maitenanceName="eb3b709c-9ca1-5472-9fb6-800a3849eda1"
              AND maintenanceCompleteTime>"2000-10-11T20:44:51Z".
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class SummarizeMaintenancesResponse(proto.Message):
    r"""Request message for SummarizeMaintenances custom method.

    Attributes:
        maintenances (MutableSequence[google.cloud.maintenance_api_v1beta.types.MaintenanceSummary]):
            The resulting summaries.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent SummarizeMaintenances
            call to list the next page. If empty, there are
            no more pages.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    maintenances: MutableSequence["MaintenanceSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10509,
        message="MaintenanceSummary",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class MaintenanceSummary(proto.Message):
    r"""MaintenanceSummary contains maintenance statistics calculated
    based on ResourceMaintenances within the scope: project and
    location.

    Attributes:
        maintenance_name (str):
            Output only. The name of the maintenance.
        title (str):
            Output only. The title of the maintenance.
        description (str):
            Output only. The description of the
            maintenance.
        category (google.cloud.maintenance_api_v1beta.types.MaintenanceCategory):
            Output only. The category of the maintenance
            event.
        maintenance_scheduled_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Scheduled start time of the maintenance. The
            maintenance will start at ``maintenanceScheduledStartTime``
            or later, with best effort to finish before
            ``maintenanceScheduledEndTime``.
        maintenance_scheduled_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. An estimated (best effort, not
            guaranteed) end time of the scheduled
            maintenance.
        maintenance_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Actual date when the maintenance started. Field
            present only after the state changed to ``RUNNING``.
        maintenance_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Actual date when the maintenance successfully
            completed. Field present only after the state changed to
            ``SUCCEEDED``.
        user_controllable (bool):
            Output only. Indicates whether the user has
            some control over that maintenance, either
            proactively before maintenance was scheduled
            with maintenance policy or with reactive
            controls after it was scheduled (see controls
            field).
        controls (MutableSequence[google.cloud.maintenance_api_v1beta.types.MaintenanceControl]):
            Output only. Control available for that
            Maintenance (might not be available for every
            resource that maintenance is applied to).
        stats (MutableSequence[google.cloud.maintenance_api_v1beta.types.MaintenanceSummary.Stats]):
            Output only. Stats is a field of
            ResourceMaintenance used to aggregate the stats.
    """

    class Stats(proto.Message):
        r"""Stats indicates the type of aggregate and the corresponding
        aggregates.

        Attributes:
            group_by (str):
                groupBy specifies the type of aggregate. For example a
                group_by might be ``"state"``
            aggregates (MutableSequence[google.cloud.maintenance_api_v1beta.types.MaintenanceSummary.Aggregate]):
                Aggregates is a list <group, count> pairs. For example, if
                the group_by is ``"state"`` a possible tuple in the
                aggregates list could be "SCHEDULED" : ``11``,
        """

        group_by: str = proto.Field(
            proto.STRING,
            number=1,
        )
        aggregates: MutableSequence["MaintenanceSummary.Aggregate"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="MaintenanceSummary.Aggregate",
            )
        )

    class Aggregate(proto.Message):
        r"""Aggregate is a <group, count> pair.

        Attributes:
            group (str):
                Specifies what specific value of the group_by the count
                represents. For example if group_by is ``"state"`` its
                corresponding group could be ``"SCHEDULED"``.
            count (int):
                The count of the group.
        """

        group: str = proto.Field(
            proto.STRING,
            number=1,
        )
        count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    maintenance_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    category: "MaintenanceCategory" = proto.Field(
        proto.ENUM,
        number=13,
        enum="MaintenanceCategory",
    )
    maintenance_scheduled_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_scheduled_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    user_controllable: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    controls: MutableSequence["MaintenanceControl"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="MaintenanceControl",
    )
    stats: MutableSequence[Stats] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=Stats,
    )


class ResourceMaintenance(proto.Message):
    r"""ResourceMaintenance is a resource that represents a
    maintenance operation on a resource.

    Attributes:
        name (str):
            Identifier. The name of the resource_maintenance resource.
            Format:
            ``"projects/{project}/locations/{location}/resourceMaintenance/{resource-maintenance-id}"``
        resource (google.cloud.maintenance_api_v1beta.types.ResourceMaintenance.Resource):
            Output only. The resource spec of the
            resource maintenance.
        maintenance (google.cloud.maintenance_api_v1beta.types.ResourceMaintenance.Maintenance):
            Output only. The details of the maintenance.
        state (google.cloud.maintenance_api_v1beta.types.ResourceMaintenance.State):
            Output only. The state of the resource
            maintenance.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource
            maintenance.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource
            maintenance.
        maintenance_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the resource
            maintenance has started.
        maintenance_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the resource
            maintenance has completed.
        maintenance_cancel_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the resource
            maintenance was cancelled.
        maintenance_scheduled_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the maintenance on
            the resource was scheduled to start.
        maintenance_scheduled_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the maintenance on
            the resource was scheduled to end.
        user_controllable (bool):
            Output only. Indicates whether the user has
            some control over that maintenance, either
             proactively before maintenance was scheduled
            with maintenance policy or  with reactive
            controls after it was scheduled (see controls
            field)
        controls (MutableSequence[google.cloud.maintenance_api_v1beta.types.MaintenanceControl]):
            Output only. The controls of the maintenance.
        labels (MutableMapping[str, str]):
            Optional. The labels on the resource, which
            can be used for categorization. similar to
            Kubernetes resource labels.
        annotations (MutableMapping[str, str]):
            Optional. Annotations is an unstructured
            key-value map stored with a resource that may be
            set by external tools to store and retrieve
            arbitrary metadata. They are not queryable and
            should be preserved when modifying objects.

            More info:
            https://kubernetes.io/docs/user-guide/annotations
        uid (str):
            Output only. The unique identifier of the
            resource. UID is unique in the time and space
            for this resource within the scope of the
            service. It is typically generated by the server
            on successful creation of a resource and must
            not be changed. UID is used to uniquely identify
            resources with resource name reuses. This should
            be a UUID4.
        etag (str):
            Output only. An opaque value that uniquely
            identifies a version or generation of a
            resource. It can be used to confirm that the
            client and server agree on the ordering of a
            resource being written.
    """

    class State(proto.Enum):
        r"""State is the state of a resource maintenance.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            SCHEDULED (1):
                Scheduled for a particular window. For
                disruptive maintenance it should respect
                maintenance policy, i.e. its available windows,
                exclusions and notification period.
            RUNNING (2):
                Maintenance is ongoing.
            CANCELLED (3):
                No longer planned, typically when other
                maintenance (e.g. upgrade to newer version)
                already happened, or the user skipped the
                maintenance.
            SUCCEEDED (4):
                Successfully completed.
        """

        STATE_UNSPECIFIED = 0
        SCHEDULED = 1
        RUNNING = 2
        CANCELLED = 3
        SUCCEEDED = 4

    class Resource(proto.Message):
        r"""Resource contains information about the resource affected by
        maintenance.

        Attributes:
            resource_name (str):
                Output only. Name is the reference to the
                consumer resource affected by the maintenance.
                Available values can be found here:

                https://cloud.google.com/asset-inventory/docs/asset-names
            location (str):
                Output only. The location of the resource. Format:
                ``us-central1``
            type_ (str):
                Output only. The type of the resource. Available values can
                be found here:
                https://cloud.google.com/asset-inventory/docs/asset-types#supported_resource_types
                Please note that not all the resource types will have their
                maintenances reported.
        """

        resource_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        location: str = proto.Field(
            proto.STRING,
            number=2,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Maintenance(proto.Message):
        r"""Maintenance is the maintenance details of a resource's
        maintenance.

        Attributes:
            maintenance_name (str):
                Maintenance is the name of the corresponding maintenance
                resource following the standard naming scheme:
                ``"{maintenance-id}"``
            title (str):
                Output only. The title of the maintenance.
            description (str):
                Output only. The description of the
                maintenance.
            category (google.cloud.maintenance_api_v1beta.types.MaintenanceCategory):
                Output only. The category of the maintenance.
        """

        maintenance_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        title: str = proto.Field(
            proto.STRING,
            number=2,
        )
        description: str = proto.Field(
            proto.STRING,
            number=3,
        )
        category: "MaintenanceCategory" = proto.Field(
            proto.ENUM,
            number=4,
            enum="MaintenanceCategory",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource: Resource = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Resource,
    )
    maintenance: Maintenance = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Maintenance,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_cancel_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_scheduled_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    maintenance_scheduled_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    user_controllable: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    controls: MutableSequence["MaintenanceControl"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="MaintenanceControl",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10401,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10402,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10201,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10202,
    )


class MaintenanceControl(proto.Message):
    r"""The control of the maintenance.

    Attributes:
        control (google.cloud.maintenance_api_v1beta.types.MaintenanceControl.Control):
            The control of the resource maintenance.
        is_custom (bool):
            Indicates whether the control is available
            only in Service Producer API (not through
            Unified Maintenance).
        documentation (str):
            Link to Service Producer documentation about maintenance
            control. Provided only when ``isCustom`` is ``true``.
    """

    class Control(proto.Enum):
        r"""Sets the type of control supported. comment (as in logs).

        Values:
            CONTROL_UNSPECIFIED (0):
                Unspecified control.
            APPLY (1):
                Apply control.
            MANAGE_POLICY (2):
                Manage policy control.
            RESCHEDULE (3):
                Reschedule control.
        """

        CONTROL_UNSPECIFIED = 0
        APPLY = 1
        MANAGE_POLICY = 2
        RESCHEDULE = 3

    control: Control = proto.Field(
        proto.ENUM,
        number=1,
        enum=Control,
    )
    is_custom: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    documentation: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListResourceMaintenancesRequest(proto.Message):
    r"""The request structure for the ListResourceMaintenances
    method.

    Attributes:
        parent (str):
            Required. The parent of the resource
            maintenance.
        page_size (int):
            The maximum number of resource maintenances
            to send per page.
        page_token (str):
            The page token: If the next_page_token from a previous
            response is provided, this request will send the subsequent
            page.
        filter (str):
            Filter the list as specified in
            https://google.aip.dev/160.
        order_by (str):
            Order results as specified in
            https://google.aip.dev/132.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=10006,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10505,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=10506,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=10507,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10508,
    )


class ListResourceMaintenancesResponse(proto.Message):
    r"""The response structure for the ListResourceMaintenances
    method.

    Attributes:
        resource_maintenances (MutableSequence[google.cloud.maintenance_api_v1beta.types.ResourceMaintenance]):
            The resulting resource maintenances.
        next_page_token (str):
            If present, the next page token can be
            provided to a subsequent
            ListResourceMaintenances call to list the next
            page. If empty, there are no more pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    resource_maintenances: MutableSequence["ResourceMaintenance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10509,
        message="ResourceMaintenance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=10510,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10511,
    )


class GetResourceMaintenanceRequest(proto.Message):
    r"""The request structure for the GetResourceMaintenance method.

    Attributes:
        name (str):
            Required. The resource name of the resource
            within a service.
    """

    name: str = proto.Field(
        proto.STRING,
        number=10001,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
