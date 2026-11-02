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

from google.cloud.datacatalog_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1",
    manifest={
        "SearchResultType",
        "SearchCatalogResult",
    },
)


class SearchResultType(proto.Enum):
    r"""The resource types that can be returned in search results.

    Values:
        SEARCH_RESULT_TYPE_UNSPECIFIED (0):
            Default unknown type.
        ENTRY (1):
            An [Entry][google.cloud.datacatalog.v1.Entry].
        TAG_TEMPLATE (2):
            A [TagTemplate][google.cloud.datacatalog.v1.TagTemplate].
        ENTRY_GROUP (3):
            An [EntryGroup][google.cloud.datacatalog.v1.EntryGroup].
    """

    SEARCH_RESULT_TYPE_UNSPECIFIED = 0
    ENTRY = 1
    TAG_TEMPLATE = 2
    ENTRY_GROUP = 3


class SearchCatalogResult(proto.Message):
    r"""Result in the response to a search request.

    Each result captures details of one entry that matches the
    search.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        search_result_type (google.cloud.datacatalog_v1.types.SearchResultType):
            Type of the search result.

            You can use this field to determine which get
            method to call to fetch the full resource.
        search_result_subtype (str):
            Sub-type of the search result.

            A dot-delimited full type of the resource. The same type you
            specify in the ``type`` search predicate.

            Examples: ``entry.table``, ``entry.dataStream``,
            ``tagTemplate``.
        relative_resource_name (str):
            The relative name of the resource in URL format.

            Examples:

            - ``projects/{PROJECT_ID}/locations/{LOCATION_ID}/entryGroups/{ENTRY_GROUP_ID}/entries/{ENTRY_ID}``
            - ``projects/{PROJECT_ID}/tagTemplates/{TAG_TEMPLATE_ID}``
        linked_resource (str):
            The full name of the Google Cloud resource the entry belongs
            to.

            For more information, see [Full Resource Name]
            (/apis/design/resource_names#full_resource_name).

            Example:

            ``//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID``
        modify_time (google.protobuf.timestamp_pb2.Timestamp):
            The last modification timestamp of the entry
            in the source system.
        integrated_system (google.cloud.datacatalog_v1.types.IntegratedSystem):
            Output only. The source system that Data
            Catalog automatically integrates with, such as
            BigQuery, Cloud Pub/Sub, or Dataproc Metastore.

            This field is a member of `oneof`_ ``system``.
        user_specified_system (str):
            Custom source system that you can manually
            integrate Data Catalog with.

            This field is a member of `oneof`_ ``system``.
        fully_qualified_name (str):
            Fully qualified name (FQN) of the resource.

            FQNs take two forms:

            - For non-regionalized resources:

              ``{SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}``

            - For regionalized resources:

              ``{SYSTEM}:{PROJECT}.{LOCATION_ID}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}``

            Example for a DPMS table:

            ``dataproc_metastore:PROJECT_ID.LOCATION_ID.INSTANCE_ID.DATABASE_ID.TABLE_ID``
        display_name (str):
            The display name of the result.
        description (str):
            Entry description that can consist of several
            sentences or paragraphs that describe entry
            contents.
    """

    search_result_type: "SearchResultType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SearchResultType",
    )
    search_result_subtype: str = proto.Field(
        proto.STRING,
        number=2,
    )
    relative_resource_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    linked_resource: str = proto.Field(
        proto.STRING,
        number=4,
    )
    modify_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    integrated_system: common.IntegratedSystem = proto.Field(
        proto.ENUM,
        number=8,
        oneof="system",
        enum=common.IntegratedSystem,
    )
    user_specified_system: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="system",
    )
    fully_qualified_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    description: str = proto.Field(
        proto.STRING,
        number=13,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
