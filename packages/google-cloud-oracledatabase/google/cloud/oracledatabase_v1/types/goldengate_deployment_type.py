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
        "GoldengateDeploymentType",
        "ListGoldengateDeploymentTypesRequest",
        "ListGoldengateDeploymentTypesResponse",
    },
)


class GoldengateDeploymentType(proto.Message):
    r"""Details of the Goldengate Deployment Type resource.

    Attributes:
        name (str):
            Identifier. The name of the Goldengate Deployment Type
            resource with the format:
            projects/{project}/locations/{region}/goldengateDeploymentTypes/{goldengate_deployment_type}
        deployment_type (google.cloud.oracledatabase_v1.types.GoldengateDeploymentType.DeploymentType):
            Output only. The deployment type of the
            Goldengate Deployment Type resource.
        category (google.cloud.oracledatabase_v1.types.GoldengateDeploymentType.DeploymentCategory):
            Output only. The category of the Goldengate
            Deployment Type resource.
        connection_types (MutableSequence[str]):
            Output only. The connection types of the
            Goldengate Deployment Type resource.
        display_name (str):
            Output only. The display name of the
            Goldengate Deployment Type resource.
        ogg_version (str):
            Output only. The Ogg version of the
            Goldengate Deployment Type resource.
        source_technologies (MutableSequence[str]):
            Output only. The source technologies of the
            Goldengate Deployment Type resource.
        supported_capabilities (MutableSequence[str]):
            Output only. The supported capabilities of
            the Goldengate Deployment Type resource.
        supported_technologies_url (str):
            Output only. The supported technologies URL
            of the Goldengate Deployment Type resource.
        target_technologies (MutableSequence[str]):
            Output only. The target technologies of the
            Goldengate Deployment Type resource.
        default_username (str):
            Output only. The default username of the
            Goldengate Deployment Type resource.
    """

    class DeploymentType(proto.Enum):
        r"""The deployment type of the Goldengate Deployment Type
        resource.

        Values:
            DEPLOYMENT_TYPE_UNSPECIFIED (0):
                Default unspecified value.
            OGG (1):
                Goldengate Deployment Type category is OGG.
            DATABASE_ORACLE (2):
                Goldengate Deployment Type category is DATABASE_ORACLE.
            BIGDATA (3):
                Goldengate Deployment Type category is
                BIGDATA.
            DATABASE_MICROSOFT_SQLSERVER (4):
                Goldengate Deployment Type category is
                DATABASE_MICROSOFT_SQLSERVER.
            DATABASE_MYSQL (5):
                Goldengate Deployment Type category is DATABASE_MYSQL.
            DATABASE_POSTGRESQL (6):
                Goldengate Deployment Type category is DATABASE_POSTGRESQL.
            DATABASE_DB2ZOS (7):
                Goldengate Deployment Type category is DATABASE_DB2ZOS.
            DATABASE_DB2I (8):
                Goldengate Deployment Type category is DATABASE_DB2I.
            GGSA (9):
                Goldengate Deployment Type category is GGSA.
            DATA_TRANSFORMS (10):
                Goldengate Deployment Type category is DATA_TRANSFORMS.
        """

        DEPLOYMENT_TYPE_UNSPECIFIED = 0
        OGG = 1
        DATABASE_ORACLE = 2
        BIGDATA = 3
        DATABASE_MICROSOFT_SQLSERVER = 4
        DATABASE_MYSQL = 5
        DATABASE_POSTGRESQL = 6
        DATABASE_DB2ZOS = 7
        DATABASE_DB2I = 8
        GGSA = 9
        DATA_TRANSFORMS = 10

    class DeploymentCategory(proto.Enum):
        r"""The category of the Goldengate Deployment Type resource.

        Values:
            DEPLOYMENT_CATEGORY_UNSPECIFIED (0):
                Default unspecified value.
            DATA_REPLICATION_CATEGORY (1):
                Goldengate Deployment Type category is
                DATA_REPLICATION_CATEGORY.
            DATA_TRANSFORMS_CATEGORY (2):
                Goldengate Deployment Type category is
                DATA_TRANSFORMS_CATEGORY.
        """

        DEPLOYMENT_CATEGORY_UNSPECIFIED = 0
        DATA_REPLICATION_CATEGORY = 1
        DATA_TRANSFORMS_CATEGORY = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deployment_type: DeploymentType = proto.Field(
        proto.ENUM,
        number=2,
        enum=DeploymentType,
    )
    category: DeploymentCategory = proto.Field(
        proto.ENUM,
        number=3,
        enum=DeploymentCategory,
    )
    connection_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ogg_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    source_technologies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    supported_capabilities: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    supported_technologies_url: str = proto.Field(
        proto.STRING,
        number=9,
    )
    target_technologies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    default_username: str = proto.Field(
        proto.STRING,
        number=11,
    )


class ListGoldengateDeploymentTypesRequest(proto.Message):
    r"""Message for listing GoldengateDeploymentTypes.

    Attributes:
        parent (str):
            Required. The parent resource.
            Format: projects/{project}/locations/{location}
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Either the deployment_type and ogg_version fields
            must be specified in the format:
            ``deployment_type="DATABASE_ORACLE"`` or
            ``ogg_version="version"``. Allowed values for
            deployment_type are: ``DATABASE_ORACLE``, ``BIGDATA``,
            ``DATABASE_MICROSOFT_SQLSERVER``, ``DATABASE_MYSQL``,
            ``DATABASE_POSTGRESQL``, ``DATABASE_DB2ZOS``,
            ``DATABASE_DB2I``, ``GGSA``, ``DATA_TRANSFORMS``.
        order_by (str):
            Optional. Hint for how to order the results
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


class ListGoldengateDeploymentTypesResponse(proto.Message):
    r"""Message for response to listing GoldengateDeploymentTypes

    Attributes:
        goldengate_deployment_types (MutableSequence[google.cloud.oracledatabase_v1.types.GoldengateDeploymentType]):
            The list of GoldengateDeploymentType
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. The resource names of
            locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    goldengate_deployment_types: MutableSequence["GoldengateDeploymentType"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="GoldengateDeploymentType",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
