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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflow_v2.types import gcs

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "ConversationInfo",
        "InputConfig",
        "ConversationDataset",
        "CreateConversationDatasetRequest",
        "GetConversationDatasetRequest",
        "ListConversationDatasetsRequest",
        "ListConversationDatasetsResponse",
        "DeleteConversationDatasetRequest",
        "ImportConversationDataRequest",
        "ImportConversationDataOperationMetadata",
        "ImportConversationDataOperationResponse",
        "CreateConversationDatasetOperationMetadata",
        "DeleteConversationDatasetOperationMetadata",
    },
)


class ConversationInfo(proto.Message):
    r"""Represents metadata of a conversation.

    Attributes:
        language_code (str):
            Optional. The language code of the conversation data within
            this dataset. See
            https://cloud.google.com/apis/design/standard_fields for
            more information. Supports all UTF-8 languages.
    """

    language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InputConfig(proto.Message):
    r"""Represents the configuration of importing a set of
    conversation files in Google Cloud Storage.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.dialogflow_v2.types.GcsSources):
            The Cloud Storage URI has the form gs:////agent\*.json.
            Wildcards are allowed and will be expanded into all matched
            JSON files, which will be read as one conversation per file.

            This field is a member of `oneof`_ ``source``.
    """

    gcs_source: gcs.GcsSources = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message=gcs.GcsSources,
    )


class ConversationDataset(proto.Message):
    r"""Represents a conversation dataset that a user imports raw
    data into. The data inside ConversationDataset can not be
    changed after ImportConversationData finishes (and calling
    ImportConversationData on a dataset that already has data is not
    allowed).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. ConversationDataset resource name. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>``
        display_name (str):
            Required. The display name of the dataset.
            Maximum of 64 bytes.
        description (str):
            Optional. The description of the dataset.
            Maximum of 10000 bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this dataset.
        input_config (google.cloud.dialogflow_v2.types.InputConfig):
            Output only. Input configurations set during
            conversation data import.
        conversation_info (google.cloud.dialogflow_v2.types.ConversationInfo):
            Output only. Metadata set during conversation
            data import.
        conversation_count (int):
            Output only. The number of conversations this
            conversation dataset contains.
        satisfies_pzi (bool):
            Output only. A read only boolean field
            reflecting Zone Isolation status of the dataset.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
        satisfies_pzs (bool):
            Output only. A read only boolean field
            reflecting Zone Separation status of the
            dataset.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    input_config: "InputConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="InputConfig",
    )
    conversation_info: "ConversationInfo" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ConversationInfo",
    )
    conversation_count: int = proto.Field(
        proto.INT64,
        number=7,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )


class CreateConversationDatasetRequest(proto.Message):
    r"""The request message for
    [ConversationDatasets.CreateConversationDataset][google.cloud.dialogflow.v2.ConversationDatasets.CreateConversationDataset].

    Attributes:
        parent (str):
            Required. The project to create conversation dataset for.
            Format: ``projects/<Project ID>/locations/<Location ID>``
        conversation_dataset (google.cloud.dialogflow_v2.types.ConversationDataset):
            Required. The conversation dataset to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    conversation_dataset: "ConversationDataset" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ConversationDataset",
    )


class GetConversationDatasetRequest(proto.Message):
    r"""The request message for
    [ConversationDatasets.GetConversationDataset][google.cloud.dialogflow.v2.ConversationDatasets.GetConversationDataset].

    Attributes:
        name (str):
            Required. The conversation dataset to retrieve. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConversationDatasetsRequest(proto.Message):
    r"""The request message for
    [ConversationDatasets.ListConversationDatasets][google.cloud.dialogflow.v2.ConversationDatasets.ListConversationDatasets].

    Attributes:
        parent (str):
            Required. The project and location name to list all
            conversation datasets for. Format:
            ``projects/<Project ID>/locations/<Location ID>``
        page_size (int):
            Optional. Maximum number of conversation
            datasets to return in a single page. By default
            100 and at most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
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


class ListConversationDatasetsResponse(proto.Message):
    r"""The response message for
    [ConversationDatasets.ListConversationDatasets][google.cloud.dialogflow.v2.ConversationDatasets.ListConversationDatasets].

    Attributes:
        conversation_datasets (MutableSequence[google.cloud.dialogflow_v2.types.ConversationDataset]):
            The list of datasets to return.
        next_page_token (str):
            The token to use to retrieve the next page of
            results, or empty if there are no more results
            in the list.
    """

    @property
    def raw_page(self):
        return self

    conversation_datasets: MutableSequence["ConversationDataset"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ConversationDataset",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteConversationDatasetRequest(proto.Message):
    r"""The request message for
    [ConversationDatasets.DeleteConversationDataset][google.cloud.dialogflow.v2.ConversationDatasets.DeleteConversationDataset].

    Attributes:
        name (str):
            Required. The conversation dataset to delete. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportConversationDataRequest(proto.Message):
    r"""The request message for
    [ConversationDatasets.ImportConversationData][google.cloud.dialogflow.v2.ConversationDatasets.ImportConversationData].

    Attributes:
        name (str):
            Required. Dataset resource name. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>``
        input_config (google.cloud.dialogflow_v2.types.InputConfig):
            Required. Configuration describing where to
            import data from.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_config: "InputConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InputConfig",
    )


class ImportConversationDataOperationMetadata(proto.Message):
    r"""Metadata for a
    [ConversationDatasets.ImportConversationData][google.cloud.dialogflow.v2.ConversationDatasets.ImportConversationData]
    operation.

    Attributes:
        conversation_dataset (str):
            The resource name of the imported conversation dataset.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset Id>``
        partial_failures (MutableSequence[google.rpc.status_pb2.Status]):
            Partial failures are failures that don't fail
            the whole long running operation, e.g. single
            files that couldn't be read.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when import conversation data
            request was created. The time is measured on
            server side.
    """

    conversation_dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partial_failures: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class ImportConversationDataOperationResponse(proto.Message):
    r"""Response used for
    [ConversationDatasets.ImportConversationData][google.cloud.dialogflow.v2.ConversationDatasets.ImportConversationData]
    long running operation.

    Attributes:
        conversation_dataset (str):
            The resource name of the imported conversation dataset.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset Id>``
        import_count (int):
            Number of conversations imported
            successfully.
    """

    conversation_dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    import_count: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateConversationDatasetOperationMetadata(proto.Message):
    r"""Metadata for [CreateConversationDataset][].

    Attributes:
        conversation_dataset (str):
            The resource name of the conversation dataset that will be
            created. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset Id>``
    """

    conversation_dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteConversationDatasetOperationMetadata(proto.Message):
    r"""Metadata for [DeleteConversationDataset][]."""


__all__ = tuple(sorted(__protobuf__.manifest))
