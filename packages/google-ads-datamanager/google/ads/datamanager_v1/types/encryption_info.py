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
    package="google.ads.datamanager.v1",
    manifest={
        "EncryptionInfo",
        "GcpWrappedKeyInfo",
        "AwsWrappedKeyInfo",
        "CoordinatorKeyInfo",
    },
)


class EncryptionInfo(proto.Message):
    r"""Encryption information for the data being ingested.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcp_wrapped_key_info (google.ads.datamanager_v1.types.GcpWrappedKeyInfo):
            Google Cloud Platform wrapped key
            information.

            This field is a member of `oneof`_ ``wrapped_key``.
        aws_wrapped_key_info (google.ads.datamanager_v1.types.AwsWrappedKeyInfo):
            Amazon Web Services wrapped key information.

            This field is a member of `oneof`_ ``wrapped_key``.
        coordinator_key_info (google.ads.datamanager_v1.types.CoordinatorKeyInfo):
            Key information for the chosen coordinator key.

            This is not supported for the
            [IngestEvents][google.ads.datamanager.v1.IngestionService.IngestEvents],
            [IngestAudienceMembers][google.ads.datamanager.v1.IngestionService.IngestAudienceMembers],
            and
            [RemoveAudienceMembers][google.ads.datamanager.v1.IngestionService.RemoveAudienceMembers]
            methods.

            This field is a member of `oneof`_ ``wrapped_key``.
    """

    gcp_wrapped_key_info: "GcpWrappedKeyInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="wrapped_key",
        message="GcpWrappedKeyInfo",
    )
    aws_wrapped_key_info: "AwsWrappedKeyInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="wrapped_key",
        message="AwsWrappedKeyInfo",
    )
    coordinator_key_info: "CoordinatorKeyInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="wrapped_key",
        message="CoordinatorKeyInfo",
    )


class GcpWrappedKeyInfo(proto.Message):
    r"""Information about the Google Cloud Platform wrapped
    key.

    Attributes:
        key_type (google.ads.datamanager_v1.types.GcpWrappedKeyInfo.KeyType):
            Required. The type of algorithm used to
            encrypt the data.
        wip_provider (str):
            Required. The `Workload
            Identity <//cloud.google.com/iam/docs/workload-identity-federation>`__
            pool provider required to use KEK.
        kek_uri (str):
            Required. Google Cloud Platform `Cloud Key Management
            Service resource
            ID <//cloud.google.com/kms/docs/getting-resource-ids>`__.
            Should be in the format of
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key}``
            or
            ``gcp-kms://projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key}``
        encrypted_dek (str):
            Required. The base64 encoded encrypted data
            encryption key.
    """

    class KeyType(proto.Enum):
        r"""The type of algorithm used to encrypt the data.

        Values:
            KEY_TYPE_UNSPECIFIED (0):
                Unspecified key type. Should never be used.
            XCHACHA20_POLY1305 (1):
                Algorithm XChaCha20-Poly1305
        """

        KEY_TYPE_UNSPECIFIED = 0
        XCHACHA20_POLY1305 = 1

    key_type: KeyType = proto.Field(
        proto.ENUM,
        number=1,
        enum=KeyType,
    )
    wip_provider: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kek_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    encrypted_dek: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AwsWrappedKeyInfo(proto.Message):
    r"""A data encryption key wrapped by an AWS KMS key.

    Attributes:
        key_type (google.ads.datamanager_v1.types.AwsWrappedKeyInfo.KeyType):
            Required. The type of algorithm used to
            encrypt the data.
        role_arn (str):
            Required. The Amazon Resource Name of the IAM Role to assume
            for KMS decryption access. Should be in the format of
            ``arn:{partition}:iam::{account_id}:role/{role_name}``
        kek_uri (str):
            Required. The URI of the AWS KMS key used to decrypt the
            DEK. Should be in the format of
            ``arn:{partition}:kms:{region}:{account_id}:key/{key_id}``
            or
            ``aws-kms://arn:{partition}:kms:{region}:{account_id}:key/{key_id}``
        encrypted_dek (str):
            Required. The base64 encoded encrypted data
            encryption key.
    """

    class KeyType(proto.Enum):
        r"""The type of algorithm used to encrypt the data.

        Values:
            KEY_TYPE_UNSPECIFIED (0):
                Unspecified key type. Should never be used.
            XCHACHA20_POLY1305 (1):
                Algorithm XChaCha20-Poly1305
        """

        KEY_TYPE_UNSPECIFIED = 0
        XCHACHA20_POLY1305 = 1

    key_type: KeyType = proto.Field(
        proto.ENUM,
        number=1,
        enum=KeyType,
    )
    role_arn: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kek_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    encrypted_dek: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CoordinatorKeyInfo(proto.Message):
    r"""Information about the coordinator key.

    Attributes:
        key_id (str):
            Required. The ID of the chosen coordinator
            key.
    """

    key_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
