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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.networksecurity.v1beta1",
    manifest={
        "GrpcEndpoint",
        "ValidationCA",
        "CertificateProviderInstance",
        "CertificateProvider",
    },
)


class GrpcEndpoint(proto.Message):
    r"""Specification of the GRPC Endpoint.

    Attributes:
        target_uri (str):
            Required. The target URI of the gRPC
            endpoint. Only UDS path is supported, and should
            start with "unix:".
    """

    target_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ValidationCA(proto.Message):
    r"""Specification of ValidationCA. Defines the mechanism to
    obtain the Certificate Authority certificate to validate the
    peer certificate.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        grpc_endpoint (google.cloud.network_security_v1beta1.types.GrpcEndpoint):
            gRPC specific configuration to access the
            gRPC server to obtain the CA certificate.

            This field is a member of `oneof`_ ``type``.
        certificate_provider_instance (google.cloud.network_security_v1beta1.types.CertificateProviderInstance):
            The certificate provider instance
            specification that will be passed to the data
            plane, which will be used to load necessary
            credential information.

            This field is a member of `oneof`_ ``type``.
    """

    grpc_endpoint: "GrpcEndpoint" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type",
        message="GrpcEndpoint",
    )
    certificate_provider_instance: "CertificateProviderInstance" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type",
        message="CertificateProviderInstance",
    )


class CertificateProviderInstance(proto.Message):
    r"""Specification of a TLS certificate provider instance.
    Workloads may have one or more CertificateProvider instances
    (plugins) and one of them is enabled and configured by
    specifying this message. Workloads use the values from this
    message to locate and load the CertificateProvider instance
    configuration.

    Attributes:
        plugin_instance (str):
            Required. Plugin instance name, used to locate and load
            CertificateProvider instance configuration. Set to
            "google_cloud_private_spiffe" to use Certificate Authority
            Service certificate provider instance.
    """

    plugin_instance: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CertificateProvider(proto.Message):
    r"""Specification of certificate provider. Defines the mechanism
    to obtain the certificate and private key for peer to peer
    authentication.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        grpc_endpoint (google.cloud.network_security_v1beta1.types.GrpcEndpoint):
            gRPC specific configuration to access the
            gRPC server to obtain the cert and private key.

            This field is a member of `oneof`_ ``type``.
        certificate_provider_instance (google.cloud.network_security_v1beta1.types.CertificateProviderInstance):
            The certificate provider instance
            specification that will be passed to the data
            plane, which will be used to load necessary
            credential information.

            This field is a member of `oneof`_ ``type``.
    """

    grpc_endpoint: "GrpcEndpoint" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type",
        message="GrpcEndpoint",
    )
    certificate_provider_instance: "CertificateProviderInstance" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type",
        message="CertificateProviderInstance",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
