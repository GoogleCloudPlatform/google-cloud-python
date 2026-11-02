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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "GoldengateDeploymentVersion",
        "GoldengateDeploymentVersionProperties",
        "ListGoldengateDeploymentVersionsRequest",
        "ListGoldengateDeploymentVersionsResponse",
    },
)


class GoldengateDeploymentVersion(proto.Message):
    r"""Details of the Goldengate Deployment Version resource.

    Attributes:
        name (str):
            Identifier. The name of the Goldengate Deployment Version
            resource with the format:
            projects/{project}/locations/{location}/goldengateDeploymentVersions/{goldengate_deployment_version}
        ocid (str):
            Output only. The deployment version ocid of
            the Goldengate Deployment Version resource.
        properties (google.cloud.oracledatabase_v1.types.GoldengateDeploymentVersionProperties):
            Output only. The technology type of the
            Goldengate Deployment Version resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ocid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    properties: "GoldengateDeploymentVersionProperties" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GoldengateDeploymentVersionProperties",
    )


class GoldengateDeploymentVersionProperties(proto.Message):
    r"""Properties of GoldengateDeploymentVersion.

    Attributes:
        deployment_type (google.cloud.oracledatabase_v1.types.GoldengateDeploymentVersionProperties.DeploymentType):
            Output only. The deployment type of the
            Goldengate Deployment Version resource.
        security_fix (bool):
            Optional. Whether the Goldengate Deployment
            Version resource is a security fix.
        ogg_version (str):
            Output only. The OGG version of the
            Goldengate Deployment Version resource.
        release_type (google.cloud.oracledatabase_v1.types.GoldengateDeploymentVersionProperties.DeploymentReleaseType):
            Output only. The release type of the
            Goldengate Deployment Version resource.
        release_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The release time of the
            Goldengate Deployment Version resource.
        support_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The support end time of the
            Goldengate Deployment Version resource.
    """

    class DeploymentType(proto.Enum):
        r"""The deployment type of the Goldengate Deployment Version
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

    class DeploymentReleaseType(proto.Enum):
        r"""The release type of the Goldengate Deployment Version
        resource.

        Values:
            DEPLOYMENT_RELEASE_TYPE_UNSPECIFIED (0):
                Default unspecified value.
            MAJOR (1):
                Goldengate Deployment Version release type is
                MAJOR.
            BUNDLE (2):
                Goldengate Deployment Version release type is
                BUNDLE.
            MINOR (3):
                Goldengate Deployment Version release type is
                MINOR.
        """

        DEPLOYMENT_RELEASE_TYPE_UNSPECIFIED = 0
        MAJOR = 1
        BUNDLE = 2
        MINOR = 3

    deployment_type: DeploymentType = proto.Field(
        proto.ENUM,
        number=1,
        enum=DeploymentType,
    )
    security_fix: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    ogg_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    release_type: DeploymentReleaseType = proto.Field(
        proto.ENUM,
        number=4,
        enum=DeploymentReleaseType,
    )
    release_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    support_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class ListGoldengateDeploymentVersionsRequest(proto.Message):
    r"""Message for listing GoldengateDeploymentVersions.

    Attributes:
        parent (str):
            Required. Parent value for
            ListGoldengateDeploymentVersionsRequest Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default. The maximum value is 1000; values above
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Either the deployment_id and deployment_type fields
            must be specified in the format: ``deployment_id="id"`` or
            ``deployment_type="DATABASE_ORACLE"``.
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


class ListGoldengateDeploymentVersionsResponse(proto.Message):
    r"""Message for response to listing GoldengateDeploymentVersions

    Attributes:
        goldengate_deployment_versions (MutableSequence[google.cloud.oracledatabase_v1.types.GoldengateDeploymentVersion]):
            The list of GoldengateDeploymentVersion
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    goldengate_deployment_versions: MutableSequence["GoldengateDeploymentVersion"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="GoldengateDeploymentVersion",
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
