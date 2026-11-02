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

import collections

import pytest

from google.api import field_behavior_pb2
from google.api import field_info_pb2
from google.api import resource_pb2
from google.cloud import extended_operations_pb2 as ex_ops_pb2
from google.protobuf import descriptor_pb2

from gapic.schema import api
from gapic.schema import metadata
from gapic.schema import wrappers

from test_utils.test_utils import (
    make_field,
    make_message,
    make_enum,
)


def test_field_properties():
    field = make_field(name="my_field", number=1, type="TYPE_BOOL")
    assert field.name == "my_field"
    assert field.number == 1
    assert field.type.python_type == bool


def test_field_is_primitive():
    primitive_field = make_field(type="TYPE_INT32")
    assert primitive_field.is_primitive


def test_field_proto_type():
    primitive_field = make_field(type="TYPE_INT32")
    assert primitive_field.proto_type == "INT32"


def test_field_not_primitive():
    message = wrappers.MessageType(
        fields={},
        nested_messages={},
        nested_enums={},
        message_pb=descriptor_pb2.DescriptorProto(),
    )
    non_primitive_field = make_field(
        type="TYPE_MESSAGE",
        type_name="bogus.Message",
        message=message,
    )
    assert not non_primitive_field.is_primitive


def test_ident():
    field = make_field(type="TYPE_BOOL")
    assert str(field.ident) == "bool"


def test_ident_repeated():
    REP = descriptor_pb2.FieldDescriptorProto.Label.Value("LABEL_REPEATED")
    field = make_field(type="TYPE_BOOL", label=REP)
    assert str(field.ident) == "MutableSequence[bool]"


def test_repeated():
    REP = descriptor_pb2.FieldDescriptorProto.Label.Value("LABEL_REPEATED")
    field = make_field(label=REP)
    assert field.repeated


def test_not_repeated():
    OPT = descriptor_pb2.FieldDescriptorProto.Label.Value("LABEL_OPTIONAL")
    field = make_field(label=OPT)
    assert not field.repeated


def test_map():
    entry_msg = make_message(
        name="SquidEntry",
        fields=(
            make_field(name="key", type="TYPE_STRING"),
            make_field(name="value", type="TYPE_STRING"),
        ),
        options=descriptor_pb2.MessageOptions(map_entry=True),
    )
    field = make_field(
        name="squids",
        type_name="mollusc.SquidEntry",
        message=entry_msg,
        label=3,
        type="TYPE_MESSAGE",
    )

    assert field.map


def test_ident_map():
    entry_msg = make_message(
        name="SquidEntry",
        fields=(
            make_field(name="key", type="TYPE_STRING"),
            make_field(name="value", type="TYPE_STRING"),
        ),
        options=descriptor_pb2.MessageOptions(map_entry=True),
    )
    field = make_field(
        name="squids",
        type_name="mollusc.SquidEntry",
        message=entry_msg,
        label=3,
        type="TYPE_MESSAGE",
    )

    assert str(field.ident) == "MutableMapping[str, str]"


def test_required():
    field = make_field()
    field.options.Extensions[field_behavior_pb2.field_behavior].append(
        field_behavior_pb2.FieldBehavior.Value("REQUIRED")
    )
    assert field.required


def test_not_required():
    field = make_field()
    assert not field.required


def test_uuid4():
    field = make_field()
    field.options.Extensions[
        field_info_pb2.field_info
    ].format = field_info_pb2.FieldInfo.Format.Value("UUID4")
    assert field.uuid4


def test_not_uuid4():
    field = make_field()
    assert not field.uuid4


def test_ident_sphinx():
    field = make_field(type="TYPE_BOOL")
    assert field.ident.sphinx == "bool"


def test_ident_sphinx_repeated():
    REP = descriptor_pb2.FieldDescriptorProto.Label.Value("LABEL_REPEATED")
    field = make_field(type="TYPE_BOOL", label=REP)
    assert field.ident.sphinx == "MutableSequence[bool]"


def test_ident_sphinx_map():
    entry_msg = make_message(
        name="SquidEntry",
        fields=(
            make_field(name="key", type="TYPE_STRING"),
            make_field(name="value", type="TYPE_STRING"),
        ),
        options=descriptor_pb2.MessageOptions(map_entry=True),
    )
    field = make_field(
        name="squids",
        type_name="mollusc.SquidEntry",
        message=entry_msg,
        label=3,
        type="TYPE_MESSAGE",
    )
    assert field.ident.sphinx == "MutableMapping[str, str]"


def test_resource_reference():
    field = make_field(type="TYPE_STRING")
    field.options.Extensions[
        resource_pb2.resource_reference
    ].type = "translate.googleapis.com/Glossary"

    assert field.resource_reference == "translate.googleapis.com/Glossary"


def test_type_primitives():
    assert make_field(type="TYPE_FLOAT").type.python_type == float
    assert make_field(type="TYPE_INT64").type.python_type == int
    assert make_field(type="TYPE_BOOL").type.python_type == bool
    assert make_field(type="TYPE_STRING").type.python_type == str
    assert make_field(type="TYPE_BYTES").type.python_type == bytes


def test_type_message():
    message = wrappers.MessageType(
        fields={},
        nested_messages={},
        nested_enums={},
        message_pb=descriptor_pb2.DescriptorProto(),
    )
    field = make_field(
        type="TYPE_MESSAGE",
        type_name="bogus.Message",
        message=message,
    )
    assert field.type == message


def test_type_enum():
    enum = wrappers.EnumType(
        values={},
        enum_pb=descriptor_pb2.EnumDescriptorProto(),
    )
    field = make_field(
        type="TYPE_ENUM",
        type_name="bogus.Enumerable",
        enum=enum,
    )
    assert field.type == enum


def test_type_invalid():
    with pytest.raises(TypeError):
        make_field(type="TYPE_GROUP").type


def test_mock_value_int():
    field = make_field(name="foo_bar", type="TYPE_INT32")
    assert field.mock_value == "728"


def test_mock_value_original_type_int():
    field = make_field(name="foo_bar", type="TYPE_INT32")
    assert field.mock_value_original_type == 728


def test_oneof():
    REP = descriptor_pb2.FieldDescriptorProto.Label.Value("LABEL_REPEATED")

    field = make_field(oneof="oneof_name")
    assert field.oneof == "oneof_name"


def test_mock_value_float():
    field = make_field(name="foo_bar", type="TYPE_DOUBLE")
    assert field.mock_value == "0.728"


def test_mock_value_original_type_float():
    field = make_field(name="foo_bar", type="TYPE_DOUBLE")
    assert field.mock_value_original_type == 0.728


def test_mock_value_bool():
    field = make_field(name="foo_bar", type="TYPE_BOOL")
    assert field.mock_value == "True"


def test_mock_value_original_type_bool():
    field = make_field(name="foo_bar", type="TYPE_BOOL")
    assert field.mock_value_original_type == True


def test_mock_value_str():
    field = make_field(name="foo_bar", type="TYPE_STRING")
    assert field.mock_value == "'foo_bar_value'"


def test_mock_value_original_type_str():
    field = make_field(name="foo_bar", type="TYPE_STRING")
    assert field.mock_value_original_type == "foo_bar_value"


def test_mock_value_bytes():
    field = make_field(name="foo_bar", type="TYPE_BYTES")
    assert field.mock_value == "b'foo_bar_blob'"


def test_mock_value_original_type_bytes():
    field = make_field(name="foo_bar", type="TYPE_BYTES")
    assert field.mock_value_original_type == b"foo_bar_blob"


def test_mock_value_repeated():
    field = make_field(name="foo_bar", type="TYPE_STRING", label=3)
    assert field.mock_value == "['foo_bar_value']"


def test_mock_value_original_type_repeated():
    field = make_field(name="foo_bar", type="TYPE_STRING", label=3)
    assert field.mock_value_original_type == ["foo_bar_value1", "foo_bar_value2"]


def test_mock_value_map():
    entry_msg = make_message(
        name="SquidEntry",
        fields=(
            make_field(name="key", type="TYPE_STRING"),
            make_field(name="value", type="TYPE_STRING"),
        ),
        options=descriptor_pb2.MessageOptions(map_entry=True),
    )
    field = make_field(
        name="squids",
        type_name="mollusc.SquidEntry",
        message=entry_msg,
        label=3,
        type="TYPE_MESSAGE",
    )

    assert field.mock_value == "{'key_value': 'value_value'}"


def test_mock_value_enum():
    values = [
        descriptor_pb2.EnumValueDescriptorProto(name="UNSPECIFIED", number=0),
        descriptor_pb2.EnumValueDescriptorProto(name="SPECIFIED", number=1),
    ]
    enum = wrappers.EnumType(
        values=[wrappers.EnumValueType(enum_value_pb=i) for i in values],
        enum_pb=descriptor_pb2.EnumDescriptorProto(value=values),
        meta=metadata.Metadata(
            address=metadata.Address(
                module="bogus",
                name="Enumerable",
            )
        ),
    )
    field = make_field(
        type="TYPE_ENUM",
        type_name="bogus.Enumerable",
        enum=enum,
    )
    assert field.mock_value == "bogus.Enumerable.SPECIFIED"


def test_mock_value_message():
    subfields = collections.OrderedDict(
        (
            ("foo", make_field(name="foo", type="TYPE_INT32")),
            ("bar", make_field(name="bar", type="TYPE_STRING")),
        )
    )
    message = wrappers.MessageType(
        fields=subfields,
        message_pb=descriptor_pb2.DescriptorProto(
            name="Message", field=[i.field_pb for i in subfields.values()]
        ),
        meta=metadata.Metadata(
            address=metadata.Address(
                module="bogus",
                name="Message",
            )
        ),
        nested_enums={},
        nested_messages={},
    )
    field = make_field(
        type="TYPE_MESSAGE",
        type_name="bogus.Message",
        message=message,
    )
    assert field.mock_value == "bogus.Message(foo=324)"


def test_mock_value_original_type_message():
    any_message_subfields = collections.OrderedDict(
        (
            ("type_url", make_field(name="type_url", number=1, type="TYPE_STRING")),
            ("value", make_field(name="value", number=2, type="TYPE_BYTES")),
        )
    )

    any_message = wrappers.MessageType(
        fields=any_message_subfields,
        message_pb=descriptor_pb2.DescriptorProto(
            name="Any", field=[i.field_pb for i in any_message_subfields.values()]
        ),
        meta=metadata.Metadata(
            address=metadata.Address(
                module="bogus", name="Any", package=("google", "protobuf")
            )
        ),
        nested_enums={},
        nested_messages={},
    )

    any_field = make_field(
        name="surprise",
        type="TYPE_MESSAGE",
        type_name="google.protobuf.Any",
        message=any_message,
    )

    subfields = collections.OrderedDict(
        (
            ("foo", make_field(name="foo", type="TYPE_INT32")),
            ("bar", make_field(name="bar", type="TYPE_STRING")),
            ("surprise", any_field),
        )
    )

    message = wrappers.MessageType(
        fields=subfields,
        message_pb=descriptor_pb2.DescriptorProto(
            name="Message", field=[i.field_pb for i in subfields.values()]
        ),
        meta=metadata.Metadata(
            address=metadata.Address(
                module="bogus",
                name="Message",
            )
        ),
        nested_enums={},
        nested_messages={},
    )

    field = make_field(
        type="TYPE_MESSAGE",
        type_name="bogus.Message",
        message=message,
    )

    mock = field.mock_value_original_type

    assert mock == {
        "foo": 324,
        "bar": "bar_value",
        "surprise": {
            "type_url": "type.googleapis.com/google.protobuf.Duration",
            "value": b"\x08\x0c\x10\xdb\x07",
        },
    }

    # Messages by definition aren't primitive
    with pytest.raises(TypeError):
        field.primitive_mock()

    # Special case for map entries
    entry_msg = make_message(
        name="MessageEntry",
        fields=(
            make_field(name="key", type="TYPE_STRING"),
            make_field(name="value", type="TYPE_STRING"),
        ),
        options=descriptor_pb2.MessageOptions(map_entry=True),
    )
    entry_field = make_field(
        name="messages",
        type_name="stuff.MessageEntry",
        message=entry_msg,
        label=3,
        type="TYPE_MESSAGE",
    )

    assert entry_field.mock_value_original_type == {}

    assert (
        any_message.fields["type_url"].primitive_mock()
        == "type.googleapis.com/google.protobuf.Empty"
    )


def test_merged_mock_value_message():
    subfields = collections.OrderedDict(
        (
            ("foo", make_field(name="foo", type="TYPE_INT32")),
            ("bar", make_field(name="bar", type="TYPE_STRING")),
        )
    )

    message = wrappers.MessageType(
        fields=subfields,
        message_pb=descriptor_pb2.DescriptorProto(
            name="Message", field=[i.field_pb for i in subfields.values()]
        ),
        meta=metadata.Metadata(
            address=metadata.Address(
                module="bogus",
                name="Message",
            )
        ),
        nested_enums={},
        nested_messages={},
    )

    field = make_field(
        type="TYPE_MESSAGE",
        type_name="bogus.Message",
        message=message,
    )

    mock = field.merged_mock_value({"foo": 777, "another": "another_value"})
    assert mock == {"foo": 777, "bar": "bar_value", "another": "another_value"}

    mock = field.merged_mock_value(None)
    assert mock == {"bar": "bar_value", "foo": 324}


def test_mock_value_original_type_enum():
    mollusc_field = make_field(
        name="class",
        enum=make_enum(
            name="Class",
            values=[
                ("UNKNOWN", 0),
                ("GASTROPOD", 1),
                ("BIVALVE", 2),
                ("CEPHALOPOD", 3),
            ],
        ),
    )

    assert mollusc_field.mock_value_original_type == 1

    empty_field = make_field(
        name="empty",
        enum=make_enum(
            name="Empty",
            values=[("UNKNOWN", 0)],
        ),
    )

    assert empty_field.mock_value_original_type == 0


def test_mock_value_original_type_enum_repeated():
    mollusc_field = make_field(
        name="class",
        enum=make_enum(
            name="Class",
            values=[
                ("UNKNOWN", 0),
                ("BIVALVE", 2),
                ("CEPHALOPOD", 3),
            ],
        ),
        label=3,
    )

    assert mollusc_field.mock_value_original_type == [2]

    empty_field = make_field(
        name="empty",
        enum=make_enum(
            name="Empty",
            values=[("UNKNOWN", 0)],
        ),
        label=3,
    )

    assert empty_field.mock_value_original_type == [0]


@pytest.mark.parametrize(
    "mock_method,expected",
    [
        (
            "mock_value",
            "ac_turtle.Turtle(turtle=ac_turtle.Turtle(turtle=turtle.Turtle(turtle=None)))",
        ),
        ("mock_value_original_type", {"turtle": {}}),
    ],
)
def test_mock_value_recursive(mock_method, expected):
    # The elaborate setup is an unfortunate requirement.
    file_pb = descriptor_pb2.FileDescriptorProto(
        name="turtle.proto",
        package="animalia.chordata.v2",
        message_type=(
            descriptor_pb2.DescriptorProto(
                # It's turtles all the way down ;)
                name="Turtle",
                field=(
                    descriptor_pb2.FieldDescriptorProto(
                        name="turtle",
                        type="TYPE_MESSAGE",
                        type_name=".animalia.chordata.v2.Turtle",
                        number=1,
                    ),
                ),
            ),
        ),
    )
    my_api = api.API.build([file_pb], package="animalia.chordata.v2")
    turtle_field = my_api.messages["animalia.chordata.v2.Turtle"].fields["turtle"]

    # If not handled properly, this will run forever and eventually OOM.
    actual = getattr(turtle_field, mock_method)
    assert actual == expected


def test_field_name_kword_disambiguation():
    from_field = make_field(
        name="from",
    )
    assert from_field.name == "from_"

    frum_field = make_field(
        name="frum",
    )
    assert frum_field.name == "frum"

    mapping_field = make_field(name="mapping")
    assert mapping_field.name == "mapping_"

    ignore_field = make_field(name="ignore_unknown_fields")
    assert ignore_field.name == "ignore_unknown_fields_"


def test_field_resource_reference():
    field = make_field(name="parent", type="TYPE_STRING")


def test_extended_operation_properties():
    options = descriptor_pb2.FieldOptions()
    options.Extensions[ex_ops_pb2.operation_request_field] = "squid"
    options.Extensions[ex_ops_pb2.operation_response_field] = "clam"
    f = make_field(options=options)

    assert f.operation_request_field == "squid"
    assert f.operation_response_field == "clam"
