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
    package="google.cloud.netapp.v1",
    manifest={
        "ListActiveDirectoriesRequest",
        "ListActiveDirectoriesResponse",
        "GetActiveDirectoryRequest",
        "CreateActiveDirectoryRequest",
        "UpdateActiveDirectoryRequest",
        "DeleteActiveDirectoryRequest",
        "ActiveDirectory",
    },
)


class ListActiveDirectoriesRequest(proto.Message):
    r"""ListActiveDirectoriesRequest for requesting multiple active
    directories.

    Attributes:
        parent (str):
            Required. Parent value for
            ListActiveDirectoriesRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, the server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListActiveDirectoriesResponse(proto.Message):
    r"""ListActiveDirectoriesResponse contains all the active
    directories requested.

    Attributes:
        active_directories (MutableSequence[google.cloud.netapp_v1.types.ActiveDirectory]):
            The list of active directories.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    active_directories: MutableSequence["ActiveDirectory"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ActiveDirectory",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetActiveDirectoryRequest(proto.Message):
    r"""GetActiveDirectory for getting a single active directory.

    Attributes:
        name (str):
            Required. Name of the active directory.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateActiveDirectoryRequest(proto.Message):
    r"""CreateActiveDirectoryRequest for creating an active
    directory.

    Attributes:
        parent (str):
            Required. Value for parent.
        active_directory (google.cloud.netapp_v1.types.ActiveDirectory):
            Required. Fields of the to be created active
            directory.
        active_directory_id (str):
            Required. ID of the active directory to
            create. Must be unique within the parent
            resource. Must contain only letters, numbers and
            hyphen, with the first character a letter , the
            last a letter or a number, and a 63 character
            maximum.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    active_directory: "ActiveDirectory" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ActiveDirectory",
    )
    active_directory_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateActiveDirectoryRequest(proto.Message):
    r"""UpdateActiveDirectoryRequest for updating an active
    directory.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Active Directory resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        active_directory (google.cloud.netapp_v1.types.ActiveDirectory):
            Required. The volume being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    active_directory: "ActiveDirectory" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ActiveDirectory",
    )


class DeleteActiveDirectoryRequest(proto.Message):
    r"""DeleteActiveDirectoryRequest for deleting a single active
    directory.

    Attributes:
        name (str):
            Required. Name of the active directory.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ActiveDirectory(proto.Message):
    r"""ActiveDirectory is the public representation of the active
    directory config.

    Attributes:
        name (str):
            Identifier. The resource name of the active directory.
            Format:
            ``projects/{project_number}/locations/{location_id}/activeDirectories/{active_directory_id}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the active
            directory.
        state (google.cloud.netapp_v1.types.ActiveDirectory.State):
            Output only. The state of the AD.
        domain (str):
            Required. Name of the Active Directory domain
        site (str):
            The Active Directory site the service will
            limit Domain Controller discovery too.
        dns (str):
            Required. Comma separated list of DNS server
            IP addresses for the Active Directory domain.
        net_bios_prefix (str):
            Required. NetBIOSPrefix is used as a prefix
            for SMB server name.
        organizational_unit (str):
            The Organizational Unit (OU) within the
            Windows Active Directory the user belongs to.
        aes_encryption (bool):
            If enabled, AES encryption will be enabled
            for SMB communication.
        username (str):
            Required. Username of the Active Directory
            domain administrator.
        password (str):
            Required. Password of the Active Directory
            domain administrator.
        backup_operators (MutableSequence[str]):
            Optional. Users to be added to the Built-in
            Backup Operator active directory group.
        administrators (MutableSequence[str]):
            Optional. Users to be added to the Built-in
            Admininstrators group.
        security_operators (MutableSequence[str]):
            Optional. Domain users to be given the
            SeSecurityPrivilege.
        kdc_hostname (str):
            Name of the active directory machine. This
            optional parameter is used only while creating
            kerberos volume
        kdc_ip (str):
            KDC server IP address for the active
            directory machine.
        nfs_users_with_ldap (bool):
            If enabled, will allow access to local users
            and LDAP users. If access is needed for only
            LDAP users, it has to be disabled.
        description (str):
            Description of the active directory.
        ldap_signing (bool):
            Specifies whether or not the LDAP traffic
            needs to be signed.
        encrypt_dc_connections (bool):
            If enabled, traffic between the SMB server to
            Domain Controller (DC) will be encrypted.
        labels (MutableMapping[str, str]):
            Labels for the active directory.
        state_details (str):
            Output only. The state details of the Active
            Directory.
    """

    class State(proto.Enum):
        r"""The Active Directory States

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified Active Directory State
            CREATING (1):
                Active Directory State is Creating
            READY (2):
                Active Directory State is Ready
            UPDATING (3):
                Active Directory State is Updating
            IN_USE (4):
                Active Directory State is In use
            DELETING (5):
                Active Directory State is Deleting
            ERROR (6):
                Active Directory State is Error
            DIAGNOSING (7):
                Active Directory State is Diagnosing.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        UPDATING = 3
        IN_USE = 4
        DELETING = 5
        ERROR = 6
        DIAGNOSING = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=4,
    )
    site: str = proto.Field(
        proto.STRING,
        number=5,
    )
    dns: str = proto.Field(
        proto.STRING,
        number=6,
    )
    net_bios_prefix: str = proto.Field(
        proto.STRING,
        number=7,
    )
    organizational_unit: str = proto.Field(
        proto.STRING,
        number=8,
    )
    aes_encryption: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    username: str = proto.Field(
        proto.STRING,
        number=10,
    )
    password: str = proto.Field(
        proto.STRING,
        number=11,
    )
    backup_operators: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    administrators: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=22,
    )
    security_operators: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    kdc_hostname: str = proto.Field(
        proto.STRING,
        number=14,
    )
    kdc_ip: str = proto.Field(
        proto.STRING,
        number=15,
    )
    nfs_users_with_ldap: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    description: str = proto.Field(
        proto.STRING,
        number=17,
    )
    ldap_signing: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    encrypt_dc_connections: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=20,
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=21,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
