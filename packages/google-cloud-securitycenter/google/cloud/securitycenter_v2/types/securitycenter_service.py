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
import proto  # type: ignore

from google.cloud.securitycenter_v2.types import (
    attack_path,
    bigquery_export,
    valued_resource,
)
from google.cloud.securitycenter_v2.types import external_system as gcs_external_system
from google.cloud.securitycenter_v2.types import finding as gcs_finding
from google.cloud.securitycenter_v2.types import mute_config as gcs_mute_config
from google.cloud.securitycenter_v2.types import (
    notification_config as gcs_notification_config,
)
from google.cloud.securitycenter_v2.types import resource as gcs_resource
from google.cloud.securitycenter_v2.types import (
    resource_value_config as gcs_resource_value_config,
)
from google.cloud.securitycenter_v2.types import security_marks as gcs_security_marks
from google.cloud.securitycenter_v2.types import source as gcs_source

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v2",
    manifest={
        "BatchCreateResourceValueConfigsRequest",
        "BatchCreateResourceValueConfigsResponse",
        "BulkMuteFindingsRequest",
        "BulkMuteFindingsResponse",
        "CreateBigQueryExportRequest",
        "CreateFindingRequest",
        "CreateMuteConfigRequest",
        "CreateNotificationConfigRequest",
        "CreateResourceValueConfigRequest",
        "CreateSourceRequest",
        "DeleteBigQueryExportRequest",
        "DeleteMuteConfigRequest",
        "DeleteNotificationConfigRequest",
        "DeleteResourceValueConfigRequest",
        "BigQueryDestination",
        "ExportFindingsMetadata",
        "ExportFindingsResponse",
        "GetBigQueryExportRequest",
        "GetMuteConfigRequest",
        "GetNotificationConfigRequest",
        "GetResourceValueConfigRequest",
        "GetSourceRequest",
        "GroupFindingsRequest",
        "GroupFindingsResponse",
        "GroupResult",
        "ListAttackPathsRequest",
        "ListAttackPathsResponse",
        "GetSimulationRequest",
        "GetValuedResourceRequest",
        "ListBigQueryExportsRequest",
        "ListBigQueryExportsResponse",
        "ListFindingsRequest",
        "ListFindingsResponse",
        "ListMuteConfigsRequest",
        "ListMuteConfigsResponse",
        "ListNotificationConfigsRequest",
        "ListNotificationConfigsResponse",
        "ListResourceValueConfigsRequest",
        "ListResourceValueConfigsResponse",
        "ListSourcesRequest",
        "ListSourcesResponse",
        "ListValuedResourcesRequest",
        "ListValuedResourcesResponse",
        "SetFindingStateRequest",
        "SetMuteRequest",
        "UpdateBigQueryExportRequest",
        "UpdateExternalSystemRequest",
        "UpdateFindingRequest",
        "UpdateMuteConfigRequest",
        "UpdateNotificationConfigRequest",
        "UpdateResourceValueConfigRequest",
        "UpdateSecurityMarksRequest",
        "UpdateSourceRequest",
    },
)


class BatchCreateResourceValueConfigsRequest(proto.Message):
    r"""Request message to create multiple resource value configs

    Attributes:
        parent (str):
            Required. Resource name of the new
            ResourceValueConfig's parent. The parent field
            in the CreateResourceValueConfigRequest messages
            must either be empty or match this field.
        requests (MutableSequence[google.cloud.securitycenter_v2.types.CreateResourceValueConfigRequest]):
            Required. The resource value configs to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateResourceValueConfigRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateResourceValueConfigRequest",
    )


class BatchCreateResourceValueConfigsResponse(proto.Message):
    r"""Response message for BatchCreateResourceValueConfigs

    Attributes:
        resource_value_configs (MutableSequence[google.cloud.securitycenter_v2.types.ResourceValueConfig]):
            The resource value configs created
    """

    resource_value_configs: MutableSequence[
        gcs_resource_value_config.ResourceValueConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_resource_value_config.ResourceValueConfig,
    )


class BulkMuteFindingsRequest(proto.Message):
    r"""Request message for bulk findings update.

    Note:

    1. If multiple bulk update requests match the same resource, the
        order in which they get executed is not defined.
    2. Once a bulk operation is started, there is no way to stop it.

    Attributes:
        parent (str):
            Required. The parent, at which bulk action needs to be
            applied. If no location is specified, findings are updated
            in global. The following list shows some examples:

            - ``organizations/[organization_id]``
            - ``organizations/[organization_id]/locations/[location_id]``
            - ``folders/[folder_id]``
            - ``folders/[folder_id]/locations/[location_id]``
            - ``projects/[project_id]``
            - ``projects/[project_id]/locations/[location_id]``
        filter (str):
            Expression that identifies findings that should be updated.
            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are supported, and ``OR`` has higher precedence
            than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. The fields map to those defined in the
            corresponding resource.

            The supported operators are:

            - ``=`` for all value types.
            - ``>``, ``<``, ``>=``, ``<=`` for integer values.
            - ``:``, meaning substring matching, for strings.

            The supported value types are:

            - string literals in quotes.
            - integer literals without quotes.
            - boolean literals ``true`` and ``false`` without quotes.
        mute_state (google.cloud.securitycenter_v2.types.BulkMuteFindingsRequest.MuteState):
            Optional. All findings matching the given filter will have
            their mute state set to this value. The default value is
            ``MUTED``. Setting this to ``UNDEFINED`` will clear the mute
            state on all matching findings.
    """

    class MuteState(proto.Enum):
        r"""The mute state.

        Values:
            MUTE_STATE_UNSPECIFIED (0):
                Unused.
            MUTED (1):
                Matching findings will be muted (default).
            UNDEFINED (2):
                Matching findings will have their mute state
                cleared.
        """

        MUTE_STATE_UNSPECIFIED = 0
        MUTED = 1
        UNDEFINED = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mute_state: MuteState = proto.Field(
        proto.ENUM,
        number=3,
        enum=MuteState,
    )


class BulkMuteFindingsResponse(proto.Message):
    r"""The response to a BulkMute request. Contains the LRO
    information.

    """


class CreateBigQueryExportRequest(proto.Message):
    r"""Request message for creating a BigQuery export.

    Attributes:
        parent (str):
            Required. The name of the parent resource of the new
            BigQuery export. Its format is
            ``organizations/[organization_id]/locations/[location_id]``,
            ``folders/[folder_id]/locations/[location_id]``, or
            ``projects/[project_id]/locations/[location_id]``.
        big_query_export (google.cloud.securitycenter_v2.types.BigQueryExport):
            Required. The BigQuery export being created.
        big_query_export_id (str):
            Required. Unique identifier provided by the
            client within the parent scope. It must consist
            of only lowercase letters, numbers, and hyphens,
            must start with a letter, must end with either a
            letter or a number, and must be 63 characters or
            less.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    big_query_export: bigquery_export.BigQueryExport = proto.Field(
        proto.MESSAGE,
        number=2,
        message=bigquery_export.BigQueryExport,
    )
    big_query_export_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateFindingRequest(proto.Message):
    r"""Request message for creating a finding.

    Attributes:
        parent (str):
            Required. Resource name of the new finding's parent. The
            following list shows some examples of the format: +
            ``organizations/[organization_id]/sources/[source_id]`` +
            ``organizations/[organization_id]/sources/[source_id]/locations/[location_id]``
        finding_id (str):
            Required. Unique identifier provided by the
            client within the parent scope. It must be
            alphanumeric and less than or equal to 32
            characters and greater than 0 characters in
            length.
        finding (google.cloud.securitycenter_v2.types.Finding):
            Required. The Finding being created. The name and
            security_marks will be ignored as they are both output only
            fields on this resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    finding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    finding: gcs_finding.Finding = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcs_finding.Finding,
    )


class CreateMuteConfigRequest(proto.Message):
    r"""Request message for creating a mute config.

    Attributes:
        parent (str):
            Required. Resource name of the new mute configs's parent.
            Its format is
            ``organizations/[organization_id]/locations/[location_id]``,
            ``folders/[folder_id]/locations/[location_id]``, or
            ``projects/[project_id]/locations/[location_id]``.
        mute_config (google.cloud.securitycenter_v2.types.MuteConfig):
            Required. The mute config being created.
        mute_config_id (str):
            Required. Unique identifier provided by the
            client within the parent scope. It must consist
            of only lowercase letters, numbers, and hyphens,
            must start with a letter, must end with either a
            letter or a number, and must be 63 characters or
            less.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mute_config: gcs_mute_config.MuteConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_mute_config.MuteConfig,
    )
    mute_config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateNotificationConfigRequest(proto.Message):
    r"""Request message for creating a notification config.

    Attributes:
        parent (str):
            Required. Resource name of the new notification config's
            parent. Its format is
            ``organizations/[organization_id]/locations/[location_id]``,
            ``folders/[folder_id]/locations/[location_id]``, or
            ``projects/[project_id]/locations/[location_id]``.
        config_id (str):
            Required.
            Unique identifier provided by the client within
            the parent scope. It must be between 1 and 128
            characters and contain alphanumeric characters,
            underscores, or hyphens only.
        notification_config (google.cloud.securitycenter_v2.types.NotificationConfig):
            Required. The notification config being
            created. The name and the service account will
            be ignored as they are both output only fields
            on this resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    notification_config: gcs_notification_config.NotificationConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcs_notification_config.NotificationConfig,
    )


class CreateResourceValueConfigRequest(proto.Message):
    r"""Request message to create single resource value config

    Attributes:
        parent (str):
            Required. Resource name of the new
            ResourceValueConfig's parent.
        resource_value_config (google.cloud.securitycenter_v2.types.ResourceValueConfig):
            Required. The resource value config being
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_value_config: gcs_resource_value_config.ResourceValueConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_resource_value_config.ResourceValueConfig,
    )


class CreateSourceRequest(proto.Message):
    r"""Request message for creating a source.

    Attributes:
        parent (str):
            Required. Resource name of the new source's parent. Its
            format should be ``organizations/[organization_id]``.
        source (google.cloud.securitycenter_v2.types.Source):
            Required. The Source being created, only the display_name
            and description will be used. All other fields will be
            ignored.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: gcs_source.Source = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_source.Source,
    )


class DeleteBigQueryExportRequest(proto.Message):
    r"""Request message for deleting a BigQuery export.

    Attributes:
        name (str):
            Required. The name of the BigQuery export to delete. The
            following list shows some examples of the format:

            -

            ``organizations/{organization}/locations/{location}/bigQueryExports/{export_id}``

            - ``folders/{folder}/locations/{location}/bigQueryExports/{export_id}``
            - ``projects/{project}/locations/{location}/bigQueryExports/{export_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteMuteConfigRequest(proto.Message):
    r"""Request message for deleting a mute config. If no location is
    specified, default is global.

    Attributes:
        name (str):
            Required. Name of the mute config to delete. The following
            list shows some examples of the format:

            - ``organizations/{organization}/muteConfigs/{config_id}``
            -

            ``organizations/{organization}/locations/{location}/muteConfigs/{config_id}``

            - ``folders/{folder}/muteConfigs/{config_id}``
            - ``folders/{folder}/locations/{location}/muteConfigs/{config_id}``
            - ``projects/{project}/muteConfigs/{config_id}``
            - ``projects/{project}/locations/{location}/muteConfigs/{config_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteNotificationConfigRequest(proto.Message):
    r"""Request message for deleting a notification config.

    Attributes:
        name (str):
            Required. Name of the notification config to delete. The
            following list shows some examples of the format:

            -

            ``organizations/[organization_id]/locations/[location_id]/notificationConfigs/[config_id]``
            +
            ``folders/[folder_id]/locations/[location_id]notificationConfigs/[config_id]``
            +
            ``projects/[project_id]/locations/[location_id]notificationConfigs/[config_id]``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteResourceValueConfigRequest(proto.Message):
    r"""Request message to delete resource value config

    Attributes:
        name (str):
            Required. Name of the ResourceValueConfig to
            delete
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BigQueryDestination(proto.Message):
    r"""The destination big query dataset to export findings to.

    Attributes:
        dataset (str):
            Required. The relative resource name of the
            destination dataset, in the form
            projects/{projectId}/datasets/{datasetId}.
    """

    dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportFindingsMetadata(proto.Message):
    r"""The LRO metadata for a ExportFindings request.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        export_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Timestamp at which export was
            started
        big_query_destination (google.cloud.securitycenter_v2.types.BigQueryDestination):
            Required. The destination big query dataset
            to export findings to.

            This field is a member of `oneof`_ ``destination``.
    """

    export_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    big_query_destination: "BigQueryDestination" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message="BigQueryDestination",
    )


class ExportFindingsResponse(proto.Message):
    r"""The response to a ExportFindings request. Contains the LRO
    information.

    """


class GetBigQueryExportRequest(proto.Message):
    r"""Request message for retrieving a BigQuery export.

    Attributes:
        name (str):
            Required. Name of the BigQuery export to retrieve. The
            following list shows some examples of the format:

            -

            ``organizations/{organization}/locations/{location}/bigQueryExports/{export_id}``

            - ``folders/{folder}/locations/{location}/bigQueryExports/{export_id}``
            - ``projects/{project}locations/{location}//bigQueryExports/{export_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetMuteConfigRequest(proto.Message):
    r"""Request message for retrieving a mute config. If no location
    is specified, default is global.

    Attributes:
        name (str):
            Required. Name of the mute config to retrieve. The following
            list shows some examples of the format:

            - ``organizations/{organization}/muteConfigs/{config_id}``
            -

            ``organizations/{organization}/locations/{location}/muteConfigs/{config_id}``

            - ``folders/{folder}/muteConfigs/{config_id}``
            - ``folders/{folder}/locations/{location}/muteConfigs/{config_id}``
            - ``projects/{project}/muteConfigs/{config_id}``
            - ``projects/{project}/locations/{location}/muteConfigs/{config_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetNotificationConfigRequest(proto.Message):
    r"""Request message for getting a notification config.

    Attributes:
        name (str):
            Required. Name of the notification config to get. The
            following list shows some examples of the format:

            -

            ``organizations/[organization_id]/locations/[location_id]/notificationConfigs/[config_id]``
            +
            ``folders/[folder_id]/locations/[location_id]/notificationConfigs/[config_id]``
            +
            ``projects/[project_id]/locations/[location_id]/notificationConfigs/[config_id]``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetResourceValueConfigRequest(proto.Message):
    r"""Request message to get resource value config

    Attributes:
        name (str):
            Required. Name of the resource value config to retrieve. Its
            format is
            organizations/{organization}/resourceValueConfigs/{config_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSourceRequest(proto.Message):
    r"""Request message for getting a source.

    Attributes:
        name (str):
            Required. Relative resource name of the source. Its format
            is ``organizations/[organization_id]/source/[source_id]``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GroupFindingsRequest(proto.Message):
    r"""Request message for grouping by findings.

    Attributes:
        parent (str):
            Required. Name of the source to groupBy. If no location is
            specified, finding is assumed to be in global. The following
            list shows some examples:

            - ``organizations/[organization_id]/sources/[source_id]``
            -

            ``organizations/[organization_id]/sources/[source_id]/locations/[location_id]``

            - ``folders/[folder_id]/sources/[source_id]``
            - ``folders/[folder_id]/sources/[source_id]/locations/[location_id]``
            - ``projects/[project_id]/sources/[source_id]``
            - ``projects/[project_id]/sources/[source_id]/locations/[location_id]``

            To groupBy across all sources provide a source_id of ``-``.
            The following list shows some examples:

            - ``organizations/{organization_id}/sources/-``
            - ``organizations/{organization_id}/sources/-/locations/[location_id]``
            - ``folders/{folder_id}/sources/-``
            - ``folders/{folder_id}/sources/-/locations/[location_id]``
            - ``projects/{project_id}/sources/-``
            - ``projects/{project_id}/sources/-/locations/[location_id]``
        filter (str):
            Expression that defines the filter to apply across findings.
            The expression is a list of one or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are supported, and ``OR`` has higher precedence
            than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. Examples include:

            - name
            - security_marks.marks.marka

            The supported operators are:

            - ``=`` for all value types.
            - ``>``, ``<``, ``>=``, ``<=`` for integer values.
            - ``:``, meaning substring matching, for strings.

            The supported value types are:

            - string literals in quotes.
            - integer literals without quotes.
            - boolean literals ``true`` and ``false`` without quotes.

            The following field and operator combinations are supported:

            - name: ``=``

            - parent: ``=``, ``:``

            - resource_name: ``=``, ``:``

            - state: ``=``, ``:``

            - category: ``=``, ``:``

            - external_uri: ``=``, ``:``

            - event_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``event_time = "2019-06-10T16:07:18-07:00"``
              ``event_time = 1560208038000``

            - severity: ``=``, ``:``

            - security_marks.marks: ``=``, ``:``

            - resource:

              - resource.name: ``=``, ``:``
              - resource.parent_name: ``=``, ``:``
              - resource.parent_display_name: ``=``, ``:``
              - resource.project_name: ``=``, ``:``
              - resource.project_display_name: ``=``, ``:``
              - resource.type: ``=``, ``:``
        group_by (str):
            Required. Expression that defines what assets fields to use
            for grouping. The string value should follow SQL syntax:
            comma separated list of fields. For example:
            "parent,resource_name".
        page_token (str):
            The value returned by the last ``GroupFindingsResponse``;
            indicates that this is a continuation of a prior
            ``GroupFindings`` call, and that the system should return
            the next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=8,
    )


class GroupFindingsResponse(proto.Message):
    r"""Response message for group by findings.

    Attributes:
        group_by_results (MutableSequence[google.cloud.securitycenter_v2.types.GroupResult]):
            Group results. There exists an element for
            each existing unique combination of
            property/values. The element contains a count
            for the number of times those specific
            property/values appear.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
        total_size (int):
            The total number of results matching the
            query.
    """

    @property
    def raw_page(self):
        return self

    group_by_results: MutableSequence["GroupResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GroupResult",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class GroupResult(proto.Message):
    r"""Result containing the properties and count of a groupBy
    request.

    Attributes:
        properties (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Properties matching the groupBy fields in the
            request.
        count (int):
            Total count of resources for the given
            properties.
    """

    properties: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Value,
    )
    count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class ListAttackPathsRequest(proto.Message):
    r"""Request message for listing the attack paths for a given
    simulation or valued resource.

    Attributes:
        parent (str):
            Required. Name of parent to list attack paths.

            Valid formats: ``organizations/{organization}``,
            ``organizations/{organization}/simulations/{simulation}``
            ``organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}``
            ``organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}``
        filter (str):
            The filter expression that filters the attack path in the
            response. Supported fields:

            - ``valued_resources`` supports =
        page_token (str):
            The value returned by the last ``ListAttackPathsResponse``;
            indicates that this is a continuation of a prior
            ``ListAttackPaths`` call, and that the system should return
            the next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ListAttackPathsResponse(proto.Message):
    r"""Response message for listing the attack paths for a given
    simulation or valued resource.

    Attributes:
        attack_paths (MutableSequence[google.cloud.securitycenter_v2.types.AttackPath]):
            The attack paths that the attack path
            simulation identified.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
    """

    @property
    def raw_page(self):
        return self

    attack_paths: MutableSequence[attack_path.AttackPath] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=attack_path.AttackPath,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSimulationRequest(proto.Message):
    r"""Request message for getting simulation.
    Simulation name can include "latest" to retrieve the latest
    simulation For example, "organizations/123/simulations/latest"

    Attributes:
        name (str):
            Required. The organization name or simulation name of this
            simulation

            Valid format:
            ``organizations/{organization}/simulations/latest``
            ``organizations/{organization}/simulations/{simulation}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetValuedResourceRequest(proto.Message):
    r"""Request message for getting a valued resource.

    Attributes:
        name (str):
            Required. The name of this valued resource

            Valid format:
            ``organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBigQueryExportsRequest(proto.Message):
    r"""Request message for listing BigQuery exports at a given scope
    e.g. organization, folder or project.

    Attributes:
        parent (str):
            Required. The parent, which owns the collection of BigQuery
            exports. Its format is
            ``organizations/[organization_id]/locations/[location_id]``,
            ``folders/[folder_id]/locations/[location_id]``, or
            ``projects/[project_id]/locations/[location_id]``.
        page_size (int):
            The maximum number of configs to return. The
            service may return fewer than this value.
            If unspecified, at most 10 configs will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListBigQueryExports`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListBigQueryExports`` must match the call that
            provided the page token.
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


class ListBigQueryExportsResponse(proto.Message):
    r"""Response message for listing BigQuery exports.

    Attributes:
        big_query_exports (MutableSequence[google.cloud.securitycenter_v2.types.BigQueryExport]):
            The BigQuery exports from the specified
            parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    big_query_exports: MutableSequence[bigquery_export.BigQueryExport] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=bigquery_export.BigQueryExport,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListFindingsRequest(proto.Message):
    r"""Request message for listing findings.

    Attributes:
        parent (str):
            Required. Name of the source the findings belong to. If no
            location is specified, the default is global. The following
            list shows some examples:

            - ``organizations/[organization_id]/sources/[source_id]``
            -

            ``organizations/[organization_id]/sources/[source_id]/locations/[location_id]``

            - ``folders/[folder_id]/sources/[source_id]``
            - ``folders/[folder_id]/sources/[source_id]/locations/[location_id]``
            - ``projects/[project_id]/sources/[source_id]``
            - ``projects/[project_id]/sources/[source_id]/locations/[location_id]``

            To list across all sources provide a source_id of ``-``. The
            following list shows some examples:

            - ``organizations/{organization_id}/sources/-``
            - ``organizations/{organization_id}/sources/-/locations/{location_id}``
            - ``folders/{folder_id}/sources/-``
            - ``folders/{folder_id}/sources/-locations/{location_id}``
            - ``projects/{projects_id}/sources/-``
            - ``projects/{projects_id}/sources/-/locations/{location_id}``
        filter (str):
            Expression that defines the filter to apply across findings.
            The expression is a list of one or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are supported, and ``OR`` has higher precedence
            than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. Examples include:

            - name
            - security_marks.marks.marka

            The supported operators are:

            - ``=`` for all value types.
            - ``>``, ``<``, ``>=``, ``<=`` for integer values.
            - ``:``, meaning substring matching, for strings.

            The supported value types are:

            - string literals in quotes.
            - integer literals without quotes.
            - boolean literals ``true`` and ``false`` without quotes.

            The following field and operator combinations are supported:

            - name: ``=``

            - parent: ``=``, ``:``

            - resource_name: ``=``, ``:``

            - state: ``=``, ``:``

            - category: ``=``, ``:``

            - external_uri: ``=``, ``:``

            - event_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``event_time = "2019-06-10T16:07:18-07:00"``
              ``event_time = 1560208038000``

            - severity: ``=``, ``:``

            - security_marks.marks: ``=``, ``:``

            - resource:

              - resource.name: ``=``, ``:``
              - resource.parent_name: ``=``, ``:``
              - resource.parent_display_name: ``=``, ``:``
              - resource.project_name: ``=``, ``:``
              - resource.project_display_name: ``=``, ``:``
              - resource.type: ``=``, ``:``
              - resource.folders.resource_folder: ``=``, ``:``
              - resource.display_name: ``=``, ``:``
        order_by (str):
            Expression that defines what fields and order to use for
            sorting. The string value should follow SQL syntax: comma
            separated list of fields. For example: "name,parent". The
            default sorting order is ascending. To specify descending
            order for a field, a suffix " desc" should be appended to
            the field name. For example: "name desc,parent". Redundant
            space characters in the syntax are insignificant. "name
            desc,parent" and " name desc , parent " are equivalent.

            The following fields are supported: name parent state
            category resource_name event_time security_marks.marks
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            A field mask to specify the Finding fields to
            be listed in the response. An empty field mask
            will list all fields.
        page_token (str):
            The value returned by the last ``ListFindingsResponse``;
            indicates that this is a continuation of a prior
            ``ListFindings`` call, and that the system should return the
            next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=7,
        message=field_mask_pb2.FieldMask,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=8,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=9,
    )


class ListFindingsResponse(proto.Message):
    r"""Response message for listing findings.

    Attributes:
        list_findings_results (MutableSequence[google.cloud.securitycenter_v2.types.ListFindingsResponse.ListFindingsResult]):
            Findings matching the list request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
        total_size (int):
            The total number of findings matching the
            query.
    """

    class ListFindingsResult(proto.Message):
        r"""Result containing the Finding.

        Attributes:
            finding (google.cloud.securitycenter_v2.types.Finding):
                Finding matching the search request.
            resource (google.cloud.securitycenter_v2.types.ListFindingsResponse.ListFindingsResult.Resource):
                Output only. Resource that is associated with
                this finding.
        """

        class Resource(proto.Message):
            r"""Information related to the Google Cloud resource that is
            associated with this finding.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                name (str):
                    The full resource name of the resource. See:
                    https://cloud.google.com/apis/design/resource_names#full_resource_name
                display_name (str):
                    The human readable name of the resource.
                type_ (str):
                    The full resource type of the resource.
                cloud_provider (google.cloud.securitycenter_v2.types.CloudProvider):
                    Indicates which cloud provider the finding is
                    from.
                service (str):
                    The service or resource provider associated
                    with the resource.
                location (str):
                    The region or location of the service (if
                    applicable).
                gcp_metadata (google.cloud.securitycenter_v2.types.GcpMetadata):
                    The GCP metadata associated with the finding.

                    This field is a member of `oneof`_ ``cloud_provider_metadata``.
                aws_metadata (google.cloud.securitycenter_v2.types.AwsMetadata):
                    The AWS metadata associated with the finding.

                    This field is a member of `oneof`_ ``cloud_provider_metadata``.
                azure_metadata (google.cloud.securitycenter_v2.types.AzureMetadata):
                    The Azure metadata associated with the
                    finding.

                    This field is a member of `oneof`_ ``cloud_provider_metadata``.
                resource_path (google.cloud.securitycenter_v2.types.ResourcePath):
                    Provides the path to the resource within the
                    resource hierarchy.
                resource_path_string (str):
                    A string representation of the resource path. For Google
                    Cloud, it has the format of
                    ``organizations/{organization_id}/folders/{folder_id}/folders/{folder_id}/projects/{project_id}``
                    where there can be any number of folders. For AWS, it has
                    the format of
                    ``org/{organization_id}/ou/{organizational_unit_id}/ou/{organizational_unit_id}/account/{account_id}``
                    where there can be any number of organizational units. For
                    Azure, it has the format of
                    ``mg/{management_group_id}/mg/{management_group_id}/subscription/{subscription_id}/rg/{resource_group_name}``
                    where there can be any number of management groups.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            display_name: str = proto.Field(
                proto.STRING,
                number=2,
            )
            type_: str = proto.Field(
                proto.STRING,
                number=3,
            )
            cloud_provider: gcs_resource.CloudProvider = proto.Field(
                proto.ENUM,
                number=4,
                enum=gcs_resource.CloudProvider,
            )
            service: str = proto.Field(
                proto.STRING,
                number=5,
            )
            location: str = proto.Field(
                proto.STRING,
                number=6,
            )
            gcp_metadata: gcs_resource.GcpMetadata = proto.Field(
                proto.MESSAGE,
                number=7,
                oneof="cloud_provider_metadata",
                message=gcs_resource.GcpMetadata,
            )
            aws_metadata: gcs_resource.AwsMetadata = proto.Field(
                proto.MESSAGE,
                number=8,
                oneof="cloud_provider_metadata",
                message=gcs_resource.AwsMetadata,
            )
            azure_metadata: gcs_resource.AzureMetadata = proto.Field(
                proto.MESSAGE,
                number=9,
                oneof="cloud_provider_metadata",
                message=gcs_resource.AzureMetadata,
            )
            resource_path: gcs_resource.ResourcePath = proto.Field(
                proto.MESSAGE,
                number=10,
                message=gcs_resource.ResourcePath,
            )
            resource_path_string: str = proto.Field(
                proto.STRING,
                number=11,
            )

        finding: gcs_finding.Finding = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcs_finding.Finding,
        )
        resource: "ListFindingsResponse.ListFindingsResult.Resource" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="ListFindingsResponse.ListFindingsResult.Resource",
        )

    @property
    def raw_page(self):
        return self

    list_findings_results: MutableSequence[ListFindingsResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ListFindingsResult,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ListMuteConfigsRequest(proto.Message):
    r"""Request message for listing  mute configs at a given scope
    e.g. organization, folder or project. If no location is
    specified, default is global.

    Attributes:
        parent (str):
            Required. The parent, which owns the collection of mute
            configs. Its format is
            ``organizations/[organization_id]", "folders/[folder_id]``,
            ``projects/[project_id]``,
            ``organizations/[organization_id]/locations/[location_id]``,
            ``folders/[folder_id]/locations/[location_id]``,
            ``projects/[project_id]/locations/[location_id]``.
        page_size (int):
            The maximum number of configs to return. The
            service may return fewer than this value.
            If unspecified, at most 10 configs will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListMuteConfigs``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListMuteConfigs`` must match the call that provided the
            page token.
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


class ListMuteConfigsResponse(proto.Message):
    r"""Response message for listing mute configs.

    Attributes:
        mute_configs (MutableSequence[google.cloud.securitycenter_v2.types.MuteConfig]):
            The mute configs from the specified parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    mute_configs: MutableSequence[gcs_mute_config.MuteConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_mute_config.MuteConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListNotificationConfigsRequest(proto.Message):
    r"""Request message for listing notification configs.

    Attributes:
        parent (str):
            Required. The name of the parent in which to list the
            notification configurations. Its format is
            "organizations/[organization_id]/locations/[location_id]",
            "folders/[folder_id]/locations/[location_id]", or
            "projects/[project_id]/locations/[location_id]".
        page_token (str):
            The value returned by the last
            ``ListNotificationConfigsResponse``; indicates that this is
            a continuation of a prior ``ListNotificationConfigs`` call,
            and that the system should return the next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ListNotificationConfigsResponse(proto.Message):
    r"""Response message for listing notification configs.

    Attributes:
        notification_configs (MutableSequence[google.cloud.securitycenter_v2.types.NotificationConfig]):
            Notification configs belonging to the
            requested parent.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
    """

    @property
    def raw_page(self):
        return self

    notification_configs: MutableSequence[
        gcs_notification_config.NotificationConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_notification_config.NotificationConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListResourceValueConfigsRequest(proto.Message):
    r"""Request message to list resource value configs of a parent

    Attributes:
        parent (str):
            Required. The parent, which owns the collection of resource
            value configs. Its format is
            ``organizations/[organization_id]``
        page_size (int):
            The maximum number of configs to return. The
            service may return fewer than this value.
            If unspecified, at most 10 configs will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListResourceValueConfigs`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListResourceValueConfigs`` must match the call that
            provided the page token.

            page_size can be specified, and the new page_size will be
            used.
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


class ListResourceValueConfigsResponse(proto.Message):
    r"""Response message to list resource value configs

    Attributes:
        resource_value_configs (MutableSequence[google.cloud.securitycenter_v2.types.ResourceValueConfig]):
            The resource value configs from the specified
            parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is empty, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    resource_value_configs: MutableSequence[
        gcs_resource_value_config.ResourceValueConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_resource_value_config.ResourceValueConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSourcesRequest(proto.Message):
    r"""Request message for listing sources.

    Attributes:
        parent (str):
            Required. Resource name of the parent of sources to list.
            Its format should be ``organizations/[organization_id]``,
            ``folders/[folder_id]``, or ``projects/[project_id]``.
        page_token (str):
            The value returned by the last ``ListSourcesResponse``;
            indicates that this is a continuation of a prior
            ``ListSources`` call, and that the system should return the
            next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=7,
    )


class ListSourcesResponse(proto.Message):
    r"""Response message for listing sources.

    Attributes:
        sources (MutableSequence[google.cloud.securitycenter_v2.types.Source]):
            Sources belonging to the requested parent.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
    """

    @property
    def raw_page(self):
        return self

    sources: MutableSequence[gcs_source.Source] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_source.Source,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListValuedResourcesRequest(proto.Message):
    r"""Request message for listing the valued resources for a given
    simulation.

    Attributes:
        parent (str):
            Required. Name of parent to list exposed resources.

            Valid formats: ``organizations/{organization}``,
            ``organizations/{organization}/simulations/{simulation}``
            ``organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}``
        filter (str):
            The filter expression that filters the valued resources in
            the response. Supported fields:

            - ``resource_value`` supports =
            - ``resource_type`` supports =
        page_token (str):
            The value returned by the last
            ``ListValuedResourcesResponse``; indicates that this is a
            continuation of a prior ``ListValuedResources`` call, and
            that the system should return the next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
        order_by (str):
            Optional. The fields by which to order the valued resources
            response.

            Supported fields:

            - ``exposed_score``

            - ``resource_value``

            - ``resource_type``

            Values should be a comma separated list of fields. For
            example: ``exposed_score,resource_value``.

            The default sorting order is descending. To specify
            ascending or descending order for a field, append a " ASC"
            or a " DESC" suffix, respectively; for example:
            ``exposed_score DESC``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListValuedResourcesResponse(proto.Message):
    r"""Response message for listing the valued resources for a given
    simulation.

    Attributes:
        valued_resources (MutableSequence[google.cloud.securitycenter_v2.types.ValuedResource]):
            The valued resources that the attack path
            simulation identified.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
        total_size (int):
            The estimated total number of results
            matching the query.
    """

    @property
    def raw_page(self):
        return self

    valued_resources: MutableSequence[valued_resource.ValuedResource] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=valued_resource.ValuedResource,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class SetFindingStateRequest(proto.Message):
    r"""Request message for updating a finding's state.

    Attributes:
        name (str):
            Required. The `relative resource
            name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__
            of the finding. If no location is specified, finding is
            assumed to be in global. The following list shows some
            examples:

            -

            ``organizations/{organization_id}/sources/{source_id}/findings/{finding_id}``
            +
            ``organizations/{organization_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}``

            - ``folders/{folder_id}/sources/{source_id}/findings/{finding_id}``
            -

            ``folders/{folder_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}``

            - ``projects/{project_id}/sources/{source_id}/findings/{finding_id}``
            -

            ``projects/{project_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}``
        state (google.cloud.securitycenter_v2.types.Finding.State):
            Required. The desired State of the finding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: gcs_finding.Finding.State = proto.Field(
        proto.ENUM,
        number=2,
        enum=gcs_finding.Finding.State,
    )


class SetMuteRequest(proto.Message):
    r"""Request message for updating a finding's mute status.

    Attributes:
        name (str):
            Required. The `relative resource
            name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__
            of the finding. If no location is specified, finding is
            assumed to be in global. The following list shows some
            examples:

            -

            ``organizations/{organization_id}/sources/{source_id}/findings/{finding_id}``
            +
            ``organizations/{organization_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}``

            - ``folders/{folder_id}/sources/{source_id}/findings/{finding_id}``
            -

            ``folders/{folder_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}``

            - ``projects/{project_id}/sources/{source_id}/findings/{finding_id}``
            -

            ``projects/{project_id}/sources/{source_id}/locations/{location_id}/findings/{finding_id}``
        mute (google.cloud.securitycenter_v2.types.Finding.Mute):
            Required. The desired state of the Mute.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mute: gcs_finding.Finding.Mute = proto.Field(
        proto.ENUM,
        number=2,
        enum=gcs_finding.Finding.Mute,
    )


class UpdateBigQueryExportRequest(proto.Message):
    r"""Request message for updating a BigQuery export.

    Attributes:
        big_query_export (google.cloud.securitycenter_v2.types.BigQueryExport):
            Required. The BigQuery export being updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
            If empty all mutable fields will be updated.
    """

    big_query_export: bigquery_export.BigQueryExport = proto.Field(
        proto.MESSAGE,
        number=1,
        message=bigquery_export.BigQueryExport,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateExternalSystemRequest(proto.Message):
    r"""Request message for updating a ExternalSystem resource.

    Attributes:
        external_system (google.cloud.securitycenter_v2.types.ExternalSystem):
            Required. The external system resource to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the
            external system resource.
            If empty all mutable fields will be updated.
    """

    external_system: gcs_external_system.ExternalSystem = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_external_system.ExternalSystem,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateFindingRequest(proto.Message):
    r"""Request message for updating or creating a finding.

    Attributes:
        finding (google.cloud.securitycenter_v2.types.Finding):
            Required. The finding resource to update or create if it
            does not already exist. parent, security_marks, and
            update_time will be ignored.

            In the case of creation, the finding id portion of the name
            must be alphanumeric and less than or equal to 32 characters
            and greater than 0 characters in length.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the finding resource.
            This field should not be specified when creating a finding.

            When updating a finding, an empty mask is treated as
            updating all mutable fields and replacing source_properties.
            Individual source_properties can be added/updated by using
            "source_properties." in the field mask.
    """

    finding: gcs_finding.Finding = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_finding.Finding,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateMuteConfigRequest(proto.Message):
    r"""Request message for updating a mute config.

    Attributes:
        mute_config (google.cloud.securitycenter_v2.types.MuteConfig):
            Required. The mute config being updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
            If empty all mutable fields will be updated.
    """

    mute_config: gcs_mute_config.MuteConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_mute_config.MuteConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateNotificationConfigRequest(proto.Message):
    r"""Request message for updating a notification config.

    Attributes:
        notification_config (google.cloud.securitycenter_v2.types.NotificationConfig):
            Required. The notification config to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the
            notification config.
            If empty all mutable fields will be updated.
    """

    notification_config: gcs_notification_config.NotificationConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_notification_config.NotificationConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateResourceValueConfigRequest(proto.Message):
    r"""Request message to update resource value config

    Attributes:
        resource_value_config (google.cloud.securitycenter_v2.types.ResourceValueConfig):
            Required. The resource value config being
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated. If empty all mutable
            fields will be updated.

            To update nested fields, include the top level field in the
            mask For example, to update gcp_metadata.resource_type,
            include the "gcp_metadata" field mask
    """

    resource_value_config: gcs_resource_value_config.ResourceValueConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_resource_value_config.ResourceValueConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateSecurityMarksRequest(proto.Message):
    r"""Request message for updating a SecurityMarks resource.

    Attributes:
        security_marks (google.cloud.securitycenter_v2.types.SecurityMarks):
            Required. The security marks resource to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the security marks
            resource.

            The field mask must not contain duplicate fields. If empty
            or set to "marks", all marks will be replaced. Individual
            marks can be updated using "marks.<mark_key>".
    """

    security_marks: gcs_security_marks.SecurityMarks = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_security_marks.SecurityMarks,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateSourceRequest(proto.Message):
    r"""Request message for updating a source.

    Attributes:
        source (google.cloud.securitycenter_v2.types.Source):
            Required. The source resource to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the source
            resource.
            If empty all mutable fields will be updated.
    """

    source: gcs_source.Source = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_source.Source,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
