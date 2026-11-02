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
    package="google.cloud.networksecurity.v1alpha1",
    manifest={
        "GatewaySecurityPolicy",
        "CreateGatewaySecurityPolicyRequest",
        "ListGatewaySecurityPoliciesRequest",
        "ListGatewaySecurityPoliciesResponse",
        "GetGatewaySecurityPolicyRequest",
        "DeleteGatewaySecurityPolicyRequest",
        "UpdateGatewaySecurityPolicyRequest",
    },
)


class GatewaySecurityPolicy(proto.Message):
    r"""The GatewaySecurityPolicy resource contains a collection of
    GatewaySecurityPolicyRules and associated metadata.

    Attributes:
        name (str):
            Required. Name of the resource. Name is of the form
            projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}
            gateway_security_policy should match the
            pattern:(^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        description (str):
            Optional. Free-text description of the
            resource.
        tls_inspection_policy (str):
            Optional. Name of a TLS Inspection Policy
            resource that defines how TLS inspection will be
            performed for any rule(s) which enables it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    tls_inspection_policy: str = proto.Field(
        proto.STRING,
        number=5,
    )


class CreateGatewaySecurityPolicyRequest(proto.Message):
    r"""Request used by the CreateGatewaySecurityPolicy method.

    Attributes:
        parent (str):
            Required. The parent resource of the GatewaySecurityPolicy.
            Must be in the format
            ``projects/{project}/locations/{location}``.
        gateway_security_policy_id (str):
            Required. Short name of the GatewaySecurityPolicy resource
            to be created. This value should be 1-63 characters long,
            containing only letters, numbers, hyphens, and underscores,
            and should not start with a number. E.g.
            "gateway_security_policy1".
        gateway_security_policy (google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicy):
            Required. GatewaySecurityPolicy resource to
            be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gateway_security_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gateway_security_policy: "GatewaySecurityPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GatewaySecurityPolicy",
    )


class ListGatewaySecurityPoliciesRequest(proto.Message):
    r"""Request used with the ListGatewaySecurityPolicies method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            GatewaySecurityPolicies should be listed, specified in the
            format ``projects/{project}/locations/{location}``.
        page_size (int):
            Maximum number of GatewaySecurityPolicies to
            return per call.
        page_token (str):
            The value returned by the last
            'ListGatewaySecurityPoliciesResponse' Indicates
            that this is a continuation of a prior
            'ListGatewaySecurityPolicies' call, and that the
            system should return the next page of data.
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


class ListGatewaySecurityPoliciesResponse(proto.Message):
    r"""Response returned by the ListGatewaySecurityPolicies method.

    Attributes:
        gateway_security_policies (MutableSequence[google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicy]):
            List of GatewaySecurityPolicies resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then 'next_page_token' is included. To get the
            next set of results, call this method again using the value
            of 'next_page_token' as 'page_token'.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    gateway_security_policies: MutableSequence["GatewaySecurityPolicy"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="GatewaySecurityPolicy",
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


class GetGatewaySecurityPolicyRequest(proto.Message):
    r"""Request used by the GetGatewaySecurityPolicy method.

    Attributes:
        name (str):
            Required. A name of the GatewaySecurityPolicy to get. Must
            be in the format
            ``projects/{project}/locations/{location}/gatewaySecurityPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteGatewaySecurityPolicyRequest(proto.Message):
    r"""Request used by the DeleteGatewaySecurityPolicy method.

    Attributes:
        name (str):
            Required. A name of the GatewaySecurityPolicy to delete.
            Must be in the format
            ``projects/{project}/locations/{location}/gatewaySecurityPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateGatewaySecurityPolicyRequest(proto.Message):
    r"""Request used by the UpdateGatewaySecurityPolicy method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the GatewaySecurityPolicy resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        gateway_security_policy (google.cloud.network_security_v1alpha1.types.GatewaySecurityPolicy):
            Required. Updated GatewaySecurityPolicy
            resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    gateway_security_policy: "GatewaySecurityPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GatewaySecurityPolicy",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
