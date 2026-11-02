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

from google.cloud.network_security_v1alpha1.types import tls

__protobuf__ = proto.module(
    package="google.cloud.networksecurity.v1alpha1",
    manifest={
        "ServerTlsPolicy",
        "ListServerTlsPoliciesRequest",
        "ListServerTlsPoliciesResponse",
        "GetServerTlsPolicyRequest",
        "CreateServerTlsPolicyRequest",
        "UpdateServerTlsPolicyRequest",
        "DeleteServerTlsPolicyRequest",
    },
)


class ServerTlsPolicy(proto.Message):
    r"""ServerTlsPolicy is a resource that specifies how a server should
    authenticate incoming requests. This resource itself does not affect
    configuration unless it is attached to a target HTTPS proxy or
    endpoint config selector resource.

    ServerTlsPolicy in the form accepted by Application Load Balancers
    can be attached only to TargetHttpsProxy with an ``EXTERNAL``,
    ``EXTERNAL_MANAGED`` or ``INTERNAL_MANAGED`` load balancing scheme.
    Traffic Director compatible ServerTlsPolicies can be attached to
    EndpointPolicy and TargetHttpsProxy with Traffic Director
    ``INTERNAL_SELF_MANAGED`` load balancing scheme.

    Attributes:
        name (str):
            Required. Name of the ServerTlsPolicy resource. It matches
            the pattern
            ``projects/*/locations/{location}/serverTlsPolicies/{server_tls_policy}``
        description (str):
            Free-text description of the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Set of label tags associated with the
            resource.
        allow_open (bool):
            This field applies only for Traffic Director policies. It is
            must be set to false for Application Load Balancer policies.

            Determines if server allows plaintext connections. If set to
            true, server allows plain text connections. By default, it
            is set to false. This setting is not exclusive of other
            encryption modes. For example, if ``allow_open`` and
            ``mtls_policy`` are set, server allows both plain text and
            mTLS connections. See documentation of other encryption
            modes to confirm compatibility.

            Consider using it if you wish to upgrade in place your
            deployment to TLS while having mixed TLS and non-TLS traffic
            reaching port :80.
        server_certificate (google.cloud.network_security_v1alpha1.types.CertificateProvider):
            Optional if policy is to be used with Traffic Director. For
            Application Load Balancers must be empty.

            Defines a mechanism to provision server identity (public and
            private keys). Cannot be combined with ``allow_open`` as a
            permissive mode that allows both plain text and TLS is not
            supported.
        mtls_policy (google.cloud.network_security_v1alpha1.types.ServerTlsPolicy.MTLSPolicy):
            This field is required if the policy is used with
            Application Load Balancers. This field can be empty for
            Traffic Director.

            Defines a mechanism to provision peer validation
            certificates for peer to peer authentication (Mutual TLS -
            mTLS). If not specified, client certificate will not be
            requested. The connection is treated as TLS and not mTLS. If
            ``allow_open`` and ``mtls_policy`` are set, server allows
            both plain text and mTLS connections.
    """

    class MTLSPolicy(proto.Message):
        r"""Specification of the MTLSPolicy.

        Attributes:
            client_validation_mode (google.cloud.network_security_v1alpha1.types.ServerTlsPolicy.MTLSPolicy.ClientValidationMode):
                When the client presents an invalid certificate or no
                certificate to the load balancer, the
                ``client_validation_mode`` specifies how the client
                connection is handled.

                Required if the policy is to be used with the Application
                Load Balancers. For Traffic Director it must be empty.
            client_validation_ca (MutableSequence[google.cloud.network_security_v1alpha1.types.ValidationCA]):
                Required if the policy is to be used with
                Traffic Director. For Application Load Balancers
                it must be empty.

                Defines the mechanism to obtain the Certificate
                Authority certificate to validate the client
                certificate.
            client_validation_trust_config (str):
                Reference to the TrustConfig from
                certificatemanager.googleapis.com namespace.

                If specified, the chain validation will be
                performed against certificates configured in the
                given TrustConfig.

                Allowed only if the policy is to be used with
                Application Load Balancers.
        """

        class ClientValidationMode(proto.Enum):
            r"""Mutual TLS certificate validation mode.

            Values:
                CLIENT_VALIDATION_MODE_UNSPECIFIED (0):
                    Not allowed.
                ALLOW_INVALID_OR_MISSING_CLIENT_CERT (1):
                    Allow connection even if certificate chain
                    validation of the client certificate failed or
                    no client certificate was presented. The proof
                    of possession of the private key is always
                    checked if client certificate was presented.
                    This mode requires the backend to implement
                    processing of data extracted from a client
                    certificate to authenticate the peer, or to
                    reject connections if the client certificate
                    fingerprint is missing.
                REJECT_INVALID (2):
                    Require a client certificate and allow connection to the
                    backend only if validation of the client certificate passed.

                    If set, requires a reference to non-empty TrustConfig
                    specified in ``client_validation_trust_config``.
            """

            CLIENT_VALIDATION_MODE_UNSPECIFIED = 0
            ALLOW_INVALID_OR_MISSING_CLIENT_CERT = 1
            REJECT_INVALID = 2

        client_validation_mode: "ServerTlsPolicy.MTLSPolicy.ClientValidationMode" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="ServerTlsPolicy.MTLSPolicy.ClientValidationMode",
            )
        )
        client_validation_ca: MutableSequence[tls.ValidationCA] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=tls.ValidationCA,
        )
        client_validation_trust_config: str = proto.Field(
            proto.STRING,
            number=4,
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
    allow_open: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    server_certificate: tls.CertificateProvider = proto.Field(
        proto.MESSAGE,
        number=7,
        message=tls.CertificateProvider,
    )
    mtls_policy: MTLSPolicy = proto.Field(
        proto.MESSAGE,
        number=8,
        message=MTLSPolicy,
    )


class ListServerTlsPoliciesRequest(proto.Message):
    r"""Request used by the ListServerTlsPolicies method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ServerTlsPolicies should be listed, specified in the format
            ``projects/*/locations/{location}``.
        page_size (int):
            Maximum number of ServerTlsPolicies to return
            per call.
        page_token (str):
            The value returned by the last
            ``ListServerTlsPoliciesResponse`` Indicates that this is a
            continuation of a prior ``ListServerTlsPolicies`` call, and
            that the system should return the next page of data.
        return_partial_success (bool):
            Optional. Setting this field to ``true`` will opt the
            request into returning the resources that are reachable, and
            into including the names of those that were unreachable in
            the [ListServerTlsPoliciesResponse.unreachable] field. This
            can only be ``true`` when reading across collections e.g.
            when ``parent`` is set to
            ``"projects/example/locations/-"``.
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


class ListServerTlsPoliciesResponse(proto.Message):
    r"""Response returned by the ListServerTlsPolicies method.

    Attributes:
        server_tls_policies (MutableSequence[google.cloud.network_security_v1alpha1.types.ServerTlsPolicy]):
            List of ServerTlsPolicy resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the request opts into
            ``return_partial_success`` and reading across collections
            e.g. when attempting to list all resources across all
            supported locations.
    """

    @property
    def raw_page(self):
        return self

    server_tls_policies: MutableSequence["ServerTlsPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ServerTlsPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetServerTlsPolicyRequest(proto.Message):
    r"""Request used by the GetServerTlsPolicy method.

    Attributes:
        name (str):
            Required. A name of the ServerTlsPolicy to get. Must be in
            the format
            ``projects/*/locations/{location}/serverTlsPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServerTlsPolicyRequest(proto.Message):
    r"""Request used by the CreateServerTlsPolicy method.

    Attributes:
        parent (str):
            Required. The parent resource of the ServerTlsPolicy. Must
            be in the format ``projects/*/locations/{location}``.
        server_tls_policy_id (str):
            Required. Short name of the ServerTlsPolicy resource to be
            created. This value should be 1-63 characters long,
            containing only letters, numbers, hyphens, and underscores,
            and should not start with a number. E.g.
            "server_mtls_policy".
        server_tls_policy (google.cloud.network_security_v1alpha1.types.ServerTlsPolicy):
            Required. ServerTlsPolicy resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    server_tls_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    server_tls_policy: "ServerTlsPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ServerTlsPolicy",
    )


class UpdateServerTlsPolicyRequest(proto.Message):
    r"""Request used by UpdateServerTlsPolicy method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ServerTlsPolicy resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        server_tls_policy (google.cloud.network_security_v1alpha1.types.ServerTlsPolicy):
            Required. Updated ServerTlsPolicy resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    server_tls_policy: "ServerTlsPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ServerTlsPolicy",
    )


class DeleteServerTlsPolicyRequest(proto.Message):
    r"""Request used by the DeleteServerTlsPolicy method.

    Attributes:
        name (str):
            Required. A name of the ServerTlsPolicy to delete. Must be
            in the format
            ``projects/*/locations/{location}/serverTlsPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
