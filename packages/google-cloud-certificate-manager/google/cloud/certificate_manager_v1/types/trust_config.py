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
    package="google.cloud.certificatemanager.v1",
    manifest={
        "ListTrustConfigsRequest",
        "ListTrustConfigsResponse",
        "GetTrustConfigRequest",
        "CreateTrustConfigRequest",
        "UpdateTrustConfigRequest",
        "DeleteTrustConfigRequest",
        "TrustConfig",
    },
)


class ListTrustConfigsRequest(proto.Message):
    r"""Request for the ``ListTrustConfigs`` method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            TrustConfigs should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. Maximum number of TrustConfigs to
            return per call.
        page_token (str):
            Optional. The value returned by the last
            ``ListTrustConfigsResponse``. Indicates that this is a
            continuation of a prior ``ListTrustConfigs`` call, and that
            the system should return the next page of data.
        filter (str):
            Optional. Filter expression to restrict the
            TrustConfigs returned.
        order_by (str):
            Optional. A list of TrustConfig field names used to specify
            the order of the returned results. The default sorting order
            is ascending. To specify descending order for a field, add a
            suffix ``" desc"``.
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


class ListTrustConfigsResponse(proto.Message):
    r"""Response for the ``ListTrustConfigs`` method.

    Attributes:
        trust_configs (MutableSequence[google.cloud.certificate_manager_v1.types.TrustConfig]):
            A list of TrustConfigs for the parent
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

    trust_configs: MutableSequence["TrustConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TrustConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetTrustConfigRequest(proto.Message):
    r"""Request for the ``GetTrustConfig`` method.

    Attributes:
        name (str):
            Required. A name of the TrustConfig to describe. Must be in
            the format ``projects/*/locations/*/trustConfigs/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTrustConfigRequest(proto.Message):
    r"""Request for the ``CreateTrustConfig`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the TrustConfig. Must be in
            the format ``projects/*/locations/*``.
        trust_config_id (str):
            Required. A user-provided name of the TrustConfig. Must
            match the regexp ``[a-z0-9-]{1,63}``.
        trust_config (google.cloud.certificate_manager_v1.types.TrustConfig):
            Required. A definition of the TrustConfig to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trust_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trust_config: "TrustConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TrustConfig",
    )


class UpdateTrustConfigRequest(proto.Message):
    r"""Request for the ``UpdateTrustConfig`` method.

    Attributes:
        trust_config (google.cloud.certificate_manager_v1.types.TrustConfig):
            Required. A definition of the TrustConfig to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask.
    """

    trust_config: "TrustConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TrustConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteTrustConfigRequest(proto.Message):
    r"""Request for the ``DeleteTrustConfig`` method.

    Attributes:
        name (str):
            Required. A name of the TrustConfig to delete. Must be in
            the format ``projects/*/locations/*/trustConfigs/*``.
        etag (str):
            Optional. The current etag of the
            TrustConfig. If an etag is provided and does not
            match the current etag of the resource, deletion
            will be blocked and an ABORTED error will be
            returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TrustConfig(proto.Message):
    r"""Defines a trust config.

    Attributes:
        name (str):
            Identifier. A user-defined name of the trust config.
            TrustConfig names must be unique globally and match pattern
            ``projects/*/locations/*/trustConfigs/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of a
            TrustConfig.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            TrustConfig.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with a
            TrustConfig.
        description (str):
            Optional. One or more paragraphs of text
            description of a TrustConfig.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        spiffe_trust_stores (MutableMapping[str, google.cloud.certificate_manager_v1.types.TrustConfig.TrustStore]):
            Optional. Defines a mapping from a trust
            domain to a TrustStore. This is used for SPIFFE
            certificate validation.
        trust_stores (MutableSequence[google.cloud.certificate_manager_v1.types.TrustConfig.TrustStore]):
            Optional. Set of trust stores to perform
            validation against.
            This field is supported when TrustConfig is
            configured with Load Balancers, currently not
            supported for SPIFFE certificate validation.

            Only one TrustStore specified is currently
            allowed.
        allowlisted_certificates (MutableSequence[google.cloud.certificate_manager_v1.types.TrustConfig.AllowlistedCertificate]):
            Optional. A certificate matching an
            allowlisted certificate is always considered
            valid as long as the certificate is parseable,
            proof of private key possession is established,
            and constraints on the certificate's SAN field
            are met.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag
            keys/values directly bound to this resource. For
            example:

              "123/environment": "production",
              "123/costCenter": "marketing".
    """

    class TrustAnchor(proto.Message):
        r"""Defines a trust anchor.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            pem_certificate (str):
                PEM root certificate of the PKI used for
                validation.
                Each certificate provided in PEM format may
                occupy up to 5kB.

                This field is a member of `oneof`_ ``kind``.
        """

        pem_certificate: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="kind",
        )

    class IntermediateCA(proto.Message):
        r"""Defines an intermediate CA.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            pem_certificate (str):
                PEM intermediate certificate used for
                building up paths for validation.

                Each certificate provided in PEM format may
                occupy up to 5kB.

                This field is a member of `oneof`_ ``kind``.
        """

        pem_certificate: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="kind",
        )

    class TrustStore(proto.Message):
        r"""Defines a trust store.

        Attributes:
            trust_anchors (MutableSequence[google.cloud.certificate_manager_v1.types.TrustConfig.TrustAnchor]):
                Optional. List of Trust Anchors to be used
                while performing validation against a given
                TrustStore.
            intermediate_cas (MutableSequence[google.cloud.certificate_manager_v1.types.TrustConfig.IntermediateCA]):
                Optional. Set of intermediate CA certificates
                used for the path building phase of chain
                validation.

                The field is currently not supported if
                TrustConfig is used for the workload certificate
                feature.
        """

        trust_anchors: MutableSequence["TrustConfig.TrustAnchor"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="TrustConfig.TrustAnchor",
        )
        intermediate_cas: MutableSequence["TrustConfig.IntermediateCA"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="TrustConfig.IntermediateCA",
            )
        )

    class AllowlistedCertificate(proto.Message):
        r"""Defines an allowlisted certificate.

        Attributes:
            pem_certificate (str):
                Required. PEM certificate that is
                allowlisted. The certificate can be up to 5k
                bytes, and must be a parseable X.509
                certificate.
        """

        pem_certificate: str = proto.Field(
            proto.STRING,
            number=1,
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
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    spiffe_trust_stores: MutableMapping[str, TrustStore] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message=TrustStore,
    )
    trust_stores: MutableSequence[TrustStore] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=TrustStore,
    )
    allowlisted_certificates: MutableSequence[AllowlistedCertificate] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message=AllowlistedCertificate,
        )
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
