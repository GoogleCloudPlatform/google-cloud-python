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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.kms.v1",
    manifest={
        "UpdateAutokeyConfigRequest",
        "GetAutokeyConfigRequest",
        "AutokeyConfig",
        "ShowEffectiveAutokeyConfigRequest",
        "ShowEffectiveAutokeyConfigResponse",
    },
)


class UpdateAutokeyConfigRequest(proto.Message):
    r"""Request message for
    [UpdateAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig].

    Attributes:
        autokey_config (google.cloud.kms_v1.types.AutokeyConfig):
            Required. [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig]
            with values to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Masks which fields of the
            [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] to
            update, e.g. ``keyProject``.
    """

    autokey_config: "AutokeyConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AutokeyConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetAutokeyConfigRequest(proto.Message):
    r"""Request message for
    [GetAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.GetAutokeyConfig].

    Attributes:
        name (str):
            Required. Name of the
            [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] resource,
            e.g. ``folders/{FOLDER_NUMBER}/autokeyConfig`` or
            ``projects/{PROJECT_NUMBER}/autokeyConfig``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AutokeyConfig(proto.Message):
    r"""Cloud KMS Autokey configuration for a folder.

    Attributes:
        name (str):
            Identifier. Name of the
            [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] resource,
            e.g. ``folders/{FOLDER_NUMBER}/autokeyConfig`` or
            ``projects/{PROJECT_NUMBER}/autokeyConfig``.
        key_project (str):
            Optional. Name of the key project, e.g.
            ``projects/{PROJECT_ID}`` or ``projects/{PROJECT_NUMBER}``,
            where Cloud KMS Autokey will provision a new
            [CryptoKey][google.cloud.kms.v1.CryptoKey] when a
            [KeyHandle][google.cloud.kms.v1.KeyHandle] is created. On
            [UpdateAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig],
            the caller will require ``cloudkms.cryptoKeys.setIamPolicy``
            permission on this key project. Once configured, for Cloud
            KMS Autokey to function properly, this key project must have
            the Cloud KMS API activated and the Cloud KMS Service Agent
            for this key project must be granted the ``cloudkms.admin``
            role (or pertinent permissions). A request with an empty key
            project field will clear the configuration.
        state (google.cloud.kms_v1.types.AutokeyConfig.State):
            Output only. The state for the AutokeyConfig.
        etag (str):
            Optional. A checksum computed by the server
            based on the value of other fields. This may be
            sent on update requests to ensure that the
            client has an up-to-date value before
            proceeding. The request will be rejected with an
            ABORTED error on a mismatched etag.
        key_project_resolution_mode (google.cloud.kms_v1.types.AutokeyConfig.KeyProjectResolutionMode):
            Optional. KeyProjectResolutionMode for the AutokeyConfig.
            Valid values are ``DEDICATED_KEY_PROJECT``,
            ``RESOURCE_PROJECT``, or ``DISABLED``.
    """

    class State(proto.Enum):
        r"""The states AutokeyConfig can be in.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the AutokeyConfig is
                unspecified.
            ACTIVE (1):
                The AutokeyConfig is currently active.
            KEY_PROJECT_DELETED (2):
                A previously configured key project has been
                deleted and the current AutokeyConfig is
                unusable.
            UNINITIALIZED (3):
                The AutokeyConfig is not yet initialized or
                has been reset to its default uninitialized
                state.
            KEY_PROJECT_PERMISSION_DENIED (4):
                The service account lacks the necessary
                permissions in the key project to configure
                Autokey.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        KEY_PROJECT_DELETED = 2
        UNINITIALIZED = 3
        KEY_PROJECT_PERMISSION_DENIED = 4

    class KeyProjectResolutionMode(proto.Enum):
        r"""Defines the resolution mode enum for the key project. The
        [KeyProjectResolutionMode][google.cloud.kms.v1.AutokeyConfig.KeyProjectResolutionMode]
        determines the mechanism by which
        [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] identifies a
        [key_project][google.cloud.kms.v1.AutokeyConfig.key_project] at its
        specific configuration node. This parameter also determines if
        Autokey can be used within this project or folder.

        Values:
            KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED (0):
                Default value. KeyProjectResolutionMode when not specified
                will act as ``DEDICATED_KEY_PROJECT``.
            DEDICATED_KEY_PROJECT (1):
                Keys are created in a dedicated project specified by
                ``key_project``.
            RESOURCE_PROJECT (2):
                Keys are created in the same project as the resource
                requesting the key. The ``key_project`` must not be set when
                this mode is used.
            DISABLED (3):
                Disables the AutokeyConfig. When this mode is set, any
                AutokeyConfig from higher levels in the resource hierarchy
                are ignored for this resource and its descendants. This
                setting can be overridden by a more specific configuration
                at a lower level. For example, if Autokey is disabled on a
                folder, it can be re-enabled on a sub-folder or project
                within that folder by setting a different mode (e.g.,
                DEDICATED_KEY_PROJECT or RESOURCE_PROJECT).
        """

        KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED = 0
        DEDICATED_KEY_PROJECT = 1
        RESOURCE_PROJECT = 2
        DISABLED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    key_project_resolution_mode: KeyProjectResolutionMode = proto.Field(
        proto.ENUM,
        number=8,
        enum=KeyProjectResolutionMode,
    )


class ShowEffectiveAutokeyConfigRequest(proto.Message):
    r"""Request message for
    [ShowEffectiveAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig].

    Attributes:
        parent (str):
            Required. Name of the resource project to the
            show effective Cloud KMS Autokey configuration
            for. This may be helpful for interrogating the
            effect of nested folder configurations on a
            given resource project.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ShowEffectiveAutokeyConfigResponse(proto.Message):
    r"""Response message for
    [ShowEffectiveAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig].

    Attributes:
        key_project (str):
            Name of the key project configured in the
            resource project's folder ancestry.
    """

    key_project: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
