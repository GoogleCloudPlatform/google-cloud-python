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
    package="google.cloud.ces.v1beta",
    manifest={
        "DataStore",
    },
)


class DataStore(proto.Message):
    r"""A DataStore resource in Vertex AI Search.

    Attributes:
        name (str):
            Required. Full resource name of the DataStore. Format:
            ``projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}``
        type_ (google.cloud.ces_v1beta.types.DataStore.DataStoreType):
            Output only. The type of the data store. This
            field is readonly and populated by the server.
        document_processing_mode (google.cloud.ces_v1beta.types.DataStore.DocumentProcessingMode):
            Output only. The document processing mode for the data store
            connection. Only set for PUBLIC_WEB and UNSTRUCTURED data
            stores.
        display_name (str):
            Output only. The display name of the data
            store.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the data store
            was created.
        connector_config (google.cloud.ces_v1beta.types.DataStore.ConnectorConfig):
            Output only. The connector config for the
            data store connection.
    """

    class DataStoreType(proto.Enum):
        r"""The type of the data store.

        Values:
            DATA_STORE_TYPE_UNSPECIFIED (0):
                Not specified. This value indicates that the
                data store type is not specified, so it will not
                be used during search.
            PUBLIC_WEB (1):
                A data store that contains public web
                content.
            UNSTRUCTURED (2):
                A data store that contains unstructured
                private data.
            FAQ (3):
                A data store that contains structured data
                used as FAQ.
            CONNECTOR (4):
                A data store that is a connector to a
                first-party or a third-party service.
        """

        DATA_STORE_TYPE_UNSPECIFIED = 0
        PUBLIC_WEB = 1
        UNSTRUCTURED = 2
        FAQ = 3
        CONNECTOR = 4

    class DocumentProcessingMode(proto.Enum):
        r"""The document processing mode of the data store.

        Values:
            DOCUMENT_PROCESSING_MODE_UNSPECIFIED (0):
                Not specified.
            DOCUMENTS (1):
                Documents are processed as documents.
            CHUNKS (2):
                Documents are converted to chunks.
        """

        DOCUMENT_PROCESSING_MODE_UNSPECIFIED = 0
        DOCUMENTS = 1
        CHUNKS = 2

    class ConnectorConfig(proto.Message):
        r"""The connector config for the data store connection.

        Attributes:
            collection (str):
                Resource name of the collection the data
                store belongs to.
            collection_display_name (str):
                Display name of the collection the data store
                belongs to.
            data_source (str):
                The name of the data source. Example: ``salesforce``,
                ``jira``, ``confluence``, ``bigquery``.
        """

        collection: str = proto.Field(
            proto.STRING,
            number=1,
        )
        collection_display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        data_source: str = proto.Field(
            proto.STRING,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: DataStoreType = proto.Field(
        proto.ENUM,
        number=2,
        enum=DataStoreType,
    )
    document_processing_mode: DocumentProcessingMode = proto.Field(
        proto.ENUM,
        number=4,
        enum=DocumentProcessingMode,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    connector_config: ConnectorConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=ConnectorConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
