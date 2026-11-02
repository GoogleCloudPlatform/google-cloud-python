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
        "ClientTlsPolicy",
        "ListClientTlsPoliciesRequest",
        "ListClientTlsPoliciesResponse",
        "GetClientTlsPolicyRequest",
        "CreateClientTlsPolicyRequest",
        "UpdateClientTlsPolicyRequest",
        "DeleteClientTlsPolicyRequest",
    },
)


class ClientTlsPolicy(proto.Message):
    r"""ClientTlsPolicy is a resource that specifies how a client
    should authenticate connections to backends of a service. This
    resource itself does not affect configuration unless it is
    attached to a backend service resource.

    Attributes:
        name (str):
            Required. Name of the ClientTlsPolicy resource. It matches
            the pattern
            ``projects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}``
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
            the resource.
        sni (str):
            Optional. Server Name Indication string to
            present to the server during TLS handshake. E.g:
            "secure.example.com".
        client_certificate (google.cloud.network_security_v1alpha1.types.CertificateProvider):
            Optional. Defines a mechanism to provision
            client identity (public and private keys) for
            peer to peer authentication. The presence of
            this dictates mTLS.
        server_validation_ca (MutableSequence[google.cloud.network_security_v1alpha1.types.ValidationCA]):
            Optional. Defines the mechanism to obtain the
            Certificate Authority certificate to validate
            the server certificate. If empty, client does
            not validate the server certificate.
    """

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
    sni: str = proto.Field(
        proto.STRING,
        number=6,
    )
    client_certificate: tls.CertificateProvider = proto.Field(
        proto.MESSAGE,
        number=7,
        message=tls.CertificateProvider,
    )
    server_validation_ca: MutableSequence[tls.ValidationCA] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=tls.ValidationCA,
    )


class ListClientTlsPoliciesRequest(proto.Message):
    r"""Request used by the ListClientTlsPolicies method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ClientTlsPolicies should be listed, specified in the format
            ``projects/*/locations/{location}``.
        page_size (int):
            Maximum number of ClientTlsPolicies to return
            per call.
        page_token (str):
            The value returned by the last
            ``ListClientTlsPoliciesResponse`` Indicates that this is a
            continuation of a prior ``ListClientTlsPolicies`` call, and
            that the system should return the next page of data.
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


class ListClientTlsPoliciesResponse(proto.Message):
    r"""Response returned by the ListClientTlsPolicies method.

    Attributes:
        client_tls_policies (MutableSequence[google.cloud.network_security_v1alpha1.types.ClientTlsPolicy]):
            List of ClientTlsPolicy resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
    """

    @property
    def raw_page(self):
        return self

    client_tls_policies: MutableSequence["ClientTlsPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ClientTlsPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetClientTlsPolicyRequest(proto.Message):
    r"""Request used by the GetClientTlsPolicy method.

    Attributes:
        name (str):
            Required. A name of the ClientTlsPolicy to get. Must be in
            the format
            ``projects/*/locations/{location}/clientTlsPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClientTlsPolicyRequest(proto.Message):
    r"""Request used by the CreateClientTlsPolicy method.

    Attributes:
        parent (str):
            Required. The parent resource of the ClientTlsPolicy. Must
            be in the format ``projects/*/locations/{location}``.
        client_tls_policy_id (str):
            Required. Short name of the ClientTlsPolicy resource to be
            created. This value should be 1-63 characters long,
            containing only letters, numbers, hyphens, and underscores,
            and should not start with a number. E.g.
            "client_mtls_policy".
        client_tls_policy (google.cloud.network_security_v1alpha1.types.ClientTlsPolicy):
            Required. ClientTlsPolicy resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_tls_policy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_tls_policy: "ClientTlsPolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ClientTlsPolicy",
    )


class UpdateClientTlsPolicyRequest(proto.Message):
    r"""Request used by UpdateClientTlsPolicy method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ClientTlsPolicy resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        client_tls_policy (google.cloud.network_security_v1alpha1.types.ClientTlsPolicy):
            Required. Updated ClientTlsPolicy resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    client_tls_policy: "ClientTlsPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ClientTlsPolicy",
    )


class DeleteClientTlsPolicyRequest(proto.Message):
    r"""Request used by the DeleteClientTlsPolicy method.

    Attributes:
        name (str):
            Required. A name of the ClientTlsPolicy to delete. Must be
            in the format
            ``projects/*/locations/{location}/clientTlsPolicies/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
