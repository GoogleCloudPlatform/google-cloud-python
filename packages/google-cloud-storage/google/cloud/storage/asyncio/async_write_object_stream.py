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
from typing import TYPE_CHECKING, Any, List, Optional, Tuple

import grpc
from google.api_core.bidi_async import AsyncBidiRpc

from google.cloud import _storage_v2
from google.cloud.storage import Blob, _grpc_conversions, _opentelemetry_metrics
from google.cloud.storage.asyncio import _utils
from google.cloud.storage.asyncio.async_abstract_object_stream import (
    _AsyncAbstractObjectStream,
)
from google.cloud.storage.asyncio.async_grpc_client import (
    AsyncGrpcClient,
    _mark_call_closing_cleanly,
    _resolve_network_path,
)

if TYPE_CHECKING:
    from google.cloud.storage.asyncio.async_appendable_object_writer import (
        Preconditions,
    )


class _AsyncWriteObjectStream(_AsyncAbstractObjectStream):
    """Class representing a gRPC bidi-stream for writing data from a GCS
      ``Appendable Object``.

    This class provides a unix socket-like interface to a GCS ``Object``, with
    methods like ``open``, ``close``, ``send``, and ``recv``.

    :type client: :class:`~google.cloud.storage.asyncio.async_grpc_client.AsyncGrpcClient.grpc_client`
    :param client: async grpc client to use for making API requests.

    :type bucket_name: str
    :param bucket_name: The name of the GCS ``bucket`` containing the object.

    :type object_name: str
    :param object_name: The name of the GCS ``Appendable Object`` to be write.

    :type generation_number: int
    :param generation_number: (Optional) If present, creates writer for that
        specific revision of that object. Use this to append data to an
        existing Appendable Object.

        Setting to ``0`` makes the `writer.open()` succeed only if
        object doesn't exist in the bucket (useful for not accidentally
        overwriting existing objects).

        Warning: If `None` and no generation precondition is set in
        `preconditions`, a new object is created. If an object with the
        same name already exists, it will be overwritten the moment
        `writer.open()` is called.

    :type write_handle: _storage_v2.BidiWriteHandle
    :param write_handle: (Optional) An existing handle for writing the object.
                        If provided, opening the bidi-gRPC connection will be faster.

    :type storage_class: Optional[str]
    :param storage_class: (Optional) The storage class of the object.

    :type preconditions: Optional[:class:`~google.cloud.storage.asyncio.async_appendable_object_writer.Preconditions`]
    :param preconditions: (Optional) Preconditions for the write operation.
        Generation preconditions apply only when creating or overwriting an
        object (``generation_number`` is ``None`` or ``0``); metageneration
        preconditions apply to both creating/overwriting and appending.
    """

    def __init__(
        self,
        client: AsyncGrpcClient.grpc_client,
        bucket_name: str,
        object_name: str,
        generation_number: Optional[int] = None,  # None means new object
        write_handle: Optional[_storage_v2.BidiWriteHandle] = None,
        routing_token: Optional[str] = None,
        blob: Optional[Blob] = None,
        storage_class: Optional[str] = None,
        preconditions: Optional["Preconditions"] = None,
        metrics_recorder: Optional[Any] = None,
    ) -> None:
        if client is None:
            raise ValueError("client must be provided")
        if bucket_name is None:
            raise ValueError("bucket_name must be provided")
        if object_name is None:
            raise ValueError("object_name must be provided")

        super().__init__(
            bucket_name=bucket_name,
            object_name=object_name,
            generation_number=generation_number,
        )
        self.client: AsyncGrpcClient.grpc_client = client
        self.write_handle: Optional[_storage_v2.BidiWriteHandle] = write_handle
        self.routing_token: Optional[str] = routing_token
        self.blob: Optional[Blob] = blob
        self.storage_class: Optional[str] = storage_class
        self.preconditions: Optional["Preconditions"] = preconditions
        self._metrics_recorder = (
            metrics_recorder
            if metrics_recorder is not None
            else _opentelemetry_metrics.get_active_recorder(client)
        )
        self._full_bucket_name = f"projects/_/buckets/{self.bucket_name}"

        self.rpc = self.client._client._transport._wrapped_methods[
            self.client._client._transport.bidi_write_object
        ]

        self.metadata = (("x-goog-request-params", f"bucket={self._full_bucket_name}"),)
        self.socket_like_rpc: Optional[AsyncBidiRpc] = None
        self._is_stream_open: bool = False
        self.first_bidi_write_req = None
        self.persisted_size = 0
        self.object_resource: Optional[_storage_v2.Object] = None

    async def open(self, metadata: Optional[List[Tuple[str, str]]] = None) -> None:
        """
        Opens the bidi-gRPC connection to write to the object.

        This method sends an initial request to start the stream and receives
        the first response containing metadata and a write handle.

        :rtype: None
        :raises ValueError: If the stream is already open.
        :raises google.api_core.exceptions.FailedPrecondition:
            If a precondition in `preconditions` (or `generation_number=0`) is
            not met.
        """
        if self._is_stream_open:
            raise ValueError("Stream is already open")

        # Create a new object or overwrite existing one if generation_number
        # is None. This makes it consistent with GCS JSON API behavior.
        # Created object type would be Appendable Object.
        # if `generation_number` == 0 new object will be created only if there
        # isn't any existing object.
        if self.generation_number is None or self.generation_number == 0:
            if self.blob:
                resource = _grpc_conversions.blob_to_proto(self.blob)
            else:
                resource = _storage_v2.Object(
                    name=self.object_name,
                    bucket=self._full_bucket_name,
                    storage_class=self.storage_class,
                )
            if_generation_match = (
                self.preconditions.if_generation_match
                if self.preconditions
                and self.preconditions.if_generation_match is not None
                else self.generation_number
            )
            self.first_bidi_write_req = _storage_v2.BidiWriteObjectRequest(
                write_object_spec=_storage_v2.WriteObjectSpec(
                    resource=resource,
                    appendable=True,
                    if_generation_match=if_generation_match,
                    if_generation_not_match=(
                        self.preconditions.if_generation_not_match
                        if self.preconditions
                        else None
                    ),
                    if_metageneration_match=(
                        self.preconditions.if_metageneration_match
                        if self.preconditions
                        else None
                    ),
                    if_metageneration_not_match=(
                        self.preconditions.if_metageneration_not_match
                        if self.preconditions
                        else None
                    ),
                ),
            )
        else:
            self.first_bidi_write_req = _storage_v2.BidiWriteObjectRequest(
                append_object_spec=_storage_v2.AppendObjectSpec(
                    bucket=self._full_bucket_name,
                    object=self.object_name,
                    generation=self.generation_number,
                    write_handle=self.write_handle if self.write_handle else None,
                    routing_token=self.routing_token if self.routing_token else None,
                    if_metageneration_match=(
                        self.preconditions.if_metageneration_match
                        if self.preconditions
                        else None
                    ),
                    if_metageneration_not_match=(
                        self.preconditions.if_metageneration_not_match
                        if self.preconditions
                        else None
                    ),
                ),
            )

        request_param_values = [f"bucket={self._full_bucket_name}"]
        final_metadata = []
        if metadata:
            for key, value in metadata:
                if key == "x-goog-request-params":
                    request_param_values.append(value)
                else:
                    final_metadata.append((key, value))

        final_metadata.append(("x-goog-request-params", "&".join(request_param_values)))
        final_metadata = _utils.inject_traceparent_to_metadata(final_metadata)

        self.socket_like_rpc = AsyncBidiRpc(
            self.rpc,
            initial_request=self.first_bidi_write_req,
            metadata=final_metadata,
        )

        try:
            await self.socket_like_rpc.open()  # this is actually 1 send
            response = await self.socket_like_rpc.recv()
        except (asyncio.CancelledError, Exception):
            await self._close_socket_like_rpc()
            raise
        if self._metrics_recorder is not None:
            net_path = self._get_network_path(received_server_response=True)
            _opentelemetry_metrics.record_pending_retry(
                self._metrics_recorder,
                operation="WriteObject",
                network_path=net_path,
            )
        self._is_stream_open = True

        if response.persisted_size:
            self.persisted_size = response.persisted_size

        if response.resource:
            if not response.resource.size:
                # Appending to a 0 byte appendable object.
                self.persisted_size = 0
            else:
                self.persisted_size = response.resource.size

            self.generation_number = response.resource.generation

        if response.write_handle:
            self.write_handle = response.write_handle

    async def _close_socket_like_rpc(self) -> None:
        try:
            await self.socket_like_rpc.close()
        except Exception:
            pass

    def _get_network_path(self, received_server_response: bool = True) -> str:
        """Resolves ``network.path`` for the active gRPC stream call."""
        return _resolve_network_path(
            call=getattr(self.socket_like_rpc, "call", None),
            received_server_response=received_server_response,
        )

    def _mark_closing_cleanly(self) -> None:
        """Marks the underlying gRPC call as closing cleanly for metrics."""
        _mark_call_closing_cleanly(getattr(self.socket_like_rpc, "call", None))

    async def close(self) -> None:
        """Closes the bidi-gRPC connection."""
        if not self._is_stream_open:
            raise ValueError("Stream is not open")
        try:
            await self.requests_done()
            self._mark_closing_cleanly()
        finally:
            self._is_stream_open = False
            await self.socket_like_rpc.close()

    async def requests_done(self):
        """Signals that all requests have been sent."""
        await self.socket_like_rpc.send(None)

        # The server may send a final "EOF" response immediately, or it may
        # first send an intermediate response followed by the EOF response depending on whether the object was finalized or not.
        first_resp = await self.socket_like_rpc.recv()
        _utils.update_write_handle_if_exists(self, first_resp)

        if first_resp != grpc.aio.EOF:
            # this persisted_size will not be upto date., also what if response
            # doesn't have persisted_size? , it'll throw error.
            if hasattr(first_resp, "persisted_size"):
                self.persisted_size = first_resp.persisted_size
            second_resp = await self.socket_like_rpc.recv()
            assert second_resp == grpc.aio.EOF

    async def send(
        self, bidi_write_object_request: _storage_v2.BidiWriteObjectRequest
    ) -> None:
        """Sends a request message on the stream.

        Args:
            bidi_write_object_request (:class:`~google.cloud._storage_v2.types.BidiReadObjectRequest`):
                The request message to send. This is typically used to specify
                the read offset and limit.
        """
        if not self._is_stream_open:
            raise ValueError("Stream is not open")
        await self.socket_like_rpc.send(bidi_write_object_request)

    async def recv(self) -> _storage_v2.BidiWriteObjectResponse:
        """Receives a response from the stream.

        This method waits for the next message from the server, which could
        contain object data or metadata.

        Returns:
            :class:`~google.cloud._storage_v2.types.BidiWriteObjectResponse`:
                The response message from the server.
        """
        if not self._is_stream_open:
            raise ValueError("Stream is not open")
        response = await self.socket_like_rpc.recv()
        # Update write_handle if present in response
        if response:
            if response.write_handle:
                self.write_handle = response.write_handle
            if response.persisted_size is not None:
                self.persisted_size = response.persisted_size
            if response.resource and response.resource.size:
                self.persisted_size = response.resource.size
        return response

    @property
    def is_stream_open(self) -> bool:
        return self._is_stream_open
