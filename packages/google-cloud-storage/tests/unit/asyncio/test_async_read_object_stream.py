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

import asyncio
from unittest import mock
from unittest.mock import AsyncMock

import pytest
from google.api_core.exceptions import Aborted

from google.cloud import _storage_v2
from google.cloud.storage.asyncio import async_read_object_stream
from google.cloud.storage.asyncio.async_read_object_stream import (
    _AsyncReadObjectStream,
)

_TEST_BUCKET_NAME = "test-bucket"
_TEST_OBJECT_NAME = "test-object"
_TEST_GENERATION_NUMBER = 12345
_TEST_OBJECT_SIZE = 1024 * 1024  # 1 MiB
_TEST_READ_HANDLE = b"test-read-handle"
_TEST_READ_HANDLE_NEW = b"test-read-handle-new"


async def instantiate_read_obj_stream(mock_client, mock_cls_async_bidi_rpc, open=True):
    """Helper to create an instance of _AsyncReadObjectStream and open it by default."""
    socket_like_rpc = AsyncMock()
    mock_cls_async_bidi_rpc.return_value = socket_like_rpc
    socket_like_rpc.open = AsyncMock()

    recv_response = mock.MagicMock(spec=_storage_v2.BidiReadObjectResponse)
    recv_response.metadata = mock.MagicMock()
    recv_response.metadata.generation = _TEST_GENERATION_NUMBER
    recv_response.metadata.size = _TEST_OBJECT_SIZE
    recv_response.metadata.finalize_time.second = 30
    recv_response.metadata.checksums.crc32c = 98765
    recv_response.read_handle = _TEST_READ_HANDLE
    socket_like_rpc.recv = AsyncMock(return_value=recv_response)

    read_obj_stream = _AsyncReadObjectStream(
        client=mock_client,
        bucket_name=_TEST_BUCKET_NAME,
        object_name=_TEST_OBJECT_NAME,
    )

    if open:
        await read_obj_stream.open()

    return read_obj_stream


async def instantiate_read_obj_stream_with_read_handle(
    mock_client, mock_cls_async_bidi_rpc, open=True
):
    """Helper to create an instance of _AsyncReadObjectStream and open it by default."""
    socket_like_rpc = AsyncMock()
    mock_cls_async_bidi_rpc.return_value = socket_like_rpc
    socket_like_rpc.open = AsyncMock()

    recv_response = mock.MagicMock(spec=_storage_v2.BidiReadObjectResponse)
    recv_response.read_handle = _TEST_READ_HANDLE_NEW
    socket_like_rpc.recv = AsyncMock(return_value=recv_response)

    read_obj_stream = _AsyncReadObjectStream(
        client=mock_client,
        bucket_name=_TEST_BUCKET_NAME,
        object_name=_TEST_OBJECT_NAME,
    )

    if open:
        await read_obj_stream.open()

    return read_obj_stream


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
def test_init_with_bucket_object_generation(mock_client, mock_async_bidi_rpc):
    # Arrange
    rpc_sentinel = mock.sentinel.A
    mock_client._client._transport.bidi_read_object = "bidi_read_object_rpc"
    mock_client._client._transport._wrapped_methods = {
        "bidi_read_object_rpc": rpc_sentinel,
    }

    # Act
    read_obj_stream = _AsyncReadObjectStream(
        client=mock_client,
        bucket_name=_TEST_BUCKET_NAME,
        object_name=_TEST_OBJECT_NAME,
        generation_number=_TEST_GENERATION_NUMBER,
        read_handle=_TEST_READ_HANDLE,
    )

    # Assert
    assert read_obj_stream.bucket_name == _TEST_BUCKET_NAME
    assert read_obj_stream.object_name == _TEST_OBJECT_NAME
    assert read_obj_stream.generation_number == _TEST_GENERATION_NUMBER
    assert read_obj_stream.read_handle == _TEST_READ_HANDLE
    assert read_obj_stream.rpc == rpc_sentinel


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_open(mock_client, mock_cls_async_bidi_rpc):
    # arrange
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=False
    )

    # act
    await read_obj_stream.open()

    # assert
    read_obj_stream.socket_like_rpc.open.assert_called_once()
    read_obj_stream.socket_like_rpc.recv.assert_called_once()

    assert read_obj_stream.generation_number == _TEST_GENERATION_NUMBER
    assert read_obj_stream.read_handle == _TEST_READ_HANDLE
    assert read_obj_stream.persisted_size == _TEST_OBJECT_SIZE
    assert read_obj_stream.is_finalized is True
    assert read_obj_stream.full_obj_server_crc32c == 98765
    assert read_obj_stream.is_stream_open


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_open_with_read_handle(mock_client, mock_cls_async_bidi_rpc):
    # arrange
    read_obj_stream = await instantiate_read_obj_stream_with_read_handle(
        mock_client, mock_cls_async_bidi_rpc, open=False
    )

    # act
    await read_obj_stream.open()

    # assert
    read_obj_stream.socket_like_rpc.open.assert_called_once()
    read_obj_stream.socket_like_rpc.recv.assert_called_once()

    assert read_obj_stream.generation_number is None
    assert read_obj_stream.persisted_size is None
    assert read_obj_stream.read_handle == _TEST_READ_HANDLE_NEW
    assert read_obj_stream.is_stream_open


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_open_when_already_open_should_raise_error(
    mock_client, mock_cls_async_bidi_rpc
):
    # arrange
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=True
    )

    # act + assert (pythonic)
    with pytest.raises(ValueError) as exc:
        await read_obj_stream.open()

    # assert
    assert str(exc.value) == "Stream is already open"


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_close(mock_client, mock_cls_async_bidi_rpc):
    # arrange
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=True
    )
    read_obj_stream.requests_done = AsyncMock()

    # act
    await read_obj_stream.close()

    # assert
    read_obj_stream.requests_done.assert_called_once()
    read_obj_stream.socket_like_rpc.close.assert_called_once()
    assert not read_obj_stream.is_stream_open


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_open_closes_rpc_when_first_recv_fails(
    mock_client, mock_cls_async_bidi_rpc
):
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=False
    )
    socket_like_rpc = mock_cls_async_bidi_rpc.return_value
    socket_like_rpc.recv = AsyncMock(
        side_effect=Aborted("Idle stream has been closed.")
    )

    with pytest.raises(Aborted):
        await read_obj_stream.open()

    socket_like_rpc.open.assert_awaited_once()
    socket_like_rpc.close.assert_awaited_once()
    assert not read_obj_stream.is_stream_open


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.parametrize("cancelled_await", ["open", "recv"])
@pytest.mark.asyncio
async def test_open_closes_rpc_when_cancelled(
    mock_client, mock_cls_async_bidi_rpc, cancelled_await
):
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=False
    )
    socket_like_rpc = mock_cls_async_bidi_rpc.return_value
    setattr(
        socket_like_rpc,
        cancelled_await,
        AsyncMock(side_effect=asyncio.CancelledError),
    )

    with pytest.raises(asyncio.CancelledError):
        await read_obj_stream.open()

    socket_like_rpc.close.assert_awaited_once()
    assert not read_obj_stream.is_stream_open


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_open_propagates_close_failure_from_failed_open(
    mock_client, mock_cls_async_bidi_rpc
):
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=False
    )
    socket_like_rpc = mock_cls_async_bidi_rpc.return_value
    socket_like_rpc.recv = AsyncMock(
        side_effect=Aborted("Idle stream has been closed.")
    )
    socket_like_rpc.close = AsyncMock(side_effect=RuntimeError("close blew up"))

    with pytest.raises(Aborted):
        await read_obj_stream.open()

    assert not read_obj_stream.is_stream_open


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_close_closes_rpc_when_requests_done_fails(
    mock_client, mock_cls_async_bidi_rpc
):
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=True
    )
    socket_like_rpc = read_obj_stream.socket_like_rpc
    read_obj_stream.requests_done = AsyncMock(
        side_effect=Aborted("Idle stream has been closed.")
    )

    with pytest.raises(Aborted):
        await read_obj_stream.close()

    socket_like_rpc.close.assert_awaited_once()
    assert not read_obj_stream.is_stream_open


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_close_skips_requests_done_on_inactive_rpc(
    mock_client, mock_cls_async_bidi_rpc
):
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=True
    )
    read_obj_stream.socket_like_rpc.is_active = False
    read_obj_stream.requests_done = AsyncMock()

    await read_obj_stream.close()

    read_obj_stream.requests_done.assert_not_called()
    read_obj_stream.socket_like_rpc.close.assert_awaited_once()
    assert not read_obj_stream.is_stream_open


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_requests_done(mock_client, mock_cls_async_bidi_rpc):
    """Test that requests_done signals the end of requests."""
    # Arrange
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=True
    )
    read_obj_stream.socket_like_rpc.send = AsyncMock()
    read_obj_stream.socket_like_rpc.recv = AsyncMock()

    # Act
    await read_obj_stream.requests_done()

    # Assert
    read_obj_stream.socket_like_rpc.send.assert_called_once_with(None)
    read_obj_stream.socket_like_rpc.recv.assert_called_once()


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_close_without_open_should_raise_error(
    mock_client, mock_cls_async_bidi_rpc
):
    # arrange
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=False
    )

    # act + assert (pythonic)
    with pytest.raises(ValueError) as exc:
        await read_obj_stream.close()

    # assert
    assert str(exc.value) == "Stream is not open"


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_send(mock_client, mock_cls_async_bidi_rpc):
    # arrange
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=True
    )

    # act
    bidi_read_object_request = _storage_v2.BidiReadObjectRequest()
    await read_obj_stream.send(bidi_read_object_request)

    # assert
    read_obj_stream.socket_like_rpc.send.assert_called_once_with(
        bidi_read_object_request
    )


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_send_without_open_should_raise_error(
    mock_client, mock_cls_async_bidi_rpc
):
    # arrange
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=False
    )

    # act + assert (pythonic)
    with pytest.raises(ValueError) as exc:
        await read_obj_stream.send(_storage_v2.BidiReadObjectRequest())

    # assert
    assert str(exc.value) == "Stream is not open"


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_recv(mock_client, mock_cls_async_bidi_rpc):
    # arrange
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=True
    )
    bidi_read_object_response = _storage_v2.BidiReadObjectResponse()
    read_obj_stream.socket_like_rpc.recv = AsyncMock(
        return_value=bidi_read_object_response
    )

    # act
    response = await read_obj_stream.recv()

    # assert
    read_obj_stream.socket_like_rpc.recv.assert_called_once()
    assert response == bidi_read_object_response


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_recv_without_open_should_raise_error(
    mock_client, mock_cls_async_bidi_rpc
):
    # arrange
    read_obj_stream = await instantiate_read_obj_stream(
        mock_client, mock_cls_async_bidi_rpc, open=False
    )

    # act + assert (pythonic)
    with pytest.raises(ValueError) as exc:
        await read_obj_stream.recv()

    # assert
    assert str(exc.value) == "Stream is not open"


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_recv_updates_read_handle_on_refresh(
    mock_client, mock_cls_async_bidi_rpc
):
    """
    Verify that the `recv` method correctly updates the stream's handle
    when a new one is provided in a server response.
    """
    # Arrange
    socket_like_rpc = AsyncMock()
    mock_cls_async_bidi_rpc.return_value = socket_like_rpc
    socket_like_rpc.open = AsyncMock()

    initial_handle = _storage_v2.BidiReadHandle(handle=b"initial-handle-token")
    response_with_initial_handle = _storage_v2.BidiReadObjectResponse(
        read_handle=initial_handle
    )
    response_without_handle = _storage_v2.BidiReadObjectResponse(read_handle=None)

    refreshed_handle = _storage_v2.BidiReadHandle(handle=b"new-refreshed-handle-token")
    response_with_refreshed_handle = _storage_v2.BidiReadObjectResponse(
        read_handle=refreshed_handle
    )

    socket_like_rpc.recv.side_effect = [
        response_with_initial_handle,
        response_without_handle,
        response_with_refreshed_handle,
    ]

    starting_handle = _storage_v2.BidiReadHandle(handle=b"starting-handle-token")
    stream = async_read_object_stream._AsyncReadObjectStream(
        client=mock_client,
        bucket_name=_TEST_BUCKET_NAME,
        object_name=_TEST_OBJECT_NAME,
        read_handle=starting_handle,
    )

    # Act & Assert
    assert stream.read_handle == starting_handle

    await stream.open()
    assert stream.read_handle == initial_handle

    await stream.recv()
    assert stream.read_handle == initial_handle

    await stream.recv()
    assert stream.read_handle == refreshed_handle


@mock.patch("google.cloud.storage.asyncio.async_read_object_stream.AsyncBidiRpc")
@mock.patch(
    "google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client"
)
@pytest.mark.asyncio
async def test_open_unfinalized_object_skips_checksum(
    mock_client, mock_cls_async_bidi_rpc
):
    socket_like_rpc = AsyncMock()
    mock_cls_async_bidi_rpc.return_value = socket_like_rpc
    socket_like_rpc.open = AsyncMock()

    recv_response = mock.MagicMock(spec=_storage_v2.BidiReadObjectResponse)
    recv_response.metadata = mock.MagicMock()
    recv_response.metadata.generation = _TEST_GENERATION_NUMBER
    recv_response.metadata.size = _TEST_OBJECT_SIZE
    recv_response.metadata.finalize_time.second = 0  # NOT finalized!
    recv_response.metadata.checksums.crc32c = 98765
    recv_response.read_handle = _TEST_READ_HANDLE
    socket_like_rpc.recv = AsyncMock(return_value=recv_response)

    read_obj_stream = _AsyncReadObjectStream(
        client=mock_client,
        bucket_name=_TEST_BUCKET_NAME,
        object_name=_TEST_OBJECT_NAME,
    )

    await read_obj_stream.open()

    assert read_obj_stream.is_finalized is False
    assert read_obj_stream.full_obj_server_crc32c is None
