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

import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.securitycenter_v1.types import asset as gcs_asset
from google.cloud.securitycenter_v1.types import (
    attack_path,
    bigquery_export,
    effective_event_threat_detection_custom_module,
    effective_security_health_analytics_custom_module,
    event_threat_detection_custom_module_validation_errors,
    folder,
    security_health_analytics_custom_config,
    valued_resource,
)
from google.cloud.securitycenter_v1.types import (
    event_threat_detection_custom_module as gcs_event_threat_detection_custom_module,
)
from google.cloud.securitycenter_v1.types import external_system as gcs_external_system
from google.cloud.securitycenter_v1.types import finding as gcs_finding
from google.cloud.securitycenter_v1.types import mute_config as gcs_mute_config
from google.cloud.securitycenter_v1.types import (
    notification_config as gcs_notification_config,
)
from google.cloud.securitycenter_v1.types import (
    organization_settings as gcs_organization_settings,
)
from google.cloud.securitycenter_v1.types import resource as gcs_resource
from google.cloud.securitycenter_v1.types import (
    resource_value_config as gcs_resource_value_config,
)
from google.cloud.securitycenter_v1.types import (
    security_health_analytics_custom_module as gcs_security_health_analytics_custom_module,
)
from google.cloud.securitycenter_v1.types import security_marks as gcs_security_marks
from google.cloud.securitycenter_v1.types import source as gcs_source

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "BulkMuteFindingsRequest",
        "BulkMuteFindingsResponse",
        "CreateFindingRequest",
        "CreateMuteConfigRequest",
        "CreateResourceValueConfigRequest",
        "BatchCreateResourceValueConfigsRequest",
        "BatchCreateResourceValueConfigsResponse",
        "DeleteResourceValueConfigRequest",
        "GetResourceValueConfigRequest",
        "ListResourceValueConfigsRequest",
        "ListResourceValueConfigsResponse",
        "UpdateResourceValueConfigRequest",
        "CreateNotificationConfigRequest",
        "CreateSecurityHealthAnalyticsCustomModuleRequest",
        "CreateSourceRequest",
        "DeleteMuteConfigRequest",
        "DeleteNotificationConfigRequest",
        "DeleteSecurityHealthAnalyticsCustomModuleRequest",
        "GetBigQueryExportRequest",
        "GetMuteConfigRequest",
        "GetNotificationConfigRequest",
        "GetOrganizationSettingsRequest",
        "GetEffectiveSecurityHealthAnalyticsCustomModuleRequest",
        "GetSecurityHealthAnalyticsCustomModuleRequest",
        "GetSourceRequest",
        "GroupAssetsRequest",
        "GroupAssetsResponse",
        "GroupFindingsRequest",
        "GroupFindingsResponse",
        "GroupResult",
        "ListDescendantSecurityHealthAnalyticsCustomModulesRequest",
        "ListDescendantSecurityHealthAnalyticsCustomModulesResponse",
        "ListValuedResourcesRequest",
        "ListValuedResourcesResponse",
        "ListAttackPathsRequest",
        "ListAttackPathsResponse",
        "GetSimulationRequest",
        "GetValuedResourceRequest",
        "ListMuteConfigsRequest",
        "ListMuteConfigsResponse",
        "ListNotificationConfigsRequest",
        "ListNotificationConfigsResponse",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesRequest",
        "ListEffectiveSecurityHealthAnalyticsCustomModulesResponse",
        "ListSecurityHealthAnalyticsCustomModulesRequest",
        "ListSecurityHealthAnalyticsCustomModulesResponse",
        "ListSourcesRequest",
        "ListSourcesResponse",
        "ListAssetsRequest",
        "ListAssetsResponse",
        "ListFindingsRequest",
        "ListFindingsResponse",
        "SetFindingStateRequest",
        "SetMuteRequest",
        "RunAssetDiscoveryRequest",
        "SimulateSecurityHealthAnalyticsCustomModuleRequest",
        "SimulateSecurityHealthAnalyticsCustomModuleResponse",
        "UpdateExternalSystemRequest",
        "UpdateFindingRequest",
        "UpdateMuteConfigRequest",
        "UpdateNotificationConfigRequest",
        "UpdateOrganizationSettingsRequest",
        "UpdateSecurityHealthAnalyticsCustomModuleRequest",
        "UpdateSourceRequest",
        "UpdateSecurityMarksRequest",
        "CreateBigQueryExportRequest",
        "UpdateBigQueryExportRequest",
        "ListBigQueryExportsRequest",
        "ListBigQueryExportsResponse",
        "DeleteBigQueryExportRequest",
        "CreateEventThreatDetectionCustomModuleRequest",
        "ValidateEventThreatDetectionCustomModuleRequest",
        "ValidateEventThreatDetectionCustomModuleResponse",
        "DeleteEventThreatDetectionCustomModuleRequest",
        "GetEventThreatDetectionCustomModuleRequest",
        "ListDescendantEventThreatDetectionCustomModulesRequest",
        "ListDescendantEventThreatDetectionCustomModulesResponse",
        "ListEventThreatDetectionCustomModulesRequest",
        "ListEventThreatDetectionCustomModulesResponse",
        "UpdateEventThreatDetectionCustomModuleRequest",
        "GetEffectiveEventThreatDetectionCustomModuleRequest",
        "ListEffectiveEventThreatDetectionCustomModulesRequest",
        "ListEffectiveEventThreatDetectionCustomModulesResponse",
    },
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
            applied. Its format is ``organizations/[organization_id]``,
            ``folders/[folder_id]``, ``projects/[project_id]``.
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
        mute_annotation (str):
            This can be a mute configuration name or any
            identifier for mute/unmute of findings based on
            the filter.
        mute_state (google.cloud.securitycenter_v1.types.BulkMuteFindingsRequest.MuteState):
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
    mute_annotation: str = proto.Field(
        proto.STRING,
        number=3,
    )
    mute_state: MuteState = proto.Field(
        proto.ENUM,
        number=4,
        enum=MuteState,
    )


class BulkMuteFindingsResponse(proto.Message):
    r"""The response to a BulkMute request. Contains the LRO
    information.

    """


class CreateFindingRequest(proto.Message):
    r"""Request message for creating a finding.

    Attributes:
        parent (str):
            Required. Resource name of the new finding's parent. Its
            format should be
            ``organizations/[organization_id]/sources/[source_id]``.
        finding_id (str):
            Required. Unique identifier provided by the
            client within the parent scope. It must be
            alphanumeric and less than or equal to 32
            characters and greater than 0 characters in
            length.
        finding (google.cloud.securitycenter_v1.types.Finding):
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
            Its format is ``organizations/[organization_id]``,
            ``folders/[folder_id]``, or ``projects/[project_id]``.
        mute_config (google.cloud.securitycenter_v1.types.MuteConfig):
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


class CreateResourceValueConfigRequest(proto.Message):
    r"""Request message to create single resource value config

    Attributes:
        parent (str):
            Required. Resource name of the new
            ResourceValueConfig's parent.
        resource_value_config (google.cloud.securitycenter_v1.types.ResourceValueConfig):
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


class BatchCreateResourceValueConfigsRequest(proto.Message):
    r"""Request message to create multiple resource value configs

    Attributes:
        parent (str):
            Required. Resource name of the new
            ResourceValueConfig's parent. The parent field
            in the CreateResourceValueConfigRequest messages
            must either be empty or match this field.
        requests (MutableSequence[google.cloud.securitycenter_v1.types.CreateResourceValueConfigRequest]):
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
        resource_value_configs (MutableSequence[google.cloud.securitycenter_v1.types.ResourceValueConfig]):
            The resource value configs created
    """

    resource_value_configs: MutableSequence[
        gcs_resource_value_config.ResourceValueConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_resource_value_config.ResourceValueConfig,
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


class GetResourceValueConfigRequest(proto.Message):
    r"""Request message to get resource value config

    Attributes:
        name (str):
            Required. Name of the resource value config to retrieve. Its
            format is
            ``organizations/{organization}/resourceValueConfigs/{config_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListResourceValueConfigsRequest(proto.Message):
    r"""Request message to list resource value configs of a parent

    Attributes:
        parent (str):
            Required. The parent, which owns the collection of resource
            value configs. Its format is
            ``organizations/[organization_id]``
        page_size (int):
            The number of results to return. The service
            may return fewer than this value.
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
        resource_value_configs (MutableSequence[google.cloud.securitycenter_v1.types.ResourceValueConfig]):
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


class UpdateResourceValueConfigRequest(proto.Message):
    r"""Request message to update resource value config

    Attributes:
        resource_value_config (google.cloud.securitycenter_v1.types.ResourceValueConfig):
            Required. The resource value config being
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
            If empty all mutable fields will be updated.
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


class CreateNotificationConfigRequest(proto.Message):
    r"""Request message for creating a notification config.

    Attributes:
        parent (str):
            Required. Resource name of the new notification config's
            parent. Its format is ``organizations/[organization_id]``,
            ``folders/[folder_id]``, or ``projects/[project_id]``.
        config_id (str):
            Required.
            Unique identifier provided by the client within
            the parent scope. It must be between 1 and 128
            characters and contain alphanumeric characters,
            underscores, or hyphens only.
        notification_config (google.cloud.securitycenter_v1.types.NotificationConfig):
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


class CreateSecurityHealthAnalyticsCustomModuleRequest(proto.Message):
    r"""Request message for creating Security Health Analytics custom
    modules.

    Attributes:
        parent (str):
            Required. Resource name of the new custom module's parent.
            Its format is
            ``organizations/{organization}/securityHealthAnalyticsSettings``,
            ``folders/{folder}/securityHealthAnalyticsSettings``, or
            ``projects/{project}/securityHealthAnalyticsSettings``
        security_health_analytics_custom_module (google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule):
            Required. SecurityHealthAnalytics custom
            module to create. The provided name is ignored
            and reset with provided parent information and
            server-generated ID.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    security_health_analytics_custom_module: gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
    )


class CreateSourceRequest(proto.Message):
    r"""Request message for creating a source.

    Attributes:
        parent (str):
            Required. Resource name of the new source's parent. Its
            format should be ``organizations/[organization_id]``.
        source (google.cloud.securitycenter_v1.types.Source):
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


class DeleteMuteConfigRequest(proto.Message):
    r"""Request message for deleting a mute config.

    Attributes:
        name (str):
            Required. Name of the mute config to delete. Its format is
            ``organizations/{organization}/muteConfigs/{config_id}``,
            ``folders/{folder}/muteConfigs/{config_id}``,
            ``projects/{project}/muteConfigs/{config_id}``,
            ``organizations/{organization}/locations/global/muteConfigs/{config_id}``,
            ``folders/{folder}/locations/global/muteConfigs/{config_id}``,
            or
            ``projects/{project}/locations/global/muteConfigs/{config_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteNotificationConfigRequest(proto.Message):
    r"""Request message for deleting a notification config.

    Attributes:
        name (str):
            Required. Name of the notification config to delete. Its
            format is
            ``organizations/[organization_id]/notificationConfigs/[config_id]``,
            ``folders/[folder_id]/notificationConfigs/[config_id]``, or
            ``projects/[project_id]/notificationConfigs/[config_id]``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteSecurityHealthAnalyticsCustomModuleRequest(proto.Message):
    r"""Request message for deleting Security Health Analytics custom
    modules.

    Attributes:
        name (str):
            Required. Name of the custom module to delete. Its format is
            ``organizations/{organization}/securityHealthAnalyticsSettings/customModules/{customModule}``,
            ``folders/{folder}/securityHealthAnalyticsSettings/customModules/{customModule}``,
            or
            ``projects/{project}/securityHealthAnalyticsSettings/customModules/{customModule}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetBigQueryExportRequest(proto.Message):
    r"""Request message for retrieving a BigQuery export.

    Attributes:
        name (str):
            Required. Name of the BigQuery export to retrieve. Its
            format is
            ``organizations/{organization}/bigQueryExports/{export_id}``,
            ``folders/{folder}/bigQueryExports/{export_id}``, or
            ``projects/{project}/bigQueryExports/{export_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetMuteConfigRequest(proto.Message):
    r"""Request message for retrieving a mute config.

    Attributes:
        name (str):
            Required. Name of the mute config to retrieve. Its format is
            ``organizations/{organization}/muteConfigs/{config_id}``,
            ``folders/{folder}/muteConfigs/{config_id}``,
            ``projects/{project}/muteConfigs/{config_id}``,
            ``organizations/{organization}/locations/global/muteConfigs/{config_id}``,
            ``folders/{folder}/locations/global/muteConfigs/{config_id}``,
            or
            ``projects/{project}/locations/global/muteConfigs/{config_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetNotificationConfigRequest(proto.Message):
    r"""Request message for getting a notification config.

    Attributes:
        name (str):
            Required. Name of the notification config to get. Its format
            is
            ``organizations/[organization_id]/notificationConfigs/[config_id]``,
            ``folders/[folder_id]/notificationConfigs/[config_id]``, or
            ``projects/[project_id]/notificationConfigs/[config_id]``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetOrganizationSettingsRequest(proto.Message):
    r"""Request message for getting organization settings.

    Attributes:
        name (str):
            Required. Name of the organization to get organization
            settings for. Its format is
            ``organizations/[organization_id]/organizationSettings``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(proto.Message):
    r"""Request message for getting effective Security Health
    Analytics custom modules.

    Attributes:
        name (str):
            Required. Name of the effective custom module to get. Its
            format is
            ``organizations/{organization}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}``,
            ``folders/{folder}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}``,
            or
            ``projects/{project}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSecurityHealthAnalyticsCustomModuleRequest(proto.Message):
    r"""Request message for getting Security Health Analytics custom
    modules.

    Attributes:
        name (str):
            Required. Name of the custom module to get. Its format is
            ``organizations/{organization}/securityHealthAnalyticsSettings/customModules/{customModule}``,
            ``folders/{folder}/securityHealthAnalyticsSettings/customModules/{customModule}``,
            or
            ``projects/{project}/securityHealthAnalyticsSettings/customModules/{customModule}``
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


class GroupAssetsRequest(proto.Message):
    r"""Request message for grouping by assets.

    Attributes:
        parent (str):
            Required. The name of the parent to group the assets by. Its
            format is ``organizations/[organization_id]``,
            ``folders/[folder_id]``, or ``projects/[project_id]``.
        filter (str):
            Expression that defines the filter to apply across assets.
            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are supported, and ``OR`` has higher precedence
            than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. The fields map to those defined in the Asset
            resource. Examples include:

            - name
            - security_center_properties.resource_name
            - resource_properties.a_property
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

            - update_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``update_time = "2019-06-10T16:07:18-07:00"``
              ``update_time = 1560208038000``

            - create_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``create_time = "2019-06-10T16:07:18-07:00"``
              ``create_time = 1560208038000``

            - iam_policy.policy_blob: ``=``, ``:``

            - resource_properties: ``=``, ``:``, ``>``, ``<``, ``>=``,
              ``<=``

            - security_marks.marks: ``=``, ``:``

            - security_center_properties.resource_name: ``=``, ``:``

            - security_center_properties.resource_display_name: ``=``,
              ``:``

            - security_center_properties.resource_type: ``=``, ``:``

            - security_center_properties.resource_parent: ``=``, ``:``

            - security_center_properties.resource_parent_display_name:
              ``=``, ``:``

            - security_center_properties.resource_project: ``=``, ``:``

            - security_center_properties.resource_project_display_name:
              ``=``, ``:``

            - security_center_properties.resource_owners: ``=``, ``:``

            For example, ``resource_properties.size = 100`` is a valid
            filter string.

            Use a partial match on the empty string to filter based on a
            property existing: ``resource_properties.my_property : ""``

            Use a negated partial match on the empty string to filter
            based on a property not existing:
            ``-resource_properties.my_property : ""``
        group_by (str):
            Required. Expression that defines what assets fields to use
            for grouping. The string value should follow SQL syntax:
            comma separated list of fields. For example:
            "security_center_properties.resource_project,security_center_properties.project".

            The following fields are supported when compare_duration is
            not set:

            - security_center_properties.resource_project
            - security_center_properties.resource_project_display_name
            - security_center_properties.resource_type
            - security_center_properties.resource_parent
            - security_center_properties.resource_parent_display_name

            The following fields are supported when compare_duration is
            set:

            - security_center_properties.resource_type
            - security_center_properties.resource_project_display_name
            - security_center_properties.resource_parent_display_name
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the GroupResult's
            "state_change" property is updated to indicate whether the
            asset was added, removed, or remained present during the
            compare_duration period of time that precedes the read_time.
            This is the time between (read_time - compare_duration) and
            read_time.

            The state change value is derived based on the presence of
            the asset at the two points in time. Intermediate state
            changes between the two times don't affect the result. For
            example, the results aren't affected if the asset is removed
            and re-created again.

            Possible "state_change" values when compare_duration is
            specified:

            - "ADDED": indicates that the asset was not present at the
              start of compare_duration, but present at reference_time.
            - "REMOVED": indicates that the asset was present at the
              start of compare_duration, but not present at
              reference_time.
            - "ACTIVE": indicates that the asset was present at both the
              start and the end of the time period defined by
              compare_duration and reference_time.

            If compare_duration is not specified, then the only possible
            state_change is "UNUSED", which will be the state_change set
            for all assets present at read_time.

            If this field is set then ``state_change`` must be a
            specified field in ``group_by``.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            assets. The filter is limited to assets existing
            at the supplied time and their values are those
            at that specific time. Absence of this field
            will default to the API's version of NOW.
        page_token (str):
            The value returned by the last ``GroupAssetsResponse``;
            indicates that this is a continuation of a prior
            ``GroupAssets`` call, and that the system should return the
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
    group_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    compare_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=8,
    )


class GroupAssetsResponse(proto.Message):
    r"""Response message for grouping by assets.

    Attributes:
        group_by_results (MutableSequence[google.cloud.securitycenter_v1.types.GroupResult]):
            Group results. There exists an element for
            each existing unique combination of
            property/values. The element contains a count
            for the number of times those specific
            property/values appear.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used for executing the groupBy request.
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
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class GroupFindingsRequest(proto.Message):
    r"""Request message for grouping by findings.

    Attributes:
        parent (str):
            Required. Name of the source to groupBy. Its format is
            ``organizations/[organization_id]/sources/[source_id]``,
            ``folders/[folder_id]/sources/[source_id]``, or
            ``projects/[project_id]/sources/[source_id]``. To groupBy
            across all sources provide a source_id of ``-``. For
            example:
            ``organizations/{organization_id}/sources/-, folders/{folder_id}/sources/-``,
            or ``projects/{project_id}/sources/-``
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
            - source_properties.a_property
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

            - workflow_state: ``=``, ``:``

            - security_marks.marks: ``=``, ``:``

            - source_properties: ``=``, ``:``, ``>``, ``<``, ``>=``,
              ``<=``

              For example, ``source_properties.size = 100`` is a valid
              filter string.

              Use a partial match on the empty string to filter based on
              a property existing:
              ``source_properties.my_property : ""``

              Use a negated partial match on the empty string to filter
              based on a property not existing:
              ``-source_properties.my_property : ""``

            - resource:

              - resource.name: ``=``, ``:``
              - resource.parent_name: ``=``, ``:``
              - resource.parent_display_name: ``=``, ``:``
              - resource.project_name: ``=``, ``:``
              - resource.project_display_name: ``=``, ``:``
              - resource.type: ``=``, ``:``
        group_by (str):
            Required. Expression that defines what assets fields to use
            for grouping (including ``state_change``). The string value
            should follow SQL syntax: comma separated list of fields.
            For example: "parent,resource_name".

            The following fields are supported when compare_duration is
            set:

            - state_change
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            findings. The filter is limited to findings
            existing at the supplied time and their values
            are those at that specific time. Absence of this
            field will default to the API's version of NOW.
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the GroupResult's
            "state_change" attribute is updated to indicate whether the
            finding had its state changed, the finding's state remained
            unchanged, or if the finding was added during the
            compare_duration period of time that precedes the read_time.
            This is the time between (read_time - compare_duration) and
            read_time.

            The state_change value is derived based on the presence and
            state of the finding at the two points in time. Intermediate
            state changes between the two times don't affect the result.
            For example, the results aren't affected if the finding is
            made inactive and then active again.

            Possible "state_change" values when compare_duration is
            specified:

            - "CHANGED": indicates that the finding was present and
              matched the given filter at the start of compare_duration,
              but changed its state at read_time.
            - "UNCHANGED": indicates that the finding was present and
              matched the given filter at the start of compare_duration
              and did not change state at read_time.
            - "ADDED": indicates that the finding did not match the
              given filter or was not present at the start of
              compare_duration, but was present at read_time.
            - "REMOVED": indicates that the finding was present and
              matched the filter at the start of compare_duration, but
              did not match the filter at read_time.

            If compare_duration is not specified, then the only possible
            state_change is "UNUSED", which will be the state_change set
            for all findings present at read_time.

            If this field is set then ``state_change`` must be a
            specified field in ``group_by``.
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
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    compare_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
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
        group_by_results (MutableSequence[google.cloud.securitycenter_v1.types.GroupResult]):
            Group results. There exists an element for
            each existing unique combination of
            property/values. The element contains a count
            for the number of times those specific
            property/values appear.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used for executing the groupBy request.
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
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
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


class ListDescendantSecurityHealthAnalyticsCustomModulesRequest(proto.Message):
    r"""Request message for listing descendant Security Health
    Analytics custom modules.

    Attributes:
        parent (str):
            Required. Name of parent to list descendant custom modules.
            Its format is
            ``organizations/{organization}/securityHealthAnalyticsSettings``,
            ``folders/{folder}/securityHealthAnalyticsSettings``, or
            ``projects/{project}/securityHealthAnalyticsSettings``
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
        page_token (str):
            The value returned by the last call
            indicating a continuation
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


class ListDescendantSecurityHealthAnalyticsCustomModulesResponse(proto.Message):
    r"""Response message for listing descendant Security Health
    Analytics custom modules.

    Attributes:
        security_health_analytics_custom_modules (MutableSequence[google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule]):
            Custom modules belonging to the requested
            parent and its descendants.
        next_page_token (str):
            If not empty, indicates that there may be
            more custom modules to be returned.
    """

    @property
    def raw_page(self):
        return self

    security_health_analytics_custom_modules: MutableSequence[
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
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
            Required. Name of parent to list valued resources.

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

            - ``resource``

            - ``display_name``

            Values should be a comma separated list of fields. For
            example: ``exposed_score,resource_value``.

            The default sorting order is descending. To specify
            ascending or descending order for a field, append a ``ASC``
            or a ``DESC`` suffix, respectively; for example:
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
        valued_resources (MutableSequence[google.cloud.securitycenter_v1.types.ValuedResource]):
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
        attack_paths (MutableSequence[google.cloud.securitycenter_v1.types.AttackPath]):
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


class ListMuteConfigsRequest(proto.Message):
    r"""Request message for listing  mute configs at a given scope
    e.g. organization, folder or project.

    Attributes:
        parent (str):
            Required. The parent, which owns the collection of mute
            configs. Its format is ``organizations/[organization_id]``,
            ``folders/[folder_id]``, ``projects/[project_id]``.
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
        mute_configs (MutableSequence[google.cloud.securitycenter_v1.types.MuteConfig]):
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
            "organizations/[organization_id]", "folders/[folder_id]", or
            "projects/[project_id]".
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
        notification_configs (MutableSequence[google.cloud.securitycenter_v1.types.NotificationConfig]):
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


class ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(proto.Message):
    r"""Request message for listing effective Security Health
    Analytics custom modules.

    Attributes:
        parent (str):
            Required. Name of parent to list effective custom modules.
            Its format is
            ``organizations/{organization}/securityHealthAnalyticsSettings``,
            ``folders/{folder}/securityHealthAnalyticsSettings``, or
            ``projects/{project}/securityHealthAnalyticsSettings``
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
        page_token (str):
            The value returned by the last call
            indicating a continuation
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


class ListEffectiveSecurityHealthAnalyticsCustomModulesResponse(proto.Message):
    r"""Response message for listing effective Security Health
    Analytics custom modules.

    Attributes:
        effective_security_health_analytics_custom_modules (MutableSequence[google.cloud.securitycenter_v1.types.EffectiveSecurityHealthAnalyticsCustomModule]):
            Effective custom modules belonging to the
            requested parent.
        next_page_token (str):
            If not empty, indicates that there may be
            more effective custom modules to be returned.
    """

    @property
    def raw_page(self):
        return self

    effective_security_health_analytics_custom_modules: MutableSequence[
        effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSecurityHealthAnalyticsCustomModulesRequest(proto.Message):
    r"""Request message for listing Security Health Analytics custom
    modules.

    Attributes:
        parent (str):
            Required. Name of parent to list custom modules. Its format
            is
            ``organizations/{organization}/securityHealthAnalyticsSettings``,
            ``folders/{folder}/securityHealthAnalyticsSettings``, or
            ``projects/{project}/securityHealthAnalyticsSettings``
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
        page_token (str):
            The value returned by the last call
            indicating a continuation
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


class ListSecurityHealthAnalyticsCustomModulesResponse(proto.Message):
    r"""Response message for listing Security Health Analytics custom
    modules.

    Attributes:
        security_health_analytics_custom_modules (MutableSequence[google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule]):
            Custom modules belonging to the requested
            parent.
        next_page_token (str):
            If not empty, indicates that there may be
            more custom modules to be returned.
    """

    @property
    def raw_page(self):
        return self

    security_health_analytics_custom_modules: MutableSequence[
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
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
        sources (MutableSequence[google.cloud.securitycenter_v1.types.Source]):
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


class ListAssetsRequest(proto.Message):
    r"""Request message for listing assets.

    Attributes:
        parent (str):
            Required. The name of the parent resource that contains the
            assets. The value that you can specify on parent depends on
            the method in which you specify parent. You can specify one
            of the following values:
            ``organizations/[organization_id]``,
            ``folders/[folder_id]``, or ``projects/[project_id]``.
        filter (str):
            Expression that defines the filter to apply across assets.
            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are supported, and ``OR`` has higher precedence
            than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. The fields map to those defined in the Asset
            resource. Examples include:

            - name
            - security_center_properties.resource_name
            - resource_properties.a_property
            - security_marks.marks.marka

            The supported operators are:

            - ``=`` for all value types.
            - ``>``, ``<``, ``>=``, ``<=`` for integer values.
            - ``:``, meaning substring matching, for strings.

            The supported value types are:

            - string literals in quotes.
            - integer literals without quotes.
            - boolean literals ``true`` and ``false`` without quotes.

            The following are the allowed field and operator
            combinations:

            - name: ``=``

            - update_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``update_time = "2019-06-10T16:07:18-07:00"``
              ``update_time = 1560208038000``

            - create_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``create_time = "2019-06-10T16:07:18-07:00"``
              ``create_time = 1560208038000``

            - iam_policy.policy_blob: ``=``, ``:``

            - resource_properties: ``=``, ``:``, ``>``, ``<``, ``>=``,
              ``<=``

            - security_marks.marks: ``=``, ``:``

            - security_center_properties.resource_name: ``=``, ``:``

            - security_center_properties.resource_display_name: ``=``,
              ``:``

            - security_center_properties.resource_type: ``=``, ``:``

            - security_center_properties.resource_parent: ``=``, ``:``

            - security_center_properties.resource_parent_display_name:
              ``=``, ``:``

            - security_center_properties.resource_project: ``=``, ``:``

            - security_center_properties.resource_project_display_name:
              ``=``, ``:``

            - security_center_properties.resource_owners: ``=``, ``:``

            For example, ``resource_properties.size = 100`` is a valid
            filter string.

            Use a partial match on the empty string to filter based on a
            property existing: ``resource_properties.my_property : ""``

            Use a negated partial match on the empty string to filter
            based on a property not existing:
            ``-resource_properties.my_property : ""``
        order_by (str):
            Expression that defines what fields and order to use for
            sorting. The string value should follow SQL syntax: comma
            separated list of fields. For example:
            "name,resource_properties.a_property". The default sorting
            order is ascending. To specify descending order for a field,
            a suffix " desc" should be appended to the field name. For
            example: "name desc,resource_properties.a_property".
            Redundant space characters in the syntax are insignificant.
            "name desc,resource_properties.a_property" and " name desc ,
            resource_properties.a_property " are equivalent.

            The following fields are supported: name update_time
            resource_properties security_marks.marks
            security_center_properties.resource_name
            security_center_properties.resource_display_name
            security_center_properties.resource_parent
            security_center_properties.resource_parent_display_name
            security_center_properties.resource_project
            security_center_properties.resource_project_display_name
            security_center_properties.resource_type
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            assets. The filter is limited to assets existing
            at the supplied time and their values are those
            at that specific time. Absence of this field
            will default to the API's version of NOW.
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the ListAssetsResult's
            "state_change" attribute is updated to indicate whether the
            asset was added, removed, or remained present during the
            compare_duration period of time that precedes the read_time.
            This is the time between (read_time - compare_duration) and
            read_time.

            The state_change value is derived based on the presence of
            the asset at the two points in time. Intermediate state
            changes between the two times don't affect the result. For
            example, the results aren't affected if the asset is removed
            and re-created again.

            Possible "state_change" values when compare_duration is
            specified:

            - "ADDED": indicates that the asset was not present at the
              start of compare_duration, but present at read_time.
            - "REMOVED": indicates that the asset was present at the
              start of compare_duration, but not present at read_time.
            - "ACTIVE": indicates that the asset was present at both the
              start and the end of the time period defined by
              compare_duration and read_time.

            If compare_duration is not specified, then the only possible
            state_change is "UNUSED", which will be the state_change set
            for all assets present at read_time.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            A field mask to specify the ListAssetsResult
            fields to be listed in the response.
            An empty field mask will list all fields.
        page_token (str):
            The value returned by the last ``ListAssetsResponse``;
            indicates that this is a continuation of a prior
            ``ListAssets`` call, and that the system should return the
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
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    compare_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
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


class ListAssetsResponse(proto.Message):
    r"""Response message for listing assets.

    Attributes:
        list_assets_results (MutableSequence[google.cloud.securitycenter_v1.types.ListAssetsResponse.ListAssetsResult]):
            Assets matching the list request.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used for executing the list request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
        total_size (int):
            The total number of assets matching the
            query.
    """

    class ListAssetsResult(proto.Message):
        r"""Result containing the Asset and its State.

        Attributes:
            asset (google.cloud.securitycenter_v1.types.Asset):
                Asset matching the search request.
            state_change (google.cloud.securitycenter_v1.types.ListAssetsResponse.ListAssetsResult.StateChange):
                State change of the asset between the points
                in time.
        """

        class StateChange(proto.Enum):
            r"""The change in state of the asset.

            When querying across two points in time this describes the change
            between the two points: ADDED, REMOVED, or ACTIVE. If there was no
            compare_duration supplied in the request the state change will be:
            UNUSED

            Values:
                UNUSED (0):
                    State change is unused, this is the canonical
                    default for this enum.
                ADDED (1):
                    Asset was added between the points in time.
                REMOVED (2):
                    Asset was removed between the points in time.
                ACTIVE (3):
                    Asset was present at both point(s) in time.
            """

            UNUSED = 0
            ADDED = 1
            REMOVED = 2
            ACTIVE = 3

        asset: gcs_asset.Asset = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcs_asset.Asset,
        )
        state_change: "ListAssetsResponse.ListAssetsResult.StateChange" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ListAssetsResponse.ListAssetsResult.StateChange",
        )

    @property
    def raw_page(self):
        return self

    list_assets_results: MutableSequence[ListAssetsResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ListAssetsResult,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ListFindingsRequest(proto.Message):
    r"""Request message for listing findings.

    Attributes:
        parent (str):
            Required. Name of the source the findings belong to. Its
            format is
            ``organizations/[organization_id]/sources/[source_id]``,
            ``folders/[folder_id]/sources/[source_id]``, or
            ``projects/[project_id]/sources/[source_id]``. To list
            across all sources provide a source_id of ``-``. For
            example: ``organizations/{organization_id}/sources/-``,
            ``folders/{folder_id}/sources/-`` or
            ``projects/{projects_id}/sources/-``
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
            - source_properties.a_property
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

            - workflow_state: ``=``, ``:``

            - security_marks.marks: ``=``, ``:``

            - source_properties: ``=``, ``:``, ``>``, ``<``, ``>=``,
              ``<=``

              For example, ``source_properties.size = 100`` is a valid
              filter string.

              Use a partial match on the empty string to filter based on
              a property existing:
              ``source_properties.my_property : ""``

              Use a negated partial match on the empty string to filter
              based on a property not existing:
              ``-source_properties.my_property : ""``

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
            separated list of fields. For example:
            "name,resource_properties.a_property". The default sorting
            order is ascending. To specify descending order for a field,
            a suffix " desc" should be appended to the field name. For
            example: "name desc,source_properties.a_property". Redundant
            space characters in the syntax are insignificant. "name
            desc,source_properties.a_property" and " name desc ,
            source_properties.a_property " are equivalent.

            The following fields are supported: name parent state
            category resource_name event_time source_properties
            security_marks.marks
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            findings. The filter is limited to findings
            existing at the supplied time and their values
            are those at that specific time. Absence of this
            field will default to the API's version of NOW.
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the ListFindingsResult's
            "state_change" attribute is updated to indicate whether the
            finding had its state changed, the finding's state remained
            unchanged, or if the finding was added in any state during
            the compare_duration period of time that precedes the
            read_time. This is the time between (read_time -
            compare_duration) and read_time.

            The state_change value is derived based on the presence and
            state of the finding at the two points in time. Intermediate
            state changes between the two times don't affect the result.
            For example, the results aren't affected if the finding is
            made inactive and then active again.

            Possible "state_change" values when compare_duration is
            specified:

            - "CHANGED": indicates that the finding was present and
              matched the given filter at the start of compare_duration,
              but changed its state at read_time.
            - "UNCHANGED": indicates that the finding was present and
              matched the given filter at the start of compare_duration
              and did not change state at read_time.
            - "ADDED": indicates that the finding did not match the
              given filter or was not present at the start of
              compare_duration, but was present at read_time.
            - "REMOVED": indicates that the finding was present and
              matched the filter at the start of compare_duration, but
              did not match the filter at read_time.

            If compare_duration is not specified, then the only possible
            state_change is "UNUSED", which will be the state_change set
            for all findings present at read_time.
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
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    compare_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
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
        list_findings_results (MutableSequence[google.cloud.securitycenter_v1.types.ListFindingsResponse.ListFindingsResult]):
            Findings matching the list request.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used for executing the list request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
        total_size (int):
            The total number of findings matching the
            query.
    """

    class ListFindingsResult(proto.Message):
        r"""Result containing the Finding and its StateChange.

        Attributes:
            finding (google.cloud.securitycenter_v1.types.Finding):
                Finding matching the search request.
            state_change (google.cloud.securitycenter_v1.types.ListFindingsResponse.ListFindingsResult.StateChange):
                State change of the finding between the
                points in time.
            resource (google.cloud.securitycenter_v1.types.ListFindingsResponse.ListFindingsResult.Resource):
                Output only. Resource that is associated with
                this finding.
        """

        class StateChange(proto.Enum):
            r"""The change in state of the finding.

            When querying across two points in time this describes the change in
            the finding between the two points: CHANGED, UNCHANGED, ADDED, or
            REMOVED. Findings can not be deleted, so REMOVED implies that the
            finding at timestamp does not match the filter specified, but it did
            at timestamp - compare_duration. If there was no compare_duration
            supplied in the request the state change will be: UNUSED

            Values:
                UNUSED (0):
                    State change is unused, this is the canonical
                    default for this enum.
                CHANGED (1):
                    The finding has changed state in some way
                    between the points in time and existed at both
                    points.
                UNCHANGED (2):
                    The finding has not changed state between the
                    points in time and existed at both points.
                ADDED (3):
                    The finding was created between the points in
                    time.
                REMOVED (4):
                    The finding at timestamp does not match the filter
                    specified, but it did at timestamp - compare_duration.
            """

            UNUSED = 0
            CHANGED = 1
            UNCHANGED = 2
            ADDED = 3
            REMOVED = 4

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
                project_name (str):
                    The full resource name of project that the
                    resource belongs to.
                project_display_name (str):
                    The project ID that the resource belongs to.
                parent_name (str):
                    The full resource name of resource's parent.
                parent_display_name (str):
                    The human readable name of resource's parent.
                folders (MutableSequence[google.cloud.securitycenter_v1.types.Folder]):
                    Contains a Folder message for each folder in
                    the assets ancestry. The first folder is the
                    deepest nested folder, and the last folder is
                    the folder directly under the Organization.
                cloud_provider (google.cloud.securitycenter_v1.types.CloudProvider):
                    Indicates which cloud provider the finding is
                    from.
                organization (str):
                    Indicates which organization / tenant the
                    finding is for.
                service (str):
                    The service or resource provider associated
                    with the resource.
                location (str):
                    The region or location of the service (if
                    applicable).
                aws_metadata (google.cloud.securitycenter_v1.types.AwsMetadata):
                    The AWS metadata associated with the finding.

                    This field is a member of `oneof`_ ``cloud_provider_metadata``.
                azure_metadata (google.cloud.securitycenter_v1.types.AzureMetadata):
                    The Azure metadata associated with the
                    finding.

                    This field is a member of `oneof`_ ``cloud_provider_metadata``.
                resource_path (google.cloud.securitycenter_v1.types.ResourcePath):
                    Provides the path to the resource within the
                    resource hierarchy.
                resource_path_string (str):
                    A string representation of the resource path. For Google
                    Cloud, it has the format of
                    ``org/{organization_id}/folder/{folder_id}/folder/{folder_id}/project/{project_id}``
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
                number=8,
            )
            type_: str = proto.Field(
                proto.STRING,
                number=6,
            )
            project_name: str = proto.Field(
                proto.STRING,
                number=2,
            )
            project_display_name: str = proto.Field(
                proto.STRING,
                number=3,
            )
            parent_name: str = proto.Field(
                proto.STRING,
                number=4,
            )
            parent_display_name: str = proto.Field(
                proto.STRING,
                number=5,
            )
            folders: MutableSequence[folder.Folder] = proto.RepeatedField(
                proto.MESSAGE,
                number=7,
                message=folder.Folder,
            )
            cloud_provider: gcs_resource.CloudProvider = proto.Field(
                proto.ENUM,
                number=9,
                enum=gcs_resource.CloudProvider,
            )
            organization: str = proto.Field(
                proto.STRING,
                number=10,
            )
            service: str = proto.Field(
                proto.STRING,
                number=11,
            )
            location: str = proto.Field(
                proto.STRING,
                number=12,
            )
            aws_metadata: gcs_resource.AwsMetadata = proto.Field(
                proto.MESSAGE,
                number=16,
                oneof="cloud_provider_metadata",
                message=gcs_resource.AwsMetadata,
            )
            azure_metadata: gcs_resource.AzureMetadata = proto.Field(
                proto.MESSAGE,
                number=17,
                oneof="cloud_provider_metadata",
                message=gcs_resource.AzureMetadata,
            )
            resource_path: gcs_resource.ResourcePath = proto.Field(
                proto.MESSAGE,
                number=18,
                message=gcs_resource.ResourcePath,
            )
            resource_path_string: str = proto.Field(
                proto.STRING,
                number=19,
            )

        finding: gcs_finding.Finding = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcs_finding.Finding,
        )
        state_change: "ListFindingsResponse.ListFindingsResult.StateChange" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="ListFindingsResponse.ListFindingsResult.StateChange",
            )
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
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class SetFindingStateRequest(proto.Message):
    r"""Request message for updating a finding's state.

    Attributes:
        name (str):
            Required. The `relative resource
            name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__
            of the finding. Example:
            ``organizations/{organization_id}/sources/{source_id}/findings/{finding_id}``,
            ``folders/{folder_id}/sources/{source_id}/findings/{finding_id}``,
            ``projects/{project_id}/sources/{source_id}/findings/{finding_id}``.
        state (google.cloud.securitycenter_v1.types.Finding.State):
            Required. The desired State of the finding.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The time at which the updated state
            takes effect.
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
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class SetMuteRequest(proto.Message):
    r"""Request message for updating a finding's mute status.

    Attributes:
        name (str):
            Required. The `relative resource
            name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__
            of the finding. Example:
            ``organizations/{organization_id}/sources/{source_id}/findings/{finding_id}``,
            ``folders/{folder_id}/sources/{source_id}/findings/{finding_id}``,
            ``projects/{project_id}/sources/{source_id}/findings/{finding_id}``.
        mute (google.cloud.securitycenter_v1.types.Finding.Mute):
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


class RunAssetDiscoveryRequest(proto.Message):
    r"""Request message for running asset discovery for an
    organization.

    Attributes:
        parent (str):
            Required. Name of the organization to run asset discovery
            for. Its format is ``organizations/[organization_id]``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SimulateSecurityHealthAnalyticsCustomModuleRequest(proto.Message):
    r"""Request message to simulate a CustomConfig against a given
    test resource. Maximum size of the request is 4 MB by default.

    Attributes:
        parent (str):
            Required. The relative resource name of the organization,
            project, or folder. For more information about relative
            resource names, see `Relative Resource
            Name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__
            Example: ``organizations/{organization_id}``
        custom_config (google.cloud.securitycenter_v1.types.CustomConfig):
            Required. The custom configuration that you
            need to test.
        resource (google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource):
            Required. Resource data to simulate custom
            module against.
    """

    class SimulatedResource(proto.Message):
        r"""Manually constructed resource name. If the custom module evaluates
        against only the resource data, you can omit the ``iam_policy_data``
        field. If it evaluates only the ``iam_policy_data`` field, you can
        omit the resource data.

        Attributes:
            resource_type (str):
                Required. The type of the resource, for example,
                ``compute.googleapis.com/Disk``.
            resource_data (google.protobuf.struct_pb2.Struct):
                Optional. A representation of the Google
                Cloud resource. Should match the Google Cloud
                resource JSON format.
            iam_policy_data (google.iam.v1.policy_pb2.Policy):
                Optional. A representation of the IAM policy.
        """

        resource_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        resource_data: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )
        iam_policy_data: policy_pb2.Policy = proto.Field(
            proto.MESSAGE,
            number=3,
            message=policy_pb2.Policy,
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_config: security_health_analytics_custom_config.CustomConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=security_health_analytics_custom_config.CustomConfig,
    )
    resource: SimulatedResource = proto.Field(
        proto.MESSAGE,
        number=3,
        message=SimulatedResource,
    )


class SimulateSecurityHealthAnalyticsCustomModuleResponse(proto.Message):
    r"""Response message for simulating a
    ``SecurityHealthAnalyticsCustomModule`` against a given resource.

    Attributes:
        result (google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleResponse.SimulatedResult):
            Result for test case in the corresponding
            request.
    """

    class SimulatedResult(proto.Message):
        r"""Possible test result.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            finding (google.cloud.securitycenter_v1.types.Finding):
                Finding that would be published for the test
                case, if a violation is detected.

                This field is a member of `oneof`_ ``result``.
            no_violation (google.protobuf.empty_pb2.Empty):
                Indicates that the test case does not trigger
                any violation.

                This field is a member of `oneof`_ ``result``.
            error (google.rpc.status_pb2.Status):
                Error encountered during the test.

                This field is a member of `oneof`_ ``result``.
        """

        finding: gcs_finding.Finding = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="result",
            message=gcs_finding.Finding,
        )
        no_violation: empty_pb2.Empty = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="result",
            message=empty_pb2.Empty,
        )
        error: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="result",
            message=status_pb2.Status,
        )

    result: SimulatedResult = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SimulatedResult,
    )


class UpdateExternalSystemRequest(proto.Message):
    r"""Request message for updating a ExternalSystem resource.

    Attributes:
        external_system (google.cloud.securitycenter_v1.types.ExternalSystem):
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
        finding (google.cloud.securitycenter_v1.types.Finding):
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
        mute_config (google.cloud.securitycenter_v1.types.MuteConfig):
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
        notification_config (google.cloud.securitycenter_v1.types.NotificationConfig):
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


class UpdateOrganizationSettingsRequest(proto.Message):
    r"""Request message for updating an organization's settings.

    Attributes:
        organization_settings (google.cloud.securitycenter_v1.types.OrganizationSettings):
            Required. The organization settings resource
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the
            settings resource.
            If empty all mutable fields will be updated.
    """

    organization_settings: gcs_organization_settings.OrganizationSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_organization_settings.OrganizationSettings,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateSecurityHealthAnalyticsCustomModuleRequest(proto.Message):
    r"""Request message for updating Security Health Analytics custom
    modules.

    Attributes:
        security_health_analytics_custom_module (google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule):
            Required. The SecurityHealthAnalytics custom
            module to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated. The only fields that can
            be updated are ``enablement_state`` and ``custom_config``.
            If empty or set to the wildcard value ``*``, both
            ``enablement_state`` and ``custom_config`` are updated.
    """

    security_health_analytics_custom_module: gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateSourceRequest(proto.Message):
    r"""Request message for updating a source.

    Attributes:
        source (google.cloud.securitycenter_v1.types.Source):
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


class UpdateSecurityMarksRequest(proto.Message):
    r"""Request message for updating a SecurityMarks resource.

    Attributes:
        security_marks (google.cloud.securitycenter_v1.types.SecurityMarks):
            Required. The security marks resource to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the security marks
            resource.

            The field mask must not contain duplicate fields. If empty
            or set to "marks", all marks will be replaced. Individual
            marks can be updated using "marks.<mark_key>".
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the updated SecurityMarks
            take effect. If not set uses current server
            time.  Updates will be applied to the
            SecurityMarks that are active immediately
            preceding this time. Must be earlier or equal to
            the server time.
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
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class CreateBigQueryExportRequest(proto.Message):
    r"""Request message for creating a BigQuery export.

    Attributes:
        parent (str):
            Required. The name of the parent resource of the new
            BigQuery export. Its format is
            ``organizations/[organization_id]``,
            ``folders/[folder_id]``, or ``projects/[project_id]``.
        big_query_export (google.cloud.securitycenter_v1.types.BigQueryExport):
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


class UpdateBigQueryExportRequest(proto.Message):
    r"""Request message for updating a BigQuery export.

    Attributes:
        big_query_export (google.cloud.securitycenter_v1.types.BigQueryExport):
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


class ListBigQueryExportsRequest(proto.Message):
    r"""Request message for listing BigQuery exports at a given scope
    e.g. organization, folder or project.

    Attributes:
        parent (str):
            Required. The parent, which owns the collection of BigQuery
            exports. Its format is ``organizations/[organization_id]``,
            ``folders/[folder_id]``, ``projects/[project_id]``.
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
        big_query_exports (MutableSequence[google.cloud.securitycenter_v1.types.BigQueryExport]):
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


class DeleteBigQueryExportRequest(proto.Message):
    r"""Request message for deleting a BigQuery export.

    Attributes:
        name (str):
            Required. The name of the BigQuery export to delete. Its
            format is
            ``organizations/{organization}/bigQueryExports/{export_id}``,
            ``folders/{folder}/bigQueryExports/{export_id}``, or
            ``projects/{project}/bigQueryExports/{export_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEventThreatDetectionCustomModuleRequest(proto.Message):
    r"""Request to create an Event Threat Detection custom module.

    Attributes:
        parent (str):
            Required. The new custom module's parent.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings``.
            - ``folders/{folder}/eventThreatDetectionSettings``.
            - ``projects/{project}/eventThreatDetectionSettings``.
        event_threat_detection_custom_module (google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule):
            Required. The module to create. The
            event_threat_detection_custom_module.name will be ignored
            and server generated.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_threat_detection_custom_module: gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    )


class ValidateEventThreatDetectionCustomModuleRequest(proto.Message):
    r"""Request to validate an Event Threat Detection custom module.

    Attributes:
        parent (str):
            Required. Resource name of the parent to validate the Custom
            Module under.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings``.
            - ``folders/{folder}/eventThreatDetectionSettings``.
            - ``projects/{project}/eventThreatDetectionSettings``.
        raw_text (str):
            Required. The raw text of the module's
            contents. Used to generate error messages.
        type_ (str):
            Required. The type of the module (e.g. CONFIGURABLE_BAD_IP).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    raw_text: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ValidateEventThreatDetectionCustomModuleResponse(proto.Message):
    r"""Response to validating an Event Threat Detection custom
    module.

    Attributes:
        errors (google.cloud.securitycenter_v1.types.CustomModuleValidationErrors):
            A list of errors returned by the validator.
            If the list is empty, there were no errors.
    """

    errors: event_threat_detection_custom_module_validation_errors.CustomModuleValidationErrors = proto.Field(
        proto.MESSAGE,
        number=2,
        message=event_threat_detection_custom_module_validation_errors.CustomModuleValidationErrors,
    )


class DeleteEventThreatDetectionCustomModuleRequest(proto.Message):
    r"""Request to delete an Event Threat Detection custom module.

    Attributes:
        name (str):
            Required. Name of the custom module to delete.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings/customModules/{module}``.
            - ``folders/{folder}/eventThreatDetectionSettings/customModules/{module}``.
            - ``projects/{project}/eventThreatDetectionSettings/customModules/{module}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetEventThreatDetectionCustomModuleRequest(proto.Message):
    r"""Request to get an Event Threat Detection custom module.

    Attributes:
        name (str):
            Required. Name of the custom module to get.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings/customModules/{module}``.
            - ``folders/{folder}/eventThreatDetectionSettings/customModules/{module}``.
            - ``projects/{project}/eventThreatDetectionSettings/customModules/{module}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDescendantEventThreatDetectionCustomModulesRequest(proto.Message):
    r"""Request to list current and descendant resident Event Threat
    Detection custom modules.

    Attributes:
        parent (str):
            Required. Name of the parent to list custom modules under.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings``.
            - ``folders/{folder}/eventThreatDetectionSettings``.
            - ``projects/{project}/eventThreatDetectionSettings``.
        page_token (str):
            A page token, received from a previous
            ``ListDescendantEventThreatDetectionCustomModules`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListDescendantEventThreatDetectionCustomModules`` must
            match the call that provided the page token.
        page_size (int):
            The maximum number of modules to return. The
            service may return fewer than this value.
            If unspecified, at most 10 configs will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
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


class ListDescendantEventThreatDetectionCustomModulesResponse(proto.Message):
    r"""Response for listing current and descendant resident
    Event Threat Detection custom modules.

    Attributes:
        event_threat_detection_custom_modules (MutableSequence[google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule]):
            Custom modules belonging to the requested
            parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    event_threat_detection_custom_modules: MutableSequence[
        gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListEventThreatDetectionCustomModulesRequest(proto.Message):
    r"""Request to list Event Threat Detection custom modules.

    Attributes:
        parent (str):
            Required. Name of the parent to list custom modules under.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings``.
            - ``folders/{folder}/eventThreatDetectionSettings``.
            - ``projects/{project}/eventThreatDetectionSettings``.
        page_token (str):
            A page token, received from a previous
            ``ListEventThreatDetectionCustomModules`` call. Provide this
            to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListEventThreatDetectionCustomModules`` must match the
            call that provided the page token.
        page_size (int):
            The maximum number of modules to return. The
            service may return fewer than this value.
            If unspecified, at most 10 configs will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
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


class ListEventThreatDetectionCustomModulesResponse(proto.Message):
    r"""Response for listing Event Threat Detection custom modules.

    Attributes:
        event_threat_detection_custom_modules (MutableSequence[google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule]):
            Custom modules belonging to the requested
            parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    event_threat_detection_custom_modules: MutableSequence[
        gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateEventThreatDetectionCustomModuleRequest(proto.Message):
    r"""Request to update an Event Threat Detection custom module.

    Attributes:
        event_threat_detection_custom_module (google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule):
            Required. The module being updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
            If empty all mutable fields will be updated.
    """

    event_threat_detection_custom_module: gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetEffectiveEventThreatDetectionCustomModuleRequest(proto.Message):
    r"""Request to get an EffectiveEventThreatDetectionCustomModule.

    Attributes:
        name (str):
            Required. The resource name of the effective Event Threat
            Detection custom module.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings/effectiveCustomModules/{module}``.
            - ``folders/{folder}/eventThreatDetectionSettings/effectiveCustomModules/{module}``.
            - ``projects/{project}/eventThreatDetectionSettings/effectiveCustomModules/{module}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListEffectiveEventThreatDetectionCustomModulesRequest(proto.Message):
    r"""Request to list effective Event Threat Detection custom
    modules.

    Attributes:
        parent (str):
            Required. Name of the parent to list custom modules for.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings``.
            - ``folders/{folder}/eventThreatDetectionSettings``.
            - ``projects/{project}/eventThreatDetectionSettings``.
        page_token (str):
            A page token, received from a previous
            ``ListEffectiveEventThreatDetectionCustomModules`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListEffectiveEventThreatDetectionCustomModules`` must
            match the call that provided the page token.
        page_size (int):
            The maximum number of modules to return. The
            service may return fewer than this value.
            If unspecified, at most 10 configs will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
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


class ListEffectiveEventThreatDetectionCustomModulesResponse(proto.Message):
    r"""Response for listing
    EffectiveEventThreatDetectionCustomModules.

    Attributes:
        effective_event_threat_detection_custom_modules (MutableSequence[google.cloud.securitycenter_v1.types.EffectiveEventThreatDetectionCustomModule]):
            Effective custom modules belonging to the
            requested parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    effective_event_threat_detection_custom_modules: MutableSequence[
        effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
