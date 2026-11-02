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

from google.cloud.network_services_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.networkservices.v1",
    manifest={
        "EndpointPolicy",
        "ListEndpointPoliciesRequest",
        "ListEndpointPoliciesResponse",
        "GetEndpointPolicyRequest",
        "CreateEndpointPolicyRequest",
        "UpdateEndpointPolicyRequest",
        "DeleteEndpointPolicyRequest",
    },
)


class EndpointPolicy(proto.Message):
    r"""EndpointPolicy is a resource that helps apply desired
    configuration on the endpoints that match specific criteria. For
    example, this resource can be used to apply "authentication
    config" an all endpoints that serve on port 8080.

    Attributes:
        name (str):
            Identifier. Name of the EndpointPolicy resource. It matches
            pattern
            ``projects/{project}/locations/*/endpointPolicies/{endpoint_policy}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the EndpointPolicy resource.
        type_ (google.cloud.network_services_v1.types.EndpointPolicy.EndpointPolicyType):
            Required. The type of endpoint policy. This
            is primarily used to validate the configuration.
        authorization_policy (str):
            Optional. This field specifies the URL of
            AuthorizationPolicy resource that applies
            authorization policies to the inbound traffic at
            the matched endpoints. Refer to Authorization.
            If this field is not specified, authorization is
            disabled(no authz checks) for this endpoint.
        endpoint_matcher (google.cloud.network_services_v1.types.EndpointMatcher):
            Required. A matcher that selects endpoints to
            which the policies should be applied.
        traffic_port_selector (google.cloud.network_services_v1.types.TrafficPortSelector):
            Optional. Port selector for the (matched)
            endpoints. If no port selector is provided, the
            matched config is applied to all ports.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        server_tls_policy (str):
            Optional. A URL referring to ServerTlsPolicy
            resource. ServerTlsPolicy is used to determine
            the authentication policy to be applied to
            terminate the inbound traffic at the identified
            backends. If this field is not set,
            authentication is disabled(open) for this
            endpoint.
        client_tls_policy (str):
            Optional. Deprecated: This field is not used and is a no-op.
            A URL referring to a ClientTlsPolicy resource.
            ClientTlsPolicy can be set to specify the authentication for
            traffic from the proxy to the actual endpoints. More
            specifically, it is applied to the outgoing traffic from the
            proxy to the endpoint. This is typically used for sidecar
            model where the proxy identifies itself as endpoint to the
            control plane, with the connection between sidecar and
            endpoint requiring authentication. If this field is not set,
            authentication is disabled(open). Applicable only when
            EndpointPolicyType is SIDECAR_PROXY.
    """

    class EndpointPolicyType(proto.Enum):
        r"""The type of endpoint policy.

        Values:
            ENDPOINT_POLICY_TYPE_UNSPECIFIED (0):
                Default value. Must not be used.
            SIDECAR_PROXY (1):
                Represents a proxy deployed as a sidecar.
            GRPC_SERVER (2):
                Represents a proxyless gRPC backend.
        """

        ENDPOINT_POLICY_TYPE_UNSPECIFIED = 0
        SIDECAR_PROXY = 1
        GRPC_SERVER = 2

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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    type_: EndpointPolicyType = proto.Field(
        proto.ENUM,
        number=5,
        enum=EndpointPolicyType,
    )
    authorization_policy: str = proto.Field(
        proto.STRING,
        number=7,
    )
    endpoint_matcher: common.EndpointMatcher = proto.Field(
        proto.MESSAGE,
        number=9,
        message=common.EndpointMatcher,
    )
    traffic_port_selector: common.TrafficPortSelector = proto.Field(
        proto.MESSAGE,
        number=10,
        message=common.TrafficPortSelector,
    )
    description: str = proto.Field(
        proto.STRING,
        number=11,
    )
    server_tls_policy: str = proto.Field(
        proto.STRING,
        number=12,
    )
    client_tls_policy: str = proto.Field(
        proto.STRING,
        number=13,
    )


class ListEndpointPoliciesRequest(proto.Message):
    r"""Request used with the ListEndpointPolicies method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            EndpointPolicies should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Maximum number of EndpointPolicies to return
            per call.
        page_token (str):
            The value returned by the last
            ``ListEndpointPoliciesResponse`` Indicates that this is a
            continuation of a prior ``ListEndpointPolicies`` call, and
            that the system should return the next page of data.
        return_partial_success (bool):
            Optional. If true, allow partial responses
            for multi-regional Aggregated List requests.
            Otherwise if one of the locations is down or
            unreachable, the Aggregated List request will
            fail.
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
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListEndpointPoliciesResponse(proto.Message):
    r"""Response returned by the ListEndpointPolicies method.

    Attributes:
        endpoint_policies (MutableSequence[google.cloud.network_services_v1.types.EndpointPolicy]):
            List of EndpointPolicy resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the request opts into
            [return_partial_success][google.cloud.networkservices.v1.ListEndpointPoliciesRequest.return_partial_success]
            and reading across collections e.g. when attempting to list
            all resources across all supported locations.
    """

    @property
    def raw_page(self):
        return self

    endpoint_policies: MutableSequence["EndpointPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EndpointPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEndpointPolicyRequest(proto.Message):
    r"""Request used with the GetEndpointPolicy method.

    Attributes:
        name (str):
            Required. A name of the EndpointPolicy to get. Must be in
            the format ``projects/*/locations/*/endpointPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEndpointPolicyRequest(proto.Message):
    r"""Request used with the CreateEndpointPolicy method.

    Attributes:
        parent (str):
            Required. The parent resource of the EndpointPolicy. Must be
            in the format ``projects/*/locations/*``.
        endpoint_policy_id (str):
            Required. Short name of the EndpointPolicy
            resource to be created. E.g. "CustomECS".
        endpoint_policy (google.cloud.network_services_v1.types.EndpointPolicy):
            Required. EndpointPolicy resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    endpoint_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    endpoint_policy: "EndpointPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EndpointPolicy",
    )


class UpdateEndpointPolicyRequest(proto.Message):
    r"""Request used with the UpdateEndpointPolicy method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the EndpointPolicy resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        endpoint_policy (google.cloud.network_services_v1.types.EndpointPolicy):
            Required. Updated EndpointPolicy resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    endpoint_policy: "EndpointPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EndpointPolicy",
    )


class DeleteEndpointPolicyRequest(proto.Message):
    r"""Request used with the DeleteEndpointPolicy method.

    Attributes:
        name (str):
            Required. A name of the EndpointPolicy to delete. Must be in
            the format ``projects/*/locations/*/endpointPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
