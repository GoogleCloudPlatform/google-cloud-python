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

"""Zero-copy deserializer for ``BidiReadObjectResponse`` messages.

The generated gRPC stub parses every response with proto-plus over upb, which
copies each data chunk twice (into the upb arena, then into a Python ``bytes``
for ``checksummed_data.content``) on the event-loop thread. Data responses are
structurally tiny apart from the chunk itself, so this module walks the wire
format directly and exposes ``content`` as a ``memoryview`` of the raw message
when :func:`is_supported` holds (or a single ``bytes`` slice when the installed
``google-crc32c`` only accepts ``bytes``). Responses carrying object metadata
(the first message of a stream opened without a read handle) or anything
unexpected fall back to the generated parser; the rest are returned as the
duck-typed :class:`_ZeroCopyBidiReadObjectResponse`.

:func:`wrapped_rpc` builds the matching ``BidiReadObject`` callable for a
transport; :class:`~google.cloud.storage.asyncio.async_read_object_stream._AsyncReadObjectStream`
prefers it over the generated one whenever :func:`is_enabled` holds.
"""

import os
import weakref

import google_crc32c
from google.protobuf.message import DecodeError

from google.cloud import _storage_v2
from google.cloud._storage_v2.services.storage.transports.base import (
    DEFAULT_CLIENT_INFO,
)
from google.cloud._storage_v2.services.storage.transports.grpc_asyncio import (
    StorageGrpcAsyncIOTransport,
)

# Off by default; set ``GCS_PYTHON_CLIENT_ZERO_COPY_BIDI_READ=1`` (or ``true``,
# ``yes``, ``on``) to use the wire parser instead of the generated one.
_ENV_VAR = "GCS_PYTHON_CLIENT_ZERO_COPY_BIDI_READ"
_ENABLED_VALUES = ("1", "true", "yes", "on")

# Protobuf wire types (low 3 bits of a field tag): varint, 8-byte fixed,
# length-delimited, 4-byte fixed. Groups (3, 4) are left to the generated parser.
_WT_VARINT, _WT_I64, _WT_LEN, _WT_I32 = 0, 1, 2, 5

_ReadRangePb = _storage_v2.ReadRange.pb()


class _ChecksummedData:
    __slots__ = ("content", "crc32c", "_has_crc32c")

    def __init__(self):
        # An absent content field is b"" like the generated parser; the last
        # message of a range that ends on a chunk boundary looks like that.
        self.content = b""
        self.crc32c = 0
        self._has_crc32c = False

    @property
    def _pb(self):
        return self

    def HasField(self, name):
        # "_crc32c" is the synthetic oneof of the proto3 ``optional`` field.
        if name in ("crc32c", "_crc32c"):
            return self._has_crc32c
        raise ValueError(f"Unknown field {name!r}")


class _ObjectRangeData:
    __slots__ = (
        "checksummed_data",
        "read_range",
        "range_end",
        "_has_checksummed_data",
        "_has_read_range",
    )

    def __init__(self):
        self.checksummed_data = _ChecksummedData()
        self.read_range = _ReadRangePb()
        self.range_end = False
        self._has_checksummed_data = False
        self._has_read_range = False

    @property
    def _pb(self):
        return self

    def HasField(self, name):
        if name == "checksummed_data":
            return self._has_checksummed_data
        if name == "read_range":
            return self._has_read_range
        raise ValueError(f"Unknown field {name!r}")


class _ZeroCopyBidiReadObjectResponse:
    """Duck-typed stand-in for a ``BidiReadObjectResponse`` without metadata.

    Only the attributes the async read path uses are provided:
    ``object_data_ranges``, ``read_handle``, ``metadata`` (always ``None``),
    ``HasField`` and ``_pb`` (itself, so code that unwraps proto-plus messages
    keeps working).
    """

    __slots__ = ("object_data_ranges", "read_handle", "metadata")

    def __init__(self, ranges, read_handle):
        self.object_data_ranges = ranges
        self.read_handle = read_handle
        self.metadata = None

    @property
    def _pb(self):
        return self

    def HasField(self, name):
        if name == "read_handle":
            return self.read_handle is not None
        if name == "metadata":
            return False
        raise ValueError(f"Unknown field {name!r}")


class _Malformed(ValueError):
    """Raised when the wire bytes do not look like a well-formed message."""


# A 10-byte varint carries 70 bits; like upb, keep only the low 64.
_UINT64_MASK = (1 << 64) - 1
# A field tag (``field_number << 3 | wire_type``) must fit in 32 bits, as in upb.
_UINT32_MAX = (1 << 32) - 1


def _varint(buf, i, end):
    """Decode the varint at ``buf[i]``; it must end at or before ``end``.

    Like upb, accept up to ten bytes and keep only the low 64 bits.
    """
    shift = 0
    result = 0
    while True:
        b = buf[i]
        i += 1
        result |= (b & 0x7F) << shift
        if b < 0x80:
            break
        shift += 7
        if shift > 63:
            raise _Malformed("varint longer than 10 bytes")
    if i > end:
        raise _Malformed("varint runs past its enclosing message")
    return result & _UINT64_MASK, i


def _tag(buf, i, end):
    """Decode a field tag at ``buf[i]`` into ``(field_number, wire_type, i)``.

    upb rejects field number 0, tags above 32 bits and tags encoded in more
    than five bytes.
    """
    start = i
    tag, i = _varint(buf, i, end)
    if tag < 8 or tag > _UINT32_MAX or i - start > 5:
        raise _Malformed("invalid field tag")
    return tag >> 3, tag & 7, i


def _length_prefixed(buf, i, end):
    """Return ``(start, stop)`` of the length-delimited field body at ``i``.

    upb rejects lengths encoded in more than five bytes.
    """
    start = i
    n, i = _varint(buf, i, end)
    if i - start > 5:
        raise _Malformed("field length longer than five bytes")
    stop = i + n
    if stop > end:
        raise _Malformed("field runs past its enclosing message")
    return i, stop


def _skip(buf, i, wt, end):
    if wt == _WT_VARINT:
        return _varint(buf, i, end)[1]
    if wt == _WT_LEN:
        return _length_prefixed(buf, i, end)[1]
    if wt == _WT_I64:
        i += 8
    elif wt == _WT_I32:
        i += 4
    else:
        raise _Malformed(f"unsupported wire type {wt}")
    if i > end:
        raise _Malformed("field runs past its enclosing message")
    return i


# The sub-message parsers fill in an existing object so that a singular
# embedded message occurring more than once is merged, as the generated
# parser does, instead of replacing what the earlier occurrence set.


def _parse_checksummed(cd, buf, mv, i, end):
    while i < end:
        f, wt, i = _tag(buf, i, end)
        if f == 1 and wt == _WT_LEN:
            start, i = _length_prefixed(buf, i, end)
            # Non-empty payloads alias the wire buffer; an empty one is b"".
            cd.content = mv[start:i] if mv is not None and i > start else buf[start:i]
        elif f == 2 and wt == _WT_I32:
            if i + 4 > end:
                raise _Malformed("crc32c runs past its enclosing message")
            cd.crc32c = int.from_bytes(buf[i : i + 4], "little")
            cd._has_crc32c = True
            i += 4
        else:
            i = _skip(buf, i, wt, end)


def _parse_range_data(buf, mv, i, end):
    rd = _ObjectRangeData()
    while i < end:
        f, wt, i = _tag(buf, i, end)
        if wt == _WT_LEN:
            start, i = _length_prefixed(buf, i, end)
            if f == 1:
                _parse_checksummed(rd.checksummed_data, buf, mv, start, i)
                rd._has_checksummed_data = True
            elif f == 2:
                rd.read_range.MergeFromString(buf[start:i])
                rd._has_read_range = True
        elif f == 3 and wt == _WT_VARINT:
            v, i = _varint(buf, i, end)
            rd.range_end = bool(v)
        else:
            i = _skip(buf, i, wt, end)
    return rd


_generated_deserialize = _storage_v2.BidiReadObjectResponse.deserialize


def deserialize(buf):
    """Parse a serialized ``BidiReadObjectResponse``; chunk payloads alias ``buf``.

    Anything that is not a plain data response (object metadata present, or
    bytes that do not parse cleanly) is handed to the generated parser, which
    either produces the real message or raises its usual ``DecodeError``. So
    is any buffer that is not an immutable ``bytes``: the chunks alias ``buf``,
    which is only safe when nothing can change or recycle it.
    """
    if type(buf) is not bytes:
        return _generated_deserialize(buf)
    try:
        mv = memoryview(buf) if is_supported() else None
        n = len(buf)
        i = 0
        ranges = []
        handle = None
        while i < n:
            f, wt, i = _tag(buf, i, n)
            if wt == _WT_LEN:
                start, end = _length_prefixed(buf, i, n)
                if f == 6:
                    ranges.append(_parse_range_data(buf, mv, start, end))
                elif f == 7:
                    if handle is None:
                        handle = _storage_v2.BidiReadHandle()
                    handle._pb.MergeFromString(buf[start:end])
                elif f == 4:
                    return _generated_deserialize(buf)
                i = end
            else:
                i = _skip(buf, i, wt, n)
        return _ZeroCopyBidiReadObjectResponse(ranges, handle)
    except (_Malformed, IndexError, DecodeError):
        return _generated_deserialize(buf)


_memoryview_supported = None


def is_supported():
    """Whether the installed ``google_crc32c`` can hash ``memoryview`` inputs.

    When true, :func:`deserialize` exposes chunk payloads as ``memoryview``
    slices of the gRPC wire buffer; when false, it slices ``bytes`` instead so
    checksum verification remains compatible with older ``google_crc32c``
    releases while still avoiding the intermediate upb arena copy. Both
    ``value`` and ``Checksum.update`` (used by full-object reads) must accept
    a ``memoryview``. The probe runs once per process.
    """
    global _memoryview_supported
    if _memoryview_supported is None:
        probe = memoryview(b"\0")
        try:
            google_crc32c.value(probe)
            google_crc32c.Checksum().update(probe)
        except Exception:
            _memoryview_supported = False
        else:
            _memoryview_supported = True
    return _memoryview_supported


def is_enabled():
    """Whether a stream should use the zero-copy parser.

    Off by default; set ``GCS_PYTHON_CLIENT_ZERO_COPY_BIDI_READ=1`` (or
    ``true``, ``yes``, ``on``) to turn it on.
    """
    return os.environ.get(_ENV_VAR, "").strip().lower() in _ENABLED_VALUES


_rpcs = weakref.WeakKeyDictionary()


def wrapped_rpc(transport):
    """Return the zero-copy ``BidiReadObject`` callable for ``transport``.

    The callable is the generated transport's stub with :func:`deserialize`
    swapped in, wrapped like the transport's own ``bidi_read_object`` entry:
    error mapping, no default retry or timeout, and the default
    ``x-goog-api-client`` header, which is what transports built by
    ``AsyncGrpcClient`` send on every RPC. Returns ``None`` when
    :func:`is_enabled` is false or ``transport`` is not the generated
    grpc_asyncio transport, in which case callers should use the generated
    wrapped method.
    """
    if not isinstance(transport, StorageGrpcAsyncIOTransport) or not is_enabled():
        return None
    rpc = _rpcs.get(transport)
    if rpc is None:
        stub = transport._logged_channel.stream_stream(
            "/google.storage.v2.Storage/BidiReadObject",
            request_serializer=_storage_v2.BidiReadObjectRequest.serialize,
            response_deserializer=deserialize,
        )
        rpc = transport._wrap_method(
            stub, default_timeout=None, client_info=DEFAULT_CLIENT_INFO
        )
        _rpcs[transport] = rpc
    return rpc
