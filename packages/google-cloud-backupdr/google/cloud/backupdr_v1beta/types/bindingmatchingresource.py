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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1beta",
    manifest={
        "GetBindingMatchingResourceRequest",
        "ListBindingMatchingResourcesRequest",
        "ListBindingMatchingResourcesResponse",
        "BindingMatchingResource",
        "AutoProtectionDetails",
    },
)


class GetBindingMatchingResourceRequest(proto.Message):
    r"""Request message for getting a BindingMatchingResource.

    Attributes:
        name (str):
            Required. The name of the matching resource to retrieve.
            Format:
            projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBindingMatchingResourcesRequest(proto.Message):
    r"""Request message for List BindingMatchingResources.

    Attributes:
        parent (str):
            Required. The project, location, auto protection policy and
            binding for which to retrieve ``BindingMatchingResources``
            information. Format:
            ``projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}``.
            In Google Cloud Backup and DR, locations map to Google Cloud
            regions, for example **us-central1**.
        page_size (int):
            Optional. The maximum number of ``BindingMatchingResources``
            to return in a single response. The default page size is 100
            and maximum page size is 200. Note that the response may
            include a partial list and a caller should only rely on the
            response's
            [next_page_token][google.cloud.backupdr.v1beta.ListBindingMatchingResourcesResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.backupdr.v1beta.ListBindingMatchingResourcesResponse.next_page_token]
            received from a previous ``ListBindingMatchingResources``
            call. Provide this to retrieve the subsequent page in a
            multi-page list of results. When paginating, all other
            parameters provided to ``ListBindingMatchingResources`` must
            match the call that provided the page token.
        filter (str):
            Optional. Field match expression used to
            filter the results.
        order_by (str):
            Optional. Field by which to sort the results.
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


class ListBindingMatchingResourcesResponse(proto.Message):
    r"""The response message for getting a list of
    ``BindingMatchingResources``.

    Attributes:
        matching_resources (MutableSequence[google.cloud.backupdr_v1beta.types.BindingMatchingResource]):
            The list of ``BindingMatchingResources`` in the
            project,location for the specified binding.
        next_page_token (str):
            A token which may be sent as
            [page_token][google.cloud.backupdr.v1beta.ListBindingMatchingResourcesRequest.page_token]
            in a subsequent ``ListBindingMatchingResources`` call to
            retrieve the next page of results. If this field is omitted
            or empty, then there are no more results to return.
    """

    @property
    def raw_page(self):
        return self

    matching_resources: MutableSequence["BindingMatchingResource"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="BindingMatchingResource",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BindingMatchingResource(proto.Message):
    r"""BindingMatchingResource contains the details of a resource
    that matches the criteria of a binding.

    Attributes:
        name (str):
            Identifier. The resource name of the
            ``BindingMatchingResource``. Format:
            ``projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}``
        resource (str):
            Required. Immutable. Resource name of the workload that
            matches the criteria of the binding.

            The format can be either a relative resource name (e.g.,
            ``projects/my-project/zones/us-central1-a/instances/my-instance``)
            or a schemeless full resource name (e.g.,
            ``//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance``).
        last_evaluation_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was last evaluated for protection.
        auto_protection_details (google.cloud.backupdr_v1beta.types.AutoProtectionDetails):
            Output only. The auto protection details of
            the resource from the current binding's
            perspective.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=2,
    )
    last_evaluation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    auto_protection_details: "AutoProtectionDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AutoProtectionDetails",
    )


class AutoProtectionDetails(proto.Message):
    r"""AutoProtectionDetails contains the protection details of a
    resource from the current binding's perspective.

    Attributes:
        state (google.cloud.backupdr_v1beta.types.AutoProtectionDetails.State):
            Output only. Protection state of the resource
            from the current binding's perspective. Output
            only.
        backup_plan_association (str):
            Output only. Resource name of backup plan
            association linked to the resource, if any.
            Format:

            projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}
        data_source (str):
            Output only. Resource name of the datasource
            linked to the resource, if any. Format:

            projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{dataSourceId}
        error (google.rpc.status_pb2.Status):
            Output only. Error during last sync for
            protection/unprotection, if any.
    """

    class State(proto.Enum):
        r"""Enum for protection state of the resource.

        Values:
            STATE_UNSPECIFIED (0):
                State unspecified.
            PROTECTED (1):
                Resource is protected.
            PROTECTION_FAILED (2):
                Resource protection failed.
            UNPROTECTING (3):
                Resource is being unprotected.
            UNPROTECTION_FAILED (4):
                Resource unprotection failed.
        """

        STATE_UNSPECIFIED = 0
        PROTECTED = 1
        PROTECTION_FAILED = 2
        UNPROTECTING = 3
        UNPROTECTION_FAILED = 4

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    backup_plan_association: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=3,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
