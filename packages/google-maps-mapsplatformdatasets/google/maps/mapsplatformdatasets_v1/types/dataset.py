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

from google.maps.mapsplatformdatasets_v1.types import data_source

__protobuf__ = proto.module(
    package="google.maps.mapsplatformdatasets.v1",
    manifest={
        "Usage",
        "Dataset",
        "Status",
    },
)


class Usage(proto.Enum):
    r"""Usage specifies where the data is intended to be used to
    inform how to process the data.

    Values:
        USAGE_UNSPECIFIED (0):
            The usage of this dataset is not set.
        USAGE_DATA_DRIVEN_STYLING (1):
            This dataset will be used for data driven
            styling.
    """

    USAGE_UNSPECIFIED = 0
    USAGE_DATA_DRIVEN_STYLING = 1


class Dataset(proto.Message):
    r"""A representation of a dataset resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Resource name. Format:
            projects/{project}/datasets/{dataset_id}
        display_name (str):
            Human readable name, shown in the console UI.

            Must be unique within a project.
        description (str):
            A description of this dataset.
        version_id (str):
            The version ID of the dataset.
        usage (MutableSequence[google.maps.mapsplatformdatasets_v1.types.Usage]):
            Specified use case for this dataset.
        local_file_source (google.maps.mapsplatformdatasets_v1.types.LocalFileSource):
            A local file source for the dataset for a
            single upload.

            This field is a member of `oneof`_ ``data_source``.
        gcs_source (google.maps.mapsplatformdatasets_v1.types.GcsSource):
            A Google Cloud Storage file source for the
            dataset for a single upload.

            This field is a member of `oneof`_ ``data_source``.
        status (google.maps.mapsplatformdatasets_v1.types.Status):
            Output only. The status of this dataset
            version.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the dataset was first
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the dataset metadata
            was last updated.
        version_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this version was
            created.
        version_description (str):
            Output only. The description for this version
            of dataset. It is provided when importing data
            to the dataset.
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
    version_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    usage: MutableSequence["Usage"] = proto.RepeatedField(
        proto.ENUM,
        number=5,
        enum="Usage",
    )
    local_file_source: data_source.LocalFileSource = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data_source",
        message=data_source.LocalFileSource,
    )
    gcs_source: data_source.GcsSource = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="data_source",
        message=data_source.GcsSource,
    )
    status: "Status" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="Status",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    version_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    version_description: str = proto.Field(
        proto.STRING,
        number=11,
    )


class Status(proto.Message):
    r"""Status of the dataset.

    Attributes:
        state (google.maps.mapsplatformdatasets_v1.types.Status.State):
            State enum for status.
        error_message (str):
            Error message indicating reason of failure.
            It is empty if the datasets is not in a failed
            state.
    """

    class State(proto.Enum):
        r"""A list of states for the dataset.

        Values:
            STATE_UNSPECIFIED (0):
                The state of this dataset is not set.
            STATE_IMPORTING (1):
                Data is being imported to a dataset.
            STATE_IMPORT_SUCCEEDED (2):
                Importing data to a dataset succeeded.
            STATE_IMPORT_FAILED (3):
                Importing data to a dataset failed.
            STATE_DELETING (4):
                The dataset is in the process of getting
                deleted.
            STATE_DELETION_FAILED (5):
                The deletion failed state. This state
                represents that dataset deletion has failed.
                Deletion may be retried.
            STATE_PROCESSING (6):
                Data is being processed.
            STATE_PROCESSING_FAILED (7):
                The processing failed state. This state
                represents that processing has failed and may
                report errors.
            STATE_NEEDS_REVIEW (8):
                This state is currently not used.
            STATE_PUBLISHING (9):
                The publishing state. This state represents
                the publishing is in progress.
            STATE_PUBLISHING_FAILED (10):
                The publishing failed states. This state
                represents that the publishing failed.
                Publishing may be retried.
            STATE_COMPLETED (11):
                The completed state. This state represents
                the dataset being available for its specific
                usage.
        """

        STATE_UNSPECIFIED = 0
        STATE_IMPORTING = 1
        STATE_IMPORT_SUCCEEDED = 2
        STATE_IMPORT_FAILED = 3
        STATE_DELETING = 4
        STATE_DELETION_FAILED = 5
        STATE_PROCESSING = 6
        STATE_PROCESSING_FAILED = 7
        STATE_NEEDS_REVIEW = 8
        STATE_PUBLISHING = 9
        STATE_PUBLISHING_FAILED = 10
        STATE_COMPLETED = 11

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
