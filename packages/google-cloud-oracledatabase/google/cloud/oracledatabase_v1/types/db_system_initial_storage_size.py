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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "DbSystemInitialStorageSize",
        "DbSystemInitialStorageSizeProperties",
        "StorageSizeDetails",
        "ListDbSystemInitialStorageSizesRequest",
        "ListDbSystemInitialStorageSizesResponse",
    },
)


class DbSystemInitialStorageSize(proto.Message):
    r"""Summary of the DbSystem initial storage size.

    Attributes:
        name (str):
            Output only. The name of the resource.
        properties (google.cloud.oracledatabase_v1.types.DbSystemInitialStorageSizeProperties):
            Output only. The properties of the DbSystem
            initial storage size summary.
    """

    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    properties: "DbSystemInitialStorageSizeProperties" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DbSystemInitialStorageSizeProperties",
    )


class DbSystemInitialStorageSizeProperties(proto.Message):
    r"""The properties of a DbSystem initial storage size summary.

    Attributes:
        storage_management (google.cloud.oracledatabase_v1.types.DbSystemInitialStorageSizeProperties.StorageManagement):
            Output only. The storage option used in DB
            system.
        shape_type (google.cloud.oracledatabase_v1.types.DbSystemInitialStorageSizeProperties.ShapeType):
            Output only. VM shape platform type
        storage_size_details (MutableSequence[google.cloud.oracledatabase_v1.types.StorageSizeDetails]):
            Output only. List of storage disk details.
        launch_from_backup_storage_size_details (MutableSequence[google.cloud.oracledatabase_v1.types.StorageSizeDetails]):
            Output only. List of storage disk details
            available for launches from backup.
    """

    class StorageManagement(proto.Enum):
        r"""The storage option used in the DB system.

        Values:
            STORAGE_MANAGEMENT_UNSPECIFIED (0):
                Unspecified storage management.
            ASM (1):
                Automatic Storage Management.
            LVM (2):
                Logical Volume Management.
        """

        STORAGE_MANAGEMENT_UNSPECIFIED = 0
        ASM = 1
        LVM = 2

    class ShapeType(proto.Enum):
        r"""The shape type of the DB system.

        Values:
            SHAPE_TYPE_UNSPECIFIED (0):
                Unspecified shape type.
            STANDARD_X86 (1):
                Standard X86.
        """

        SHAPE_TYPE_UNSPECIFIED = 0
        STANDARD_X86 = 1

    storage_management: StorageManagement = proto.Field(
        proto.ENUM,
        number=1,
        enum=StorageManagement,
    )
    shape_type: ShapeType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ShapeType,
    )
    storage_size_details: MutableSequence["StorageSizeDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="StorageSizeDetails",
    )
    launch_from_backup_storage_size_details: MutableSequence["StorageSizeDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="StorageSizeDetails",
        )
    )


class StorageSizeDetails(proto.Message):
    r"""The initial storage size, in gigabytes, that is applicable
    for virtual machine DBSystem.

    Attributes:
        data_storage_size_in_gbs (int):
            Output only. The data storage size, in
            gigabytes, that is applicable for virtual
            machine DBSystem.
        reco_storage_size_in_gbs (int):
            Output only. The RECO/REDO storage size, in
            gigabytes, that is applicable for virtual
            machine DBSystem.
    """

    data_storage_size_in_gbs: int = proto.Field(
        proto.INT32,
        number=1,
    )
    reco_storage_size_in_gbs: int = proto.Field(
        proto.INT32,
        number=2,
    )


class ListDbSystemInitialStorageSizesRequest(proto.Message):
    r"""The request for ``DbSystemInitialStorageSizes.List``.

    Attributes:
        parent (str):
            Required. The parent value for the
            DbSystemInitialStorageSize resource with the
            format: projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, a maximum of 50
            DbSystemInitialStorageSizes will be returned.
            The maximum value is 1000; values above 1000
            will be reset to 1000.
        page_token (str):
            Optional. A token identifying the requested
            page of results to return. All fields except the
            filter should remain the same as in the request
            that provided this page token.
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


class ListDbSystemInitialStorageSizesResponse(proto.Message):
    r"""The response for ``DbSystemInitialStorageSizes.List``.

    Attributes:
        db_system_initial_storage_sizes (MutableSequence[google.cloud.oracledatabase_v1.types.DbSystemInitialStorageSize]):
            The list of DbSystemInitialStorageSizes.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    db_system_initial_storage_sizes: MutableSequence["DbSystemInitialStorageSize"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DbSystemInitialStorageSize",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
