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

import array

import pytest

from google.cloud.ndb import _legacy_entity_pb as entity_module
from google.cloud.ndb import _legacy_protocol_buffer as pb_module


def _get_decoder(s):
    a = array.array("B")
    a.frombytes(s)
    d = pb_module.Decoder(a, 0, len(a))
    return d


class TestEntityProto:
    @staticmethod
    def test_constructor():
        entity = entity_module.EntityProto()
        assert entity.property_ == []

    @staticmethod
    def test_TryMerge_set_kind():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x20\x2a")
        entity.TryMerge(d)
        assert entity.has_kind()
        assert entity.kind() == 42

    @staticmethod
    def test_TryMerge_set_kind_uri():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x2a\x01\x41")
        entity.TryMerge(d)
        assert entity.has_kind_uri()
        assert entity.kind_uri().decode() == "A"

    @staticmethod
    def test_TryMerge_mutable_key_app():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x6a\x03\x6a\x01\x41")
        entity.TryMerge(d)
        assert entity.key().has_app()
        assert entity.key().app.decode() == "A"

    @staticmethod
    def test_TryMerge_mutable_key_namespace():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x6a\x04\xa2\x01\x01\x42")
        entity.TryMerge(d)
        assert entity.key().has_name_space()
        assert entity.key().name_space.decode() == "B"

    @staticmethod
    def test_TryMerge_mutable_key_database():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x6a\x04\xba\x01\x01\x43")
        entity.TryMerge(d)
        assert entity.key().has_database_id()
        assert entity.key().database_id.decode() == "C"

    @staticmethod
    def test_TryMerge_mutable_key_path():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x6a\x0c\x72\x0a\x0b\x12\x01\x44\x18\x01\x22\x01\x45\x0c")
        entity.TryMerge(d)
        assert entity.has_key()  # noqa: W601
        assert entity.key().has_path()
        element = entity.key().path.element_list()[0]
        assert element.has_type()
        # assert element.type.decode() == "D"
        assert element.type == "D"
        assert element.has_id()
        assert element.id == 1
        assert element.has_name()
        assert element.name.decode() == "E"

    @staticmethod
    def test_TryMerge_mutable_key_path_not_bytes():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x6a\x0c\x72\x0a\x0b\x12\x01\x44\x18\x01\x22\x01\x45\x0c")
        entity.TryMerge(d)
        assert entity.has_key()  # noqa: W601
        assert entity.key().has_path()
        element = entity.key().path.element_list()[0]
        assert element.has_type()
        assert element.type == "D"
        # Not quite sure how this type could be set from a decoder string
        element.set_type("E")
        assert element.type == "E"

    @staticmethod
    def test_TryMerge_mutable_key_path_with_skip_data():
        entity = entity_module.EntityProto()
        d = _get_decoder(
            b"\x6a\x0f\x72\x0d\x02\x01\x01\x0b\x12\x01\x44\x18\x01\x22\x01\x45\x0c"
        )
        entity.TryMerge(d)
        assert entity.key().has_path()

    @staticmethod
    def test_TryMerge_mutable_key_path_truncated():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x6a\x03\x72\x01\x00")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            entity.TryMerge(d)

    @staticmethod
    def test_TryMerge_mutable_key_path_element_with_skip_data():
        entity = entity_module.EntityProto()
        d = _get_decoder(
            b"\x6a\x0f\x72\x0d\x0b\x02\x01\x01\x12\x01\x44\x18\x01\x22\x01\x45\x0c"
        )
        entity.TryMerge(d)
        assert entity.key().has_path()

    @staticmethod
    def test_TryMerge_mutable_key_path_element_truncated():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x6a\x04\x72\x02\x0b\x00")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            entity.TryMerge(d)

    @staticmethod
    def test_TryMerge_mutable_key_with_skip_data():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x6a\x07\x02\x01\x01\xa2\x01\x01\x42")
        entity.TryMerge(d)
        assert entity.key().has_name_space()
        assert entity.key().name_space.decode() == "B"

    @staticmethod
    def test_TryMerge_mutable_key_decode_error():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x6a\x01\x00")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            entity.TryMerge(d)

    @staticmethod
    def test_TryMerge_property_meaning():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x02\x08\x0e")
        entity.TryMerge(d)
        assert entity.property_list()[0].has_meaning()
        meaning = entity.property_list()[0].meaning()
        assert meaning == 14
        assert entity.property_list()[0].Meaning_Name(meaning) == "BLOB"

    @staticmethod
    def test_TryMerge_property_meaning_uri():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x03\x12\x01\x41")
        entity.TryMerge(d)
        assert entity.property_list()[0].has_meaning_uri()
        assert entity.property_list()[0].meaning_uri().decode() == "A"

    @staticmethod
    def test_TryMerge_property_name():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x03\x1a\x01\x41")
        entity.TryMerge(d)
        assert entity.property_list()[0].has_name()
        assert entity.property_list()[0].name().decode() == "A"

    @staticmethod
    def test_TryMerge_property_multiple():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x02\x20\x01")
        entity.TryMerge(d)
        assert entity.property_list()[0].has_multiple()
        assert entity.property_list()[0].multiple()

    @staticmethod
    def test_TryMerge_property_stashed():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x02\x30\x02")
        entity.TryMerge(d)
        assert entity.property_list()[0].has_stashed()
        assert entity.property_list()[0].stashed() == 2

    @staticmethod
    def test_TryMerge_property_computed():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x02\x38\x01")
        entity.TryMerge(d)
        assert entity.property_list()[0].has_computed()
        assert entity.property_list()[0].computed()

    @staticmethod
    def test_TryMerge_property_skip_data():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x05\x38\x01\x02\x01\x01")
        entity.TryMerge(d)
        assert entity.property_list()[0].has_computed()

    @staticmethod
    def test_TryMerge_property_truncated():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x01\x00")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            entity.TryMerge(d)

    @staticmethod
    def test_TryMerge_property_string():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x08\x1a\x01\x46\x2a\x03\x1a\x01\x47")
        entity.TryMerge(d)
        assert entity.entity_props()["F"].decode() == "G"

    @staticmethod
    def test_TryMerge_property_int():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x07\x1a\x01\x46\x2a\x02\x08\x01")
        entity.TryMerge(d)
        assert entity.entity_props()["F"] == 1

    @staticmethod
    def test_TryMerge_property_double():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x0e\x1a\x01\x46\x2a\x09\x21\x00\x00\x00\x00\x00\x00E@")
        entity.TryMerge(d)
        assert entity.entity_props()["F"] == 42.0

    @staticmethod
    def test_TryMerge_property_boolean():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x07\x1a\x01\x46\x2a\x02\x10\x01")
        entity.TryMerge(d)
        assert entity.entity_props()["F"]

    @staticmethod
    def test_TryMerge_property_point():
        entity = entity_module.EntityProto()
        d = _get_decoder(
            b"\x72\x19\x1a\x01\x46\x2a\x14\x2b\x31\x00\x00\x00\x00\x00\x00E@"
            b"\x39\x00\x00\x00\x00\x00\x00E@\x2c"
        )
        entity.TryMerge(d)
        point = entity.entity_props()["F"]
        assert point.has_x()
        assert point.x() == 42.0
        assert point.has_y()
        assert point.y() == 42.0

    @staticmethod
    def test_TryMerge_property_point_skip_data():
        entity = entity_module.EntityProto()
        d = _get_decoder(
            b"\x72\x1c\x1a\x01\x46\x2a\x17\x2b\x31\x00\x00\x00\x00\x00\x00E@"
            b"\x39\x00\x00\x00\x00\x00\x00E@\x02\x01\x01\x2c"
        )
        entity.TryMerge(d)
        point = entity.entity_props()["F"]
        assert point.has_x()
        assert point.x() == 42.0
        assert point.has_y()
        assert point.y() == 42.0

    @staticmethod
    def test_TryMerge_property_point_truncated():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x07\x1a\x01\x46\x2a\x02\x2b\x00")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            entity.TryMerge(d)

    @staticmethod
    def test_TryMerge_property_reference_app():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x0a\x1a\x01\x46\x2a\x05\x63\x6a\x01\x41\x64")
        entity.TryMerge(d)
        assert entity.entity_props()["F"].has_app()
        assert entity.entity_props()["F"].app().decode() == "A"

    @staticmethod
    def test_TryMerge_property_reference_pathelement():
        entity = entity_module.EntityProto()
        d = _get_decoder(
            b"\x72\x13\x1a\x01\x46\x2a\x0e\x63\x73\x7a\x01\x42"
            b"\x8a\x01\x01\x43\x80\x01\x01\x74\x64"
        )
        entity.TryMerge(d)
        element = entity.entity_props()["F"].pathelement_list()[0]
        assert element.has_type()
        assert element.type().decode() == "B"
        assert element.has_id()
        assert element.id() == 1
        assert element.has_name()
        assert element.name().decode() == "C"

    @staticmethod
    def test_TryMerge_property_reference_pathelement_skip_data():
        entity = entity_module.EntityProto()
        d = _get_decoder(
            b"\x72\x16\x1a\x01\x46\x2a\x11\x63\x73\x7a\x01\x42"
            b"\x8a\x01\x01\x43\x80\x01\x01\x02\x01\x01\x74\x64"
        )
        entity.TryMerge(d)
        element = entity.entity_props()["F"].pathelement_list()[0]
        assert element.has_type()
        assert element.type().decode() == "B"
        assert element.has_id()
        assert element.id() == 1
        assert element.has_name()
        assert element.name().decode() == "C"

    @staticmethod
    def test_TryMerge_property_reference_pathelement_truncated():
        entity = entity_module.EntityProto()
        d = _get_decoder(
            b"\x72\x14\x1a\x01\x46\x2a\x0f\x63\x73\x7a\x01\x42"
            b"\x8a\x01\x01\x43\x80\x01\x01\x00\x74\x64"
        )
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            entity.TryMerge(d)

    @staticmethod
    def test_TryMerge_property_reference_name_space():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x0b\x1a\x01\x46\x2a\x06\x63\xa2\x01\x01\x41\x64")
        entity.TryMerge(d)
        assert entity.entity_props()["F"].has_name_space()
        assert entity.entity_props()["F"].name_space().decode() == "A"

    @staticmethod
    def test_TryMerge_property_reference_database_id():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x0b\x1a\x01\x46\x2a\x06\x63\xba\x01\x01\x41\x64")
        entity.TryMerge(d)
        assert entity.entity_props()["F"].has_database_id()
        assert entity.entity_props()["F"].database_id().decode() == "A"

    @staticmethod
    def test_TryMerge_property_reference_skip_data():
        entity = entity_module.EntityProto()
        d = _get_decoder(
            b"\x72\x0d\x1a\x01\x46\x2a\x08\x63\x02\x01\x01\x6a\x01\x41\x64"
        )
        entity.TryMerge(d)
        assert entity.entity_props()["F"].has_app()
        assert entity.entity_props()["F"].app().decode() == "A"

    @staticmethod
    def test_TryMerge_property_reference_truncated():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x07\x1a\x01\x46\x2a\x02\x63\x00")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            entity.TryMerge(d)

    @staticmethod
    def test_TryMerge_property_value_skip_data():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x0a\x1a\x01\x46\x2a\x05\x02\x01\x01\x10\x01")
        entity.TryMerge(d)
        assert entity.entity_props()["F"] == 1

    @staticmethod
    def test_TryMerge_property_value_truncated():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x72\x03\x2a\x01\x00")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            entity.TryMerge(d)

    @staticmethod
    def test_TryMerge_raw_property_string():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x7a\x08\x1a\x01\x46\x2a\x03\x1a\x01\x47")
        entity.TryMerge(d)
        assert entity.entity_props()["F"].decode() == "G"

    @staticmethod
    def test_TryMerge_with_skip_data():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x02\x01\x01\x7a\x08\x1a\x01\x46\x2a\x03\x1a\x01\x47")
        entity.TryMerge(d)
        assert entity.entity_props()["F"].decode() == "G"

    @staticmethod
    def test_TryMerge_decode_error():
        entity = entity_module.EntityProto()
        d = _get_decoder(b"\x00")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            entity.TryMerge(d)

    @staticmethod
    def test__get_property_value_empty_property():
        entity = entity_module.EntityProto()
        prop = entity_module.PropertyValue()
        assert entity._get_property_value(prop) is None


class TestDecoder:
    @staticmethod
    def test_prefixed_string_truncated():
        d = _get_decoder(b"\x10")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.getPrefixedString()

    @staticmethod
    def test_boolean_corrupted():
        d = _get_decoder(b"\x10")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.getBoolean()

    @staticmethod
    def test_double_truncated():
        d = _get_decoder(b"\x10")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.getDouble()

    @staticmethod
    def test_get8_truncated():
        d = _get_decoder(b"")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.get8()

    @staticmethod
    def test_get16():
        d = _get_decoder(b"\x01\x00")
        assert d.get16() == 1

    @staticmethod
    def test_get16_truncated():
        d = _get_decoder(b"\x10")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.get16()

    @staticmethod
    def test_get32():
        d = _get_decoder(b"\x01\x00\x00\x00")
        assert d.get32() == 1

    @staticmethod
    def test_getVarInt32_negative():
        d = _get_decoder(b"\xc7\xf5\xff\xff\xff\xff\xff\xff\xff\x01")
        assert d.getVarInt32() == -1337

    @staticmethod
    def test_get32_truncated():
        d = _get_decoder(b"\x10")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.get32()

    @staticmethod
    def test_get64():
        d = _get_decoder(b"\x01\x00\x00\x00\x00\x00\x00\x00")
        assert d.get64() == 1

    @staticmethod
    def test_getVarInt64_negative():
        d = _get_decoder(b"\xc7\xf5\xff\xff\xff\xff\xff\xff\xff\x01")
        assert d.getVarInt64() == -1337

    @staticmethod
    def test_get64_truncated():
        d = _get_decoder(b"\x10")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.get64()

    @staticmethod
    def test_skip_truncated():
        d = _get_decoder(b"\x10")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.skip(5)

    @staticmethod
    def test_skipData_numeric():
        d = _get_decoder(b"\x01")
        d.skipData(0)
        assert d.idx == 1

    @staticmethod
    def test_skipData_double():
        d = _get_decoder(b"\x01\x00\x00\x00\x00\x00\x00\x00")
        d.skipData(1)
        assert d.idx == 8

    @staticmethod
    def test_skipData_float():
        d = _get_decoder(b"\x01\x00\x00\x00")
        d.skipData(5)
        assert d.idx == 4

    @staticmethod
    def test_skipData_startgroup():
        d = _get_decoder(b"\x00\x01\x04")
        d.skipData(3)
        assert d.idx == 3

    @staticmethod
    def test_skipData_endgroup_no_startgroup():
        d = _get_decoder(b"\x10")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.skipData(4)

    @staticmethod
    def test_skipData_bad_tag():
        d = _get_decoder(b"\x10")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.skipData(7)

    @staticmethod
    def test_skipData_startgroup_bad_endgoup():
        d = _get_decoder(b"\x00\x01\x2c")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.skipData(3)

    @staticmethod
    def test_getVarInt32_too_many_bytes():
        d = _get_decoder(b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.getVarInt32()

    @staticmethod
    def test_getVarInt32_corrupted():
        d = _get_decoder(b"\x81\x81\x81\x81\x81\x81\x81\x71")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.getVarInt32()

    @staticmethod
    def test_getVarInt64_too_many_bytes():
        d = _get_decoder(b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff")
        with pytest.raises(pb_module.ProtocolBufferDecodeError):
            d.getVarInt64()
