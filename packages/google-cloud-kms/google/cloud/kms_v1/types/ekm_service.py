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
    package="google.cloud.kms.v1",
    manifest={
        "ListEkmConnectionsRequest",
        "ListEkmConnectionsResponse",
        "GetEkmConnectionRequest",
        "CreateEkmConnectionRequest",
        "UpdateEkmConnectionRequest",
        "GetEkmConfigRequest",
        "UpdateEkmConfigRequest",
        "Certificate",
        "EkmConnection",
        "EkmConfig",
        "VerifyConnectivityRequest",
        "VerifyConnectivityResponse",
    },
)


class ListEkmConnectionsRequest(proto.Message):
    r"""Request message for
    [EkmService.ListEkmConnections][google.cloud.kms.v1.EkmService.ListEkmConnections].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the [EkmConnections][google.cloud.kms.v1.EkmConnection] to
            list, in the format ``projects/*/locations/*``.
        page_size (int):
            Optional. Optional limit on the number of
            [EkmConnections][google.cloud.kms.v1.EkmConnection] to
            include in the response. Further
            [EkmConnections][google.cloud.kms.v1.EkmConnection] can
            subsequently be obtained by including the
            [ListEkmConnectionsResponse.next_page_token][google.cloud.kms.v1.ListEkmConnectionsResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Optional pagination token, returned earlier via
            [ListEkmConnectionsResponse.next_page_token][google.cloud.kms.v1.ListEkmConnectionsResponse.next_page_token].
        filter (str):
            Optional. Only include resources that match the filter in
            the response. For more information, see `Sorting and
            filtering list
            results <https://cloud.google.com/kms/docs/sorting-and-filtering>`__.
        order_by (str):
            Optional. Specify how the results should be sorted. If not
            specified, the results will be sorted in the default order.
            For more information, see `Sorting and filtering list
            results <https://cloud.google.com/kms/docs/sorting-and-filtering>`__.
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


class ListEkmConnectionsResponse(proto.Message):
    r"""Response message for
    [EkmService.ListEkmConnections][google.cloud.kms.v1.EkmService.ListEkmConnections].

    Attributes:
        ekm_connections (MutableSequence[google.cloud.kms_v1.types.EkmConnection]):
            The list of
            [EkmConnections][google.cloud.kms.v1.EkmConnection].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListEkmConnectionsRequest.page_token][google.cloud.kms.v1.ListEkmConnectionsRequest.page_token]
            to retrieve the next page of results.
        total_size (int):
            The total number of
            [EkmConnections][google.cloud.kms.v1.EkmConnection] that
            matched the query.

            This field is not populated if
            [ListEkmConnectionsRequest.filter][google.cloud.kms.v1.ListEkmConnectionsRequest.filter]
            is applied.
    """

    @property
    def raw_page(self):
        return self

    ekm_connections: MutableSequence["EkmConnection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EkmConnection",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GetEkmConnectionRequest(proto.Message):
    r"""Request message for
    [EkmService.GetEkmConnection][google.cloud.kms.v1.EkmService.GetEkmConnection].

    Attributes:
        name (str):
            Required. The [name][google.cloud.kms.v1.EkmConnection.name]
            of the [EkmConnection][google.cloud.kms.v1.EkmConnection] to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEkmConnectionRequest(proto.Message):
    r"""Request message for
    [EkmService.CreateEkmConnection][google.cloud.kms.v1.EkmService.CreateEkmConnection].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the [EkmConnection][google.cloud.kms.v1.EkmConnection], in
            the format ``projects/*/locations/*``.
        ekm_connection_id (str):
            Required. It must be unique within a location and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``.
        ekm_connection (google.cloud.kms_v1.types.EkmConnection):
            Required. An
            [EkmConnection][google.cloud.kms.v1.EkmConnection] with
            initial field values.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ekm_connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ekm_connection: "EkmConnection" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EkmConnection",
    )


class UpdateEkmConnectionRequest(proto.Message):
    r"""Request message for
    [EkmService.UpdateEkmConnection][google.cloud.kms.v1.EkmService.UpdateEkmConnection].

    Attributes:
        ekm_connection (google.cloud.kms_v1.types.EkmConnection):
            Required. [EkmConnection][google.cloud.kms.v1.EkmConnection]
            with updated values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields to be updated in
            this request.
    """

    ekm_connection: "EkmConnection" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EkmConnection",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetEkmConfigRequest(proto.Message):
    r"""Request message for
    [EkmService.GetEkmConfig][google.cloud.kms.v1.EkmService.GetEkmConfig].

    Attributes:
        name (str):
            Required. The [name][google.cloud.kms.v1.EkmConfig.name] of
            the [EkmConfig][google.cloud.kms.v1.EkmConfig] to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateEkmConfigRequest(proto.Message):
    r"""Request message for
    [EkmService.UpdateEkmConfig][google.cloud.kms.v1.EkmService.UpdateEkmConfig].

    Attributes:
        ekm_config (google.cloud.kms_v1.types.EkmConfig):
            Required. [EkmConfig][google.cloud.kms.v1.EkmConfig] with
            updated values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields to be updated in
            this request.
    """

    ekm_config: "EkmConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EkmConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class Certificate(proto.Message):
    r"""A [Certificate][google.cloud.kms.v1.Certificate] represents an X.509
    certificate used to authenticate HTTPS connections to EKM replicas.

    Attributes:
        raw_der (bytes):
            Required. The raw certificate bytes in DER
            format.
        parsed (bool):
            Output only. True if the certificate was
            parsed successfully.
        issuer (str):
            Output only. The issuer distinguished name in RFC 2253
            format. Only present if
            [parsed][google.cloud.kms.v1.Certificate.parsed] is true.
        subject (str):
            Output only. The subject distinguished name in RFC 2253
            format. Only present if
            [parsed][google.cloud.kms.v1.Certificate.parsed] is true.
        subject_alternative_dns_names (MutableSequence[str]):
            Output only. The subject Alternative DNS names. Only present
            if [parsed][google.cloud.kms.v1.Certificate.parsed] is true.
        not_before_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The certificate is not valid before this time.
            Only present if
            [parsed][google.cloud.kms.v1.Certificate.parsed] is true.
        not_after_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The certificate is not valid after this time.
            Only present if
            [parsed][google.cloud.kms.v1.Certificate.parsed] is true.
        serial_number (str):
            Output only. The certificate serial number as a hex string.
            Only present if
            [parsed][google.cloud.kms.v1.Certificate.parsed] is true.
        sha256_fingerprint (str):
            Output only. The SHA-256 certificate fingerprint as a hex
            string. Only present if
            [parsed][google.cloud.kms.v1.Certificate.parsed] is true.
    """

    raw_der: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    parsed: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    issuer: str = proto.Field(
        proto.STRING,
        number=3,
    )
    subject: str = proto.Field(
        proto.STRING,
        number=4,
    )
    subject_alternative_dns_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    not_before_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    not_after_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    serial_number: str = proto.Field(
        proto.STRING,
        number=8,
    )
    sha256_fingerprint: str = proto.Field(
        proto.STRING,
        number=9,
    )


class EkmConnection(proto.Message):
    r"""An [EkmConnection][google.cloud.kms.v1.EkmConnection] represents an
    individual EKM connection. It can be used for creating
    [CryptoKeys][google.cloud.kms.v1.CryptoKey] and
    [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] with a
    [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of
    [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC], as
    well as performing cryptographic operations using keys created
    within the [EkmConnection][google.cloud.kms.v1.EkmConnection].

    Attributes:
        name (str):
            Output only. The resource name for the
            [EkmConnection][google.cloud.kms.v1.EkmConnection] in the
            format ``projects/*/locations/*/ekmConnections/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            [EkmConnection][google.cloud.kms.v1.EkmConnection] was
            created.
        service_resolvers (MutableSequence[google.cloud.kms_v1.types.EkmConnection.ServiceResolver]):
            Optional. A list of
            [ServiceResolvers][google.cloud.kms.v1.EkmConnection.ServiceResolver]
            where the EKM can be reached. There should be one
            ServiceResolver per EKM replica. Currently, only a single
            [ServiceResolver][google.cloud.kms.v1.EkmConnection.ServiceResolver]
            is supported.
        etag (str):
            Optional. Etag of the currently stored
            [EkmConnection][google.cloud.kms.v1.EkmConnection].
        key_management_mode (google.cloud.kms_v1.types.EkmConnection.KeyManagementMode):
            Optional. Describes who can perform control plane operations
            on the EKM. If unset, this defaults to
            [MANUAL][google.cloud.kms.v1.EkmConnection.KeyManagementMode.MANUAL].
        crypto_space_path (str):
            Optional. Identifies the EKM Crypto Space that this
            [EkmConnection][google.cloud.kms.v1.EkmConnection] maps to.
            Note: This field is required if
            [KeyManagementMode][google.cloud.kms.v1.EkmConnection.KeyManagementMode]
            is
            [CLOUD_KMS][google.cloud.kms.v1.EkmConnection.KeyManagementMode.CLOUD_KMS].
    """

    class KeyManagementMode(proto.Enum):
        r"""[KeyManagementMode][google.cloud.kms.v1.EkmConnection.KeyManagementMode]
        describes who can perform control plane cryptographic operations
        using this [EkmConnection][google.cloud.kms.v1.EkmConnection].

        Values:
            KEY_MANAGEMENT_MODE_UNSPECIFIED (0):
                Not specified.
            MANUAL (1):
                EKM-side key management operations on
                [CryptoKeys][google.cloud.kms.v1.CryptoKey] created with
                this [EkmConnection][google.cloud.kms.v1.EkmConnection] must
                be initiated from the EKM directly and cannot be performed
                from Cloud KMS. This means that:

                - When creating a
                  [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                  associated with this
                  [EkmConnection][google.cloud.kms.v1.EkmConnection], the
                  caller must supply the key path of pre-existing external
                  key material that will be linked to the
                  [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].
                - Destruction of external key material cannot be requested
                  via the Cloud KMS API and must be performed directly in
                  the EKM.
                - Automatic rotation of key material is not supported.
            CLOUD_KMS (2):
                All [CryptoKeys][google.cloud.kms.v1.CryptoKey] created with
                this [EkmConnection][google.cloud.kms.v1.EkmConnection] use
                EKM-side key management operations initiated from Cloud KMS.
                This means that:

                - When a
                  [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                  associated with this
                  [EkmConnection][google.cloud.kms.v1.EkmConnection] is
                  created, the EKM automatically generates new key material
                  and a new key path. The caller cannot supply the key path
                  of pre-existing external key material.
                - Destruction of external key material associated with this
                  [EkmConnection][google.cloud.kms.v1.EkmConnection] can be
                  requested by calling
                  [DestroyCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion].
                - Automatic rotation of key material is supported.
        """

        KEY_MANAGEMENT_MODE_UNSPECIFIED = 0
        MANUAL = 1
        CLOUD_KMS = 2

    class ServiceResolver(proto.Message):
        r"""A
        [ServiceResolver][google.cloud.kms.v1.EkmConnection.ServiceResolver]
        represents an EKM replica that can be reached within an
        [EkmConnection][google.cloud.kms.v1.EkmConnection].

        Attributes:
            service_directory_service (str):
                Required. The resource name of the Service Directory service
                pointing to an EKM replica, in the format
                ``projects/*/locations/*/namespaces/*/services/*``.
            endpoint_filter (str):
                Optional. The filter applied to the endpoints
                of the resolved service. If no filter is
                specified, all endpoints will be considered. An
                endpoint will be chosen arbitrarily from the
                filtered list for each request.

                For endpoint filter syntax and examples, see
                https://cloud.google.com/service-directory/docs/reference/rpc/google.cloud.servicedirectory.v1#resolveservicerequest.
            hostname (str):
                Required. The hostname of the EKM replica
                used at TLS and HTTP layers.
            server_certificates (MutableSequence[google.cloud.kms_v1.types.Certificate]):
                Required. A list of leaf server certificates used to
                authenticate HTTPS connections to the EKM replica.
                Currently, a maximum of 10
                [Certificate][google.cloud.kms.v1.Certificate] is supported.
        """

        service_directory_service: str = proto.Field(
            proto.STRING,
            number=1,
        )
        endpoint_filter: str = proto.Field(
            proto.STRING,
            number=2,
        )
        hostname: str = proto.Field(
            proto.STRING,
            number=3,
        )
        server_certificates: MutableSequence["Certificate"] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="Certificate",
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
    service_resolvers: MutableSequence[ServiceResolver] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=ServiceResolver,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=5,
    )
    key_management_mode: KeyManagementMode = proto.Field(
        proto.ENUM,
        number=6,
        enum=KeyManagementMode,
    )
    crypto_space_path: str = proto.Field(
        proto.STRING,
        number=7,
    )


class EkmConfig(proto.Message):
    r"""An [EkmConfig][google.cloud.kms.v1.EkmConfig] is a singleton
    resource that represents configuration parameters that apply to all
    [CryptoKeys][google.cloud.kms.v1.CryptoKey] and
    [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] with a
    [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of
    [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC] in
    a given project and location.

    Attributes:
        name (str):
            Output only. The resource name for the
            [EkmConfig][google.cloud.kms.v1.EkmConfig] in the format
            ``projects/*/locations/*/ekmConfig``.
        default_ekm_connection (str):
            Optional. Resource name of the default
            [EkmConnection][google.cloud.kms.v1.EkmConnection]. Setting
            this field to the empty string removes the default.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_ekm_connection: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VerifyConnectivityRequest(proto.Message):
    r"""Request message for
    [EkmService.VerifyConnectivity][google.cloud.kms.v1.EkmService.VerifyConnectivity].

    Attributes:
        name (str):
            Required. The [name][google.cloud.kms.v1.EkmConnection.name]
            of the [EkmConnection][google.cloud.kms.v1.EkmConnection] to
            verify.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VerifyConnectivityResponse(proto.Message):
    r"""Response message for
    [EkmService.VerifyConnectivity][google.cloud.kms.v1.EkmService.VerifyConnectivity].

    """


__all__ = tuple(sorted(__protobuf__.manifest))
