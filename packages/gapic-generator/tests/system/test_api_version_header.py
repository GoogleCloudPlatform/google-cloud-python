# Copyright 2024 Google LLC
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

try:
    from google.api_core import version_header
except ImportError:
    version_header = None


def test_api_version_in_grpc_trailing_metadata(echo):
    if not version_header:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )

    # This feature requires version 0.35.0 of `gapic-showcase` or newer which has the
    # ability to echo request headers
    content = "The hail in Wales falls mainly on the snails."
    responses = echo.expand(
        {
            "content": content,
        }
    )
    if isinstance(echo.transport, type(echo).get_transport_class("grpc")):
        response_metadata = [
            (metadata.key, metadata.value) for metadata in responses.trailing_metadata()
        ]
        assert ("x-goog-api-version", "v1_20240408") in response_metadata
    else:
        assert "X-Showcase-Request-X-Goog-Api-Version" in responses._response.headers
        assert (
            responses._response.headers["X-Showcase-Request-X-Goog-Api-Version"]
            == "v1_20240408"
        )
