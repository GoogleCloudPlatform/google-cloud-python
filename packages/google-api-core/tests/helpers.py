# Copyright 2024 Google LLC
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

"""Helpers for tests"""

import functools
import logging
from typing import List

import proto
import pytest
from google.protobuf import duration_pb2, timestamp_pb2
from google.protobuf.json_format import MessageToJson


class Genre(proto.Enum):
    GENRE_UNSPECIFIED = 0
    CLASSICAL = 1
    JAZZ = 2
    ROCK = 3


class Composer(proto.Message):
    given_name = proto.Field(proto.STRING, number=1)
    family_name = proto.Field(proto.STRING, number=2)
    relateds = proto.RepeatedField(proto.STRING, number=3)
    indices = proto.MapField(proto.STRING, proto.STRING, number=4)


class Song(proto.Message):
    composer = proto.Field(Composer, number=1)
    title = proto.Field(proto.STRING, number=2)
    lyrics = proto.Field(proto.STRING, number=3)
    year = proto.Field(proto.INT32, number=4)
    genre = proto.Field(Genre, number=5)
    is_five_mins_longer = proto.Field(proto.BOOL, number=6)
    score = proto.Field(proto.DOUBLE, number=7)
    likes = proto.Field(proto.INT64, number=8)
    duration = proto.Field(duration_pb2.Duration, number=9)
    date_added = proto.Field(timestamp_pb2.Timestamp, number=10)


class EchoResponse(proto.Message):
    content = proto.Field(proto.STRING, number=1)


def parse_responses(response_message_cls, all_responses: List[proto.Message]) -> bytes:
    # json.dumps returns a string surrounded with quotes that need to be stripped
    # in order to be an actual JSON.
    json_responses = [
        (
            response_message_cls.to_json(response).strip('"')
            if issubclass(response_message_cls, proto.Message)
            else MessageToJson(response).strip('"')
        )
        for response in all_responses
    ]
    logging.info(f"Sending JSON stream: {json_responses}")
    ret_val = "[{}]".format(",".join(json_responses))
    return bytes(ret_val, "utf-8")


warn_deprecated_credentials_file = functools.partial(
    # This is used to test that the auth credentials file deprecation
    # warning is emitted as expected.
    pytest.warns,
    DeprecationWarning,
    match="argument is deprecated because of a potential security risk",
)


def assert_uninstrumented_gapic_callable(
    wrapped,
    result,
    mock_target,
    mock_trace=None,
    expected_result="success",
):
    """Verifies that an uninstrumented RPC callable succeeds without tracing overhead.

    1. Proves the RPC executed successfully with the expected return value.
    2. Proves the OpenTelemetry API was never invoked.
    3. Proves the callable holds no tracer or span configuration.
    """
    # 1. Prove the RPC executed successfully
    assert result == expected_result
    mock_target.assert_called_once()

    # 2. Prove the OpenTelemetry API was never invoked
    if mock_trace is not None:
        mock_trace.get_tracer.assert_not_called()

    # 3. Prove the callable holds no span factory
    assert getattr(wrapped, "_start_span_fn", None) is None
