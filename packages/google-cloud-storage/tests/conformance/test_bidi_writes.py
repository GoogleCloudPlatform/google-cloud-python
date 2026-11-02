import subprocess
import time
import urllib
import uuid

import grpc
import pytest
import requests
from google.api_core import client_options, exceptions
from google.api_core.retry_async import AsyncRetry
from google.auth import credentials as auth_credentials

from google.cloud import _storage_v2 as storage_v2
from google.cloud.storage.asyncio.async_appendable_object_writer import (
    AsyncAppendableObjectWriter,
)
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from tests.conformance._utils import start_grpc_server

# --- Configuration ---
TEST_BENCH_ENDPOINT = (
    "http://localhost:9002"  # 9000 in VM is taken by test_conformance.py, 9001 by reads
)
_PORT = urllib.parse.urlsplit(TEST_BENCH_ENDPOINT).port
_GRPC_PORT = 8888

PROJECT_NUMBER = "12345"  # A dummy project number is fine for the testbench.
GRPC_ENDPOINT = f"localhost:{_GRPC_PORT}"
HTTP_ENDPOINT = TEST_BENCH_ENDPOINT

_DEFAULT_IMAGE_NAME = "gcr.io/cloud-devrel-public-resources/storage-testbench"
_DEFAULT_IMAGE_TAG = "latest"
_DOCKER_IMAGE = f"{_DEFAULT_IMAGE_NAME}:{_DEFAULT_IMAGE_TAG}"
_PULL_CMD = ["docker", "pull", _DOCKER_IMAGE]
_RUN_CMD = [
    "docker",
    "run",
    "--name",
    "bidi_writes_container",
    "--rm",
    "-d",
    "-p",
    f"{_PORT}:9000",
    "-p",
    f"{_GRPC_PORT}:8888",
    _DOCKER_IMAGE,
]
_DOCKER_STOP_CMD = [
    "docker",
    "stop",
    "bidi_writes_container",
]


@pytest.fixture(scope="module")
def testbench():
    subprocess.run(_PULL_CMD)
    proc = subprocess.Popen(_RUN_CMD)
    time.sleep(10)
    yield GRPC_ENDPOINT, HTTP_ENDPOINT
    subprocess.run(_DOCKER_STOP_CMD)
    proc.kill()


CONTENT = b"A" * 1024 * 1024 * 10  # 10 MiB


def _is_retryable(exc):
    return isinstance(
        exc,
        (
            exceptions.InternalServerError,
            exceptions.ServiceUnavailable,
            exceptions.DeadlineExceeded,
            exceptions.TooManyRequests,
            exceptions.Aborted,  # For Redirects
        ),
    )


async def run_test_scenario(
    gapic_client,
    http_client,
    bucket_name,
    object_name,
    scenario,
):
    """Runs a single fault-injection test scenario."""
    print(f"\n--- RUNNING SCENARIO: {scenario['name']} ---")
    retry_count = 0

    def on_retry_error(exc):
        nonlocal retry_count
        retry_count += 1
        print(f"Retry attempt {retry_count} triggered by: {type(exc).__name__}")

    custom_retry = AsyncRetry(
        predicate=_is_retryable,
        on_error=on_retry_error,
        initial=0.1,  # Short backoff for fast tests
        multiplier=1.0,
    )

    use_default = scenario.get("use_default_policy", False)
    policy_to_pass = None if use_default else custom_retry

    retry_test_id = None
    try:
        # 1. Create a Retry Test resource on the testbench.
        retry_test_config = {
            "instructions": {scenario["method"]: [scenario["instruction"]]},
            "transport": "GRPC",
        }
        resp = http_client.post(f"{HTTP_ENDPOINT}/retry_test", json=retry_test_config)
        resp.raise_for_status()
        retry_test_id = resp.json()["id"]

        # 2. Set up writer and metadata for fault injection.
        grpc_client = AsyncGrpcClient._create_insecure_grpc_client(
            client_options=client_options.ClientOptions(api_endpoint=GRPC_ENDPOINT),
        )
        writer = AsyncAppendableObjectWriter(
            grpc_client,
            bucket_name,
            object_name,
            writer_options={"FLUSH_INTERVAL_BYTES": 2 * 1024 * 1024},
        )
        fault_injection_metadata = (("x-retry-test-id", retry_test_id),)

        # 3. Execute the write and assert the outcome.
        try:
            await writer.open(
                metadata=fault_injection_metadata, retry_policy=policy_to_pass
            )
            await writer.append(
                CONTENT, metadata=fault_injection_metadata, retry_policy=policy_to_pass
            )
            # await writer.finalize()
            f_o_c = scenario.get("finalize_on_close", True)
            await writer.close(finalize_on_close=f_o_c, retry_policy=policy_to_pass)

            # If an exception was expected, this line should not be reached.
            if scenario["expected_error"] is not None:
                raise AssertionError(
                    f"Expected exception {scenario['expected_error']} was not raised."
                )

            # 4. Verify the object content if applicable.
            if not scenario.get("skip_verification"):
                read_request = storage_v2.ReadObjectRequest(
                    bucket=f"projects/_/buckets/{bucket_name}",
                    object=object_name,
                )
                read_stream = await gapic_client.read_object(request=read_request)
                data = b""
                async for chunk in read_stream:
                    data += chunk.checksummed_data.content
                assert data == CONTENT

            if scenario["expected_error"] is None:
                # Scenarios like 503, 500, smarter resumption, and redirects
                # SHOULD trigger at least one retry attempt.
                if not use_default:
                    assert retry_count > 0, (
                        f"Test passed but no retry was actually triggered for {scenario['name']}!"
                    )
                else:
                    print("Successfully recovered using library's default policy.")
                print(f"Success: {scenario['name']}")

        except Exception as e:
            if scenario["expected_error"] is None or not isinstance(
                e, scenario["expected_error"]
            ):
                raise

    finally:
        # 5. Clean up the Retry Test resource.
        if retry_test_id:
            http_client.delete(f"{HTTP_ENDPOINT}/retry_test/{retry_test_id}")


@pytest.mark.asyncio
async def test_bidi_writes(testbench):
    """Main function to set up resources and run all test scenarios."""
    grpc_endpoint, http_endpoint = testbench
    start_grpc_server(
        grpc_endpoint, http_endpoint
    )  # Ensure the testbench gRPC server is running before this test executes.
    channel = grpc.aio.insecure_channel(grpc_endpoint)
    creds = auth_credentials.AnonymousCredentials()
    transport = storage_v2.services.storage.transports.StorageGrpcAsyncIOTransport(
        channel=channel,
        credentials=creds,
    )
    gapic_client = storage_v2.StorageAsyncClient(transport=transport)
    http_client = requests.Session()

    bucket_name = f"grpc-test-bucket-{uuid.uuid4().hex[:8]}"
    object_name_prefix = "retry-test-object-"

    # Define all test scenarios
    test_scenarios = [
        {
            "name": "Retry on Service Unavailable (503)",
            "method": "storage.objects.insert",
            "instruction": "return-503",
            "expected_error": None,
        },
        {
            "name": "Retry on 500",
            "method": "storage.objects.insert",
            "instruction": "return-500",
            "expected_error": None,
        },
        {
            "name": "Retry on 504",
            "method": "storage.objects.insert",
            "instruction": "return-504",
            "expected_error": None,
        },
        {
            "name": "Retry on 429",
            "method": "storage.objects.insert",
            "instruction": "return-429",
            "expected_error": None,
        },
        # TODO: b/490280918
        {
            "name": "Smarter Resumption: Retry 503 after partial data",
            "method": "storage.objects.insert",
            "instruction": "return-503-after-3072K",  # 3072 KiB == 3 MiB
            "expected_error": None,
        },
        {
            "name": "Retry on BidiWriteObjectRedirectedError",
            "method": "storage.objects.insert",
            "instruction": "redirect-send-handle-and-token-tokenval",
            "expected_error": None,
        },
        {
            "name": "Retry exactly on finalize/close (Redirect Error)",
            "method": "storage.objects.insert",
            "instruction": "redirect-send-handle-and-token-mytoken-on-finish-write",
            "expected_error": None,
        },
        {
            "name": "Retry exactly on finalize/close (503)",
            "method": "storage.objects.insert",
            "instruction": "return-503-on-finish-write",
            "expected_error": None,
        },
        {
            "name": "Retry exactly on close (finalize_on_close=False) (503)",
            "method": "storage.objects.insert",
            "instruction": "return-503-on-half-close",
            "expected_error": None,
            "finalize_on_close": False,
            "skip_verification": True,
        },
    ]

    try:
        bucket_resource = storage_v2.Bucket(project=f"projects/{PROJECT_NUMBER}")
        create_bucket_request = storage_v2.CreateBucketRequest(
            parent="projects/_", bucket_id=bucket_name, bucket=bucket_resource
        )
        await gapic_client.create_bucket(request=create_bucket_request)

        for i, scenario in enumerate(test_scenarios):
            object_name = f"{object_name_prefix}{i}"
            await run_test_scenario(
                gapic_client,
                http_client,
                bucket_name,
                object_name,
                scenario,
            )

    except Exception:
        import traceback

        traceback.print_exc()
    finally:
        # Clean up the test bucket.
        try:
            list_objects_req = storage_v2.ListObjectsRequest(
                parent=f"projects/_/buckets/{bucket_name}",
            )
            list_objects_res = await gapic_client.list_objects(request=list_objects_req)
            async for obj in list_objects_res:
                delete_object_req = storage_v2.DeleteObjectRequest(
                    bucket=f"projects/_/buckets/{bucket_name}", object=obj.name
                )
                await gapic_client.delete_object(request=delete_object_req)

            delete_bucket_req = storage_v2.DeleteBucketRequest(
                name=f"projects/_/buckets/{bucket_name}"
            )
            await gapic_client.delete_bucket(request=delete_bucket_req)
        except Exception as e:
            print(f"Warning: Cleanup failed: {e}")
