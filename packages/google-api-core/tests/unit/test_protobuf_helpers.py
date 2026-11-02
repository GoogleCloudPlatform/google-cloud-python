# Copyright 2017 Google LLC
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

import re

import pytest
from google.api import http_pb2
from google.longrunning import operations_pb2
from google.protobuf import (
    any_pb2,
    message,
    source_context_pb2,
    struct_pb2,
    timestamp_pb2,
    type_pb2,
    wrappers_pb2,
)
from google.type import color_pb2, date_pb2, timeofday_pb2

from google.api_core import protobuf_helpers


def test_from_any_pb_success():
    in_message = date_pb2.Date(year=1990)
    in_message_any = any_pb2.Any()
    in_message_any.Pack(in_message)
    out_message = protobuf_helpers.from_any_pb(date_pb2.Date, in_message_any)

    assert in_message == out_message


def test_from_any_pb_wrapped_success():
    # Declare a message class conforming to wrapped messages.
    class WrappedDate(object):
        def __init__(self, **kwargs):
            self._pb = date_pb2.Date(**kwargs)

        def __eq__(self, other):
            return self._pb == other

        @classmethod
        def pb(cls, msg):
            return msg._pb

    # Run the same test as `test_from_any_pb_success`, but using the
    # wrapped class.
    in_message = date_pb2.Date(year=1990)
    in_message_any = any_pb2.Any()
    in_message_any.Pack(in_message)
    out_message = protobuf_helpers.from_any_pb(WrappedDate, in_message_any)

    assert out_message == in_message


def test_from_any_pb_failure():
    in_message = any_pb2.Any()
    in_message.Pack(date_pb2.Date(year=1990))

    with pytest.raises(
        TypeError,
        match=re.escape(
            "Could not convert `google.type.Date` with underlying type `google.protobuf.any_pb2.Any` to `google.type.TimeOfDay`"
        ),
    ):
        protobuf_helpers.from_any_pb(timeofday_pb2.TimeOfDay, in_message)


def test_check_protobuf_helpers_ok():
    assert protobuf_helpers.check_oneof() is None
    assert protobuf_helpers.check_oneof(foo="bar") is None
    assert protobuf_helpers.check_oneof(foo="bar", baz=None) is None
    assert protobuf_helpers.check_oneof(foo=None, baz="bacon") is None
    assert protobuf_helpers.check_oneof(foo="bar", spam=None, eggs=None) is None


def test_check_protobuf_helpers_failures():
    with pytest.raises(ValueError):
        protobuf_helpers.check_oneof(foo="bar", spam="eggs")
    with pytest.raises(ValueError):
        protobuf_helpers.check_oneof(foo="bar", baz="bacon", spam="eggs")
    with pytest.raises(ValueError):
        protobuf_helpers.check_oneof(foo="bar", spam=0, eggs=None)


def test_get_messages():
    answer = protobuf_helpers.get_messages(date_pb2)

    # Ensure that Date was exported properly.
    assert answer["Date"] is date_pb2.Date

    # Ensure that no non-Message objects were exported.
    for value in answer.values():
        assert issubclass(value, message.Message)


def test_get_dict_absent():
    with pytest.raises(KeyError):
        assert protobuf_helpers.get({}, "foo")


def test_get_dict_present():
    assert protobuf_helpers.get({"foo": "bar"}, "foo") == "bar"


def test_get_dict_default():
    assert protobuf_helpers.get({}, "foo", default="bar") == "bar"


def test_get_dict_nested():
    assert protobuf_helpers.get({"foo": {"bar": "baz"}}, "foo.bar") == "baz"


def test_get_dict_nested_default():
    assert protobuf_helpers.get({}, "foo.baz", default="bacon") == "bacon"
    assert protobuf_helpers.get({"foo": {}}, "foo.baz", default="bacon") == "bacon"


def test_get_msg_sentinel():
    msg = timestamp_pb2.Timestamp()
    with pytest.raises(KeyError):
        assert protobuf_helpers.get(msg, "foo")


def test_get_msg_present():
    msg = timestamp_pb2.Timestamp(seconds=42)
    assert protobuf_helpers.get(msg, "seconds") == 42


def test_get_msg_default():
    msg = timestamp_pb2.Timestamp()
    assert protobuf_helpers.get(msg, "foo", default="bar") == "bar"


def test_invalid_object():
    with pytest.raises(TypeError):
        protobuf_helpers.get(object(), "foo", "bar")


def test_set_dict():
    mapping = {}
    protobuf_helpers.set(mapping, "foo", "bar")
    assert mapping == {"foo": "bar"}


def test_set_msg():
    msg = timestamp_pb2.Timestamp()
    protobuf_helpers.set(msg, "seconds", 42)
    assert msg.seconds == 42


def test_set_dict_nested():
    mapping = {}
    protobuf_helpers.set(mapping, "foo.bar", "baz")
    assert mapping == {"foo": {"bar": "baz"}}


def test_set_invalid_object():
    with pytest.raises(TypeError):
        protobuf_helpers.set(object(), "foo", "bar")


def test_set_list():
    list_ops_response = operations_pb2.ListOperationsResponse()

    protobuf_helpers.set(
        list_ops_response,
        "operations",
        [{"name": "foo"}, operations_pb2.Operation(name="bar")],
    )

    assert len(list_ops_response.operations) == 2

    for operation in list_ops_response.operations:
        assert isinstance(operation, operations_pb2.Operation)

    assert list_ops_response.operations[0].name == "foo"
    assert list_ops_response.operations[1].name == "bar"


def test_set_list_clear_existing():
    list_ops_response = operations_pb2.ListOperationsResponse(
        operations=[{"name": "baz"}]
    )

    protobuf_helpers.set(
        list_ops_response,
        "operations",
        [{"name": "foo"}, operations_pb2.Operation(name="bar")],
    )

    assert len(list_ops_response.operations) == 2
    for operation in list_ops_response.operations:
        assert isinstance(operation, operations_pb2.Operation)
    assert list_ops_response.operations[0].name == "foo"
    assert list_ops_response.operations[1].name == "bar"


def test_set_msg_with_msg_field():
    rule = http_pb2.HttpRule()
    pattern = http_pb2.CustomHttpPattern(kind="foo", path="bar")

    protobuf_helpers.set(rule, "custom", pattern)

    assert rule.custom.kind == "foo"
    assert rule.custom.path == "bar"


def test_set_msg_with_dict_field():
    rule = http_pb2.HttpRule()
    pattern = {"kind": "foo", "path": "bar"}

    protobuf_helpers.set(rule, "custom", pattern)

    assert rule.custom.kind == "foo"
    assert rule.custom.path == "bar"


def test_set_msg_nested_key():
    rule = http_pb2.HttpRule(custom=http_pb2.CustomHttpPattern(kind="foo", path="bar"))

    protobuf_helpers.set(rule, "custom.kind", "baz")

    assert rule.custom.kind == "baz"
    assert rule.custom.path == "bar"


def test_setdefault_dict_unset():
    mapping = {}
    protobuf_helpers.setdefault(mapping, "foo", "bar")
    assert mapping == {"foo": "bar"}


def test_setdefault_dict_falsy():
    mapping = {"foo": None}
    protobuf_helpers.setdefault(mapping, "foo", "bar")
    assert mapping == {"foo": "bar"}


def test_setdefault_dict_truthy():
    mapping = {"foo": "bar"}
    protobuf_helpers.setdefault(mapping, "foo", "baz")
    assert mapping == {"foo": "bar"}


def test_setdefault_pb2_falsy():
    operation = operations_pb2.Operation()
    protobuf_helpers.setdefault(operation, "name", "foo")
    assert operation.name == "foo"


def test_setdefault_pb2_truthy():
    operation = operations_pb2.Operation(name="bar")
    protobuf_helpers.setdefault(operation, "name", "foo")
    assert operation.name == "bar"


def test_field_mask_invalid_args():
    with pytest.raises(ValueError):
        protobuf_helpers.field_mask("foo", any_pb2.Any())
    with pytest.raises(ValueError):
        protobuf_helpers.field_mask(any_pb2.Any(), "bar")
    with pytest.raises(ValueError):
        protobuf_helpers.field_mask(any_pb2.Any(), operations_pb2.Operation())


def test_field_mask_equal_values():
    assert protobuf_helpers.field_mask(None, None).paths == []

    original = struct_pb2.Value(number_value=1.0)
    modified = struct_pb2.Value(number_value=1.0)
    assert protobuf_helpers.field_mask(original, modified).paths == []

    original = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=1.0))
    modified = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=1.0))
    assert protobuf_helpers.field_mask(original, modified).paths == []

    original = struct_pb2.ListValue(values=[struct_pb2.Value(number_value=1.0)])
    modified = struct_pb2.ListValue(values=[struct_pb2.Value(number_value=1.0)])
    assert protobuf_helpers.field_mask(original, modified).paths == []

    original = struct_pb2.Struct(fields={"bar": struct_pb2.Value(number_value=1.0)})
    modified = struct_pb2.Struct(fields={"bar": struct_pb2.Value(number_value=1.0)})
    assert protobuf_helpers.field_mask(original, modified).paths == []


def test_field_mask_zero_values():
    # Singular Values
    original = color_pb2.Color(red=0.0)
    modified = None
    assert protobuf_helpers.field_mask(original, modified).paths == []

    original = None
    modified = color_pb2.Color(red=0.0)
    assert protobuf_helpers.field_mask(original, modified).paths == []

    # Repeated Values
    original = struct_pb2.ListValue(values=[])
    modified = None
    assert protobuf_helpers.field_mask(original, modified).paths == []

    original = None
    modified = struct_pb2.ListValue(values=[])
    assert protobuf_helpers.field_mask(original, modified).paths == []

    # Maps
    original = struct_pb2.Struct(fields={})
    modified = None
    assert protobuf_helpers.field_mask(original, modified).paths == []

    original = None
    modified = struct_pb2.Struct(fields={})
    assert protobuf_helpers.field_mask(original, modified).paths == []

    # Oneofs
    original = struct_pb2.Value(number_value=0.0)
    modified = None
    assert protobuf_helpers.field_mask(original, modified).paths == []

    original = None
    modified = struct_pb2.Value(number_value=0.0)
    assert protobuf_helpers.field_mask(original, modified).paths == []


def test_field_mask_singular_field_diffs():
    original = type_pb2.Type(name="name")
    modified = type_pb2.Type()
    assert protobuf_helpers.field_mask(original, modified).paths == ["name"]

    original = type_pb2.Type(name="name")
    modified = type_pb2.Type()
    assert protobuf_helpers.field_mask(original, modified).paths == ["name"]

    original = None
    modified = type_pb2.Type(name="name")
    assert protobuf_helpers.field_mask(original, modified).paths == ["name"]

    original = type_pb2.Type(name="name")
    modified = None
    assert protobuf_helpers.field_mask(original, modified).paths == ["name"]


def test_field_mask_message_diffs():
    original = type_pb2.Type()
    modified = type_pb2.Type(
        source_context=source_context_pb2.SourceContext(file_name="name")
    )
    assert protobuf_helpers.field_mask(original, modified).paths == [
        "source_context.file_name"
    ]

    original = type_pb2.Type(
        source_context=source_context_pb2.SourceContext(file_name="name")
    )
    modified = type_pb2.Type()
    assert protobuf_helpers.field_mask(original, modified).paths == ["source_context"]

    original = type_pb2.Type(
        source_context=source_context_pb2.SourceContext(file_name="name")
    )
    modified = type_pb2.Type(
        source_context=source_context_pb2.SourceContext(file_name="other_name")
    )
    assert protobuf_helpers.field_mask(original, modified).paths == [
        "source_context.file_name"
    ]

    original = None
    modified = type_pb2.Type(
        source_context=source_context_pb2.SourceContext(file_name="name")
    )
    assert protobuf_helpers.field_mask(original, modified).paths == [
        "source_context.file_name"
    ]

    original = type_pb2.Type(
        source_context=source_context_pb2.SourceContext(file_name="name")
    )
    modified = None
    assert protobuf_helpers.field_mask(original, modified).paths == ["source_context"]


def test_field_mask_wrapper_type_diffs():
    original = color_pb2.Color()
    modified = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=1.0))
    assert protobuf_helpers.field_mask(original, modified).paths == ["alpha"]

    original = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=1.0))
    modified = color_pb2.Color()
    assert protobuf_helpers.field_mask(original, modified).paths == ["alpha"]

    original = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=1.0))
    modified = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=2.0))
    assert protobuf_helpers.field_mask(original, modified).paths == ["alpha"]

    original = None
    modified = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=2.0))
    assert protobuf_helpers.field_mask(original, modified).paths == ["alpha"]

    original = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=1.0))
    modified = None
    assert protobuf_helpers.field_mask(original, modified).paths == ["alpha"]


def test_field_mask_repeated_diffs():
    original = struct_pb2.ListValue()
    modified = struct_pb2.ListValue(
        values=[struct_pb2.Value(number_value=1.0), struct_pb2.Value(number_value=2.0)]
    )
    assert protobuf_helpers.field_mask(original, modified).paths == ["values"]

    original = struct_pb2.ListValue(
        values=[struct_pb2.Value(number_value=1.0), struct_pb2.Value(number_value=2.0)]
    )
    modified = struct_pb2.ListValue()
    assert protobuf_helpers.field_mask(original, modified).paths == ["values"]

    original = None
    modified = struct_pb2.ListValue(
        values=[struct_pb2.Value(number_value=1.0), struct_pb2.Value(number_value=2.0)]
    )
    assert protobuf_helpers.field_mask(original, modified).paths == ["values"]

    original = struct_pb2.ListValue(
        values=[struct_pb2.Value(number_value=1.0), struct_pb2.Value(number_value=2.0)]
    )
    modified = None
    assert protobuf_helpers.field_mask(original, modified).paths == ["values"]

    original = struct_pb2.ListValue(
        values=[struct_pb2.Value(number_value=1.0), struct_pb2.Value(number_value=2.0)]
    )
    modified = struct_pb2.ListValue(
        values=[struct_pb2.Value(number_value=2.0), struct_pb2.Value(number_value=1.0)]
    )
    assert protobuf_helpers.field_mask(original, modified).paths == ["values"]


def test_field_mask_map_diffs():
    original = struct_pb2.Struct()
    modified = struct_pb2.Struct(fields={"foo": struct_pb2.Value(number_value=1.0)})
    assert protobuf_helpers.field_mask(original, modified).paths == ["fields"]

    original = struct_pb2.Struct(fields={"foo": struct_pb2.Value(number_value=1.0)})
    modified = struct_pb2.Struct()
    assert protobuf_helpers.field_mask(original, modified).paths == ["fields"]

    original = None
    modified = struct_pb2.Struct(fields={"foo": struct_pb2.Value(number_value=1.0)})
    assert protobuf_helpers.field_mask(original, modified).paths == ["fields"]

    original = struct_pb2.Struct(fields={"foo": struct_pb2.Value(number_value=1.0)})
    modified = None
    assert protobuf_helpers.field_mask(original, modified).paths == ["fields"]

    original = struct_pb2.Struct(fields={"foo": struct_pb2.Value(number_value=1.0)})
    modified = struct_pb2.Struct(fields={"foo": struct_pb2.Value(number_value=2.0)})
    assert protobuf_helpers.field_mask(original, modified).paths == ["fields"]

    original = struct_pb2.Struct(fields={"foo": struct_pb2.Value(number_value=1.0)})
    modified = struct_pb2.Struct(fields={"bar": struct_pb2.Value(number_value=1.0)})
    assert protobuf_helpers.field_mask(original, modified).paths == ["fields"]


def test_field_mask_different_level_diffs():
    original = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=1.0))
    modified = color_pb2.Color(alpha=wrappers_pb2.FloatValue(value=2.0), red=1.0)
    assert sorted(protobuf_helpers.field_mask(original, modified).paths) == [
        "alpha",
        "red",
    ]


def test_field_mask_ignore_trailing_underscore():
    import proto

    class Foo(proto.Message):
        type_ = proto.Field(proto.STRING, number=1)
        input_config = proto.Field(proto.STRING, number=2)

    modified = Foo(type_="bar", input_config="baz")

    assert sorted(protobuf_helpers.field_mask(None, Foo.pb(modified)).paths) == [
        "input_config",
        "type",
    ]


def test_field_mask_ignore_trailing_underscore_with_nesting():
    import proto

    class Bar(proto.Message):
        class Baz(proto.Message):
            input_config = proto.Field(proto.STRING, number=1)

        type_ = proto.Field(Baz, number=1)

    modified = Bar()
    modified.type_.input_config = "foo"

    assert sorted(protobuf_helpers.field_mask(None, Bar.pb(modified)).paths) == [
        "type.input_config",
    ]
