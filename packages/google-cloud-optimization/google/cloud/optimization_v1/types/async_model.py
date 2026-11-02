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
    package="google.cloud.optimization.v1",
    manifest={
        "DataFormat",
        "InputConfig",
        "OutputConfig",
        "GcsSource",
        "GcsDestination",
        "AsyncModelMetadata",
    },
)


class DataFormat(proto.Enum):
    r"""Data formats for input and output files.

    Values:
        DATA_FORMAT_UNSPECIFIED (0):
            Default value.
        JSON (1):
            Input data in json format.
        STRING (2):
            Input data in string format.
    """

    DATA_FORMAT_UNSPECIFIED = 0
    JSON = 1
    STRING = 2


class InputConfig(proto.Message):
    r"""The desired input location information.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.optimization_v1.types.GcsSource):
            The Google Cloud Storage location to read the
            input from. This must be a single file.

            This field is a member of `oneof`_ ``source``.
        data_format (google.cloud.optimization_v1.types.DataFormat):
            The input data format that used to store the
            model in Cloud Storage.
    """

    gcs_source: "GcsSource" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="GcsSource",
    )
    data_format: "DataFormat" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DataFormat",
    )


class OutputConfig(proto.Message):
    r"""The desired output location.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.optimization_v1.types.GcsDestination):
            The Google Cloud Storage location to write
            the output to.

            This field is a member of `oneof`_ ``destination``.
        data_format (google.cloud.optimization_v1.types.DataFormat):
            The output data format that used to store the
            results in Cloud Storage.
    """

    gcs_destination: "GcsDestination" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message="GcsDestination",
    )
    data_format: "DataFormat" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DataFormat",
    )


class GcsSource(proto.Message):
    r"""The Google Cloud Storage location where the input file will
    be read from.

    Attributes:
        uri (str):
            Required. URI of the Google Cloud Storage
            location.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GcsDestination(proto.Message):
    r"""The Google Cloud Storage location where the output file will
    be written to.

    Attributes:
        uri (str):
            Required. URI of the Google Cloud Storage
            location.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AsyncModelMetadata(proto.Message):
    r"""The long running operation metadata for async model related
    methods.

    Attributes:
        state (google.cloud.optimization_v1.types.AsyncModelMetadata.State):
            The state of the current operation.
        state_message (str):
            A message providing more details about the
            current state of the operation. For example, the
            error message if the operation is failed.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The creation time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The last update time of the operation.
    """

    class State(proto.Enum):
        r"""Possible states of the operation.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            RUNNING (1):
                Request is being processed.
            SUCCEEDED (2):
                The operation completed successfully.
            CANCELLED (3):
                The operation was cancelled.
            FAILED (4):
                The operation has failed.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        CANCELLED = 3
        FAILED = 4

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
