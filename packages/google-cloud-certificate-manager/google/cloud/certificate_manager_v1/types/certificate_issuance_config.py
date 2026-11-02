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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.certificatemanager.v1",
    manifest={
        "ListCertificateIssuanceConfigsRequest",
        "ListCertificateIssuanceConfigsResponse",
        "GetCertificateIssuanceConfigRequest",
        "CreateCertificateIssuanceConfigRequest",
        "UpdateCertificateIssuanceConfigRequest",
        "DeleteCertificateIssuanceConfigRequest",
        "CertificateIssuanceConfig",
    },
)


class ListCertificateIssuanceConfigsRequest(proto.Message):
    r"""Request for the ``ListCertificateIssuanceConfigs`` method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            certificate should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. Maximum number of certificate
            configs to return per call.
        page_token (str):
            Optional. The value returned by the last
            ``ListCertificateIssuanceConfigsResponse``. Indicates that
            this is a continuation of a prior
            ``ListCertificateIssuanceConfigs`` call, and that the system
            should return the next page of data.
        filter (str):
            Optional. Filter expression to restrict the
            Certificates Configs returned.
        order_by (str):
            Optional. A list of Certificate Config field names used to
            specify the order of the returned results. The default
            sorting order is ascending. To specify descending order for
            a field, add a suffix ``" desc"``.
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


class ListCertificateIssuanceConfigsResponse(proto.Message):
    r"""Response for the ``ListCertificateIssuanceConfigs`` method.

    Attributes:
        certificate_issuance_configs (MutableSequence[google.cloud.certificate_manager_v1.types.CertificateIssuanceConfig]):
            A list of certificate configs for the parent
            resource.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    certificate_issuance_configs: MutableSequence["CertificateIssuanceConfig"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="CertificateIssuanceConfig",
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


class GetCertificateIssuanceConfigRequest(proto.Message):
    r"""Request for the ``GetCertificateIssuanceConfig`` method.

    Attributes:
        name (str):
            Required. A name of the certificate issuance config to
            describe. Must be in the format
            ``projects/*/locations/*/certificateIssuanceConfigs/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCertificateIssuanceConfigRequest(proto.Message):
    r"""Request for the ``CreateCertificateIssuanceConfig`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the certificate issuance
            config. Must be in the format ``projects/*/locations/*``.
        certificate_issuance_config_id (str):
            Required. A user-provided name of the
            certificate config.
        certificate_issuance_config (google.cloud.certificate_manager_v1.types.CertificateIssuanceConfig):
            Required. A definition of the certificate
            issuance config to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    certificate_issuance_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    certificate_issuance_config: "CertificateIssuanceConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CertificateIssuanceConfig",
    )


class UpdateCertificateIssuanceConfigRequest(proto.Message):
    r"""Request for the ``UpdateCertificateIssuanceConfig`` method.

    Attributes:
        certificate_issuance_config (google.cloud.certificate_manager_v1.types.CertificateIssuanceConfig):
            Required. A definition of the certificate
            issuance config to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask.
    """

    certificate_issuance_config: "CertificateIssuanceConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CertificateIssuanceConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCertificateIssuanceConfigRequest(proto.Message):
    r"""Request for the ``DeleteCertificateIssuanceConfig`` method.

    Attributes:
        name (str):
            Required. A name of the certificate issuance config to
            delete. Must be in the format
            ``projects/*/locations/*/certificateIssuanceConfigs/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CertificateIssuanceConfig(proto.Message):
    r"""CertificateIssuanceConfig specifies how to issue and manage a
    certificate.

    Attributes:
        name (str):
            Identifier. A user-defined name of the certificate issuance
            config. CertificateIssuanceConfig names must be unique
            globally and match pattern
            ``projects/*/locations/*/certificateIssuanceConfigs/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of a
            CertificateIssuanceConfig.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            CertificateIssuanceConfig.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with a
            CertificateIssuanceConfig.
        description (str):
            Optional. One or more paragraphs of text
            description of a CertificateIssuanceConfig.
        certificate_authority_config (google.cloud.certificate_manager_v1.types.CertificateIssuanceConfig.CertificateAuthorityConfig):
            Required. The CA that issues the workload
            certificate. It includes the CA address, type,
            authentication to CA service, etc.
        lifetime (google.protobuf.duration_pb2.Duration):
            Required. Workload certificate lifetime
            requested.
        rotation_window_percentage (int):
            Required. Specifies the percentage of elapsed
            time of the certificate lifetime to wait before
            renewing the certificate. Must be a number
            between 1-99, inclusive.
        key_algorithm (google.cloud.certificate_manager_v1.types.CertificateIssuanceConfig.KeyAlgorithm):
            Required. The key algorithm to use when
            generating the private key.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag
            keys/values directly bound to this resource. For
            example:

              "123/environment": "production",
              "123/costCenter": "marketing".
    """

    class KeyAlgorithm(proto.Enum):
        r"""The type of keypair to generate.

        Values:
            KEY_ALGORITHM_UNSPECIFIED (0):
                Unspecified key algorithm.
            RSA_2048 (1):
                Specifies RSA with a 2048-bit modulus.
            ECDSA_P256 (4):
                Specifies ECDSA with curve P256.
        """

        KEY_ALGORITHM_UNSPECIFIED = 0
        RSA_2048 = 1
        ECDSA_P256 = 4

    class CertificateAuthorityConfig(proto.Message):
        r"""The CA that issues the workload certificate. It includes CA
        address, type, authentication to CA service, etc.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            certificate_authority_service_config (google.cloud.certificate_manager_v1.types.CertificateIssuanceConfig.CertificateAuthorityConfig.CertificateAuthorityServiceConfig):
                Defines a CertificateAuthorityServiceConfig.

                This field is a member of `oneof`_ ``kind``.
        """

        class CertificateAuthorityServiceConfig(proto.Message):
            r"""Contains information required to contact CA service.

            Attributes:
                ca_pool (str):
                    Required. A CA pool resource used to issue a certificate.
                    The CA pool string has a relative resource path following
                    the form
                    "projects/{project}/locations/{location}/caPools/{ca_pool}".
            """

            ca_pool: str = proto.Field(
                proto.STRING,
                number=1,
            )

        certificate_authority_service_config: "CertificateIssuanceConfig.CertificateAuthorityConfig.CertificateAuthorityServiceConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="kind",
            message="CertificateIssuanceConfig.CertificateAuthorityConfig.CertificateAuthorityServiceConfig",
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    certificate_authority_config: CertificateAuthorityConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        message=CertificateAuthorityConfig,
    )
    lifetime: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    rotation_window_percentage: int = proto.Field(
        proto.INT32,
        number=8,
    )
    key_algorithm: KeyAlgorithm = proto.Field(
        proto.ENUM,
        number=9,
        enum=KeyAlgorithm,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
