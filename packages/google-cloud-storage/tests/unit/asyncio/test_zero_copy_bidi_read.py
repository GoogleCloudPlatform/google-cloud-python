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

"""Tests for the zero-copy ``BidiReadObjectResponse`` deserializer."""

import logging
from unittest import mock

import google_crc32c
import grpc
import pytest
from google.api_core import client_info as api_core_client_info
from google.api_core.gapic_v1.client_info import ClientInfo
from google.auth.credentials import AnonymousCredentials
from google.protobuf.message import DecodeError

from google.cloud import _storage_v2
from google.cloud._storage_v2.services.storage.transports.base import (
    DEFAULT_CLIENT_INFO,
)
from google.cloud._storage_v2.services.storage.transports.grpc_asyncio import (
    StorageGrpcAsyncIOTransport,
)
from google.cloud.storage.asyncio import _zero_copy_bidi_read
from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from google.cloud.storage.asyncio.async_read_object_stream import (
    _AsyncReadObjectStream,
)

PAYLOAD = bytes(range(256)) * 8
_orig_crc32c_value = google_crc32c.value
_orig_checksum_update = google_crc32c.Checksum.update


@pytest.fixture(autouse=True)
def _crc32c_accepts_memoryview(monkeypatch):
    monkeypatch.setattr(
        google_crc32c, "value", lambda data: _orig_crc32c_value(bytes(data))
    )
    monkeypatch.setattr(
        google_crc32c.Checksum,
        "update",
        lambda self, chunk: _orig_checksum_update(self, bytes(chunk)),
    )
    # is_supported() caches its probe; re-probe the patched functions.
    monkeypatch.setattr(_zero_copy_bidi_read, "_memoryview_supported", None)


# Field numbers from google/storage/v2/storage.proto.
_RESPONSE_METADATA, _RESPONSE_RANGES, _RESPONSE_HANDLE = 4, 6, 7
_RANGE_CHECKSUMMED, _RANGE_READ_RANGE, _RANGE_END = 1, 2, 3
_CHECKSUMMED_CONTENT, _CHECKSUMMED_CRC32C = 1, 2
_READ_RANGE_OFFSET, _READ_RANGE_LENGTH, _READ_RANGE_ID = 1, 2, 3
_HANDLE_HANDLE = 1
_UNKNOWN = 15

# --- minimal wire-format encoder -----------------------------------------------


def _varint(value):
    out = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        if not value:
            out.append(byte)
            return bytes(out)
        out.append(byte | 0x80)


def _tag(number, wire_type):
    return _varint(number << 3 | wire_type)


def _varint_field(number, value):
    return _tag(number, 0) + _varint(value)


def _i64_field(number, value):
    return _tag(number, 1) + value.to_bytes(8, "little")


def _len_field(number, payload):
    return _tag(number, 2) + _varint(len(payload)) + payload


def _i32_field(number, value):
    return _tag(number, 5) + value.to_bytes(4, "little")


def _read_range(offset=4096, length=len(PAYLOAD), read_id=7, extra=b""):
    return (
        _varint_field(_READ_RANGE_OFFSET, offset)
        + _varint_field(_READ_RANGE_LENGTH, length)
        + _varint_field(_READ_RANGE_ID, read_id)
        + extra
    )


def _checksummed(content=PAYLOAD, crc32c=None, extra=b""):
    body = _len_field(_CHECKSUMMED_CONTENT, content)
    if crc32c is not None:
        body += _i32_field(_CHECKSUMMED_CRC32C, crc32c)
    return body + extra


def _range_data(checksummed=None, read_range=None, range_end=True, extra=b""):
    body = b""
    if checksummed is not None:
        body += _len_field(_RANGE_CHECKSUMMED, checksummed)
    if read_range is not None:
        body += _len_field(_RANGE_READ_RANGE, read_range)
    if range_end:
        body += _varint_field(_RANGE_END, 1)
    return body + extra


def _response(*ranges, handle=None, extra=b""):
    body = b"".join(_len_field(_RESPONSE_RANGES, r) for r in ranges)
    if handle is not None:
        body += _len_field(_RESPONSE_HANDLE, handle)
    return body + extra


def _data_response(content=PAYLOAD, crc32c=None, handle=None):
    return _response(
        _range_data(_checksummed(content, crc32c), _read_range(length=len(content))),
        handle=None if handle is None else _len_field(_HANDLE_HANDLE, handle),
    )


def _assert_same_as_generated(buf):
    """Parse ``buf`` with both parsers and check the zero-copy one matches."""
    expected = _storage_v2.BidiReadObjectResponse.deserialize(buf)
    actual = _zero_copy_bidi_read.deserialize(buf)

    assert isinstance(actual, _zero_copy_bidi_read._ZeroCopyBidiReadObjectResponse)
    assert actual.metadata is None
    assert not actual.HasField("metadata")
    assert actual.HasField("read_handle") == expected._pb.HasField("read_handle")
    if actual.HasField("read_handle"):
        assert isinstance(actual.read_handle, _storage_v2.BidiReadHandle)
        assert actual.read_handle.handle == expected.read_handle.handle
    else:
        assert actual.read_handle is None

    assert len(actual.object_data_ranges) == len(expected.object_data_ranges)
    for got, want in zip(actual.object_data_ranges, expected.object_data_ranges):
        assert got.HasField("read_range") == want._pb.HasField("read_range")
        assert got.HasField("checksummed_data") == want._pb.HasField("checksummed_data")
        assert got.read_range.read_offset == want.read_range.read_offset
        assert got.read_range.read_length == want.read_range.read_length
        assert got.read_range.read_id == want.read_range.read_id
        assert got.range_end == want.range_end
        # Non-empty payloads are views of the wire buffer, empty ones b"".
        assert type(got.checksummed_data.content) is (
            memoryview if want.checksummed_data.content else bytes
        )
        assert bytes(got.checksummed_data.content) == want.checksummed_data.content
        assert got.checksummed_data.HasField(
            "crc32c"
        ) == want.checksummed_data._pb.HasField("crc32c")
        assert got.checksummed_data.crc32c == want.checksummed_data.crc32c
        # Code that unwraps proto-plus messages with ``._pb`` sees the same,
        # including the proto3 ``optional`` field's synthetic oneof.
        assert got._pb.HasField("read_range") == want._pb.HasField("read_range")
        assert got.checksummed_data._pb.HasField(
            "_crc32c"
        ) == want.checksummed_data._pb.HasField("_crc32c")
    return actual


# --- deserialize ---------------------------------------------------------------


# Per-case checks for test_deserialize, run after the equivalence assertions.


def _check_field_values(buf, response):
    # Literal values, independent of the generated parser used as the oracle.
    [range_data] = response.object_data_ranges
    assert range_data.read_range.read_offset == 4096
    assert range_data.read_range.read_length == len(PAYLOAD)
    assert range_data.read_range.read_id == 7
    assert range_data.range_end is True
    assert bytes(range_data.checksummed_data.content) == PAYLOAD
    assert range_data.checksummed_data.crc32c == google_crc32c.value(PAYLOAD)


def _check_content_is_a_view_of_the_wire_buffer(buf, response):
    assert response.object_data_ranges[0].checksummed_data.content.obj is buf


def _check_read_handle_is_a_bidi_read_handle(buf, response):
    assert response.read_handle.handle == b"opaque"
    # The SDK feeds a captured handle straight back into the next open.
    spec = _storage_v2.BidiReadObjectSpec(read_handle=response.read_handle)
    assert spec.read_handle.handle == b"opaque"


_UNKNOWN_FIELDS = (
    _varint_field(_UNKNOWN, 1)
    + _i64_field(_UNKNOWN, 2)
    + _i32_field(_UNKNOWN, 3)
    + _len_field(_UNKNOWN, b"ignored")
)


@pytest.mark.parametrize(
    "buf, check",
    [
        pytest.param(
            _data_response(crc32c=google_crc32c.value(PAYLOAD)),
            _check_field_values,
            id="data",
        ),
        pytest.param(
            _data_response(), _check_content_is_a_view_of_the_wire_buffer, id="view"
        ),
        pytest.param(
            _data_response(handle=b"opaque"),
            _check_read_handle_is_a_bidi_read_handle,
            id="read_handle",
        ),
        pytest.param(
            _storage_v2.BidiReadObjectResponse.serialize(
                _storage_v2.BidiReadObjectResponse(
                    object_data_ranges=[
                        _storage_v2.ObjectRangeData(
                            checksummed_data=_storage_v2.ChecksummedData(
                                content=PAYLOAD, crc32c=google_crc32c.value(PAYLOAD)
                            ),
                            read_range=_storage_v2.ReadRange(
                                read_offset=4096, read_length=len(PAYLOAD), read_id=7
                            ),
                            range_end=True,
                        )
                    ],
                    read_handle=_storage_v2.BidiReadHandle(handle=b"opaque"),
                )
            ),
            None,
            id="proto_plus_serialization",
        ),
        pytest.param(_data_response(), None, id="without_crc32c"),
        pytest.param(
            _response(
                _range_data(
                    _checksummed(b"first"), _read_range(0, 5, 1), range_end=False
                ),
                _range_data(_checksummed(b"second"), _read_range(5, 6, 2)),
            ),
            None,
            id="multiple_ranges",
        ),
        pytest.param(b"", None, id="empty_message"),
        pytest.param(
            _response(_range_data(_checksummed())), None, id="range_without_read_range"
        ),
        pytest.param(
            _response(_range_data(read_range=_read_range())),
            None,
            id="range_without_checksummed_data",
        ),
        pytest.param(
            _data_response() + _UNKNOWN_FIELDS, None, id="unknown_top_level_fields"
        ),
        pytest.param(
            _response(
                _range_data(
                    _checksummed(extra=_UNKNOWN_FIELDS),
                    _read_range(extra=_UNKNOWN_FIELDS),
                    extra=_UNKNOWN_FIELDS,
                ),
                handle=_len_field(_HANDLE_HANDLE, b"opaque") + _UNKNOWN_FIELDS,
            ),
            None,
            id="unknown_nested_fields",
        ),
        pytest.param(
            _response(
                _range_data(
                    read_range=_tag(_READ_RANGE_ID, 0) + (b"\xff" * 9 + b"\x7f")
                )
            ),
            None,
            id="over_long_varint_keeps_low_64_bits",
        ),
        pytest.param(
            _response(
                _range_data(
                    extra=_len_field(
                        _RANGE_READ_RANGE, _varint_field(_READ_RANGE_OFFSET, 4096)
                    )
                    + _len_field(_RANGE_READ_RANGE, _varint_field(_READ_RANGE_ID, 7))
                    + _len_field(
                        _RANGE_CHECKSUMMED,
                        _len_field(_CHECKSUMMED_CONTENT, PAYLOAD),
                    )
                    + _len_field(
                        _RANGE_CHECKSUMMED,
                        _i32_field(_CHECKSUMMED_CRC32C, 1234),
                    )
                ),
                handle=_len_field(_HANDLE_HANDLE, b"opaque"),
            )
            + _len_field(_RESPONSE_HANDLE, b""),
            None,
            id="merges_split_sub_messages",
        ),
    ],
)
def test_deserialize(buf, check):
    response = _assert_same_as_generated(buf)
    if check is not None:
        check(buf, response)


@pytest.mark.parametrize(
    "offset, length, read_id",
    [
        pytest.param(-1, -1, -1, id="minus_one"),
        pytest.param(-5, 0, -(1 << 55), id="negative"),
        pytest.param(-(1 << 63), (1 << 63) - 1, 1, id="int64_extremes"),
    ],
)
def test_deserialize_signed_int64_read_range(offset, length, read_id):
    # read_offset, read_length and read_id are int64; negative values travel
    # as ten-byte two's-complement varints.
    message = _storage_v2.BidiReadObjectResponse(
        object_data_ranges=[
            _storage_v2.ObjectRangeData(
                read_range=_storage_v2.ReadRange(
                    read_offset=offset, read_length=length, read_id=read_id
                )
            )
        ]
    )
    response = _assert_same_as_generated(
        _storage_v2.BidiReadObjectResponse.serialize(message)
    )
    read_range = response.object_data_ranges[0].read_range
    assert (read_range.read_offset, read_range.read_length, read_range.read_id) == (
        offset,
        length,
        read_id,
    )


def test_deserialize_metadata_response_uses_generated_parser():
    metadata = _storage_v2.Object(name="o", bucket="projects/_/buckets/b", size=10)
    buf = _storage_v2.BidiReadObjectResponse.serialize(
        _storage_v2.BidiReadObjectResponse(metadata=metadata)
    )
    response = _zero_copy_bidi_read.deserialize(buf)
    assert isinstance(response, _storage_v2.BidiReadObjectResponse)
    assert response.metadata.size == 10


def test_deserialize_unknown_group_uses_generated_parser():
    # Start-group/end-group wire types are valid protobuf that the zero-copy
    # path does not understand; the generated parser keeps them as unknown fields.
    buf = _data_response() + _tag(_UNKNOWN, 3) + _tag(_UNKNOWN, 4)
    response = _zero_copy_bidi_read.deserialize(buf)
    assert isinstance(response, _storage_v2.BidiReadObjectResponse)
    assert response.object_data_ranges[0].checksummed_data.content == PAYLOAD


@pytest.mark.parametrize(
    "buf",
    [
        pytest.param(
            # object_data_ranges (6 bytes) whose checksummed_data claims 8 bytes,
            # followed by a well-formed read_handle.
            bytes([0x32, 0x06, 0x0A, 0x08]) + b"abcd" + bytes([0x3A, 0x02, 0x0A, 0x00]),
            id="inner_length_past_enclosing_message",
        ),
        pytest.param(
            bytes([0x32]) + b"\x80" * 10 + b"\x00", id="varint_longer_than_10_bytes"
        ),
        pytest.param(bytes([0x32, 0x10, 0x0A, 0x00]), id="truncated_message"),
        pytest.param(
            _response(_range_data(_checksummed()))[:-3], id="truncated_tag_varint"
        ),
        pytest.param(
            _response(_range_data(_checksummed(extra=_tag(_CHECKSUMMED_CRC32C, 5)))),
            id="crc32c_past_enclosing_message",
        ),
        pytest.param(
            _response(_range_data(read_range=_tag(_READ_RANGE_OFFSET, 0) + b"\x80")),
            id="read_range_varint_runs_past_enclosing_message",
        ),
        pytest.param(
            _response(_range_data(range_end=False, extra=_tag(_RANGE_END, 0) + b"\x80"))
            + _varint_field(_UNKNOWN, 1),
            id="range_end_varint_runs_past_enclosing_message",
        ),
        pytest.param(
            _data_response() + _tag(_UNKNOWN, 1) + b"\x00" * 3,
            id="truncated_fixed64",
        ),
        pytest.param(
            _data_response() + _tag(_UNKNOWN, 5) + b"\x00",
            id="truncated_fixed32",
        ),
        pytest.param(b"\x00\x00", id="field_number_zero"),
        pytest.param(
            _response(_range_data(extra=b"\x00\x00")),
            id="field_number_zero_in_range_data",
        ),
        pytest.param(
            _response(_range_data(_checksummed(extra=b"\x00\x00"))),
            id="field_number_zero_in_checksummed_data",
        ),
        pytest.param(
            _response(_range_data(read_range=_read_range(extra=b"\x00\x00"))),
            id="field_number_zero_in_read_range",
        ),
        pytest.param(
            _response(handle=b"\x00\x00"),
            id="field_number_zero_in_read_handle",
        ),
        pytest.param(
            # Wire type 6 ensures the pure-Python protobuf backend also raises
            # DecodeError after _tag() rejects the >32-bit tag value.
            _tag(1 << 29, 6) + b"\x01" + _data_response(),
            id="field_number_too_large",
        ),
        pytest.param(
            # Field 6 / wire type 6 padded to a six-byte varint: _tag() rejects
            # i - start > 5 before inspecting the wire type, and both upb and
            # the pure-Python backend raise DecodeError on the fallback call.
            b"\xb6\x80\x80\x80\x80\x00" + _varint(2) + _varint_field(_RANGE_END, 1),
            id="tag_longer_than_five_bytes",
        ),
    ],
)
def test_deserialize_malformed_input_raises_like_generated_parser(buf):
    with pytest.raises(DecodeError):
        _storage_v2.BidiReadObjectResponse.deserialize(buf)
    with pytest.raises(DecodeError):
        _zero_copy_bidi_read.deserialize(buf)


@pytest.mark.parametrize(
    "buf",
    [
        pytest.param(b"\x32\x80\x80\x80\x80\x80\x00", id="six_byte_length"),
        pytest.param(b"\x32" + b"\x80" * 9 + b"\x02", id="length_wraps_to_zero"),
        pytest.param(
            b"\x32\x09\x0a\x07\x0a\x80\x80\x80\x80\x80\x00",
            id="nested_six_byte_length",
        ),
    ],
)
def test_deserialize_defers_overlong_length_prefix_to_generated_parser(
    monkeypatch, buf
):
    # upb in protobuf 7 rejects a length encoded in more than five bytes while
    # protobuf 6 and the pure-Python backend accept it, so the zero-copy
    # parser leaves the verdict to the installed generated parser.
    monkeypatch.setattr(
        _zero_copy_bidi_read,
        "_generated_deserialize",
        lambda data: mock.sentinel.generated,
    )
    assert _zero_copy_bidi_read.deserialize(buf) is mock.sentinel.generated


def test_has_field_rejects_unknown_names():
    response = _zero_copy_bidi_read.deserialize(_data_response(crc32c=1))
    [range_data] = response.object_data_ranges
    for message in (response, range_data, range_data.checksummed_data):
        with pytest.raises(ValueError):
            message.HasField("no_such_field")


def test_zero_copy_response_pb_is_itself():
    # ReadsResumptionStrategy unwraps ``response._pb`` before calling HasField.
    response = _zero_copy_bidi_read.deserialize(_data_response())
    assert response._pb is response


# --- is_supported / is_enabled -------------------------------------------------


def test_is_supported_requires_crc32c_to_accept_memoryview(monkeypatch):
    probed_with = []

    def bytes_only(data):
        probed_with.append(type(data))
        raise TypeError("argument 1 must be read-only bytes-like object")

    monkeypatch.setattr(google_crc32c, "value", bytes_only)
    assert _zero_copy_bidi_read.is_supported() is False
    assert probed_with == [memoryview]
    monkeypatch.setattr(google_crc32c, "value", lambda data: len(data))
    monkeypatch.setattr(_zero_copy_bidi_read, "_memoryview_supported", None)
    assert _zero_copy_bidi_read.is_supported() is True


def test_is_supported_probes_crc32c_once(monkeypatch):
    probes = []

    def counting_value(data):
        probes.append(type(data))
        return 0

    monkeypatch.setattr(google_crc32c, "value", counting_value)
    assert _zero_copy_bidi_read.is_supported() is True
    assert _zero_copy_bidi_read.is_supported() is True
    assert probes == [memoryview]


def test_is_supported_requires_checksum_update_to_accept_memoryview(monkeypatch):
    # Full-object reads also feed each chunk to Checksum.update.
    probed_with = []

    def bytes_only(self, chunk):
        probed_with.append(type(chunk))
        raise TypeError("argument 2 must be read-only bytes-like object")

    monkeypatch.setattr(google_crc32c.Checksum, "update", bytes_only)
    assert _zero_copy_bidi_read.is_supported() is False
    assert probed_with == [memoryview]


def test_deserialize_slices_bytes_when_memoryview_crc32c_not_supported(monkeypatch):
    monkeypatch.setattr(_zero_copy_bidi_read, "is_supported", lambda: False)
    response = _zero_copy_bidi_read.deserialize(_data_response(crc32c=1))
    assert isinstance(response, _zero_copy_bidi_read._ZeroCopyBidiReadObjectResponse)
    content = response.object_data_ranges[0].checksummed_data.content
    assert type(content) is bytes
    assert content == PAYLOAD


@pytest.mark.parametrize("supported", [False, True])
def test_deserialize_empty_chunk_content_is_bytes(monkeypatch, supported):
    # The last message of a read that ends on a chunk boundary carries a
    # checksum and range_end but no content field; crc32c releases that do
    # not take memoryview must still be able to hash it.
    monkeypatch.setattr(_zero_copy_bidi_read, "is_supported", lambda: supported)
    buf = _response(
        _range_data(
            _i32_field(_CHECKSUMMED_CRC32C, google_crc32c.value(b"")),
            _read_range(length=0),
        )
    )
    response = _zero_copy_bidi_read.deserialize(buf)
    checksummed = response.object_data_ranges[0].checksummed_data
    assert type(checksummed.content) is bytes
    assert checksummed.content == b""
    assert checksummed.HasField("crc32c")
    _assert_same_as_generated(buf)


@pytest.mark.parametrize("value", [None, "", "0", "false", "No", " off "])
def test_is_enabled_defaults_to_off(monkeypatch, value):
    assert _zero_copy_bidi_read._ENV_VAR == "GCS_PYTHON_CLIENT_ZERO_COPY_BIDI_READ"
    if value is None:
        monkeypatch.delenv(_zero_copy_bidi_read._ENV_VAR, raising=False)
    else:
        monkeypatch.setenv(_zero_copy_bidi_read._ENV_VAR, value)
    assert _zero_copy_bidi_read.is_enabled() is False


@pytest.mark.parametrize("value", ["1", "true", "Yes", " on "])
def test_is_enabled_by_environment(monkeypatch, value):
    monkeypatch.setenv(_zero_copy_bidi_read._ENV_VAR, value)
    assert _zero_copy_bidi_read.is_enabled() is True


@pytest.mark.parametrize("wrap", [bytearray, memoryview])
def test_deserialize_only_aliases_immutable_bytes(wrap):
    # A mutable or recyclable buffer must not be aliased by the chunks.
    response = _zero_copy_bidi_read.deserialize(wrap(_data_response(crc32c=1)))
    assert isinstance(response, _storage_v2.BidiReadObjectResponse)
    assert isinstance(response.object_data_ranges[0].checksummed_data.content, bytes)


# --- wrapped_rpc ---------------------------------------------------------------


def _transport(target):
    # Built like AsyncGrpcClient's transports, without client_info.
    return StorageGrpcAsyncIOTransport(
        channel=grpc.aio.insecure_channel(target),
        credentials=AnonymousCredentials(),
    )


def test_wrapped_rpc_ignores_transports_it_does_not_know(monkeypatch):
    monkeypatch.setenv(_zero_copy_bidi_read._ENV_VAR, "1")
    assert _zero_copy_bidi_read.wrapped_rpc(object()) is None


@pytest.mark.asyncio
async def test_wrapped_rpc_returns_none_when_not_enabled(monkeypatch):
    monkeypatch.setenv(_zero_copy_bidi_read._ENV_VAR, "0")
    transport = _transport("localhost:1")
    try:
        assert _zero_copy_bidi_read.wrapped_rpc(transport) is None
    finally:
        await transport.close()


@pytest.mark.asyncio
async def test_wrapped_rpc_is_built_once_per_transport(monkeypatch):
    monkeypatch.setenv(_zero_copy_bidi_read._ENV_VAR, "1")
    transport = _transport("localhost:1")
    other = _transport("localhost:1")
    try:
        rpc = _zero_copy_bidi_read.wrapped_rpc(transport)
        assert rpc is not None
        assert rpc is not transport._wrapped_methods[transport.bidi_read_object]
        assert _zero_copy_bidi_read.wrapped_rpc(transport) is rpc
        assert _zero_copy_bidi_read.wrapped_rpc(other) is not rpc
    finally:
        await transport.close()
        await other.close()


# --- end to end through _AsyncReadObjectStream ---------------------------------


class _FakeStorageServer:
    """In-process gRPC server that answers BidiReadObject with canned bytes."""

    def __init__(self, responses):
        self._responses = list(responses)
        self.requests = []
        self.invocation_metadata = None
        self._server = grpc.aio.server()
        handler = grpc.method_handlers_generic_handler(
            "google.storage.v2.Storage",
            {"BidiReadObject": grpc.stream_stream_rpc_method_handler(self._handle)},
        )
        self._server.add_generic_rpc_handlers((handler,))
        self._port = self._server.add_insecure_port("localhost:0")

    @property
    def target(self):
        return f"localhost:{self._port}"

    async def _handle(self, request_iterator, context):
        self.invocation_metadata = dict(context.invocation_metadata())
        async for request in request_iterator:
            self.requests.append(_storage_v2.BidiReadObjectRequest.deserialize(request))
            yield self._responses.pop(0)

    async def __aenter__(self):
        await self._server.start()
        return self

    async def __aexit__(self, *exc_info):
        await self._server.stop(None)


@pytest.fixture
def keep_google_logger_propagation(monkeypatch):
    # Building a real GAPIC client runs api-core's client_logging
    # initialization, which switches off propagation on the "google" logger
    # and would hide log records from ``caplog`` in later test modules.
    logger = logging.getLogger("google")
    monkeypatch.setattr(logger, "propagate", logger.propagate)


@pytest.mark.asyncio
@pytest.mark.parametrize("enabled", [True, False])
async def test_read_object_stream_end_to_end(
    monkeypatch, keep_google_logger_propagation, enabled
):
    monkeypatch.setattr(_zero_copy_bidi_read, "is_supported", lambda: True)
    monkeypatch.setenv(_zero_copy_bidi_read._ENV_VAR, "1" if enabled else "0")
    crc = google_crc32c.value(PAYLOAD)
    first = _storage_v2.BidiReadObjectResponse.serialize(
        _storage_v2.BidiReadObjectResponse(
            metadata=_storage_v2.Object(
                name="o", bucket="projects/_/buckets/b", generation=5, size=2048
            ),
            read_handle=_storage_v2.BidiReadHandle(handle=b"opaque"),
        )
    )
    second = _data_response(crc32c=crc)

    async with _FakeStorageServer([first, second]) as server:
        transport = _transport(server.target)
        client = _storage_v2.StorageAsyncClient(transport=transport)
        stream = _AsyncReadObjectStream(
            client=client,
            bucket_name="b",
            object_name="o",
        )
        try:
            await stream.open()
            assert stream.generation_number == 5
            assert stream.persisted_size == 2048
            assert stream.read_handle.handle == b"opaque"

            await stream.send(
                _storage_v2.BidiReadObjectRequest(
                    read_ranges=[
                        _storage_v2.ReadRange(
                            read_offset=4096, read_length=len(PAYLOAD), read_id=7
                        )
                    ]
                )
            )
            response = await stream.recv()
            await stream.close()
        finally:
            await transport.close()

    [range_data] = response.object_data_ranges
    content = range_data.checksummed_data.content
    assert isinstance(content, memoryview if enabled else bytes)
    assert bytes(content) == PAYLOAD
    assert range_data.checksummed_data.crc32c == crc
    assert range_data.read_range.read_id == 7
    assert (
        isinstance(response, _zero_copy_bidi_read._ZeroCopyBidiReadObjectResponse)
        is enabled
    )

    assert server.requests[0].read_object_spec.object_ == "o"
    assert server.requests[1].read_ranges[0].read_id == 7
    assert server.invocation_metadata["x-goog-request-params"] == (
        "bucket=projects/_/buckets/b"
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("enabled", [True, False])
@pytest.mark.parametrize(
    "client_info",
    [
        pytest.param(None, id="default"),
        pytest.param(
            api_core_client_info.ClientInfo(user_agent="gcsfs/1"), id="api_core"
        ),
        pytest.param(ClientInfo(user_agent="gcsfs/1"), id="gapic_v1"),
    ],
)
async def test_downloader_sends_same_api_client_header_with_either_parser(
    monkeypatch, keep_google_logger_propagation, enabled, client_info
):
    monkeypatch.setattr(_zero_copy_bidi_read, "is_supported", lambda: True)
    monkeypatch.setenv(_zero_copy_bidi_read._ENV_VAR, "1" if enabled else "0")
    first = _storage_v2.BidiReadObjectResponse.serialize(
        _storage_v2.BidiReadObjectResponse(
            metadata=_storage_v2.Object(name="o", bucket="projects/_/buckets/b")
        )
    )

    async with _FakeStorageServer([first]) as server:
        transports = []

        def create_grpc_client(**kwargs):
            # Like AsyncGrpcClient, build the transport without client_info,
            # after the constructor has updated the ClientInfo it was given.
            transports.append(_transport(server.target))
            return _storage_v2.StorageAsyncClient(transport=transports[0])

        with mock.patch.object(
            AsyncGrpcClient, "_create_async_grpc_client", side_effect=create_grpc_client
        ):
            client = AsyncGrpcClient(credentials=mock.Mock(), client_info=client_info)
        try:
            mrd = await AsyncMultiRangeDownloader.create_mrd(client, "b", "o")
            await mrd.close()
        finally:
            await transports[0].close()

    # The generated stub sends the transport's default header on every RPC.
    header = server.invocation_metadata["x-goog-api-client"]
    assert header.split() == DEFAULT_CLIENT_INFO.to_user_agent().split()
