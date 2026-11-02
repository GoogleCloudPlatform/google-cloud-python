# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.oslogin.v1",
    manifest={
        "OperatingSystemType",
        "PosixAccount",
        "SshPublicKey",
    },
)


class OperatingSystemType(proto.Enum):
    r"""The operating system options for account entries."""

    OPERATING_SYSTEM_TYPE_UNSPECIFIED = 0
    LINUX = 1
    WINDOWS = 2


class PosixAccount(proto.Message):
    r"""The POSIX account information associated with a Google
    account.

    Attributes:
        primary (bool):
            Only one POSIX account can be marked as
            primary.
        username (str):
            The username of the POSIX account.
        uid (int):
            The user ID.
        gid (int):
            The default group ID.
        home_directory (str):
            The path to the home directory for this
            account.
        shell (str):
            The path to the logic shell for this account.
        gecos (str):
            The GECOS (user information) entry for this
            account.
        system_id (str):
            System identifier for which account the
            username or uid applies to. By default, the
            empty value is used.
        account_id (str):
            Output only. A POSIX account identifier.
        operating_system_type (google.cloud.oslogin.v1.types.OperatingSystemType):
            The operating system type where this account
            applies.
        name (str):
            Output only. The canonical resource name.
    """

    primary = proto.Field(
        proto.BOOL,
        number=1,
    )
    username = proto.Field(
        proto.STRING,
        number=2,
    )
    uid = proto.Field(
        proto.INT64,
        number=3,
    )
    gid = proto.Field(
        proto.INT64,
        number=4,
    )
    home_directory = proto.Field(
        proto.STRING,
        number=5,
    )
    shell = proto.Field(
        proto.STRING,
        number=6,
    )
    gecos = proto.Field(
        proto.STRING,
        number=7,
    )
    system_id = proto.Field(
        proto.STRING,
        number=8,
    )
    account_id = proto.Field(
        proto.STRING,
        number=9,
    )
    operating_system_type = proto.Field(
        proto.ENUM,
        number=10,
        enum="OperatingSystemType",
    )
    name = proto.Field(
        proto.STRING,
        number=11,
    )


class SshPublicKey(proto.Message):
    r"""The SSH public key information associated with a Google
    account.

    Attributes:
        key (str):
            Public key text in SSH format, defined by RFC4253 section
            6.6.
        expiration_time_usec (int):
            An expiration time in microseconds since
            epoch.
        fingerprint (str):
            Output only. The SHA-256 fingerprint of the
            SSH public key.
        name (str):
            Output only. The canonical resource name.
    """

    key = proto.Field(
        proto.STRING,
        number=1,
    )
    expiration_time_usec = proto.Field(
        proto.INT64,
        number=2,
    )
    fingerprint = proto.Field(
        proto.STRING,
        number=3,
    )
    name = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
