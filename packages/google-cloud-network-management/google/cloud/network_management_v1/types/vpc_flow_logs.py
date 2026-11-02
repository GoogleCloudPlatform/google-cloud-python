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
import proto  # type: ignore

from google.cloud.network_management_v1.types import (
    vpc_flow_logs_config as gcn_vpc_flow_logs_config,
)

__protobuf__ = proto.module(
    package="google.cloud.networkmanagement.v1",
    manifest={
        "ListVpcFlowLogsConfigsRequest",
        "ListVpcFlowLogsConfigsResponse",
        "GetVpcFlowLogsConfigRequest",
        "CreateVpcFlowLogsConfigRequest",
        "UpdateVpcFlowLogsConfigRequest",
        "DeleteVpcFlowLogsConfigRequest",
        "QueryOrgVpcFlowLogsConfigsRequest",
        "QueryOrgVpcFlowLogsConfigsResponse",
        "ShowEffectiveFlowLogsConfigsRequest",
        "ShowEffectiveFlowLogsConfigsResponse",
    },
)


class ListVpcFlowLogsConfigsRequest(proto.Message):
    r"""Request for the ``ListVpcFlowLogsConfigs`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the VpcFlowLogsConfig, in
            one of the following formats:

            - For project-level resources:
              ``projects/{project_id}/locations/global``

            - For organization-level resources:
              ``organizations/{organization_id}/locations/global``
        page_size (int):
            Optional. Number of ``VpcFlowLogsConfigs`` to return.
        page_token (str):
            Optional. Page token from an earlier query, as returned in
            ``next_page_token``.
        filter (str):
            Optional. Lists the ``VpcFlowLogsConfigs`` that match the
            filter expression. A filter expression must use the
            supported [CEL logic operators]
            (https://cloud.google.com/vpc/docs/about-flow-logs-records#supported_cel_logic_operators).
        order_by (str):
            Optional. Field to use to sort the list.
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


class ListVpcFlowLogsConfigsResponse(proto.Message):
    r"""Response for the ``ListVpcFlowLogsConfigs`` method.

    Attributes:
        vpc_flow_logs_configs (MutableSequence[google.cloud.network_management_v1.types.VpcFlowLogsConfig]):
            List of VPC Flow Log configurations.
        next_page_token (str):
            Page token to fetch the next set of
            configurations.
        unreachable (MutableSequence[str]):
            Locations that could not be reached (when querying all
            locations with ``-``).
    """

    @property
    def raw_page(self):
        return self

    vpc_flow_logs_configs: MutableSequence[
        gcn_vpc_flow_logs_config.VpcFlowLogsConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_vpc_flow_logs_config.VpcFlowLogsConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetVpcFlowLogsConfigRequest(proto.Message):
    r"""Request for the ``GetVpcFlowLogsConfig`` method.

    Attributes:
        name (str):
            Required. The resource name of the VpcFlowLogsConfig, in one
            of the following formats:

            - For project-level resources:
              ``projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}``

            - For organization-level resources:
              ``organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateVpcFlowLogsConfigRequest(proto.Message):
    r"""Request for the ``CreateVpcFlowLogsConfig`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the VpcFlowLogsConfig to
            create, in one of the following formats:

            - For project-level resources:
              ``projects/{project_id}/locations/global``

            - For organization-level resources:
              ``organizations/{organization_id}/locations/global``
        vpc_flow_logs_config_id (str):
            Required. ID of the ``VpcFlowLogsConfig``.
        vpc_flow_logs_config (google.cloud.network_management_v1.types.VpcFlowLogsConfig):
            Required. A ``VpcFlowLogsConfig`` resource
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vpc_flow_logs_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vpc_flow_logs_config: gcn_vpc_flow_logs_config.VpcFlowLogsConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcn_vpc_flow_logs_config.VpcFlowLogsConfig,
    )


class UpdateVpcFlowLogsConfigRequest(proto.Message):
    r"""Request for the ``UpdateVpcFlowLogsConfig`` method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. For example, to change the state
            of the configuration to ENABLED, specify ``update_mask`` =
            ``"state"``, and the ``vpc_flow_logs_config`` would be:
            ``vpc_flow_logs_config = { name = "projects/my-project/locations/global/vpcFlowLogsConfigs/my-config" state = "ENABLED" }``
        vpc_flow_logs_config (google.cloud.network_management_v1.types.VpcFlowLogsConfig):
            Required. Only fields specified in update_mask are updated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    vpc_flow_logs_config: gcn_vpc_flow_logs_config.VpcFlowLogsConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcn_vpc_flow_logs_config.VpcFlowLogsConfig,
    )


class DeleteVpcFlowLogsConfigRequest(proto.Message):
    r"""Request for the ``DeleteVpcFlowLogsConfig`` method.

    Attributes:
        name (str):
            Required. The resource name of the VpcFlowLogsConfig, in one
            of the following formats:

            - For a project-level resource:
              ``projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}``

            - For an organization-level resource:
              ``organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class QueryOrgVpcFlowLogsConfigsRequest(proto.Message):
    r"""Request for the ``QueryOrgVpcFlowLogsConfigs`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the VpcFlowLogsConfig,
            specified in the following format:
            ``projects/{project_id}/locations/global``
        page_size (int):
            Optional. Number of ``VpcFlowLogsConfigs`` to return.
        page_token (str):
            Optional. Page token from an earlier query, as returned in
            ``next_page_token``.
        filter (str):
            Optional. Lists the ``VpcFlowLogsConfigs`` that match the
            filter expression. A filter expression must use the
            supported [CEL logic operators]
            (https://cloud.google.com/vpc/docs/about-flow-logs-records#supported_cel_logic_operators).
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


class QueryOrgVpcFlowLogsConfigsResponse(proto.Message):
    r"""Response for the ``QueryVpcFlowLogsConfigs`` method.

    Attributes:
        vpc_flow_logs_configs (MutableSequence[google.cloud.network_management_v1.types.VpcFlowLogsConfig]):
            List of VPC Flow Log configurations.
        next_page_token (str):
            Page token to fetch the next set of
            configurations.
        unreachable (MutableSequence[str]):
            Locations that could not be reached (when querying all
            locations with ``-``).
    """

    @property
    def raw_page(self):
        return self

    vpc_flow_logs_configs: MutableSequence[
        gcn_vpc_flow_logs_config.VpcFlowLogsConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_vpc_flow_logs_config.VpcFlowLogsConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ShowEffectiveFlowLogsConfigsRequest(proto.Message):
    r"""Request for the ``ShowEffectiveFlowLogsConfigs`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the VpcFlowLogsConfig,
            specified in the following format:
            ``projects/{project_id}/locations/global``
        resource (str):
            Required. The resource to get the effective
            VPC Flow Logs configuration for. The resource
            must belong to the same project as the parent.
            The resource must be a network, subnetwork,
            interconnect attachment, VPN tunnel, or a
            project.
        page_size (int):
            Optional. Number of ``EffectiveVpcFlowLogsConfigs`` to
            return. Default is 30.
        page_token (str):
            Optional. Page token from an earlier query, as returned in
            ``next_page_token``.
        filter (str):
            Optional. Lists the ``EffectiveVpcFlowLogsConfigs`` that
            match the filter expression. A filter expression must use
            the supported [CEL logic operators]
            (https://cloud.google.com/vpc/docs/about-flow-logs-records#supported_cel_logic_operators).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource: str = proto.Field(
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


class ShowEffectiveFlowLogsConfigsResponse(proto.Message):
    r"""Response for the ``ShowEffectiveFlowLogsConfigs`` method.

    Attributes:
        effective_flow_logs_configs (MutableSequence[google.cloud.network_management_v1.types.EffectiveVpcFlowLogsConfig]):
            List of Effective Vpc Flow Logs
            configurations.
        next_page_token (str):
            Page token to fetch the next set of
            configurations.
        unreachable (MutableSequence[str]):
            Locations that could not be reached (when querying all
            locations with ``-``).
    """

    @property
    def raw_page(self):
        return self

    effective_flow_logs_configs: MutableSequence[
        gcn_vpc_flow_logs_config.EffectiveVpcFlowLogsConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcn_vpc_flow_logs_config.EffectiveVpcFlowLogsConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
