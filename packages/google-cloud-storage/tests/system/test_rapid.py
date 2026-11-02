"""System tests for Rapid Buckets and RCU.

Usage:

RUN_RCU_SYSTEM_TESTS=True RCU_BUCKET=<bucket_name> RUN_SYSTEM_TESTS_ON_PREPROD=True pytest packages/google-cloud-storage/tests/system/test_rapid.py

and for Rapid Buckets:

RUN_RAPID_SYSTEM_TESTS=True RAPID_BUCKET=<> CROSS_REGION_BUCKET=<> pytest packages/google-cloud-storage/tests/system/test_rapid.py
"""

# py standard imports
import asyncio
import datetime
import gc
import os
import random
import uuid
from io import BytesIO

# python additional imports
import google_crc32c
import pytest
from google.api_core import exceptions
from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import FailedPrecondition, NotFound, OutOfRange

from google.cloud import kms
from google.cloud.storage._helpers import _parse_bool_env
from google.cloud.storage.asyncio.async_appendable_object_writer import (
    _DEFAULT_FLUSH_INTERVAL_BYTES,
    AsyncAppendableObjectWriter,
)
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from google.cloud.storage.blob import (
    ObjectContexts,
    ObjectCustomContextPayload,
)

PREPROD_GRPC_ENDPOINT = "storage-preprod-test-grpc.googleusercontent.com:443"
# Run system test for either Rapid or RCU. But not both => XOR
pytestmark = pytest.mark.skipif(
    not (
        _parse_bool_env("RUN_RAPID_SYSTEM_TESTS", default=False)
        ^ _parse_bool_env("RUN_RCU_SYSTEM_TESTS", default=False)
    ),
    reason="Any one of Rapid or RCU system tests need to be explicitly enabled. This helps scheduling tests in Kokoro and Cloud Build.",
)


# TODO: replace this with a fixture once rapid bucket creation / deletion
# is supported in grpc client or json client.
_RAPID_BUCKET = os.getenv("RAPID_BUCKET")
_CROSS_REGION_BUCKET = os.getenv("CROSS_REGION_BUCKET")
_BYTES_TO_UPLOAD = b"dummy_bytes_to_write_read_and_delete_appendable_object"

RCU_SYSTEM_TESTS = _parse_bool_env("RUN_RCU_SYSTEM_TESTS", default=False)
_RCU_BUCKET = os.getenv("RCU_BUCKET")
_BUCKET_UNDER_TEST = _RCU_BUCKET if RCU_SYSTEM_TESTS else _RAPID_BUCKET


async def create_async_grpc_client(attempt_direct_path=True, preprod=False):
    """Initializes async client and gets the current event loop."""
    return AsyncGrpcClient(
        attempt_direct_path=attempt_direct_path,
        client_options=ClientOptions(api_endpoint=PREPROD_GRPC_ENDPOINT)
        if preprod
        else None,
    )


@pytest.fixture(scope="session")
def rapid_kms_key(storage_client, kms_client):
    """Provisions a KMS key in the same location as of the rapid bucket."""
    # Get the rapid bucket and extract its location
    bucket = storage_client.get_bucket(_BUCKET_UNDER_TEST)
    location = bucket.location.lower()

    project = storage_client.project
    # Keep legacy "zonal" naming to reuse existing KMS resources in the test project.
    keyring_name = "gcs-test-zonal-ring"
    key_name = "gcs-test-zonal-key"

    keyring_path = kms_client.key_ring_path(project, location, keyring_name)

    # Create the KeyRing if it doesn't exist
    try:
        kms_client.get_key_ring(name=keyring_path)
    except NotFound:
        parent = f"projects/{project}/locations/{location}"
        kms_client.create_key_ring(
            request={"parent": parent, "key_ring_id": keyring_name, "key_ring": {}}
        )

        # Grant GCS service account permissions to use the key
        service_account_email = storage_client.get_service_account_email()
        policy = {
            "bindings": [
                {
                    "role": "roles/cloudkms.cryptoKeyEncrypterDecrypter",
                    "members": [f"serviceAccount:{service_account_email}"],
                }
            ]
        }
        kms_client.set_iam_policy(request={"resource": keyring_path, "policy": policy})

    # Create the CryptoKey if it doesn't exist
    key_path = kms_client.crypto_key_path(project, location, keyring_name, key_name)
    try:
        kms_client.get_crypto_key(name=key_path)
    except NotFound:
        purpose = kms.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT
        key = {"purpose": purpose}
        kms_client.create_crypto_key(
            request={
                "parent": keyring_path,
                "crypto_key_id": key_name,
                "crypto_key": key,
            }
        )

    return key_path


@pytest.fixture(scope="session")
def event_loop():
    """Redefine pytest-asyncio's event_loop fixture to be session-scoped."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def grpc_clients(event_loop, run_system_tests_on_preprod):
    # grpc clients has to be instantiated in the event loop,
    # otherwise grpc creates it's own event loop and attaches to the client.
    # Which will lead to deadlock because client running in one event loop and
    # MRD or Appendable-Writer in another.
    # https://github.com/grpc/grpc/blob/61fe9b40a986792ab7d4eb8924027b671faf26ba/src/python/grpcio/grpc/aio/_channel.py#L369
    # https://github.com/grpc/grpc/blob/61fe9b40a986792ab7d4eb8924027b671faf26ba/src/python/grpcio/grpc/_cython/_cygrpc/aio/common.pyx.pxi#L249
    clients = {
        True: event_loop.run_until_complete(
            create_async_grpc_client(
                attempt_direct_path=True, preprod=run_system_tests_on_preprod
            )
        ),
        False: event_loop.run_until_complete(
            create_async_grpc_client(
                attempt_direct_path=False, preprod=run_system_tests_on_preprod
            )
        ),
    }
    return clients


# This fixture is for tests that are NOT parametrized by attempt_direct_path
@pytest.fixture
def grpc_client(grpc_clients):
    return grpc_clients[False]


@pytest.fixture
def grpc_client_direct(grpc_clients):
    return grpc_clients[True]


def _get_equal_dist(a: int, b: int) -> tuple[int, int]:
    step = (b - a) // 3
    return a + step, a + 2 * step


@pytest.mark.skipif(
    RCU_SYSTEM_TESTS, reason="X regions reads/writes for RCU not supported in SDK yet"
)
@pytest.mark.parametrize(
    "object_size",
    [
        256,  # less than _chunk size
        10 * 1024 * 1024,  # less than _MAX_BUFFER_SIZE_BYTES
        20 * 1024 * 1024,  # greater than _MAX_BUFFER_SIZE
    ],
)
def test_basic_wrd_x_region(
    storage_client,
    blobs_to_delete,
    object_size,
    event_loop,
    grpc_client,
):
    object_name = f"test_basic_wrd-{str(uuid.uuid4())}"

    async def _run():
        object_data = os.urandom(object_size)
        object_checksum = google_crc32c.value(object_data)

        writer = AsyncAppendableObjectWriter(
            grpc_client, _CROSS_REGION_BUCKET, object_name
        )
        await writer.open()
        await writer.append(object_data)
        object_metadata = await writer.close(finalize_on_close=True)
        assert object_metadata.size == object_size
        assert int(object_metadata.checksums.crc32c) == object_checksum

        buffer = BytesIO()
        mrd = AsyncMultiRangeDownloader(grpc_client, _CROSS_REGION_BUCKET, object_name)
        async with mrd:
            assert mrd._open_retries == 1
            # (0, 0) means read the whole object
            await mrd.download_ranges([(0, 0, buffer)])
            assert mrd.persisted_size == object_size

        assert buffer.getvalue() == object_data

        # Clean up; use json client (i.e. `storage_client` fixture) to delete.
        blobs_to_delete.append(
            storage_client.bucket(_CROSS_REGION_BUCKET).blob(object_name)
        )
        del writer
        gc.collect()

    event_loop.run_until_complete(_run())


@pytest.mark.parametrize(
    "object_size",
    [
        256,  # less than _chunk size
        10 * 1024 * 1024,  # less than _MAX_BUFFER_SIZE_BYTES
        20 * 1024 * 1024,  # greater than _MAX_BUFFER_SIZE
    ],
)
@pytest.mark.parametrize(
    "attempt_direct_path",
    [True, False],
)
def test_basic_wrd(
    storage_client,
    blobs_to_delete,
    attempt_direct_path,
    object_size,
    event_loop,
    grpc_clients,
):
    object_name = f"test_basic_wrd-{str(uuid.uuid4())}"

    async def _run():
        object_data = os.urandom(object_size)
        object_checksum = google_crc32c.value(object_data)
        grpc_client = grpc_clients[attempt_direct_path]
        writer = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(object_data)
        object_metadata = await writer.close(finalize_on_close=True)
        assert object_metadata.size == object_size
        assert int(object_metadata.checksums.crc32c) == object_checksum

        buffer = BytesIO()
        async with AsyncMultiRangeDownloader(
            grpc_client, _BUCKET_UNDER_TEST, object_name
        ) as mrd:
            # (0, 0) means read the whole object
            await mrd.download_ranges([(0, 0, buffer)])
            assert mrd.persisted_size == object_size

        assert buffer.getvalue() == object_data

        # Clean up; use json client (i.e. `storage_client` fixture) to delete.
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )
        del writer
        gc.collect()

    event_loop.run_until_complete(_run())


@pytest.mark.parametrize(
    "object_size",
    [
        10,  # less than _chunk size,
        10 * 1024 * 1024,  # less than _MAX_BUFFER_SIZE_BYTES
        20 * 1024 * 1024,  # greater than _MAX_BUFFER_SIZE_BYTES
    ],
)
def test_basic_wrd_in_slices(
    storage_client, blobs_to_delete, object_size, event_loop, grpc_client
):
    object_name = f"test_basic_wrd-{str(uuid.uuid4())}"

    async def _run():
        object_data = os.urandom(object_size)
        object_checksum = google_crc32c.value(object_data)

        writer = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        mark1, mark2 = _get_equal_dist(0, object_size)
        await writer.append(object_data[0:mark1])
        await writer.append(object_data[mark1:mark2])
        await writer.append(object_data[mark2:])
        object_metadata = await writer.close(finalize_on_close=True)
        assert object_metadata.size == object_size
        assert int(object_metadata.checksums.crc32c) == object_checksum

        mrd = AsyncMultiRangeDownloader(grpc_client, _BUCKET_UNDER_TEST, object_name)
        buffer = BytesIO()
        await mrd.open()
        # (0, 0) means read the whole object
        await mrd.download_ranges([(0, 0, buffer)])
        await mrd.close()
        assert buffer.getvalue() == object_data
        assert mrd.persisted_size == object_size

        # Clean up; use json client (i.e. `storage_client` fixture) to delete.
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )
        del writer
        del mrd
        gc.collect()

    event_loop.run_until_complete(_run())


@pytest.mark.parametrize(
    "flush_interval",
    [
        2 * 1024 * 1024,
        4 * 1024 * 1024,
        8 * 1024 * 1024,
        _DEFAULT_FLUSH_INTERVAL_BYTES,
    ],
)
def test_wrd_with_non_default_flush_interval(
    storage_client,
    blobs_to_delete,
    flush_interval,
    event_loop,
    grpc_client,
):
    object_name = f"test_basic_wrd-{str(uuid.uuid4())}"
    object_size = 9 * 1024 * 1024

    async def _run():
        object_data = os.urandom(object_size)
        object_checksum = google_crc32c.value(object_data)

        writer = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
            writer_options={"FLUSH_INTERVAL_BYTES": flush_interval},
        )
        await writer.open()
        mark1, mark2 = _get_equal_dist(0, object_size)
        await writer.append(object_data[0:mark1])
        await writer.append(object_data[mark1:mark2])
        await writer.append(object_data[mark2:])
        object_metadata = await writer.close(finalize_on_close=True)
        assert object_metadata.size == object_size
        assert int(object_metadata.checksums.crc32c) == object_checksum

        mrd = AsyncMultiRangeDownloader(grpc_client, _BUCKET_UNDER_TEST, object_name)
        buffer = BytesIO()
        await mrd.open()
        # (0, 0) means read the whole object
        await mrd.download_ranges([(0, 0, buffer)])
        await mrd.close()
        assert buffer.getvalue() == object_data
        assert mrd.persisted_size == object_size

        # Clean up; use json client (i.e. `storage_client` fixture) to delete.
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )
        del writer
        del mrd
        gc.collect()

    event_loop.run_until_complete(_run())


@pytest.mark.skipif(
    RCU_SYSTEM_TESTS, reason="Write from blob for RCU not supported in SDK yet"
)
def test_write_from_blob(
    storage_client,
    blobs_to_delete,
    event_loop,
    grpc_client,
):
    object_name = f"test_from_blob-{str(uuid.uuid4())[:4]}"
    content_type = "text/plain"
    metadata = {"environment": "system-test"}
    cache_control = "public, max-age=3600"
    content_disposition = "attachment; filename=test.txt"
    content_encoding = "identity"
    content_language = "en"
    custom_time = datetime.datetime(2025, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    test_data = b"system-test-data"

    async def _run():
        # 1. Create a Blob instance
        blob = storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        blob.content_type = content_type
        blob.metadata = metadata
        blob.cache_control = cache_control
        blob.content_disposition = content_disposition
        blob.content_encoding = content_encoding
        blob.content_language = content_language
        blob.custom_time = custom_time
        if RCU_SYSTEM_TESTS:
            blob.storage_class = "RAPID"

        # 2. Use from_blob to create the writer
        writer = AsyncAppendableObjectWriter.from_blob(grpc_client, blob)
        await writer.open()
        await writer.append(test_data)
        await writer.close(finalize_on_close=True)

        # 3. Verify the object metadata
        obj = await grpc_client.get_object(
            bucket_name=_BUCKET_UNDER_TEST,
            object_name=object_name,
        )

        assert obj.content_type == content_type
        assert obj.metadata["environment"] == "system-test"
        assert obj.cache_control == cache_control
        assert obj.content_disposition == content_disposition
        assert obj.content_encoding == content_encoding
        assert obj.content_language == content_language
        assert int(obj.custom_time.timestamp()) == int(custom_time.timestamp())

        blobs_to_delete.append(blob)

    event_loop.run_until_complete(_run())


@pytest.mark.skipif(
    RCU_SYSTEM_TESTS,
    reason="Write from blob with KMS key for RCU not supported in SDK yet",
)
def test_write_from_blob_with_kms_key(
    storage_client,
    blobs_to_delete,
    event_loop,
    grpc_client,
    rapid_kms_key,
):
    """Verifies AsyncAppendableObjectWriter.from_blob correctly applies KMS encryption."""

    object_name = f"test_from_blob_kms-{str(uuid.uuid4())[:4]}"
    test_data = b"kms-protected-data"

    async def _run():
        # Create a local Blob instance with the KMS key
        blob = storage_client.bucket(_BUCKET_UNDER_TEST).blob(
            object_name, kms_key_name=rapid_kms_key
        )

        writer = AsyncAppendableObjectWriter.from_blob(grpc_client, blob)

        await writer.open()
        await writer.append(test_data)

        await writer.close(finalize_on_close=True)

        # Verify the encryption metadata
        obj = await grpc_client.get_object(
            bucket_name=_BUCKET_UNDER_TEST,
            object_name=object_name,
        )

        # Assert that the object was encrypted with the correct key
        # GCS appends a version suffix, so we use startswith()
        assert obj.kms_key.startswith(rapid_kms_key)

        blobs_to_delete.append(blob)

    event_loop.run_until_complete(_run())


def test_write_blob_with_contexts(
    event_loop, grpc_client_direct, storage_client, blobs_to_delete
):
    async def _run():
        bucket = storage_client.bucket(_BUCKET_UNDER_TEST)
        blob_name = f"ObjectContextsGrpc-{uuid.uuid4().hex}"
        blob = bucket.blob(blob_name)
        blob.contexts = ObjectContexts(
            blob, custom={"foo": ObjectCustomContextPayload(value="bar")}
        )
        if RCU_SYSTEM_TESTS:
            blob.storage_class = "RAPID"

        writer = AsyncAppendableObjectWriter.from_blob(grpc_client_direct, blob)
        await writer.open()
        await writer.append(b"grpc-test")
        await writer.close(finalize_on_close=True)

        try:
            blobs = list(
                storage_client.list_blobs(
                    _BUCKET_UNDER_TEST, filter_='contexts."foo"="bar"'
                )
            )
            names = [b.name for b in blobs]
            assert blob_name in names

            # Assert contexts via gRPC GetObject
            obj_proto = await grpc_client_direct.get_object(
                _BUCKET_UNDER_TEST, blob_name
            )
            assert "foo" in obj_proto.contexts.custom
            assert obj_proto.contexts.custom["foo"].value == "bar"
        finally:
            blobs_to_delete.append(
                storage_client.bucket(_BUCKET_UNDER_TEST).blob(blob_name)
            )

    event_loop.run_until_complete(_run())


def test_read_unfinalized_appendable_object(
    storage_client, blobs_to_delete, event_loop, grpc_client_direct
):
    object_name = f"read_unfinalized_appendable_object-{str(uuid.uuid4())[:4]}"

    async def _run():
        grpc_client = grpc_client_direct
        writer = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(_BYTES_TO_UPLOAD)
        await writer.flush()

        mrd = AsyncMultiRangeDownloader(grpc_client, _BUCKET_UNDER_TEST, object_name)
        buffer = BytesIO()
        await mrd.open()
        assert mrd.persisted_size == len(_BYTES_TO_UPLOAD)
        # (0, 0) means read the whole object
        await mrd.download_ranges([(0, 0, buffer)])
        await mrd.close()
        assert buffer.getvalue() == _BYTES_TO_UPLOAD

        # Clean up; use json client (i.e. `storage_client` fixture) to delete.
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )
        del writer
        del mrd
        gc.collect()

    event_loop.run_until_complete(_run())


@pytest.mark.skip(reason="Flaky test b/478129078")
def test_mrd_open_with_read_handle(event_loop, grpc_client_direct):
    object_name = f"test_read_handl-{str(uuid.uuid4())[:4]}"

    async def _run():
        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(_BYTES_TO_UPLOAD)
        await writer.close()

        mrd = AsyncMultiRangeDownloader(
            grpc_client_direct, _BUCKET_UNDER_TEST, object_name
        )
        await mrd.open()
        read_handle = mrd.read_handle
        await mrd.close()

        # Open a new MRD using the `read_handle` obtained above
        new_mrd = AsyncMultiRangeDownloader(
            grpc_client_direct, _BUCKET_UNDER_TEST, object_name, read_handle=read_handle
        )
        await new_mrd.open()
        # persisted_size not set when opened with read_handle
        assert new_mrd.persisted_size is None
        buffer = BytesIO()
        await new_mrd.download_ranges([(0, 0, buffer)])
        await new_mrd.close()
        assert buffer.getvalue() == _BYTES_TO_UPLOAD
        del mrd
        del new_mrd
        gc.collect()

    event_loop.run_until_complete(_run())


def test_mrd_open_with_read_handle_over_cloud_path(event_loop, grpc_client):
    object_name = f"test_read_handl-{str(uuid.uuid4())[:4]}"

    async def _run():
        writer = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(_BYTES_TO_UPLOAD)
        await writer.close()

        mrd = AsyncMultiRangeDownloader(grpc_client, _BUCKET_UNDER_TEST, object_name)
        await mrd.open()
        read_handle = mrd.read_handle
        await mrd.close()

        # Open a new MRD using the `read_handle` obtained above
        new_mrd = AsyncMultiRangeDownloader(
            grpc_client, _BUCKET_UNDER_TEST, object_name, read_handle=read_handle
        )
        await new_mrd.open()
        # persisted_size is set regardless of whether we use read_handle or not
        # because read_handle won't work in CLOUD_PATH.
        assert new_mrd.persisted_size == len(_BYTES_TO_UPLOAD)
        buffer = BytesIO()
        await new_mrd.download_ranges([(0, 0, buffer)])
        await new_mrd.close()
        assert buffer.getvalue() == _BYTES_TO_UPLOAD
        del mrd
        del new_mrd
        gc.collect()

    event_loop.run_until_complete(_run())


def test_wrd_open_with_write_handle(
    event_loop, grpc_client_direct, storage_client, blobs_to_delete
):
    object_name = f"test_write_handl-{str(uuid.uuid4())[:4]}"

    async def _run():
        # 1. Create an object and get its write_handle
        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        write_handle = writer.write_handle
        await writer.close()

        # 2. Open a new writer using the obtained `write_handle` and generation
        new_writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            write_handle=write_handle,
            generation=writer.generation,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await new_writer.open()
        # Verify that the new writer is open and has the same write_handle
        assert new_writer.is_stream_open
        assert new_writer.generation == writer.generation

        # 3. Append some data using the new writer
        test_data = b"data_from_new_writer"
        await new_writer.append(test_data)
        await new_writer.close()

        # 4. Verify the data was written correctly by reading it back
        mrd = AsyncMultiRangeDownloader(
            grpc_client_direct, _BUCKET_UNDER_TEST, object_name
        )
        buffer = BytesIO()
        await mrd.open()
        await mrd.download_ranges([(0, 0, buffer)])
        await mrd.close()
        assert buffer.getvalue() == test_data

        # Clean up
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )
        del writer
        del new_writer
        del mrd
        gc.collect()

    event_loop.run_until_complete(_run())


def test_read_unfinalized_appendable_object_with_generation(
    storage_client, blobs_to_delete, event_loop, grpc_client_direct
):
    object_name = f"read_unfinalized_appendable_object-{str(uuid.uuid4())[:4]}"
    grpc_client = grpc_client_direct

    async def _run():
        async def _read_and_verify(expected_content, generation=None):
            """Helper to read object content and verify against expected."""
            mrd = AsyncMultiRangeDownloader(
                grpc_client, _BUCKET_UNDER_TEST, object_name, generation
            )
            buffer = BytesIO()
            await mrd.open()
            try:
                assert mrd.persisted_size == len(expected_content)
                await mrd.download_ranges([(0, 0, buffer)])
                assert buffer.getvalue() == expected_content
            finally:
                await mrd.close()
            return mrd

        # First write
        writer = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(_BYTES_TO_UPLOAD)
        await writer.flush()
        generation = writer.generation

        # First read
        mrd = await _read_and_verify(_BYTES_TO_UPLOAD)

        # Second write, using generation from the first write.
        writer_2 = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            generation=generation,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer_2.open()
        await writer_2.append(_BYTES_TO_UPLOAD)
        await writer_2.flush()

        # Second read
        mrd_2 = await _read_and_verify(_BYTES_TO_UPLOAD + _BYTES_TO_UPLOAD, generation)

        # Clean up
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )
        del writer
        del writer_2
        del mrd
        del mrd_2
        gc.collect()

    event_loop.run_until_complete(_run())


def test_open_with_generation_zero(
    storage_client, blobs_to_delete, event_loop, grpc_client
):
    """Tests that using `generation=0` fails if the object already exists.

    This test verifies that:
    1. An object can be created using `AsyncAppendableObjectWriter` with `generation=0`.
    2. Attempting to create the same object again with `generation=0` raises a
       `FailedPrecondition` error with a 400 status code, because the
       precondition (object must not exist) is not met.
    """
    object_name = f"test_append_with_generation-{uuid.uuid4()}"

    async def _run():
        writer = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            generation=0,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )

        # Empty object is created.
        await writer.open()
        assert writer.is_stream_open

        await writer.close()
        assert not writer.is_stream_open

        with pytest.raises(FailedPrecondition) as exc_info:
            writer_fail = AsyncAppendableObjectWriter(
                grpc_client,
                _BUCKET_UNDER_TEST,
                object_name,
                generation=0,
                storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
            )
            await writer_fail.open()
        assert exc_info.value.code == 400

        # cleanup
        del writer
        gc.collect()

        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )

    event_loop.run_until_complete(_run())


def test_open_existing_object_with_gen_None_overrides_existing(
    storage_client, blobs_to_delete, event_loop, grpc_client
):
    """
    Test that a new writer when specifies `None` overrides the existing object.
    """
    object_name = f"test_append_with_generation-{uuid.uuid4()}"

    async def _run():
        writer = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            generation=0,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )

        # Empty object is created.
        await writer.open()
        assert writer.is_stream_open
        old_gen = writer.generation

        await writer.close()
        assert not writer.is_stream_open

        new_writer = AsyncAppendableObjectWriter(
            grpc_client,
            _BUCKET_UNDER_TEST,
            object_name,
            generation=None,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await new_writer.open()
        assert new_writer.generation != old_gen

        # cleanup
        del writer
        del new_writer
        gc.collect()

        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )

    event_loop.run_until_complete(_run())


def test_delete_object_using_grpc_client(event_loop, grpc_client_direct):
    """
    Test that a new writer when specifies `None` overrides the existing object.
    """
    object_name = f"test_append_with_generation-{uuid.uuid4()}"

    async def _run():
        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            generation=0,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )

        # Empty object is created.
        await writer.open()
        await writer.append(b"some_bytes")
        await writer.close()

        await grpc_client_direct.delete_object(_BUCKET_UNDER_TEST, object_name)

        # trying to get raises raises 404.
        with pytest.raises(NotFound):
            # TODO: Remove this once GET_OBJECT is exposed in `AsyncGrpcClient`
            await grpc_client_direct._grpc_client.get_object(
                bucket=f"projects/_/buckets/{_BUCKET_UNDER_TEST}", object_=object_name
            )
        # cleanup
        del writer
        gc.collect()

    event_loop.run_until_complete(_run())


@pytest.mark.parametrize(
    "ranges_desc, chunk_ranges",
    [
        ("small", [(1, 100)] * 3),
        ("medium", [(100, 100000)] * 3),
        ("large", [(1000000, 2000000)] * 3),
        ("mixed", [(1, 100), (100, 100000), (1000000, 2000000)]),
    ],
)
def test_mrd_concurrent_download(
    storage_client,
    blobs_to_delete,
    event_loop,
    grpc_client_direct,
    ranges_desc,
    chunk_ranges,
):
    """
    Test that mrd can handle concurrent `download_ranges` calls correctly.
    Tests overlapping ranges, minimal concurrency,
    parametrized chunk sizes (small/medium/large/mixed), and full object fetching alongside specific chunks.
    """
    object_size = 15 * 1024 * 1024  # 15MB
    object_name = f"test_mrd_concurrent-{uuid.uuid4()}"

    async def _run():
        object_data = os.urandom(object_size)

        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(object_data)
        await writer.close(finalize_on_close=True)

        async with AsyncMultiRangeDownloader(
            grpc_client_direct, _BUCKET_UNDER_TEST, object_name
        ) as mrd:
            tasks = []
            ranges_to_fetch = []

            for min_len, max_len in chunk_ranges:
                start = random.randint(0, object_size - max_len)
                length = random.randint(min_len, max_len)
                ranges_to_fetch.append((start, length))

            # Full object fetching concurrently
            ranges_to_fetch.append((0, 0))

            random.shuffle(ranges_to_fetch)

            buffers = [BytesIO() for _ in range(len(ranges_to_fetch))]

            for idx, (start, length) in enumerate(ranges_to_fetch):
                tasks.append(
                    asyncio.create_task(
                        mrd.download_ranges([(start, length, buffers[idx])])
                    )
                )

            await asyncio.gather(*tasks)

            # Validation
            for idx, (start, length) in enumerate(ranges_to_fetch):
                if length == 0:
                    expected_data = object_data[start:]
                else:
                    expected_data = object_data[start : start + length]
                assert buffers[idx].getvalue() == expected_data

        del writer
        gc.collect()
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )

    event_loop.run_until_complete(_run())


def test_mrd_concurrent_download_cancellation(
    storage_client, blobs_to_delete, event_loop, grpc_client_direct
):
    """
    Test task cancellation / abort mid-stream.
    Tests that downloading gracefully manages memory and internal references
    when tasks are canceled during active multiplexing, without breaking remaining downloads.
    """
    object_size = 20 * 1024 * 1024  # 20MB
    object_name = f"test_mrd_cancel-{uuid.uuid4()}"

    async def _run():
        object_data = os.urandom(object_size)

        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(object_data)
        await writer.close(finalize_on_close=True)

        async with AsyncMultiRangeDownloader(
            grpc_client_direct, _BUCKET_UNDER_TEST, object_name
        ) as mrd:
            tasks = []
            num_chunks = 40
            chunk_size = object_size // num_chunks
            buffers = [BytesIO() for _ in range(num_chunks)]

            for i in range(num_chunks):
                start = i * chunk_size
                tasks.append(
                    asyncio.create_task(
                        mrd.download_ranges([(start, chunk_size, buffers[i])])
                    )
                )

            # Yield control to event loop so tasks send Bidi requests, but do not wait for server responses
            await asyncio.sleep(0)

            # Cancel a subset of evenly distributed tasks
            for i in range(0, num_chunks, 2):
                tasks[i].cancel()

            results = await asyncio.gather(*tasks, return_exceptions=True)

            for i in range(num_chunks):
                if i % 2 == 0:
                    assert isinstance(results[i], asyncio.CancelledError)
                else:
                    start = i * chunk_size
                    expected_data = object_data[start : start + chunk_size]
                    assert buffers[i].getvalue() == expected_data

        del writer
        gc.collect()
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )

    event_loop.run_until_complete(_run())


def test_mrd_concurrent_download_out_of_bounds(
    storage_client, blobs_to_delete, event_loop, grpc_client_direct
):
    """
    Test out-of-bounds & edge ranges concurrent with valid requests.
    Verifies isolation: invalid bounds generate correct exceptions and don't stall the stream
    for concurrently valid requests.
    """
    object_size = 2 * 1024 * 1024  # 2MB
    object_name = f"test_mrd_oob-{uuid.uuid4()}"

    async def _run():
        object_data = os.urandom(object_size)

        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(object_data)
        await writer.close(finalize_on_close=True)

        async with AsyncMultiRangeDownloader(
            grpc_client_direct, _BUCKET_UNDER_TEST, object_name
        ) as mrd:
            valid_buffer = BytesIO()
            valid_task = asyncio.create_task(
                mrd.download_ranges([(0, 100, valid_buffer)])
            )

            oob_buffer = BytesIO()
            oob_task = asyncio.create_task(
                mrd.download_ranges([(object_size + 1000, 100, oob_buffer)])
            )

            results = await asyncio.gather(valid_task, oob_task, return_exceptions=True)

            # Verify valid one processed correctly
            assert valid_buffer.getvalue() == object_data[:100]

            # Verify fully OOB request returned Exception
            assert isinstance(results[1], OutOfRange)

        del writer
        gc.collect()
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )

    event_loop.run_until_complete(_run())


@pytest.mark.parametrize(
    "read_start, read_length, enable_checksum",
    [
        (0, 0, True),
        (0, 1024 * 1024, True),
        (0, 0, False),
    ],
)
def test_mrd_checksum_validation(
    storage_client,
    blobs_to_delete,
    event_loop,
    grpc_client_direct,
    read_start,
    read_length,
    enable_checksum,
):
    """
    Tests full downloads with specified offset, length, and enable_checksum toggle on finalized objects.
    """
    object_size = 1024 * 1024  # 1MB
    object_name = f"test_mrd_chksum-{uuid.uuid4()}"

    async def _run():
        object_data = os.urandom(object_size)

        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(object_data)
        await writer.close(finalize_on_close=True)

        async with AsyncMultiRangeDownloader(
            grpc_client_direct, _BUCKET_UNDER_TEST, object_name
        ) as mrd:
            buffer = BytesIO()
            await mrd.download_ranges(
                [(read_start, read_length, buffer)], enable_checksum=enable_checksum
            )
            assert buffer.getvalue() == object_data

        # cleanup
        del writer
        gc.collect()
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )

    event_loop.run_until_complete(_run())


def test_mrd_checksum_unfinalized_appendable_skipped(
    storage_client, blobs_to_delete, event_loop, grpc_client_direct
):
    """
    Verifies that live, unfinalized appendable objects skip the full-object checksum check
    naturally without raising any exceptions.
    """
    object_name = f"test_mrd_chksum_unfin-{uuid.uuid4()}"

    async def _run():
        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(_BYTES_TO_UPLOAD)
        await writer.flush()  # Flushed but not finalized!

        # Download the unfinalized appendable object with enable_checksum=True
        async with AsyncMultiRangeDownloader(
            grpc_client_direct, _BUCKET_UNDER_TEST, object_name
        ) as mrd:
            buffer = BytesIO()
            # Since it's unfinalized, it should skip the checksum check without raising
            await mrd.download_ranges([(0, 0, buffer)], enable_checksum=True)
            assert buffer.getvalue() == _BYTES_TO_UPLOAD

        # cleanup
        await writer.close()
        del writer
        gc.collect()
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )

    event_loop.run_until_complete(_run())


def test_finalize_with_correct_checksum(
    storage_client,
    blobs_to_delete,
    event_loop,
    grpc_client_direct,
):
    object_name = f"appendable_checksum_success_{uuid.uuid4()}"
    object_data = b"Hello, appendable object with correct checksum!"
    object_checksum = google_crc32c.value(object_data)

    async def _run():
        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(object_data)
        object_metadata = await writer.finalize(full_object_checksum=object_checksum)

        assert object_metadata.size == len(object_data)
        assert int(object_metadata.checksums.crc32c) == object_checksum

        # clean up
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )
        del writer
        gc.collect()

    event_loop.run_until_complete(_run())


def test_finalize_with_incorrect_checksum_fails(
    storage_client,
    blobs_to_delete,
    event_loop,
    grpc_client_direct,
):
    object_name = f"appendable_checksum_fail_{uuid.uuid4()}"
    object_data = b"Hello, appendable object with incorrect checksum!"
    object_checksum = google_crc32c.value(object_data)
    incorrect_checksum = object_checksum + 1

    async def _run():
        writer = AsyncAppendableObjectWriter(
            grpc_client_direct,
            _BUCKET_UNDER_TEST,
            object_name,
            storage_class="RAPID" if RCU_SYSTEM_TESTS else None,
        )
        await writer.open()
        await writer.append(object_data)

        # Finalization should fail with an exception due to mismatch
        with pytest.raises(exceptions.InvalidArgument) as excinfo:
            await writer.finalize(full_object_checksum=incorrect_checksum)

        # Assert that the error relates to checksum verification/mismatch
        error_msg = str(excinfo.value).lower()
        assert (
            "crc32c" in error_msg or "checksum" in error_msg or "mismatch" in error_msg
        )

        # clean up
        blobs_to_delete.append(
            storage_client.bucket(_BUCKET_UNDER_TEST).blob(object_name)
        )
        del writer
        gc.collect()

    event_loop.run_until_complete(_run())
