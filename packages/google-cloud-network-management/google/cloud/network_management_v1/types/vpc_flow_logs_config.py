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
    package="google.cloud.networkmanagement.v1",
    manifest={
        "VpcFlowLogsConfig",
        "EffectiveVpcFlowLogsConfig",
    },
)


class VpcFlowLogsConfig(proto.Message):
    r"""A configuration to generate VPC Flow Logs.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Unique name of the configuration. The name can
            have one of the following forms:

            - For project-level configurations:
              ``projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}``

            - For organization-level configurations:
              ``organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}``
        description (str):
            Optional. The user-supplied description of
            the VPC Flow Logs configuration. Maximum of 512
            characters.

            This field is a member of `oneof`_ ``_description``.
        state (google.cloud.network_management_v1.types.VpcFlowLogsConfig.State):
            Optional. The state of the VPC Flow Log
            configuration. Default value is ENABLED. When
            creating a new configuration, it must be
            enabled. Setting state=DISABLED will pause the
            log generation for this config.

            This field is a member of `oneof`_ ``_state``.
        aggregation_interval (google.cloud.network_management_v1.types.VpcFlowLogsConfig.AggregationInterval):
            Optional. The aggregation interval for the logs. Default
            value is INTERVAL_5_SEC.

            This field is a member of `oneof`_ ``_aggregation_interval``.
        flow_sampling (float):
            Optional. The value of the field must be in (0, 1]. The
            sampling rate of VPC Flow Logs where 1.0 means all collected
            logs are reported. Setting the sampling rate to 0.0 is not
            allowed. If you want to disable VPC Flow Logs, use the state
            field instead. Default value is 1.0.

            This field is a member of `oneof`_ ``_flow_sampling``.
        metadata (google.cloud.network_management_v1.types.VpcFlowLogsConfig.Metadata):
            Optional. Configures whether all, none or a subset of
            metadata fields should be added to the reported VPC flow
            logs. Default value is INCLUDE_ALL_METADATA.

            This field is a member of `oneof`_ ``_metadata``.
        metadata_fields (MutableSequence[str]):
            Optional. Custom metadata fields to include in the reported
            VPC flow logs. Can only be specified if "metadata" was set
            to CUSTOM_METADATA.
        filter_expr (str):
            Optional. Export filter used to define which
            VPC Flow Logs should be logged.

            This field is a member of `oneof`_ ``_filter_expr``.
        cross_project_metadata (google.cloud.network_management_v1.types.VpcFlowLogsConfig.CrossProjectMetadata):
            Optional. Determines whether to include cross project
            annotations in the logs. This field is available only for
            organization configurations. If not specified in org configs
            will be set to CROSS_PROJECT_METADATA_ENABLED.

            This field is a member of `oneof`_ ``_cross_project_metadata``.
        target_resource_state (google.cloud.network_management_v1.types.VpcFlowLogsConfig.TargetResourceState):
            Output only. Describes the state of the
            configured target resource for diagnostic
            purposes.

            This field is a member of `oneof`_ ``_target_resource_state``.
        network (str):
            Traffic will be logged from VMs, VPN tunnels and
            Interconnect Attachments within the network. Format:
            projects/{project_id}/global/networks/{name}

            This field is a member of `oneof`_ ``target_resource``.
        subnet (str):
            Traffic will be logged from VMs within the subnetwork.
            Format:
            projects/{project_id}/regions/{region}/subnetworks/{name}

            This field is a member of `oneof`_ ``target_resource``.
        interconnect_attachment (str):
            Traffic will be logged from the Interconnect Attachment.
            Format:
            projects/{project_id}/regions/{region}/interconnectAttachments/{name}

            This field is a member of `oneof`_ ``target_resource``.
        vpn_tunnel (str):
            Traffic will be logged from the VPN Tunnel. Format:
            projects/{project_id}/regions/{region}/vpnTunnels/{name}

            This field is a member of `oneof`_ ``target_resource``.
        labels (MutableMapping[str, str]):
            Optional. Resource labels to represent
            user-provided metadata.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the config was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the config was updated.
    """

    class State(proto.Enum):
        r"""Determines whether this configuration will be generating
        logs.

        Values:
            STATE_UNSPECIFIED (0):
                If not specified, will default to ENABLED.
            ENABLED (1):
                When ENABLED, this configuration will
                generate logs.
            DISABLED (2):
                When DISABLED, this configuration will not
                generate logs.
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    class AggregationInterval(proto.Enum):
        r"""Toggles the aggregation interval for collecting flow logs by
        5-tuple.

        Values:
            AGGREGATION_INTERVAL_UNSPECIFIED (0):
                If not specified, will default to INTERVAL_5_SEC.
            INTERVAL_5_SEC (1):
                Aggregate logs in 5s intervals.
            INTERVAL_30_SEC (2):
                Aggregate logs in 30s intervals.
            INTERVAL_1_MIN (3):
                Aggregate logs in 1m intervals.
            INTERVAL_5_MIN (4):
                Aggregate logs in 5m intervals.
            INTERVAL_10_MIN (5):
                Aggregate logs in 10m intervals.
            INTERVAL_15_MIN (6):
                Aggregate logs in 15m intervals.
        """

        AGGREGATION_INTERVAL_UNSPECIFIED = 0
        INTERVAL_5_SEC = 1
        INTERVAL_30_SEC = 2
        INTERVAL_1_MIN = 3
        INTERVAL_5_MIN = 4
        INTERVAL_10_MIN = 5
        INTERVAL_15_MIN = 6

    class Metadata(proto.Enum):
        r"""Configures which log fields would be included.

        Values:
            METADATA_UNSPECIFIED (0):
                If not specified, will default to INCLUDE_ALL_METADATA.
            INCLUDE_ALL_METADATA (1):
                Include all metadata fields.
            EXCLUDE_ALL_METADATA (2):
                Exclude all metadata fields.
            CUSTOM_METADATA (3):
                Include only custom fields (specified in metadata_fields).
        """

        METADATA_UNSPECIFIED = 0
        INCLUDE_ALL_METADATA = 1
        EXCLUDE_ALL_METADATA = 2
        CUSTOM_METADATA = 3

    class CrossProjectMetadata(proto.Enum):
        r"""Determines whether to include cross project annotations in the logs.
        Project configurations will always have
        CROSS_PROJECT_METADATA_DISABLED.

        Values:
            CROSS_PROJECT_METADATA_UNSPECIFIED (0):
                If not specified, the default is
                CROSS_PROJECT_METADATA_ENABLED.
            CROSS_PROJECT_METADATA_ENABLED (1):
                When CROSS_PROJECT_METADATA_ENABLED, metadata from other
                projects will be included in the logs.
            CROSS_PROJECT_METADATA_DISABLED (2):
                When CROSS_PROJECT_METADATA_DISABLED, metadata from other
                projects will not be included in the logs.
        """

        CROSS_PROJECT_METADATA_UNSPECIFIED = 0
        CROSS_PROJECT_METADATA_ENABLED = 1
        CROSS_PROJECT_METADATA_DISABLED = 2

    class TargetResourceState(proto.Enum):
        r"""Output only. Indicates whether the target resource exists,
        for diagnostic purposes.

        Values:
            TARGET_RESOURCE_STATE_UNSPECIFIED (0):
                Unspecified target resource state.
            TARGET_RESOURCE_EXISTS (1):
                Indicates that the target resource exists.
            TARGET_RESOURCE_DOES_NOT_EXIST (2):
                Indicates that the target resource does not
                exist.
        """

        TARGET_RESOURCE_STATE_UNSPECIFIED = 0
        TARGET_RESOURCE_EXISTS = 1
        TARGET_RESOURCE_DOES_NOT_EXIST = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=State,
    )
    aggregation_interval: AggregationInterval = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=AggregationInterval,
    )
    flow_sampling: float = proto.Field(
        proto.FLOAT,
        number=5,
        optional=True,
    )
    metadata: Metadata = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=Metadata,
    )
    metadata_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    filter_expr: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    cross_project_metadata: CrossProjectMetadata = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=CrossProjectMetadata,
    )
    target_resource_state: TargetResourceState = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum=TargetResourceState,
    )
    network: str = proto.Field(
        proto.STRING,
        number=100,
        oneof="target_resource",
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=101,
        oneof="target_resource",
    )
    interconnect_attachment: str = proto.Field(
        proto.STRING,
        number=102,
        oneof="target_resource",
    )
    vpn_tunnel: str = proto.Field(
        proto.STRING,
        number=103,
        oneof="target_resource",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class EffectiveVpcFlowLogsConfig(proto.Message):
    r"""A configuration to generate a response for
    GetEffectiveVpcFlowLogsConfig request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Unique name of the configuration. The name can have one of
            the following forms:

            - For project-level configurations:
              ``projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}``

            - For organization-level configurations:
              ``organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}``

            - For a Compute config, the name will be the path of the
              subnet:
              ``projects/{project_id}/regions/{region}/subnetworks/{subnet_id}``
        state (google.cloud.network_management_v1.types.VpcFlowLogsConfig.State):
            The state of the VPC Flow Log configuration.
            Default value is ENABLED. When creating a new
            configuration, it must be enabled. Setting
            state=DISABLED will pause the log generation for
            this config.

            This field is a member of `oneof`_ ``_state``.
        aggregation_interval (google.cloud.network_management_v1.types.VpcFlowLogsConfig.AggregationInterval):
            The aggregation interval for the logs. Default value is
            INTERVAL_5_SEC.

            This field is a member of `oneof`_ ``_aggregation_interval``.
        flow_sampling (float):
            The value of the field must be in (0, 1]. The sampling rate
            of VPC Flow Logs where 1.0 means all collected logs are
            reported. Setting the sampling rate to 0.0 is not allowed.
            If you want to disable VPC Flow Logs, use the state field
            instead. Default value is 1.0.

            This field is a member of `oneof`_ ``_flow_sampling``.
        metadata (google.cloud.network_management_v1.types.VpcFlowLogsConfig.Metadata):
            Configures whether all, none or a subset of metadata fields
            should be added to the reported VPC flow logs. Default value
            is INCLUDE_ALL_METADATA.

            This field is a member of `oneof`_ ``_metadata``.
        metadata_fields (MutableSequence[str]):
            Custom metadata fields to include in the reported VPC flow
            logs. Can only be specified if "metadata" was set to
            CUSTOM_METADATA.
        filter_expr (str):
            Export filter used to define which VPC Flow
            Logs should be logged.

            This field is a member of `oneof`_ ``_filter_expr``.
        cross_project_metadata (google.cloud.network_management_v1.types.VpcFlowLogsConfig.CrossProjectMetadata):
            Determines whether to include cross project annotations in
            the logs. This field is available only for organization
            configurations. If not specified in org configs will be set
            to CROSS_PROJECT_METADATA_ENABLED.

            This field is a member of `oneof`_ ``_cross_project_metadata``.
        network (str):
            Traffic will be logged from VMs, VPN tunnels and
            Interconnect Attachments within the network. Format:
            projects/{project_id}/global/networks/{name}

            This field is a member of `oneof`_ ``target_resource``.
        subnet (str):
            Traffic will be logged from VMs within the subnetwork.
            Format:
            projects/{project_id}/regions/{region}/subnetworks/{name}

            This field is a member of `oneof`_ ``target_resource``.
        interconnect_attachment (str):
            Traffic will be logged from the Interconnect Attachment.
            Format:
            projects/{project_id}/regions/{region}/interconnectAttachments/{name}

            This field is a member of `oneof`_ ``target_resource``.
        vpn_tunnel (str):
            Traffic will be logged from the VPN Tunnel. Format:
            projects/{project_id}/regions/{region}/vpnTunnels/{name}

            This field is a member of `oneof`_ ``target_resource``.
        scope (google.cloud.network_management_v1.types.EffectiveVpcFlowLogsConfig.Scope):
            Specifies the scope of the config (e.g.,
            SUBNET, NETWORK, ORGANIZATION..).

            This field is a member of `oneof`_ ``_scope``.
    """

    class Scope(proto.Enum):
        r"""The scope for this flow log configuration.

        Values:
            SCOPE_UNSPECIFIED (0):
                Scope is unspecified.
            SUBNET (1):
                Target resource is a subnet (Network
                Management API).
            COMPUTE_API_SUBNET (2):
                Target resource is a subnet, and the config
                originates from the Compute API.
            NETWORK (3):
                Target resource is a network.
            VPN_TUNNEL (4):
                Target resource is a VPN tunnel.
            INTERCONNECT_ATTACHMENT (5):
                Target resource is an interconnect
                attachment.
            ORGANIZATION (6):
                Configuration applies to an entire
                organization.
        """

        SCOPE_UNSPECIFIED = 0
        SUBNET = 1
        COMPUTE_API_SUBNET = 2
        NETWORK = 3
        VPN_TUNNEL = 4
        INTERCONNECT_ATTACHMENT = 5
        ORGANIZATION = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: "VpcFlowLogsConfig.State" = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum="VpcFlowLogsConfig.State",
    )
    aggregation_interval: "VpcFlowLogsConfig.AggregationInterval" = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum="VpcFlowLogsConfig.AggregationInterval",
    )
    flow_sampling: float = proto.Field(
        proto.FLOAT,
        number=5,
        optional=True,
    )
    metadata: "VpcFlowLogsConfig.Metadata" = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum="VpcFlowLogsConfig.Metadata",
    )
    metadata_fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    filter_expr: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    cross_project_metadata: "VpcFlowLogsConfig.CrossProjectMetadata" = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum="VpcFlowLogsConfig.CrossProjectMetadata",
    )
    network: str = proto.Field(
        proto.STRING,
        number=100,
        oneof="target_resource",
    )
    subnet: str = proto.Field(
        proto.STRING,
        number=101,
        oneof="target_resource",
    )
    interconnect_attachment: str = proto.Field(
        proto.STRING,
        number=102,
        oneof="target_resource",
    )
    vpn_tunnel: str = proto.Field(
        proto.STRING,
        number=103,
        oneof="target_resource",
    )
    scope: Scope = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum=Scope,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
