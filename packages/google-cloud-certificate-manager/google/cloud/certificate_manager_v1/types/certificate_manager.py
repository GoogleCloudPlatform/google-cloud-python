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
        "ServingState",
        "ListCertificatesRequest",
        "ListCertificatesResponse",
        "GetCertificateRequest",
        "CreateCertificateRequest",
        "UpdateCertificateRequest",
        "DeleteCertificateRequest",
        "ListCertificateMapsRequest",
        "ListCertificateMapsResponse",
        "GetCertificateMapRequest",
        "CreateCertificateMapRequest",
        "UpdateCertificateMapRequest",
        "DeleteCertificateMapRequest",
        "ListCertificateMapEntriesRequest",
        "ListCertificateMapEntriesResponse",
        "GetCertificateMapEntryRequest",
        "CreateCertificateMapEntryRequest",
        "UpdateCertificateMapEntryRequest",
        "DeleteCertificateMapEntryRequest",
        "ListDnsAuthorizationsRequest",
        "ListDnsAuthorizationsResponse",
        "GetDnsAuthorizationRequest",
        "CreateDnsAuthorizationRequest",
        "UpdateDnsAuthorizationRequest",
        "DeleteDnsAuthorizationRequest",
        "OperationMetadata",
        "Certificate",
        "CertificateMap",
        "CertificateMapEntry",
        "DnsAuthorization",
    },
)


class ServingState(proto.Enum):
    r"""Defines set of serving states associated with a resource.

    Values:
        SERVING_STATE_UNSPECIFIED (0):
            The status is undefined.
        ACTIVE (1):
            The configuration is serving.
        PENDING (2):
            Update is in progress. Some frontends may
            serve this configuration.
    """

    SERVING_STATE_UNSPECIFIED = 0
    ACTIVE = 1
    PENDING = 2


class ListCertificatesRequest(proto.Message):
    r"""Request for the ``ListCertificates`` method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            certificate should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. Maximum number of certificates to
            return per call.
        page_token (str):
            Optional. The value returned by the last
            ``ListCertificatesResponse``. Indicates that this is a
            continuation of a prior ``ListCertificates`` call, and that
            the system should return the next page of data.
        filter (str):
            Optional. Filter expression to restrict the
            Certificates returned.
        order_by (str):
            Optional. A list of Certificate field names used to specify
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


class ListCertificatesResponse(proto.Message):
    r"""Response for the ``ListCertificates`` method.

    Attributes:
        certificates (MutableSequence[google.cloud.certificate_manager_v1.types.Certificate]):
            A list of certificates for the parent
            resource.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            A list of locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    certificates: MutableSequence["Certificate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Certificate",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCertificateRequest(proto.Message):
    r"""Request for the ``GetCertificate`` method.

    Attributes:
        name (str):
            Required. A name of the certificate to describe. Must be in
            the format ``projects/*/locations/*/certificates/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCertificateRequest(proto.Message):
    r"""Request for the ``CreateCertificate`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the certificate. Must be in
            the format ``projects/*/locations/*``.
        certificate_id (str):
            Required. A user-provided name of the
            certificate.
        certificate (google.cloud.certificate_manager_v1.types.Certificate):
            Required. A definition of the certificate to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    certificate_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    certificate: "Certificate" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Certificate",
    )


class UpdateCertificateRequest(proto.Message):
    r"""Request for the ``UpdateCertificate`` method.

    Attributes:
        certificate (google.cloud.certificate_manager_v1.types.Certificate):
            Required. A definition of the certificate to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask.
    """

    certificate: "Certificate" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Certificate",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCertificateRequest(proto.Message):
    r"""Request for the ``DeleteCertificate`` method.

    Attributes:
        name (str):
            Required. A name of the certificate to delete. Must be in
            the format ``projects/*/locations/*/certificates/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCertificateMapsRequest(proto.Message):
    r"""Request for the ``ListCertificateMaps`` method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            certificate maps should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. Maximum number of certificate maps
            to return per call.
        page_token (str):
            Optional. The value returned by the last
            ``ListCertificateMapsResponse``. Indicates that this is a
            continuation of a prior ``ListCertificateMaps`` call, and
            that the system should return the next page of data.
        filter (str):
            Optional. Filter expression to restrict the
            Certificates Maps returned.
        order_by (str):
            Optional. A list of Certificate Map field names used to
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


class ListCertificateMapsResponse(proto.Message):
    r"""Response for the ``ListCertificateMaps`` method.

    Attributes:
        certificate_maps (MutableSequence[google.cloud.certificate_manager_v1.types.CertificateMap]):
            A list of certificate maps for the parent
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

    certificate_maps: MutableSequence["CertificateMap"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CertificateMap",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCertificateMapRequest(proto.Message):
    r"""Request for the ``GetCertificateMap`` method.

    Attributes:
        name (str):
            Required. A name of the certificate map to describe. Must be
            in the format ``projects/*/locations/*/certificateMaps/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCertificateMapRequest(proto.Message):
    r"""Request for the ``CreateCertificateMap`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the certificate map. Must
            be in the format ``projects/*/locations/*``.
        certificate_map_id (str):
            Required. A user-provided name of the
            certificate map.
        certificate_map (google.cloud.certificate_manager_v1.types.CertificateMap):
            Required. A definition of the certificate map
            to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    certificate_map_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    certificate_map: "CertificateMap" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CertificateMap",
    )


class UpdateCertificateMapRequest(proto.Message):
    r"""Request for the ``UpdateCertificateMap`` method.

    Attributes:
        certificate_map (google.cloud.certificate_manager_v1.types.CertificateMap):
            Required. A definition of the certificate map
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask.
    """

    certificate_map: "CertificateMap" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CertificateMap",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCertificateMapRequest(proto.Message):
    r"""Request for the ``DeleteCertificateMap`` method.

    Attributes:
        name (str):
            Required. A name of the certificate map to delete. Must be
            in the format ``projects/*/locations/*/certificateMaps/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCertificateMapEntriesRequest(proto.Message):
    r"""Request for the ``ListCertificateMapEntries`` method.

    Attributes:
        parent (str):
            Required. The project, location and certificate map from
            which the certificate map entries should be listed,
            specified in the format
            ``projects/*/locations/*/certificateMaps/*``.
        page_size (int):
            Optional. Maximum number of certificate map
            entries to return. The service may return fewer
            than this value. If unspecified, at most 50
            certificate map entries will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. The value returned by the last
            ``ListCertificateMapEntriesResponse``. Indicates that this
            is a continuation of a prior ``ListCertificateMapEntries``
            call, and that the system should return the next page of
            data.
        filter (str):
            Optional. Filter expression to restrict the
            returned Certificate Map Entries.
        order_by (str):
            Optional. A list of Certificate Map Entry field names used
            to specify the order of the returned results. The default
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


class ListCertificateMapEntriesResponse(proto.Message):
    r"""Response for the ``ListCertificateMapEntries`` method.

    Attributes:
        certificate_map_entries (MutableSequence[google.cloud.certificate_manager_v1.types.CertificateMapEntry]):
            A list of certificate map entries for the
            parent resource.
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

    certificate_map_entries: MutableSequence["CertificateMapEntry"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="CertificateMapEntry",
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


class GetCertificateMapEntryRequest(proto.Message):
    r"""Request for the ``GetCertificateMapEntry`` method.

    Attributes:
        name (str):
            Required. A name of the certificate map entry to describe.
            Must be in the format
            ``projects/*/locations/*/certificateMaps/*/certificateMapEntries/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCertificateMapEntryRequest(proto.Message):
    r"""Request for the ``CreateCertificateMapEntry`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the certificate map entry.
            Must be in the format
            ``projects/*/locations/*/certificateMaps/*``.
        certificate_map_entry_id (str):
            Required. A user-provided name of the
            certificate map entry.
        certificate_map_entry (google.cloud.certificate_manager_v1.types.CertificateMapEntry):
            Required. A definition of the certificate map
            entry to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    certificate_map_entry_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    certificate_map_entry: "CertificateMapEntry" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CertificateMapEntry",
    )


class UpdateCertificateMapEntryRequest(proto.Message):
    r"""Request for the ``UpdateCertificateMapEntry`` method.

    Attributes:
        certificate_map_entry (google.cloud.certificate_manager_v1.types.CertificateMapEntry):
            Required. A definition of the certificate map
            entry to create map entry.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask.
    """

    certificate_map_entry: "CertificateMapEntry" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CertificateMapEntry",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCertificateMapEntryRequest(proto.Message):
    r"""Request for the ``DeleteCertificateMapEntry`` method.

    Attributes:
        name (str):
            Required. A name of the certificate map entry to delete.
            Must be in the format
            ``projects/*/locations/*/certificateMaps/*/certificateMapEntries/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDnsAuthorizationsRequest(proto.Message):
    r"""Request for the ``ListDnsAuthorizations`` method.

    Attributes:
        parent (str):
            Required. The project and location from which the dns
            authorizations should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. Maximum number of dns
            authorizations to return per call.
        page_token (str):
            Optional. The value returned by the last
            ``ListDnsAuthorizationsResponse``. Indicates that this is a
            continuation of a prior ``ListDnsAuthorizations`` call, and
            that the system should return the next page of data.
        filter (str):
            Optional. Filter expression to restrict the
            Dns Authorizations returned.
        order_by (str):
            Optional. A list of Dns Authorization field names used to
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


class ListDnsAuthorizationsResponse(proto.Message):
    r"""Response for the ``ListDnsAuthorizations`` method.

    Attributes:
        dns_authorizations (MutableSequence[google.cloud.certificate_manager_v1.types.DnsAuthorization]):
            A list of dns authorizations for the parent
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

    dns_authorizations: MutableSequence["DnsAuthorization"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DnsAuthorization",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDnsAuthorizationRequest(proto.Message):
    r"""Request for the ``GetDnsAuthorization`` method.

    Attributes:
        name (str):
            Required. A name of the dns authorization to describe. Must
            be in the format
            ``projects/*/locations/*/dnsAuthorizations/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDnsAuthorizationRequest(proto.Message):
    r"""Request for the ``CreateDnsAuthorization`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the dns authorization. Must
            be in the format ``projects/*/locations/*``.
        dns_authorization_id (str):
            Required. A user-provided name of the dns
            authorization.
        dns_authorization (google.cloud.certificate_manager_v1.types.DnsAuthorization):
            Required. A definition of the dns
            authorization to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dns_authorization_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dns_authorization: "DnsAuthorization" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DnsAuthorization",
    )


class UpdateDnsAuthorizationRequest(proto.Message):
    r"""Request for the ``UpdateDnsAuthorization`` method.

    Attributes:
        dns_authorization (google.cloud.certificate_manager_v1.types.DnsAuthorization):
            Required. A definition of the dns
            authorization to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask.
    """

    dns_authorization: "DnsAuthorization" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DnsAuthorization",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteDnsAuthorizationRequest(proto.Message):
    r"""Request for the ``DeleteDnsAuthorization`` method.

    Attributes:
        name (str):
            Required. A name of the dns authorization to delete. Must be
            in the format
            ``projects/*/locations/*/dnsAuthorizations/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation. Output
    only.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            Name of the verb executed by the operation.
        status_message (str):
            Human-readable status of the operation, if
            any.
        requested_cancellation (bool):
            Identifies whether the user has requested cancellation of
            the operation. Operations that have successfully been
            cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of ``1``,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            API version used to start the operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Certificate(proto.Message):
    r"""Defines TLS certificate.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. A user-defined name of the certificate.
            Certificate names must be unique globally and match pattern
            ``projects/*/locations/*/certificates/*``.
        description (str):
            Optional. One or more paragraphs of text
            description of a certificate.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of a
            Certificate.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            Certificate.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with a
            Certificate.
        self_managed (google.cloud.certificate_manager_v1.types.Certificate.SelfManagedCertificate):
            If set, defines data of a self-managed
            certificate.

            This field is a member of `oneof`_ ``type``.
        managed (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate):
            If set, contains configuration and state of a
            managed certificate.

            This field is a member of `oneof`_ ``type``.
        managed_identity (google.cloud.certificate_manager_v1.types.Certificate.ManagedIdentityCertificate):
            If set, contains configuration and state of a
            managed identity certificate.

            This field is a member of `oneof`_ ``type``.
        san_dnsnames (MutableSequence[str]):
            Output only. The list of Subject Alternative
            Names of dnsName type defined in the certificate
            (see RFC 5280 4.2.1.6). Managed certificates
            that haven't been provisioned yet have this
            field populated with a value of the
            managed.domains field.
        pem_certificate (str):
            Output only. The PEM-encoded certificate
            chain.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The expiry timestamp of a
            Certificate.
        scope (google.cloud.certificate_manager_v1.types.Certificate.Scope):
            Optional. Immutable. The scope of the
            certificate.
        used_by (MutableSequence[google.cloud.certificate_manager_v1.types.Certificate.UsedBy]):
            Output only. The list of resources that use
            this Certificate.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag
            keys/values directly bound to this resource. For
            example:

              "123/environment": "production",
              "123/costCenter": "marketing".
    """

    class Scope(proto.Enum):
        r"""Certificate scope.

        Values:
            DEFAULT (0):
                Use the DEFAULT scope if you plan to use the
                certificate with global external Application
                Load Balancer, global external proxy Network
                Load Balancer, or any of the regional Google
                Cloud services.
            EDGE_CACHE (1):
                Use the EDGE_CACHE scope if you plan to use the certificate
                with Media CDN. The certificates are served from Edge Points
                of Presence. See
                https://cloud.google.com/vpc/docs/edge-locations.
            ALL_REGIONS (2):
                Use the ALL_REGIONS scope if you plan to use the certificate
                with cross-region internal Application Load Balancer. The
                certificates are served from all Google Cloud regions. See
                https://cloud.google.com/compute/docs/regions-zones.
            CLIENT_AUTH (3):
                Associated with certificates used as client
                certificates in Backend mTLS.
        """

        DEFAULT = 0
        EDGE_CACHE = 1
        ALL_REGIONS = 2
        CLIENT_AUTH = 3

    class SelfManagedCertificate(proto.Message):
        r"""Certificate data for a SelfManaged Certificate.
        SelfManaged Certificates are uploaded by the user. Updating such
        certificates before they expire remains the user's
        responsibility.

        Attributes:
            pem_certificate (str):
                Optional. Input only. The PEM-encoded
                certificate chain. Leaf certificate comes first,
                followed by intermediate ones if any.
            pem_private_key (str):
                Optional. Input only. The PEM-encoded private
                key of the leaf certificate.
        """

        pem_certificate: str = proto.Field(
            proto.STRING,
            number=1,
        )
        pem_private_key: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class ManagedCertificate(proto.Message):
        r"""Configuration and state of a Managed Certificate.
        Certificate Manager provisions and renews Managed Certificates
        automatically, for as long as it's authorized to do so.

        Attributes:
            domains (MutableSequence[str]):
                Optional. Immutable. The domains for which a
                managed SSL certificate will be generated.
                Wildcard domains are only supported with DNS
                challenge resolution.
            dns_authorizations (MutableSequence[str]):
                Optional. Immutable. Authorizations that will
                be used for performing domain authorization.
            issuance_config (str):
                Optional. Immutable. The resource name for a
                [CertificateIssuanceConfig][google.cloud.certificatemanager.v1.CertificateIssuanceConfig]
                used to configure private PKI certificates in the format
                ``projects/*/locations/*/certificateIssuanceConfigs/*``. If
                this field is not set, the certificates will instead be
                publicly signed as documented at
                https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa.
            state (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.State):
                Output only. State of the managed certificate
                resource.
            provisioning_issue (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.ProvisioningIssue):
                Output only. Information about issues with
                provisioning a Managed Certificate.
            authorization_attempt_info (MutableSequence[google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.AuthorizationAttemptInfo]):
                Output only. Detailed state of the latest
                authorization attempt for each domain specified
                for managed certificate resource.
        """

        class State(proto.Enum):
            r"""State of the managed certificate resource.

            Values:
                STATE_UNSPECIFIED (0):
                    State is unspecified.
                PROVISIONING (1):
                    Certificate Manager attempts to provision or renew the
                    certificate. If the process takes longer than expected,
                    consult the ``provisioning_issue`` field.
                FAILED (2):
                    Multiple certificate provisioning attempts failed and
                    Certificate Manager gave up. To try again, delete and create
                    a new managed Certificate resource. For details see the
                    ``provisioning_issue`` field.
                ACTIVE (3):
                    The certificate management is working, and a
                    certificate has been provisioned.
            """

            STATE_UNSPECIFIED = 0
            PROVISIONING = 1
            FAILED = 2
            ACTIVE = 3

        class ProvisioningIssue(proto.Message):
            r"""Information about issues with provisioning a Managed
            Certificate.

            Attributes:
                reason (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.ProvisioningIssue.Reason):
                    Output only. Reason for provisioning
                    failures.
                details (str):
                    Output only. Human readable explanation about
                    the issue. Provided to help address the
                    configuration issues. Not guaranteed to be
                    stable. For programmatic access use Reason enum.
            """

            class Reason(proto.Enum):
                r"""Reason for provisioning failures.

                Values:
                    REASON_UNSPECIFIED (0):
                        Reason is unspecified.
                    AUTHORIZATION_ISSUE (1):
                        Certificate provisioning failed due to an issue with one or
                        more of the domains on the certificate. For details of which
                        domains failed, consult the ``authorization_attempt_info``
                        field.
                    RATE_LIMITED (2):
                        Exceeded Certificate Authority quotas or
                        internal rate limits of the system. Provisioning
                        may take longer to complete.
                """

                REASON_UNSPECIFIED = 0
                AUTHORIZATION_ISSUE = 1
                RATE_LIMITED = 2

            reason: "Certificate.ManagedCertificate.ProvisioningIssue.Reason" = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="Certificate.ManagedCertificate.ProvisioningIssue.Reason",
                )
            )
            details: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class AuthorizationAttemptInfo(proto.Message):
            r"""State of the latest attempt to authorize a domain for
            certificate issuance.

            Attributes:
                domain (str):
                    Output only. Domain name of the authorization
                    attempt.
                state (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.AuthorizationAttemptInfo.State):
                    Output only. State of the domain for managed
                    certificate issuance.
                failure_reason (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason):
                    Output only. Reason for failure of the
                    authorization attempt for the domain.
                details (str):
                    Output only. Human readable explanation for
                    reaching the state. Provided to help address the
                    configuration issues. Not guaranteed to be
                    stable. For programmatic access use
                    FailureReason enum.
                attempt_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. The timestamp, when the
                    authorization attempt was made.
                troubleshooting (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting):
                    Output only. Troubleshooting information for
                    the authorization attempt. This field is only
                    populated if the authorization attempt failed.
            """

            class State(proto.Enum):
                r"""State of the domain for managed certificate issuance.

                Values:
                    STATE_UNSPECIFIED (0):
                        State is unspecified.
                    AUTHORIZING (1):
                        Certificate provisioning for this domain is
                        under way. Google Cloud will attempt to
                        authorize the domain.
                    AUTHORIZED (6):
                        A managed certificate can be provisioned, no
                        issues for this domain.
                    FAILED (7):
                        Attempt to authorize the domain failed. This prevents the
                        Managed Certificate from being issued. See
                        ``failure_reason`` and ``details`` fields for more
                        information.
                """

                STATE_UNSPECIFIED = 0
                AUTHORIZING = 1
                AUTHORIZED = 6
                FAILED = 7

            class FailureReason(proto.Enum):
                r"""Reason for failure of the authorization attempt for the
                domain.

                Values:
                    FAILURE_REASON_UNSPECIFIED (0):
                        FailureReason is unspecified.
                    CONFIG (1):
                        There was a problem with the user's DNS or
                        load balancer configuration for this domain.
                    CAA (2):
                        Certificate issuance forbidden by an explicit
                        CAA record for the domain or a failure to check
                        CAA records for the domain.
                    RATE_LIMITED (3):
                        Reached a CA or internal rate-limit for the
                        domain, e.g. for certificates per top-level
                        private domain.
                """

                FAILURE_REASON_UNSPECIFIED = 0
                CONFIG = 1
                CAA = 2
                RATE_LIMITED = 3

            class Troubleshooting(proto.Message):
                r"""Troubleshooting information for the authorization attempt.

                Attributes:
                    issues (MutableSequence[google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.Issue]):
                        Output only. The list of issues discovered
                        during the authorization attempt.
                    cname (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.CNAME):
                        Output only. CNAME troubleshooting
                        information.
                    ips (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.IPs):
                        Output only. IPs troubleshooting information.
                """

                class Issue(proto.Enum):
                    r"""The issue discovered during the authorization attempt.

                    Values:
                        ISSUE_UNSPECIFIED (0):
                            Issue is unspecified.
                        CNAME_MISMATCH (1):
                            The resolved CNAME value doesn't match the
                            expected CNAME.
                        RESOLVED_TO_NOT_SERVING (2):
                            Domain has A/AAAA records that point to IPs,
                            where the certificate is not attached.
                        RESOLVED_TO_SERVING_ON_ALT_PORTS (3):
                            Domain has A/AAAA records that point to IPs,
                            where the certificate is attached, but port 443
                            is not open.
                        NO_RESOLVED_IPS (4):
                            Domain doesn't have any A/AAAA records.
                        CERTIFICATE_NOT_ATTACHED (5):
                            Certificate is not configured to be served
                            from any IPs (e.g. Certificate is not attached
                            to any load balancer).
                    """

                    ISSUE_UNSPECIFIED = 0
                    CNAME_MISMATCH = 1
                    RESOLVED_TO_NOT_SERVING = 2
                    RESOLVED_TO_SERVING_ON_ALT_PORTS = 3
                    NO_RESOLVED_IPS = 4
                    CERTIFICATE_NOT_ATTACHED = 5

                class CNAME(proto.Message):
                    r"""CNAME troubleshooting information.

                    Attributes:
                        name (str):
                            Output only. The name of the CNAME record for the domain,
                            equals to ``dns_resource_record.name`` in the corresponding
                            ``DnsAuthorization``.
                        expected_data (str):
                            Output only. The expected value of the CNAME record for the
                            domain, equals to ``dns_resource_record.data`` in the
                            corresponding ``DnsAuthorization``.
                        resolved_data (MutableSequence[str]):
                            Output only. The resolved CNAME chain. Empty list if the
                            CNAME record for ``CNAME.name`` is not found. Otherwise the
                            first item is the value of the CNAME record for
                            ``CNAME.name``. If the CNAME chain is longer, the second
                            item is the value of the CNAME record for the first item,
                            and so on.
                    """

                    name: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )
                    expected_data: str = proto.Field(
                        proto.STRING,
                        number=2,
                    )
                    resolved_data: MutableSequence[str] = proto.RepeatedField(
                        proto.STRING,
                        number=3,
                    )

                class IPs(proto.Message):
                    r"""IPs troubleshooting information.

                    Attributes:
                        serving (MutableSequence[str]):
                            Output only. The list of IP addresses, where
                            the certificate is attached and port 443 is
                            open.
                        serving_on_alt_ports (MutableSequence[str]):
                            Output only. The list of IP addresses, where
                            the certificate is attached, but port 443 is not
                            open.
                        resolved (MutableSequence[str]):
                            Output only. The list of IP addresses
                            resolved from the domain's A/AAAA records. Can
                            contain both ipv4 and ipv6 addresses.
                    """

                    serving: MutableSequence[str] = proto.RepeatedField(
                        proto.STRING,
                        number=1,
                    )
                    serving_on_alt_ports: MutableSequence[str] = proto.RepeatedField(
                        proto.STRING,
                        number=2,
                    )
                    resolved: MutableSequence[str] = proto.RepeatedField(
                        proto.STRING,
                        number=3,
                    )

                issues: MutableSequence[
                    "Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.Issue"
                ] = proto.RepeatedField(
                    proto.ENUM,
                    number=1,
                    enum="Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.Issue",
                )
                cname: "Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.CNAME" = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.CNAME",
                )
                ips: "Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.IPs" = proto.Field(
                    proto.MESSAGE,
                    number=3,
                    message="Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.IPs",
                )

            domain: str = proto.Field(
                proto.STRING,
                number=1,
            )
            state: "Certificate.ManagedCertificate.AuthorizationAttemptInfo.State" = proto.Field(
                proto.ENUM,
                number=2,
                enum="Certificate.ManagedCertificate.AuthorizationAttemptInfo.State",
            )
            failure_reason: "Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason" = proto.Field(
                proto.ENUM,
                number=3,
                enum="Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason",
            )
            details: str = proto.Field(
                proto.STRING,
                number=4,
            )
            attempt_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=5,
                message=timestamp_pb2.Timestamp,
            )
            troubleshooting: "Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting" = proto.Field(
                proto.MESSAGE,
                number=6,
                message="Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting",
            )

        domains: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        dns_authorizations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        issuance_config: str = proto.Field(
            proto.STRING,
            number=6,
        )
        state: "Certificate.ManagedCertificate.State" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Certificate.ManagedCertificate.State",
        )
        provisioning_issue: "Certificate.ManagedCertificate.ProvisioningIssue" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="Certificate.ManagedCertificate.ProvisioningIssue",
            )
        )
        authorization_attempt_info: MutableSequence[
            "Certificate.ManagedCertificate.AuthorizationAttemptInfo"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="Certificate.ManagedCertificate.AuthorizationAttemptInfo",
        )

    class ManagedIdentityCertificate(proto.Message):
        r"""Configuration and state of a Managed Identity Certificate.
        Certificate Manager provisions and renews Managed Identity
        Certificates automatically, for as long as it's authorized to do
        so.

        Attributes:
            identity (str):
                Required. Immutable. SPIFFE ID of the Managed
                Identity used for this certificate.
            state (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.State):
                Output only. State of the managed certificate
                resource.
            provisioning_issue (google.cloud.certificate_manager_v1.types.Certificate.ManagedCertificate.ProvisioningIssue):
                Output only. Information about issues with
                provisioning a managed certificate.
        """

        identity: str = proto.Field(
            proto.STRING,
            number=1,
        )
        state: "Certificate.ManagedCertificate.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Certificate.ManagedCertificate.State",
        )
        provisioning_issue: "Certificate.ManagedCertificate.ProvisioningIssue" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="Certificate.ManagedCertificate.ProvisioningIssue",
            )
        )

    class UsedBy(proto.Message):
        r"""Defines a resource that uses the certificate.

        Attributes:
            name (str):
                Output only. Full name of the resource
                https://google.aip.dev/122#full-resource-names, e.g.
                ``//certificatemanager.googleapis.com/projects/*/locations/*/certificateMaps/*/certificateMapEntries/*``
                or
                ``//compute.googleapis.com/projects/*/locations/*/targetHttpsProxies/*``.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
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
    self_managed: SelfManagedCertificate = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="type",
        message=SelfManagedCertificate,
    )
    managed: ManagedCertificate = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="type",
        message=ManagedCertificate,
    )
    managed_identity: ManagedIdentityCertificate = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="type",
        message=ManagedIdentityCertificate,
    )
    san_dnsnames: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    pem_certificate: str = proto.Field(
        proto.STRING,
        number=9,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    scope: Scope = proto.Field(
        proto.ENUM,
        number=12,
        enum=Scope,
    )
    used_by: MutableSequence[UsedBy] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=UsedBy,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=17,
    )


class CertificateMap(proto.Message):
    r"""Defines a collection of certificate configurations.

    Attributes:
        name (str):
            Identifier. A user-defined name of the Certificate Map.
            Certificate Map names must be unique globally and match
            pattern ``projects/*/locations/*/certificateMaps/*``.
        description (str):
            Optional. One or more paragraphs of text
            description of a certificate map.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of a
            Certificate Map.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp of a
            Certificate Map.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with a
            Certificate Map.
        gclb_targets (MutableSequence[google.cloud.certificate_manager_v1.types.CertificateMap.GclbTarget]):
            Output only. A list of GCLB targets that use
            this Certificate Map. A Target Proxy is only
            present on this list if it's attached to a
            Forwarding Rule.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag
            keys/values directly bound to this resource. For
            example:

              "123/environment": "production",
              "123/costCenter": "marketing".
    """

    class GclbTarget(proto.Message):
        r"""Describes a Target Proxy that uses this Certificate Map.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            target_https_proxy (str):
                Output only. This field returns the resource name in the
                following format:
                ``//compute.googleapis.com/projects/*/global/targetHttpsProxies/*``.

                This field is a member of `oneof`_ ``target_proxy``.
            target_ssl_proxy (str):
                Output only. This field returns the resource name in the
                following format:
                ``//compute.googleapis.com/projects/*/global/targetSslProxies/*``.

                This field is a member of `oneof`_ ``target_proxy``.
            ip_configs (MutableSequence[google.cloud.certificate_manager_v1.types.CertificateMap.GclbTarget.IpConfig]):
                Output only. IP configurations for this
                Target Proxy where the Certificate Map is
                serving.
        """

        class IpConfig(proto.Message):
            r"""Defines IP configuration where this Certificate Map is
            serving.

            Attributes:
                ip_address (str):
                    Output only. An external IP address.
                ports (MutableSequence[int]):
                    Output only. Ports.
            """

            ip_address: str = proto.Field(
                proto.STRING,
                number=1,
            )
            ports: MutableSequence[int] = proto.RepeatedField(
                proto.UINT32,
                number=3,
            )

        target_https_proxy: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="target_proxy",
        )
        target_ssl_proxy: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="target_proxy",
        )
        ip_configs: MutableSequence["CertificateMap.GclbTarget.IpConfig"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="CertificateMap.GclbTarget.IpConfig",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    gclb_targets: MutableSequence[GclbTarget] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=GclbTarget,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )


class CertificateMapEntry(proto.Message):
    r"""Defines a certificate map entry.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. A user-defined name of the Certificate Map
            Entry. Certificate Map Entry names must be unique globally
            and match pattern
            ``projects/*/locations/*/certificateMaps/*/certificateMapEntries/*``.
        description (str):
            Optional. One or more paragraphs of text
            description of a certificate map entry.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of a
            Certificate Map Entry.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp of a
            Certificate Map Entry.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with a
            Certificate Map Entry.
        hostname (str):
            A Hostname (FQDN, e.g. ``example.com``) or a wildcard
            hostname expression (``*.example.com``) for a set of
            hostnames with common suffix. Used as Server Name Indication
            (SNI) for selecting a proper certificate.

            This field is a member of `oneof`_ ``match``.
        matcher (google.cloud.certificate_manager_v1.types.CertificateMapEntry.Matcher):
            A predefined matcher for particular cases,
            other than SNI selection.

            This field is a member of `oneof`_ ``match``.
        certificates (MutableSequence[str]):
            Optional. A set of Certificates defines for the given
            ``hostname``. There can be defined up to four certificates
            in each Certificate Map Entry. Each certificate must match
            pattern ``projects/*/locations/*/certificates/*``.
        state (google.cloud.certificate_manager_v1.types.ServingState):
            Output only. A serving state of this
            Certificate Map Entry.
    """

    class Matcher(proto.Enum):
        r"""Defines predefined cases other than SNI-hostname match when
        this configuration should be applied.

        Values:
            MATCHER_UNSPECIFIED (0):
                A matcher has't been recognized.
            PRIMARY (1):
                A primary certificate that is served when SNI
                wasn't specified in the request or SNI couldn't
                be found in the map.
        """

        MATCHER_UNSPECIFIED = 0
        PRIMARY = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
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
    hostname: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="match",
    )
    matcher: Matcher = proto.Field(
        proto.ENUM,
        number=10,
        oneof="match",
        enum=Matcher,
    )
    certificates: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    state: "ServingState" = proto.Field(
        proto.ENUM,
        number=8,
        enum="ServingState",
    )


class DnsAuthorization(proto.Message):
    r"""A DnsAuthorization resource describes a way to perform domain
    authorization for certificate issuance.

    Attributes:
        name (str):
            Identifier. A user-defined name of the dns authorization.
            DnsAuthorization names must be unique globally and match
            pattern ``projects/*/locations/*/dnsAuthorizations/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of a
            DnsAuthorization.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            DnsAuthorization.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with a
            DnsAuthorization.
        description (str):
            Optional. One or more paragraphs of text
            description of a DnsAuthorization.
        domain (str):
            Required. Immutable. A domain that is being authorized. A
            DnsAuthorization resource covers a single domain and its
            wildcard, e.g. authorization for ``example.com`` can be used
            to issue certificates for ``example.com`` and
            ``*.example.com``.
        dns_resource_record (google.cloud.certificate_manager_v1.types.DnsAuthorization.DnsResourceRecord):
            Output only. DNS Resource Record that needs
            to be added to DNS configuration.
        type_ (google.cloud.certificate_manager_v1.types.DnsAuthorization.Type):
            Optional. Immutable. Type of DnsAuthorization. If unset
            during resource creation the following default will be used:

            - in location ``global``: FIXED_RECORD,
            - in other locations: PER_PROJECT_RECORD.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag
            keys/values directly bound to this resource. For
            example:

              "123/environment": "production",
              "123/costCenter": "marketing".
    """

    class Type(proto.Enum):
        r"""DnsAuthorization type.

        Values:
            TYPE_UNSPECIFIED (0):
                Type is unspecified.
            FIXED_RECORD (1):
                FIXED_RECORD DNS authorization uses DNS-01 validation
                method.
            PER_PROJECT_RECORD (2):
                PER_PROJECT_RECORD DNS authorization allows for independent
                management of Google-managed certificates with DNS
                authorization across multiple projects.
        """

        TYPE_UNSPECIFIED = 0
        FIXED_RECORD = 1
        PER_PROJECT_RECORD = 2

    class DnsResourceRecord(proto.Message):
        r"""The structure describing the DNS Resource Record that needs
        to be added to DNS configuration for the authorization to be
        usable by certificate.

        Attributes:
            name (str):
                Output only. Fully qualified name of the DNS Resource
                Record. e.g. ``_acme-challenge.example.com``
            type_ (str):
                Output only. Type of the DNS Resource Record.
                Currently always set to "CNAME".
            data (str):
                Output only. Data of the DNS Resource Record.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=2,
        )
        data: str = proto.Field(
            proto.STRING,
            number=3,
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
    domain: str = proto.Field(
        proto.STRING,
        number=6,
    )
    dns_resource_record: DnsResourceRecord = proto.Field(
        proto.MESSAGE,
        number=10,
        message=DnsResourceRecord,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=11,
        enum=Type,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
