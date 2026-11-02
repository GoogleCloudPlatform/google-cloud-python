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
    package="google.cloud.gkebackup.v1",
    manifest={
        "Namespaces",
        "NamespacedName",
        "NamespacedNames",
        "EncryptionKey",
        "VolumeTypeEnum",
    },
)


class Namespaces(proto.Message):
    r"""A list of Kubernetes Namespaces.

    Attributes:
        namespaces (MutableSequence[str]):
            Optional. A list of Kubernetes Namespaces.
    """

    namespaces: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class NamespacedName(proto.Message):
    r"""A reference to a namespaced resource in Kubernetes.

    Attributes:
        namespace (str):
            Optional. The Namespace of the Kubernetes
            resource.
        name (str):
            Optional. The name of the Kubernetes
            resource.
    """

    namespace: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class NamespacedNames(proto.Message):
    r"""A list of namespaced Kubernetes resources.

    Attributes:
        namespaced_names (MutableSequence[google.cloud.gke_backup_v1.types.NamespacedName]):
            Optional. A list of namespaced Kubernetes
            resources.
    """

    namespaced_names: MutableSequence["NamespacedName"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NamespacedName",
    )


class EncryptionKey(proto.Message):
    r"""Defined a customer managed encryption key that will be used
    to encrypt Backup artifacts.

    Attributes:
        gcp_kms_encryption_key (str):
            Optional. Google Cloud KMS encryption key. Format:
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``
    """

    gcp_kms_encryption_key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VolumeTypeEnum(proto.Message):
    r"""Message to encapsulate VolumeType enum."""

    class VolumeType(proto.Enum):
        r"""Supported volume types.

        Values:
            VOLUME_TYPE_UNSPECIFIED (0):
                Default
            GCE_PERSISTENT_DISK (1):
                Compute Engine Persistent Disk volume
        """

        VOLUME_TYPE_UNSPECIFIED = 0
        GCE_PERSISTENT_DISK = 1


__all__ = tuple(sorted(__protobuf__.manifest))
