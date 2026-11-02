# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import functools
import itertools
from unittest import mock

import pytest  # type: ignore

import google_crc32c

EMPTY = b""
EMPTY_CRC = 0x00000000

# From: https://tools.ietf.org/html/rfc3720#appendix-B.4
#
#   32 bytes of zeroes:
#
#     Byte:        0  1  2  3
#
#        0:       00 00 00 00
#      ...
#       28:       00 00 00 00
#
#      CRC:       aa 36 91 8a

ALL_ZEROS = b"\x00" * 32
ALL_ZEROS_CRC = 0x8A9136AA

#   32 bytes of ones:
#
#     Byte:        0  1  2  3
#
#        0:       ff ff ff ff
#      ...
#       28:       ff ff ff ff
#
#      CRC:       43 ab a8 62

ALL_ONES = b"\xff" * 32
ALL_ONES_CRC = 0x62A8AB43

#
#   32 bytes of incrementing 00..1f:
#
#     Byte:        0  1  2  3
#
#        0:       00 01 02 03
#      ...
#       28:       1c 1d 1e 1f
#
#      CRC:       4e 79 dd 46

INCREMENTING = bytes(range(32))
INCREMENTING_CRC = 0x46DD794E

#
#   32 bytes of decrementing 1f..00:
#
#     Byte:        0  1  2  3
#
#        0:       1f 1e 1d 1c
#      ...
#       28:       03 02 01 00
#
#      CRC:       5c db 3f 11

DECREMENTING = bytes(reversed(range(32)))
DECREMENTING_CRC = 0x113FDB5C

#
#    An iSCSI - SCSI Read (10) Command PDU
#
#    Byte:        0  1  2  3
#
#       0:       01 c0 00 00
#       4:       00 00 00 00
#       8:       00 00 00 00
#      12:       00 00 00 00
#      16:       14 00 00 00
#      20:       00 00 04 00
#      24:       00 00 00 14
#      28:       00 00 00 18
#      32:       28 00 00 00
#      36:       00 00 00 00
#      40:       02 00 00 00
#      44:       00 00 00 00
#
#     CRC:       56 3a 96 d9

ISCSI_SCSI_READ_10_COMMAND_PDU = [
    0x01,
    0xC0,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x14,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x04,
    0x00,
    0x00,
    0x00,
    0x00,
    0x14,
    0x00,
    0x00,
    0x00,
    0x18,
    0x28,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x02,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
]
ISCSI_LENGTH = len(ISCSI_SCSI_READ_10_COMMAND_PDU)
ISCSI_BYTES = bytes(ISCSI_SCSI_READ_10_COMMAND_PDU)
ISCSI_CRC = 0xD9963A56


def iscsi_chunks(chunksize):
    for index in itertools.islice(range(ISCSI_LENGTH), 0, None, chunksize):
        yield ISCSI_SCSI_READ_10_COMMAND_PDU[index : index + chunksize]


_EXPECTED = [
    (EMPTY, EMPTY_CRC),
    (ALL_ZEROS, ALL_ZEROS_CRC),
    (ALL_ONES, ALL_ONES_CRC),
    (INCREMENTING, INCREMENTING_CRC),
    (DECREMENTING, DECREMENTING_CRC),
    (ISCSI_SCSI_READ_10_COMMAND_PDU, ISCSI_CRC),
    (ISCSI_BYTES, ISCSI_CRC),
]


def test_extend_w_empty_chunk():
    crc = 123
    assert google_crc32c.extend(crc, b"") == crc


def test_extend_w_multiple_chunks():
    crc = 0

    for chunk in iscsi_chunks(7):
        chunk_bytes = bytes(chunk)
        crc = google_crc32c.extend(crc, chunk_bytes)

    assert crc == ISCSI_CRC


def test_extend_w_reduce():
    chunks = [bytes(chunk) for chunk in iscsi_chunks(3)]
    assert functools.reduce(google_crc32c.extend, chunks, 0) == ISCSI_CRC


@pytest.mark.parametrize("chunk, expected", _EXPECTED)
def test_value(chunk, expected):
    assert google_crc32c.value(bytes(chunk)) == expected


def pytest_generate_tests(metafunc):
    if "_crc32c" in metafunc.fixturenames:
        metafunc.parametrize("_crc32c", ["python", "cext"], indirect=True)


@pytest.fixture
def _crc32c(request):
    if request.param == "python":
        from google_crc32c import python

        return python
    elif request.param == "cext":
        try:
            from google_crc32c import cext

            return cext  # pragma: NO COVER
        except ImportError:  # pragma: NO COVER
            pytest.skip("C extension not compiled")  # pragma: NO COVER
    else:  # pragma: NO COVER
        raise ValueError("invalid internal test config")


class TestChecksum(object):
    @staticmethod
    def test_ctor_defaults(_crc32c):
        helper = google_crc32c.Checksum()
        assert helper._crc == 0

    @staticmethod
    def test_ctor_explicit(_crc32c):
        chunk = b"DEADBEEF"
        helper = google_crc32c.Checksum(chunk)
        assert helper._crc == google_crc32c.value(chunk)

    @staticmethod
    def test_update_array():
        import array

        from google_crc32c import python

        chunk = array.array("B", b"DEADBEEF")
        helper = python.Checksum()
        helper.update(chunk)
        assert helper._crc == python.value(b"DEADBEEF")

    @staticmethod
    def test_update(_crc32c):
        chunk = b"DEADBEEF"
        helper = google_crc32c.Checksum()
        helper.update(chunk)
        assert helper._crc == google_crc32c.value(chunk)

    @staticmethod
    def test_update_w_multiple_chunks(_crc32c):
        helper = google_crc32c.Checksum()

        for index in itertools.islice(range(ISCSI_LENGTH), 0, None, 7):
            chunk = ISCSI_SCSI_READ_10_COMMAND_PDU[index : index + 7]
            helper.update(bytes(chunk))

        assert helper._crc == ISCSI_CRC

    @staticmethod
    def test_digest_zero(_crc32c):
        helper = google_crc32c.Checksum()
        assert helper.digest() == b"\x00" * 4

    @staticmethod
    def test_digest_nonzero(_crc32c):
        helper = google_crc32c.Checksum()
        helper._crc = 0x01020304
        assert helper.digest() == b"\x01\x02\x03\x04"

    @staticmethod
    def test_hexdigest_zero(_crc32c):
        helper = google_crc32c.Checksum()
        assert helper.hexdigest() == b"00" * 4

    @staticmethod
    def test_hexdigest_nonzero(_crc32c):
        helper = google_crc32c.Checksum()
        helper._crc = 0x091A3B2C
        assert helper.hexdigest() == b"091a3b2c"

    @staticmethod
    def test_copy(_crc32c):
        chunk = b"DEADBEEF"
        helper = google_crc32c.Checksum(chunk)
        clone = helper.copy()
        before = helper._crc
        helper.update(b"FACEDACE")
        assert clone._crc == before

    @staticmethod
    @pytest.mark.parametrize("chunksize", [1, 3, 5, 7, 11, 13, ISCSI_LENGTH])
    def test_consume_stream(_crc32c, chunksize):
        helper = google_crc32c.Checksum()
        expected = [bytes(chunk) for chunk in iscsi_chunks(chunksize)]
        stream = mock.Mock(spec=["read"])
        stream.read.side_effect = expected + [b""]

        found = list(helper.consume(stream, chunksize))

        assert helper._crc == ISCSI_CRC
        assert found == expected
        for call in stream.read.call_args_list:
            assert call == mock.call(chunksize)


def test_common_checksum():
    from google_crc32c._checksum import CommonChecksum

    class DummyChecksum(CommonChecksum):
        __slots__ = ("_crc",)

    checksum = DummyChecksum()
    assert checksum._crc == 0
    with pytest.raises(NotImplementedError):
        checksum.update(b"data")

    with pytest.raises(NotImplementedError):
        DummyChecksum(b"foo")
