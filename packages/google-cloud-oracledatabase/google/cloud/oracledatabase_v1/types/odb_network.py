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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "OdbNetwork",
        "CreateOdbNetworkRequest",
        "DeleteOdbNetworkRequest",
        "UpdateOdbNetworkRequest",
        "ListOdbNetworksRequest",
        "ListOdbNetworksResponse",
        "GetOdbNetworkRequest",
        "PscInterfaceConfig",
        "ServiceConnectivityConfig",
    },
)


class OdbNetwork(proto.Message):
    r"""Represents OdbNetwork resource.

    Attributes:
        name (str):
            Identifier. The name of the OdbNetwork resource in the
            following format:
            projects/{project}/locations/{region}/odbNetworks/{odb_network}
        network (str):
            Required. Immutable. The name of the VPC
            network in the following format:
            projects/{project}/global/networks/{network}
        labels (MutableMapping[str, str]):
            Optional. Labels or tags associated with the
            resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            OdbNetwork was created.
        state (google.cloud.oracledatabase_v1.types.OdbNetwork.State):
            Output only. State of the ODB Network.
        entitlement_id (str):
            Output only. The ID of the subscription
            entitlement associated with the OdbNetwork.
        gcp_oracle_zone (str):
            Optional. Immutable. The GCP Oracle zone
            where OdbNetwork is hosted. Example:
            us-east4-b-r2. If not specified, the system will
            pick a zone based on availability.
        service_connectivity_config (google.cloud.oracledatabase_v1.types.ServiceConnectivityConfig):
            Optional. Configuration to enable the service
            (Oracledatabase@Google Cloud) to establish connectivity to
            the database.

            This should be specified if you intend to associate this
            OdbNetwork with a DatabaseConnection resource to
            ``ExecuteSQL`` on the database, or to create a
            ServiceIntegration with the Database.

            Please don't specify it otherwise to avoid complicating the
            network setup.
        reconciling (bool):
            Output only. Indicates whether the OdbNetwork
            is currently reconciling changes.
    """

    class State(proto.Enum):
        r"""The various lifecycle states of the ODB Network.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified value.
            PROVISIONING (1):
                Indicates that the resource is in
                provisioning state.
            AVAILABLE (2):
                Indicates that the resource is in available
                state.
            TERMINATING (3):
                Indicates that the resource is in terminating
                state.
            FAILED (4):
                Indicates that the resource is in failed
                state.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        TERMINATING = 3
        FAILED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    network: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    gcp_oracle_zone: str = proto.Field(
        proto.STRING,
        number=7,
    )
    service_connectivity_config: "ServiceConnectivityConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="ServiceConnectivityConfig",
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class CreateOdbNetworkRequest(proto.Message):
    r"""The request for ``OdbNetwork.Create``.

    Attributes:
        parent (str):
            Required. The parent value for the OdbNetwork
            in the following format:
            projects/{project}/locations/{location}.
        odb_network_id (str):
            Required. The ID of the OdbNetwork to create. This value is
            restricted to (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and
            must be a maximum of 63 characters in length. The value must
            start with a letter and end with a letter or a number.
        odb_network (google.cloud.oracledatabase_v1.types.OdbNetwork):
            Required. Details of the OdbNetwork instance
            to create.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    odb_network_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    odb_network: "OdbNetwork" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OdbNetwork",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteOdbNetworkRequest(proto.Message):
    r"""The request for ``OdbNetwork.Delete``.

    Attributes:
        name (str):
            Required. The name of the resource in the following format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

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


class UpdateOdbNetworkRequest(proto.Message):
    r"""The request for ``OdbNetwork.Update``.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A mask specifying which fields in the OdbNetwork
            should be updated. A field specified in the mask is updated.
            If a mask isn't provided, the service treats this as an
            implied field mask equivalent to all fields that are
            populated (have a non-empty value). To clear or unset a
            field, the field must be explicitly specified in the
            ``update_mask``.
        odb_network (google.cloud.oracledatabase_v1.types.OdbNetwork):
            Required. The resource being updated. Note only ``labels``
            and ``service_connectivity_config`` can be updated. The
            provided labels will completely replace the existing labels.
            Any existing label keys that are not included in the update
            request will be deleted. Not providing labels and
            update_mask will not update the labels. To clear all labels,
            specify ``labels`` in the ``update_mask`` and omit or leave
            the ``labels`` field empty in the update request.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    odb_network: "OdbNetwork" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OdbNetwork",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListOdbNetworksRequest(proto.Message):
    r"""The request for ``OdbNetwork.List``.

    Attributes:
        parent (str):
            Required. The parent value for the ODB
            Network in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 ODB Networks
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
        order_by (str):
            Optional. An expression for ordering the
            results of the request.
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


class ListOdbNetworksResponse(proto.Message):
    r"""The response for ``OdbNetwork.List``.

    Attributes:
        odb_networks (MutableSequence[google.cloud.oracledatabase_v1.types.OdbNetwork]):
            The list of ODB Networks.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    odb_networks: MutableSequence["OdbNetwork"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OdbNetwork",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetOdbNetworkRequest(proto.Message):
    r"""The request for ``OdbNetwork.Get``.

    Attributes:
        name (str):
            Required. The name of the OdbNetwork in the following
            format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PscInterfaceConfig(proto.Message):
    r"""Configuration for a Private Service Connect (PSC) interface
    used by Oracledatabase@Google Cloud to establish private
    connectivity to the database.

    Attributes:
        network_attachment (str):
            Optional. The resource name of the Network Attachment that
            Oracledatabase@Google Cloud will use to establish private
            connectivity to the database via a Private Service Connect
            Interface (PSC-I). Format:
            projects/{project}/regions/{region}/networkAttachments/{network_attachment}
    """

    network_attachment: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ServiceConnectivityConfig(proto.Message):
    r"""Configuration to enable the service (Oracledatabase@Google Cloud) to
    establish connectivity to the database.

    This should be specified if you intend to associate this OdbNetwork
    with a DatabaseConnection resource to ``ExecuteSQL`` on the
    database, or to create a ServiceIntegration with the Database.

    Please don't specify it otherwise to avoid complicating the network
    setup.

    Attributes:
        psc_interface_config (google.cloud.oracledatabase_v1.types.PscInterfaceConfig):
            Optional. Configuration for Private Service
            Connect (PSC) interface.
    """

    psc_interface_config: "PscInterfaceConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PscInterfaceConfig",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
