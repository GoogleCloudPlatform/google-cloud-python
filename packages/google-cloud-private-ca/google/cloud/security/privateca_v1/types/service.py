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

from google.cloud.security.privateca_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.security.privateca.v1",
    manifest={
        "CreateCertificateRequest",
        "GetCertificateRequest",
        "ListCertificatesRequest",
        "ListCertificatesResponse",
        "RevokeCertificateRequest",
        "UpdateCertificateRequest",
        "ActivateCertificateAuthorityRequest",
        "CreateCertificateAuthorityRequest",
        "DisableCertificateAuthorityRequest",
        "EnableCertificateAuthorityRequest",
        "FetchCertificateAuthorityCsrRequest",
        "FetchCertificateAuthorityCsrResponse",
        "GetCertificateAuthorityRequest",
        "ListCertificateAuthoritiesRequest",
        "ListCertificateAuthoritiesResponse",
        "UndeleteCertificateAuthorityRequest",
        "DeleteCertificateAuthorityRequest",
        "UpdateCertificateAuthorityRequest",
        "CreateCaPoolRequest",
        "UpdateCaPoolRequest",
        "DeleteCaPoolRequest",
        "FetchCaCertsRequest",
        "FetchCaCertsResponse",
        "GetCaPoolRequest",
        "ListCaPoolsRequest",
        "ListCaPoolsResponse",
        "GetCertificateRevocationListRequest",
        "ListCertificateRevocationListsRequest",
        "ListCertificateRevocationListsResponse",
        "UpdateCertificateRevocationListRequest",
        "CreateCertificateTemplateRequest",
        "DeleteCertificateTemplateRequest",
        "GetCertificateTemplateRequest",
        "ListCertificateTemplatesRequest",
        "ListCertificateTemplatesResponse",
        "UpdateCertificateTemplateRequest",
        "OperationMetadata",
    },
)


class CreateCertificateRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.CreateCertificate][google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificate].

    Attributes:
        parent (str):
            Required. The resource name of the
            [CaPool][google.cloud.security.privateca.v1.CaPool]
            associated with the
            [Certificate][google.cloud.security.privateca.v1.Certificate],
            in the format ``projects/*/locations/*/caPools/*``.
        certificate_id (str):
            Optional. It must be unique within a location and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``. This field is
            required when using a
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in the Enterprise
            [CertificateAuthority.tier][google.cloud.security.privateca.v1.CertificateAuthority.tier],
            but is optional and its value is ignored otherwise.
        certificate (google.cloud.security.privateca_v1.types.Certificate):
            Required. A
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            with initial field values.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. If this is true, no
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            resource will be persisted regardless of the
            [CaPool][google.cloud.security.privateca.v1.CaPool]'s
            [tier][google.cloud.security.privateca.v1.CaPool.tier], and
            the returned
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            will not contain the
            [pem_certificate][google.cloud.security.privateca.v1.Certificate.pem_certificate]
            field.
        issuing_certificate_authority_id (str):
            Optional. The resource ID of the
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            that should issue the certificate. This optional field will
            ignore the load-balancing scheme of the Pool and directly
            issue the certificate from the CA with the specified ID,
            contained in the same
            [CaPool][google.cloud.security.privateca.v1.CaPool]
            referenced by ``parent``. Per-CA quota rules apply. If left
            empty, a
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            will be chosen from the
            [CaPool][google.cloud.security.privateca.v1.CaPool] by the
            service. For example, to issue a
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            from a Certificate Authority with resource name
            "projects/my-project/locations/us-central1/caPools/my-pool/certificateAuthorities/my-ca",
            you can set the
            [parent][google.cloud.security.privateca.v1.CreateCertificateRequest.parent]
            to
            "projects/my-project/locations/us-central1/caPools/my-pool"
            and the
            [issuing_certificate_authority_id][google.cloud.security.privateca.v1.CreateCertificateRequest.issuing_certificate_authority_id]
            to "my-ca".
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    certificate_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    certificate: resources.Certificate = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Certificate,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    issuing_certificate_authority_id: str = proto.Field(
        proto.STRING,
        number=6,
    )


class GetCertificateRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.GetCertificate][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificate].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.security.privateca.v1.Certificate.name]
            of the
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCertificatesRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.ListCertificates][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificates].

    Attributes:
        parent (str):
            Required. The resource name of the parent associated with
            the
            [Certificates][google.cloud.security.privateca.v1.Certificate],
            in the format ``projects/*/locations/*/caPools/*``. The
            parent resource name can be in one of two forms:

            1. **Specific CA Pool:** To list certificates within a
               single CA Pool: ``projects/*/locations/*/caPools/*``

            2. **All CA Pools in a Location:** To list certificates
               across *all* CA Pools in a given project and location,
               use the wildcard character (``-``) in place of the CA
               Pool ID. Example: ``projects/*/locations/*/caPools/-``
        page_size (int):
            Optional. Limit on the number of
            [Certificates][google.cloud.security.privateca.v1.Certificate]
            to include in the response. Further
            [Certificates][google.cloud.security.privateca.v1.Certificate]
            can subsequently be obtained by including the
            [ListCertificatesResponse.next_page_token][google.cloud.security.privateca.v1.ListCertificatesResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Pagination token, returned earlier via
            [ListCertificatesResponse.next_page_token][google.cloud.security.privateca.v1.ListCertificatesResponse.next_page_token].
        filter (str):
            Optional. Only include resources that match the filter in
            the response. For details on supported filters and syntax,
            see `Certificates Filtering
            documentation <https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#filtering_support>`__.
        order_by (str):
            Optional. Specify how the results should be sorted. For
            details on supported fields and syntax, see `Certificates
            Sorting
            documentation <https://cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates#sorting_support>`__.
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
    r"""Response message for
    [CertificateAuthorityService.ListCertificates][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificates].

    Attributes:
        certificates (MutableSequence[google.cloud.security.privateca_v1.types.Certificate]):
            The list of
            [Certificates][google.cloud.security.privateca.v1.Certificate].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListCertificatesRequest.page_token][google.cloud.security.privateca.v1.ListCertificatesRequest.page_token]
            to retrieve the next page of results.
        unreachable (MutableSequence[str]):
            A list of locations (e.g. "us-west1") that
            could not be reached.
    """

    @property
    def raw_page(self):
        return self

    certificates: MutableSequence[resources.Certificate] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Certificate,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class RevokeCertificateRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.RevokeCertificate][google.cloud.security.privateca.v1.CertificateAuthorityService.RevokeCertificate].

    Attributes:
        name (str):
            Required. The resource name for this
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            in the format
            ``projects/*/locations/*/caPools/*/certificates/*``.
        reason (google.cloud.security.privateca_v1.types.RevocationReason):
            Required. The
            [RevocationReason][google.cloud.security.privateca.v1.RevocationReason]
            for revoking this certificate.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reason: resources.RevocationReason = proto.Field(
        proto.ENUM,
        number=2,
        enum=resources.RevocationReason,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateCertificateRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.UpdateCertificate][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificate].

    Attributes:
        certificate (google.cloud.security.privateca_v1.types.Certificate):
            Required.
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            with updated values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A list of fields to be updated in
            this request.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    certificate: resources.Certificate = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Certificate,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ActivateCertificateAuthorityRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.ActivateCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.ActivateCertificateAuthority].

    Attributes:
        name (str):
            Required. The resource name for this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.
        pem_ca_certificate (str):
            Required. The signed CA certificate issued from
            [FetchCertificateAuthorityCsrResponse.pem_csr][google.cloud.security.privateca.v1.FetchCertificateAuthorityCsrResponse.pem_csr].
        subordinate_config (google.cloud.security.privateca_v1.types.SubordinateConfig):
            Required. Must include information about the issuer of
            'pem_ca_certificate', and any further issuers until the
            self-signed CA.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pem_ca_certificate: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subordinate_config: resources.SubordinateConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.SubordinateConfig,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateCertificateAuthorityRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.CreateCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateAuthority].

    Attributes:
        parent (str):
            Required. The resource name of the
            [CaPool][google.cloud.security.privateca.v1.CaPool]
            associated with the
            [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority],
            in the format ``projects/*/locations/*/caPools/*``.
        certificate_authority_id (str):
            Required. It must be unique within a location and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``
        certificate_authority (google.cloud.security.privateca_v1.types.CertificateAuthority):
            Required. A
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            with initial field values.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    certificate_authority_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    certificate_authority: resources.CertificateAuthority = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.CertificateAuthority,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DisableCertificateAuthorityRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.DisableCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.DisableCertificateAuthority].

    Attributes:
        name (str):
            Required. The resource name for this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        ignore_dependent_resources (bool):
            Optional. This field allows this CA to be
            disabled even if it's being depended on by
            another resource. However, doing so may result
            in unintended and unrecoverable effects on any
            dependent resources since the CA will no longer
            be able to issue certificates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ignore_dependent_resources: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class EnableCertificateAuthorityRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.EnableCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.EnableCertificateAuthority].

    Attributes:
        name (str):
            Required. The resource name for this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

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


class FetchCertificateAuthorityCsrRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.FetchCertificateAuthorityCsr][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr].

    Attributes:
        name (str):
            Required. The resource name for this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchCertificateAuthorityCsrResponse(proto.Message):
    r"""Response message for
    [CertificateAuthorityService.FetchCertificateAuthorityCsr][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr].

    Attributes:
        pem_csr (str):
            Output only. The PEM-encoded signed
            certificate signing request (CSR).
    """

    pem_csr: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetCertificateAuthorityRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.GetCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateAuthority].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.security.privateca.v1.CertificateAuthority.name]
            of the
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCertificateAuthoritiesRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.ListCertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateAuthorities].

    Attributes:
        parent (str):
            Required. The resource name of the
            [CaPool][google.cloud.security.privateca.v1.CaPool]
            associated with the
            [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority],
            in the format ``projects/*/locations/*/caPools/*``.
        page_size (int):
            Optional. Limit on the number of
            [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority]
            to include in the response. Further
            [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority]
            can subsequently be obtained by including the
            [ListCertificateAuthoritiesResponse.next_page_token][google.cloud.security.privateca.v1.ListCertificateAuthoritiesResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Pagination token, returned earlier via
            [ListCertificateAuthoritiesResponse.next_page_token][google.cloud.security.privateca.v1.ListCertificateAuthoritiesResponse.next_page_token].
        filter (str):
            Optional. Only include resources that match
            the filter in the response.
        order_by (str):
            Optional. Specify how the results should be
            sorted.
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


class ListCertificateAuthoritiesResponse(proto.Message):
    r"""Response message for
    [CertificateAuthorityService.ListCertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateAuthorities].

    Attributes:
        certificate_authorities (MutableSequence[google.cloud.security.privateca_v1.types.CertificateAuthority]):
            The list of
            [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListCertificateAuthoritiesRequest.page_token][google.cloud.security.privateca.v1.ListCertificateAuthoritiesRequest.page_token]
            to retrieve the next page of results.
        unreachable (MutableSequence[str]):
            A list of locations (e.g. "us-west1") that
            could not be reached.
    """

    @property
    def raw_page(self):
        return self

    certificate_authorities: MutableSequence[resources.CertificateAuthority] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.CertificateAuthority,
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


class UndeleteCertificateAuthorityRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.UndeleteCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.UndeleteCertificateAuthority].

    Attributes:
        name (str):
            Required. The resource name for this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

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


class DeleteCertificateAuthorityRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.DeleteCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateAuthority].

    Attributes:
        name (str):
            Required. The resource name for this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        ignore_active_certificates (bool):
            Optional. This field allows the CA to be
            deleted even if the CA has active certs. Active
            certs include both unrevoked and unexpired
            certs.
        skip_grace_period (bool):
            Optional. If this flag is set, the
            Certificate Authority will be deleted as soon as
            possible without a 30-day grace period where
            undeletion would have been allowed. If you
            proceed, there will be no way to recover this
            CA.
        ignore_dependent_resources (bool):
            Optional. This field allows this CA to be
            deleted even if it's being depended on by
            another resource. However, doing so may result
            in unintended and unrecoverable effects on any
            dependent resources since the CA will no longer
            be able to issue certificates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ignore_active_certificates: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    skip_grace_period: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    ignore_dependent_resources: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class UpdateCertificateAuthorityRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.UpdateCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateAuthority].

    Attributes:
        certificate_authority (google.cloud.security.privateca_v1.types.CertificateAuthority):
            Required.
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            with updated values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A list of fields to be updated in
            this request.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    certificate_authority: resources.CertificateAuthority = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.CertificateAuthority,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateCaPoolRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.CreateCaPool][google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCaPool].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the [CaPool][google.cloud.security.privateca.v1.CaPool], in
            the format ``projects/*/locations/*``.
        ca_pool_id (str):
            Required. It must be unique within a location and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``
        ca_pool (google.cloud.security.privateca_v1.types.CaPool):
            Required. A
            [CaPool][google.cloud.security.privateca.v1.CaPool] with
            initial field values.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ca_pool_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ca_pool: resources.CaPool = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.CaPool,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateCaPoolRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.UpdateCaPool][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCaPool].

    Attributes:
        ca_pool (google.cloud.security.privateca_v1.types.CaPool):
            Required.
            [CaPool][google.cloud.security.privateca.v1.CaPool] with
            updated values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A list of fields to be updated in
            this request.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    ca_pool: resources.CaPool = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.CaPool,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteCaPoolRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.DeleteCaPool][google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCaPool].

    Attributes:
        name (str):
            Required. The resource name for this
            [CaPool][google.cloud.security.privateca.v1.CaPool] in the
            format ``projects/*/locations/*/caPools/*``.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        ignore_dependent_resources (bool):
            Optional. This field allows this pool to be
            deleted even if it's being depended on by
            another resource. However, doing so may result
            in unintended and unrecoverable effects on any
            dependent resources since the pool will no
            longer be able to issue certificates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ignore_dependent_resources: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class FetchCaCertsRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.FetchCaCerts][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCaCerts].

    Attributes:
        ca_pool (str):
            Required. The resource name for the
            [CaPool][google.cloud.security.privateca.v1.CaPool] in the
            format ``projects/*/locations/*/caPools/*``.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    ca_pool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchCaCertsResponse(proto.Message):
    r"""Response message for
    [CertificateAuthorityService.FetchCaCerts][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCaCerts].

    Attributes:
        ca_certs (MutableSequence[google.cloud.security.privateca_v1.types.FetchCaCertsResponse.CertChain]):
            The PEM encoded CA certificate chains of all certificate
            authorities in this
            [CaPool][google.cloud.security.privateca.v1.CaPool] in the
            ENABLED, DISABLED, or STAGED states.
    """

    class CertChain(proto.Message):
        r"""

        Attributes:
            certificates (MutableSequence[str]):
                The certificates that form the CA chain, from
                leaf to root order.
        """

        certificates: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    ca_certs: MutableSequence[CertChain] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CertChain,
    )


class GetCaPoolRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.GetCaPool][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCaPool].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.security.privateca.v1.CaPool.name] of
            the [CaPool][google.cloud.security.privateca.v1.CaPool] to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCaPoolsRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.ListCaPools][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCaPools].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the [CaPools][google.cloud.security.privateca.v1.CaPool], in
            the format ``projects/*/locations/*``.
        page_size (int):
            Optional. Limit on the number of
            [CaPools][google.cloud.security.privateca.v1.CaPool] to
            include in the response. Further
            [CaPools][google.cloud.security.privateca.v1.CaPool] can
            subsequently be obtained by including the
            [ListCaPoolsResponse.next_page_token][google.cloud.security.privateca.v1.ListCaPoolsResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Pagination token, returned earlier via
            [ListCaPoolsResponse.next_page_token][google.cloud.security.privateca.v1.ListCaPoolsResponse.next_page_token].
        filter (str):
            Optional. Only include resources that match
            the filter in the response.
        order_by (str):
            Optional. Specify how the results should be
            sorted.
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


class ListCaPoolsResponse(proto.Message):
    r"""Response message for
    [CertificateAuthorityService.ListCaPools][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCaPools].

    Attributes:
        ca_pools (MutableSequence[google.cloud.security.privateca_v1.types.CaPool]):
            The list of
            [CaPools][google.cloud.security.privateca.v1.CaPool].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListCertificateAuthoritiesRequest.page_token][google.cloud.security.privateca.v1.ListCertificateAuthoritiesRequest.page_token]
            to retrieve the next page of results.
        unreachable (MutableSequence[str]):
            A list of locations (e.g. "us-west1") that
            could not be reached.
    """

    @property
    def raw_page(self):
        return self

    ca_pools: MutableSequence[resources.CaPool] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.CaPool,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCertificateRevocationListRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.GetCertificateRevocationList][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateRevocationList].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.security.privateca.v1.CertificateRevocationList.name]
            of the
            [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCertificateRevocationListsRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.ListCertificateRevocationLists][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateRevocationLists].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the
            [CertificateRevocationLists][google.cloud.security.privateca.v1.CertificateRevocationList],
            in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.
        page_size (int):
            Optional. Limit on the number of
            [CertificateRevocationLists][google.cloud.security.privateca.v1.CertificateRevocationList]
            to include in the response. Further
            [CertificateRevocationLists][google.cloud.security.privateca.v1.CertificateRevocationList]
            can subsequently be obtained by including the
            [ListCertificateRevocationListsResponse.next_page_token][google.cloud.security.privateca.v1.ListCertificateRevocationListsResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Pagination token, returned earlier via
            [ListCertificateRevocationListsResponse.next_page_token][google.cloud.security.privateca.v1.ListCertificateRevocationListsResponse.next_page_token].
        filter (str):
            Optional. Only include resources that match
            the filter in the response.
        order_by (str):
            Optional. Specify how the results should be
            sorted.
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


class ListCertificateRevocationListsResponse(proto.Message):
    r"""Response message for
    [CertificateAuthorityService.ListCertificateRevocationLists][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateRevocationLists].

    Attributes:
        certificate_revocation_lists (MutableSequence[google.cloud.security.privateca_v1.types.CertificateRevocationList]):
            The list of
            [CertificateRevocationLists][google.cloud.security.privateca.v1.CertificateRevocationList].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListCertificateRevocationListsRequest.page_token][google.cloud.security.privateca.v1.ListCertificateRevocationListsRequest.page_token]
            to retrieve the next page of results.
        unreachable (MutableSequence[str]):
            A list of locations (e.g. "us-west1") that
            could not be reached.
    """

    @property
    def raw_page(self):
        return self

    certificate_revocation_lists: MutableSequence[
        resources.CertificateRevocationList
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.CertificateRevocationList,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateCertificateRevocationListRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.UpdateCertificateRevocationList][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateRevocationList].

    Attributes:
        certificate_revocation_list (google.cloud.security.privateca_v1.types.CertificateRevocationList):
            Required.
            [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
            with updated values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A list of fields to be updated in
            this request.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    certificate_revocation_list: resources.CertificateRevocationList = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.CertificateRevocationList,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateCertificateTemplateRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.CreateCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.CreateCertificateTemplate].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate],
            in the format ``projects/*/locations/*``.
        certificate_template_id (str):
            Required. It must be unique within a location and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``
        certificate_template (google.cloud.security.privateca_v1.types.CertificateTemplate):
            Required. A
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
            with initial field values.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    certificate_template_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    certificate_template: resources.CertificateTemplate = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.CertificateTemplate,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteCertificateTemplateRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.DeleteCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.DeleteCertificateTemplate].

    Attributes:
        name (str):
            Required. The resource name for this
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
            in the format
            ``projects/*/locations/*/certificateTemplates/*``.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

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


class GetCertificateTemplateRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.GetCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.GetCertificateTemplate].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.security.privateca.v1.CertificateTemplate.name]
            of the
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCertificateTemplatesRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.ListCertificateTemplates][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateTemplates].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the
            [CertificateTemplates][google.cloud.security.privateca.v1.CertificateTemplate],
            in the format ``projects/*/locations/*``.
        page_size (int):
            Optional. Limit on the number of
            [CertificateTemplates][google.cloud.security.privateca.v1.CertificateTemplate]
            to include in the response. Further
            [CertificateTemplates][google.cloud.security.privateca.v1.CertificateTemplate]
            can subsequently be obtained by including the
            [ListCertificateTemplatesResponse.next_page_token][google.cloud.security.privateca.v1.ListCertificateTemplatesResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Pagination token, returned earlier via
            [ListCertificateTemplatesResponse.next_page_token][google.cloud.security.privateca.v1.ListCertificateTemplatesResponse.next_page_token].
        filter (str):
            Optional. Only include resources that match
            the filter in the response.
        order_by (str):
            Optional. Specify how the results should be
            sorted.
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


class ListCertificateTemplatesResponse(proto.Message):
    r"""Response message for
    [CertificateAuthorityService.ListCertificateTemplates][google.cloud.security.privateca.v1.CertificateAuthorityService.ListCertificateTemplates].

    Attributes:
        certificate_templates (MutableSequence[google.cloud.security.privateca_v1.types.CertificateTemplate]):
            The list of
            [CertificateTemplates][google.cloud.security.privateca.v1.CertificateTemplate].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListCertificateTemplatesRequest.page_token][google.cloud.security.privateca.v1.ListCertificateTemplatesRequest.page_token]
            to retrieve the next page of results.
        unreachable (MutableSequence[str]):
            A list of locations (e.g. "us-west1") that
            could not be reached.
    """

    @property
    def raw_page(self):
        return self

    certificate_templates: MutableSequence[resources.CertificateTemplate] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.CertificateTemplate,
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


class UpdateCertificateTemplateRequest(proto.Message):
    r"""Request message for
    [CertificateAuthorityService.UpdateCertificateTemplate][google.cloud.security.privateca.v1.CertificateAuthorityService.UpdateCertificateTemplate].

    Attributes:
        certificate_template (google.cloud.security.privateca_v1.types.CertificateTemplate):
            Required.
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
            with updated values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A list of fields to be updated in
            this request.
        request_id (str):
            Optional. An ID to identify requests. Specify
            a unique request ID so that if you must retry
            your request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    certificate_template: resources.CertificateTemplate = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.CertificateTemplate,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
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


__all__ = tuple(sorted(__protobuf__.manifest))
