# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from google import showcase


def test_metadata_string(echo):
    echo.echo(
        showcase.EchoRequest(
            content="The hail in Wales falls mainly on the snails.",
            request_id="some_value",
            other_request_id="",
        ),
        metadata=[("some-key", "some_value")],
    )


def test_metadata_binary(echo):
    echo.echo(
        showcase.EchoRequest(
            content="The hail in Wales falls mainly on the snails.",
            request_id="some_value",
            other_request_id="",
        ),
        metadata=[("some-key-bin", b"some_value")],
    )

    if isinstance(echo.transport, type(echo).get_transport_class("grpc")):
        # See https://github.com/googleapis/gapic-generator-python/issues/2250
        # and https://github.com/grpc/grpc/pull/38127.
        # When the metadata key ends in `-bin`, the value should be of type
        # `bytes`` rather than `str``. Otherwise, gRPC raises a TypeError.
        with pytest.raises(TypeError, match="(?i)expected bytes"):
            echo.echo(
                showcase.EchoRequest(
                    content="The hail in Wales falls mainly on the snails.",
                    request_id="some_value",
                    other_request_id="",
                ),
                metadata=[("some-key-bin", "some_value")],
            )
