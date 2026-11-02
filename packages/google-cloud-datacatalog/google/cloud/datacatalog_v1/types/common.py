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
    package="google.cloud.datacatalog.v1",
    manifest={
        "IntegratedSystem",
        "ManagingSystem",
        "PersonalDetails",
    },
)


class IntegratedSystem(proto.Enum):
    r"""This enum lists all the systems that Data Catalog integrates
    with.

    Values:
        INTEGRATED_SYSTEM_UNSPECIFIED (0):
            Default unknown system.
        BIGQUERY (1):
            BigQuery.
        CLOUD_PUBSUB (2):
            Cloud Pub/Sub.
        DATAPROC_METASTORE (3):
            Dataproc Metastore.
        DATAPLEX (4):
            Dataplex.
        CLOUD_SPANNER (6):
            Cloud Spanner
        CLOUD_BIGTABLE (7):
            Cloud Bigtable
        CLOUD_SQL (8):
            Cloud Sql
        LOOKER (9):
            Looker
        VERTEX_AI (10):
            Vertex AI
    """

    INTEGRATED_SYSTEM_UNSPECIFIED = 0
    BIGQUERY = 1
    CLOUD_PUBSUB = 2
    DATAPROC_METASTORE = 3
    DATAPLEX = 4
    CLOUD_SPANNER = 6
    CLOUD_BIGTABLE = 7
    CLOUD_SQL = 8
    LOOKER = 9
    VERTEX_AI = 10


class ManagingSystem(proto.Enum):
    r"""This enum describes all the systems that manage
    Taxonomy and PolicyTag resources in DataCatalog.

    Values:
        MANAGING_SYSTEM_UNSPECIFIED (0):
            Default value
        MANAGING_SYSTEM_DATAPLEX (1):
            Dataplex.
        MANAGING_SYSTEM_OTHER (2):
            Other
    """

    MANAGING_SYSTEM_UNSPECIFIED = 0
    MANAGING_SYSTEM_DATAPLEX = 1
    MANAGING_SYSTEM_OTHER = 2


class PersonalDetails(proto.Message):
    r"""Entry metadata relevant only to the user and private to them.

    Attributes:
        starred (bool):
            True if the entry is starred by the user;
            false otherwise.
        star_time (google.protobuf.timestamp_pb2.Timestamp):
            Set if the entry is starred; unset otherwise.
    """

    starred: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    star_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
