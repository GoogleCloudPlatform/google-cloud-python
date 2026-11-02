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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.expr_pb2 as expr_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.security.privateca.v1",
    manifest={
        "AttributeType",
        "RevocationReason",
        "SubjectRequestMode",
        "CertificateAuthority",
        "CaPool",
        "EncryptionSpec",
        "CertificateRevocationList",
        "Certificate",
        "CertificateTemplate",
        "X509Parameters",
        "SubordinateConfig",
        "PublicKey",
        "CertificateConfig",
        "CertificateDescription",
        "ObjectId",
        "X509Extension",
        "KeyUsage",
        "AttributeTypeAndValue",
        "RelativeDistinguishedName",
        "Subject",
        "SubjectAltNames",
        "CertificateIdentityConstraints",
        "CertificateExtensionConstraints",
    },
)


class AttributeType(proto.Enum):
    r"""[AttributeType][google.cloud.security.privateca.v1.AttributeType]
    specifies the type of Attribute in a relative distinguished name.

    Values:
        ATTRIBUTE_TYPE_UNSPECIFIED (0):
            Attribute type is unspecified.
        COMMON_NAME (1):
            The "common name" of the subject.
        COUNTRY_CODE (2):
            The country code of the subject.
        ORGANIZATION (3):
            The organization of the subject.
        ORGANIZATIONAL_UNIT (4):
            The organizational unit of the subject.
        LOCALITY (5):
            The locality or city of the subject.
        PROVINCE (6):
            The province, territory, or regional state of
            the subject.
        STREET_ADDRESS (7):
            The street address of the subject.
        POSTAL_CODE (8):
            The postal code of the subject.
    """

    ATTRIBUTE_TYPE_UNSPECIFIED = 0
    COMMON_NAME = 1
    COUNTRY_CODE = 2
    ORGANIZATION = 3
    ORGANIZATIONAL_UNIT = 4
    LOCALITY = 5
    PROVINCE = 6
    STREET_ADDRESS = 7
    POSTAL_CODE = 8


class RevocationReason(proto.Enum):
    r"""A
    [RevocationReason][google.cloud.security.privateca.v1.RevocationReason]
    indicates whether a
    [Certificate][google.cloud.security.privateca.v1.Certificate] has
    been revoked, and the reason for revocation. These correspond to
    standard revocation reasons from RFC 5280. Note that the enum labels
    and values in this definition are not the same ASN.1 values defined
    in RFC 5280. These values will be translated to the correct ASN.1
    values when a CRL is created.

    Values:
        REVOCATION_REASON_UNSPECIFIED (0):
            Default unspecified value. This value does indicate that a
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            has been revoked, but that a reason has not been recorded.
        KEY_COMPROMISE (1):
            Key material for this
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            may have leaked.
        CERTIFICATE_AUTHORITY_COMPROMISE (2):
            The key material for a certificate authority
            in the issuing path may have leaked.
        AFFILIATION_CHANGED (3):
            The subject or other attributes in this
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            have changed.
        SUPERSEDED (4):
            This
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            has been superseded.
        CESSATION_OF_OPERATION (5):
            This
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            or entities in the issuing path have ceased to operate.
        CERTIFICATE_HOLD (6):
            This
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            should not be considered valid, it is expected that it may
            become valid in the future.
        PRIVILEGE_WITHDRAWN (7):
            This
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            no longer has permission to assert the listed attributes.
        ATTRIBUTE_AUTHORITY_COMPROMISE (8):
            The authority which determines appropriate attributes for a
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            may have been compromised.
    """

    REVOCATION_REASON_UNSPECIFIED = 0
    KEY_COMPROMISE = 1
    CERTIFICATE_AUTHORITY_COMPROMISE = 2
    AFFILIATION_CHANGED = 3
    SUPERSEDED = 4
    CESSATION_OF_OPERATION = 5
    CERTIFICATE_HOLD = 6
    PRIVILEGE_WITHDRAWN = 7
    ATTRIBUTE_AUTHORITY_COMPROMISE = 8


class SubjectRequestMode(proto.Enum):
    r"""Describes the way in which a
    [Certificate][google.cloud.security.privateca.v1.Certificate]'s
    [Subject][google.cloud.security.privateca.v1.Subject] and/or
    [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames]
    will be resolved.

    Values:
        SUBJECT_REQUEST_MODE_UNSPECIFIED (0):
            Not specified.
        DEFAULT (1):
            The default mode used in most cases. Indicates that the
            certificate's
            [Subject][google.cloud.security.privateca.v1.Subject] and/or
            [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames]
            are specified in the certificate request. This mode requires
            the caller to have the ``privateca.certificates.create``
            permission.
        RDN_SEQUENCE (3):
            A mode used to get an accurate representation of the Subject
            field's distinguished name. Indicates that the certificate's
            [Subject][google.cloud.security.privateca.v1.Subject] and/or
            [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames]
            are specified in the certificate request. When parsing a PEM
            CSR this mode will maintain the sequence of RDNs found in
            the CSR's subject field in the issued
            [Certificate][google.cloud.security.privateca.v1.Certificate].
            This mode requires the caller to have the
            ``privateca.certificates.create`` permission.
        REFLECTED_SPIFFE (2):
            A mode reserved for special cases. Indicates that the
            certificate should have one SPIFFE
            [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames]
            set by the service based on the caller's identity. This mode
            will ignore any explicitly specified
            [Subject][google.cloud.security.privateca.v1.Subject] and/or
            [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames]
            in the certificate request. This mode requires the caller to
            have the ``privateca.certificates.createForSelf``
            permission.
    """

    SUBJECT_REQUEST_MODE_UNSPECIFIED = 0
    DEFAULT = 1
    RDN_SEQUENCE = 3
    REFLECTED_SPIFFE = 2


class CertificateAuthority(proto.Message):
    r"""A
    [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
    represents an individual Certificate Authority. A
    [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
    can be used to create
    [Certificates][google.cloud.security.privateca.v1.Certificate].

    Attributes:
        name (str):
            Identifier. The resource name for this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.
        type_ (google.cloud.security.privateca_v1.types.CertificateAuthority.Type):
            Required. Immutable. The
            [Type][google.cloud.security.privateca.v1.CertificateAuthority.Type]
            of this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
        config (google.cloud.security.privateca_v1.types.CertificateConfig):
            Required. Immutable. The config used to
            create a self-signed X.509 certificate or CSR.
        lifetime (google.protobuf.duration_pb2.Duration):
            Required. Immutable. The desired lifetime of the CA
            certificate. Used to create the "not_before_time" and
            "not_after_time" fields inside an X.509 certificate.
        key_spec (google.cloud.security.privateca_v1.types.CertificateAuthority.KeyVersionSpec):
            Required. Immutable. Used when issuing certificates for this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
            If this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            is a self-signed CertificateAuthority, this key is also used
            to sign the self-signed CA certificate. Otherwise, it is
            used to sign a CSR.
        subordinate_config (google.cloud.security.privateca_v1.types.SubordinateConfig):
            Optional. If this is a subordinate
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority],
            this field will be set with the subordinate configuration,
            which describes its issuers. This may be updated, but this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            must continue to validate.
        tier (google.cloud.security.privateca_v1.types.CaPool.Tier):
            Output only. The
            [CaPool.Tier][google.cloud.security.privateca.v1.CaPool.Tier]
            of the [CaPool][google.cloud.security.privateca.v1.CaPool]
            that includes this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
        state (google.cloud.security.privateca_v1.types.CertificateAuthority.State):
            Output only. The
            [State][google.cloud.security.privateca.v1.CertificateAuthority.State]
            for this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
        pem_ca_certificates (MutableSequence[str]):
            Output only. This
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
            certificate chain, including the current
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
            certificate. Ordered such that the root issuer is the final
            element (consistent with RFC 5246). For a self-signed CA,
            this will only list the current
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
            certificate.
        ca_certificate_descriptions (MutableSequence[google.cloud.security.privateca_v1.types.CertificateDescription]):
            Output only. A structured description of this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
            CA certificate and its issuers. Ordered as self-to-root.
        gcs_bucket (str):
            Immutable. The name of a Cloud Storage bucket where this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            will publish content, such as the CA certificate and CRLs.
            This must be a bucket name, without any prefixes (such as
            ``gs://``) or suffixes (such as ``.googleapis.com``). For
            example, to use a bucket named ``my-bucket``, you would
            simply specify ``my-bucket``. If not specified, a managed
            bucket will be created.
        access_urls (google.cloud.security.privateca_v1.types.CertificateAuthority.AccessUrls):
            Output only. URLs for accessing content
            published by this CA, such as the CA certificate
            and CRLs.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            was last updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            was soft deleted, if it is in the
            [DELETED][google.cloud.security.privateca.v1.CertificateAuthority.State.DELETED]
            state.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            will be permanently purged, if it is in the
            [DELETED][google.cloud.security.privateca.v1.CertificateAuthority.State.DELETED]
            state.
        labels (MutableMapping[str, str]):
            Optional. Labels with user-defined metadata.
        user_defined_access_urls (google.cloud.security.privateca_v1.types.CertificateAuthority.UserDefinedAccessUrls):
            Optional. User-defined URLs for CA
            certificate and CRLs. The service does not
            publish content to these URLs. It is up to the
            user to mirror content to these URLs.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
    """

    class Type(proto.Enum):
        r"""The type of a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority],
        indicating its issuing chain.

        Values:
            TYPE_UNSPECIFIED (0):
                Not specified.
            SELF_SIGNED (1):
                Self-signed CA.
            SUBORDINATE (2):
                Subordinate CA. Could be issued by a Private CA
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                or an unmanaged CA.
        """

        TYPE_UNSPECIFIED = 0
        SELF_SIGNED = 1
        SUBORDINATE = 2

    class State(proto.Enum):
        r"""The state of a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority],
        indicating if it can be used.

        Values:
            STATE_UNSPECIFIED (0):
                Not specified.
            ENABLED (1):
                Certificates can be issued from this CA. CRLs will be
                generated for this CA. The CA will be part of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]'s trust
                anchor, and will be used to issue certificates from the
                [CaPool][google.cloud.security.privateca.v1.CaPool].
            DISABLED (2):
                Certificates cannot be issued from this CA. CRLs will still
                be generated. The CA will be part of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]'s trust
                anchor, but will not be used to issue certificates from the
                [CaPool][google.cloud.security.privateca.v1.CaPool].
            STAGED (3):
                Certificates can be issued from this CA. CRLs will be
                generated for this CA. The CA will be part of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]'s trust
                anchor, but will not be used to issue certificates from the
                [CaPool][google.cloud.security.privateca.v1.CaPool].
            AWAITING_USER_ACTIVATION (4):
                Certificates cannot be issued from this CA. CRLs will not be
                generated. The CA will not be part of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]'s trust
                anchor, and will not be used to issue certificates from the
                [CaPool][google.cloud.security.privateca.v1.CaPool].
            DELETED (5):
                Certificates cannot be issued from this CA. CRLs will not be
                generated. The CA may still be recovered by calling
                [CertificateAuthorityService.UndeleteCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.UndeleteCertificateAuthority]
                before
                [expire_time][google.cloud.security.privateca.v1.CertificateAuthority.expire_time].
                The CA will not be part of the
                [CaPool][google.cloud.security.privateca.v1.CaPool]'s trust
                anchor, and will not be used to issue certificates from the
                [CaPool][google.cloud.security.privateca.v1.CaPool].
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2
        STAGED = 3
        AWAITING_USER_ACTIVATION = 4
        DELETED = 5

    class SignHashAlgorithm(proto.Enum):
        r"""The algorithm of a Cloud KMS CryptoKeyVersion of a
        [CryptoKey][google.cloud.kms.v1.CryptoKey] with the
        [CryptoKeyPurpose][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose]
        value ``ASYMMETRIC_SIGN``. These values correspond to the
        [CryptoKeyVersionAlgorithm][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm]
        values. For RSA signing algorithms, the PSS algorithms should be
        preferred, use PKCS1 algorithms if required for compatibility. For
        further recommendations, see
        https://cloud.google.com/kms/docs/algorithms#algorithm_recommendations.

        Values:
            SIGN_HASH_ALGORITHM_UNSPECIFIED (0):
                Not specified.
            RSA_PSS_2048_SHA256 (1):
                maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_2048_SHA256
            RSA_PSS_3072_SHA256 (2):
                maps to CryptoKeyVersionAlgorithm. RSA_SIGN_PSS_3072_SHA256
            RSA_PSS_4096_SHA256 (3):
                maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_4096_SHA256
            RSA_PKCS1_2048_SHA256 (6):
                maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_2048_SHA256
            RSA_PKCS1_3072_SHA256 (7):
                maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_3072_SHA256
            RSA_PKCS1_4096_SHA256 (8):
                maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_4096_SHA256
            EC_P256_SHA256 (4):
                maps to CryptoKeyVersionAlgorithm.EC_SIGN_P256_SHA256
            EC_P384_SHA384 (5):
                maps to CryptoKeyVersionAlgorithm.EC_SIGN_P384_SHA384
        """

        SIGN_HASH_ALGORITHM_UNSPECIFIED = 0
        RSA_PSS_2048_SHA256 = 1
        RSA_PSS_3072_SHA256 = 2
        RSA_PSS_4096_SHA256 = 3
        RSA_PKCS1_2048_SHA256 = 6
        RSA_PKCS1_3072_SHA256 = 7
        RSA_PKCS1_4096_SHA256 = 8
        EC_P256_SHA256 = 4
        EC_P384_SHA384 = 5

    class AccessUrls(proto.Message):
        r"""URLs where a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        will publish content.

        Attributes:
            ca_certificate_access_url (str):
                The URL where this
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
                CA certificate is published. This will only be set for CAs
                that have been activated.
            crl_access_urls (MutableSequence[str]):
                The URLs where this
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
                CRLs are published. This will only be set for CAs that have
                been activated.
        """

        ca_certificate_access_url: str = proto.Field(
            proto.STRING,
            number=1,
        )
        crl_access_urls: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class KeyVersionSpec(proto.Message):
        r"""A Cloud KMS key configuration that a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        will use.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            cloud_kms_key_version (str):
                The resource name for an existing Cloud KMS CryptoKeyVersion
                in the format
                ``projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*``.
                This option enables full flexibility in the key's
                capabilities and properties.

                This field is a member of `oneof`_ ``KeyVersion``.
            algorithm (google.cloud.security.privateca_v1.types.CertificateAuthority.SignHashAlgorithm):
                The algorithm to use for creating a managed Cloud KMS key
                for a for a simplified experience. All managed keys will be
                have their
                [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] as
                ``HSM``.

                This field is a member of `oneof`_ ``KeyVersion``.
        """

        cloud_kms_key_version: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="KeyVersion",
        )
        algorithm: "CertificateAuthority.SignHashAlgorithm" = proto.Field(
            proto.ENUM,
            number=2,
            oneof="KeyVersion",
            enum="CertificateAuthority.SignHashAlgorithm",
        )

    class UserDefinedAccessUrls(proto.Message):
        r"""User-defined URLs for accessing content published by this
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

        Attributes:
            aia_issuing_certificate_urls (MutableSequence[str]):
                Optional. A list of URLs where the issuer CA certificate may
                be downloaded, which appears in the "Authority Information
                Access" extension in the certificate. If specified, the
                default [Cloud Storage
                URLs][google.cloud.security.privateca.v1.CertificateAuthority.AccessUrls.ca_certificate_access_url]
                will be omitted.
            crl_access_urls (MutableSequence[str]):
                Optional. A list of URLs where to obtain CRL information,
                i.e. the DistributionPoint.fullName described by
                https://tools.ietf.org/html/rfc5280#section-4.2.1.13. If
                specified, the default [Cloud Storage
                URLs][google.cloud.security.privateca.v1.CertificateAuthority.AccessUrls.crl_access_urls]
                will be omitted.
        """

        aia_issuing_certificate_urls: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        crl_access_urls: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    config: "CertificateConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CertificateConfig",
    )
    lifetime: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    key_spec: KeyVersionSpec = proto.Field(
        proto.MESSAGE,
        number=5,
        message=KeyVersionSpec,
    )
    subordinate_config: "SubordinateConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SubordinateConfig",
    )
    tier: "CaPool.Tier" = proto.Field(
        proto.ENUM,
        number=7,
        enum="CaPool.Tier",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    pem_ca_certificates: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    ca_certificate_descriptions: MutableSequence["CertificateDescription"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message="CertificateDescription",
        )
    )
    gcs_bucket: str = proto.Field(
        proto.STRING,
        number=11,
    )
    access_urls: AccessUrls = proto.Field(
        proto.MESSAGE,
        number=12,
        message=AccessUrls,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=17,
    )
    user_defined_access_urls: UserDefinedAccessUrls = proto.Field(
        proto.MESSAGE,
        number=18,
        message=UserDefinedAccessUrls,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=20,
    )


class CaPool(proto.Message):
    r"""A [CaPool][google.cloud.security.privateca.v1.CaPool] represents a
    group of
    [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority]
    that form a trust anchor. A
    [CaPool][google.cloud.security.privateca.v1.CaPool] can be used to
    manage issuance policies for one or more
    [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
    resources and to rotate CA certificates in and out of the trust
    anchor.

    Attributes:
        name (str):
            Identifier. The resource name for this
            [CaPool][google.cloud.security.privateca.v1.CaPool] in the
            format ``projects/*/locations/*/caPools/*``.
        tier (google.cloud.security.privateca_v1.types.CaPool.Tier):
            Required. Immutable. The
            [Tier][google.cloud.security.privateca.v1.CaPool.Tier] of
            this [CaPool][google.cloud.security.privateca.v1.CaPool].
        issuance_policy (google.cloud.security.privateca_v1.types.CaPool.IssuancePolicy):
            Optional. The
            [IssuancePolicy][google.cloud.security.privateca.v1.CaPool.IssuancePolicy]
            to control how
            [Certificates][google.cloud.security.privateca.v1.Certificate]
            will be issued from this
            [CaPool][google.cloud.security.privateca.v1.CaPool].
        publishing_options (google.cloud.security.privateca_v1.types.CaPool.PublishingOptions):
            Optional. The
            [PublishingOptions][google.cloud.security.privateca.v1.CaPool.PublishingOptions]
            to follow when issuing
            [Certificates][google.cloud.security.privateca.v1.Certificate]
            from any
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in this [CaPool][google.cloud.security.privateca.v1.CaPool].
        encryption_spec (google.cloud.security.privateca_v1.types.EncryptionSpec):
            Optional. When
            [EncryptionSpec][google.cloud.security.privateca.v1.EncryptionSpec]
            is provided, the
            [Subject][google.cloud.security.privateca.v1.Subject],
            [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames],
            and the PEM-encoded certificate fields will be encrypted at
            rest.
        labels (MutableMapping[str, str]):
            Optional. Labels with user-defined metadata.
    """

    class Tier(proto.Enum):
        r"""The tier of a [CaPool][google.cloud.security.privateca.v1.CaPool],
        indicating its supported functionality and/or billing SKU.

        Values:
            TIER_UNSPECIFIED (0):
                Not specified.
            ENTERPRISE (1):
                Enterprise tier.
            DEVOPS (2):
                DevOps tier.
        """

        TIER_UNSPECIFIED = 0
        ENTERPRISE = 1
        DEVOPS = 2

    class PublishingOptions(proto.Message):
        r"""Options relating to the publication of each
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
        CA certificate and CRLs and their inclusion as extensions in issued
        [Certificates][google.cloud.security.privateca.v1.Certificate]. The
        options set here apply to certificates issued by any
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        in the [CaPool][google.cloud.security.privateca.v1.CaPool].

        Attributes:
            publish_ca_cert (bool):
                Optional. When true, publishes each
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
                CA certificate and includes its URL in the "Authority
                Information Access" X.509 extension in all issued
                [Certificates][google.cloud.security.privateca.v1.Certificate].
                If this is false, the CA certificate will not be published
                and the corresponding X.509 extension will not be written in
                issued certificates.
            publish_crl (bool):
                Optional. When true, publishes each
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
                CRL and includes its URL in the "CRL Distribution Points"
                X.509 extension in all issued
                [Certificates][google.cloud.security.privateca.v1.Certificate].
                If this is false, CRLs will not be published and the
                corresponding X.509 extension will not be written in issued
                certificates. CRLs will expire 7 days from their creation.
                However, we will rebuild daily. CRLs are also rebuilt
                shortly after a certificate is revoked.
            encoding_format (google.cloud.security.privateca_v1.types.CaPool.PublishingOptions.EncodingFormat):
                Optional. Specifies the encoding format of each
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                resource's CA certificate and CRLs. If this is omitted, CA
                certificates and CRLs will be published in PEM.
        """

        class EncodingFormat(proto.Enum):
            r"""Supported encoding formats for publishing.

            Values:
                ENCODING_FORMAT_UNSPECIFIED (0):
                    Not specified. By default, PEM format will be
                    used.
                PEM (1):
                    The
                    [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
                    CA certificate and CRLs will be published in PEM format.
                DER (2):
                    The
                    [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]'s
                    CA certificate and CRLs will be published in DER format.
            """

            ENCODING_FORMAT_UNSPECIFIED = 0
            PEM = 1
            DER = 2

        publish_ca_cert: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        publish_crl: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        encoding_format: "CaPool.PublishingOptions.EncodingFormat" = proto.Field(
            proto.ENUM,
            number=3,
            enum="CaPool.PublishingOptions.EncodingFormat",
        )

    class IssuancePolicy(proto.Message):
        r"""Defines controls over all certificate issuance within a
        [CaPool][google.cloud.security.privateca.v1.CaPool].

        Attributes:
            allowed_key_types (MutableSequence[google.cloud.security.privateca_v1.types.CaPool.IssuancePolicy.AllowedKeyType]):
                Optional. If any
                [AllowedKeyType][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType]
                is specified, then the certificate request's public key must
                match one of the key types listed here. Otherwise, any key
                may be used.
            backdate_duration (google.protobuf.duration_pb2.Duration):
                Optional. If set, all certificates issued from this
                [CaPool][google.cloud.security.privateca.v1.CaPool] will be
                backdated by this duration. The 'not_before_time' will be
                the issuance time minus this
                [backdate_duration][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.backdate_duration],
                and the 'not_after_time' will be adjusted to preserve the
                requested lifetime. The maximum duration that a certificate
                can be backdated with these options is 48 hours in the past.
                This option cannot be set if
                [allow_requester_specified_not_before_time][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.allow_requester_specified_not_before_time]
                is set.
            allow_requester_specified_not_before_time (bool):
                Optional. If set to true, allows requesters to specify the
                [requested_not_before_time][google.cloud.security.privateca.v1.Certificate.requested_not_before_time]
                field when creating a
                [Certificate][google.cloud.security.privateca.v1.Certificate].
                Certificates requested with this option enabled will have a
                'not_before_time' equal to the value specified in the
                request. The 'not_after_time' will be adjusted to preserve
                the requested lifetime. The maximum time that a certificate
                can be backdated with these options is 48 hours in the past.
                This option cannot be set if
                [backdate_duration][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.backdate_duration]
                is set.
            maximum_lifetime (google.protobuf.duration_pb2.Duration):
                Optional. The maximum lifetime allowed for issued
                [Certificates][google.cloud.security.privateca.v1.Certificate].
                Note that if the issuing
                [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
                expires before a
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                resource's requested maximum_lifetime, the effective
                lifetime will be explicitly truncated to match it.
            allowed_issuance_modes (google.cloud.security.privateca_v1.types.CaPool.IssuancePolicy.IssuanceModes):
                Optional. If specified, then only methods allowed in the
                [IssuanceModes][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes]
                may be used to issue
                [Certificates][google.cloud.security.privateca.v1.Certificate].
            baseline_values (google.cloud.security.privateca_v1.types.X509Parameters):
                Optional. A set of X.509 values that will be applied to all
                certificates issued through this
                [CaPool][google.cloud.security.privateca.v1.CaPool]. If a
                certificate request includes conflicting values for the same
                properties, they will be overwritten by the values defined
                here. If a certificate request uses a
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
                that defines conflicting
                [predefined_values][google.cloud.security.privateca.v1.CertificateTemplate.predefined_values]
                for the same properties, the certificate issuance request
                will fail.
            identity_constraints (google.cloud.security.privateca_v1.types.CertificateIdentityConstraints):
                Optional. Describes constraints on identities that may
                appear in
                [Certificates][google.cloud.security.privateca.v1.Certificate]
                issued through this
                [CaPool][google.cloud.security.privateca.v1.CaPool]. If this
                is omitted, then this
                [CaPool][google.cloud.security.privateca.v1.CaPool] will not
                add restrictions on a certificate's identity.
            passthrough_extensions (google.cloud.security.privateca_v1.types.CertificateExtensionConstraints):
                Optional. Describes the set of X.509 extensions that may
                appear in a
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                issued through this
                [CaPool][google.cloud.security.privateca.v1.CaPool]. If a
                certificate request sets extensions that don't appear in the
                [passthrough_extensions][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.passthrough_extensions],
                those extensions will be dropped. If a certificate request
                uses a
                [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
                with
                [predefined_values][google.cloud.security.privateca.v1.CertificateTemplate.predefined_values]
                that don't appear here, the certificate issuance request
                will fail. If this is omitted, then this
                [CaPool][google.cloud.security.privateca.v1.CaPool] will not
                add restrictions on a certificate's X.509 extensions. These
                constraints do not apply to X.509 extensions set in this
                [CaPool][google.cloud.security.privateca.v1.CaPool]'s
                [baseline_values][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.baseline_values].
        """

        class AllowedKeyType(proto.Message):
            r"""Describes a "type" of key that may be used in a
            [Certificate][google.cloud.security.privateca.v1.Certificate] issued
            from a [CaPool][google.cloud.security.privateca.v1.CaPool]. Note
            that a single
            [AllowedKeyType][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.AllowedKeyType]
            may refer to either a fully-qualified key algorithm, such as RSA
            4096, or a family of key algorithms, such as any RSA key.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                rsa (google.cloud.security.privateca_v1.types.CaPool.IssuancePolicy.AllowedKeyType.RsaKeyType):
                    Represents an allowed RSA key type.

                    This field is a member of `oneof`_ ``key_type``.
                elliptic_curve (google.cloud.security.privateca_v1.types.CaPool.IssuancePolicy.AllowedKeyType.EcKeyType):
                    Represents an allowed Elliptic Curve key
                    type.

                    This field is a member of `oneof`_ ``key_type``.
            """

            class RsaKeyType(proto.Message):
                r"""Describes an RSA key that may be used in a
                [Certificate][google.cloud.security.privateca.v1.Certificate] issued
                from a [CaPool][google.cloud.security.privateca.v1.CaPool].

                Attributes:
                    min_modulus_size (int):
                        Optional. The minimum allowed RSA modulus
                        size (inclusive), in bits. If this is not set,
                        or if set to zero, the service-level min RSA
                        modulus size will continue to apply.
                    max_modulus_size (int):
                        Optional. The maximum allowed RSA modulus
                        size (inclusive), in bits. If this is not set,
                        or if set to zero, the service will not enforce
                        an explicit upper bound on RSA modulus sizes.
                """

                min_modulus_size: int = proto.Field(
                    proto.INT64,
                    number=1,
                )
                max_modulus_size: int = proto.Field(
                    proto.INT64,
                    number=2,
                )

            class EcKeyType(proto.Message):
                r"""Describes an Elliptic Curve key that may be used in a
                [Certificate][google.cloud.security.privateca.v1.Certificate] issued
                from a [CaPool][google.cloud.security.privateca.v1.CaPool].

                Attributes:
                    signature_algorithm (google.cloud.security.privateca_v1.types.CaPool.IssuancePolicy.AllowedKeyType.EcKeyType.EcSignatureAlgorithm):
                        Optional. A signature algorithm that must be
                        used. If this is omitted, any EC-based signature
                        algorithm will be allowed.
                """

                class EcSignatureAlgorithm(proto.Enum):
                    r"""Describes an elliptic curve-based signature algorithm that may be
                    used in a
                    [Certificate][google.cloud.security.privateca.v1.Certificate] issued
                    from a [CaPool][google.cloud.security.privateca.v1.CaPool].

                    Values:
                        EC_SIGNATURE_ALGORITHM_UNSPECIFIED (0):
                            Not specified. Signifies that any signature
                            algorithm may be used.
                        ECDSA_P256 (1):
                            Refers to the Elliptic Curve Digital
                            Signature Algorithm over the NIST P-256 curve.
                        ECDSA_P384 (2):
                            Refers to the Elliptic Curve Digital
                            Signature Algorithm over the NIST P-384 curve.
                        EDDSA_25519 (3):
                            Refers to the Edwards-curve Digital Signature
                            Algorithm over curve 25519, as described in RFC
                            8410.
                    """

                    EC_SIGNATURE_ALGORITHM_UNSPECIFIED = 0
                    ECDSA_P256 = 1
                    ECDSA_P384 = 2
                    EDDSA_25519 = 3

                signature_algorithm: "CaPool.IssuancePolicy.AllowedKeyType.EcKeyType.EcSignatureAlgorithm" = proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="CaPool.IssuancePolicy.AllowedKeyType.EcKeyType.EcSignatureAlgorithm",
                )

            rsa: "CaPool.IssuancePolicy.AllowedKeyType.RsaKeyType" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="key_type",
                message="CaPool.IssuancePolicy.AllowedKeyType.RsaKeyType",
            )
            elliptic_curve: "CaPool.IssuancePolicy.AllowedKeyType.EcKeyType" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    oneof="key_type",
                    message="CaPool.IssuancePolicy.AllowedKeyType.EcKeyType",
                )
            )

        class IssuanceModes(proto.Message):
            r"""[IssuanceModes][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.IssuanceModes]
            specifies the allowed ways in which
            [Certificates][google.cloud.security.privateca.v1.Certificate] may
            be requested from this
            [CaPool][google.cloud.security.privateca.v1.CaPool].

            Attributes:
                allow_csr_based_issuance (bool):
                    Optional. When true, allows callers to create
                    [Certificates][google.cloud.security.privateca.v1.Certificate]
                    by specifying a CSR.
                allow_config_based_issuance (bool):
                    Optional. When true, allows callers to create
                    [Certificates][google.cloud.security.privateca.v1.Certificate]
                    by specifying a
                    [CertificateConfig][google.cloud.security.privateca.v1.CertificateConfig].
            """

            allow_csr_based_issuance: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            allow_config_based_issuance: bool = proto.Field(
                proto.BOOL,
                number=2,
            )

        allowed_key_types: MutableSequence["CaPool.IssuancePolicy.AllowedKeyType"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="CaPool.IssuancePolicy.AllowedKeyType",
            )
        )
        backdate_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=7,
            message=duration_pb2.Duration,
        )
        allow_requester_specified_not_before_time: bool = proto.Field(
            proto.BOOL,
            number=8,
        )
        maximum_lifetime: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        allowed_issuance_modes: "CaPool.IssuancePolicy.IssuanceModes" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="CaPool.IssuancePolicy.IssuanceModes",
        )
        baseline_values: "X509Parameters" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="X509Parameters",
        )
        identity_constraints: "CertificateIdentityConstraints" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="CertificateIdentityConstraints",
        )
        passthrough_extensions: "CertificateExtensionConstraints" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="CertificateExtensionConstraints",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tier: Tier = proto.Field(
        proto.ENUM,
        number=2,
        enum=Tier,
    )
    issuance_policy: IssuancePolicy = proto.Field(
        proto.MESSAGE,
        number=3,
        message=IssuancePolicy,
    )
    publishing_options: PublishingOptions = proto.Field(
        proto.MESSAGE,
        number=4,
        message=PublishingOptions,
    )
    encryption_spec: "EncryptionSpec" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="EncryptionSpec",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )


class EncryptionSpec(proto.Message):
    r"""The configuration used for encrypting data at rest.

    Attributes:
        cloud_kms_key (str):
            The resource name for a Cloud KMS key in the format
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
    """

    cloud_kms_key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CertificateRevocationList(proto.Message):
    r"""A
    [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
    corresponds to a signed X.509 certificate Revocation List (CRL). A
    CRL contains the serial numbers of certificates that should no
    longer be trusted.

    Attributes:
        name (str):
            Identifier. The resource name for this
            [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
            in the format
            ``projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*``.
        sequence_number (int):
            Output only. The CRL sequence number that appears in
            pem_crl.
        revoked_certificates (MutableSequence[google.cloud.security.privateca_v1.types.CertificateRevocationList.RevokedCertificate]):
            Output only. The revoked serial numbers that appear in
            pem_crl.
        pem_crl (str):
            Output only. The PEM-encoded X.509 CRL.
        access_url (str):
            Output only. The location where 'pem_crl' can be accessed.
        state (google.cloud.security.privateca_v1.types.CertificateRevocationList.State):
            Output only. The
            [State][google.cloud.security.privateca.v1.CertificateRevocationList.State]
            for this
            [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
            was updated.
        revision_id (str):
            Output only. The revision ID of this
            [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].
            A new revision is committed whenever a new CRL is published.
            The format is an 8-character hexadecimal string.
        labels (MutableMapping[str, str]):
            Optional. Labels with user-defined metadata.
    """

    class State(proto.Enum):
        r"""The state of a
        [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList],
        indicating if it is current.

        Values:
            STATE_UNSPECIFIED (0):
                Not specified.
            ACTIVE (1):
                The
                [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
                is up to date.
            SUPERSEDED (2):
                The
                [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList]
                is no longer current.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        SUPERSEDED = 2

    class RevokedCertificate(proto.Message):
        r"""Describes a revoked
        [Certificate][google.cloud.security.privateca.v1.Certificate].

        Attributes:
            certificate (str):
                The resource name for the
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                in the format
                ``projects/*/locations/*/caPools/*/certificates/*``.
            hex_serial_number (str):
                The serial number of the
                [Certificate][google.cloud.security.privateca.v1.Certificate].
            revocation_reason (google.cloud.security.privateca_v1.types.RevocationReason):
                The reason the
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                was revoked.
        """

        certificate: str = proto.Field(
            proto.STRING,
            number=1,
        )
        hex_serial_number: str = proto.Field(
            proto.STRING,
            number=2,
        )
        revocation_reason: "RevocationReason" = proto.Field(
            proto.ENUM,
            number=3,
            enum="RevocationReason",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sequence_number: int = proto.Field(
        proto.INT64,
        number=2,
    )
    revoked_certificates: MutableSequence[RevokedCertificate] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=RevokedCertificate,
    )
    pem_crl: str = proto.Field(
        proto.STRING,
        number=4,
    )
    access_url: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )


class Certificate(proto.Message):
    r"""A [Certificate][google.cloud.security.privateca.v1.Certificate]
    corresponds to a signed X.509 certificate issued by a
    [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name for this
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            in the format
            ``projects/*/locations/*/caPools/*/certificates/*``.
        pem_csr (str):
            Immutable. A pem-encoded X.509 certificate
            signing request (CSR).

            This field is a member of `oneof`_ ``certificate_config``.
        config (google.cloud.security.privateca_v1.types.CertificateConfig):
            Immutable. A description of the certificate
            and key that does not require X.509 or ASN.1.

            This field is a member of `oneof`_ ``certificate_config``.
        issuer_certificate_authority (str):
            Output only. The resource name of the issuing
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.
        lifetime (google.protobuf.duration_pb2.Duration):
            Required. Immutable. The desired lifetime of a certificate.
            Used to create the "not_before_time" and "not_after_time"
            fields inside an X.509 certificate. Note that the lifetime
            may be truncated if it would extend past the life of any
            certificate authority in the issuing chain.
        certificate_template (str):
            Immutable. The resource name for a
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
            used to issue this certificate, in the format
            ``projects/*/locations/*/certificateTemplates/*``. If this
            is specified, the caller must have the necessary permission
            to use this template. If this is omitted, no template will
            be used. This template must be in the same location as the
            [Certificate][google.cloud.security.privateca.v1.Certificate].
        subject_mode (google.cloud.security.privateca_v1.types.SubjectRequestMode):
            Immutable. Specifies how the
            [Certificate][google.cloud.security.privateca.v1.Certificate]'s
            identity fields are to be decided. If this is omitted, the
            ``DEFAULT`` subject mode will be used.
        revocation_details (google.cloud.security.privateca_v1.types.Certificate.RevocationDetails):
            Output only. Details regarding the revocation of this
            [Certificate][google.cloud.security.privateca.v1.Certificate].
            This
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            is considered revoked if and only if this field is present.
        pem_certificate (str):
            Output only. The pem-encoded, signed X.509
            certificate.
        certificate_description (google.cloud.security.privateca_v1.types.CertificateDescription):
            Output only. A structured description of the
            issued X.509 certificate.
        pem_certificate_chain (MutableSequence[str]):
            Output only. The chain that may be used to
            verify the X.509 certificate. Expected to be in
            issuer-to-root order according to RFC 5246.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Labels with user-defined metadata.
        requested_not_before_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The requested
            [not_before_time][google.cloud.security.privateca.v1.CertificateDescription.SubjectDescription.not_before_time]
            of this
            [Certificate][google.cloud.security.privateca.v1.Certificate].
            This field may only be set if the
            [CaPool.IssuancePolicy.allow_requester_specified_not_before_time][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.allow_requester_specified_not_before_time]
            field is set to true for the issuing
            [CaPool][google.cloud.security.privateca.v1.CaPool].

            If this field is specified, the certificate will be issued
            with this 'not_before_time'. If this is not specified, the
            'not_before_time' will be set to the issuance time or
            issuance time minus
            [backdate_duration][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.backdate_duration]
            depending on the
            [CaPool][google.cloud.security.privateca.v1.CaPool]
            configuration.
    """

    class RevocationDetails(proto.Message):
        r"""Describes fields that are relavent to the revocation of a
        [Certificate][google.cloud.security.privateca.v1.Certificate].

        Attributes:
            revocation_state (google.cloud.security.privateca_v1.types.RevocationReason):
                Indicates why a
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                was revoked.
            revocation_time (google.protobuf.timestamp_pb2.Timestamp):
                The time at which this
                [Certificate][google.cloud.security.privateca.v1.Certificate]
                was revoked.
        """

        revocation_state: "RevocationReason" = proto.Field(
            proto.ENUM,
            number=1,
            enum="RevocationReason",
        )
        revocation_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pem_csr: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="certificate_config",
    )
    config: "CertificateConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="certificate_config",
        message="CertificateConfig",
    )
    issuer_certificate_authority: str = proto.Field(
        proto.STRING,
        number=4,
    )
    lifetime: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    certificate_template: str = proto.Field(
        proto.STRING,
        number=6,
    )
    subject_mode: "SubjectRequestMode" = proto.Field(
        proto.ENUM,
        number=7,
        enum="SubjectRequestMode",
    )
    revocation_details: RevocationDetails = proto.Field(
        proto.MESSAGE,
        number=8,
        message=RevocationDetails,
    )
    pem_certificate: str = proto.Field(
        proto.STRING,
        number=9,
    )
    certificate_description: "CertificateDescription" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="CertificateDescription",
    )
    pem_certificate_chain: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )
    requested_not_before_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )


class CertificateTemplate(proto.Message):
    r"""A
    [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
    refers to a managed template for certificate issuance.

    Attributes:
        name (str):
            Identifier. The resource name for this
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
            in the format
            ``projects/*/locations/*/certificateTemplates/*``.
        maximum_lifetime (google.protobuf.duration_pb2.Duration):
            Optional. The maximum lifetime allowed for issued
            [Certificates][google.cloud.security.privateca.v1.Certificate]
            that use this template. If the issuing
            [CaPool][google.cloud.security.privateca.v1.CaPool]
            resource's
            [IssuancePolicy][google.cloud.security.privateca.v1.CaPool.IssuancePolicy]
            specifies a
            [maximum_lifetime][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.maximum_lifetime]
            the minimum of the two durations will be the maximum
            lifetime for issued
            [Certificates][google.cloud.security.privateca.v1.Certificate].
            Note that if the issuing
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            expires before a
            [Certificate][google.cloud.security.privateca.v1.Certificate]'s
            requested maximum_lifetime, the effective lifetime will be
            explicitly truncated to match it.
        predefined_values (google.cloud.security.privateca_v1.types.X509Parameters):
            Optional. A set of X.509 values that will be applied to all
            issued certificates that use this template. If the
            certificate request includes conflicting values for the same
            properties, they will be overwritten by the values defined
            here. If the issuing
            [CaPool][google.cloud.security.privateca.v1.CaPool]'s
            [IssuancePolicy][google.cloud.security.privateca.v1.CaPool.IssuancePolicy]
            defines conflicting
            [baseline_values][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.baseline_values]
            for the same properties, the certificate issuance request
            will fail.
        identity_constraints (google.cloud.security.privateca_v1.types.CertificateIdentityConstraints):
            Optional. Describes constraints on identities that may be
            appear in
            [Certificates][google.cloud.security.privateca.v1.Certificate]
            issued using this template. If this is omitted, then this
            template will not add restrictions on a certificate's
            identity.
        passthrough_extensions (google.cloud.security.privateca_v1.types.CertificateExtensionConstraints):
            Optional. Describes the set of X.509 extensions that may
            appear in a
            [Certificate][google.cloud.security.privateca.v1.Certificate]
            issued using this
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].
            If a certificate request sets extensions that don't appear
            in the
            [passthrough_extensions][google.cloud.security.privateca.v1.CertificateTemplate.passthrough_extensions],
            those extensions will be dropped. If the issuing
            [CaPool][google.cloud.security.privateca.v1.CaPool]'s
            [IssuancePolicy][google.cloud.security.privateca.v1.CaPool.IssuancePolicy]
            defines
            [baseline_values][google.cloud.security.privateca.v1.CaPool.IssuancePolicy.baseline_values]
            that don't appear here, the certificate issuance request
            will fail. If this is omitted, then this template will not
            add restrictions on a certificate's X.509 extensions. These
            constraints do not apply to X.509 extensions set in this
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]'s
            [predefined_values][google.cloud.security.privateca.v1.CertificateTemplate.predefined_values].
        description (str):
            Optional. A human-readable description of
            scenarios this template is intended for.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Labels with user-defined metadata.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    maximum_lifetime: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=9,
        message=duration_pb2.Duration,
    )
    predefined_values: "X509Parameters" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="X509Parameters",
    )
    identity_constraints: "CertificateIdentityConstraints" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CertificateIdentityConstraints",
    )
    passthrough_extensions: "CertificateExtensionConstraints" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CertificateExtensionConstraints",
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )


class X509Parameters(proto.Message):
    r"""An
    [X509Parameters][google.cloud.security.privateca.v1.X509Parameters]
    is used to describe certain fields of an X.509 certificate, such as
    the key usage fields, fields specific to CA certificates,
    certificate policy extensions and custom extensions.

    Attributes:
        key_usage (google.cloud.security.privateca_v1.types.KeyUsage):
            Optional. Indicates the intended use for keys
            that correspond to a certificate.
        ca_options (google.cloud.security.privateca_v1.types.X509Parameters.CaOptions):
            Optional. Describes options in this
            [X509Parameters][google.cloud.security.privateca.v1.X509Parameters]
            that are relevant in a CA certificate. If not specified, a
            default basic constraints extension with ``is_ca=false``
            will be added for leaf certificates.
        policy_ids (MutableSequence[google.cloud.security.privateca_v1.types.ObjectId]):
            Optional. Describes the X.509 certificate
            policy object identifiers, per
            https://tools.ietf.org/html/rfc5280#section-4.2.1.4.
        aia_ocsp_servers (MutableSequence[str]):
            Optional. Describes Online Certificate Status
            Protocol (OCSP) endpoint addresses that appear
            in the "Authority Information Access" extension
            in the certificate.
        name_constraints (google.cloud.security.privateca_v1.types.X509Parameters.NameConstraints):
            Optional. Describes the X.509 name
            constraints extension.
        additional_extensions (MutableSequence[google.cloud.security.privateca_v1.types.X509Extension]):
            Optional. Describes custom X.509 extensions.
    """

    class CaOptions(proto.Message):
        r"""Describes the X.509 basic constraints extension, per `RFC 5280
        section
        4.2.1.9 <https://tools.ietf.org/html/rfc5280#section-4.2.1.9>`__


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            is_ca (bool):
                Optional. Refers to the "CA" boolean field in
                the X.509 extension. When this value is missing,
                the basic constraints extension will be omitted
                from the certificate.

                This field is a member of `oneof`_ ``_is_ca``.
            max_issuer_path_length (int):
                Optional. Refers to the path length
                constraint field in the X.509 extension. For a
                CA certificate, this value describes the depth
                of subordinate CA certificates that are allowed.
                If this value is less than 0, the request will
                fail. If this value is missing, the max path
                length will be omitted from the certificate.

                This field is a member of `oneof`_ ``_max_issuer_path_length``.
        """

        is_ca: bool = proto.Field(
            proto.BOOL,
            number=1,
            optional=True,
        )
        max_issuer_path_length: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )

    class NameConstraints(proto.Message):
        r"""Describes the X.509 name constraints extension, per
        https://tools.ietf.org/html/rfc5280#section-4.2.1.10

        Attributes:
            critical (bool):
                Indicates whether or not the name constraints
                are marked critical.
            permitted_dns_names (MutableSequence[str]):
                Contains permitted DNS names. Any DNS name that can be
                constructed by simply adding zero or more labels to the
                left-hand side of the name satisfies the name constraint.
                For example, ``example.com``, ``www.example.com``,
                ``www.sub.example.com`` would satisfy ``example.com`` while
                ``example1.com`` does not.
            excluded_dns_names (MutableSequence[str]):
                Contains excluded DNS names. Any DNS name that can be
                constructed by simply adding zero or more labels to the
                left-hand side of the name satisfies the name constraint.
                For example, ``example.com``, ``www.example.com``,
                ``www.sub.example.com`` would satisfy ``example.com`` while
                ``example1.com`` does not.
            permitted_ip_ranges (MutableSequence[str]):
                Contains the permitted IP ranges. For IPv4
                addresses, the ranges are expressed using CIDR
                notation as specified in RFC 4632. For IPv6
                addresses, the ranges are expressed in similar
                encoding as IPv4 addresses.
            excluded_ip_ranges (MutableSequence[str]):
                Contains the excluded IP ranges. For IPv4
                addresses, the ranges are expressed using CIDR
                notation as specified in RFC 4632. For IPv6
                addresses, the ranges are expressed in similar
                encoding as IPv4 addresses.
            permitted_email_addresses (MutableSequence[str]):
                Contains the permitted email addresses. The value can be a
                particular email address, a hostname to indicate all email
                addresses on that host or a domain with a leading period
                (e.g. ``.example.com``) to indicate all email addresses in
                that domain.
            excluded_email_addresses (MutableSequence[str]):
                Contains the excluded email addresses. The value can be a
                particular email address, a hostname to indicate all email
                addresses on that host or a domain with a leading period
                (e.g. ``.example.com``) to indicate all email addresses in
                that domain.
            permitted_uris (MutableSequence[str]):
                Contains the permitted URIs that apply to the host part of
                the name. The value can be a hostname or a domain with a
                leading period (like ``.example.com``)
            excluded_uris (MutableSequence[str]):
                Contains the excluded URIs that apply to the host part of
                the name. The value can be a hostname or a domain with a
                leading period (like ``.example.com``)
        """

        critical: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        permitted_dns_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        excluded_dns_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        permitted_ip_ranges: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        excluded_ip_ranges: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )
        permitted_email_addresses: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=6,
        )
        excluded_email_addresses: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=7,
        )
        permitted_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=8,
        )
        excluded_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=9,
        )

    key_usage: "KeyUsage" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="KeyUsage",
    )
    ca_options: CaOptions = proto.Field(
        proto.MESSAGE,
        number=2,
        message=CaOptions,
    )
    policy_ids: MutableSequence["ObjectId"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ObjectId",
    )
    aia_ocsp_servers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    name_constraints: NameConstraints = proto.Field(
        proto.MESSAGE,
        number=6,
        message=NameConstraints,
    )
    additional_extensions: MutableSequence["X509Extension"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="X509Extension",
    )


class SubordinateConfig(proto.Message):
    r"""Describes a subordinate CA's issuers. This is either a resource name
    to a known issuing
    [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority],
    or a PEM issuer certificate chain.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        certificate_authority (str):
            Required. This can refer to a
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            that was used to create a subordinate
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
            This field is used for information and usability purposes
            only. The resource name is in the format
            ``projects/*/locations/*/caPools/*/certificateAuthorities/*``.

            This field is a member of `oneof`_ ``subordinate_config``.
        pem_issuer_chain (google.cloud.security.privateca_v1.types.SubordinateConfig.SubordinateConfigChain):
            Required. Contains the PEM certificate chain for the issuers
            of this
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority],
            but not pem certificate for this CA itself.

            This field is a member of `oneof`_ ``subordinate_config``.
    """

    class SubordinateConfigChain(proto.Message):
        r"""This message describes a subordinate CA's issuer certificate
        chain. This wrapper exists for compatibility reasons.

        Attributes:
            pem_certificates (MutableSequence[str]):
                Required. Expected to be in leaf-to-root
                order according to RFC 5246.
        """

        pem_certificates: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    certificate_authority: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="subordinate_config",
    )
    pem_issuer_chain: SubordinateConfigChain = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="subordinate_config",
        message=SubordinateConfigChain,
    )


class PublicKey(proto.Message):
    r"""A [PublicKey][google.cloud.security.privateca.v1.PublicKey]
    describes a public key.

    Attributes:
        key (bytes):
            Required. A public key. The padding and encoding must match
            with the ``KeyFormat`` value specified for the ``format``
            field.
        format_ (google.cloud.security.privateca_v1.types.PublicKey.KeyFormat):
            Required. The format of the public key.
    """

    class KeyFormat(proto.Enum):
        r"""Types of public keys formats that are supported. Currently, only
        ``PEM`` format is supported.

        Values:
            KEY_FORMAT_UNSPECIFIED (0):
                Default unspecified value.
            PEM (1):
                The key is PEM-encoded as defined in `RFC
                7468 <https://tools.ietf.org/html/rfc7468>`__. It can be any
                of the following: a PEM-encoded PKCS#1/RFC 3447 RSAPublicKey
                structure, an RFC 5280
                `SubjectPublicKeyInfo <https://tools.ietf.org/html/rfc5280#section-4.1>`__
                or a PEM-encoded X.509 certificate signing request (CSR). If
                a
                `SubjectPublicKeyInfo <https://tools.ietf.org/html/rfc5280#section-4.1>`__
                is specified, it can contain a A PEM-encoded PKCS#1/RFC 3447
                RSAPublicKey or a NIST P-256/secp256r1/prime256v1 or P-384
                key. If a CSR is specified, it will used solely for the
                purpose of extracting the public key. When generated by the
                service, it will always be an RFC 5280
                `SubjectPublicKeyInfo <https://tools.ietf.org/html/rfc5280#section-4.1>`__
                structure containing an algorithm identifier and a key.
        """

        KEY_FORMAT_UNSPECIFIED = 0
        PEM = 1

    key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    format_: KeyFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=KeyFormat,
    )


class CertificateConfig(proto.Message):
    r"""A
    [CertificateConfig][google.cloud.security.privateca.v1.CertificateConfig]
    describes an X.509 certificate or CSR that is to be created, as an
    alternative to using ASN.1.

    Attributes:
        subject_config (google.cloud.security.privateca_v1.types.CertificateConfig.SubjectConfig):
            Required. Specifies some of the values in a
            certificate that are related to the subject.
        x509_config (google.cloud.security.privateca_v1.types.X509Parameters):
            Required. Describes how some of the technical
            X.509 fields in a certificate should be
            populated.
        public_key (google.cloud.security.privateca_v1.types.PublicKey):
            Optional. The public key that corresponds to this config.
            This is, for example, used when issuing
            [Certificates][google.cloud.security.privateca.v1.Certificate],
            but not when creating a self-signed
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            or
            [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
            CSR.
        subject_key_id (google.cloud.security.privateca_v1.types.CertificateConfig.KeyId):
            Optional. When specified this provides a
            custom SKI to be used in the certificate. This
            should only be used to maintain a SKI of an
            existing CA originally created outside CA
            service, which was not generated using method
            (1) described in RFC 5280 section 4.2.1.2.
    """

    class SubjectConfig(proto.Message):
        r"""These values are used to create the distinguished name and
        subject alternative name fields in an X.509 certificate.

        Attributes:
            subject (google.cloud.security.privateca_v1.types.Subject):
                Optional. Contains distinguished name fields
                such as the common name, location and
                organization.
            subject_alt_name (google.cloud.security.privateca_v1.types.SubjectAltNames):
                Optional. The subject alternative name
                fields.
        """

        subject: "Subject" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Subject",
        )
        subject_alt_name: "SubjectAltNames" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="SubjectAltNames",
        )

    class KeyId(proto.Message):
        r"""A KeyId identifies a specific public key, usually by hashing
        the public key.

        Attributes:
            key_id (str):
                Required. The value of this KeyId encoded in
                lowercase hexadecimal. This is most likely the
                160 bit SHA-1 hash of the public key.
        """

        key_id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    subject_config: SubjectConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SubjectConfig,
    )
    x509_config: "X509Parameters" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="X509Parameters",
    )
    public_key: "PublicKey" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PublicKey",
    )
    subject_key_id: KeyId = proto.Field(
        proto.MESSAGE,
        number=4,
        message=KeyId,
    )


class CertificateDescription(proto.Message):
    r"""A
    [CertificateDescription][google.cloud.security.privateca.v1.CertificateDescription]
    describes an X.509 certificate or CSR that has been issued, as an
    alternative to using ASN.1 / X.509.

    Attributes:
        subject_description (google.cloud.security.privateca_v1.types.CertificateDescription.SubjectDescription):
            Describes some of the values in a certificate
            that are related to the subject and lifetime.
        x509_description (google.cloud.security.privateca_v1.types.X509Parameters):
            Describes some of the technical X.509 fields
            in a certificate.
        public_key (google.cloud.security.privateca_v1.types.PublicKey):
            The public key that corresponds to an issued
            certificate.
        subject_key_id (google.cloud.security.privateca_v1.types.CertificateDescription.KeyId):
            Provides a means of identifiying certificates
            that contain a particular public key, per
            https://tools.ietf.org/html/rfc5280#section-4.2.1.2.
        authority_key_id (google.cloud.security.privateca_v1.types.CertificateDescription.KeyId):
            Identifies the subject_key_id of the parent certificate, per
            https://tools.ietf.org/html/rfc5280#section-4.2.1.1
        crl_distribution_points (MutableSequence[str]):
            Describes a list of locations to obtain CRL
            information, i.e. the DistributionPoint.fullName
            described by
            https://tools.ietf.org/html/rfc5280#section-4.2.1.13
        aia_issuing_certificate_urls (MutableSequence[str]):
            Describes lists of issuer CA certificate URLs
            that appear in the "Authority Information
            Access" extension in the certificate.
        cert_fingerprint (google.cloud.security.privateca_v1.types.CertificateDescription.CertificateFingerprint):
            The hash of the x.509 certificate.
        tbs_certificate_digest (str):
            The hash of the pre-signed certificate, which
            will be signed by the CA. Corresponds to the TBS
            Certificate in
            https://tools.ietf.org/html/rfc5280#section-4.1.2.
            The field will always be populated.
    """

    class SubjectDescription(proto.Message):
        r"""These values describe fields in an issued X.509 certificate
        such as the distinguished name, subject alternative names,
        serial number, and lifetime.

        Attributes:
            subject (google.cloud.security.privateca_v1.types.Subject):
                Contains distinguished name fields such as
                the common name, location and / organization.
            subject_alt_name (google.cloud.security.privateca_v1.types.SubjectAltNames):
                The subject alternative name fields.
            hex_serial_number (str):
                The serial number encoded in lowercase
                hexadecimal.
            lifetime (google.protobuf.duration_pb2.Duration):
                For convenience, the actual lifetime of an
                issued certificate.
            not_before_time (google.protobuf.timestamp_pb2.Timestamp):
                The time at which the certificate becomes
                valid.
            not_after_time (google.protobuf.timestamp_pb2.Timestamp):
                The time after which the certificate is expired. Per RFC
                5280, the validity period for a certificate is the period of
                time from not_before_time through not_after_time, inclusive.
                Corresponds to 'not_before_time' + 'lifetime' - 1 second.
        """

        subject: "Subject" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Subject",
        )
        subject_alt_name: "SubjectAltNames" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="SubjectAltNames",
        )
        hex_serial_number: str = proto.Field(
            proto.STRING,
            number=3,
        )
        lifetime: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        not_before_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )
        not_after_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )

    class KeyId(proto.Message):
        r"""A KeyId identifies a specific public key, usually by hashing
        the public key.

        Attributes:
            key_id (str):
                Optional. The value of this KeyId encoded in
                lowercase hexadecimal. This is most likely the
                160 bit SHA-1 hash of the public key.
        """

        key_id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class CertificateFingerprint(proto.Message):
        r"""A group of fingerprints for the x509 certificate.

        Attributes:
            sha256_hash (str):
                The SHA 256 hash, encoded in hexadecimal, of
                the DER x509 certificate.
        """

        sha256_hash: str = proto.Field(
            proto.STRING,
            number=1,
        )

    subject_description: SubjectDescription = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SubjectDescription,
    )
    x509_description: "X509Parameters" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="X509Parameters",
    )
    public_key: "PublicKey" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PublicKey",
    )
    subject_key_id: KeyId = proto.Field(
        proto.MESSAGE,
        number=4,
        message=KeyId,
    )
    authority_key_id: KeyId = proto.Field(
        proto.MESSAGE,
        number=5,
        message=KeyId,
    )
    crl_distribution_points: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    aia_issuing_certificate_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    cert_fingerprint: CertificateFingerprint = proto.Field(
        proto.MESSAGE,
        number=8,
        message=CertificateFingerprint,
    )
    tbs_certificate_digest: str = proto.Field(
        proto.STRING,
        number=9,
    )


class ObjectId(proto.Message):
    r"""An [ObjectId][google.cloud.security.privateca.v1.ObjectId] specifies
    an object identifier (OID). These provide context and describe types
    in ASN.1 messages.

    Attributes:
        object_id_path (MutableSequence[int]):
            Required. The parts of an OID path. The most
            significant parts of the path come first.
    """

    object_id_path: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )


class X509Extension(proto.Message):
    r"""An [X509Extension][google.cloud.security.privateca.v1.X509Extension]
    specifies an X.509 extension, which may be used in different parts
    of X.509 objects like certificates, CSRs, and CRLs.

    Attributes:
        object_id (google.cloud.security.privateca_v1.types.ObjectId):
            Required. The OID for this X.509 extension.
        critical (bool):
            Optional. Indicates whether or not this
            extension is critical (i.e., if the client does
            not know how to handle this extension, the
            client should consider this to be an error).
        value (bytes):
            Required. The value of this X.509 extension.
    """

    object_id: "ObjectId" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ObjectId",
    )
    critical: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    value: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )


class KeyUsage(proto.Message):
    r"""A [KeyUsage][google.cloud.security.privateca.v1.KeyUsage] describes
    key usage values that may appear in an X.509 certificate.

    Attributes:
        base_key_usage (google.cloud.security.privateca_v1.types.KeyUsage.KeyUsageOptions):
            Describes high-level ways in which a key may
            be used.
        extended_key_usage (google.cloud.security.privateca_v1.types.KeyUsage.ExtendedKeyUsageOptions):
            Detailed scenarios in which a key may be
            used.
        unknown_extended_key_usages (MutableSequence[google.cloud.security.privateca_v1.types.ObjectId]):
            Used to describe extended key usages that are not listed in
            the
            [KeyUsage.ExtendedKeyUsageOptions][google.cloud.security.privateca.v1.KeyUsage.ExtendedKeyUsageOptions]
            message.
    """

    class KeyUsageOptions(proto.Message):
        r"""[KeyUsage.KeyUsageOptions][google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions]
        corresponds to the key usage values described in
        https://tools.ietf.org/html/rfc5280#section-4.2.1.3.

        Attributes:
            digital_signature (bool):
                The key may be used for digital signatures.
            content_commitment (bool):
                The key may be used for cryptographic
                commitments. Note that this may also be referred
                to as "non-repudiation".
            key_encipherment (bool):
                The key may be used to encipher other keys.
            data_encipherment (bool):
                The key may be used to encipher data.
            key_agreement (bool):
                The key may be used in a key agreement
                protocol.
            cert_sign (bool):
                The key may be used to sign certificates.
            crl_sign (bool):
                The key may be used sign certificate
                revocation lists.
            encipher_only (bool):
                The key may be used to encipher only.
            decipher_only (bool):
                The key may be used to decipher only.
        """

        digital_signature: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        content_commitment: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        key_encipherment: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        data_encipherment: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        key_agreement: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        cert_sign: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        crl_sign: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        encipher_only: bool = proto.Field(
            proto.BOOL,
            number=8,
        )
        decipher_only: bool = proto.Field(
            proto.BOOL,
            number=9,
        )

    class ExtendedKeyUsageOptions(proto.Message):
        r"""[KeyUsage.ExtendedKeyUsageOptions][google.cloud.security.privateca.v1.KeyUsage.ExtendedKeyUsageOptions]
        has fields that correspond to certain common OIDs that could be
        specified as an extended key usage value.

        Attributes:
            server_auth (bool):
                Corresponds to OID 1.3.6.1.5.5.7.3.1.
                Officially described as "TLS WWW server
                authentication", though regularly used for
                non-WWW TLS.
            client_auth (bool):
                Corresponds to OID 1.3.6.1.5.5.7.3.2.
                Officially described as "TLS WWW client
                authentication", though regularly used for
                non-WWW TLS.
            code_signing (bool):
                Corresponds to OID 1.3.6.1.5.5.7.3.3.
                Officially described as "Signing of downloadable
                executable code client authentication".
            email_protection (bool):
                Corresponds to OID 1.3.6.1.5.5.7.3.4.
                Officially described as "Email protection".
            time_stamping (bool):
                Corresponds to OID 1.3.6.1.5.5.7.3.8.
                Officially described as "Binding the hash of an
                object to a time".
            ocsp_signing (bool):
                Corresponds to OID 1.3.6.1.5.5.7.3.9.
                Officially described as "Signing OCSP
                responses".
        """

        server_auth: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        client_auth: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        code_signing: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        email_protection: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        time_stamping: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        ocsp_signing: bool = proto.Field(
            proto.BOOL,
            number=6,
        )

    base_key_usage: KeyUsageOptions = proto.Field(
        proto.MESSAGE,
        number=1,
        message=KeyUsageOptions,
    )
    extended_key_usage: ExtendedKeyUsageOptions = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ExtendedKeyUsageOptions,
    )
    unknown_extended_key_usages: MutableSequence["ObjectId"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ObjectId",
    )


class AttributeTypeAndValue(proto.Message):
    r"""[AttributeTypeAndValue][google.cloud.security.privateca.v1.AttributeTypeAndValue]
    specifies an attribute type and value. It can use either a OID or
    enum value to specify the attribute type.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.cloud.security.privateca_v1.types.AttributeType):
            The attribute type of the attribute and value
            pair.

            This field is a member of `oneof`_ ``attribute_type``.
        object_id (google.cloud.security.privateca_v1.types.ObjectId):
            Object ID for an attribute type of an
            attribute and value pair.

            This field is a member of `oneof`_ ``attribute_type``.
        value (str):
            The value for the attribute type.
    """

    type_: "AttributeType" = proto.Field(
        proto.ENUM,
        number=1,
        oneof="attribute_type",
        enum="AttributeType",
    )
    object_id: "ObjectId" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="attribute_type",
        message="ObjectId",
    )
    value: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RelativeDistinguishedName(proto.Message):
    r"""[RelativeDistinguishedName][google.cloud.security.privateca.v1.RelativeDistinguishedName]
    specifies a relative distinguished name which will be used to build
    a distinguished name.

    Attributes:
        attributes (MutableSequence[google.cloud.security.privateca_v1.types.AttributeTypeAndValue]):
            Attributes describes the attribute value
            assertions in the RDN.
    """

    attributes: MutableSequence["AttributeTypeAndValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AttributeTypeAndValue",
    )


class Subject(proto.Message):
    r"""[Subject][google.cloud.security.privateca.v1.Subject] describes
    parts of a distinguished name that, in turn, describes the subject
    of the certificate.

    Attributes:
        common_name (str):
            The "common name" of the subject.
        country_code (str):
            The country code of the subject.
        organization (str):
            The organization of the subject.
        organizational_unit (str):
            The organizational_unit of the subject.
        locality (str):
            The locality or city of the subject.
        province (str):
            The province, territory, or regional state of
            the subject.
        street_address (str):
            The street address of the subject.
        postal_code (str):
            The postal code of the subject.
        rdn_sequence (MutableSequence[google.cloud.security.privateca_v1.types.RelativeDistinguishedName]):
            This field can be used in place of the named
            subject fields.
    """

    common_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    country_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    organization: str = proto.Field(
        proto.STRING,
        number=3,
    )
    organizational_unit: str = proto.Field(
        proto.STRING,
        number=4,
    )
    locality: str = proto.Field(
        proto.STRING,
        number=5,
    )
    province: str = proto.Field(
        proto.STRING,
        number=6,
    )
    street_address: str = proto.Field(
        proto.STRING,
        number=7,
    )
    postal_code: str = proto.Field(
        proto.STRING,
        number=8,
    )
    rdn_sequence: MutableSequence["RelativeDistinguishedName"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="RelativeDistinguishedName",
    )


class SubjectAltNames(proto.Message):
    r"""[SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames]
    corresponds to a more modern way of listing what the asserted
    identity is in a certificate (i.e., compared to the "common name" in
    the distinguished name).

    Attributes:
        dns_names (MutableSequence[str]):
            Contains only valid, fully-qualified host
            names.
        uris (MutableSequence[str]):
            Contains only valid RFC 3986 URIs.
        email_addresses (MutableSequence[str]):
            Contains only valid RFC 2822 E-mail
            addresses.
        ip_addresses (MutableSequence[str]):
            Contains only valid 32-bit IPv4 addresses or
            RFC 4291 IPv6 addresses.
        custom_sans (MutableSequence[google.cloud.security.privateca_v1.types.X509Extension]):
            Contains additional subject alternative name values. For
            each custom_san, the ``value`` field must contain an ASN.1
            encoded UTF8String.
    """

    dns_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    email_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    custom_sans: MutableSequence["X509Extension"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="X509Extension",
    )


class CertificateIdentityConstraints(proto.Message):
    r"""Describes constraints on a
    [Certificate][google.cloud.security.privateca.v1.Certificate]'s
    [Subject][google.cloud.security.privateca.v1.Subject] and
    [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cel_expression (google.type.expr_pb2.Expr):
            Optional. A CEL expression that may be used
            to validate the resolved X.509 Subject and/or
            Subject Alternative Name before a certificate is
            signed. To see the full allowed syntax and some
            examples, see
            https://cloud.google.com/certificate-authority-service/docs/using-cel
        allow_subject_passthrough (bool):
            Required. If this is true, the
            [Subject][google.cloud.security.privateca.v1.Subject] field
            may be copied from a certificate request into the signed
            certificate. Otherwise, the requested
            [Subject][google.cloud.security.privateca.v1.Subject] will
            be discarded.

            This field is a member of `oneof`_ ``_allow_subject_passthrough``.
        allow_subject_alt_names_passthrough (bool):
            Required. If this is true, the
            [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames]
            extension may be copied from a certificate request into the
            signed certificate. Otherwise, the requested
            [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames]
            will be discarded.

            This field is a member of `oneof`_ ``_allow_subject_alt_names_passthrough``.
    """

    cel_expression: expr_pb2.Expr = proto.Field(
        proto.MESSAGE,
        number=1,
        message=expr_pb2.Expr,
    )
    allow_subject_passthrough: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    allow_subject_alt_names_passthrough: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )


class CertificateExtensionConstraints(proto.Message):
    r"""Describes a set of X.509 extensions that may be part of some
    certificate issuance controls.

    Attributes:
        known_extensions (MutableSequence[google.cloud.security.privateca_v1.types.CertificateExtensionConstraints.KnownCertificateExtension]):
            Optional. A set of named X.509 extensions. Will be combined
            with
            [additional_extensions][google.cloud.security.privateca.v1.CertificateExtensionConstraints.additional_extensions]
            to determine the full set of X.509 extensions.
        additional_extensions (MutableSequence[google.cloud.security.privateca_v1.types.ObjectId]):
            Optional. A set of
            [ObjectIds][google.cloud.security.privateca.v1.ObjectId]
            identifying custom X.509 extensions. Will be combined with
            [known_extensions][google.cloud.security.privateca.v1.CertificateExtensionConstraints.known_extensions]
            to determine the full set of X.509 extensions.
    """

    class KnownCertificateExtension(proto.Enum):
        r"""Describes well-known X.509 extensions that can appear in a
        [Certificate][google.cloud.security.privateca.v1.Certificate], not
        including the
        [SubjectAltNames][google.cloud.security.privateca.v1.SubjectAltNames]
        extension.

        Values:
            KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED (0):
                Not specified.
            BASE_KEY_USAGE (1):
                Refers to a certificate's Key Usage extension, as described
                in `RFC 5280 section
                4.2.1.3 <https://tools.ietf.org/html/rfc5280#section-4.2.1.3>`__.
                This corresponds to the
                [KeyUsage.base_key_usage][google.cloud.security.privateca.v1.KeyUsage.base_key_usage]
                field.
            EXTENDED_KEY_USAGE (2):
                Refers to a certificate's Extended Key Usage extension, as
                described in `RFC 5280 section
                4.2.1.12 <https://tools.ietf.org/html/rfc5280#section-4.2.1.12>`__.
                This corresponds to the
                [KeyUsage.extended_key_usage][google.cloud.security.privateca.v1.KeyUsage.extended_key_usage]
                message.
            CA_OPTIONS (3):
                Refers to a certificate's Basic Constraints extension, as
                described in `RFC 5280 section
                4.2.1.9 <https://tools.ietf.org/html/rfc5280#section-4.2.1.9>`__.
                This corresponds to the
                [X509Parameters.ca_options][google.cloud.security.privateca.v1.X509Parameters.ca_options]
                field.
            POLICY_IDS (4):
                Refers to a certificate's Policy object identifiers, as
                described in `RFC 5280 section
                4.2.1.4 <https://tools.ietf.org/html/rfc5280#section-4.2.1.4>`__.
                This corresponds to the
                [X509Parameters.policy_ids][google.cloud.security.privateca.v1.X509Parameters.policy_ids]
                field.
            AIA_OCSP_SERVERS (5):
                Refers to OCSP servers in a certificate's Authority
                Information Access extension, as described in `RFC 5280
                section
                4.2.2.1 <https://tools.ietf.org/html/rfc5280#section-4.2.2.1>`__,
                This corresponds to the
                [X509Parameters.aia_ocsp_servers][google.cloud.security.privateca.v1.X509Parameters.aia_ocsp_servers]
                field.
            NAME_CONSTRAINTS (6):
                Refers to Name Constraints extension as described in `RFC
                5280 section
                4.2.1.10 <https://tools.ietf.org/html/rfc5280#section-4.2.1.10>`__
        """

        KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED = 0
        BASE_KEY_USAGE = 1
        EXTENDED_KEY_USAGE = 2
        CA_OPTIONS = 3
        POLICY_IDS = 4
        AIA_OCSP_SERVERS = 5
        NAME_CONSTRAINTS = 6

    known_extensions: MutableSequence[KnownCertificateExtension] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=KnownCertificateExtension,
    )
    additional_extensions: MutableSequence["ObjectId"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ObjectId",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
