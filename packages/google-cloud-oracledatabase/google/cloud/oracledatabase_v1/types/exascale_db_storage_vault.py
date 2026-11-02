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
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "ExascaleDbStorageVault",
        "ExascaleDbStorageVaultProperties",
        "ExascaleDbStorageDetails",
        "GetExascaleDbStorageVaultRequest",
        "ListExascaleDbStorageVaultsRequest",
        "ListExascaleDbStorageVaultsResponse",
        "CreateExascaleDbStorageVaultRequest",
        "DeleteExascaleDbStorageVaultRequest",
    },
)


class ExascaleDbStorageVault(proto.Message):
    r"""ExascaleDbStorageVault represents a storage vault exadb vm
    cluster resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExascaleDbStorageVault/

    Attributes:
        name (str):
            Identifier. The resource name of the ExascaleDbStorageVault.
            Format:
            projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}
        display_name (str):
            Required. The display name for the
            ExascaleDbStorageVault. The name does not have
            to be unique within your project. The name must
            be 1-255 characters long and can only contain
            alphanumeric characters.
        gcp_oracle_zone (str):
            Optional. The GCP Oracle zone where Oracle
            ExascaleDbStorageVault is hosted. Example:
            us-east4-b-r2. If not specified, the system will
            pick a zone based on availability.
        properties (google.cloud.oracledatabase_v1.types.ExascaleDbStorageVaultProperties):
            Required. The properties of the
            ExascaleDbStorageVault.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time when the
            ExascaleDbStorageVault was created.
        entitlement_id (str):
            Output only. The ID of the subscription
            entitlement associated with the
            ExascaleDbStorageVault.
        labels (MutableMapping[str, str]):
            Optional. The labels or tags associated with
            the ExascaleDbStorageVault.
        exadata_infrastructure (str):
            Optional. The Exadata Infrastructure resource on which
            ExascaleDbStorageVault resource is created, in the following
            format:
            projects/{project}/locations/{region}/cloudExadataInfrastuctures/{cloud_extradata_infrastructure}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gcp_oracle_zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    properties: "ExascaleDbStorageVaultProperties" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ExascaleDbStorageVaultProperties",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    exadata_infrastructure: str = proto.Field(
        proto.STRING,
        number=8,
    )


class ExascaleDbStorageVaultProperties(proto.Message):
    r"""The properties of the ExascaleDbStorageVault.
    next ID: 12

    Attributes:
        ocid (str):
            Output only. The OCID for the
            ExascaleDbStorageVault.
        time_zone (google.type.datetime_pb2.TimeZone):
            Output only. The time zone of the
            ExascaleDbStorageVault.
        exascale_db_storage_details (google.cloud.oracledatabase_v1.types.ExascaleDbStorageDetails):
            Required. The storage details of the
            ExascaleDbStorageVault.
        state (google.cloud.oracledatabase_v1.types.ExascaleDbStorageVaultProperties.State):
            Output only. The state of the
            ExascaleDbStorageVault.
        description (str):
            Optional. The description of the
            ExascaleDbStorageVault.
        vm_cluster_ids (MutableSequence[str]):
            Output only. The list of VM cluster OCIDs
            associated with the ExascaleDbStorageVault.
        vm_cluster_count (int):
            Output only. The number of VM clusters
            associated with the ExascaleDbStorageVault.
        additional_flash_cache_percent (int):
            Optional. The size of additional flash cache
            in percentage of high capacity database storage.
        oci_uri (str):
            Output only. Deep link to the OCI console to
            view this resource.
        attached_shape_attributes (MutableSequence[google.cloud.oracledatabase_v1.types.ExascaleDbStorageVaultProperties.ShapeAttribute]):
            Output only. The shape attributes of the VM
            clusters attached to the ExascaleDbStorageVault.
        available_shape_attributes (MutableSequence[google.cloud.oracledatabase_v1.types.ExascaleDbStorageVaultProperties.ShapeAttribute]):
            Output only. The shape attributes available
            for the VM clusters to be attached to the
            ExascaleDbStorageVault.
    """

    class State(proto.Enum):
        r"""The state of the ExascaleDbStorageVault.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the ExascaleDbStorageVault is
                unspecified.
            PROVISIONING (1):
                The ExascaleDbStorageVault is being
                provisioned.
            AVAILABLE (2):
                The ExascaleDbStorageVault is available.
            UPDATING (3):
                The ExascaleDbStorageVault is being updated.
            TERMINATING (4):
                The ExascaleDbStorageVault is being deleted.
            TERMINATED (5):
                The ExascaleDbStorageVault has been deleted.
            FAILED (6):
                The ExascaleDbStorageVault has failed.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        UPDATING = 3
        TERMINATING = 4
        TERMINATED = 5
        FAILED = 6

    class ShapeAttribute(proto.Enum):
        r"""The shape attribute of the VM clusters attached to the
        ExascaleDbStorageVault.

        Values:
            SHAPE_ATTRIBUTE_UNSPECIFIED (0):
                Default unspecified value.
            SMART_STORAGE (1):
                Indicates that the resource is in smart
                storage.
            BLOCK_STORAGE (2):
                Indicates that the resource is in block
                storage.
        """

        SHAPE_ATTRIBUTE_UNSPECIFIED = 0
        SMART_STORAGE = 1
        BLOCK_STORAGE = 2

    ocid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    time_zone: datetime_pb2.TimeZone = proto.Field(
        proto.MESSAGE,
        number=2,
        message=datetime_pb2.TimeZone,
    )
    exascale_db_storage_details: "ExascaleDbStorageDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ExascaleDbStorageDetails",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    vm_cluster_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    vm_cluster_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    additional_flash_cache_percent: int = proto.Field(
        proto.INT32,
        number=7,
    )
    oci_uri: str = proto.Field(
        proto.STRING,
        number=8,
    )
    attached_shape_attributes: MutableSequence[ShapeAttribute] = proto.RepeatedField(
        proto.ENUM,
        number=10,
        enum=ShapeAttribute,
    )
    available_shape_attributes: MutableSequence[ShapeAttribute] = proto.RepeatedField(
        proto.ENUM,
        number=11,
        enum=ShapeAttribute,
    )


class ExascaleDbStorageDetails(proto.Message):
    r"""The storage details of the ExascaleDbStorageVault.

    Attributes:
        available_size_gbs (int):
            Output only. The available storage capacity
            for the ExascaleDbStorageVault, in gigabytes
            (GB).
        total_size_gbs (int):
            Required. The total storage allocation for
            the ExascaleDbStorageVault, in gigabytes (GB).
    """

    available_size_gbs: int = proto.Field(
        proto.INT32,
        number=1,
    )
    total_size_gbs: int = proto.Field(
        proto.INT32,
        number=2,
    )


class GetExascaleDbStorageVaultRequest(proto.Message):
    r"""The request for ``ExascaleDbStorageVault.Get``.

    Attributes:
        name (str):
            Required. The name of the ExascaleDbStorageVault in the
            following format:
            projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListExascaleDbStorageVaultsRequest(proto.Message):
    r"""The request for ``ExascaleDbStorageVault.List``.

    Attributes:
        parent (str):
            Required. The parent value for
            ExascaleDbStorageVault in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50
            ExascaleDbStorageVaults will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the
            results of the request. Filter the list as
            specified in https://google.aip.dev/160.
        order_by (str):
            Optional. An expression for ordering the
            results of the request. Order results as
            specified in https://google.aip.dev/132.
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


class ListExascaleDbStorageVaultsResponse(proto.Message):
    r"""The response for ``ExascaleDbStorageVault.List``.

    Attributes:
        exascale_db_storage_vaults (MutableSequence[google.cloud.oracledatabase_v1.types.ExascaleDbStorageVault]):
            The ExascaleDbStorageVaults.
        next_page_token (str):
            A token identifying a page of results the
            server should return. If present, the next page
            token can be provided to a subsequent
            ListExascaleDbStorageVaults call to list the
            next page. If empty, there are no more pages.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    exascale_db_storage_vaults: MutableSequence["ExascaleDbStorageVault"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ExascaleDbStorageVault",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateExascaleDbStorageVaultRequest(proto.Message):
    r"""The request for ``ExascaleDbStorageVault.Create``.

    Attributes:
        parent (str):
            Required. The value for parent of the
            ExascaleDbStorageVault in the following format:
            projects/{project}/locations/{location}.
        exascale_db_storage_vault_id (str):
            Required. The ID of the ExascaleDbStorageVault to create.
            This value is restricted to
            (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
            maximum of 63 characters in length. The value must start
            with a letter and end with a letter or a number.
        exascale_db_storage_vault (google.cloud.oracledatabase_v1.types.ExascaleDbStorageVault):
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
    exascale_db_storage_vault_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    exascale_db_storage_vault: "ExascaleDbStorageVault" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ExascaleDbStorageVault",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteExascaleDbStorageVaultRequest(proto.Message):
    r"""The request message for ``ExascaleDbStorageVault.Delete``.

    Attributes:
        name (str):
            Required. The name of the ExascaleDbStorageVault in the
            following format:
            projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}.
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


__all__ = tuple(sorted(__protobuf__.manifest))
