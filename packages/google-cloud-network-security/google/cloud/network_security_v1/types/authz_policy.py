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
    package="google.cloud.networksecurity.v1",
    manifest={
        "AuthzPolicy",
        "CreateAuthzPolicyRequest",
        "ListAuthzPoliciesRequest",
        "ListAuthzPoliciesResponse",
        "GetAuthzPolicyRequest",
        "UpdateAuthzPolicyRequest",
        "DeleteAuthzPolicyRequest",
    },
)


class AuthzPolicy(proto.Message):
    r"""``AuthzPolicy`` is a resource that allows to forward traffic to a
    callout backend designed to scan the traffic for security purposes.

    Attributes:
        name (str):
            Required. Identifier. Name of the ``AuthzPolicy`` resource
            in the following format:
            ``projects/{project}/locations/{location}/authzPolicies/{authz_policy}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        description (str):
            Optional. A human-readable description of the
            resource.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with the ``AuthzPolicy``
            resource.

            The format must comply with `the following
            requirements </compute/docs/labeling-resources#requirements>`__.
        target (google.cloud.network_security_v1.types.AuthzPolicy.Target):
            Required. Specifies the set of resources to
            which this policy should be applied to.
        http_rules (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule]):
            Optional. A list of authorization HTTP rules
            to match against the incoming request. A policy
            match occurs when at least one HTTP rule matches
            the request or when no HTTP rules are specified
            in the policy. At least one HTTP Rule is
            required for Allow or Deny Action. Limited to 5
            rules.
        network_rules (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule]):
            Optional. A list of authorization network
            rules to match against the incoming request. A
            policy match occurs when at least one network
            rule matches the request.
            At least one network rule is required for Allow
            or Deny Action if no HTTP rules are provided.
            Network rules are mutually exclusive with HTTP
            rules. Limited to 5 rules.
        action (google.cloud.network_security_v1.types.AuthzPolicy.AuthzAction):
            Required. Can be one of ``ALLOW``, ``DENY``, ``CUSTOM``.

            When the action is ``CUSTOM``, ``customProvider`` must be
            specified.

            When the action is ``ALLOW``, only requests matching the
            policy will be allowed.

            When the action is ``DENY``, only requests matching the
            policy will be denied.

            When a request arrives, the policies are evaluated in the
            following order:

            1. If there is a ``CUSTOM`` policy that matches the request,
               the ``CUSTOM`` policy is evaluated using the custom
               authorization providers and the request is denied if the
               provider rejects the request.

            2. If there are any ``DENY`` policies that match the
               request, the request is denied.

            3. If there are no ``ALLOW`` policies for the resource or if
               any of the ``ALLOW`` policies match the request, the
               request is allowed.

            4. Else the request is denied by default if none of the
               configured AuthzPolicies with ``ALLOW`` action match the
               request.
        custom_provider (google.cloud.network_security_v1.types.AuthzPolicy.CustomProvider):
            Optional. Required if the action is ``CUSTOM``. Allows
            delegating authorization decisions to Cloud IAP or to
            Service Extensions. One of ``cloudIap`` or
            ``authzExtension`` must be specified.
        policy_profile (google.cloud.network_security_v1.types.AuthzPolicy.PolicyProfile):
            Optional. Immutable. Defines the type of authorization being
            performed. If not specified, ``REQUEST_AUTHZ`` is applied.
            This field cannot be changed once AuthzPolicy is created.
    """

    class LoadBalancingScheme(proto.Enum):
        r"""Load balancing schemes supported by the ``AuthzPolicy`` resource.
        The valid values are ``INTERNAL_MANAGED`` and ``EXTERNAL_MANAGED``.
        For more information, refer to `Backend services
        overview <https://cloud.google.com/load-balancing/docs/backend-service>`__.

        Values:
            LOAD_BALANCING_SCHEME_UNSPECIFIED (0):
                Default value. Do not use.
            INTERNAL_MANAGED (1):
                Signifies that this is used for Regional
                internal or Cross-region internal Application
                Load Balancing.
            EXTERNAL_MANAGED (2):
                Signifies that this is used for Global
                external or Regional external Application Load
                Balancing.
            INTERNAL_SELF_MANAGED (3):
                Signifies that this is used for Cloud Service
                Mesh. Meant for use by CSM GKE controller only.
        """

        LOAD_BALANCING_SCHEME_UNSPECIFIED = 0
        INTERNAL_MANAGED = 1
        EXTERNAL_MANAGED = 2
        INTERNAL_SELF_MANAGED = 3

    class AuthzAction(proto.Enum):
        r"""The action to be applied to this policy. Valid values are ``ALLOW``,
        ``DENY``, ``CUSTOM``.

        Values:
            AUTHZ_ACTION_UNSPECIFIED (0):
                Unspecified action.
            ALLOW (1):
                Allow request to pass through to the backend.
            DENY (2):
                Deny the request and return a HTTP 404 to the
                client.
            CUSTOM (3):
                Delegate the authorization decision to an
                external authorization engine.
        """

        AUTHZ_ACTION_UNSPECIFIED = 0
        ALLOW = 1
        DENY = 2
        CUSTOM = 3

    class PolicyProfile(proto.Enum):
        r"""The type of authorization being performed.
        New values may be added in the future.

        Values:
            POLICY_PROFILE_UNSPECIFIED (0):
                Unspecified policy profile.
            REQUEST_AUTHZ (1):
                Applies to request authorization. ``CUSTOM`` authorization
                policies with Authz extensions will be allowed with
                ``EXT_AUTHZ_GRPC`` or ``EXT_PROC_GRPC`` protocols.
                Extensions are invoked only for request header events.
            CONTENT_AUTHZ (2):
                Applies to content security, sanitization, etc. Only
                ``CUSTOM`` action is allowed in this policy profile.
                AuthzExtensions in the custom provider must support
                ``EXT_PROC_GRPC`` protocol only and be capable of receiving
                all ``EXT_PROC_GRPC`` events (REQUEST_HEADERS, REQUEST_BODY,
                REQUEST_TRAILERS, RESPONSE_HEADERS, RESPONSE_BODY,
                RESPONSE_TRAILERS) with ``FULL_DUPLEX_STREAMED`` body send
                mode.
        """

        POLICY_PROFILE_UNSPECIFIED = 0
        REQUEST_AUTHZ = 1
        CONTENT_AUTHZ = 2

    class Target(proto.Message):
        r"""Specifies the set of targets to which this policy should be
        applied to.

        Attributes:
            load_balancing_scheme (google.cloud.network_security_v1.types.AuthzPolicy.LoadBalancingScheme):
                Optional. All gateways and forwarding rules referenced by
                this policy and extensions must share the same load
                balancing scheme. Required only when targeting forwarding
                rules. If targeting Secure Web Proxy, this field must be
                ``INTERNAL_MANAGED`` or not specified. Must not be specified
                when targeting Agent Gateway. Supported values:
                ``INTERNAL_MANAGED`` and ``EXTERNAL_MANAGED``. For more
                information, refer to `Backend services
                overview <https://cloud.google.com/load-balancing/docs/backend-service>`__.
            resources (MutableSequence[str]):
                Required. A list of references to the
                Forwarding Rules, Secure Web Proxy Gateways, or
                Agent Gateways on which this policy will be
                applied.
        """

        load_balancing_scheme: "AuthzPolicy.LoadBalancingScheme" = proto.Field(
            proto.ENUM,
            number=8,
            enum="AuthzPolicy.LoadBalancingScheme",
        )
        resources: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class AuthzRule(proto.Message):
        r"""Conditions to match against the incoming request.

        Attributes:
            from_ (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.From):
                Optional. Describes properties of a source of
                a request.
            to (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To):
                Optional. Describes properties of a target of
                a request.
            when (str):
                Optional. CEL expression that describes the
                conditions to be satisfied for the action. The
                result of the CEL expression is ANDed with the
                from and to. Refer to the CEL language reference
                for a list of available attributes.
        """

        class StringMatch(proto.Message):
            r"""Determines how a string value should be matched.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                exact (str):
                    The input string must match exactly the string specified
                    here.

                    Examples:

                    - ``abc`` only matches the value ``abc``.

                    This field is a member of `oneof`_ ``match_pattern``.
                prefix (str):
                    The input string must have the prefix specified here. Note:
                    empty prefix is not allowed, please use regex instead.

                    Examples:

                    - ``abc`` matches the value ``abc.xyz``

                    This field is a member of `oneof`_ ``match_pattern``.
                suffix (str):
                    The input string must have the suffix specified here. Note:
                    empty prefix is not allowed, please use regex instead.

                    Examples:

                    - ``abc`` matches the value ``xyz.abc``

                    This field is a member of `oneof`_ ``match_pattern``.
                contains (str):
                    The input string must have the substring specified here.
                    Note: empty contains match is not allowed, please use regex
                    instead.

                    Examples:

                    - ``abc`` matches the value ``xyz.abc.def``

                    This field is a member of `oneof`_ ``match_pattern``.
                ignore_case (bool):
                    If true, indicates the exact/prefix/suffix/contains matching
                    should be case insensitive. For example, the matcher
                    ``data`` will match both input string ``Data`` and ``data``
                    if set to true.
            """

            exact: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="match_pattern",
            )
            prefix: str = proto.Field(
                proto.STRING,
                number=2,
                oneof="match_pattern",
            )
            suffix: str = proto.Field(
                proto.STRING,
                number=3,
                oneof="match_pattern",
            )
            contains: str = proto.Field(
                proto.STRING,
                number=4,
                oneof="match_pattern",
            )
            ignore_case: bool = proto.Field(
                proto.BOOL,
                number=5,
            )

        class IpBlock(proto.Message):
            r"""Represents a range of IP Addresses.

            Attributes:
                prefix (str):
                    Required. The address prefix.
                length (int):
                    Required. The length of the address range.
            """

            prefix: str = proto.Field(
                proto.STRING,
                number=1,
            )
            length: int = proto.Field(
                proto.INT32,
                number=2,
            )

        class RequestResource(proto.Message):
            r"""Describes the properties of a client VM resource accessing
            the internal application load balancers.

            Attributes:
                tag_value_id_set (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.RequestResource.TagValueIdSet):
                    Optional. A list of resource tag value
                    permanent IDs to match against the resource
                    manager tags value associated with the source VM
                    of a request.
                iam_service_account (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch):
                    Optional. An IAM service account to match
                    against the source service account of the VM
                    sending the request.
            """

            class TagValueIdSet(proto.Message):
                r"""Describes a set of resource tag value permanent IDs to match
                against the resource manager tags value associated with the
                source VM of a request.

                Attributes:
                    ids (MutableSequence[int]):
                        Required. A list of resource tag value
                        permanent IDs to match against the resource
                        manager tags value associated with the source VM
                        of a request. The match follows AND semantics
                        which means all the ids must match. Limited to 5
                        ids in the Tag value id set.
                """

                ids: MutableSequence[int] = proto.RepeatedField(
                    proto.INT64,
                    number=1,
                )

            tag_value_id_set: "AuthzPolicy.AuthzRule.RequestResource.TagValueIdSet" = (
                proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="AuthzPolicy.AuthzRule.RequestResource.TagValueIdSet",
                )
            )
            iam_service_account: "AuthzPolicy.AuthzRule.StringMatch" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="AuthzPolicy.AuthzRule.StringMatch",
            )

        class HeaderMatch(proto.Message):
            r"""Determines how a HTTP header should be matched.

            Attributes:
                name (str):
                    Optional. Specifies the name of the header in
                    the request.
                value (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch):
                    Optional. Specifies how the header match will
                    be performed.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            value: "AuthzPolicy.AuthzRule.StringMatch" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="AuthzPolicy.AuthzRule.StringMatch",
            )

        class Principal(proto.Message):
            r"""Describes the properties of a principal to be matched
            against.

            Attributes:
                principal_selector (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.Principal.PrincipalSelector):
                    Optional. An enum to decide what principal value the
                    principal rule will match against. If not specified, the
                    PrincipalSelector is CLIENT_CERT_URI_SAN.
                principal (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch):
                    Required. A non-empty string whose value is matched against
                    the principal value based on the principal_selector. Only
                    exact match can be applied for CLIENT_CERT_URI_SAN,
                    CLIENT_CERT_DNS_NAME_SAN, CLIENT_CERT_COMMON_NAME selectors.
            """

            class PrincipalSelector(proto.Enum):
                r"""The principal value the principal rule will match against.

                Values:
                    PRINCIPAL_SELECTOR_UNSPECIFIED (0):
                        Unspecified principal selector. It will be treated as
                        CLIENT_CERT_URI_SAN by default.
                    CLIENT_CERT_URI_SAN (1):
                        The principal rule is matched against a list
                        of URI SANs in the validated client's
                        certificate. A match happens when there is any
                        exact URI SAN value match. This is the default
                        principal selector.
                    CLIENT_CERT_DNS_NAME_SAN (2):
                        The principal rule is matched against a list of DNS Name
                        SANs in the validated client's certificate. A match happens
                        when there is any exact DNS Name SAN value match. This is
                        only applicable for Application Load Balancers except for
                        classic Global External Application load balancer.
                        CLIENT_CERT_DNS_NAME_SAN is not supported for
                        INTERNAL_SELF_MANAGED load balancing scheme.
                    CLIENT_CERT_COMMON_NAME (3):
                        The principal rule is matched against the common name in the
                        client's certificate. Authorization against multiple common
                        names in the client certificate is not supported. Requests
                        with multiple common names in the client certificate will be
                        rejected if CLIENT_CERT_COMMON_NAME is set as the principal
                        selector. A match happens when there is an exact common name
                        value match. This is only applicable for Application Load
                        Balancers except for global external Application Load
                        Balancer and classic Application Load Balancer.
                        CLIENT_CERT_COMMON_NAME is not supported for
                        INTERNAL_SELF_MANAGED load balancing scheme.
                """

                PRINCIPAL_SELECTOR_UNSPECIFIED = 0
                CLIENT_CERT_URI_SAN = 1
                CLIENT_CERT_DNS_NAME_SAN = 2
                CLIENT_CERT_COMMON_NAME = 3

            principal_selector: "AuthzPolicy.AuthzRule.Principal.PrincipalSelector" = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="AuthzPolicy.AuthzRule.Principal.PrincipalSelector",
                )
            )
            principal: "AuthzPolicy.AuthzRule.StringMatch" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="AuthzPolicy.AuthzRule.StringMatch",
            )

        class From(proto.Message):
            r"""Describes properties of one or more sources of a request.

            Attributes:
                sources (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.From.RequestSource]):
                    Optional. Describes the properties of a
                    request's sources. At least one of sources or
                    notSources must be specified. Limited to 1
                    source. A match occurs when ANY source (in
                    sources or notSources) matches the request.
                    Within a single source, the match follows AND
                    semantics across fields and OR semantics within
                    a single field, i.e. a match occurs when ANY
                    principal matches AND ANY ipBlocks match.
                not_sources (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.From.RequestSource]):
                    Optional. Describes the negated properties of
                    request sources. Matches requests from sources
                    that do not match the criteria specified in this
                    field. At least one of sources or notSources
                    must be specified.
            """

            class RequestSource(proto.Message):
                r"""Describes the properties of a single source.

                Attributes:
                    principals (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.Principal]):
                        Optional. A list of identities derived from
                        the client's certificate. This field will not
                        match on a request unless frontend mutual TLS is
                        enabled for the forwarding rule or Gateway and
                        the client certificate has been successfully
                        validated by mTLS.
                        Each identity is a string whose value is matched
                        against a list of URI SANs, DNS Name SANs, or
                        the common name in the client's certificate. A
                        match happens when any principal matches with
                        the rule. Limited to 50 principals per
                        Authorization Policy for regional internal
                        Application Load Balancers, regional external
                        Application Load Balancers, cross-region
                        internal Application Load Balancers, and Cloud
                        Service Mesh. This field is not supported for
                        global external Application Load Balancers.
                    ip_blocks (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.IpBlock]):
                        Optional. A list of IP addresses or IP address ranges to
                        match against the source IP address of the request. Limited
                        to 10 ip_blocks per Authorization Policy
                    resources (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.RequestResource]):
                        Optional. A list of resources to match
                        against the resource of the source VM of a
                        request. Limited to 10 resources per
                        Authorization Policy.
                """

                principals: MutableSequence["AuthzPolicy.AuthzRule.Principal"] = (
                    proto.RepeatedField(
                        proto.MESSAGE,
                        number=1,
                        message="AuthzPolicy.AuthzRule.Principal",
                    )
                )
                ip_blocks: MutableSequence["AuthzPolicy.AuthzRule.IpBlock"] = (
                    proto.RepeatedField(
                        proto.MESSAGE,
                        number=2,
                        message="AuthzPolicy.AuthzRule.IpBlock",
                    )
                )
                resources: MutableSequence["AuthzPolicy.AuthzRule.RequestResource"] = (
                    proto.RepeatedField(
                        proto.MESSAGE,
                        number=3,
                        message="AuthzPolicy.AuthzRule.RequestResource",
                    )
                )

            sources: MutableSequence["AuthzPolicy.AuthzRule.From.RequestSource"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=1,
                    message="AuthzPolicy.AuthzRule.From.RequestSource",
                )
            )
            not_sources: MutableSequence["AuthzPolicy.AuthzRule.From.RequestSource"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=2,
                    message="AuthzPolicy.AuthzRule.From.RequestSource",
                )
            )

        class To(proto.Message):
            r"""Describes properties of one or more targets of a request.

            Attributes:
                operations (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation]):
                    Optional. Describes properties of one or more
                    targets of a request. At least one of operations
                    or notOperations must be specified. Limited to 1
                    operation. A match occurs when ANY operation (in
                    operations or notOperations) matches. Within an
                    operation, the match follows AND semantics
                    across fields and OR semantics within a field,
                    i.e. a match occurs when ANY path matches AND
                    ANY header matches and ANY method matches.
                not_operations (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation]):
                    Optional. Describes the negated properties of
                    the targets of a request. Matches requests for
                    operations that do not match the criteria
                    specified in this field. At least one of
                    operations or notOperations must be specified.
            """

            class RequestOperation(proto.Message):
                r"""Describes properties of one or more targets of a request.

                Attributes:
                    header_set (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation.HeaderSet):
                        Optional. A list of headers to match against
                        in http header.
                    hosts (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch]):
                        Optional. A list of HTTP Hosts to match
                        against. The match can be one of exact, prefix,
                        suffix, or contains (substring match). Matches
                        are always case sensitive unless the ignoreCase
                        is set. Limited to 10 hosts per Authorization
                        Policy.
                    paths (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch]):
                        Optional. A list of paths to match against.
                        The match can be one of exact, prefix, suffix,
                        or contains (substring match). Matches are
                        always case sensitive unless the ignoreCase is
                        set. Limited to 10 paths per Authorization
                        Policy.
                        Note that this path match includes the query
                        parameters. For gRPC services, this should be a
                        fully-qualified name of the form
                        /package.service/method.
                    methods (MutableSequence[str]):
                        Optional. A list of HTTP methods to match
                        against. Each entry must be a valid HTTP method
                        name (GET, PUT, POST, HEAD, PATCH, DELETE,
                        OPTIONS). It only allows exact match and is
                        always case sensitive. Limited to 10 methods per
                        Authorization Policy.
                    mcp (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation.MCP):
                        Optional. Defines the MCP protocol attributes
                        to match on. If the MCP payload in the request
                        body cannot be successfully parsed, the request
                        will be denied. This field can be set only for
                        AuthzPolicies targeting AgentGateway resources.
                    snis (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch]):
                        Optional. A list of SNIs to match against.
                        The match can be one of exact, prefix, suffix,
                        or contains (substring match). If there is no
                        SNI (i.e. plaintext HTTP traffic), the request
                        will be denied. Matches are always case
                        sensitive unless the ignoreCase is set. Limited
                        to 10 SNIs per Authorization Policy.
                """

                class BaseProtocolMethodsOption(proto.Enum):
                    r"""Describes the option to match against the base MCP protocol
                    methods.

                    Values:
                        BASE_PROTOCOL_METHODS_OPTION_UNSPECIFIED (0):
                            Unspecified option. Defaults to SKIP_BASE_PROTOCOL_METHODS.
                        SKIP_BASE_PROTOCOL_METHODS (1):
                            Skip matching on the base MCP protocol
                            methods.
                        MATCH_BASE_PROTOCOL_METHODS (2):
                            Match on the base MCP protocol methods.
                    """

                    BASE_PROTOCOL_METHODS_OPTION_UNSPECIFIED = 0
                    SKIP_BASE_PROTOCOL_METHODS = 1
                    MATCH_BASE_PROTOCOL_METHODS = 2

                class HeaderSet(proto.Message):
                    r"""Describes a set of HTTP headers to match against.

                    Attributes:
                        headers (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.HeaderMatch]):
                            Required. A list of headers to match against
                            in http header. The match can be one of exact,
                            prefix, suffix, or contains (substring match).
                            The match follows AND semantics which means all
                            the headers must match. Matches are always case
                            sensitive unless the ignoreCase is set. Limited
                            to 10 headers per Authorization Policy.
                    """

                    headers: MutableSequence["AuthzPolicy.AuthzRule.HeaderMatch"] = (
                        proto.RepeatedField(
                            proto.MESSAGE,
                            number=1,
                            message="AuthzPolicy.AuthzRule.HeaderMatch",
                        )
                    )

                class MCPMethod(proto.Message):
                    r"""Describes a set of MCP methods to match against.

                    Attributes:
                        name (str):
                            Required. The MCP method to match against. Allowed values
                            are as follows:

                            1. ``tools``, ``prompts``, ``resources`` - these will match
                               against all sub methods under the respective methods.
                            2. ``prompts/list``, ``tools/list``, ``resources/list``,
                               ``resources/templates/list``
                            3. ``prompts/get``, ``tools/call``, ``resources/subscribe``,
                               ``resources/unsubscribe``, ``resources/read`` Params
                               cannot be specified for categories 1 and 2.
                        params (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch]):
                            Optional. A list of MCP method parameters to
                            match against. The match can be one of exact,
                            prefix, suffix, or contains (substring match).
                            Matches are always case sensitive unless the
                            ignoreCase is set. Limited to 10 MCP method
                            parameters per Authorization Policy.
                    """

                    name: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )
                    params: MutableSequence["AuthzPolicy.AuthzRule.StringMatch"] = (
                        proto.RepeatedField(
                            proto.MESSAGE,
                            number=2,
                            message="AuthzPolicy.AuthzRule.StringMatch",
                        )
                    )

                class MCP(proto.Message):
                    r"""Describes a set of MCP protocol attributes to match against
                    for a given MCP request.

                    Attributes:
                        base_protocol_methods_option (google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation.BaseProtocolMethodsOption):
                            Optional. If specified, matches on the MCP protocol’s
                            non-access specific methods namely:

                            - initialize
                            - completion/
                            - logging/
                            - notifications/
                            - ping Defaults to SKIP_BASE_PROTOCOL_METHODS if not
                              specified.
                        methods (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation.MCPMethod]):
                            Optional. A list of MCP methods and associated parameters to
                            match on. It is recommended to use this field to match on
                            tools, prompts and resource accesses while setting the
                            baseProtocolMethodsOption to MATCH_BASE_PROTOCOL_METHODS to
                            match on all the other MCP protocol methods. Limited to 10
                            MCP methods per Authorization Policy.
                    """

                    base_protocol_methods_option: "AuthzPolicy.AuthzRule.To.RequestOperation.BaseProtocolMethodsOption" = proto.Field(
                        proto.ENUM,
                        number=1,
                        enum="AuthzPolicy.AuthzRule.To.RequestOperation.BaseProtocolMethodsOption",
                    )
                    methods: MutableSequence[
                        "AuthzPolicy.AuthzRule.To.RequestOperation.MCPMethod"
                    ] = proto.RepeatedField(
                        proto.MESSAGE,
                        number=2,
                        message="AuthzPolicy.AuthzRule.To.RequestOperation.MCPMethod",
                    )

                header_set: "AuthzPolicy.AuthzRule.To.RequestOperation.HeaderSet" = (
                    proto.Field(
                        proto.MESSAGE,
                        number=1,
                        message="AuthzPolicy.AuthzRule.To.RequestOperation.HeaderSet",
                    )
                )
                hosts: MutableSequence["AuthzPolicy.AuthzRule.StringMatch"] = (
                    proto.RepeatedField(
                        proto.MESSAGE,
                        number=2,
                        message="AuthzPolicy.AuthzRule.StringMatch",
                    )
                )
                paths: MutableSequence["AuthzPolicy.AuthzRule.StringMatch"] = (
                    proto.RepeatedField(
                        proto.MESSAGE,
                        number=3,
                        message="AuthzPolicy.AuthzRule.StringMatch",
                    )
                )
                methods: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=4,
                )
                mcp: "AuthzPolicy.AuthzRule.To.RequestOperation.MCP" = proto.Field(
                    proto.MESSAGE,
                    number=5,
                    message="AuthzPolicy.AuthzRule.To.RequestOperation.MCP",
                )
                snis: MutableSequence["AuthzPolicy.AuthzRule.StringMatch"] = (
                    proto.RepeatedField(
                        proto.MESSAGE,
                        number=7,
                        message="AuthzPolicy.AuthzRule.StringMatch",
                    )
                )

            operations: MutableSequence["AuthzPolicy.AuthzRule.To.RequestOperation"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=1,
                    message="AuthzPolicy.AuthzRule.To.RequestOperation",
                )
            )
            not_operations: MutableSequence[
                "AuthzPolicy.AuthzRule.To.RequestOperation"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="AuthzPolicy.AuthzRule.To.RequestOperation",
            )

        from_: "AuthzPolicy.AuthzRule.From" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="AuthzPolicy.AuthzRule.From",
        )
        to: "AuthzPolicy.AuthzRule.To" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="AuthzPolicy.AuthzRule.To",
        )
        when: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class CustomProvider(proto.Message):
        r"""Allows delegating authorization decisions to Cloud IAP or to
        Service Extensions.

        Attributes:
            cloud_iap (google.cloud.network_security_v1.types.AuthzPolicy.CustomProvider.CloudIap):
                Optional. Delegates authorization decisions
                to Cloud IAP. Applicable only for managed load
                balancers. Enabling Cloud IAP at the AuthzPolicy
                level is not compatible with Cloud IAP settings
                in the BackendService. Enabling IAP in both
                places will result in request failure. Ensure
                that IAP is enabled in either the AuthzPolicy or
                the BackendService but not in both places.
            authz_extension (google.cloud.network_security_v1.types.AuthzPolicy.CustomProvider.AuthzExtension):
                Optional. Delegate authorization decision to
                user authored Service Extension. Only one of
                cloudIap or authzExtension can be specified.
        """

        class CloudIap(proto.Message):
            r"""Optional. Delegates authorization decisions to Cloud IAP.
            Applicable only for managed load balancers. Enabling Cloud IAP
            at the AuthzPolicy level is not compatible with Cloud IAP
            settings in the BackendService. Enabling IAP in both places will
            result in request failure. Ensure that IAP is enabled in either
            the AuthzPolicy or the BackendService but not in both places.

            """

        class AuthzExtension(proto.Message):
            r"""Optional. Delegate authorization decision to user authored
            extension. Only one of cloudIap or authzExtension can be
            specified.

            Attributes:
                resources (MutableSequence[str]):
                    Required. A list of references to
                    authorization extensions that will be invoked
                    for requests matching this policy. Limited to 1
                    custom provider.
            """

            resources: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        cloud_iap: "AuthzPolicy.CustomProvider.CloudIap" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="AuthzPolicy.CustomProvider.CloudIap",
        )
        authz_extension: "AuthzPolicy.CustomProvider.AuthzExtension" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="AuthzPolicy.CustomProvider.AuthzExtension",
        )

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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    target: Target = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Target,
    )
    http_rules: MutableSequence[AuthzRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=AuthzRule,
    )
    network_rules: MutableSequence[AuthzRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=AuthzRule,
    )
    action: AuthzAction = proto.Field(
        proto.ENUM,
        number=8,
        enum=AuthzAction,
    )
    custom_provider: CustomProvider = proto.Field(
        proto.MESSAGE,
        number=10,
        message=CustomProvider,
    )
    policy_profile: PolicyProfile = proto.Field(
        proto.ENUM,
        number=11,
        enum=PolicyProfile,
    )


class CreateAuthzPolicyRequest(proto.Message):
    r"""Message for creating an ``AuthzPolicy`` resource.

    Attributes:
        parent (str):
            Required. The parent resource of the ``AuthzPolicy``
            resource. Must be in the format
            ``projects/{project}/locations/{location}``.
        authz_policy_id (str):
            Required. User-provided ID of the ``AuthzPolicy`` resource
            to be created.
        authz_policy (google.cloud.network_security_v1.types.AuthzPolicy):
            Required. ``AuthzPolicy`` resource to be created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
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
    authz_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    authz_policy: "AuthzPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AuthzPolicy",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAuthzPoliciesRequest(proto.Message):
    r"""Message for requesting list of ``AuthzPolicy`` resources.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ``AuthzPolicy`` resources are listed, specified in the
            following format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. The server
            might return fewer items than requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results that the server returns.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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


class ListAuthzPoliciesResponse(proto.Message):
    r"""Message for response to listing ``AuthzPolicy`` resources.

    Attributes:
        authz_policies (MutableSequence[google.cloud.network_security_v1.types.AuthzPolicy]):
            The list of ``AuthzPolicy`` resources.
        next_page_token (str):
            A token identifying a page of results that
            the server returns.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    authz_policies: MutableSequence["AuthzPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AuthzPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAuthzPolicyRequest(proto.Message):
    r"""Message for getting a ``AuthzPolicy`` resource.

    Attributes:
        name (str):
            Required. A name of the ``AuthzPolicy`` resource to get.
            Must be in the format
            ``projects/{project}/locations/{location}/authzPolicies/{authz_policy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAuthzPolicyRequest(proto.Message):
    r"""Message for updating an ``AuthzPolicy`` resource.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Used to specify the fields to be overwritten in
            the ``AuthzPolicy`` resource by the update. The fields
            specified in the ``update_mask`` are relative to the
            resource, not the full request. A field is overwritten if it
            is in the mask. If the user does not specify a mask, then
            all fields are overwritten.
        authz_policy (google.cloud.network_security_v1.types.AuthzPolicy):
            Required. ``AuthzPolicy`` resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
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
    authz_policy: "AuthzPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AuthzPolicy",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteAuthzPolicyRequest(proto.Message):
    r"""Message for deleting an ``AuthzPolicy`` resource.

    Attributes:
        name (str):
            Required. The name of the ``AuthzPolicy`` resource to
            delete. Must be in the format
            ``projects/{project}/locations/{location}/authzPolicies/{authz_policy}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
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
