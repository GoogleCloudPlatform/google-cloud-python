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
    package="google.cloud.networksecurity.v1beta1",
    manifest={
        "AuthorizationPolicy",
        "ListAuthorizationPoliciesRequest",
        "ListAuthorizationPoliciesResponse",
        "GetAuthorizationPolicyRequest",
        "CreateAuthorizationPolicyRequest",
        "UpdateAuthorizationPolicyRequest",
        "DeleteAuthorizationPolicyRequest",
    },
)


class AuthorizationPolicy(proto.Message):
    r"""AuthorizationPolicy is a resource that specifies how a server
    should authorize incoming connections. This resource in itself
    does not change the configuration unless it's attached to a
    target https proxy or endpoint config selector resource.

    Attributes:
        name (str):
            Required. Name of the AuthorizationPolicy resource. It
            matches pattern
            ``projects/{project}/locations/{location}/authorizationPolicies/<authorization_policy>``.
        description (str):
            Optional. Free-text description of the
            resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the AuthorizationPolicy resource.
        action (google.cloud.network_security_v1beta1.types.AuthorizationPolicy.Action):
            Required. The action to take when a rule
            match is found. Possible values are "ALLOW" or
            "DENY".
        rules (MutableSequence[google.cloud.network_security_v1beta1.types.AuthorizationPolicy.Rule]):
            Optional. List of rules to match. Note that at least one of
            the rules must match in order for the action specified in
            the 'action' field to be taken. A rule is a match if there
            is a matching source and destination. If left blank, the
            action specified in the ``action`` field will be applied on
            every request.
    """

    class Action(proto.Enum):
        r"""Possible values that define what action to take.

        Values:
            ACTION_UNSPECIFIED (0):
                Default value.
            ALLOW (1):
                Grant access.
            DENY (2):
                Deny access.
                Deny rules should be avoided unless they are
                used to provide a default "deny all" fallback.
        """

        ACTION_UNSPECIFIED = 0
        ALLOW = 1
        DENY = 2

    class Rule(proto.Message):
        r"""Specification of rules.

        Attributes:
            sources (MutableSequence[google.cloud.network_security_v1beta1.types.AuthorizationPolicy.Rule.Source]):
                Optional. List of attributes for the traffic source. All of
                the sources must match. A source is a match if both
                principals and ip_blocks match. If not set, the action
                specified in the 'action' field will be applied without any
                rule checks for the source.
            destinations (MutableSequence[google.cloud.network_security_v1beta1.types.AuthorizationPolicy.Rule.Destination]):
                Optional. List of attributes for the traffic
                destination. All of the destinations must match.
                A destination is a match if a request matches
                all the specified hosts, ports, methods and
                headers. If not set, the action specified in the
                'action' field will be applied without any rule
                checks for the destination.
        """

        class Source(proto.Message):
            r"""Specification of traffic source attributes.

            Attributes:
                principals (MutableSequence[str]):
                    Optional. List of peer identities to match for
                    authorization. At least one principal should match. Each
                    peer can be an exact match, or a prefix match (example,
                    "namespace/*") or a suffix match (example,
                    "*/service-account") or a presence match "\*". Authorization
                    based on the principal name without certificate validation
                    (configured by ServerTlsPolicy resource) is considered
                    insecure.
                ip_blocks (MutableSequence[str]):
                    Optional. List of CIDR ranges to match based
                    on source IP address. At least one IP block
                    should match. Single IP (e.g., "1.2.3.4") and
                    CIDR (e.g., "1.2.3.0/24") are supported.
                    Authorization based on source IP alone should be
                    avoided. The IP addresses of any load balancers
                    or proxies should be considered untrusted.
            """

            principals: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            ip_blocks: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )

        class Destination(proto.Message):
            r"""Specification of traffic destination attributes.

            Attributes:
                hosts (MutableSequence[str]):
                    Required. List of host names to match. Matched against the
                    ":authority" header in http requests. At least one host
                    should match. Each host can be an exact match, or a prefix
                    match (example "mydomain.\ *") or a suffix match (example
                    "*.myorg.com") or a presence (any) match "\*".
                ports (MutableSequence[int]):
                    Required. List of destination ports to match.
                    At least one port should match.
                methods (MutableSequence[str]):
                    Optional. A list of HTTP methods to match. At
                    least one method should match. Should not be set
                    for gRPC services.
                http_header_match (google.cloud.network_security_v1beta1.types.AuthorizationPolicy.Rule.Destination.HttpHeaderMatch):
                    Optional. Match against key:value pair in
                    http header. Provides a flexible match based on
                    HTTP headers, for potentially advanced use
                    cases. At least one header should match. Avoid
                    using header matches to make authorization
                    decisions unless there is a strong guarantee
                    that requests arrive through a trusted client or
                    proxy.
            """

            class HttpHeaderMatch(proto.Message):
                r"""Specification of HTTP header match attributes.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    regex_match (str):
                        Required. The value of the header must match
                        the regular expression specified in regexMatch.
                        For regular expression grammar, please see:
                        en.cppreference.com/w/cpp/regex/ecmascript For
                        matching against a port specified in the HTTP
                        request, use a headerMatch with headerName set
                        to Host and a regular expression that satisfies
                        the RFC2616 Host header's port specifier.

                        This field is a member of `oneof`_ ``type``.
                    header_name (str):
                        Required. The name of the HTTP header to
                        match. For matching against the HTTP request's
                        authority, use a headerMatch with the header
                        name ":authority". For matching a request's
                        method, use the headerName ":method".
                """

                regex_match: str = proto.Field(
                    proto.STRING,
                    number=2,
                    oneof="type",
                )
                header_name: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            hosts: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            ports: MutableSequence[int] = proto.RepeatedField(
                proto.UINT32,
                number=2,
            )
            methods: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=4,
            )
            http_header_match: "AuthorizationPolicy.Rule.Destination.HttpHeaderMatch" = proto.Field(
                proto.MESSAGE,
                number=5,
                message="AuthorizationPolicy.Rule.Destination.HttpHeaderMatch",
            )

        sources: MutableSequence["AuthorizationPolicy.Rule.Source"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="AuthorizationPolicy.Rule.Source",
            )
        )
        destinations: MutableSequence["AuthorizationPolicy.Rule.Destination"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="AuthorizationPolicy.Rule.Destination",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    action: Action = proto.Field(
        proto.ENUM,
        number=6,
        enum=Action,
    )
    rules: MutableSequence[Rule] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=Rule,
    )


class ListAuthorizationPoliciesRequest(proto.Message):
    r"""Request used with the ListAuthorizationPolicies method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            AuthorizationPolicies should be listed, specified in the
            format ``projects/{project}/locations/{location}``.
        page_size (int):
            Maximum number of AuthorizationPolicies to
            return per call.
        page_token (str):
            The value returned by the last
            ``ListAuthorizationPoliciesResponse`` Indicates that this is
            a continuation of a prior ``ListAuthorizationPolicies``
            call, and that the system should return the next page of
            data.
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


class ListAuthorizationPoliciesResponse(proto.Message):
    r"""Response returned by the ListAuthorizationPolicies method.

    Attributes:
        authorization_policies (MutableSequence[google.cloud.network_security_v1beta1.types.AuthorizationPolicy]):
            List of AuthorizationPolicies resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
    """

    @property
    def raw_page(self):
        return self

    authorization_policies: MutableSequence["AuthorizationPolicy"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AuthorizationPolicy",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAuthorizationPolicyRequest(proto.Message):
    r"""Request used by the GetAuthorizationPolicy method.

    Attributes:
        name (str):
            Required. A name of the AuthorizationPolicy to get. Must be
            in the format
            ``projects/{project}/locations/{location}/authorizationPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAuthorizationPolicyRequest(proto.Message):
    r"""Request used by the CreateAuthorizationPolicy method.

    Attributes:
        parent (str):
            Required. The parent resource of the AuthorizationPolicy.
            Must be in the format
            ``projects/{project}/locations/{location}``.
        authorization_policy_id (str):
            Required. Short name of the AuthorizationPolicy resource to
            be created. This value should be 1-63 characters long,
            containing only letters, numbers, hyphens, and underscores,
            and should not start with a number. E.g. "authz_policy".
        authorization_policy (google.cloud.network_security_v1beta1.types.AuthorizationPolicy):
            Required. AuthorizationPolicy resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    authorization_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    authorization_policy: "AuthorizationPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AuthorizationPolicy",
    )


class UpdateAuthorizationPolicyRequest(proto.Message):
    r"""Request used by the UpdateAuthorizationPolicy method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the AuthorizationPolicy resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        authorization_policy (google.cloud.network_security_v1beta1.types.AuthorizationPolicy):
            Required. Updated AuthorizationPolicy
            resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    authorization_policy: "AuthorizationPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AuthorizationPolicy",
    )


class DeleteAuthorizationPolicyRequest(proto.Message):
    r"""Request used by the DeleteAuthorizationPolicy method.

    Attributes:
        name (str):
            Required. A name of the AuthorizationPolicy to delete. Must
            be in the format
            ``projects/{project}/locations/{location}/authorizationPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
