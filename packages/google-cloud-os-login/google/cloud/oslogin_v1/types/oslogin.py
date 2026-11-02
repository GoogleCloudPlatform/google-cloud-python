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

from google.cloud.oslogin_v1.common.types import common

__protobuf__ = proto.module(
    package="google.cloud.oslogin.v1",
    manifest={
        "LoginProfile",
        "CreateSshPublicKeyRequest",
        "DeletePosixAccountRequest",
        "DeleteSshPublicKeyRequest",
        "GetLoginProfileRequest",
        "GetSshPublicKeyRequest",
        "ImportSshPublicKeyRequest",
        "ImportSshPublicKeyResponse",
        "UpdateSshPublicKeyRequest",
    },
)


class LoginProfile(proto.Message):
    r"""The user profile information used for logging in to a virtual
    machine on Google Compute Engine.

    Attributes:
        name (str):
            Required. A unique user ID.
        posix_accounts (MutableSequence[google.cloud.oslogin_v1.common.types.PosixAccount]):
            The list of POSIX accounts associated with
            the user.
        ssh_public_keys (MutableMapping[str, google.cloud.oslogin_v1.common.types.SshPublicKey]):
            A map from SSH public key fingerprint to the
            associated key object.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    posix_accounts: MutableSequence[common.PosixAccount] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=common.PosixAccount,
    )
    ssh_public_keys: MutableMapping[str, common.SshPublicKey] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message=common.SshPublicKey,
    )


class CreateSshPublicKeyRequest(proto.Message):
    r"""A request message for creating an SSH public key.

    Attributes:
        parent (str):
            Required. The unique ID for the user in format
            ``users/{user}``.
        ssh_public_key (google.cloud.oslogin_v1.common.types.SshPublicKey):
            Required. The SSH public key and expiration
            time.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ssh_public_key: common.SshPublicKey = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.SshPublicKey,
    )


class DeletePosixAccountRequest(proto.Message):
    r"""A request message for deleting a POSIX account entry.

    Attributes:
        name (str):
            Required. A reference to the POSIX account to update. POSIX
            accounts are identified by the project ID they are
            associated with. A reference to the POSIX account is in
            format ``users/{user}/projects/{project}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteSshPublicKeyRequest(proto.Message):
    r"""A request message for deleting an SSH public key.

    Attributes:
        name (str):
            Required. The fingerprint of the public key to update.
            Public keys are identified by their SHA-256 fingerprint. The
            fingerprint of the public key is in format
            ``users/{user}/sshPublicKeys/{fingerprint}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetLoginProfileRequest(proto.Message):
    r"""A request message for retrieving the login profile
    information for a user.

    Attributes:
        name (str):
            Required. The unique ID for the user in format
            ``users/{user}``.
        project_id (str):
            The project ID of the Google Cloud Platform
            project.
        system_id (str):
            A system ID for filtering the results of the
            request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    system_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetSshPublicKeyRequest(proto.Message):
    r"""A request message for retrieving an SSH public key.

    Attributes:
        name (str):
            Required. The fingerprint of the public key to retrieve.
            Public keys are identified by their SHA-256 fingerprint. The
            fingerprint of the public key is in format
            ``users/{user}/sshPublicKeys/{fingerprint}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportSshPublicKeyRequest(proto.Message):
    r"""A request message for importing an SSH public key.

    Attributes:
        parent (str):
            Required. The unique ID for the user in format
            ``users/{user}``.
        ssh_public_key (google.cloud.oslogin_v1.common.types.SshPublicKey):
            Optional. The SSH public key and expiration
            time.
        project_id (str):
            The project ID of the Google Cloud Platform
            project.
        regions (MutableSequence[str]):
            Optional. The regions to which to assert that
            the key was written. If unspecified, defaults to
            all regions. Regions are listed at
            https://cloud.google.com/about/locations#region.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ssh_public_key: common.SshPublicKey = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.SshPublicKey,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class ImportSshPublicKeyResponse(proto.Message):
    r"""A response message for importing an SSH public key.

    Attributes:
        login_profile (google.cloud.oslogin_v1.types.LoginProfile):
            The login profile information for the user.
        details (str):
            Detailed information about import results.
    """

    login_profile: "LoginProfile" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="LoginProfile",
    )
    details: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateSshPublicKeyRequest(proto.Message):
    r"""A request message for updating an SSH public key.

    Attributes:
        name (str):
            Required. The fingerprint of the public key to update.
            Public keys are identified by their SHA-256 fingerprint. The
            fingerprint of the public key is in format
            ``users/{user}/sshPublicKeys/{fingerprint}``.
        ssh_public_key (google.cloud.oslogin_v1.common.types.SshPublicKey):
            Required. The SSH public key and expiration
            time.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask to control which fields get updated.
            Updates all if not present.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ssh_public_key: common.SshPublicKey = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.SshPublicKey,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
