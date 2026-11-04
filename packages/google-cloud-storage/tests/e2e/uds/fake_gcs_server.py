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

"""A hermetic, in-memory fake of the ``google.storage.v2.Storage`` gRPC service.

Only the RPCs needed by the UDS end-to-end tests are implemented:

* ``BidiWriteObject`` (appendable and non-appendable uploads, takeover via
  ``AppendObjectSpec``, ``flush`` / ``state_lookup`` / ``finish_write``).
* ``BidiReadObject`` (multi-range reads, tail reads, ``OUT_OF_RANGE`` errors
  carrying a ``google.storage.v2.BidiReadObjectError`` status detail).
* ``GetObject`` and ``DeleteObject``.

The response shapes mirror the real service as consumed by the
google-cloud-rust ``google-cloud-storage`` client (see
``src/storage/src/storage/bidi_write/{transport,worker,connector}.rs`` and
``src/storage/src/storage/bidi/*.rs``):

* The first ``BidiWriteObjectResponse`` always carries ``resource`` (with
  ``generation`` and ``size`` == persisted bytes, including any data sent in
  the first request) plus ``write_handle`` and ``persisted_data_checksums``.
* ``state_lookup`` requests (and a client half-close of an unfinalized
  appendable upload) are answered with ``persisted_size``; ``flush`` alone is
  not answered, exactly as documented on ``BidiWriteObjectRequest``.
* ``finish_write`` is answered with ``resource`` including ``finalize_time``
  and ``checksums.crc32c``.
* The first ``BidiReadObjectResponse`` carries ``metadata`` and
  ``read_handle``; data is returned as ``ObjectRangeData`` whose
  ``read_range`` is ``(chunk_offset, chunk_length, read_id)`` and whose last
  chunk has ``range_end=True``.

The server binds to ``127.0.0.1`` only.
"""

from __future__ import annotations

import dataclasses
import datetime
import itertools
from typing import Any, Dict, List, Optional, Tuple

import google_crc32c
import grpc
from google.protobuf import any_pb2, empty_pb2
from google.rpc import code_pb2, status_pb2

from google.cloud import _storage_v2

SERVICE_NAME = "google.storage.v2.Storage"
#: Maximum payload of a single ``ChecksummedData`` sent on reads.
MAX_READ_CHUNK_SIZE = 2 * 1024 * 1024
_MAX_MESSAGE_SIZE = 64 * 1024 * 1024
_BUCKET_PREFIX = "projects/_/buckets/"

# Resource attributes copied from ``WriteObjectSpec.resource``.
_COPIED_STRING_ATTRS = (
    "content_type",
    "content_encoding",
    "content_disposition",
    "content_language",
    "cache_control",
    "storage_class",
    "kms_key",
)


def crc32c(data: bytes) -> int:
    """Returns the CRC32C of ``data`` as an unsigned 32-bit int."""
    return google_crc32c.value(bytes(data))


def _now() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def normalize_bucket(bucket: str) -> str:
    """Returns ``projects/_/buckets/<bucket>`` for either a short or full name."""
    if bucket.startswith("projects/"):
        return bucket
    return _BUCKET_PREFIX + bucket


@dataclasses.dataclass
class FakeObject:
    """One generation of an object stored in the fake."""

    bucket: str
    name: str
    generation: int
    metageneration: int = 1
    data: bytearray = dataclasses.field(default_factory=bytearray)
    finalized: bool = False
    appendable: bool = True
    content_type: str = ""
    content_encoding: str = ""
    content_disposition: str = ""
    content_language: str = ""
    cache_control: str = ""
    storage_class: str = "STANDARD"
    kms_key: str = ""
    metadata: Dict[str, str] = dataclasses.field(default_factory=dict)
    custom_time: Optional[datetime.datetime] = None
    create_time: datetime.datetime = dataclasses.field(default_factory=_now)
    update_time: datetime.datetime = dataclasses.field(default_factory=_now)
    finalize_time: Optional[datetime.datetime] = None
    #: Incremented on every writer takeover; stale writer streams are rejected.
    writer_epoch: int = 0
    #: When true, ``checksums.crc32c`` reported in metadata is deliberately wrong.
    corrupt_reported_crc32c: bool = False

    @property
    def size(self) -> int:
        return len(self.data)

    @property
    def crc32c(self) -> int:
        return crc32c(self.data)

    def to_proto(self) -> _storage_v2.Object:
        obj = _storage_v2.Object(
            name=self.name,
            bucket=self.bucket,
            generation=self.generation,
            metageneration=self.metageneration,
            size=self.size,
            storage_class=self.storage_class,
            content_type=self.content_type,
            content_encoding=self.content_encoding,
            content_disposition=self.content_disposition,
            content_language=self.content_language,
            cache_control=self.cache_control,
            kms_key=self.kms_key,
            metadata=dict(self.metadata),
            create_time=self.create_time,
            update_time=self.update_time,
            etag=f"{self.generation}-{self.metageneration}",
        )
        if self.custom_time is not None:
            obj.custom_time = self.custom_time
        if self.finalized:
            obj.finalize_time = self.finalize_time
            reported = self.crc32c
            if self.corrupt_reported_crc32c:
                reported ^= 0xFFFFFFFF
            obj.checksums = _storage_v2.ObjectChecksums(crc32c=reported)
        return obj


@dataclasses.dataclass
class _InjectedError:
    code: grpc.StatusCode
    message: str
    after_requests: int


class FakeGcsState:
    """The mutable state of a fake server, also the test-facing control API."""

    def __init__(self) -> None:
        self.objects: Dict[Tuple[str, str], FakeObject] = {}
        #: Every request received, as ``(method_name, request)`` tuples.
        self.requests: List[Tuple[str, Any]] = []
        #: Invocation metadata of every call, as ``(method_name, {key: value})``.
        self.call_metadata: List[Tuple[str, Dict[str, Any]]] = []
        self._generations = itertools.count(1_700_000_000_000_001)
        self._handles = itertools.count(1)
        self._corrupt_read_chunks = 0
        self._injected: Dict[str, List[_InjectedError]] = {}

    # ----------------------------------------------------------------- helpers
    def next_generation(self) -> int:
        return next(self._generations)

    def next_handle(self, prefix: str) -> bytes:
        return f"{prefix}-{next(self._handles)}".encode()

    def get_object(self, bucket: str, name: str) -> Optional[FakeObject]:
        """Returns the live object (or ``None``), accepting short bucket names."""
        return self.objects.get((normalize_bucket(bucket), name))

    def put_object(
        self,
        bucket: str,
        name: str,
        data: bytes = b"",
        *,
        finalized: bool = True,
        appendable: bool = False,
        **attrs: Any,
    ) -> FakeObject:
        """Seeds an object directly, bypassing the RPCs. Returns it."""
        now = _now()
        obj = FakeObject(
            bucket=normalize_bucket(bucket),
            name=name,
            generation=self.next_generation(),
            data=bytearray(data),
            finalized=finalized,
            appendable=appendable,
            finalize_time=now if finalized else None,
            create_time=now,
            update_time=now,
            **attrs,
        )
        self.objects[(obj.bucket, name)] = obj
        return obj

    def requests_for(self, method: str) -> List[Any]:
        return [r for m, r in self.requests if m == method]

    def _record_call(self, method: str, context) -> None:
        self.call_metadata.append(
            (method, {k: v for k, v in (context.invocation_metadata() or ())})
        )

    # ------------------------------------------------------- fault injection
    def corrupt_next_read_chunks(self, count: int = 1) -> None:
        """Makes the next ``count`` read chunks carry a wrong ``crc32c``.

        The payload bytes are unchanged; only ``ChecksummedData.crc32c`` is
        flipped, so a client validating per-chunk checksums must fail.
        """
        self._corrupt_read_chunks += count

    def corrupt_object_crc32c(self, bucket: str, name: str) -> None:
        """Makes metadata for the object report a wrong ``checksums.crc32c``.

        Use it to exercise full-object checksum validation on reads.
        """
        obj = self.get_object(bucket, name)
        if obj is None:
            raise KeyError((bucket, name))
        obj.corrupt_reported_crc32c = True

    def inject_error(
        self,
        method: str,
        code: grpc.StatusCode,
        message: str = "injected error",
        *,
        count: int = 1,
        after_requests: int = 0,
    ) -> None:
        """Fails the next ``count`` calls of ``method`` with ``code``.

        For streaming methods the call fails when the request with index
        ``after_requests`` (0 == the first request) arrives, *before* that
        request is processed; earlier requests are handled normally. Unary
        methods ignore ``after_requests``.
        """
        self._injected.setdefault(method, []).extend(
            _InjectedError(code, message, after_requests) for _ in range(count)
        )

    def _take_read_corruption(self) -> bool:
        if self._corrupt_read_chunks > 0:
            self._corrupt_read_chunks -= 1
            return True
        return False

    def _claim_injection(self, method: str) -> Optional[_InjectedError]:
        queue = self._injected.get(method)
        return queue.pop(0) if queue else None


async def _maybe_fail(injection: Optional[_InjectedError], index: int, context) -> None:
    """Aborts the call if ``injection`` is due at request ``index``."""
    if injection is not None and injection.after_requests == index:
        await context.abort(injection.code, injection.message)


def _check_preconditions(obj: Optional[FakeObject], spec, errors: list) -> None:
    """Evaluates generation / metageneration preconditions present on ``spec``."""
    current_gen = obj.generation if obj is not None else 0
    fields = type(spec).meta.fields
    if "if_generation_match" in fields and "if_generation_match" in spec:
        if spec.if_generation_match != current_gen:
            errors.append(
                f"if_generation_match={spec.if_generation_match} but current "
                f"generation is {current_gen}"
            )
    if "if_generation_not_match" in fields and "if_generation_not_match" in spec:
        if spec.if_generation_not_match == current_gen:
            errors.append(
                f"if_generation_not_match={spec.if_generation_not_match} matched"
            )
    if obj is not None:
        if "if_metageneration_match" in spec:
            if spec.if_metageneration_match != obj.metageneration:
                errors.append(
                    f"if_metageneration_match={spec.if_metageneration_match} but "
                    f"current metageneration is {obj.metageneration}"
                )
        if "if_metageneration_not_match" in spec:
            if spec.if_metageneration_not_match == obj.metageneration:
                errors.append(
                    f"if_metageneration_not_match={spec.if_metageneration_not_match} matched"
                )


class FakeStorageServicer:
    """Implements the subset of ``google.storage.v2.Storage`` described above."""

    def __init__(self, state: FakeGcsState) -> None:
        self.state = state

    def generic_handler(self) -> grpc.GenericRpcHandler:
        s = _storage_v2
        return grpc.method_handlers_generic_handler(
            SERVICE_NAME,
            {
                "BidiWriteObject": grpc.stream_stream_rpc_method_handler(
                    self.bidi_write_object,
                    request_deserializer=s.BidiWriteObjectRequest.deserialize,
                    response_serializer=s.BidiWriteObjectResponse.serialize,
                ),
                "BidiReadObject": grpc.stream_stream_rpc_method_handler(
                    self.bidi_read_object,
                    request_deserializer=s.BidiReadObjectRequest.deserialize,
                    response_serializer=s.BidiReadObjectResponse.serialize,
                ),
                "GetObject": grpc.unary_unary_rpc_method_handler(
                    self.get_object,
                    request_deserializer=s.GetObjectRequest.deserialize,
                    response_serializer=s.Object.serialize,
                ),
                "DeleteObject": grpc.unary_unary_rpc_method_handler(
                    self.delete_object,
                    request_deserializer=s.DeleteObjectRequest.deserialize,
                    response_serializer=empty_pb2.Empty.SerializeToString,
                ),
            },
        )

    # ------------------------------------------------------------ lookups
    def _lookup(
        self, bucket: str, name: str, generation: Optional[int]
    ) -> Optional[FakeObject]:
        obj = self.state.get_object(bucket, name)
        if obj is None:
            return None
        if generation and obj.generation != generation:
            return None
        return obj

    # ------------------------------------------------------------- unary
    async def get_object(self, request, context):
        self.state._record_call("GetObject", context)
        self.state.requests.append(("GetObject", request))
        await _maybe_fail(self.state._claim_injection("GetObject"), 0, context)
        generation = request.generation if "generation" in request else None
        obj = self._lookup(request.bucket, request.object_, generation)
        if obj is None:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"No such object: {request.bucket}/{request.object_}",
            )
        errors: list = []
        _check_preconditions(obj, request, errors)
        if errors:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, "; ".join(errors))
        return obj.to_proto()

    async def delete_object(self, request, context):
        self.state._record_call("DeleteObject", context)
        self.state.requests.append(("DeleteObject", request))
        await _maybe_fail(self.state._claim_injection("DeleteObject"), 0, context)
        generation = request.generation if "generation" in request else None
        obj = self._lookup(request.bucket, request.object_, generation)
        if obj is None:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"No such object: {request.bucket}/{request.object_}",
            )
        errors: list = []
        _check_preconditions(obj, request, errors)
        if errors:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, "; ".join(errors))
        del self.state.objects[(obj.bucket, obj.name)]
        return empty_pb2.Empty()

    # -------------------------------------------------------- bidi write
    async def _open_write(self, spec, context) -> FakeObject:
        resource = spec.resource
        if not resource.bucket or not resource.name:
            await context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "write_object_spec.resource must set bucket and name",
            )
        bucket = normalize_bucket(resource.bucket)
        existing = self.state.get_object(bucket, resource.name)
        errors: list = []
        _check_preconditions(existing, spec, errors)
        if errors:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, "; ".join(errors))
        now = _now()
        obj = FakeObject(
            bucket=bucket,
            name=resource.name,
            generation=self.state.next_generation(),
            appendable=bool(spec.appendable),
            metadata=dict(resource.metadata),
            create_time=now,
            update_time=now,
        )
        for attr in _COPIED_STRING_ATTRS:
            value = getattr(resource, attr)
            if value:
                setattr(obj, attr, value)
        if "custom_time" in resource:
            obj.custom_time = resource.custom_time
        if obj.appendable:
            # Appendable objects are visible (and readable) while being written.
            self.state.objects[(bucket, obj.name)] = obj
        return obj

    async def _open_append(self, spec, context) -> FakeObject:
        obj = self._lookup(spec.bucket, spec.object_, spec.generation or None)
        if obj is None:
            await context.abort(
                grpc.StatusCode.NOT_FOUND,
                f"No such object: {spec.bucket}/{spec.object_}#{spec.generation}",
            )
        if not obj.appendable:
            await context.abort(
                grpc.StatusCode.FAILED_PRECONDITION,
                "Object is not appendable",
            )
        if obj.finalized:
            await context.abort(
                grpc.StatusCode.FAILED_PRECONDITION,
                "Object is already finalized and cannot be appended to",
            )
        errors: list = []
        _check_preconditions(obj, spec, errors)
        if errors:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, "; ".join(errors))
        return obj

    def _write_handle(self, obj: FakeObject) -> _storage_v2.BidiWriteHandle:
        return _storage_v2.BidiWriteHandle(
            handle=f"wh-{obj.generation}-{obj.writer_epoch}".encode()
        )

    def _persisted_checksums(self, obj: FakeObject) -> _storage_v2.ObjectChecksums:
        return _storage_v2.ObjectChecksums(crc32c=obj.crc32c)

    def _resource_response(
        self, obj: FakeObject
    ) -> _storage_v2.BidiWriteObjectResponse:
        return _storage_v2.BidiWriteObjectResponse(
            resource=obj.to_proto(),
            write_handle=self._write_handle(obj),
            persisted_data_checksums=self._persisted_checksums(obj),
        )

    def _size_response(self, obj: FakeObject) -> _storage_v2.BidiWriteObjectResponse:
        return _storage_v2.BidiWriteObjectResponse(
            persisted_size=obj.size,
            write_handle=self._write_handle(obj),
            persisted_data_checksums=self._persisted_checksums(obj),
        )

    async def bidi_write_object(self, request_iterator, context):
        method = "BidiWriteObject"
        obj: Optional[FakeObject] = None
        epoch = -1
        self.state._record_call(method, context)
        injection = self.state._claim_injection(method)
        index = 0
        async for req in request_iterator:
            self.state.requests.append((method, req))
            await _maybe_fail(injection, index, context)
            first = index == 0
            index += 1
            if first:
                if "write_object_spec" in req:
                    obj = await self._open_write(req.write_object_spec, context)
                elif "append_object_spec" in req:
                    obj = await self._open_append(req.append_object_spec, context)
                else:
                    await context.abort(
                        grpc.StatusCode.INVALID_ARGUMENT,
                        "The first BidiWriteObjectRequest must set "
                        "write_object_spec or append_object_spec",
                    )
                obj.writer_epoch += 1
                epoch = obj.writer_epoch
            else:
                if "write_object_spec" in req or "append_object_spec" in req:
                    await context.abort(
                        grpc.StatusCode.INVALID_ARGUMENT,
                        "write_object_spec / append_object_spec are only "
                        "allowed in the first request",
                    )
                if obj.writer_epoch != epoch:
                    await context.abort(
                        grpc.StatusCode.FAILED_PRECONDITION,
                        "The upload was taken over by another writer",
                    )

            if "checksummed_data" in req:
                if obj.finalized:
                    await context.abort(
                        grpc.StatusCode.FAILED_PRECONDITION,
                        "Cannot write to a finalized object",
                    )
                cd = req.checksummed_data
                content = bytes(cd.content)
                if req.write_offset != obj.size:
                    await context.abort(
                        grpc.StatusCode.OUT_OF_RANGE,
                        f"write_offset={req.write_offset} does not match the "
                        f"persisted size {obj.size}",
                    )
                if "crc32c" in cd and cd.crc32c != crc32c(content):
                    await context.abort(
                        grpc.StatusCode.INVALID_ARGUMENT,
                        f"Checksum mismatch at write_offset={req.write_offset}: "
                        f"client crc32c={cd.crc32c}, computed={crc32c(content)}",
                    )
                obj.data.extend(content)
                obj.update_time = _now()

            if req.finish_write:
                if obj.finalized:
                    await context.abort(
                        grpc.StatusCode.FAILED_PRECONDITION,
                        "The object is already finalized",
                    )
                if "object_checksums" in req and "crc32c" in req.object_checksums:
                    want = req.object_checksums.crc32c
                    if want != obj.crc32c:
                        await context.abort(
                            grpc.StatusCode.INVALID_ARGUMENT,
                            f"Object checksum mismatch: client crc32c={want}, "
                            f"computed={obj.crc32c}",
                        )
                now = _now()
                obj.finalized = True
                obj.finalize_time = now
                obj.update_time = now
                # Non-appendable objects only become visible on finalization.
                self.state.objects[(obj.bucket, obj.name)] = obj
                yield self._resource_response(obj)
            elif first:
                yield self._resource_response(obj)
            elif req.state_lookup:
                yield self._size_response(obj)

        # Per the API, closing the stream of an unfinalized upload yields one
        # final response with the persisted size.
        if obj is not None and not obj.finalized and obj.writer_epoch == epoch:
            yield self._size_response(obj)

    # --------------------------------------------------------- bidi read
    async def _abort_out_of_range(self, context, bad: List[Tuple[int, str]]) -> None:
        range_errors = [
            _storage_v2.ReadRangeError(
                read_id=read_id,
                status=status_pb2.Status(code=code_pb2.OUT_OF_RANGE, message=msg),
            )
            for read_id, msg in bad
        ]
        detail = any_pb2.Any()
        detail.Pack(
            _storage_v2.BidiReadObjectError.pb(
                _storage_v2.BidiReadObjectError(read_range_errors=range_errors)
            )
        )
        message = "; ".join(msg for _, msg in bad)
        status = status_pb2.Status(
            code=code_pb2.OUT_OF_RANGE, message=message, details=[detail]
        )
        await context.abort(
            grpc.StatusCode.OUT_OF_RANGE,
            message,
            trailing_metadata=(
                ("grpc-status-details-bin", status.SerializeToString()),
            ),
        )

    def _range_chunks(
        self, obj: FakeObject, rng
    ) -> List[_storage_v2.BidiReadObjectResponse]:
        data = bytes(obj.data)
        size = len(data)
        if rng.read_offset < 0:
            start = max(0, size + rng.read_offset)
        else:
            start = rng.read_offset
        end = size if rng.read_length == 0 else min(size, start + rng.read_length)
        responses = []
        offset = start
        while True:
            chunk = data[offset : min(end, offset + MAX_READ_CHUNK_SIZE)]
            last = offset + len(chunk) >= end
            range_data = _storage_v2.ObjectRangeData(
                read_range=_storage_v2.ReadRange(
                    read_offset=offset,
                    read_length=len(chunk),
                    read_id=rng.read_id,
                ),
                range_end=last,
            )
            # Empty ranges (e.g. reading at EOF) carry no checksummed_data.
            if chunk:
                checksum = crc32c(chunk)
                if self.state._take_read_corruption():
                    checksum ^= 0xFFFFFFFF
                range_data.checksummed_data = _storage_v2.ChecksummedData(
                    content=chunk, crc32c=checksum
                )
            responses.append(
                _storage_v2.BidiReadObjectResponse(object_data_ranges=[range_data])
            )
            offset += len(chunk)
            if last:
                return responses

    async def bidi_read_object(self, request_iterator, context):
        method = "BidiReadObject"
        obj: Optional[FakeObject] = None
        self.state._record_call(method, context)
        injection = self.state._claim_injection(method)
        index = 0
        async for req in request_iterator:
            self.state.requests.append((method, req))
            await _maybe_fail(injection, index, context)
            first = index == 0
            index += 1
            if first:
                if "read_object_spec" not in req:
                    await context.abort(
                        grpc.StatusCode.INVALID_ARGUMENT,
                        "The first BidiReadObjectRequest must set read_object_spec",
                    )
                spec = req.read_object_spec
                generation = spec.generation if "generation" in spec else None
                obj = self._lookup(spec.bucket, spec.object_, generation)
                if obj is None:
                    await context.abort(
                        grpc.StatusCode.NOT_FOUND,
                        f"No such object: {spec.bucket}/{spec.object_}",
                    )
                errors: list = []
                _check_preconditions(obj, spec, errors)
                if errors:
                    await context.abort(
                        grpc.StatusCode.FAILED_PRECONDITION, "; ".join(errors)
                    )
                yield _storage_v2.BidiReadObjectResponse(
                    metadata=obj.to_proto(),
                    read_handle=_storage_v2.BidiReadHandle(
                        handle=self.state.next_handle("rh")
                    ),
                )

            size = obj.size
            bad: List[Tuple[int, str]] = []
            for rng in req.read_ranges:
                if rng.read_length < 0:
                    await context.abort(
                        grpc.StatusCode.INVALID_ARGUMENT,
                        f"read_length must be >= 0 (read_id={rng.read_id})",
                    )
                if rng.read_offset > size:
                    bad.append(
                        (
                            rng.read_id,
                            f"read_offset={rng.read_offset} is beyond the object "
                            f"size {size} (read_id={rng.read_id})",
                        )
                    )
            if bad:
                await self._abort_out_of_range(context, bad)
            for rng in req.read_ranges:
                for response in self._range_chunks(obj, rng):
                    yield response


async def start_fake_gcs() -> Tuple[str, grpc.aio.Server, FakeGcsState]:
    """Starts a fake GCS gRPC server on ``127.0.0.1`` with an ephemeral port.

    Returns:
        ``(endpoint, server, state)`` where ``endpoint`` is
        ``"http://127.0.0.1:<port>"``, ``server`` is the running
        ``grpc.aio.Server`` (stop it with ``await server.stop(None)``) and
        ``state`` is the :class:`FakeGcsState` used to seed objects, inspect
        requests and inject faults.
    """
    state = FakeGcsState()
    server = grpc.aio.server(
        options=[
            ("grpc.max_receive_message_length", _MAX_MESSAGE_SIZE),
            ("grpc.max_send_message_length", _MAX_MESSAGE_SIZE),
        ]
    )
    server.add_generic_rpc_handlers((FakeStorageServicer(state).generic_handler(),))
    port = server.add_insecure_port("127.0.0.1:0")
    if not port:
        raise RuntimeError("failed to bind fake GCS server to 127.0.0.1")
    await server.start()
    return f"http://127.0.0.1:{port}", server, state
