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
    package="google.cloud.dialogflow.v2",
    manifest={
        "GetEncryptionSpecRequest",
        "EncryptionSpec",
        "InitializeEncryptionSpecRequest",
        "InitializeEncryptionSpecResponse",
        "InitializeEncryptionSpecMetadata",
    },
)


class GetEncryptionSpecRequest(proto.Message):
    r"""The request to get location-level encryption specification.

    Attributes:
        name (str):
            Required. The name of the encryption spec
            resource to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EncryptionSpec(proto.Message):
    r"""A customer-managed encryption key specification that can be
    applied to all created resources (e.g. Conversation).

    Attributes:
        name (str):
            Immutable. The resource name of the
            encryption key specification resource. Format:

            projects/{project}/locations/{location}/encryptionSpec
        kms_key (str):
            Required. The name of customer-managed encryption key that
            is used to secure a resource and its sub-resources. If
            empty, the resource is secured by the default Google
            encryption key. Only the key in the same location as this
            resource is allowed to be used for encryption. Format:
            ``projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{key}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class InitializeEncryptionSpecRequest(proto.Message):
    r"""The request to initialize a location-level encryption
    specification.

    Attributes:
        encryption_spec (google.cloud.dialogflow_v2.types.EncryptionSpec):
            Required. The encryption spec used for CMEK encryption. It
            is required that the kms key is in the same region as the
            endpoint. The same key will be used for all provisioned
            resources, if encryption is available. If the kms_key_name
            is left empty, no encryption will be enforced.
    """

    encryption_spec: "EncryptionSpec" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EncryptionSpec",
    )


class InitializeEncryptionSpecResponse(proto.Message):
    r"""The response to initialize a location-level encryption
    specification.

    """


class InitializeEncryptionSpecMetadata(proto.Message):
    r"""Metadata for initializing a location-level encryption
    specification.

    Attributes:
        request (google.cloud.dialogflow_v2.types.InitializeEncryptionSpecRequest):
            Output only. The original request for
            initialization.
    """

    request: "InitializeEncryptionSpecRequest" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="InitializeEncryptionSpecRequest",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
