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
        "GoldengateConnectionType",
        "ListGoldengateConnectionTypesRequest",
        "ListGoldengateConnectionTypesResponse",
    },
)


class GoldengateConnectionType(proto.Message):
    r"""Details of the Goldengate Connection Type resource.

    Attributes:
        name (str):
            Identifier. The name of the Goldengate Connection Type
            resource with the format:
            projects/{project}/locations/{region}/goldengateConnectionTypes/{goldengate_connection_type}
        connection_type (google.cloud.oracledatabase_v1.types.GoldengateConnectionType.ConnectionType):
            Output only. The connection type of the
            Goldengate Connection Type resource.
        technology_types (MutableSequence[str]):
            Output only. The technology type of the
            Goldengate Connection Type resource.
    """

    class ConnectionType(proto.Enum):
        r"""The connection type of the Goldengate Connection Type
        resource.

        Values:
            CONNECTION_TYPE_UNSPECIFIED (0):
                Default unspecified value.
            GOLDENGATE (1):
                Goldengate Connection Type category is
                GOLDENGATE.
            KAFKA (2):
                Goldengate Connection Type category is KAFKA.
            KAFKA_SCHEMA_REGISTRY (3):
                Goldengate Connection Type category is
                KAFKA_SCHEMA_REGISTRY.
            MYSQL (4):
                Goldengate Connection Type category is MYSQL.
            JAVA_MESSAGE_SERVICE (5):
                Goldengate Connection Type category is JAVA_MESSAGE_SERVICE.
            MICROSOFT_SQLSERVER (6):
                Goldengate Connection Type category is MICROSOFT_SQLSERVER.
            OCI_OBJECT_STORAGE (7):
                Goldengate Connection Type category is OCI_OBJECT_STORAGE.
            ORACLE (8):
                Goldengate Connection Type category is
                ORACLE.
            AZURE_DATA_LAKE_STORAGE (9):
                Goldengate Connection Type category is
                AZURE_DATA_LAKE_STORAGE.
            POSTGRESQL (10):
                Goldengate Connection Type category is
                POSTGRESQL.
            AZURE_SYNAPSE_ANALYTICS (11):
                Goldengate Connection Type category is
                AZURE_SYNAPSE_ANALYTICS.
            SNOWFLAKE (12):
                Goldengate Connection Type category is
                SNOWFLAKE.
            AMAZON_S3 (13):
                Goldengate Connection Type category is AMAZON_S3.
            HDFS (14):
                Goldengate Connection Type category is HDFS.
            ORACLE_AI_DATA_PLATFORM (15):
                Goldengate Connection Type category is
                ORACLE_AI_DATA_PLATFORM.
            ORACLE_NOSQL (16):
                Goldengate Connection Type category is ORACLE_NOSQL.
            MONGODB (17):
                Goldengate Connection Type category is
                MONGODB.
            AMAZON_KINESIS (18):
                Goldengate Connection Type category is AMAZON_KINESIS.
            AMAZON_REDSHIFT (19):
                Goldengate Connection Type category is AMAZON_REDSHIFT.
            DB2 (20):
                Goldengate Connection Type category is DB2.
            REDIS (21):
                Goldengate Connection Type category is REDIS.
            ELASTICSEARCH (22):
                Goldengate Connection Type category is
                ELASTICSEARCH.
            GENERIC (23):
                Goldengate Connection Type category is
                GENERIC.
            GOOGLE_CLOUD_STORAGE (24):
                Goldengate Connection Type category is GOOGLE_CLOUD_STORAGE.
            GOOGLE_BIGQUERY (25):
                Goldengate Connection Type category is GOOGLE_BIGQUERY.
            DATABRICKS (26):
                Goldengate Connection Type category is
                DATABRICKS.
            GOOGLE_PUBSUB (27):
                Goldengate Connection Type category is GOOGLE_PUBSUB.
            MICROSOFT_FABRIC (28):
                Goldengate Connection Type category is MICROSOFT_FABRIC.
            ICEBERG (29):
                Goldengate Connection Type category is
                ICEBERG.
        """

        CONNECTION_TYPE_UNSPECIFIED = 0
        GOLDENGATE = 1
        KAFKA = 2
        KAFKA_SCHEMA_REGISTRY = 3
        MYSQL = 4
        JAVA_MESSAGE_SERVICE = 5
        MICROSOFT_SQLSERVER = 6
        OCI_OBJECT_STORAGE = 7
        ORACLE = 8
        AZURE_DATA_LAKE_STORAGE = 9
        POSTGRESQL = 10
        AZURE_SYNAPSE_ANALYTICS = 11
        SNOWFLAKE = 12
        AMAZON_S3 = 13
        HDFS = 14
        ORACLE_AI_DATA_PLATFORM = 15
        ORACLE_NOSQL = 16
        MONGODB = 17
        AMAZON_KINESIS = 18
        AMAZON_REDSHIFT = 19
        DB2 = 20
        REDIS = 21
        ELASTICSEARCH = 22
        GENERIC = 23
        GOOGLE_CLOUD_STORAGE = 24
        GOOGLE_BIGQUERY = 25
        DATABRICKS = 26
        GOOGLE_PUBSUB = 27
        MICROSOFT_FABRIC = 28
        ICEBERG = 29

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_type: ConnectionType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ConnectionType,
    )
    technology_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListGoldengateConnectionTypesRequest(proto.Message):
    r"""Message for listing GoldengateConnectionTypes.

    Attributes:
        parent (str):
            Required. Parent value for
            ListGoldengateConnectionTypesRequest Format:
            projects/{project}/locations/{location}
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
            request. The connection_type field must be specified in the
            format: ``connection_type="ORACLE"``.
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


class ListGoldengateConnectionTypesResponse(proto.Message):
    r"""Message for response to listing GoldengateConnectionTypes

    Attributes:
        goldengate_connection_types (MutableSequence[google.cloud.oracledatabase_v1.types.GoldengateConnectionType]):
            The list of GoldengateConnectionType
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

    goldengate_connection_types: MutableSequence["GoldengateConnectionType"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="GoldengateConnectionType",
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
