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
import re
from typing import Sequence, Tuple

import pytest

from google.api import field_behavior_pb2
from google.api import resource_pb2
from google.cloud import extended_operations_pb2 as ex_ops_pb2
from google.protobuf import descriptor_pb2

from gapic.schema import naming
from gapic.schema import metadata
from gapic.schema import wrappers

from test_utils.test_utils import (
    make_enum,
    make_field,
    make_message,
)


def test_message_properties():
    message = make_message("MyMessage")
    assert message.name == "MyMessage"


def test_message_docstring():
    L = descriptor_pb2.SourceCodeInfo.Location

    meta = metadata.Metadata(
        documentation=L(
            leading_comments="Lorem ipsum",
            trailing_comments="dolor set amet",
        )
    )
    message = make_message("Name", meta=meta)
    assert message.meta.doc == "Lorem ipsum"


def test_message_ident():
    message = make_message("Baz", package="foo.v1", module="bar")
    assert str(message.ident) == "bar.Baz"
    assert message.ident.sphinx == "foo.v1.bar.Baz"


def test_message_ident_collisions():
    message = make_message("Baz", package="foo.v1", module="bar").with_context(
        collisions=frozenset({"bar"}),
    )
    assert str(message.ident) == "fv_bar.Baz"
    assert message.ident.sphinx == "foo.v1.bar.Baz"


def test_message_pb2_sphinx_ident():
    meta = metadata.Metadata(
        address=metadata.Address(
            name="Timestamp",
            package=("google", "protobuf"),
            module="timestamp",
            api_naming=naming.NewNaming(proto_package="foo.bar"),
        )
    )
    message = make_message(
        "Timestamp", package="google.protobuf", module="timestamp", meta=meta
    )
    assert message.ident.sphinx == "google.protobuf.timestamp_pb2.Timestamp"


def test_get_field():
    fields = (make_field("field_one"), make_field("field_two"))
    message = make_message("Message", fields=fields)
    field_one = message.get_field("field_one")
    assert isinstance(field_one, wrappers.Field)
    assert field_one.name == "field_one"


def test_field_types():
    # Create the inner message.
    inner_msg = make_message(
        "InnerMessage",
        fields=(
            make_field(
                "hidden_message",
                message=make_message("HiddenMessage"),
            ),
        ),
    )
    inner_enum = make_enum("InnerEnum")

    # Create the outer message, which contains an Inner as a field.
    fields = (
        make_field("inner_message", message=inner_msg),
        make_field("inner_enum", enum=inner_enum),
        make_field("not_interesting"),
    )
    outer = make_message("Outer", fields=fields)

    # Assert that composite field types are recognized but primitives are not.
    assert len(outer.field_types) == 2
    assert inner_msg in outer.field_types
    assert inner_enum in outer.field_types


def test_field_types_recursive():
    enumeration = make_enum("Enumeration")
    innest_msg = make_message(
        "InnestMessage", fields=(make_field("enumeration", enum=enumeration),)
    )
    inner_msg = make_message(
        "InnerMessage", fields=(make_field("innest_message", message=innest_msg),)
    )
    topmost_msg = make_message(
        "TopmostMessage",
        fields=(
            make_field("inner_message", message=inner_msg),
            make_field("uninteresting"),
        ),
    )

    actual = {t.name for t in topmost_msg.recursive_field_types}
    expected = {t.name for t in (enumeration, innest_msg, inner_msg)}
    assert actual == expected


def test_get_field_recursive():
    # Create the inner message.
    inner_fields = (make_field("zero"), make_field("one"))
    inner = make_message("Inner", fields=inner_fields, package="foo.v1")

    # Create the outer message, which contains an Inner as a field.
    outer_field = make_field("inner", message=inner)
    outer = make_message("Outer", fields=(outer_field,))

    # Assert that a recursive retrieval works.
    assert outer.get_field("inner", "zero") == inner_fields[0]
    assert outer.get_field("inner", "one") == inner_fields[1]
    assert outer.get_field("inner.one") == inner_fields[1]


def test_get_field_nested_not_found_error():
    # Create the inner message.
    inner_field = make_field("zero")
    inner = make_message("Inner", fields=(inner_field,), package="foo.v1")

    # Create the outer message, which contains an Inner as a field.
    outer_field = make_field("inner", message=inner)
    outer = make_message("Outer", fields=(outer_field,))

    # Assert that a recursive retrieval fails.
    with pytest.raises(KeyError):
        assert outer.get_field("inner", "zero", "beyond")


def test_get_field_nonterminal_repeated_error():
    # Create the inner message.
    inner_fields = (make_field("zero"), make_field("one"))
    inner = make_message("Inner", fields=inner_fields, package="foo.v1")

    # Create the outer message, which contains an Inner as a field.
    outer_field = make_field("inner", message=inner, repeated=True)
    outer = make_message("Outer", fields=(outer_field,))

    # Assert that a recursive retrieval fails.
    with pytest.raises(KeyError):
        assert outer.get_field("inner", "zero") == inner_fields[0]
    with pytest.raises(KeyError):
        assert outer.get_field("inner", "one") == inner_fields[1]


def test_resource_path():
    options = descriptor_pb2.MessageOptions()
    resource = options.Extensions[resource_pb2.resource]
    resource.pattern.append("kingdoms/{kingdom}/phyla/{phylum}/classes/{klass}")
    resource.pattern.append("kingdoms/{kingdom}/divisions/{division}/classes/{klass}")
    resource.type = "taxonomy.biology.com/Class"
    message = make_message("Squid", options=options)

    assert message.resource_path == "kingdoms/{kingdom}/phyla/{phylum}/classes/{klass}"
    assert message.resource_path_args == ["kingdom", "phylum", "klass"]
    assert message.resource_type == "Class"


def test_resource_path_with_wildcard():
    options = descriptor_pb2.MessageOptions()
    resource = options.Extensions[resource_pb2.resource]
    resource.pattern.append("kingdoms/{kingdom}/phyla/{phylum}/classes/{klass=**}")
    resource.pattern.append("kingdoms/{kingdom}/divisions/{division}/classes/{klass}")
    resource.type = "taxonomy.biology.com/Class"
    message = make_message("Squid", options=options)

    assert (
        message.resource_path == "kingdoms/{kingdom}/phyla/{phylum}/classes/{klass=**}"
    )
    assert message.resource_path_args == ["kingdom", "phylum", "klass"]
    assert message.resource_type == "Class"
    assert re.match(
        message.path_regex_str, "kingdoms/my-kingdom/phyla/my-phylum/classes/my-klass"
    )
    assert re.match(
        message.path_regex_str,
        "kingdoms/my-kingdom/phyla/my-phylum/classes/my-klass/additional-segment",
    )
    assert (
        re.match(message.path_regex_str, "kingdoms/my-kingdom/phyla/my-phylum/classes/")
        is None
    )
    assert (
        message.resource_path_formatted
        == "kingdoms/{kingdom}/phyla/{phylum}/classes/{klass}"
    )


def test_resource_path_pure_wildcard():
    options = descriptor_pb2.MessageOptions()
    resource = options.Extensions[resource_pb2.resource]
    resource.pattern.append("*")
    resource.type = "taxonomy.biology.com/Class"
    message = make_message("Squid", options=options)

    # Pure wildcard resource names do not really help construct resources
    # but they are a part of the spec so we need to support them, which means at
    # least not failing.
    assert message.resource_path == "*"
    assert message.resource_path_args == []
    assert message.resource_type == "Class"

    # Pure wildcard resource names match everything...
    assert re.match(
        message.path_regex_str, "kingdoms/my-kingdom/phyla/my-phylum/classes/my-klass"
    )
    assert re.match(
        message.path_regex_str,
        "kingdoms/my-kingdom/phyla/my-phylum/classes/my-klass/additional-segment",
    )
    assert re.match(
        message.path_regex_str, "kingdoms/my-kingdom/phyla/my-phylum/classes/"
    )


def test_parse_resource_path():
    options = descriptor_pb2.MessageOptions()
    resource = options.Extensions[resource_pb2.resource]
    resource.pattern.append("kingdoms/{kingdom}/phyla/{phylum}/classes/{klass}")
    resource.type = "taxonomy.biology.com/Klass"
    message = make_message("Klass", options=options)

    # Plausible resource ID path
    path = "kingdoms/animalia/phyla/mollusca/classes/cephalopoda"
    expected = {
        "kingdom": "animalia",
        "phylum": "mollusca",
        "klass": "cephalopoda",
    }
    actual = re.match(message.path_regex_str, path).groupdict()

    assert expected == actual

    options2 = descriptor_pb2.MessageOptions()
    resource2 = options2.Extensions[resource_pb2.resource]
    resource2.pattern.append("kingdoms-{kingdom}_{phylum}#classes%{klass}")
    resource2.type = "taxonomy.biology.com/Klass"
    message2 = make_message("Klass", options=options2)

    # Plausible resource ID path from a non-standard schema
    path2 = "kingdoms-Animalia/_Mollusca~#classes%Cephalopoda"
    expected2 = {
        "kingdom": "Animalia/",
        "phylum": "Mollusca~",
        "klass": "Cephalopoda",
    }
    actual2 = re.match(message2.path_regex_str, path2).groupdict()

    assert expected2 == actual2


def test_field_map():
    # Create an Entry message.
    entry_msg = make_message(
        name="FooEntry",
        fields=(
            make_field(name="key", type=9),
            make_field(name="value", type=9),
        ),
        options=descriptor_pb2.MessageOptions(map_entry=True),
    )
    entry_field = make_field("foos", message=entry_msg, repeated=True)
    assert entry_msg.map
    assert entry_field.map


def test_oneof_fields():
    mass_kg = make_field(name="mass_kg", oneof="mass", type=5)
    mass_lbs = make_field(name="mass_lbs", oneof="mass", type=5)
    length_m = make_field(name="length_m", oneof="length", type=5)
    length_f = make_field(name="length_f", oneof="length", type=5)
    color = make_field(name="color", type=5)
    request = make_message(
        name="CreateMolluscRequest",
        fields=(
            mass_kg,
            mass_lbs,
            length_m,
            length_f,
            color,
        ),
    )
    actual_oneofs = request.oneof_fields()
    expected_oneofs = {
        "mass": [mass_kg, mass_lbs],
        "length": [length_m, length_f],
    }
    assert actual_oneofs == expected_oneofs


def test_required_fields():
    REQUIRED = field_behavior_pb2.FieldBehavior.Value("REQUIRED")

    mass_kg = make_field(name="mass_kg", type=5)
    mass_kg.options.Extensions[field_behavior_pb2.field_behavior].append(REQUIRED)

    length_m = make_field(name="length_m", type=5)
    length_m.options.Extensions[field_behavior_pb2.field_behavior].append(REQUIRED)

    color = make_field(name="color", type=5)
    color.options.Extensions[field_behavior_pb2.field_behavior].append(REQUIRED)

    request = make_message(
        name="CreateMolluscRequest",
        fields=(
            mass_kg,
            length_m,
            color,
        ),
    )

    assert set(request.required_fields) == {mass_kg, length_m, color}


def test_is_extended_operation():
    T = descriptor_pb2.FieldDescriptorProto.Type

    # Canonical Operation

    operation = make_message(
        name="Operation",
        fields=tuple(
            make_field(name=name, type=T.Value("TYPE_STRING"), number=i)
            for i, name in enumerate(
                ("name", "status", "error_code", "error_message"), start=1
            )
        ),
    )
    for f in operation.fields.values():
        options = descriptor_pb2.FieldOptions()
        # Note: The field numbers were carefully chosen to be the corresponding enum values.
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    assert operation.is_extended_operation
    assert operation.extended_operation_status_field == operation.fields["status"]

    # Missing a required field
    missing = make_message(
        name="Operation",
        fields=tuple(
            make_field(name=name, type=T.Value("TYPE_STRING"), number=i)
            # Missing error_message
            for i, name in enumerate(("name", "status", "error_code"), start=1)
        ),
    )
    for f in missing.fields.values():
        options = descriptor_pb2.FieldOptions()
        # Note: The field numbers were carefully chosen to be the corresponding enum values.
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    assert not missing.is_extended_operation

    # Named incorrectly
    my_message = make_message(
        name="MyMessage",
        fields=tuple(
            make_field(name=name, type=T.Value("TYPE_STRING"), number=i)
            for i, name in enumerate(
                ("name", "status", "error_code", "error_message"), start=1
            )
        ),
    )
    for f in my_message.fields.values():
        options = descriptor_pb2.FieldOptions()
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    assert not my_message.is_extended_operation

    # Duplicated annotation
    for mapping in range(1, 5):
        duplicate = make_message(
            name="Operation",
            fields=tuple(
                make_field(name=name, type=T.Value("TYPE_STRING"), number=i)
                for i, name in enumerate(
                    ("name", "status", "error_code", "error_message"), start=1
                )
            ),
        )
        for f in duplicate.fields.values():
            options = descriptor_pb2.FieldOptions()
            # All set to the same value
            options.Extensions[ex_ops_pb2.operation_field] = mapping
            f.options.MergeFrom(options)

        with pytest.raises(TypeError):
            duplicate.is_extended_operation

    # Just totally not an operation
    random_message = make_message(
        "MyOperation",
        fields=[
            make_field(name="moniker", type=T.Value("TYPE_STRING"), number=1),
        ],
    )

    assert not random_message.is_extended_operation
    assert not random_message.extended_operation_status_field


def test_extended_operation_request_response_fields():
    T = descriptor_pb2.FieldDescriptorProto.Type
    # Operation request
    request = make_message(
        name="Request",
        fields=[
            make_field(name=name, type=T.Value("TYPE_STRING"), number=i)
            for i, name in enumerate(("project", "name", "armor_class", "id"), start=1)
        ],
    )
    expected = (request.fields["project"], request.fields["id"])
    for field in expected:
        options = descriptor_pb2.FieldOptions()
        options.Extensions[ex_ops_pb2.operation_request_field] = field.name
        field.options.MergeFrom(options)

    actual = request.extended_operation_request_fields
    assert actual == expected

    # Operation response
    poll_request = make_message(
        name="GetRequest",
        fields=[
            make_field(name=name, type=T.Value("TYPE_STRING"), number=i)
            for i, name in enumerate(("name", "rank", "affinity", "serial"))
        ],
    )
    expected = (poll_request.fields["name"], poll_request.fields["affinity"])
    for field in expected:
        field.options.Extensions[ex_ops_pb2.operation_response_field] = field.name

    actual = poll_request.extended_operation_response_fields
    assert actual == expected


def test_message_type_resource_type_with_alias():
    # 1. Cleanly mock the options
    opts = descriptor_pb2.MessageOptions()
    opts.Extensions[resource_pb2.resource].type = "ces.googleapis.com/Tool"
    
    msg_pb = descriptor_pb2.DescriptorProto(name="MyMessage", options=opts)
    
    # 2. Explicitly instantiate MessageType here instead
    # of using `make_message` to inject 'resource_name_aliases' field.
    message = wrappers.MessageType(
        message_pb=msg_pb,
        fields={},
        nested_enums={},
        nested_messages={},
        resource_name_aliases={"ces.googleapis.com/Tool": "CesTool"},
    )
    
    # 3. Verify it intercepted the default Protobuf logic
    # and returned the alias
    assert message.resource_type == "CesTool"


def test_message_type_resource_type_without_alias():
    # 1. Cleanly mock the options
    opts = descriptor_pb2.MessageOptions()
    opts.Extensions[resource_pb2.resource].type = "ces.googleapis.com/Tool"
    msg_pb = descriptor_pb2.DescriptorProto(name="MyMessage", options=opts)
    
    # 2. Instantiate WITHOUT any aliases matching this resource
    message = wrappers.MessageType(
        message_pb=msg_pb,
        fields={},
        nested_enums={},
        nested_messages={},
        resource_name_aliases={"some.other/Resource": "OtherAlias"},
    )
    
    # 3. Verify it falls back to the default type ("Tool")
    assert message.resource_type == "Tool"
