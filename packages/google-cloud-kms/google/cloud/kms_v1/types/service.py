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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.kms_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.kms.v1",
    manifest={
        "ListKeyRingsRequest",
        "ListCryptoKeysRequest",
        "ListCryptoKeyVersionsRequest",
        "ListImportJobsRequest",
        "ListRetiredResourcesRequest",
        "ListKeyRingsResponse",
        "ListCryptoKeysResponse",
        "ListCryptoKeyVersionsResponse",
        "ListImportJobsResponse",
        "ListRetiredResourcesResponse",
        "GetKeyRingRequest",
        "GetCryptoKeyRequest",
        "GetCryptoKeyVersionRequest",
        "GetPublicKeyRequest",
        "GetImportJobRequest",
        "GetRetiredResourceRequest",
        "CreateKeyRingRequest",
        "CreateCryptoKeyRequest",
        "CreateCryptoKeyVersionRequest",
        "DeleteCryptoKeyRequest",
        "DeleteCryptoKeyVersionRequest",
        "ImportCryptoKeyVersionRequest",
        "ImportTrustedKeyWrappedCryptoKeyVersionRequest",
        "ExportTrustedKeyWrappedCryptoKeyVersionRequest",
        "ExportTrustedKeyWrappedCryptoKeyVersionResponse",
        "CreateImportJobRequest",
        "UpdateCryptoKeyRequest",
        "UpdateCryptoKeyVersionRequest",
        "UpdateCryptoKeyPrimaryVersionRequest",
        "DestroyCryptoKeyVersionRequest",
        "RestoreCryptoKeyVersionRequest",
        "EncryptRequest",
        "DecryptRequest",
        "RawEncryptRequest",
        "RawDecryptRequest",
        "AsymmetricSignRequest",
        "AsymmetricDecryptRequest",
        "MacSignRequest",
        "MacVerifyRequest",
        "DecapsulateRequest",
        "GenerateRandomBytesRequest",
        "EncryptResponse",
        "DecryptResponse",
        "RawEncryptResponse",
        "RawDecryptResponse",
        "AsymmetricSignResponse",
        "AsymmetricDecryptResponse",
        "MacSignResponse",
        "MacVerifyResponse",
        "DecapsulateResponse",
        "GenerateRandomBytesResponse",
        "Digest",
        "LocationMetadata",
        "DeleteCryptoKeyMetadata",
        "DeleteCryptoKeyVersionMetadata",
    },
)


class ListKeyRingsRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.ListKeyRings][google.cloud.kms.v1.KeyManagementService.ListKeyRings].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the [KeyRings][google.cloud.kms.v1.KeyRing], in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. Optional limit on the number of
            [KeyRings][google.cloud.kms.v1.KeyRing] to include in the
            response. Further [KeyRings][google.cloud.kms.v1.KeyRing]
            can subsequently be obtained by including the
            [ListKeyRingsResponse.next_page_token][google.cloud.kms.v1.ListKeyRingsResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Optional pagination token, returned earlier via
            [ListKeyRingsResponse.next_page_token][google.cloud.kms.v1.ListKeyRingsResponse.next_page_token].
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


class ListCryptoKeysRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.ListCryptoKeys][google.cloud.kms.v1.KeyManagementService.ListCryptoKeys].

    Attributes:
        parent (str):
            Required. The resource name of the
            [KeyRing][google.cloud.kms.v1.KeyRing] to list, in the
            format ``projects/*/locations/*/keyRings/*``.
        page_size (int):
            Optional. Optional limit on the number of
            [CryptoKeys][google.cloud.kms.v1.CryptoKey] to include in
            the response. Further
            [CryptoKeys][google.cloud.kms.v1.CryptoKey] can subsequently
            be obtained by including the
            [ListCryptoKeysResponse.next_page_token][google.cloud.kms.v1.ListCryptoKeysResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Optional pagination token, returned earlier via
            [ListCryptoKeysResponse.next_page_token][google.cloud.kms.v1.ListCryptoKeysResponse.next_page_token].
        version_view (google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionView):
            The fields of the primary version to include
            in the response.
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
    version_view: resources.CryptoKeyVersion.CryptoKeyVersionView = proto.Field(
        proto.ENUM,
        number=4,
        enum=resources.CryptoKeyVersion.CryptoKeyVersionView,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListCryptoKeyVersionsRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.ListCryptoKeyVersions][google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions].

    Attributes:
        parent (str):
            Required. The resource name of the
            [CryptoKey][google.cloud.kms.v1.CryptoKey] to list, in the
            format ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
        page_size (int):
            Optional. Optional limit on the number of
            [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] to
            include in the response. Further
            [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
            can subsequently be obtained by including the
            [ListCryptoKeyVersionsResponse.next_page_token][google.cloud.kms.v1.ListCryptoKeyVersionsResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Optional pagination token, returned earlier via
            [ListCryptoKeyVersionsResponse.next_page_token][google.cloud.kms.v1.ListCryptoKeyVersionsResponse.next_page_token].
        view (google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionView):
            The fields to include in the response.
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
    view: resources.CryptoKeyVersion.CryptoKeyVersionView = proto.Field(
        proto.ENUM,
        number=4,
        enum=resources.CryptoKeyVersion.CryptoKeyVersionView,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListImportJobsRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.ListImportJobs][google.cloud.kms.v1.KeyManagementService.ListImportJobs].

    Attributes:
        parent (str):
            Required. The resource name of the
            [KeyRing][google.cloud.kms.v1.KeyRing] to list, in the
            format ``projects/*/locations/*/keyRings/*``.
        page_size (int):
            Optional. Optional limit on the number of
            [ImportJobs][google.cloud.kms.v1.ImportJob] to include in
            the response. Further
            [ImportJobs][google.cloud.kms.v1.ImportJob] can subsequently
            be obtained by including the
            [ListImportJobsResponse.next_page_token][google.cloud.kms.v1.ListImportJobsResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Optional pagination token, returned earlier via
            [ListImportJobsResponse.next_page_token][google.cloud.kms.v1.ListImportJobsResponse.next_page_token].
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


class ListRetiredResourcesRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.ListRetiredResources][google.cloud.kms.v1.KeyManagementService.ListRetiredResources].

    Attributes:
        parent (str):
            Required. The project-specific location holding the
            [RetiredResources][google.cloud.kms.v1.RetiredResource], in
            the format ``projects/*/locations/*``.
        page_size (int):
            Optional. Optional limit on the number of
            [RetiredResources][google.cloud.kms.v1.RetiredResource] to
            be included in the response. Further
            [RetiredResources][google.cloud.kms.v1.RetiredResource] can
            subsequently be obtained by including the
            [ListRetiredResourcesResponse.next_page_token][google.cloud.kms.v1.ListRetiredResourcesResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Optional pagination token, returned earlier via
            [ListRetiredResourcesResponse.next_page_token][google.cloud.kms.v1.ListRetiredResourcesResponse.next_page_token].
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


class ListKeyRingsResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.ListKeyRings][google.cloud.kms.v1.KeyManagementService.ListKeyRings].

    Attributes:
        key_rings (MutableSequence[google.cloud.kms_v1.types.KeyRing]):
            The list of [KeyRings][google.cloud.kms.v1.KeyRing].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListKeyRingsRequest.page_token][google.cloud.kms.v1.ListKeyRingsRequest.page_token]
            to retrieve the next page of results.
        total_size (int):
            The total number of [KeyRings][google.cloud.kms.v1.KeyRing]
            that matched the query.

            This field is not populated if
            [ListKeyRingsRequest.filter][google.cloud.kms.v1.ListKeyRingsRequest.filter]
            is applied.
    """

    @property
    def raw_page(self):
        return self

    key_rings: MutableSequence[resources.KeyRing] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.KeyRing,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ListCryptoKeysResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.ListCryptoKeys][google.cloud.kms.v1.KeyManagementService.ListCryptoKeys].

    Attributes:
        crypto_keys (MutableSequence[google.cloud.kms_v1.types.CryptoKey]):
            The list of [CryptoKeys][google.cloud.kms.v1.CryptoKey].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListCryptoKeysRequest.page_token][google.cloud.kms.v1.ListCryptoKeysRequest.page_token]
            to retrieve the next page of results.
        total_size (int):
            The total number of
            [CryptoKeys][google.cloud.kms.v1.CryptoKey] that matched the
            query.

            This field is not populated if
            [ListCryptoKeysRequest.filter][google.cloud.kms.v1.ListCryptoKeysRequest.filter]
            is applied.
    """

    @property
    def raw_page(self):
        return self

    crypto_keys: MutableSequence[resources.CryptoKey] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.CryptoKey,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ListCryptoKeyVersionsResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.ListCryptoKeyVersions][google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions].

    Attributes:
        crypto_key_versions (MutableSequence[google.cloud.kms_v1.types.CryptoKeyVersion]):
            The list of
            [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListCryptoKeyVersionsRequest.page_token][google.cloud.kms.v1.ListCryptoKeyVersionsRequest.page_token]
            to retrieve the next page of results.
        total_size (int):
            The total number of
            [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
            that matched the query.

            This field is not populated if
            [ListCryptoKeyVersionsRequest.filter][google.cloud.kms.v1.ListCryptoKeyVersionsRequest.filter]
            is applied.
    """

    @property
    def raw_page(self):
        return self

    crypto_key_versions: MutableSequence[resources.CryptoKeyVersion] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.CryptoKeyVersion,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ListImportJobsResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.ListImportJobs][google.cloud.kms.v1.KeyManagementService.ListImportJobs].

    Attributes:
        import_jobs (MutableSequence[google.cloud.kms_v1.types.ImportJob]):
            The list of [ImportJobs][google.cloud.kms.v1.ImportJob].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListImportJobsRequest.page_token][google.cloud.kms.v1.ListImportJobsRequest.page_token]
            to retrieve the next page of results.
        total_size (int):
            The total number of
            [ImportJobs][google.cloud.kms.v1.ImportJob] that matched the
            query.

            This field is not populated if
            [ListImportJobsRequest.filter][google.cloud.kms.v1.ListImportJobsRequest.filter]
            is applied.
    """

    @property
    def raw_page(self):
        return self

    import_jobs: MutableSequence[resources.ImportJob] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.ImportJob,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ListRetiredResourcesResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.ListRetiredResources][google.cloud.kms.v1.KeyManagementService.ListRetiredResources].

    Attributes:
        retired_resources (MutableSequence[google.cloud.kms_v1.types.RetiredResource]):
            The list of
            [RetiredResources][google.cloud.kms.v1.RetiredResource].
        next_page_token (str):
            A token to retrieve the next page of results. Pass this
            value in
            [ListRetiredResourcesRequest.page_token][google.cloud.kms.v1.ListRetiredResourcesRequest.page_token]
            to retrieve the next page of results.
        total_size (int):
            The total number of
            [RetiredResources][google.cloud.kms.v1.RetiredResource] that
            matched the query.
    """

    @property
    def raw_page(self):
        return self

    retired_resources: MutableSequence[resources.RetiredResource] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.RetiredResource,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT64,
        number=3,
    )


class GetKeyRingRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.GetKeyRing][google.cloud.kms.v1.KeyManagementService.GetKeyRing].

    Attributes:
        name (str):
            Required. The [name][google.cloud.kms.v1.KeyRing.name] of
            the [KeyRing][google.cloud.kms.v1.KeyRing] to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetCryptoKeyRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.GetCryptoKey][google.cloud.kms.v1.KeyManagementService.GetCryptoKey].

    Attributes:
        name (str):
            Required. The [name][google.cloud.kms.v1.CryptoKey.name] of
            the [CryptoKey][google.cloud.kms.v1.CryptoKey] to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetCryptoKeyVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.GetCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.GetCryptoKeyVersion].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.CryptoKeyVersion.name] of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetPublicKeyRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.CryptoKeyVersion.name] of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            public key to get.
        public_key_format (google.cloud.kms_v1.types.PublicKey.PublicKeyFormat):
            Optional. The [PublicKey][google.cloud.kms.v1.PublicKey]
            format specified by the user. This field is required for PQC
            algorithms. If specified, the public key will be exported
            through the
            [public_key][google.cloud.kms.v1.PublicKey.public_key] field
            in the requested format. Otherwise, the
            [pem][google.cloud.kms.v1.PublicKey.pem] field will be
            populated for non-PQC algorithms, and an error will be
            returned for PQC algorithms.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    public_key_format: resources.PublicKey.PublicKeyFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=resources.PublicKey.PublicKeyFormat,
    )


class GetImportJobRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.GetImportJob][google.cloud.kms.v1.KeyManagementService.GetImportJob].

    Attributes:
        name (str):
            Required. The [name][google.cloud.kms.v1.ImportJob.name] of
            the [ImportJob][google.cloud.kms.v1.ImportJob] to get.
        public_key_format (google.cloud.kms_v1.types.PublicKey.PublicKeyFormat):
            Optional. Specifies the [WrappingPublicKey][] format. If not
            specified:

            - For RSA-based import methods, the wrapping key will be
              returned in PEM format
            - For pure ML-KEM-based import methods, the wrapping key
              will be returned in the raw bytes format specified in
              FIPS-203
            - For X-Wing-based import methods, the wrapping key will be
              returned in the raw bytes format specified in
              https://datatracker.ietf.org/doc/draft-connolly-cfrg-xwing-kem.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    public_key_format: resources.PublicKey.PublicKeyFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=resources.PublicKey.PublicKeyFormat,
    )


class GetRetiredResourceRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.GetRetiredResource][google.cloud.kms.v1.KeyManagementService.GetRetiredResource].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.RetiredResource.name] of the
            [RetiredResource][google.cloud.kms.v1.RetiredResource] to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateKeyRingRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.CreateKeyRing][google.cloud.kms.v1.KeyManagementService.CreateKeyRing].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the [KeyRings][google.cloud.kms.v1.KeyRing], in the format
            ``projects/*/locations/*``.
        key_ring_id (str):
            Required. It must be unique within a location and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``
        key_ring (google.cloud.kms_v1.types.KeyRing):
            Required. A [KeyRing][google.cloud.kms.v1.KeyRing] with
            initial field values.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key_ring_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    key_ring: resources.KeyRing = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.KeyRing,
    )


class CreateCryptoKeyRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.CreateCryptoKey][google.cloud.kms.v1.KeyManagementService.CreateCryptoKey].

    Attributes:
        parent (str):
            Required. The [name][google.cloud.kms.v1.KeyRing.name] of
            the KeyRing associated with the
            [CryptoKeys][google.cloud.kms.v1.CryptoKey].
        crypto_key_id (str):
            Required. It must be unique within a KeyRing and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``
        crypto_key (google.cloud.kms_v1.types.CryptoKey):
            Required. A [CryptoKey][google.cloud.kms.v1.CryptoKey] with
            initial field values.
        skip_initial_version_creation (bool):
            If set to true, the request will create a
            [CryptoKey][google.cloud.kms.v1.CryptoKey] without any
            [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion].
            You must manually call
            [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion]
            or
            [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion]
            before you can use this
            [CryptoKey][google.cloud.kms.v1.CryptoKey].
        trusted_wrapping_enabled (bool):
            Optional. Whether trusted wrapping will be enabled on the
            first
            [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
            created for this [CryptoKey][google.cloud.kms.v1.CryptoKey].
            This field is only supported for keys with
            [CryptoKeyVersionTemplate.protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level]
            [HSM_SINGLE_TENANT][google.cloud.kms.v1.ProtectionLevel.HSM_SINGLE_TENANT].
            This field is supported for all
            [CryptoKeyPurposes][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose]
            except
            [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    crypto_key_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    crypto_key: resources.CryptoKey = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.CryptoKey,
    )
    skip_initial_version_creation: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    trusted_wrapping_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class CreateCryptoKeyVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion].

    Attributes:
        parent (str):
            Required. The [name][google.cloud.kms.v1.CryptoKey.name] of
            the [CryptoKey][google.cloud.kms.v1.CryptoKey] associated
            with the
            [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion].
        crypto_key_version (google.cloud.kms_v1.types.CryptoKeyVersion):
            Required. A
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            with initial field values.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    crypto_key_version: resources.CryptoKeyVersion = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.CryptoKeyVersion,
    )


class DeleteCryptoKeyRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.DeleteCryptoKey][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKey].

    Attributes:
        name (str):
            Required. The [name][google.cloud.kms.v1.CryptoKey.name] of
            the [CryptoKey][google.cloud.kms.v1.CryptoKey] to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteCryptoKeyVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.DeleteCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKeyVersion].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.CryptoKeyVersion.name] of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportCryptoKeyVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The [name][google.cloud.kms.v1.CryptoKey.name] of
            the [CryptoKey][google.cloud.kms.v1.CryptoKey] to be
            imported into.

            The create permission is only required on this key when
            creating a new
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].
        crypto_key_version (str):
            Optional. The optional
            [name][google.cloud.kms.v1.CryptoKeyVersion.name] of an
            existing
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            target for an import operation. If this field is not
            present, a new
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            containing the supplied key material is created.

            If this field is present, the supplied key material is
            imported into the existing
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]. To
            import into an existing
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion],
            the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            must be a child of
            [ImportCryptoKeyVersionRequest.parent][google.cloud.kms.v1.ImportCryptoKeyVersionRequest.parent],
            have been previously created via
            [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion],
            and be in
            [DESTROYED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROYED]
            or
            [IMPORT_FAILED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.IMPORT_FAILED]
            state. The key material and algorithm must match the
            previous
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            exactly if the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] has
            ever contained key material.
        algorithm (google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm):
            Required. The
            [algorithm][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm]
            of the key being imported. This does not need to match the
            [version_template][google.cloud.kms.v1.CryptoKey.version_template]
            of the [CryptoKey][google.cloud.kms.v1.CryptoKey] this
            version imports into.
        import_job (str):
            Required. The [name][google.cloud.kms.v1.ImportJob.name] of
            the [ImportJob][google.cloud.kms.v1.ImportJob] that was used
            to wrap this key material.
        wrapped_key (bytes):
            Optional. The wrapped key material to import.

            Before wrapping, key material must be formatted. If
            importing symmetric key material, the expected key material
            format is plain bytes. If importing asymmetric key material,
            the expected key material format is PKCS#8-encoded DER (the
            PrivateKeyInfo structure from RFC 5208).

            When wrapping with import methods
            ([RSA_OAEP_3072_SHA1_AES_256][google.cloud.kms.v1.ImportJob.ImportMethod.RSA_OAEP_3072_SHA1_AES_256]
            or
            [RSA_OAEP_4096_SHA1_AES_256][google.cloud.kms.v1.ImportJob.ImportMethod.RSA_OAEP_4096_SHA1_AES_256]
            or
            [RSA_OAEP_3072_SHA256_AES_256][google.cloud.kms.v1.ImportJob.ImportMethod.RSA_OAEP_3072_SHA256_AES_256]
            or
            [RSA_OAEP_4096_SHA256_AES_256][google.cloud.kms.v1.ImportJob.ImportMethod.RSA_OAEP_4096_SHA256_AES_256]),

            this field must contain the concatenation of:

            .. raw:: html

                <ol>
                  <li>An ephemeral AES-256 wrapping key wrapped with the
                      [public_key][google.cloud.kms.v1.ImportJob.public_key] using
                      RSAES-OAEP with SHA-1/SHA-256, MGF1 with SHA-1/SHA-256, and an empty
                      label.
                  </li>
                  <li>The formatted key to be imported, wrapped with the ephemeral AES-256
                      key using AES-KWP (RFC 5649).
                  </li>
                </ol>

            This format is the same as the format produced by PKCS#11
            mechanism CKM_RSA_AES_KEY_WRAP.

            When wrapping with import methods
            ([RSA_OAEP_3072_SHA256][google.cloud.kms.v1.ImportJob.ImportMethod.RSA_OAEP_3072_SHA256]
            or
            [RSA_OAEP_4096_SHA256][google.cloud.kms.v1.ImportJob.ImportMethod.RSA_OAEP_4096_SHA256]),

            this field must contain the formatted key to be imported,
            wrapped with the
            [public_key][google.cloud.kms.v1.ImportJob.public_key] using
            RSAES-OAEP with SHA-256, MGF1 with SHA-256, and an empty
            label.
        rsa_aes_wrapped_key (bytes):
            Optional. This field has the same meaning as
            [wrapped_key][google.cloud.kms.v1.ImportCryptoKeyVersionRequest.wrapped_key].
            Prefer to use that field in new work. Either that field or
            this field (but not both) must be specified.

            This field is a member of `oneof`_ ``wrapped_key_material``.
        trusted_wrapping_enabled (bool):
            Optional. Whether trusted wrapping will be enabled on the
            imported [CryptoKeyVersion]. This field is only supported
            for keys with
            [CryptoKeyVersionTemplate.protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level]
            [HSM_SINGLE_TENANT][google.cloud.kms.v1.ProtectionLevel.HSM_SINGLE_TENANT].
            This field is supported for all
            [CryptoKeyPurposes][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose]
            besides
            [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    crypto_key_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    algorithm: resources.CryptoKeyVersion.CryptoKeyVersionAlgorithm = proto.Field(
        proto.ENUM,
        number=2,
        enum=resources.CryptoKeyVersion.CryptoKeyVersionAlgorithm,
    )
    import_job: str = proto.Field(
        proto.STRING,
        number=4,
    )
    wrapped_key: bytes = proto.Field(
        proto.BYTES,
        number=8,
    )
    rsa_aes_wrapped_key: bytes = proto.Field(
        proto.BYTES,
        number=5,
        oneof="wrapped_key_material",
    )
    trusted_wrapping_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class ImportTrustedKeyWrappedCryptoKeyVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.ImportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportTrustedKeyWrappedCryptoKeyVersion].

    Attributes:
        parent (str):
            Required. The [name][google.cloud.kms.v1.CryptoKey.name] of
            the [CryptoKey][google.cloud.kms.v1.CryptoKey] to be
            imported into.
        importing_key (str):
            Required. Required - the CKV of the trusted
            key used to import. This can be the name of a
            CryptoKeyVersion or a CryptoKey.
        crypto_key_version (str):
            Optional. The optional
            [name][google.cloud.kms.v1.CryptoKeyVersion.name] of an
            existing
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            target for an import operation. If this field is not
            present, a new
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            containing the supplied key material is created.

            If this field is present, the supplied key material is
            imported into the existing
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]. To
            import into an existing
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion],
            the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            must be a child of
            [ImportTrustedKeyWrappedCryptoKeyVersionRequest.parent][google.cloud.kms.v1.ImportTrustedKeyWrappedCryptoKeyVersionRequest.parent],
            have been previously created via
            [ImportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportTrustedKeyWrappedCryptoKeyVersion],
            and be in
            [DESTROYED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROYED]
            or
            [IMPORT_FAILED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.IMPORT_FAILED]
            state. The key material and algorithm must match the
            previous
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            exactly if the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] has
            ever contained key material
        wrapped_key (bytes):
            Required. The target key pre-wrapped on
            premises.
        algorithm (google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm):
            Required. Required - The
            [algorithm][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm]
            of the key being imported. This does not need to match the
            [version_template][google.cloud.kms.v1.CryptoKey.version_template]
            of the [CryptoKey][google.cloud.kms.v1.CryptoKey] this
            version imports into.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    importing_key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    crypto_key_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    wrapped_key: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    algorithm: resources.CryptoKeyVersion.CryptoKeyVersionAlgorithm = proto.Field(
        proto.ENUM,
        number=5,
        enum=resources.CryptoKeyVersion.CryptoKeyVersionAlgorithm,
    )


class ExportTrustedKeyWrappedCryptoKeyVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.CryptoKeyVersion.name] of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            export. The
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            must have
            [trusted_wrapping_enabled][google.cloud.kms.v1.CryptoKeyVersion.trusted_wrapping_enabled]
            set to true.
        wrapping_key (str):
            Required. The
            [name][google.cloud.kms.v1.CryptoKeyVersion.name] of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use as a wrapping key. The
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            must have
            [hsm_trusted][google.cloud.kms.v1.CryptoKeyVersion.hsm_trusted]
            set to true.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    wrapping_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExportTrustedKeyWrappedCryptoKeyVersionResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion].

    Attributes:
        wrapped_key (bytes):
            The wrapped key material.
        wrapped_key_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [ExportTrustedKeyWrappedCryptoKeyVersionResponse.wrapped_key][google.cloud.kms.v1.ExportTrustedKeyWrappedCryptoKeyVersionResponse.wrapped_key].
            An integrity check of
            [ExportTrustedKeyWrappedCryptoKeyVersionResponse.wrapped_key][google.cloud.kms.v1.ExportTrustedKeyWrappedCryptoKeyVersionResponse.wrapped_key]
            can be performed by computing the CRC32C checksum of
            [ExportTrustedKeyWrappedCryptoKeyVersionResponse.wrapped_key][google.cloud.kms.v1.ExportTrustedKeyWrappedCryptoKeyVersionResponse.wrapped_key]
            and comparing your results to this field. Discard the
            response in case of non-matching checksum values, and
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
    """

    wrapped_key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    wrapped_key_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int64Value,
    )


class CreateImportJobRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.CreateImportJob][google.cloud.kms.v1.KeyManagementService.CreateImportJob].

    Attributes:
        parent (str):
            Required. The [name][google.cloud.kms.v1.KeyRing.name] of
            the [KeyRing][google.cloud.kms.v1.KeyRing] associated with
            the [ImportJobs][google.cloud.kms.v1.ImportJob].
        import_job_id (str):
            Required. It must be unique within a KeyRing and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``
        import_job (google.cloud.kms_v1.types.ImportJob):
            Required. An [ImportJob][google.cloud.kms.v1.ImportJob] with
            initial field values.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    import_job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    import_job: resources.ImportJob = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.ImportJob,
    )


class UpdateCryptoKeyRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.UpdateCryptoKey][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKey].

    Attributes:
        crypto_key (google.cloud.kms_v1.types.CryptoKey):
            Required. [CryptoKey][google.cloud.kms.v1.CryptoKey] with
            updated values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields to be updated in
            this request.
    """

    crypto_key: resources.CryptoKey = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.CryptoKey,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateCryptoKeyVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.UpdateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyVersion].

    Attributes:
        crypto_key_version (google.cloud.kms_v1.types.CryptoKeyVersion):
            Required.
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            with updated values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields to be updated in
            this request.
    """

    crypto_key_version: resources.CryptoKeyVersion = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.CryptoKeyVersion,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateCryptoKeyPrimaryVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKey][google.cloud.kms.v1.CryptoKey] to update.
        crypto_key_version_id (str):
            Required. The id of the child
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use as primary.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    crypto_key_version_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DestroyCryptoKeyVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.DestroyCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            destroy.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RestoreCryptoKeyVersionRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            restore.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EncryptRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKey][google.cloud.kms.v1.CryptoKey] or
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use for encryption.

            If a [CryptoKey][google.cloud.kms.v1.CryptoKey] is
            specified, the server will use its [primary
            version][google.cloud.kms.v1.CryptoKey.primary].
        plaintext (bytes):
            Required. The data to encrypt. Must be no larger than 64KiB.

            The maximum size depends on the key version's
            [protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level].
            For
            [SOFTWARE][google.cloud.kms.v1.ProtectionLevel.SOFTWARE],
            [EXTERNAL][google.cloud.kms.v1.ProtectionLevel.EXTERNAL],
            and
            [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC]
            keys, the plaintext must be no larger than 64KiB. For
            [HSM][google.cloud.kms.v1.ProtectionLevel.HSM] keys, the
            combined length of the plaintext and
            additional_authenticated_data fields must be no larger than
            8KiB.
        additional_authenticated_data (bytes):
            Optional. Optional data that, if specified, must also be
            provided during decryption through
            [DecryptRequest.additional_authenticated_data][google.cloud.kms.v1.DecryptRequest.additional_authenticated_data].

            The maximum size depends on the key version's
            [protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level].
            For
            [SOFTWARE][google.cloud.kms.v1.ProtectionLevel.SOFTWARE],
            [EXTERNAL][google.cloud.kms.v1.ProtectionLevel.EXTERNAL],
            and
            [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC]
            keys the AAD must be no larger than 64KiB. For
            [HSM][google.cloud.kms.v1.ProtectionLevel.HSM] keys, the
            combined length of the plaintext and
            additional_authenticated_data fields must be no larger than
            8KiB.
        plaintext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [EncryptRequest.plaintext][google.cloud.kms.v1.EncryptRequest.plaintext].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [EncryptRequest.plaintext][google.cloud.kms.v1.EncryptRequest.plaintext]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([EncryptRequest.plaintext][google.cloud.kms.v1.EncryptRequest.plaintext])
            is equal to
            [EncryptRequest.plaintext_crc32c][google.cloud.kms.v1.EncryptRequest.plaintext_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
        additional_authenticated_data_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [EncryptRequest.additional_authenticated_data][google.cloud.kms.v1.EncryptRequest.additional_authenticated_data].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [EncryptRequest.additional_authenticated_data][google.cloud.kms.v1.EncryptRequest.additional_authenticated_data]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([EncryptRequest.additional_authenticated_data][google.cloud.kms.v1.EncryptRequest.additional_authenticated_data])
            is equal to
            [EncryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.EncryptRequest.additional_authenticated_data_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    plaintext: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    additional_authenticated_data: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    plaintext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.Int64Value,
    )
    additional_authenticated_data_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=8,
        message=wrappers_pb2.Int64Value,
    )


class DecryptRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKey][google.cloud.kms.v1.CryptoKey] to use for
            decryption. The server will choose the appropriate version.
        ciphertext (bytes):
            Required. The encrypted data originally returned in
            [EncryptResponse.ciphertext][google.cloud.kms.v1.EncryptResponse.ciphertext].
        additional_authenticated_data (bytes):
            Optional. Optional data that must match the data originally
            supplied in
            [EncryptRequest.additional_authenticated_data][google.cloud.kms.v1.EncryptRequest.additional_authenticated_data].
        ciphertext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [DecryptRequest.ciphertext][google.cloud.kms.v1.DecryptRequest.ciphertext].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [DecryptRequest.ciphertext][google.cloud.kms.v1.DecryptRequest.ciphertext]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([DecryptRequest.ciphertext][google.cloud.kms.v1.DecryptRequest.ciphertext])
            is equal to
            [DecryptRequest.ciphertext_crc32c][google.cloud.kms.v1.DecryptRequest.ciphertext_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
        additional_authenticated_data_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [DecryptRequest.additional_authenticated_data][google.cloud.kms.v1.DecryptRequest.additional_authenticated_data].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [DecryptRequest.additional_authenticated_data][google.cloud.kms.v1.DecryptRequest.additional_authenticated_data]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([DecryptRequest.additional_authenticated_data][google.cloud.kms.v1.DecryptRequest.additional_authenticated_data])
            is equal to
            [DecryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.DecryptRequest.additional_authenticated_data_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ciphertext: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    additional_authenticated_data: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    ciphertext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int64Value,
    )
    additional_authenticated_data_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.Int64Value,
    )


class RawEncryptRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.RawEncrypt][google.cloud.kms.v1.KeyManagementService.RawEncrypt].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use for encryption.
        plaintext (bytes):
            Required. The data to encrypt. Must be no larger than 64KiB.

            The maximum size depends on the key version's
            [protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level].
            For [SOFTWARE][google.cloud.kms.v1.ProtectionLevel.SOFTWARE]
            keys, the plaintext must be no larger than 64KiB. For
            [HSM][google.cloud.kms.v1.ProtectionLevel.HSM] keys, the
            combined length of the plaintext and
            additional_authenticated_data fields must be no larger than
            8KiB.
        additional_authenticated_data (bytes):
            Optional. Optional data that, if specified, must also be
            provided during decryption through
            [RawDecryptRequest.additional_authenticated_data][google.cloud.kms.v1.RawDecryptRequest.additional_authenticated_data].

            This field may only be used in conjunction with an
            [algorithm][google.cloud.kms.v1.CryptoKeyVersion.algorithm]
            that accepts additional authenticated data (for example,
            AES-GCM).

            The maximum size depends on the key version's
            [protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level].
            For [SOFTWARE][google.cloud.kms.v1.ProtectionLevel.SOFTWARE]
            keys, the plaintext must be no larger than 64KiB. For
            [HSM][google.cloud.kms.v1.ProtectionLevel.HSM] keys, the
            combined length of the plaintext and
            additional_authenticated_data fields must be no larger than
            8KiB.
        plaintext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [RawEncryptRequest.plaintext][google.cloud.kms.v1.RawEncryptRequest.plaintext].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received plaintext using
            this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C(plaintext) is equal to plaintext_crc32c, and if so,
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        additional_authenticated_data_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [RawEncryptRequest.additional_authenticated_data][google.cloud.kms.v1.RawEncryptRequest.additional_authenticated_data].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            additional_authenticated_data using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C(additional_authenticated_data) is equal to
            additional_authenticated_data_crc32c, and if so, perform a
            limited number of retries. A persistent mismatch may
            indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        initialization_vector (bytes):
            Optional. A customer-supplied initialization vector that
            will be used for encryption. If it is not provided for
            AES-CBC and AES-CTR, one will be generated. It will be
            returned in
            [RawEncryptResponse.initialization_vector][google.cloud.kms.v1.RawEncryptResponse.initialization_vector].
        initialization_vector_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [RawEncryptRequest.initialization_vector][google.cloud.kms.v1.RawEncryptRequest.initialization_vector].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            initialization_vector using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C(initialization_vector) is equal to
            initialization_vector_crc32c, and if so, perform a limited
            number of retries. A persistent mismatch may indicate an
            issue in your computation of the CRC32C checksum. Note: This
            field is defined as int64 for reasons of compatibility
            across different languages. However, it is a non-negative
            integer, which will never exceed 2^32-1, and can be safely
            downconverted to uint32 in languages that support this type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    plaintext: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    additional_authenticated_data: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    plaintext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int64Value,
    )
    additional_authenticated_data_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int64Value,
    )
    initialization_vector: bytes = proto.Field(
        proto.BYTES,
        number=6,
    )
    initialization_vector_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.Int64Value,
    )


class RawDecryptRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.RawDecrypt][google.cloud.kms.v1.KeyManagementService.RawDecrypt].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use for decryption.
        ciphertext (bytes):
            Required. The encrypted data originally returned in
            [RawEncryptResponse.ciphertext][google.cloud.kms.v1.RawEncryptResponse.ciphertext].
        additional_authenticated_data (bytes):
            Optional. Optional data that must match the data originally
            supplied in
            [RawEncryptRequest.additional_authenticated_data][google.cloud.kms.v1.RawEncryptRequest.additional_authenticated_data].
        initialization_vector (bytes):
            Required. The initialization vector (IV) used during
            encryption, which must match the data originally provided in
            [RawEncryptResponse.initialization_vector][google.cloud.kms.v1.RawEncryptResponse.initialization_vector].
        tag_length (int):
            The length of the authentication tag that is
            appended to the end of the ciphertext. If
            unspecified (0), the default value for the key's
            algorithm will be used (for AES-GCM, the default
            value is 16).
        ciphertext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [RawDecryptRequest.ciphertext][google.cloud.kms.v1.RawDecryptRequest.ciphertext].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received ciphertext using
            this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C(ciphertext) is equal to ciphertext_crc32c, and if so,
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        additional_authenticated_data_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [RawDecryptRequest.additional_authenticated_data][google.cloud.kms.v1.RawDecryptRequest.additional_authenticated_data].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            additional_authenticated_data using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C(additional_authenticated_data) is equal to
            additional_authenticated_data_crc32c, and if so, perform a
            limited number of retries. A persistent mismatch may
            indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        initialization_vector_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [RawDecryptRequest.initialization_vector][google.cloud.kms.v1.RawDecryptRequest.initialization_vector].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            initialization_vector using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C(initialization_vector) is equal to
            initialization_vector_crc32c, and if so, perform a limited
            number of retries. A persistent mismatch may indicate an
            issue in your computation of the CRC32C checksum. Note: This
            field is defined as int64 for reasons of compatibility
            across different languages. However, it is a non-negative
            integer, which will never exceed 2^32-1, and can be safely
            downconverted to uint32 in languages that support this type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ciphertext: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    additional_authenticated_data: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    initialization_vector: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    tag_length: int = proto.Field(
        proto.INT32,
        number=5,
    )
    ciphertext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.Int64Value,
    )
    additional_authenticated_data_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.Int64Value,
    )
    initialization_vector_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=8,
        message=wrappers_pb2.Int64Value,
    )


class AsymmetricSignRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use for signing.
        digest (google.cloud.kms_v1.types.Digest):
            Optional. The digest of the data to sign. The digest must be
            produced with the same digest algorithm as specified by the
            key version's
            [algorithm][google.cloud.kms.v1.CryptoKeyVersion.algorithm].

            This field may not be supplied if
            [AsymmetricSignRequest.data][google.cloud.kms.v1.AsymmetricSignRequest.data]
            is supplied.
        digest_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [AsymmetricSignRequest.digest][google.cloud.kms.v1.AsymmetricSignRequest.digest].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [AsymmetricSignRequest.digest][google.cloud.kms.v1.AsymmetricSignRequest.digest]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([AsymmetricSignRequest.digest][google.cloud.kms.v1.AsymmetricSignRequest.digest])
            is equal to
            [AsymmetricSignRequest.digest_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.digest_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
        data (bytes):
            Optional. The data to sign. It can't be supplied if
            [AsymmetricSignRequest.digest][google.cloud.kms.v1.AsymmetricSignRequest.digest]
            is supplied.
        data_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [AsymmetricSignRequest.data][google.cloud.kms.v1.AsymmetricSignRequest.data].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [AsymmetricSignRequest.data][google.cloud.kms.v1.AsymmetricSignRequest.data]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([AsymmetricSignRequest.data][google.cloud.kms.v1.AsymmetricSignRequest.data])
            is equal to
            [AsymmetricSignRequest.data_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.data_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    digest: "Digest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Digest",
    )
    digest_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int64Value,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=6,
    )
    data_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.Int64Value,
    )


class AsymmetricDecryptRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.AsymmetricDecrypt][google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use for decryption.
        ciphertext (bytes):
            Required. The data encrypted with the named
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]'s
            public key using OAEP.
        ciphertext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [AsymmetricDecryptRequest.ciphertext][google.cloud.kms.v1.AsymmetricDecryptRequest.ciphertext].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [AsymmetricDecryptRequest.ciphertext][google.cloud.kms.v1.AsymmetricDecryptRequest.ciphertext]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([AsymmetricDecryptRequest.ciphertext][google.cloud.kms.v1.AsymmetricDecryptRequest.ciphertext])
            is equal to
            [AsymmetricDecryptRequest.ciphertext_crc32c][google.cloud.kms.v1.AsymmetricDecryptRequest.ciphertext_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ciphertext: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    ciphertext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int64Value,
    )


class MacSignRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.MacSign][google.cloud.kms.v1.KeyManagementService.MacSign].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use for signing.
        data (bytes):
            Required. The data to sign. The MAC tag is
            computed over this data field based on the
            specific algorithm.
        data_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [MacSignRequest.data][google.cloud.kms.v1.MacSignRequest.data].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [MacSignRequest.data][google.cloud.kms.v1.MacSignRequest.data]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([MacSignRequest.data][google.cloud.kms.v1.MacSignRequest.data])
            is equal to
            [MacSignRequest.data_crc32c][google.cloud.kms.v1.MacSignRequest.data_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    data_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int64Value,
    )


class MacVerifyRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.MacVerify][google.cloud.kms.v1.KeyManagementService.MacVerify].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use for verification.
        data (bytes):
            Required. The data used previously as a
            [MacSignRequest.data][google.cloud.kms.v1.MacSignRequest.data]
            to generate the MAC tag.
        data_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [MacVerifyRequest.data][google.cloud.kms.v1.MacVerifyRequest.data].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [MacVerifyRequest.data][google.cloud.kms.v1.MacVerifyRequest.data]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([MacVerifyRequest.data][google.cloud.kms.v1.MacVerifyRequest.data])
            is equal to
            [MacVerifyRequest.data_crc32c][google.cloud.kms.v1.MacVerifyRequest.data_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
        mac (bytes):
            Required. The signature to verify.
        mac_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. An optional CRC32C checksum of the
            [MacVerifyRequest.mac][google.cloud.kms.v1.MacVerifyRequest.mac].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [MacVerifyRequest.mac][google.cloud.kms.v1.MacVerifyRequest.mac]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([MacVerifyRequest.mac][google.cloud.kms.v1.MacVerifyRequest.mac])
            is equal to
            [MacVerifyRequest.mac_crc32c][google.cloud.kms.v1.MacVerifyRequest.mac_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    data_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int64Value,
    )
    mac: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    mac_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int64Value,
    )


class DecapsulateRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.Decapsulate][google.cloud.kms.v1.KeyManagementService.Decapsulate].

    Attributes:
        name (str):
            Required. The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
            use for decapsulation.
        ciphertext (bytes):
            Required. The ciphertext produced from encapsulation with
            the named
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            public key(s).
        ciphertext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Optional. A CRC32C checksum of the
            [DecapsulateRequest.ciphertext][google.cloud.kms.v1.DecapsulateRequest.ciphertext].
            If specified,
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will verify the integrity of the received
            [DecapsulateRequest.ciphertext][google.cloud.kms.v1.DecapsulateRequest.ciphertext]
            using this checksum.
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            will report an error if the checksum verification fails. If
            you receive a checksum error, your client should verify that
            CRC32C([DecapsulateRequest.ciphertext][google.cloud.kms.v1.DecapsulateRequest.ciphertext])
            is equal to
            [DecapsulateRequest.ciphertext_crc32c][google.cloud.kms.v1.DecapsulateRequest.ciphertext_crc32c],
            and if so, perform a limited number of retries. A persistent
            mismatch may indicate an issue in your computation of the
            CRC32C checksum. Note: This field is defined as int64 for
            reasons of compatibility across different languages.
            However, it is a non-negative integer, which will never
            exceed 2^32-1, and can be safely downconverted to uint32 in
            languages that support this type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ciphertext: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    ciphertext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int64Value,
    )


class GenerateRandomBytesRequest(proto.Message):
    r"""Request message for
    [KeyManagementService.GenerateRandomBytes][google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes].

    Attributes:
        location (str):
            The project-specific location in which to
            generate random bytes. For example,
            "projects/my-project/locations/us-central1".
        length_bytes (int):
            The length in bytes of the amount of
            randomness to retrieve.  Minimum 8 bytes,
            maximum 1024 bytes.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            to use when generating the random data. Currently, only
            [HSM][google.cloud.kms.v1.ProtectionLevel.HSM] protection
            level is supported.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    length_bytes: int = proto.Field(
        proto.INT32,
        number=2,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=3,
        enum=resources.ProtectionLevel,
    )


class EncryptResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].

    Attributes:
        name (str):
            The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used in encryption. Check this field to verify that the
            intended resource was used for encryption.
        ciphertext (bytes):
            The encrypted data.
        ciphertext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [EncryptResponse.ciphertext][google.cloud.kms.v1.EncryptResponse.ciphertext].
            An integrity check of
            [EncryptResponse.ciphertext][google.cloud.kms.v1.EncryptResponse.ciphertext]
            can be performed by computing the CRC32C checksum of
            [EncryptResponse.ciphertext][google.cloud.kms.v1.EncryptResponse.ciphertext]
            and comparing your results to this field. Discard the
            response in case of non-matching checksum values, and
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        verified_plaintext_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [EncryptRequest.plaintext_crc32c][google.cloud.kms.v1.EncryptRequest.plaintext_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the
            [plaintext][google.cloud.kms.v1.EncryptRequest.plaintext]. A
            false value of this field indicates either that
            [EncryptRequest.plaintext_crc32c][google.cloud.kms.v1.EncryptRequest.plaintext_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [EncryptRequest.plaintext_crc32c][google.cloud.kms.v1.EncryptRequest.plaintext_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        verified_additional_authenticated_data_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [EncryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.EncryptRequest.additional_authenticated_data_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the
            [AAD][google.cloud.kms.v1.EncryptRequest.additional_authenticated_data].
            A false value of this field indicates either that
            [EncryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.EncryptRequest.additional_authenticated_data_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [EncryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.EncryptRequest.additional_authenticated_data_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used in encryption.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ciphertext: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    ciphertext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int64Value,
    )
    verified_plaintext_crc32c: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    verified_additional_authenticated_data_crc32c: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=7,
        enum=resources.ProtectionLevel,
    )


class DecryptResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt].

    Attributes:
        plaintext (bytes):
            The decrypted data originally supplied in
            [EncryptRequest.plaintext][google.cloud.kms.v1.EncryptRequest.plaintext].
        plaintext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [DecryptResponse.plaintext][google.cloud.kms.v1.DecryptResponse.plaintext].
            An integrity check of
            [DecryptResponse.plaintext][google.cloud.kms.v1.DecryptResponse.plaintext]
            can be performed by computing the CRC32C checksum of
            [DecryptResponse.plaintext][google.cloud.kms.v1.DecryptResponse.plaintext]
            and comparing your results to this field. Discard the
            response in case of non-matching checksum values, and
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: receiving this response message indicates
            that
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            is able to successfully decrypt the
            [ciphertext][google.cloud.kms.v1.DecryptRequest.ciphertext].
            Note: This field is defined as int64 for reasons of
            compatibility across different languages. However, it is a
            non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        used_primary (bool):
            Whether the Decryption was performed using
            the primary key version.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used in decryption.
    """

    plaintext: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    plaintext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int64Value,
    )
    used_primary: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=4,
        enum=resources.ProtectionLevel,
    )


class RawEncryptResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.RawEncrypt][google.cloud.kms.v1.KeyManagementService.RawEncrypt].

    Attributes:
        ciphertext (bytes):
            The encrypted data. In the case of AES-GCM, the
            authentication tag is the
            [tag_length][google.cloud.kms.v1.RawEncryptResponse.tag_length]
            bytes at the end of this field.
        initialization_vector (bytes):
            The initialization vector (IV) generated by the service
            during encryption. This value must be stored and provided in
            [RawDecryptRequest.initialization_vector][google.cloud.kms.v1.RawDecryptRequest.initialization_vector]
            at decryption time.
        tag_length (int):
            The length of the authentication tag that is
            appended to the end of the ciphertext.
        ciphertext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [RawEncryptResponse.ciphertext][google.cloud.kms.v1.RawEncryptResponse.ciphertext].
            An integrity check of ciphertext can be performed by
            computing the CRC32C checksum of ciphertext and comparing
            your results to this field. Discard the response in case of
            non-matching checksum values, and perform a limited number
            of retries. A persistent mismatch may indicate an issue in
            your computation of the CRC32C checksum. Note: This field is
            defined as int64 for reasons of compatibility across
            different languages. However, it is a non-negative integer,
            which will never exceed 2^32-1, and can be safely
            downconverted to uint32 in languages that support this type.
        initialization_vector_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [RawEncryptResponse.initialization_vector][google.cloud.kms.v1.RawEncryptResponse.initialization_vector].
            An integrity check of initialization_vector can be performed
            by computing the CRC32C checksum of initialization_vector
            and comparing your results to this field. Discard the
            response in case of non-matching checksum values, and
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        verified_plaintext_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [RawEncryptRequest.plaintext_crc32c][google.cloud.kms.v1.RawEncryptRequest.plaintext_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the plaintext. A
            false value of this field indicates either that
            [RawEncryptRequest.plaintext_crc32c][google.cloud.kms.v1.RawEncryptRequest.plaintext_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [RawEncryptRequest.plaintext_crc32c][google.cloud.kms.v1.RawEncryptRequest.plaintext_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        verified_additional_authenticated_data_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [RawEncryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.RawEncryptRequest.additional_authenticated_data_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of
            additional_authenticated_data. A false value of this field
            indicates either that //
            [RawEncryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.RawEncryptRequest.additional_authenticated_data_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [RawEncryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.RawEncryptRequest.additional_authenticated_data_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        verified_initialization_vector_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [RawEncryptRequest.initialization_vector_crc32c][google.cloud.kms.v1.RawEncryptRequest.initialization_vector_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of
            initialization_vector. A false value of this field indicates
            either that
            [RawEncryptRequest.initialization_vector_crc32c][google.cloud.kms.v1.RawEncryptRequest.initialization_vector_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [RawEncryptRequest.initialization_vector_crc32c][google.cloud.kms.v1.RawEncryptRequest.initialization_vector_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        name (str):
            The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used in encryption. Check this field to verify that the
            intended resource was used for encryption.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used in encryption.
    """

    ciphertext: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    initialization_vector: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    tag_length: int = proto.Field(
        proto.INT32,
        number=3,
    )
    ciphertext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.Int64Value,
    )
    initialization_vector_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int64Value,
    )
    verified_plaintext_crc32c: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    verified_additional_authenticated_data_crc32c: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    verified_initialization_vector_crc32c: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=9,
        enum=resources.ProtectionLevel,
    )


class RawDecryptResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.RawDecrypt][google.cloud.kms.v1.KeyManagementService.RawDecrypt].

    Attributes:
        plaintext (bytes):
            The decrypted data.
        plaintext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [RawDecryptResponse.plaintext][google.cloud.kms.v1.RawDecryptResponse.plaintext].
            An integrity check of plaintext can be performed by
            computing the CRC32C checksum of plaintext and comparing
            your results to this field. Discard the response in case of
            non-matching checksum values, and perform a limited number
            of retries. A persistent mismatch may indicate an issue in
            your computation of the CRC32C checksum. Note: receiving
            this response message indicates that
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            is able to successfully decrypt the
            [ciphertext][google.cloud.kms.v1.RawDecryptRequest.ciphertext].
            Note: This field is defined as int64 for reasons of
            compatibility across different languages. However, it is a
            non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used in decryption.
        verified_ciphertext_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [RawDecryptRequest.ciphertext_crc32c][google.cloud.kms.v1.RawDecryptRequest.ciphertext_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the ciphertext. A
            false value of this field indicates either that
            [RawDecryptRequest.ciphertext_crc32c][google.cloud.kms.v1.RawDecryptRequest.ciphertext_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [RawDecryptRequest.ciphertext_crc32c][google.cloud.kms.v1.RawDecryptRequest.ciphertext_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        verified_additional_authenticated_data_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [RawDecryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.RawDecryptRequest.additional_authenticated_data_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of
            additional_authenticated_data. A false value of this field
            indicates either that //
            [RawDecryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.RawDecryptRequest.additional_authenticated_data_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [RawDecryptRequest.additional_authenticated_data_crc32c][google.cloud.kms.v1.RawDecryptRequest.additional_authenticated_data_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        verified_initialization_vector_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [RawDecryptRequest.initialization_vector_crc32c][google.cloud.kms.v1.RawDecryptRequest.initialization_vector_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of
            initialization_vector. A false value of this field indicates
            either that
            [RawDecryptRequest.initialization_vector_crc32c][google.cloud.kms.v1.RawDecryptRequest.initialization_vector_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [RawDecryptRequest.initialization_vector_crc32c][google.cloud.kms.v1.RawDecryptRequest.initialization_vector_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
    """

    plaintext: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    plaintext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int64Value,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=3,
        enum=resources.ProtectionLevel,
    )
    verified_ciphertext_crc32c: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    verified_additional_authenticated_data_crc32c: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    verified_initialization_vector_crc32c: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class AsymmetricSignResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].

    Attributes:
        signature (bytes):
            The created signature.
        signature_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [AsymmetricSignResponse.signature][google.cloud.kms.v1.AsymmetricSignResponse.signature].
            An integrity check of
            [AsymmetricSignResponse.signature][google.cloud.kms.v1.AsymmetricSignResponse.signature]
            can be performed by computing the CRC32C checksum of
            [AsymmetricSignResponse.signature][google.cloud.kms.v1.AsymmetricSignResponse.signature]
            and comparing your results to this field. Discard the
            response in case of non-matching checksum values, and
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        verified_digest_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [AsymmetricSignRequest.digest_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.digest_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the
            [digest][google.cloud.kms.v1.AsymmetricSignRequest.digest].
            A false value of this field indicates either that
            [AsymmetricSignRequest.digest_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.digest_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [AsymmetricSignRequest.digest_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.digest_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        name (str):
            The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used for signing. Check this field to verify that the
            intended resource was used for signing.
        verified_data_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [AsymmetricSignRequest.data_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.data_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the
            [data][google.cloud.kms.v1.AsymmetricSignRequest.data]. A
            false value of this field indicates either that
            [AsymmetricSignRequest.data_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.data_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [AsymmetricSignRequest.data_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.data_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used for signing.
    """

    signature: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    signature_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int64Value,
    )
    verified_digest_crc32c: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    verified_data_crc32c: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=6,
        enum=resources.ProtectionLevel,
    )


class AsymmetricDecryptResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.AsymmetricDecrypt][google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt].

    Attributes:
        plaintext (bytes):
            The decrypted data originally encrypted with
            the matching public key.
        plaintext_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [AsymmetricDecryptResponse.plaintext][google.cloud.kms.v1.AsymmetricDecryptResponse.plaintext].
            An integrity check of
            [AsymmetricDecryptResponse.plaintext][google.cloud.kms.v1.AsymmetricDecryptResponse.plaintext]
            can be performed by computing the CRC32C checksum of
            [AsymmetricDecryptResponse.plaintext][google.cloud.kms.v1.AsymmetricDecryptResponse.plaintext]
            and comparing your results to this field. Discard the
            response in case of non-matching checksum values, and
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        verified_ciphertext_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [AsymmetricDecryptRequest.ciphertext_crc32c][google.cloud.kms.v1.AsymmetricDecryptRequest.ciphertext_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the
            [ciphertext][google.cloud.kms.v1.AsymmetricDecryptRequest.ciphertext].
            A false value of this field indicates either that
            [AsymmetricDecryptRequest.ciphertext_crc32c][google.cloud.kms.v1.AsymmetricDecryptRequest.ciphertext_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [AsymmetricDecryptRequest.ciphertext_crc32c][google.cloud.kms.v1.AsymmetricDecryptRequest.ciphertext_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used in decryption.
    """

    plaintext: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    plaintext_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.Int64Value,
    )
    verified_ciphertext_crc32c: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=4,
        enum=resources.ProtectionLevel,
    )


class MacSignResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.MacSign][google.cloud.kms.v1.KeyManagementService.MacSign].

    Attributes:
        name (str):
            The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used for signing. Check this field to verify that the
            intended resource was used for signing.
        mac (bytes):
            The created signature.
        mac_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [MacSignResponse.mac][google.cloud.kms.v1.MacSignResponse.mac].
            An integrity check of
            [MacSignResponse.mac][google.cloud.kms.v1.MacSignResponse.mac]
            can be performed by computing the CRC32C checksum of
            [MacSignResponse.mac][google.cloud.kms.v1.MacSignResponse.mac]
            and comparing your results to this field. Discard the
            response in case of non-matching checksum values, and
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
        verified_data_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [MacSignRequest.data_crc32c][google.cloud.kms.v1.MacSignRequest.data_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the
            [data][google.cloud.kms.v1.MacSignRequest.data]. A false
            value of this field indicates either that
            [MacSignRequest.data_crc32c][google.cloud.kms.v1.MacSignRequest.data_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [MacSignRequest.data_crc32c][google.cloud.kms.v1.MacSignRequest.data_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used for signing.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mac: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    mac_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int64Value,
    )
    verified_data_crc32c: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=5,
        enum=resources.ProtectionLevel,
    )


class MacVerifyResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.MacVerify][google.cloud.kms.v1.KeyManagementService.MacVerify].

    Attributes:
        name (str):
            The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used for verification. Check this field to verify that the
            intended resource was used for verification.
        success (bool):
            This field indicates whether or not the verification
            operation for
            [MacVerifyRequest.mac][google.cloud.kms.v1.MacVerifyRequest.mac]
            over
            [MacVerifyRequest.data][google.cloud.kms.v1.MacVerifyRequest.data]
            was successful.
        verified_data_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [MacVerifyRequest.data_crc32c][google.cloud.kms.v1.MacVerifyRequest.data_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the
            [data][google.cloud.kms.v1.MacVerifyRequest.data]. A false
            value of this field indicates either that
            [MacVerifyRequest.data_crc32c][google.cloud.kms.v1.MacVerifyRequest.data_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [MacVerifyRequest.data_crc32c][google.cloud.kms.v1.MacVerifyRequest.data_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        verified_mac_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [MacVerifyRequest.mac_crc32c][google.cloud.kms.v1.MacVerifyRequest.mac_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the
            [data][google.cloud.kms.v1.MacVerifyRequest.mac]. A false
            value of this field indicates either that
            [MacVerifyRequest.mac_crc32c][google.cloud.kms.v1.MacVerifyRequest.mac_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [MacVerifyRequest.mac_crc32c][google.cloud.kms.v1.MacVerifyRequest.mac_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        verified_success_integrity (bool):
            Integrity verification field. This value is used for the
            integrity verification of [MacVerifyResponse.success]. If
            the value of this field contradicts the value of
            [MacVerifyResponse.success], discard the response and
            perform a limited number of retries.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used for verification.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    success: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    verified_data_crc32c: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    verified_mac_crc32c: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    verified_success_integrity: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=6,
        enum=resources.ProtectionLevel,
    )


class DecapsulateResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.Decapsulate][google.cloud.kms.v1.KeyManagementService.Decapsulate].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used for decapsulation. Check this field to verify that the
            intended resource was used for decapsulation.
        shared_secret (bytes):
            The decapsulated shared_secret originally encapsulated with
            the matching public key.
        shared_secret_crc32c (int):
            Integrity verification field. A CRC32C checksum of the
            returned
            [DecapsulateResponse.shared_secret][google.cloud.kms.v1.DecapsulateResponse.shared_secret].
            An integrity check of
            [DecapsulateResponse.shared_secret][google.cloud.kms.v1.DecapsulateResponse.shared_secret]
            can be performed by computing the CRC32C checksum of
            [DecapsulateResponse.shared_secret][google.cloud.kms.v1.DecapsulateResponse.shared_secret]
            and comparing your results to this field. Discard the
            response in case of non-matching checksum values, and
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: receiving this response message indicates
            that
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            is able to successfully decrypt the
            [ciphertext][google.cloud.kms.v1.DecapsulateRequest.ciphertext].
            Note: This field is defined as int64 for reasons of
            compatibility across different languages. However, it is a
            non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.

            This field is a member of `oneof`_ ``_shared_secret_crc32c``.
        verified_ciphertext_crc32c (bool):
            Integrity verification field. A flag indicating whether
            [DecapsulateRequest.ciphertext_crc32c][google.cloud.kms.v1.DecapsulateRequest.ciphertext_crc32c]
            was received by
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService]
            and used for the integrity verification of the
            [ciphertext][google.cloud.kms.v1.DecapsulateRequest.ciphertext].
            A false value of this field indicates either that
            [DecapsulateRequest.ciphertext_crc32c][google.cloud.kms.v1.DecapsulateRequest.ciphertext_crc32c]
            was left unset or that it was not delivered to
            [KeyManagementService][google.cloud.kms.v1.KeyManagementService].
            If you've set
            [DecapsulateRequest.ciphertext_crc32c][google.cloud.kms.v1.DecapsulateRequest.ciphertext_crc32c]
            but this field is still false, discard the response and
            perform a limited number of retries.
        protection_level (google.cloud.kms_v1.types.ProtectionLevel):
            The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
            of the
            [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
            used in decapsulation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    shared_secret: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    shared_secret_crc32c: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    verified_ciphertext_crc32c: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    protection_level: resources.ProtectionLevel = proto.Field(
        proto.ENUM,
        number=5,
        enum=resources.ProtectionLevel,
    )


class GenerateRandomBytesResponse(proto.Message):
    r"""Response message for
    [KeyManagementService.GenerateRandomBytes][google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes].

    Attributes:
        data (bytes):
            The generated data.
        data_crc32c (google.protobuf.wrappers_pb2.Int64Value):
            Integrity verification field. A CRC32C checksum of the
            returned
            [GenerateRandomBytesResponse.data][google.cloud.kms.v1.GenerateRandomBytesResponse.data].
            An integrity check of
            [GenerateRandomBytesResponse.data][google.cloud.kms.v1.GenerateRandomBytesResponse.data]
            can be performed by computing the CRC32C checksum of
            [GenerateRandomBytesResponse.data][google.cloud.kms.v1.GenerateRandomBytesResponse.data]
            and comparing your results to this field. Discard the
            response in case of non-matching checksum values, and
            perform a limited number of retries. A persistent mismatch
            may indicate an issue in your computation of the CRC32C
            checksum. Note: This field is defined as int64 for reasons
            of compatibility across different languages. However, it is
            a non-negative integer, which will never exceed 2^32-1, and
            can be safely downconverted to uint32 in languages that
            support this type.
    """

    data: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    data_crc32c: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int64Value,
    )


class Digest(proto.Message):
    r"""A [Digest][google.cloud.kms.v1.Digest] holds a cryptographic message
    digest.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sha256 (bytes):
            A message digest produced with the SHA-256
            algorithm.

            This field is a member of `oneof`_ ``digest``.
        sha384 (bytes):
            A message digest produced with the SHA-384
            algorithm.

            This field is a member of `oneof`_ ``digest``.
        sha512 (bytes):
            A message digest produced with the SHA-512
            algorithm.

            This field is a member of `oneof`_ ``digest``.
        external_mu (bytes):
            A message digest produced with SHAKE-256, to
            be used with ML-DSA external-μ algorithms only.
            See "message representative" note in section
            6.2, algorithm 7 of the FIPS-204 standard:

            https://doi.org/10.6028/nist.fips.204

            This field is a member of `oneof`_ ``digest``.
    """

    sha256: bytes = proto.Field(
        proto.BYTES,
        number=1,
        oneof="digest",
    )
    sha384: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="digest",
    )
    sha512: bytes = proto.Field(
        proto.BYTES,
        number=3,
        oneof="digest",
    )
    external_mu: bytes = proto.Field(
        proto.BYTES,
        number=4,
        oneof="digest",
    )


class LocationMetadata(proto.Message):
    r"""Cloud KMS metadata for the given
    [google.cloud.location.Location][google.cloud.location.Location].

    Attributes:
        hsm_available (bool):
            Indicates whether
            [CryptoKeys][google.cloud.kms.v1.CryptoKey] with
            [protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level]
            [HSM][google.cloud.kms.v1.ProtectionLevel.HSM] can be
            created in this location.
        ekm_available (bool):
            Indicates whether
            [CryptoKeys][google.cloud.kms.v1.CryptoKey] with
            [protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level]
            [EXTERNAL][google.cloud.kms.v1.ProtectionLevel.EXTERNAL] can
            be created in this location.
        hsm_single_tenant_available (bool):
            Indicates whether
            [CryptoKeys][google.cloud.kms.v1.CryptoKey] with
            [protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level]
            [HSM_SINGLE_TENANT][google.cloud.kms.v1.ProtectionLevel.HSM_SINGLE_TENANT]
            can be created in this location.
    """

    hsm_available: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    ekm_available: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    hsm_single_tenant_available: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteCryptoKeyMetadata(proto.Message):
    r"""Represents the metadata of the
    [KeyManagementService.DeleteCryptoKey][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKey]
    long-running operation.

    Attributes:
        retired_resource (str):
            Output only. The resource name of the
            [RetiredResource][google.cloud.kms.v1.RetiredResource]
            created as a result of this operation, in the format
            ``projects/*/locations/*/retiredResources/*``.
    """

    retired_resource: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteCryptoKeyVersionMetadata(proto.Message):
    r"""Represents the metadata of the
    [KeyManagementService.DeleteCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKeyVersion]
    long-running operation.

    """


__all__ = tuple(sorted(__protobuf__.manifest))
