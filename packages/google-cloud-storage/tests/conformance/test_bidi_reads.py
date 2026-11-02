import io
import subprocess
import time
import traceback
import urllib
import uuid

import pytest
import requests
from google.api_core import client_options, exceptions

from google.cloud import _storage_v2 as storage_v2
from google.cloud.storage.asyncio.async_appendable_object_writer import (
    AsyncAppendableObjectWriter,
)
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from tests.conformance._utils import start_grpc_server

# --- Configuration ---


TEST_BENCH_ENDPOINT = (
    "http://localhost:9001"  # 9000 in VM is taken by test_conformance.py
)
_PORT = urllib.parse.urlsplit(TEST_BENCH_ENDPOINT).port
_GRPC_PORT = 8888

PROJECT_NUMBER = "12345"  # A dummy project number is fine for the testbench.
GRPC_ENDPOINT = f"localhost:{_GRPC_PORT}"
CONTENT_LENGTH = 1024 * 10  # 10 KB

_DEFAULT_IMAGE_NAME = "gcr.io/cloud-devrel-public-resources/storage-testbench"
_DEFAULT_IMAGE_TAG = "latest"
_DOCKER_IMAGE = f"{_DEFAULT_IMAGE_NAME}:{_DEFAULT_IMAGE_TAG}"
_PULL_CMD = ["docker", "pull", _DOCKER_IMAGE]
_RUN_CMD = [
    "docker",
    "run",
    "--name",
    "bidi_reads_container",
    "--rm",
    "-d",
    "-p",
    f"{_PORT}:9000",
    "-p",
    f"{_GRPC_PORT}:{_GRPC_PORT}",
    _DOCKER_IMAGE,
]
_DOCKER_STOP_CMD = [
    "docker",
    "stop",
    "bidi_reads_container",
]


@pytest.fixture(scope="module")
def testbench():
    subprocess.run(_PULL_CMD)
    proc = subprocess.Popen(_RUN_CMD)
    time.sleep(10)
    yield GRPC_ENDPOINT, TEST_BENCH_ENDPOINT
    subprocess.run(_DOCKER_STOP_CMD)
    proc.kill()


def _is_retriable(exc):
    """Predicate for identifying retriable errors."""
    return isinstance(
        exc,
        (
            exceptions.ServiceUnavailable,
            exceptions.Aborted,  # Required to retry on redirect
            exceptions.InternalServerError,
            exceptions.ResourceExhausted,
        ),
    )


async def run_test_scenario(http_client, bucket_name, object_name, scenario):
    """Runs a single fault-injection test scenario."""
    print(f"\n--- RUNNING SCENARIO: {scenario['name']} ---")

    retry_test_id = None
    try:
        # 1. Create a Retry Test resource on the testbench.
        retry_test_config = {
            "instructions": {scenario["method"]: [scenario["instruction"]]},
            "transport": "GRPC",
        }
        resp = http_client.post(
            f"{TEST_BENCH_ENDPOINT}/retry_test", json=retry_test_config
        )
        resp.raise_for_status()
        retry_test_id = resp.json()["id"]

        # 2. Set up downloader and metadata for fault injection.
        grpc_client = AsyncGrpcClient._create_insecure_grpc_client(
            client_options=client_options.ClientOptions(api_endpoint=GRPC_ENDPOINT),
        )
        downloader = await AsyncMultiRangeDownloader.create_mrd(
            grpc_client, bucket_name, object_name
        )
        fault_injection_metadata = (("x-retry-test-id", retry_test_id),)

        buffer = io.BytesIO()

        # 3. Execute the download and assert the outcome.
        try:
            await downloader.download_ranges(
                [(0, 5 * 1024, buffer), (6 * 1024, 4 * 1024, buffer)],
                metadata=fault_injection_metadata,
            )
            # If an exception was expected, this line should not be reached.
            if scenario["expected_error"] is not None:
                raise AssertionError(
                    f"Expected exception {scenario['expected_error']} was not raised."
                )

            assert len(buffer.getvalue()) == 9 * 1024

        except scenario["expected_error"] as e:
            print(f"Caught expected exception for {scenario['name']}: {e}")

        await downloader.close()

    finally:
        # 4. Clean up the Retry Test resource.
        if retry_test_id:
            http_client.delete(f"{TEST_BENCH_ENDPOINT}/retry_test/{retry_test_id}")


@pytest.mark.asyncio
async def test_bidi_reads(testbench):
    """Main function to set up resources and run all test scenarios."""
    grpc_endpoint, test_bench_endpoint = testbench
    print("starting grpc server", grpc_endpoint, test_bench_endpoint)
    start_grpc_server(
        grpc_endpoint, test_bench_endpoint
    )  # Ensure the testbench gRPC server is running before this test executes.

    grpc_client = AsyncGrpcClient._create_insecure_grpc_client(
        client_options=client_options.ClientOptions(api_endpoint=GRPC_ENDPOINT),
    )
    gapic_client = grpc_client.grpc_client
    http_client = requests.Session()

    bucket_name = f"grpc-test-bucket-{uuid.uuid4().hex[:8]}"
    object_name = "retry-test-object"

    # Define all test scenarios
    test_scenarios = [
        {
            "name": "Smarter Resumption: Retry 503 after partial data",
            "method": "storage.objects.get",
            "instruction": "return-broken-stream-after-2K",
            "expected_error": None,
        },
    ]

    try:
        # Create a single bucket and object for all tests to use.
        content = b"A" * CONTENT_LENGTH
        bucket_resource = storage_v2.Bucket(project=f"projects/{PROJECT_NUMBER}")
        create_bucket_request = storage_v2.CreateBucketRequest(
            parent="projects/_", bucket_id=bucket_name, bucket=bucket_resource
        )
        _ = await gapic_client.create_bucket(request=create_bucket_request)
        w = AsyncAppendableObjectWriter(grpc_client, bucket_name, object_name)
        await w.open()
        await w.append(content)
        _ = await w.close(finalize_on_close=True)

        # Run all defined test scenarios.
        for scenario in test_scenarios:
            await run_test_scenario(http_client, bucket_name, object_name, scenario)

        # Define and run test scenarios specifically for the open() method
        open_test_scenarios = [
            {
                "name": "Open: Retry on 503",
                "method": "storage.objects.get",
                "instruction": "return-503",
                "expected_error": None,
            },
            {
                "name": "Open: Retry on BidiReadObjectRedirectedError",
                "method": "storage.objects.get",
                "instruction": "redirect-send-handle-and-token-tokenval",
                "expected_error": None,
            },
            {
                "name": "Open: Fail Fast on 401",
                "method": "storage.objects.get",
                "instruction": "return-401",
                "expected_error": exceptions.Unauthorized,
            },
            {
                "name": "Retry on 500",
                "method": "storage.objects.get",
                "instruction": "return-500",
                "expected_error": None,
            },
            {
                "name": "Retry on 504",
                "method": "storage.objects.get",
                "instruction": "return-504",
                "expected_error": None,
            },
            {
                "name": "Retry on 429",
                "method": "storage.objects.get",
                "instruction": "return-429",
                "expected_error": None,
            },
        ]
        for scenario in open_test_scenarios:
            await run_open_test_scenario(
                http_client, bucket_name, object_name, scenario
            )

    except Exception as e:
        print(f"Test failed with error: {e}. Traceback: {traceback.format_exc()}")
        raise e
    finally:
        # Clean up the test bucket.
        try:
            delete_object_req = storage_v2.DeleteObjectRequest(
                bucket="projects/_/buckets/" + bucket_name, object=object_name
            )
            await gapic_client.delete_object(request=delete_object_req)

            delete_bucket_req = storage_v2.DeleteBucketRequest(
                name=f"projects/_/buckets/{bucket_name}"
            )
            await gapic_client.delete_bucket(request=delete_bucket_req)
        except Exception as e:
            print(f"Warning: Cleanup failed: {e}")


async def run_open_test_scenario(http_client, bucket_name, object_name, scenario):
    """Runs a fault-injection test scenario specifically for the open() method."""
    print(f"\n--- RUNNING OPEN SCENARIO: {scenario['name']} ---")

    retry_test_id = None
    try:
        # 1. Create a Retry Test resource on the testbench.
        retry_test_config = {
            "instructions": {scenario["method"]: [scenario["instruction"]]},
            "transport": "GRPC",
        }
        resp = http_client.post(
            f"{TEST_BENCH_ENDPOINT}/retry_test", json=retry_test_config
        )
        resp.raise_for_status()
        retry_test_id = resp.json()["id"]

        # 2. Set up metadata for fault injection.
        fault_injection_metadata = (("x-retry-test-id", retry_test_id),)

        # 3. Execute the open (via create_mrd) and assert the outcome.
        try:
            grpc_client = AsyncGrpcClient._create_insecure_grpc_client(
                client_options=client_options.ClientOptions(api_endpoint=GRPC_ENDPOINT),
            )
            downloader = await AsyncMultiRangeDownloader.create_mrd(
                grpc_client,
                bucket_name,
                object_name,
                metadata=fault_injection_metadata,
            )

            # If open was successful, perform a simple download to ensure the stream is usable.
            buffer = io.BytesIO()
            await downloader.download_ranges([(0, 1024, buffer)])
            await downloader.close()
            assert len(buffer.getvalue()) == 1024

            # If an exception was expected, this line should not be reached.
            if scenario["expected_error"] is not None:
                raise AssertionError(
                    f"Expected exception {scenario['expected_error']} was not raised."
                )

        except scenario["expected_error"] as e:
            print(f"Caught expected exception for {scenario['name']}: {e}")

    finally:
        # 4. Clean up the Retry Test resource.
        if retry_test_id:
            http_client.delete(f"{TEST_BENCH_ENDPOINT}/retry_test/{retry_test_id}")
