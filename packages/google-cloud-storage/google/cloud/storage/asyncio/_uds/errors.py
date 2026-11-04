# Copyright 2026 Google LLC
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

"""Errors and error mapping for the private gRPC-over-UDS (Rust Core SDK) backend."""

from __future__ import annotations

import logging

from google.api_core import exceptions

logger = logging.getLogger(__name__)


class CoreSdkUnavailableError(exceptions.GoogleAPICallError, ValueError, RuntimeError):
    """Raised when the Rust Core SDK (``gcs-core-server``) path cannot be used.

    This is raised:

    * whenever ``--force-use-core-sdk`` (``GOOGLE_CLOUD_STORAGE_FORCE_USE_CORE_SDK=1``,
      ``-X gcs_force_use_core_sdk`` or ``GOOGLE_CLOUD_STORAGE_UDS=on``) is active and the
      Python SDK cannot reach Cloud Storage through the Rust Core SDK for any reason
      (missing binary, unreachable socket, server identity mismatch, unsupported
      platform, capability mismatch, unsupported ``Blob`` attributes, ...). GAPIC is
      never used as a silent fallback in that mode.
    * whenever DirectPath is explicitly enforced (``attempt_direct_path=True`` passed
      explicitly, a ``google-c2p:///`` endpoint, or
      ``GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS``) while the UDS backend is enabled: the
      Rust Core SDK only supports gRPC CloudPath.
    """

    def __init__(self, message, errors=(), **kwargs):
        super().__init__(message, errors=errors, **kwargs)

    def __str__(self):
        # GoogleAPICallError prefixes `code` (None here); keep the message readable.
        return str(self.message)


def to_api_exception(err):
    """Maps a ``grpc.aio.AioRpcError`` from the UDS server to a ``google.api_core`` exception."""
    import grpc

    from google.cloud.storage.exceptions import DataCorruption

    if isinstance(err, exceptions.GoogleAPICallError):
        return err
    if not isinstance(err, grpc.RpcError):
        return err
    try:
        code = err.code()
        details = err.details() or ""
    except Exception:  # pragma: NO COVER - defensive
        return exceptions.InternalServerError(str(err))
    if code == grpc.StatusCode.DATA_LOSS:
        return DataCorruption(None, details)
    return exceptions.from_grpc_error(err)


def range_error_to_exception(range_error):
    """Maps a per-range ``RangeError`` message to a ``google.api_core`` exception."""
    import grpc

    from google.cloud.storage.exceptions import DataCorruption

    if (
        range_error.checksum_mismatch
        or range_error.code == grpc.StatusCode.DATA_LOSS.value[0]
    ):
        # The Rust SDK validated per-chunk / full-object CRC32C (or detected a truncated
        # range); surface it exactly like the GAPIC path does.
        return DataCorruption(
            None, f"Checksum mismatch while reading range: {range_error.message}"
        )
    status = None
    for s in grpc.StatusCode:
        if s.value[0] == range_error.code:
            status = s
            break
    if status is None:
        return exceptions.Unknown(range_error.message)
    return exceptions.from_grpc_status(status, range_error.message)


def object_from_resource(resource):
    """Converts a ``gcscore.v1.ObjectResource`` into a ``_storage_v2.Object``.

    The full resource travels as proto3 JSON (``object_json``) produced by the Rust
    SDK's public ``serde::Serialize`` impl of ``model::Object``; the typed fields are a
    fallback if JSON parsing fails.
    """
    from google.cloud import _storage_v2

    if resource is None:
        return None
    if resource.object_json:
        try:
            return _storage_v2.Object.from_json(
                resource.object_json, ignore_unknown_fields=True
            )
        except Exception as exc:  # pragma: NO COVER - defensive fallback
            logger.debug("object_json parse failed, using typed fields: %s", exc)
    obj = _storage_v2.Object(
        bucket=resource.bucket,
        name=resource.name,
        generation=resource.generation,
        metageneration=resource.metageneration,
        size=resource.size,
        storage_class=resource.storage_class,
        etag=resource.etag,
        content_type=resource.content_type,
        content_encoding=resource.content_encoding,
        metadata=dict(resource.metadata),
        kms_key=resource.kms_key,
    )
    if resource.HasField("crc32c") or resource.md5_hash:
        obj.checksums = _storage_v2.ObjectChecksums(
            crc32c=resource.crc32c if resource.HasField("crc32c") else None,
            md5_hash=resource.md5_hash or None,
        )
    return obj


async def stream_write(call, req) -> None:
    """Writes ``req`` to a bidi stream without clobbering peer close status.

    ``grpc.aio.StreamStreamCall.write`` catches ``cygrpc.InternalError``
    (raised as ``ExecuteBatchError`` when C-core has already closed the stream
    on its poller thread before asyncio processes ``RECV_STATUS_ON_CLIENT``)
    and calls ``set_internal_error``, replacing the server's real status (for
    example ``UNAVAILABLE``) with ``INTERNAL`` (``"Internal error from Core"``).
    Waiting for ``call.code()`` on ``InternalError`` lets ``RECV_STATUS_ON_CLIENT``
    deliver the peer's status instead.
    """
    import asyncio

    import grpc
    from grpc._cython import cygrpc

    if not isinstance(call, grpc.aio.StreamStreamCall):
        await call.write(req)
        return
    if call.done():
        raise asyncio.InvalidStateError("RPC already finished.")
    await call.wait_for_connection()
    try:
        await call._cython_call.send_serialized_message(req.SerializeToString())
    except cygrpc.InternalError as err:
        await call.code()
        await call._raise_for_status()
        raise asyncio.InvalidStateError(str(err)) from err
    except asyncio.CancelledError:
        call.cancel()
        raise
