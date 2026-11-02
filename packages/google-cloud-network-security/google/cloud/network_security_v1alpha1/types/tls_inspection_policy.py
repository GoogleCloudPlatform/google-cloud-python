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
        "TlsInspectionPolicy",
        "CreateTlsInspectionPolicyRequest",
        "ListTlsInspectionPoliciesRequest",
        "ListTlsInspectionPoliciesResponse",
        "GetTlsInspectionPolicyRequest",
        "DeleteTlsInspectionPolicyRequest",
        "UpdateTlsInspectionPolicyRequest",
    },
)


class TlsInspectionPolicy(proto.Message):
    r"""The TlsInspectionPolicy resource contains references to CA
    pools in Certificate Authority Service and associated metadata.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Name of the resource. Name is of the form
            projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}
            tls_inspection_policy should match the
            pattern:(^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$).
        description (str):
            Optional. Free-text description of the
            resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        ca_pool (str):
            Required. A CA pool resource used to issue interception
            certificates. The CA pool string has a relative resource
            path following the form
            "projects/{project}/locations/{location}/caPools/{ca_pool}".
        trust_config (str):
            Optional. A TrustConfig resource used when making a
            connection to the TLS server. This is a relative resource
            path following the form
            "projects/{project}/locations/{location}/trustConfigs/{trust_config}".
            This is necessary to intercept TLS connections to servers
            with certificates signed by a private CA or self-signed
            certificates. Note that Secure Web Proxy does not yet honor
            this field.
        exclude_public_ca_set (bool):
            Optional. If FALSE (the default), use our default set of
            public CAs in addition to any CAs specified in trust_config.
            These public CAs are currently based on the Mozilla Root
            Program and are subject to change over time. If TRUE, do not
            accept our default set of public CAs. Only CAs specified in
            trust_config will be accepted. This defaults to FALSE (use
            public CAs in addition to trust_config) for backwards
            compatibility, but trusting public root CAs is *not
            recommended* unless the traffic in question is outbound to
            public web servers. When possible, prefer setting this to
            "false" and explicitly specifying trusted CAs and
            certificates in a TrustConfig. Note that Secure Web Proxy
            does not yet honor this field.

            This field is a member of `oneof`_ ``_exclude_public_ca_set``.
        min_tls_version (google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy.TlsVersion):
            Optional. Minimum TLS version that the
            firewall should use when negotiating connections
            with both clients and servers. If this is not
            set, then the default value is to allow the
            broadest set of clients and servers (TLS 1.0 or
            higher). Setting this to more restrictive values
            may improve security, but may also prevent the
            firewall from connecting to some clients or
            servers.
            Note that Secure Web Proxy does not yet honor
            this field.
        tls_feature_profile (google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy.Profile):
            Optional. The selected Profile. If this is not set, then the
            default value is to allow the broadest set of clients and
            servers ("PROFILE_COMPATIBLE"). Setting this to more
            restrictive values may improve security, but may also
            prevent the TLS inspection proxy from connecting to some
            clients or servers. Note that Secure Web Proxy does not yet
            honor this field.
        custom_tls_features (MutableSequence[str]):
            Optional. List of custom TLS cipher suites selected. This
            field is valid only if the selected tls_feature_profile is
            CUSTOM. The
            [compute.SslPoliciesService.ListAvailableFeatures][] method
            returns the set of features that can be specified in this
            list. Note that Secure Web Proxy does not yet honor this
            field.
    """

    class TlsVersion(proto.Enum):
        r"""The minimum version of TLS protocol that can be used by
        clients or servers to establish a connection with the TLS
        inspection proxy.

        Values:
            TLS_VERSION_UNSPECIFIED (0):
                Indicates no TLS version was specified.
            TLS_1_0 (1):
                TLS 1.0
            TLS_1_1 (2):
                TLS 1.1
            TLS_1_2 (3):
                TLS 1.2
            TLS_1_3 (4):
                TLS 1.3
        """

        TLS_VERSION_UNSPECIFIED = 0
        TLS_1_0 = 1
        TLS_1_1 = 2
        TLS_1_2 = 3
        TLS_1_3 = 4

    class Profile(proto.Enum):
        r"""Profile specifies the set of TLS cipher suites (and possibly
        other features in the future) that can be used by the firewall
        when negotiating TLS connections with clients and servers. The
        meaning of these fields is identical to the load balancers'
        SSLPolicy resource.

        Values:
            PROFILE_UNSPECIFIED (0):
                Indicates no profile was specified.
            PROFILE_COMPATIBLE (1):
                Compatible profile. Allows the broadest set
                of clients, even those which support only
                out-of-date SSL features to negotiate with the
                TLS inspection proxy.
            PROFILE_MODERN (2):
                Modern profile. Supports a wide set of SSL
                features, allowing modern clients to negotiate
                SSL with the TLS inspection proxy.
            PROFILE_RESTRICTED (3):
                Restricted profile. Supports a reduced set of
                SSL features, intended to meet stricter
                compliance requirements.
            PROFILE_CUSTOM (4):
                Custom profile. Allow only the set of allowed SSL features
                specified in the custom_features field of SslPolicy.
        """

        PROFILE_UNSPECIFIED = 0
        PROFILE_COMPATIBLE = 1
        PROFILE_MODERN = 2
        PROFILE_RESTRICTED = 3
        PROFILE_CUSTOM = 4

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
    ca_pool: str = proto.Field(
        proto.STRING,
        number=5,
    )
    trust_config: str = proto.Field(
        proto.STRING,
        number=6,
    )
    exclude_public_ca_set: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )
    min_tls_version: TlsVersion = proto.Field(
        proto.ENUM,
        number=8,
        enum=TlsVersion,
    )
    tls_feature_profile: Profile = proto.Field(
        proto.ENUM,
        number=9,
        enum=Profile,
    )
    custom_tls_features: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )


class CreateTlsInspectionPolicyRequest(proto.Message):
    r"""Request used by the CreateTlsInspectionPolicy method.

    Attributes:
        parent (str):
            Required. The parent resource of the TlsInspectionPolicy.
            Must be in the format
            ``projects/{project}/locations/{location}``.
        tls_inspection_policy_id (str):
            Required. Short name of the TlsInspectionPolicy resource to
            be created. This value should be 1-63 characters long,
            containing only letters, numbers, hyphens, and underscores,
            and should not start with a number. E.g.
            "tls_inspection_policy1".
        tls_inspection_policy (google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy):
            Required. TlsInspectionPolicy resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tls_inspection_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tls_inspection_policy: "TlsInspectionPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TlsInspectionPolicy",
    )


class ListTlsInspectionPoliciesRequest(proto.Message):
    r"""Request used with the ListTlsInspectionPolicies method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            TlsInspectionPolicies should be listed, specified in the
            format ``projects/{project}/locations/{location}``.
        page_size (int):
            Maximum number of TlsInspectionPolicies to
            return per call.
        page_token (str):
            The value returned by the last
            'ListTlsInspectionPoliciesResponse' Indicates
            that this is a continuation of a prior
            'ListTlsInspectionPolicies' call, and that the
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


class ListTlsInspectionPoliciesResponse(proto.Message):
    r"""Response returned by the ListTlsInspectionPolicies method.

    Attributes:
        tls_inspection_policies (MutableSequence[google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy]):
            List of TlsInspectionPolicies resources.
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

    tls_inspection_policies: MutableSequence["TlsInspectionPolicy"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="TlsInspectionPolicy",
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


class GetTlsInspectionPolicyRequest(proto.Message):
    r"""Request used by the GetTlsInspectionPolicy method.

    Attributes:
        name (str):
            Required. A name of the TlsInspectionPolicy to get. Must be
            in the format
            ``projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteTlsInspectionPolicyRequest(proto.Message):
    r"""Request used by the DeleteTlsInspectionPolicy method.

    Attributes:
        name (str):
            Required. A name of the TlsInspectionPolicy to delete. Must
            be in the format
            ``projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}``.
        force (bool):
            If set to true, any rules for this
            TlsInspectionPolicy will also be deleted.
            (Otherwise, the request will only work if the
            TlsInspectionPolicy has no rules.)
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class UpdateTlsInspectionPolicyRequest(proto.Message):
    r"""Request used by the UpdateTlsInspectionPolicy method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the TlsInspectionPolicy resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        tls_inspection_policy (google.cloud.network_security_v1alpha1.types.TlsInspectionPolicy):
            Required. Updated TlsInspectionPolicy
            resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    tls_inspection_policy: "TlsInspectionPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TlsInspectionPolicy",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
