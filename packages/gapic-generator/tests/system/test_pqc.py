# Copyright 2026 Google LLC
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

import grpc
from packaging.version import Version
import pytest
from google import showcase


@pytest.fixture(autouse=True)
def require_tls(use_tls):
    if not use_tls:
        pytest.skip("PQC integration test requires standard TLS (--tls flag) to be enabled.")


def _verify_pqc_metadata(interceptor, transport_name):
    """Extracts and verifies negotiated PQC group and supported groups from interceptor metadata."""
    response_metadata = getattr(interceptor, "response_metadata", []) or []
    headers = {key.lower(): value for key, value in response_metadata}
    negotiated_group = headers.get("x-showcase-tls-group")
    supported_groups = headers.get("x-showcase-tls-client-supported-groups")

    assert negotiated_group is not None, "Failed: Showcase server did not return negotiated TLS group header."
    assert supported_groups is not None, "Failed: Showcase server did not return client advertised supported groups."

    # Enforce PQC compliance by verifying a post-quantum MLKEM group was negotiated.
    # Substring check ("MLKEM" in ...) ensures compatibility across different transport and library group strings.
    assert (
        "MLKEM" in negotiated_group
    ), f"Failed: {transport_name} Connection did not negotiate a post-quantum MLKEM group! Negotiated: {negotiated_group}"


def test_pqc_grpc(intercepted_echo_grpc):
    """Verifies that the gRPC client library negotiates post-quantum MLKEM with Showcase server."""
    # TODO(https://github.com/googleapis/google-cloud-python/issues/17752):
    # Remove this check once grpcio >= 1.83.0 is enforced across all client libraries.
    if Version(grpc.__version__) < Version("1.83.0"):
        pytest.skip(f"gRPC PQC negotiation requires grpcio >= 1.83.0 (current: {grpc.__version__})")

    client, interceptor = intercepted_echo_grpc
    response = client.echo(request=showcase.EchoRequest(content="Verify PQC connection."))
    assert response.content == "Verify PQC connection."
    _verify_pqc_metadata(interceptor, "grpc")


def test_pqc_rest(intercepted_echo_rest):
    """Verifies that the REST client library negotiates post-quantum MLKEM with Showcase server."""
    client, interceptor = intercepted_echo_rest
    response = client.echo(request=showcase.EchoRequest(content="Verify PQC connection."))
    assert response.content == "Verify PQC connection."
    _verify_pqc_metadata(interceptor, "rest")


@pytest.mark.asyncio
async def test_pqc_grpc_async(intercepted_echo_grpc_async):
    """Verifies that the async gRPC client library negotiates post-quantum MLKEM with Showcase server."""
    # TODO(https://github.com/googleapis/google-cloud-python/issues/17752):
    # Remove this check once grpcio >= 1.83.0 is enforced across all client libraries.
    if Version(grpc.__version__) < Version("1.83.0"):
        pytest.skip(
            f"gRPC PQC negotiation requires grpcio >= 1.83.0 (current: {grpc.__version__})"
        )

    client, interceptor = intercepted_echo_grpc_async
    response = await client.echo(
        request=showcase.EchoRequest(content="Verify PQC connection.")
    )
    assert response.content == "Verify PQC connection."
    _verify_pqc_metadata(interceptor, "grpc_asyncio")
