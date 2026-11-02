# Copyright 2025 Google LLC
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

import datetime
import unittest.mock as mock
from unittest.mock import AsyncMock, MagicMock

import grpc
import pytest

from google.cloud import _storage_v2
from google.cloud.storage import Blob, Bucket
from google.cloud.storage.asyncio.async_write_object_stream import (
    _AsyncWriteObjectStream,
)
from google.cloud.storage.blob import ObjectContexts, ObjectCustomContextPayload

BUCKET = "my-bucket"
OBJECT = "my-object"
GENERATION = 12345
WRITE_HANDLE = b"test-handle"
FULL_BUCKET_PATH = f"projects/_/buckets/{BUCKET}"


@pytest.fixture
def mock_client():
    """Fixture to provide a mock gRPC client."""
    client = MagicMock()
    # Mocking transport internal structures
    mock_transport = MagicMock()
    mock_transport.bidi_write_object = mock.sentinel.bidi_write_object
    mock_transport._wrapped_methods = {
        mock.sentinel.bidi_write_object: mock.sentinel.wrapped_bidi_write_object
    }
    client._client._transport = mock_transport
    return client


class TestAsyncWriteObjectStream:
    """Test suite for AsyncWriteObjectStream."""

    # -------------------------------------------------------------------------
    # Initialization Tests
    # -------------------------------------------------------------------------

    def test_init_basic(self, mock_client):
        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT)
        assert stream.bucket_name == BUCKET
        assert stream.object_name == OBJECT
        assert stream._full_bucket_name == FULL_BUCKET_PATH
        assert stream.metadata == (
            ("x-goog-request-params", f"bucket={FULL_BUCKET_PATH}"),
        )
        assert not stream.is_stream_open
        assert stream.storage_class is None

    @pytest.mark.parametrize("storage_class", ["STANDARD", "RAPID"])
    def test_init_with_storage_class(self, mock_client, storage_class):
        stream = _AsyncWriteObjectStream(
            mock_client, BUCKET, OBJECT, storage_class=storage_class
        )
        assert stream.storage_class == storage_class

    @pytest.mark.parametrize("storage_class", ["STANDARD", "RAPID"])
    def test_init_with_blob_storage_class(self, mock_client, storage_class):
        mock_blob = mock.Mock(spec=Blob)
        mock_blob.name = OBJECT
        mock_blob.bucket = mock.Mock(spec=Bucket)
        mock_blob.bucket.name = BUCKET
        mock_blob.storage_class = storage_class

        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT, blob=mock_blob)
        assert stream.blob.storage_class == storage_class

    def test_init_raises_value_error(self, mock_client):
        with pytest.raises(ValueError, match="client must be provided"):
            _AsyncWriteObjectStream(None, BUCKET, OBJECT)
        with pytest.raises(ValueError, match="bucket_name must be provided"):
            _AsyncWriteObjectStream(mock_client, None, OBJECT)
        with pytest.raises(ValueError, match="object_name must be provided"):
            _AsyncWriteObjectStream(mock_client, BUCKET, None)

    # -------------------------------------------------------------------------
    # Open Stream Tests
    # -------------------------------------------------------------------------

    @mock.patch("google.cloud.storage.asyncio.async_write_object_stream.AsyncBidiRpc")
    @pytest.mark.asyncio
    async def test_open_new_object(self, mock_rpc_cls, mock_client):
        mock_rpc = mock_rpc_cls.return_value
        mock_rpc.open = AsyncMock()

        # We don't use spec here to avoid descriptor issues with nested protos
        mock_response = MagicMock()
        mock_response.persisted_size = 0
        mock_response.resource.generation = GENERATION
        mock_response.resource.size = 0
        mock_response.write_handle = WRITE_HANDLE
        mock_rpc.recv = AsyncMock(return_value=mock_response)

        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT)
        await stream.open()

        # Check if BidiRpc was initialized with WriteObjectSpec
        call_args = mock_rpc_cls.call_args
        initial_request = call_args.kwargs["initial_request"]
        # In proto3, string fields default to "" rather than None
        resource = initial_request.write_object_spec.resource
        assert "storage_class" not in resource
        assert resource.storage_class == ""
        assert initial_request.write_object_spec.appendable

        assert stream.is_stream_open
        assert stream.write_handle == WRITE_HANDLE
        assert stream.generation_number == GENERATION

    @mock.patch("google.cloud.storage.asyncio.async_write_object_stream.AsyncBidiRpc")
    @pytest.mark.asyncio
    @pytest.mark.parametrize("storage_class", ["STANDARD", "RAPID"])
    async def test_open_new_object_with_storage_class(
        self, mock_rpc_cls, mock_client, storage_class
    ):
        mock_rpc = mock_rpc_cls.return_value
        mock_rpc.open = AsyncMock()

        mock_response = MagicMock()
        mock_response.persisted_size = 0
        mock_response.resource.generation = GENERATION
        mock_response.resource.size = 0
        mock_response.write_handle = WRITE_HANDLE
        mock_rpc.recv = AsyncMock(return_value=mock_response)

        stream = _AsyncWriteObjectStream(
            mock_client, BUCKET, OBJECT, storage_class=storage_class
        )
        await stream.open()

        call_args = mock_rpc_cls.call_args
        initial_request = call_args.kwargs["initial_request"]
        assert initial_request.write_object_spec is not None
        assert initial_request.write_object_spec.resource.name == OBJECT
        assert initial_request.write_object_spec.resource.storage_class == storage_class
        assert initial_request.write_object_spec.appendable

        assert stream.is_stream_open
        assert stream.write_handle == WRITE_HANDLE
        assert stream.generation_number == GENERATION

    @mock.patch("google.cloud.storage.asyncio.async_write_object_stream.AsyncBidiRpc")
    @pytest.mark.asyncio
    async def test_open_existing_object_with_token(self, mock_rpc_cls, mock_client):
        mock_rpc = mock_rpc_cls.return_value
        mock_rpc.open = AsyncMock()

        # Ensure resource is None so persisted_size logic doesn't get overwritten by child mocks
        mock_response = MagicMock()
        mock_response.persisted_size = 1024
        mock_response.resource = None
        mock_response.write_handle = WRITE_HANDLE
        mock_rpc.recv = AsyncMock(return_value=mock_response)

        stream = _AsyncWriteObjectStream(
            mock_client,
            BUCKET,
            OBJECT,
            generation_number=GENERATION,
            routing_token="token-123",
        )
        await stream.open()

        # Verify AppendObjectSpec attributes
        initial_request = mock_rpc_cls.call_args.kwargs["initial_request"]
        assert initial_request.append_object_spec is not None
        assert initial_request.append_object_spec.generation == GENERATION
        assert initial_request.append_object_spec.routing_token == "token-123"
        assert stream.persisted_size == 1024

    @mock.patch("google.cloud.storage.asyncio.async_write_object_stream.AsyncBidiRpc")
    @pytest.mark.asyncio
    async def test_open_metadata_merging(self, mock_rpc_cls, mock_client):
        mock_rpc = mock_rpc_cls.return_value
        mock_rpc.open = AsyncMock()
        mock_rpc.recv = AsyncMock(return_value=MagicMock(resource=None))

        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT)
        extra_metadata = [("x-custom", "val"), ("x-goog-request-params", "extra=param")]

        await stream.open(metadata=extra_metadata)

        # Verify that metadata combined bucket and extra params
        passed_metadata = mock_rpc_cls.call_args.kwargs["metadata"]
        meta_dict = dict(passed_metadata)
        assert meta_dict["x-custom"] == "val"
        # Params should be comma separated
        params = meta_dict["x-goog-request-params"]
        assert f"bucket={FULL_BUCKET_PATH}" in params
        assert "extra=param" in params

    @mock.patch("google.cloud.storage.asyncio.async_write_object_stream.AsyncBidiRpc")
    @pytest.mark.asyncio
    async def test_open_new_object_with_blob_sync_attrs(
        self, mock_rpc_cls, mock_client
    ):
        mock_rpc = mock_rpc_cls.return_value
        mock_rpc.open = AsyncMock()
        mock_rpc.recv = AsyncMock(return_value=MagicMock(resource=None))

        mock_bucket = mock.Mock(spec=Bucket)
        mock_bucket.name = BUCKET

        mock_blob = mock.Mock(spec=Blob)
        mock_blob.name = OBJECT
        mock_blob.bucket = mock_bucket
        mock_blob.content_type = "text/plain"
        mock_blob.metadata = {"test-key": "test-value"}
        mock_blob.kms_key_name = "kms-key-name"
        mock_blob.cache_control = "cache-control"
        mock_blob.content_disposition = "content-disposition"
        mock_blob.content_encoding = "content-encoding"
        mock_blob.content_language = "content-language"
        mock_blob.temporary_hold = True
        mock_blob.event_based_hold = True
        mock_blob.storage_class = "RAPID"

        custom_time = datetime.datetime(
            2025, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        mock_blob.custom_time = custom_time

        acl_mock = MagicMock()
        acl_mock.loaded = True
        acl_mock.__iter__.return_value = iter(
            [{"role": "READER", "entity": "allUsers"}]
        )
        mock_blob.acl = acl_mock

        retain_until_time = datetime.datetime(
            2026, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        mock_blob.retention = {
            "mode": "Locked",
            "retain_until_time": retain_until_time,
        }
        payload = ObjectCustomContextPayload(value="context-value")
        mock_blob.contexts = ObjectContexts(mock_blob, custom={"context-key": payload})

        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT, blob=mock_blob)
        assert stream.blob.storage_class == "RAPID"
        await stream.open()

        # Verify initial request contains synced attributes from blob
        initial_request = mock_rpc_cls.call_args.kwargs["initial_request"]
        resource = initial_request.write_object_spec.resource

        assert resource.content_type == "text/plain"
        assert resource.metadata == {"test-key": "test-value"}
        assert resource.kms_key == "kms-key-name"
        assert resource.cache_control == "cache-control"
        assert resource.content_disposition == "content-disposition"
        assert resource.content_encoding == "content-encoding"
        assert resource.content_language == "content-language"
        assert resource.temporary_hold is True
        assert resource.event_based_hold is True
        assert resource.storage_class == "RAPID"

        assert int(resource.custom_time.timestamp()) == int(custom_time.timestamp())

        assert len(resource.acl) == 1
        assert resource.acl[0].role == "READER"
        assert resource.acl[0].entity == "allUsers"

        assert resource.retention.mode == _storage_v2.Object.Retention.Mode.LOCKED
        assert int(resource.retention.retain_until_time.timestamp()) == int(
            retain_until_time.timestamp()
        )
        assert "context-key" in resource.contexts.custom
        assert resource.contexts.custom["context-key"].value == "context-value"

    @pytest.mark.asyncio
    async def test_open_already_open_raises(self, mock_client):
        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT)
        stream._is_stream_open = True
        with pytest.raises(ValueError, match="already open"):
            await stream.open()

    # -------------------------------------------------------------------------
    # Send & Recv & Close Tests
    # -------------------------------------------------------------------------

    @mock.patch("google.cloud.storage.asyncio.async_write_object_stream.AsyncBidiRpc")
    @pytest.mark.asyncio
    async def test_send_and_recv_logic(self, mock_rpc_cls, mock_client):
        # Setup open stream
        mock_rpc = mock_rpc_cls.return_value
        mock_rpc.open = AsyncMock()
        mock_rpc.send = AsyncMock()  # Crucial: Must be AsyncMock
        mock_rpc.recv = AsyncMock(return_value=MagicMock(resource=None))

        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT)
        await stream.open()

        # Test Send
        req = _storage_v2.BidiWriteObjectRequest(write_offset=0)
        await stream.send(req)
        mock_rpc.send.assert_awaited_with(req)

        # Test Recv with state update
        mock_response = MagicMock()
        mock_response.persisted_size = 5000
        mock_response.write_handle = b"new-handle"
        mock_response.resource = None
        mock_rpc.recv.return_value = mock_response

        res = await stream.recv()
        assert res.persisted_size == 5000
        assert stream.persisted_size == 5000
        assert stream.write_handle == b"new-handle"

    @pytest.mark.asyncio
    async def test_close_success(self, mock_client):
        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT)
        stream._is_stream_open = True
        stream.socket_like_rpc = AsyncMock()

        stream.socket_like_rpc.send = AsyncMock()
        first_resp = _storage_v2.BidiWriteObjectResponse(persisted_size=100)
        stream.socket_like_rpc.recv = AsyncMock(side_effect=[first_resp, grpc.aio.EOF])
        stream.socket_like_rpc.close = AsyncMock()

        await stream.close()
        stream.socket_like_rpc.close.assert_awaited_once()
        assert not stream.is_stream_open
        assert stream.persisted_size == 100

    @pytest.mark.asyncio
    async def test_close_with_persisted_size_then_eof(self, mock_client):
        """Test close when first recv has persisted_size, second is EOF."""
        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT)
        stream._is_stream_open = True
        stream.socket_like_rpc = AsyncMock()

        # First response has persisted_size (NOT EOF, intermediate)
        persisted_resp = _storage_v2.BidiWriteObjectResponse(persisted_size=500)
        # Second response is EOF (None)
        eof_resp = grpc.aio.EOF

        stream.socket_like_rpc.send = AsyncMock()
        stream.socket_like_rpc.recv = AsyncMock(side_effect=[persisted_resp, eof_resp])
        stream.socket_like_rpc.close = AsyncMock()

        await stream.close()

        # Verify two recv calls: first has persisted_size (NOT EOF), so read second (EOF)
        assert stream.socket_like_rpc.recv.await_count == 2
        assert stream.persisted_size == 500
        assert not stream.is_stream_open

    @pytest.mark.asyncio
    async def test_close_with_grpc_aio_eof_response(self, mock_client):
        """Test close when first recv is grpc.aio.EOF sentinel."""
        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT)
        stream._is_stream_open = True
        stream.socket_like_rpc = AsyncMock()

        # First recv returns grpc.aio.EOF (explicit sentinel from finalize)
        stream.socket_like_rpc.send = AsyncMock()
        stream.socket_like_rpc.recv = AsyncMock(return_value=grpc.aio.EOF)
        stream.socket_like_rpc.close = AsyncMock()

        await stream.close()

        # Verify only one recv call (grpc.aio.EOF=EOF, so don't read second)
        assert stream.socket_like_rpc.recv.await_count == 1
        assert not stream.is_stream_open

    @pytest.mark.asyncio
    async def test_methods_require_open_raises(self, mock_client):
        stream = _AsyncWriteObjectStream(mock_client, BUCKET, OBJECT)
        with pytest.raises(ValueError, match="Stream is not open"):
            await stream.send(MagicMock())
        with pytest.raises(ValueError, match="Stream is not open"):
            await stream.recv()
        with pytest.raises(ValueError, match="Stream is not open"):
            await stream.close()
