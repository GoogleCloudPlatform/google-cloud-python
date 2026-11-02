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
    package="google.cloud.databasecenter.v1beta",
    manifest={
        "Engine",
        "ProductType",
        "Product",
    },
)


class Engine(proto.Enum):
    r"""Engine refers to underlying database binary running in an
    instance.

    Values:
        ENGINE_UNSPECIFIED (0):
            UNSPECIFIED means engine type is not known or
            available.
        ENGINE_MYSQL (1):
            MySQL binary running as an engine in the
            database instance.
        ENGINE_POSTGRES (2):
            Postgres binary running as engine in database
            instance.
        ENGINE_SQL_SERVER (3):
            SQLServer binary running as engine in
            database instance.
        ENGINE_NATIVE (4):
            Native database binary running as engine in
            instance.
        ENGINE_MEMORYSTORE_FOR_REDIS (8):
            Memorystore with Redis dialect.
        ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER (9):
            Memorystore with Redis cluster dialect.
        ENGINE_FIRESTORE_WITH_NATIVE_MODE (10):
            Firestore with native mode.
        ENGINE_FIRESTORE_WITH_DATASTORE_MODE (11):
            Firestore with datastore mode.
        ENGINE_EXADATA_ORACLE (12):
            Oracle Exadata engine.
        ENGINE_ADB_SERVERLESS_ORACLE (13):
            Oracle Autonomous DB Serverless engine.
        ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE (14):
            Firestore with MongoDB compatibility.
        ENGINE_OTHER (6):
            Other refers to rest of other database
            engine. This is to be when engine is known, but
            it is not present in this enum.
    """

    ENGINE_UNSPECIFIED = 0
    ENGINE_MYSQL = 1
    ENGINE_POSTGRES = 2
    ENGINE_SQL_SERVER = 3
    ENGINE_NATIVE = 4
    ENGINE_MEMORYSTORE_FOR_REDIS = 8
    ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER = 9
    ENGINE_FIRESTORE_WITH_NATIVE_MODE = 10
    ENGINE_FIRESTORE_WITH_DATASTORE_MODE = 11
    ENGINE_EXADATA_ORACLE = 12
    ENGINE_ADB_SERVERLESS_ORACLE = 13
    ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE = 14
    ENGINE_OTHER = 6


class ProductType(proto.Enum):
    r"""ProductType is used to identify a database service offering
    either in a cloud provider or on-premise. This enum needs to be
    updated whenever we introduce a new ProductType.

    Values:
        PRODUCT_TYPE_UNSPECIFIED (0):
            PRODUCT_TYPE_UNSPECIFIED means product type is not known or
            that the user didn't provide this field in the request.
        PRODUCT_TYPE_CLOUD_SQL (1):
            Cloud SQL product area in Google Cloud
        PRODUCT_TYPE_ALLOYDB (2):
            AlloyDB product area in Google Cloud
        PRODUCT_TYPE_SPANNER (3):
            Spanner product area in Google Cloud
        PRODUCT_TYPE_BIGTABLE (6):
            Bigtable product area in Google Cloud
        PRODUCT_TYPE_MEMORYSTORE (7):
            Memorystore product area in Google Cloud
        PRODUCT_TYPE_FIRESTORE (8):
            Firestore product area in Google Cloud
        PRODUCT_TYPE_COMPUTE_ENGINE (9):
            Compute Engine self managed databases
        PRODUCT_TYPE_ORACLE_ON_GCP (10):
            Oracle product area in Google Cloud
        PRODUCT_TYPE_BIGQUERY (11):
            BigQuery product area in Google Cloud
        PRODUCT_TYPE_OTHER (5):
            Other refers to rest of other product type.
            This is to be when product type is known, but it
            is not present in this enum.
    """

    PRODUCT_TYPE_UNSPECIFIED = 0
    PRODUCT_TYPE_CLOUD_SQL = 1
    PRODUCT_TYPE_ALLOYDB = 2
    PRODUCT_TYPE_SPANNER = 3
    PRODUCT_TYPE_BIGTABLE = 6
    PRODUCT_TYPE_MEMORYSTORE = 7
    PRODUCT_TYPE_FIRESTORE = 8
    PRODUCT_TYPE_COMPUTE_ENGINE = 9
    PRODUCT_TYPE_ORACLE_ON_GCP = 10
    PRODUCT_TYPE_BIGQUERY = 11
    PRODUCT_TYPE_OTHER = 5


class Product(proto.Message):
    r"""Product specification for databasecenter resources.

    Attributes:
        type_ (google.cloud.databasecenter_v1beta.types.ProductType):
            Optional. Type of specific database product.
            It could be CloudSQL, AlloyDB etc..
        engine (google.cloud.databasecenter_v1beta.types.Engine):
            Optional. The specific engine that the
            underlying database is running.
        version (str):
            Optional. Version of the underlying database
            engine. Example values: For MySQL, it could be
            "8.0", "5.7" etc. For Postgres, it could be
            "14", "15" etc.
        minor_version (str):
            Optional. Minor version of the underlying
            database engine. Example values: For MySQL, it
            could be "8.0.35", "5.7.25" etc. For PostgreSQL,
            it could be "14.4", "15.5" etc.
    """

    type_: "ProductType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ProductType",
    )
    engine: "Engine" = proto.Field(
        proto.ENUM,
        number=2,
        enum="Engine",
    )
    version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    minor_version: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
