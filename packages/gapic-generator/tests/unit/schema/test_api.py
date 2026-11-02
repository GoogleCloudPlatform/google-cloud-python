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
from typing import Any, Dict, Sequence
from unittest import mock

import pytest
import yaml
from google.api import (
    annotations_pb2,  # type: ignore
    client_pb2,
    field_behavior_pb2,
    field_info_pb2,
    resource_pb2,
)
from google.api_core import exceptions
from google.cloud import extended_operations_pb2 as ex_ops_pb2
from google.cloud.location import locations_pb2
from google.gapic.metadata import gapic_metadata_pb2
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.longrunning import operations_pb2
from google.protobuf import descriptor_pb2
from google.protobuf.json_format import MessageToJson

from gapic.schema import api, imp, mixins, naming, wrappers
from gapic.utils import Options
from test_utils.test_utils import (
    make_enum_pb2,
    make_field,
    make_field_pb2,
    make_file_pb2,
    make_message_pb2,
    make_naming,
    make_oneof_pb2,
)


def test_api_build():
    # Put together a couple of minimal protos.
    fd = (
        make_file_pb2(
            name="dep.proto",
            package="google.dep",
            messages=(make_message_pb2(name="ImportedMessage", fields=()),),
        ),
        make_file_pb2(
            name="common.proto",
            package="google.example.v1.common",
            messages=(make_message_pb2(name="Bar"),),
        ),
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Foo", fields=()),
                make_message_pb2(
                    name="GetFooRequest",
                    fields=(
                        make_field_pb2(
                            name="imported_message",
                            number=1,
                            type_name=".google.dep.ImportedMessage",
                        ),
                        make_field_pb2(name="primitive", number=2, type=1),
                    ),
                ),
                make_message_pb2(
                    name="GetFooResponse",
                    fields=(
                        make_field_pb2(
                            name="foo", number=1, type_name=".google.example.v1.Foo"
                        ),
                    ),
                ),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetFoo",
                            input_type="google.example.v1.GetFooRequest",
                            output_type="google.example.v1.GetFooResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    # Create an API with those protos.
    api_schema = api.API.build(fd, package="google.example.v1")

    # Establish that the API has the data expected.
    assert isinstance(api_schema, api.API)
    assert len(api_schema.all_protos) == 3
    assert len(api_schema.protos) == 2
    assert "google.dep.ImportedMessage" not in api_schema.messages
    assert "google.example.v1.common.Bar" in api_schema.messages
    assert "google.example.v1.Foo" in api_schema.messages
    assert "google.example.v1.GetFooRequest" in api_schema.messages
    assert "google.example.v1.GetFooResponse" in api_schema.messages
    assert "google.example.v1.FooService" in api_schema.services
    assert len(api_schema.enums) == 0
    assert api_schema.protos["foo.proto"].python_modules == (
        imp.Import(package=("google", "dep"), module="dep_pb2"),
    )

    assert api_schema.requires_package(("google", "example", "v1"))

    assert not api_schema.requires_package(("elgoog", "example", "v1"))

    # Establish that the subpackages work.
    assert "common" in api_schema.subpackages
    sub = api_schema.subpackages["common"]
    assert len(sub.protos) == 1
    assert "google.example.v1.common.Bar" in sub.messages
    assert "google.example.v1.Foo" not in sub.messages


def test_top_level_messages():
    message_pbs = (
        make_message_pb2(name="Mollusc", nested_type=(make_message_pb2(name="Squid"),)),
    )
    fds = (
        make_file_pb2(
            messages=message_pbs,
            package="google.example.v3",
        ),
    )
    api_schema = api.API.build(fds, package="google.example.v3")
    actual = [m.name for m in api_schema.top_level_messages.values()]
    expected = ["Mollusc"]
    assert expected == actual


def test_top_level_enum():
    # Test that a nested enum works properly.
    message_pbs = (
        make_message_pb2(
            name="Coleoidea",
            enum_type=(
                make_enum_pb2(
                    "Superorder",
                    "Decapodiformes",
                    "Octopodiformes",
                    "Palaeoteuthomorpha",
                ),
            ),
        ),
    )
    enum_pbs = (
        make_enum_pb2(
            "Order",
            "Gastropoda",
            "Bivalvia",
            "Cephalopoda",
        ),
    )
    fds = (
        make_file_pb2(
            messages=message_pbs,
            enums=enum_pbs,
            package="google.example.v3",
        ),
    )
    api_schema = api.API.build(fds, package="google.example.v3")
    actual = [e.name for e in api_schema.top_level_enums.values()]
    expected = ["Order"]
    assert expected == actual


def test_proto_build():
    fdp = descriptor_pb2.FileDescriptorProto(
        name="my_proto_file.proto",
        package="google.example.v1",
    )
    proto = api.Proto.build(fdp, file_to_generate=True, naming=make_naming())
    assert isinstance(proto, api.Proto)


def test_proto_names():
    # Put together a couple of minimal protos.
    fd = (
        make_file_pb2(
            name="dep.proto",
            package="google.dep",
            messages=(make_message_pb2(name="ImportedMessage", fields=()),),
        ),
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Foo", fields=()),
                make_message_pb2(
                    name="Bar",
                    fields=(
                        make_field_pb2(
                            name="imported_message",
                            number=1,
                            type_name=".google.dep.ImportedMessage",
                        ),
                        make_field_pb2(name="primitive", number=2, type=1),
                    ),
                ),
                make_message_pb2(
                    name="Baz",
                    fields=(
                        make_field_pb2(
                            name="foo", number=1, type_name=".google.example.v1.Foo"
                        ),
                    ),
                ),
            ),
        ),
    )

    # Create an API with those protos.
    api_schema = api.API.build(fd, package="google.example.v1")
    proto = api_schema.protos["foo.proto"]
    assert proto.names == {"Foo", "Bar", "Baz", "foo", "imported_message", "primitive"}
    assert proto.disambiguate("enum") == "enum"
    assert proto.disambiguate("foo") == "_foo"


def test_proto_with_invalid_characters():
    # Protos with filenames that contain `.` in the basename
    # cannot be directly imported. Test that `.` is changed to `_`
    # See https://peps.python.org/pep-0008/#package-and-module-names

    test_cases = [
        {"name": "k8s.min.proto", "expected": "k8s_min.proto"},
        {"name": "k8s.min.test.proto", "expected": "k8s_min_test.proto"},
    ]

    for test_case in test_cases:
        fd = (
            make_file_pb2(
                name=test_case["name"],
                package="google.keywords.v1",
                messages=(make_message_pb2(name="ImportRequest", fields=()),),
            ),
        )
        api_schema = api.API.build(fd, package="google.keywords.v1")
        assert set(api_schema.protos.keys()) == {
            test_case["expected"],
        }


def test_proto_keyword_fname():
    # Protos with filenames that happen to be python keywords
    # cannot be directly imported.
    # Check that the file names are unspecialized when building the API object.
    fd = (
        make_file_pb2(
            name="import.proto",
            package="google.keywords.v1",
            messages=(make_message_pb2(name="ImportRequest", fields=()),),
        ),
        make_file_pb2(
            name="import_.proto",
            package="google.keywords.v1",
            messages=(make_message_pb2(name="ImportUnderRequest", fields=()),),
        ),
        make_file_pb2(
            name="class_.proto",
            package="google.keywords.v1",
            messages=(make_message_pb2(name="ClassUnderRequest", fields=()),),
        ),
        make_file_pb2(
            name="class.proto",
            package="google.keywords.v1",
            messages=(make_message_pb2(name="ClassRequest", fields=()),),
        ),
        make_file_pb2(
            name="metadata.proto",
            package="google.keywords.v1",
            messages=(make_message_pb2(name="MetadataRequest", fields=()),),
        ),
        make_file_pb2(
            name="retry.proto",
            package="google.keywords.v1",
            messages=(make_message_pb2(name="RetryRequest", fields=()),),
        ),
        make_file_pb2(
            name="timeout.proto",
            package="google.keywords.v1",
            messages=(make_message_pb2(name="TimeoutRequest", fields=()),),
        ),
        make_file_pb2(
            name="request.proto",
            package="google.keywords.v1",
            messages=(make_message_pb2(name="RequestRequest", fields=()),),
        ),
    )

    # We can't create new collisions, so check that renames cascade.
    api_schema = api.API.build(fd, package="google.keywords.v1")
    assert set(api_schema.protos.keys()) == {
        "import_.proto",
        "import__.proto",
        "class_.proto",
        "class__.proto",
        "metadata_.proto",
        "retry_.proto",
        "timeout_.proto",
        "request_.proto",
    }


def test_proto_oneof():
    # Put together a couple of minimal protos.
    fd = (
        make_file_pb2(
            name="dep.proto",
            package="google.dep",
            messages=(make_message_pb2(name="ImportedMessage", fields=()),),
        ),
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Foo", fields=()),
                make_message_pb2(
                    name="Bar",
                    fields=(
                        make_field_pb2(
                            name="imported_message",
                            number=1,
                            type_name=".google.dep.ImportedMessage",
                            oneof_index=0,
                        ),
                        make_field_pb2(
                            name="primitive", number=2, type=1, oneof_index=0
                        ),
                    ),
                    oneof_decl=(make_oneof_pb2(name="value_type"),),
                ),
            ),
        ),
    )

    # Create an API with those protos.
    api_schema = api.API.build(fd, package="google.example.v1")
    proto = api_schema.protos["foo.proto"]
    assert proto.names == {"imported_message", "Bar", "primitive", "Foo"}
    oneofs = proto.messages["google.example.v1.Bar"].oneofs
    assert len(oneofs) == 1
    assert "value_type" in oneofs.keys()


def test_proto_names_import_collision():
    # Put together a couple of minimal protos.
    fd = (
        make_file_pb2(
            name="a/b/c/spam.proto",
            package="a.b.c",
            messages=(make_message_pb2(name="ImportedMessage", fields=()),),
        ),
        make_file_pb2(
            name="x/y/z/spam.proto",
            package="x.y.z",
            messages=(make_message_pb2(name="OtherMessage", fields=()),),
        ),
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Foo", fields=()),
                make_message_pb2(
                    name="Bar",
                    fields=(
                        make_field_pb2(
                            name="imported_message",
                            number=1,
                            type_name=".a.b.c.ImportedMessage",
                        ),
                        make_field_pb2(
                            name="other_message",
                            number=2,
                            type_name=".x.y.z.OtherMessage",
                        ),
                        make_field_pb2(name="primitive", number=3, type=1),
                    ),
                ),
                make_message_pb2(
                    name="Baz",
                    fields=(
                        make_field_pb2(
                            name="foo", number=1, type_name=".google.example.v1.Foo"
                        ),
                    ),
                ),
            ),
        ),
    )

    # Create an API with those protos.
    api_schema = api.API.build(fd, package="google.example.v1")
    proto = api_schema.protos["foo.proto"]
    assert proto.names == {
        "Foo",
        "Bar",
        "Baz",
        "foo",
        "imported_message",
        "other_message",
        "primitive",
        "spam",
    }


def test_proto_names_import_collision_flattening():
    lro_proto = api.Proto.build(
        make_file_pb2(
            name="operations.proto",
            package="google.longrunning",
            messages=(make_message_pb2(name="Operation"),),
        ),
        file_to_generate=False,
        naming=make_naming(),
    )

    fd = (
        make_file_pb2(
            name="mollusc.proto",
            package="google.animalia.mollusca",
            messages=(
                make_message_pb2(
                    name="Mollusc",
                ),
                make_message_pb2(
                    name="MolluscResponse",
                ),
                make_message_pb2(
                    name="MolluscMetadata",
                ),
            ),
        ),
        make_file_pb2(
            name="squid.proto",
            package="google.animalia.mollusca",
            messages=(
                make_message_pb2(
                    name="IdentifySquidRequest",
                    fields=(
                        make_field_pb2(
                            name="mollusc",
                            number=1,
                            type_name=".google.animalia.mollusca.Mollusc",
                        ),
                    ),
                ),
                make_message_pb2(
                    name="IdentifySquidResponse",
                    fields=(),
                ),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="SquidIdentificationService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="IdentifyMollusc",
                            input_type="google.animalia.mollusca.IdentifySquidRequest",
                            output_type="google.longrunning.Operation",
                        ),
                    ),
                ),
            ),
        ),
    )

    method_options = fd[1].service[0].method[0].options
    # Notice that a signature field collides with the name of an imported module
    method_options.Extensions[client_pb2.method_signature].append("mollusc")
    method_options.Extensions[operations_pb2.operation_info].MergeFrom(
        operations_pb2.OperationInfo(
            response_type="google.animalia.mollusca.MolluscResponse",
            metadata_type="google.animalia.mollusca.MolluscMetadata",
        )
    )
    api_schema = api.API.build(
        fd,
        package="google.animalia.mollusca",
        prior_protos={
            "google/longrunning/operations.proto": lro_proto,
        },
    )

    actual_imports = {
        ref_type.ident.python_import
        for service in api_schema.services.values()
        for method in service.methods.values()
        for ref_type in method.ref_types
    }

    expected_imports = {
        imp.Import(
            package=("google", "animalia", "mollusca", "types"),
            module="mollusc",
            alias="gam_mollusc",
        ),
        imp.Import(
            package=("google", "animalia", "mollusca", "types"),
            module="squid",
        ),
        imp.Import(
            package=("google", "api_core"),
            module="operation",
        ),
        imp.Import(
            package=("google", "api_core"),
            module="operation_async",
        ),
    }

    assert expected_imports == actual_imports

    method = api_schema.services[
        "google.animalia.mollusca.SquidIdentificationService"
    ].methods["IdentifyMollusc"]

    actual_response_import = method.lro.response_type.ident.python_import
    expected_response_import = imp.Import(
        package=("google", "animalia", "mollusca", "types"),
        module="mollusc",
        alias="gam_mollusc",
    )
    assert actual_response_import == expected_response_import


def test_proto_builder_constructor():
    sentinel_message = descriptor_pb2.DescriptorProto()
    sentinel_enum = descriptor_pb2.EnumDescriptorProto()
    sentinel_service = descriptor_pb2.ServiceDescriptorProto()

    # Create a file descriptor proto. It does not matter that none
    # of the sentinels have actual data because this test just ensures
    # they are sent off to the correct methods unmodified.
    fdp = make_file_pb2(
        messages=(sentinel_message,),
        enums=(sentinel_enum,),
        services=(sentinel_service,),
    )

    # Test the load function.
    with mock.patch.object(api._ProtoBuilder, "_load_children") as lc:
        pb = api._ProtoBuilder(
            fdp,
            file_to_generate=True,
            naming=make_naming(),
        )

        # There should be three total calls to load the different types
        # of children.
        assert lc.call_count == 3

        # The enum type should come first.
        _, args, _ = lc.mock_calls[0]
        assert args[0][0] == sentinel_enum
        assert args[1] == pb._load_enum

        # The message type should come second.
        _, args, _ = lc.mock_calls[1]
        assert args[0][0] == sentinel_message
        assert args[1] == pb._load_message

        # The services should come third.
        _, args, _ = lc.mock_calls[2]
        assert args[0][0] == sentinel_service
        assert args[1] == pb._load_service


def test_not_target_file():
    """Establish that services are not ignored for untargeted protos."""
    message_pb = make_message_pb2(
        name="Foo", fields=(make_field_pb2(name="bar", type=3, number=1),)
    )
    service_pb = descriptor_pb2.ServiceDescriptorProto()
    fdp = make_file_pb2(messages=(message_pb,), services=(service_pb,))

    # Actually make the proto object.
    proto = api.Proto.build(fdp, file_to_generate=False, naming=make_naming())

    # The proto object should have the message, but no service.
    assert len(proto.messages) == 1
    assert len(proto.services) == 0


def test_messages():
    L = descriptor_pb2.SourceCodeInfo.Location

    message_pb = make_message_pb2(
        name="Foo", fields=(make_field_pb2(name="bar", type=3, number=1),)
    )
    locations = (
        L(path=(4, 0), leading_comments="This is the Foo message."),
        L(path=(4, 0, 2, 0), leading_comments="This is the bar field."),
    )
    fdp = make_file_pb2(
        messages=(message_pb,),
        locations=locations,
        package="google.example.v2",
    )

    # Make the proto object.
    proto = api.Proto.build(fdp, file_to_generate=True, naming=make_naming())

    # Get the message.
    assert len(proto.messages) == 1
    message = proto.messages["google.example.v2.Foo"]
    assert isinstance(message, wrappers.MessageType)
    assert message.meta.doc == "This is the Foo message."
    assert len(message.fields) == 1
    assert message.fields["bar"].meta.doc == "This is the bar field."


def test_messages_reverse_declaration_order():
    # Test that if a message is used as a field higher in the same file,
    # that things still work.
    message_pbs = (
        make_message_pb2(
            name="Foo",
            fields=(
                make_field_pb2(
                    name="bar", number=1, type_name=".google.example.v3.Bar"
                ),
            ),
        ),
        make_message_pb2(name="Bar"),
    )
    fdp = make_file_pb2(
        messages=message_pbs,
        package="google.example.v3",
    )

    # Make the proto object.
    proto = api.Proto.build(fdp, file_to_generate=True, naming=make_naming())

    # Get the message.
    assert len(proto.messages) == 2
    Foo = proto.messages["google.example.v3.Foo"]
    assert Foo.fields["bar"].message == proto.messages["google.example.v3.Bar"]


def test_messages_recursive():
    # Test that if a message is used inside itself, that things will still
    # work.
    message_pbs = (
        make_message_pb2(
            name="Foo",
            fields=(
                make_field_pb2(
                    name="foo", number=1, type_name=".google.example.v3.Foo"
                ),
            ),
        ),
    )
    fdp = make_file_pb2(
        messages=message_pbs,
        package="google.example.v3",
    )

    # Make the proto object.
    proto = api.Proto.build(fdp, file_to_generate=True, naming=make_naming())

    # Get the message.
    assert len(proto.messages) == 1
    Foo = proto.messages["google.example.v3.Foo"]
    assert Foo.fields["foo"].message == proto.messages["google.example.v3.Foo"]


def test_messages_nested():
    # Test that a nested message works properly.
    message_pbs = (
        make_message_pb2(name="Foo", nested_type=(make_message_pb2(name="Bar"),)),
    )
    fdp = make_file_pb2(
        messages=message_pbs,
        package="google.example.v3",
    )

    # Make the proto object.
    proto = api.Proto.build(fdp, file_to_generate=True, naming=make_naming())

    # Set short variables for the names.
    foo = "google.example.v3.Foo"
    bar = "google.example.v3.Foo.Bar"

    # Get the message.
    assert len(proto.all_messages) == 2
    assert proto.all_messages[foo].name == "Foo"
    assert proto.all_messages[bar].name == "Bar"

    # Assert that the `messages` property only shows top-level messages.
    assert len(proto.messages) == 1
    assert proto.messages[foo] is proto.messages[foo]
    assert bar not in proto.messages


def test_out_of_order_enums():
    # Enums can be referenced as field types before they
    # are defined in the proto file.
    # This happens when they're a nested type within a message.
    messages = (
        make_message_pb2(
            name="Squid",
            fields=(
                make_field_pb2(
                    name="base_color",
                    type_name="google.mollusca.Chromatophore.Color",
                    number=1,
                ),
            ),
        ),
        make_message_pb2(
            name="Chromatophore",
            enum_type=(descriptor_pb2.EnumDescriptorProto(name="Color", value=()),),
        ),
    )
    fd = (
        make_file_pb2(
            name="squid.proto",
            package="google.mollusca",
            messages=messages,
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="SquidService",
                ),
            ),
        ),
    )
    api_schema = api.API.build(fd, package="google.mollusca")
    field_type = api_schema.messages["google.mollusca.Squid"].fields["base_color"].type
    enum_type = api_schema.enums["google.mollusca.Chromatophore.Color"]
    assert field_type == enum_type


def test_undefined_type():
    fd = (
        make_file_pb2(
            name="mollusc.proto",
            package="google.mollusca",
            messages=(
                make_message_pb2(
                    name="Mollusc",
                    fields=(
                        make_field_pb2(
                            name="class",
                            type_name="google.mollusca.Class",
                            number=1,
                        ),
                    ),
                ),
            ),
        ),
    )
    with pytest.raises(TypeError):
        api.API.build(fd, package="google.mollusca")


def test_python_modules_nested():
    fd = (
        make_file_pb2(
            name="dep.proto",
            package="google.dep",
            messages=(make_message_pb2(name="ImportedMessage", fields=()),),
        ),
        make_file_pb2(
            name="baa.proto",
            package="google.baa",
            messages=(make_message_pb2(name="ImportedMessageBaa", fields=()),),
        ),
        make_file_pb2(
            name="bab.v1.proto",
            package="google.bab.v1",
            messages=(make_message_pb2(name="ImportedMessageBab", fields=()),),
        ),
        make_file_pb2(
            name="common.proto",
            package="google.example.v1.common",
            messages=(make_message_pb2(name="Bar"),),
        ),
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(
                    name="GetFooRequest",
                    fields=(
                        make_field_pb2(name="primitive", number=2, type=1),
                        make_field_pb2(
                            name="foo",
                            number=3,
                            type=1,
                            type_name=".google.example.v1.GetFooRequest.Foo",
                        ),
                    ),
                    nested_type=(
                        make_message_pb2(
                            name="Foo",
                            fields=(
                                make_field_pb2(
                                    name="imported_message",
                                    number=1,
                                    type_name=".google.dep.ImportedMessage",
                                ),
                            ),
                        ),
                        make_message_pb2(
                            name="Baa",
                            fields=(
                                make_field_pb2(
                                    name="imported_message_baa",
                                    number=1,
                                    type_name=".google.baa.ImportedMessageBaa",
                                ),
                            ),
                        ),
                        make_message_pb2(
                            name="Bab",
                            fields=(
                                make_field_pb2(
                                    name="imported_message_bab",
                                    number=1,
                                    type_name=".google.bab.v1.ImportedMessageBab",
                                ),
                            ),
                        ),
                    ),
                ),
                make_message_pb2(
                    name="GetFooResponse",
                    fields=(
                        make_field_pb2(
                            name="foo",
                            number=1,
                            type_name=".google.example.v1.GetFooRequest.Foo",
                        ),
                    ),
                ),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetFoo",
                            input_type="google.example.v1.GetFooRequest",
                            output_type="google.example.v1.GetFooResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    api_schema = api.API.build(fd, package="google.example.v1")

    assert api_schema.protos["foo.proto"].python_modules == (
        imp.Import(package=("google", "baa"), module="baa_pb2"),
        imp.Import(package=("google", "bab", "v1"), module="bab_v1_pb2"),
        imp.Import(package=("google", "dep"), module="dep_pb2"),
    )
    assert (
        api_schema.protos["foo.proto"]
        .all_messages["google.example.v1.GetFooRequest.Bab"]
        .fields["imported_message_bab"]
        .ident.sphinx
        == "google.bab.v1.bab_v1_pb2.ImportedMessageBab"
    )

    # Ensure that we can change the import statements to cater for a
    # dependency that uses proto-plus types.
    # For example,
    # `from google.bar import bar_pb2` becomes `from google.bar.types import bar``
    # `from google.baz.v2 import baz_pb2` becomes `from google.baz_v2.types improt baz_v2`
    api_schema = api.API.build(
        fd,
        package="google.example.v1",
        opts=Options(
            proto_plus_deps="+".join(
                (
                    "google.baa",
                    "google.bab.v1",
                )
            )
        ),
    )
    assert api_schema.protos["foo.proto"].python_modules == (
        imp.Import(package=("google", "baa", "types"), module="baa"),
        imp.Import(package=("google", "bab_v1", "types"), module="bab_v1"),
        imp.Import(package=("google", "dep"), module="dep_pb2"),
    )

    assert (
        api_schema.protos["foo.proto"]
        .all_messages["google.example.v1.GetFooRequest.Bab"]
        .fields["imported_message_bab"]
        .ident.sphinx
        == "google.bab_v1.types.ImportedMessageBab"
    )


def test_services():
    L = descriptor_pb2.SourceCodeInfo.Location

    # Make a silly helper method to not repeat some of the structure.
    def _n(method_name: str):
        return {
            "service": "google.example.v2.FooService",
            "method": method_name,
        }

    # Set up retry information.
    opts = Options(
        retry={
            "methodConfig": [
                {"name": [_n("TimeoutableGetFoo")], "timeout": "30s"},
                {
                    "name": [_n("RetryableGetFoo")],
                    "retryPolicy": {
                        "maxAttempts": 3,
                        "initialBackoff": "%dn" % 1e6,
                        "maxBackoff": "60s",
                        "backoffMultiplier": 1.5,
                        "retryableStatusCodes": ["UNAVAILABLE", "ABORTED"],
                    },
                },
            ]
        }
    )

    # Set up messages for our RPC.
    request_message_pb = make_message_pb2(
        name="GetFooRequest", fields=(make_field_pb2(name="name", type=9, number=1),)
    )
    response_message_pb = make_message_pb2(name="GetFooResponse", fields=())

    # Set up the service with an RPC.
    service_pb = descriptor_pb2.ServiceDescriptorProto(
        name="FooService",
        method=(
            descriptor_pb2.MethodDescriptorProto(
                name="GetFoo",
                input_type="google.example.v2.GetFooRequest",
                output_type="google.example.v2.GetFooResponse",
            ),
            descriptor_pb2.MethodDescriptorProto(
                name="TimeoutableGetFoo",
                input_type="google.example.v2.GetFooRequest",
                output_type="google.example.v2.GetFooResponse",
            ),
            descriptor_pb2.MethodDescriptorProto(
                name="RetryableGetFoo",
                input_type="google.example.v2.GetFooRequest",
                output_type="google.example.v2.GetFooResponse",
            ),
        ),
    )

    # Fake-document our fake stuff.
    locations = (
        L(path=(6, 0), leading_comments="This is the FooService service."),
        L(path=(6, 0, 2, 0), leading_comments="This is the GetFoo method."),
        L(path=(4, 0), leading_comments="This is the GetFooRequest message."),
        L(path=(4, 1), leading_comments="This is the GetFooResponse message."),
    )

    # Finally, set up the file that encompasses these.
    fdp = make_file_pb2(
        name="test.proto",
        package="google.example.v2",
        messages=(request_message_pb, response_message_pb),
        services=(service_pb,),
        locations=locations,
    )

    # Make the proto object.
    proto = api.API.build(
        [fdp],
        "google.example.v2",
        opts=opts,
    ).protos["test.proto"]

    # Establish that our data looks correct.
    assert len(proto.services) == 1
    assert len(proto.messages) == 2
    service = proto.services["google.example.v2.FooService"]
    assert service.meta.doc == "This is the FooService service."
    assert len(service.methods) == 3
    method = service.methods["GetFoo"]
    assert method.meta.doc == "This is the GetFoo method."
    assert isinstance(method.input, wrappers.MessageType)
    assert isinstance(method.output, wrappers.MessageType)
    assert method.input.name == "GetFooRequest"
    assert method.input.meta.doc == "This is the GetFooRequest message."
    assert method.output.name == "GetFooResponse"
    assert method.output.meta.doc == "This is the GetFooResponse message."
    assert not method.timeout
    assert not method.retry

    # Establish that the retry information on a timeout-able method also
    # looks correct.
    timeout_method = service.methods["TimeoutableGetFoo"]
    assert timeout_method.timeout == pytest.approx(30.0)
    assert not timeout_method.retry

    # Establish that the retry information on the retryable method also
    # looks correct.
    retry_method = service.methods["RetryableGetFoo"]
    assert retry_method.timeout is None
    assert retry_method.retry.max_attempts == 3
    assert retry_method.retry.initial_backoff == pytest.approx(0.001)
    assert retry_method.retry.backoff_multiplier == pytest.approx(1.5)
    assert retry_method.retry.max_backoff == pytest.approx(60.0)
    assert retry_method.retry.retryable_exceptions == {
        exceptions.ServiceUnavailable,
        exceptions.Aborted,
    }


def test_prior_protos():
    L = descriptor_pb2.SourceCodeInfo.Location

    # Set up a prior proto that mimics google/protobuf/empty.proto
    empty_proto = api.Proto.build(
        make_file_pb2(
            name="empty.proto",
            package="google.protobuf",
            messages=(make_message_pb2(name="Empty"),),
        ),
        file_to_generate=False,
        naming=make_naming(),
    )

    # Set up the service with an RPC.
    service_pb = descriptor_pb2.ServiceDescriptorProto(
        name="PingService",
        method=(
            descriptor_pb2.MethodDescriptorProto(
                name="Ping",
                input_type="google.protobuf.Empty",
                output_type="google.protobuf.Empty",
            ),
        ),
    )

    # Fake-document our fake stuff.
    locations = (
        L(path=(6, 0), leading_comments="This is the PingService service."),
        L(path=(6, 0, 2, 0), leading_comments="This is the Ping method."),
    )

    # Finally, set up the file that encompasses these.
    fdp = make_file_pb2(
        package="google.example.v1",
        services=(service_pb,),
        locations=locations,
    )

    # Make the proto object.
    proto = api.Proto.build(
        fdp,
        file_to_generate=True,
        prior_protos={
            "google/protobuf/empty.proto": empty_proto,
        },
        naming=make_naming(),
    )

    # Establish that our data looks correct.
    assert len(proto.services) == 1
    assert len(empty_proto.messages) == 1
    assert len(proto.messages) == 0
    service = proto.services["google.example.v1.PingService"]
    assert service.meta.doc == "This is the PingService service."
    assert len(service.methods) == 1
    method = service.methods["Ping"]
    assert isinstance(method.input, wrappers.MessageType)
    assert isinstance(method.output, wrappers.MessageType)
    assert method.input.name == "Empty"
    assert method.output.name == "Empty"
    assert method.meta.doc == "This is the Ping method."


def test_lro():
    # Set up a prior proto that mimics google/protobuf/empty.proto
    lro_proto = api.Proto.build(
        make_file_pb2(
            name="operations.proto",
            package="google.longrunning",
            messages=(make_message_pb2(name="Operation"),),
        ),
        file_to_generate=False,
        naming=make_naming(),
    )

    # Set up a method with LRO annotations.
    method_pb2 = descriptor_pb2.MethodDescriptorProto(
        name="AsyncDoThing",
        input_type="google.example.v3.AsyncDoThingRequest",
        output_type="google.longrunning.Operation",
    )
    method_pb2.options.Extensions[operations_pb2.operation_info].MergeFrom(
        operations_pb2.OperationInfo(
            response_type="google.example.v3.AsyncDoThingResponse",
            metadata_type="google.example.v3.AsyncDoThingMetadata",
        ),
    )

    # Set up the service with an RPC.
    service_pb = descriptor_pb2.ServiceDescriptorProto(
        name="LongRunningService",
        method=(method_pb2,),
    )

    # Set up the messages, including the annotated ones.
    messages = (
        make_message_pb2(name="AsyncDoThingRequest", fields=()),
        make_message_pb2(name="AsyncDoThingResponse", fields=()),
        make_message_pb2(name="AsyncDoThingMetadata", fields=()),
    )

    # Finally, set up the file that encompasses these.
    fdp = make_file_pb2(
        package="google.example.v3",
        messages=messages,
        services=(service_pb,),
    )

    # Make the proto object.
    proto = api.Proto.build(
        fdp,
        file_to_generate=True,
        prior_protos={
            "google/longrunning/operations.proto": lro_proto,
        },
        naming=make_naming(),
    )

    # Establish that our data looks correct.
    assert len(proto.services) == 1
    assert len(proto.messages) == 3
    assert len(lro_proto.messages) == 1


def test_lro_operation_no_annotation():
    # A method that returns google.longrunning.Operation,
    # but has no operation_info option, is treated as not lro.

    # Set up a prior proto that mimics google/protobuf/empty.proto
    lro_proto = api.Proto.build(
        make_file_pb2(
            name="operations.proto",
            package="google.longrunning",
            messages=(make_message_pb2(name="Operation"),),
        ),
        file_to_generate=False,
        naming=make_naming(),
    )

    # Set up a method that returns an Operation, but has no annotation.
    method_pb2 = descriptor_pb2.MethodDescriptorProto(
        name="GetOperation",
        input_type="google.example.v3.GetOperationRequest",
        output_type="google.longrunning.Operation",
    )

    # Set up the service with an RPC.
    service_pb = descriptor_pb2.ServiceDescriptorProto(
        name="OperationService",
        method=(method_pb2,),
    )

    # Set up the messages, including the annotated ones.
    messages = (make_message_pb2(name="GetOperationRequest", fields=()),)

    # Finally, set up the file that encompasses these.
    fdp = make_file_pb2(
        package="google.example.v3",
        messages=messages,
        services=(service_pb,),
    )

    # Make the proto object.
    proto = api.Proto.build(
        fdp,
        file_to_generate=True,
        prior_protos={
            "google/longrunning/operations.proto": lro_proto,
        },
        naming=make_naming(),
    )

    service = proto.services["google.example.v3.OperationService"]
    method = service.methods["GetOperation"]
    assert method.lro is None


def test_lro_bad_annotation():
    # Set up a prior proto that mimics google/protobuf/empty.proto
    lro_proto = api.Proto.build(
        make_file_pb2(
            name="operations.proto",
            package="google.longrunning",
            messages=(make_message_pb2(name="Operation"),),
        ),
        file_to_generate=False,
        naming=make_naming(),
    )

    # Set up a method with an LRO and incomplete annotation.
    method_pb2 = descriptor_pb2.MethodDescriptorProto(
        name="AsyncDoThing",
        input_type="google.example.v3.AsyncDoThingRequest",
        output_type="google.longrunning.Operation",
    )
    method_pb2.options.Extensions[operations_pb2.operation_info].MergeFrom(
        operations_pb2.OperationInfo(
            response_type="google.example.v3.AsyncDoThingResponse",
        ),
    )

    # Set up the service with an RPC.
    service_pb = descriptor_pb2.ServiceDescriptorProto(
        name="LongRunningService",
        method=(method_pb2,),
    )

    # Set up the messages, including the annotated ones.
    messages = (make_message_pb2(name="AsyncDoThingRequest", fields=()),)

    # Finally, set up the file that encompasses these.
    fdp = make_file_pb2(
        package="google.example.v3",
        messages=messages,
        services=(service_pb,),
    )

    # Make the proto object.
    with pytest.raises(TypeError):
        api.Proto.build(
            fdp,
            file_to_generate=True,
            prior_protos={
                "google/longrunning/operations.proto": lro_proto,
            },
            naming=make_naming(),
        )


def test_cross_file_lro():
    # Protobuf annotations for longrunning operations use strings to name types.
    # As far as the protobuf compiler is concerned they don't reference the
    # _types_ at all, so the corresponding proto file that owns the types
    # does not need to be imported.
    # This creates a potential issue when building rich structures around
    # LRO returning methods. This test is intended to verify that the issue
    # is handled correctly.

    # Set up a prior proto that mimics google/protobuf/empty.proto
    lro_proto = api.Proto.build(
        make_file_pb2(
            name="operations.proto",
            package="google.longrunning",
            messages=(make_message_pb2(name="Operation"),),
        ),
        file_to_generate=False,
        naming=make_naming(),
    )

    # Set up a method with LRO annotations.
    method_pb2 = descriptor_pb2.MethodDescriptorProto(
        name="AsyncDoThing",
        input_type="google.example.v3.AsyncDoThingRequest",
        output_type="google.longrunning.Operation",
    )
    method_pb2.options.Extensions[operations_pb2.operation_info].MergeFrom(
        operations_pb2.OperationInfo(
            response_type="google.example.v3.AsyncDoThingResponse",
            metadata_type="google.example.v3.AsyncDoThingMetadata",
        ),
    )

    # Set up the service with an RPC.
    service_file = make_file_pb2(
        name="service_file.proto",
        package="google.example.v3",
        messages=(make_message_pb2(name="AsyncDoThingRequest", fields=()),),
        services=(
            descriptor_pb2.ServiceDescriptorProto(
                name="LongRunningService",
                method=(method_pb2,),
            ),
        ),
    )

    # Set up the messages, including the annotated ones.
    # This file is distinct and is not explicitly imported
    # into the file that defines the service.
    messages_file = make_file_pb2(
        name="messages_file.proto",
        package="google.example.v3",
        messages=(
            make_message_pb2(name="AsyncDoThingResponse", fields=()),
            make_message_pb2(name="AsyncDoThingMetadata", fields=()),
        ),
    )

    api_schema = api.API.build(
        file_descriptors=(
            service_file,
            messages_file,
        ),
        package="google.example.v3",
        prior_protos={
            "google/longrunning/operations.proto": lro_proto,
        },
    )

    method = (
        api_schema.all_protos["service_file.proto"]
        .services["google.example.v3.LongRunningService"]
        .methods["AsyncDoThing"]
    )

    assert method.lro
    assert method.lro.response_type.name == "AsyncDoThingResponse"
    assert method.lro.metadata_type.name == "AsyncDoThingMetadata"


def test_extended_lro():
    initiate_options = descriptor_pb2.MethodOptions()
    initiate_options.Extensions[ex_ops_pb2.operation_service] = "OpsService"

    polling_method_options = descriptor_pb2.MethodOptions()
    polling_method_options.Extensions[ex_ops_pb2.operation_polling_method] = True

    T = descriptor_pb2.FieldDescriptorProto.Type
    operation_fields = tuple(
        make_field_pb2(name=name, type=T.Value("TYPE_STRING"), number=i)
        for i, name in enumerate(
            ("name", "status", "error_code", "error_message"), start=1
        )
    )
    for f in operation_fields:
        options = descriptor_pb2.FieldOptions()
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    api_schema = api.Proto.build(
        make_file_pb2(
            "extended_lro.proto",
            package="exlro",
            messages=(
                make_message_pb2(name="Operation", fields=operation_fields),
                make_message_pb2(name="InitialRequest"),
                make_message_pb2(name="GetOperationRequest"),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="OpsService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="Get",
                            input_type="exlro.GetOperationRequest",
                            output_type="exlro.Operation",
                            options=polling_method_options,
                        ),
                    ),
                ),
                descriptor_pb2.ServiceDescriptorProto(
                    name="BasicService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="Initiate",
                            input_type="exlro.InitialRequest",
                            output_type="exlro.Operation",
                            options=initiate_options,
                        ),
                    ),
                ),
            ),
        ),
        file_to_generate=True,
        naming=make_naming(),
    )

    initiate = api_schema.services["exlro.BasicService"].methods["Initiate"]
    assert initiate.extended_lro
    assert (
        initiate.extended_lro.request_type
        == api_schema.messages["exlro.GetOperationRequest"]
    )
    assert (
        initiate.extended_lro.operation_type == api_schema.messages["exlro.Operation"]
    )


def test_extended_lro_no_such_service():
    initiate_options = descriptor_pb2.MethodOptions()
    initiate_options.Extensions[ex_ops_pb2.operation_service] = "Nonesuch"

    polling_method_options = descriptor_pb2.MethodOptions()
    polling_method_options.Extensions[ex_ops_pb2.operation_polling_method] = True

    T = descriptor_pb2.FieldDescriptorProto.Type
    operation_fields = tuple(
        make_field_pb2(name=name, type=T.Value("TYPE_STRING"), number=i)
        for i, name in enumerate(
            ("name", "status", "error_code", "error_message"), start=1
        )
    )
    for f in operation_fields:
        options = descriptor_pb2.FieldOptions()
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    with pytest.raises(ValueError):
        api_schema = api.Proto.build(
            make_file_pb2(
                "extended_lro.proto",
                package="exlro",
                messages=(
                    make_message_pb2(
                        name="Operation",
                        fields=operation_fields,
                    ),
                    make_message_pb2(name="InitialRequest"),
                    make_message_pb2(name="GetOperationRequest"),
                ),
                services=(
                    descriptor_pb2.ServiceDescriptorProto(
                        name="OpsService",
                        method=(
                            descriptor_pb2.MethodDescriptorProto(
                                name="Get",
                                input_type="exlro.GetOperationRequest",
                                output_type="exlro.Operation",
                                options=polling_method_options,
                            ),
                        ),
                    ),
                    descriptor_pb2.ServiceDescriptorProto(
                        name="BasicService",
                        method=(
                            descriptor_pb2.MethodDescriptorProto(
                                name="Initiate",
                                input_type="exlro.InitialRequest",
                                output_type="exlro.Operation",
                                options=initiate_options,
                            ),
                        ),
                    ),
                ),
            ),
            file_to_generate=True,
            naming=make_naming(),
        )


def test_extended_lro_no_polling_method():
    initiate_options = descriptor_pb2.MethodOptions()
    initiate_options.Extensions[ex_ops_pb2.operation_service] = "OpsService"

    T = descriptor_pb2.FieldDescriptorProto.Type
    operation_fields = tuple(
        make_field_pb2(name=name, type=T.Value("TYPE_STRING"), number=i)
        for i, name in enumerate(
            ("name", "status", "error_code", "error_message"), start=1
        )
    )
    for f in operation_fields:
        options = descriptor_pb2.FieldOptions()
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    with pytest.raises(ValueError):
        api_schema = api.Proto.build(
            make_file_pb2(
                "extended_lro.proto",
                package="exlro",
                messages=(
                    make_message_pb2(
                        name="Operation",
                        fields=operation_fields,
                    ),
                    make_message_pb2(
                        name="InitialRequest",
                    ),
                    make_message_pb2(
                        name="GetOperationRequest",
                    ),
                ),
                services=(
                    descriptor_pb2.ServiceDescriptorProto(
                        name="OpsService",
                        method=(
                            descriptor_pb2.MethodDescriptorProto(
                                name="Get",
                                input_type="exlro.GetOperationRequest",
                                output_type="exlro.Operation",
                            ),
                        ),
                    ),
                    descriptor_pb2.ServiceDescriptorProto(
                        name="BasicService",
                        method=(
                            descriptor_pb2.MethodDescriptorProto(
                                name="Initiate",
                                input_type="exlro.InitialRequest",
                                output_type="exlro.Operation",
                                options=initiate_options,
                            ),
                        ),
                    ),
                ),
            ),
            file_to_generate=True,
            naming=make_naming(),
        )


def test_extended_lro_different_output_types():
    initiate_options = descriptor_pb2.MethodOptions()
    initiate_options.Extensions[ex_ops_pb2.operation_service] = "OpsService"

    polling_method_options = descriptor_pb2.MethodOptions()
    polling_method_options.Extensions[ex_ops_pb2.operation_polling_method] = True

    T = descriptor_pb2.FieldDescriptorProto.Type
    operation_fields = tuple(
        make_field_pb2(name=name, type=T.Value("TYPE_STRING"), number=i)
        for i, name in enumerate(
            ("name", "status", "error_code", "error_message"), start=1
        )
    )
    for f in operation_fields:
        options = descriptor_pb2.FieldOptions()
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    with pytest.raises(ValueError):
        api_schema = api.Proto.build(
            make_file_pb2(
                "extended_lro.proto",
                package="exlro",
                messages=(
                    make_message_pb2(
                        name="Operation",
                        fields=operation_fields,
                    ),
                    make_message_pb2(
                        name="InitialRequest",
                    ),
                    make_message_pb2(
                        name="GetOperationRequest",
                    ),
                    make_message_pb2(
                        name="GetOperationResponse",
                    ),
                ),
                services=(
                    descriptor_pb2.ServiceDescriptorProto(
                        name="OpsService",
                        method=(
                            descriptor_pb2.MethodDescriptorProto(
                                name="Get",
                                input_type="exlro.GetOperationRequest",
                                output_type="exlro.GetOperationResponse",
                                options=polling_method_options,
                            ),
                        ),
                    ),
                    descriptor_pb2.ServiceDescriptorProto(
                        name="BasicService",
                        method=(
                            descriptor_pb2.MethodDescriptorProto(
                                name="Initiate",
                                input_type="exlro.InitialRequest",
                                output_type="exlro.Operation",
                                options=initiate_options,
                            ),
                        ),
                    ),
                ),
            ),
            file_to_generate=True,
            naming=make_naming(),
        )


def test_extended_lro_not_an_operation():
    initiate_options = descriptor_pb2.MethodOptions()
    initiate_options.Extensions[ex_ops_pb2.operation_service] = "OpsService"

    polling_method_options = descriptor_pb2.MethodOptions()
    polling_method_options.Extensions[ex_ops_pb2.operation_polling_method] = True

    with pytest.raises(ValueError):
        api_schema = api.Proto.build(
            make_file_pb2(
                "extended_lro.proto",
                package="exlro",
                messages=(
                    make_message_pb2(name="Operation"),
                    make_message_pb2(name="InitialRequest"),
                    make_message_pb2(name="GetOperationRequest"),
                ),
                services=(
                    descriptor_pb2.ServiceDescriptorProto(
                        name="OpsService",
                        method=(
                            descriptor_pb2.MethodDescriptorProto(
                                name="Get",
                                input_type="exlro.GetOperationRequest",
                                output_type="exlro.Operation",
                                options=polling_method_options,
                            ),
                        ),
                    ),
                    descriptor_pb2.ServiceDescriptorProto(
                        name="BasicService",
                        method=(
                            descriptor_pb2.MethodDescriptorProto(
                                name="Initiate",
                                input_type="exlro.InitialRequest",
                                output_type="exlro.Operation",
                                options=initiate_options,
                            ),
                        ),
                    ),
                ),
            ),
            file_to_generate=True,
            naming=make_naming(),
        )


def test_enums():
    L = descriptor_pb2.SourceCodeInfo.Location
    enum_pb = descriptor_pb2.EnumDescriptorProto(
        name="Silly",
        value=(
            descriptor_pb2.EnumValueDescriptorProto(name="ZERO", number=0),
            descriptor_pb2.EnumValueDescriptorProto(name="ONE", number=1),
            descriptor_pb2.EnumValueDescriptorProto(name="THREE", number=3),
        ),
    )
    fdp = make_file_pb2(
        package="google.enum.v1",
        enums=(enum_pb,),
        locations=(
            L(path=(5, 0), leading_comments="This is the Silly enum."),
            L(path=(5, 0, 2, 0), leading_comments="This is the zero value."),
            L(path=(5, 0, 2, 1), leading_comments="This is the one value."),
        ),
    )
    proto = api.Proto.build(fdp, file_to_generate=True, naming=make_naming())
    assert len(proto.enums) == 1
    enum = proto.enums["google.enum.v1.Silly"]
    assert enum.meta.doc == "This is the Silly enum."
    assert isinstance(enum, wrappers.EnumType)
    assert len(enum.values) == 3
    assert all([isinstance(i, wrappers.EnumValueType) for i in enum.values])
    assert enum.values[0].name == "ZERO"
    assert enum.values[0].meta.doc == "This is the zero value."
    assert enum.values[1].name == "ONE"
    assert enum.values[1].meta.doc == "This is the one value."
    assert enum.values[2].name == "THREE"
    assert enum.values[2].meta.doc == ""


def test_file_level_resources():
    fdp = make_file_pb2(
        name="nomenclature.proto",
        package="nomenclature.linneaen.v1",
        messages=(
            make_message_pb2(
                name="CreateSpeciesRequest",
                fields=(make_field_pb2(name="species", number=1, type=9),),
            ),
            make_message_pb2(
                name="CreateSpeciesResponse",
            ),
        ),
        services=(
            descriptor_pb2.ServiceDescriptorProto(
                name="SpeciesService",
                method=(
                    descriptor_pb2.MethodDescriptorProto(
                        name="CreateSpecies",
                        input_type="nomenclature.linneaen.v1.CreateSpeciesRequest",
                        output_type="nomenclature.linneaen.v1.CreateSpeciesResponse",
                    ),
                ),
            ),
        ),
    )
    res_pb2 = fdp.options.Extensions[resource_pb2.resource_definition]
    definitions = [
        (
            "nomenclature.linnaen.com/Species",
            "families/{family}/genera/{genus}/species/{species}",
        ),
        ("nomenclature.linnaen.com/Phylum", "kingdoms/{kingdom}/phyla/{phylum}"),
    ]
    for type_, pattern in definitions:
        resource_definition = res_pb2.add()
        resource_definition.type = type_
        resource_definition.pattern.append(pattern)

    species_field = fdp.message_type[0].field[0]
    resource_reference = species_field.options.Extensions[
        resource_pb2.resource_reference
    ]
    resource_reference.type = "nomenclature.linnaen.com/Species"

    api_schema = api.API.build([fdp], package="nomenclature.linneaen.v1")
    actual = api_schema.protos["nomenclature.proto"].resource_messages
    expected = collections.OrderedDict(
        (
            (
                "nomenclature.linnaen.com/Phylum",
                wrappers.CommonResource(
                    type_name="nomenclature.linnaen.com/Phylum",
                    pattern="kingdoms/{kingdom}/phyla/{phylum}",
                ).message_type,
            ),
            (
                "nomenclature.linnaen.com/Species",
                wrappers.CommonResource(
                    type_name="nomenclature.linnaen.com/Species",
                    pattern="families/{family}/genera/{genus}/species/{species}",
                ).message_type,
            ),
        )
    )

    assert actual == expected

    # The proto file _owns_ the file level resources, but the service needs to
    # see them too because the client class owns all the helper methods.
    service = api_schema.services["nomenclature.linneaen.v1.SpeciesService"]
    actual = service.visible_resources
    assert actual == expected

    # The service doesn't own any method that owns a message that references
    # Phylum, so the service doesn't count it among its resource messages.
    expected.pop("nomenclature.linnaen.com/Phylum")
    expected = tuple(expected.values())
    actual = service.resource_messages

    assert actual == expected


def test_resources_referenced_but_not_typed(reference_attr="type"):
    fdp = make_file_pb2(
        name="nomenclature.proto",
        package="nomenclature.linneaen.v1",
        messages=(
            make_message_pb2(
                name="Species",
            ),
            make_message_pb2(
                name="CreateSpeciesRequest",
                fields=(make_field_pb2(name="species", number=1, type=9),),
            ),
            make_message_pb2(
                name="CreateSpeciesResponse",
            ),
        ),
        services=(
            descriptor_pb2.ServiceDescriptorProto(
                name="SpeciesService",
                method=(
                    descriptor_pb2.MethodDescriptorProto(
                        name="CreateSpecies",
                        input_type="nomenclature.linneaen.v1.CreateSpeciesRequest",
                        output_type="nomenclature.linneaen.v1.CreateSpeciesResponse",
                    ),
                ),
            ),
        ),
    )

    # Set up the resource
    species_resource_opts = fdp.message_type[0].options.Extensions[
        resource_pb2.resource
    ]
    species_resource_opts.type = "nomenclature.linnaen.com/Species"
    species_resource_opts.pattern.append(
        "families/{family}/genera/{genus}/species/{species}"
    )

    # Set up the reference
    name_resource_opts = (
        fdp.message_type[1].field[0].options.Extensions[resource_pb2.resource_reference]
    )
    if reference_attr == "type":
        name_resource_opts.type = species_resource_opts.type
    else:
        name_resource_opts.child_type = species_resource_opts.type

    api_schema = api.API.build([fdp], package="nomenclature.linneaen.v1")
    expected = (api_schema.messages["nomenclature.linneaen.v1.Species"],)
    actual = api_schema.services[
        "nomenclature.linneaen.v1.SpeciesService"
    ].resource_messages

    assert actual == expected


def test_resources_referenced_but_not_typed_child_type():
    test_resources_referenced_but_not_typed("child_type")


def test_map_field_name_disambiguation():
    squid_file_pb = descriptor_pb2.FileDescriptorProto(
        name="mollusc.proto",
        package="animalia.mollusca.v2",
        message_type=(
            descriptor_pb2.DescriptorProto(
                name="Mollusc",
            ),
        ),
    )
    method_types_file_pb = descriptor_pb2.FileDescriptorProto(
        name="mollusc_service.proto",
        package="animalia.mollusca.v2",
        message_type=(
            descriptor_pb2.DescriptorProto(
                name="CreateMolluscRequest",
                field=(
                    descriptor_pb2.FieldDescriptorProto(
                        name="mollusc",
                        type="TYPE_MESSAGE",
                        type_name=".animalia.mollusca.v2.Mollusc",
                        number=1,
                    ),
                    descriptor_pb2.FieldDescriptorProto(
                        name="molluscs_map",
                        type="TYPE_MESSAGE",
                        number=2,
                        type_name=".animalia.mollusca.v2.CreateMolluscRequest.MolluscsMapEntry",
                        label="LABEL_REPEATED",
                    ),
                ),
                nested_type=(
                    descriptor_pb2.DescriptorProto(
                        name="MolluscsMapEntry",
                        field=(
                            descriptor_pb2.FieldDescriptorProto(
                                name="key",
                                type="TYPE_STRING",
                                number=1,
                            ),
                            descriptor_pb2.FieldDescriptorProto(
                                name="value",
                                type="TYPE_MESSAGE",
                                number=2,
                                # We use the same type for the map value as for
                                # the singleton above to better highlight the
                                # problem raised in
                                # https://github.com/googleapis/gapic-generator-python/issues/618.
                                # The module _is_ disambiguated for singleton
                                # fields but NOT for map fields.
                                type_name=".animalia.mollusca.v2.Mollusc",
                            ),
                        ),
                        options=descriptor_pb2.MessageOptions(map_entry=True),
                    ),
                ),
            ),
        ),
    )
    my_api = api.API.build(
        file_descriptors=[squid_file_pb, method_types_file_pb],
    )
    create = my_api.messages["animalia.mollusca.v2.CreateMolluscRequest"]
    mollusc = create.fields["mollusc"]
    molluscs_map = create.fields["molluscs_map"]
    mollusc_ident = str(mollusc.type.ident)
    mollusc_map_ident = str(molluscs_map.message.fields["value"].type.ident)

    # The same module used in the same place should have the same import alias.
    # Because there's a "mollusc" name used, the import should be disambiguated.
    assert mollusc_ident == mollusc_map_ident == "am_mollusc.Mollusc"


def test_gapic_metadata():
    apiVersion = "2025-11-03"
    serviceOptions = descriptor_pb2.ServiceOptions()
    serviceOptions.Extensions[client_pb2.api_version] = apiVersion

    api_schema = api.API.build(
        file_descriptors=[
            descriptor_pb2.FileDescriptorProto(
                name="cephalopod.proto",
                package="animalia.mollusca.v1",
                message_type=[
                    descriptor_pb2.DescriptorProto(
                        name="MolluscRequest",
                    ),
                    descriptor_pb2.DescriptorProto(
                        name="Mollusc",
                    ),
                ],
                service=[
                    descriptor_pb2.ServiceDescriptorProto(
                        name="Squid",
                        method=[
                            descriptor_pb2.MethodDescriptorProto(
                                name="Ramshorn",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                            descriptor_pb2.MethodDescriptorProto(
                                name="Humboldt",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                            descriptor_pb2.MethodDescriptorProto(
                                name="Giant",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                        ],
                        options=serviceOptions,
                    ),
                    descriptor_pb2.ServiceDescriptorProto(
                        name="Octopus",
                        method=[
                            descriptor_pb2.MethodDescriptorProto(
                                name="GiantPacific",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                            descriptor_pb2.MethodDescriptorProto(
                                name="BlueSpot",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                        ],
                    ),
                ],
            )
        ]
    )

    opts = Options.build("transport=grpc")
    expected = gapic_metadata_pb2.GapicMetadata(
        schema="1.0",
        comment="This file maps proto services/RPCs to the corresponding library clients/methods",
        language="python",
        proto_package="animalia.mollusca.v1",
        library_package="animalia.mollusca_v1",
        services={
            "Octopus": gapic_metadata_pb2.GapicMetadata.ServiceForTransport(
                clients={
                    "grpc": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="OctopusClient",
                        rpcs={
                            "BlueSpot": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["blue_spot"]
                            ),
                            "GiantPacific": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant_pacific"]
                            ),
                        },
                    ),
                    "grpc-async": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="OctopusAsyncClient",
                        rpcs={
                            "BlueSpot": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["blue_spot"]
                            ),
                            "GiantPacific": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant_pacific"]
                            ),
                        },
                    ),
                }
            ),
            "Squid": gapic_metadata_pb2.GapicMetadata.ServiceForTransport(
                api_version=apiVersion,
                clients={
                    "grpc": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="SquidClient",
                        rpcs={
                            "Giant": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant"]
                            ),
                            "Humboldt": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["humboldt"]
                            ),
                            "Ramshorn": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["ramshorn"]
                            ),
                        },
                    ),
                    "grpc-async": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="SquidAsyncClient",
                        rpcs={
                            "Giant": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant"]
                            ),
                            "Humboldt": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["humboldt"]
                            ),
                            "Ramshorn": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["ramshorn"]
                            ),
                        },
                    ),
                },
            ),
        },
    )
    actual = api_schema.gapic_metadata(opts)
    assert expected == actual
    expected = MessageToJson(expected, sort_keys=True)
    actual = api_schema.gapic_metadata_json(opts)
    assert expected == actual

    opts = Options.build("transport=rest")
    expected = gapic_metadata_pb2.GapicMetadata(
        schema="1.0",
        comment="This file maps proto services/RPCs to the corresponding library clients/methods",
        language="python",
        proto_package="animalia.mollusca.v1",
        library_package="animalia.mollusca_v1",
        services={
            "Octopus": gapic_metadata_pb2.GapicMetadata.ServiceForTransport(
                clients={
                    "rest": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="OctopusClient",
                        rpcs={
                            "BlueSpot": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["blue_spot"]
                            ),
                            "GiantPacific": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant_pacific"]
                            ),
                        },
                    )
                }
            ),
            "Squid": gapic_metadata_pb2.GapicMetadata.ServiceForTransport(
                api_version=apiVersion,
                clients={
                    "rest": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="SquidClient",
                        rpcs={
                            "Giant": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant"]
                            ),
                            "Humboldt": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["humboldt"]
                            ),
                            "Ramshorn": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["ramshorn"]
                            ),
                        },
                    ),
                },
            ),
        },
    )
    actual = api_schema.gapic_metadata(opts)
    assert expected == actual
    expected = MessageToJson(expected, sort_keys=True)
    actual = api_schema.gapic_metadata_json(opts)
    assert expected == actual

    opts = Options.build("transport=rest+grpc")
    expected = gapic_metadata_pb2.GapicMetadata(
        schema="1.0",
        comment="This file maps proto services/RPCs to the corresponding library clients/methods",
        language="python",
        proto_package="animalia.mollusca.v1",
        library_package="animalia.mollusca_v1",
        services={
            "Octopus": gapic_metadata_pb2.GapicMetadata.ServiceForTransport(
                clients={
                    "grpc": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="OctopusClient",
                        rpcs={
                            "BlueSpot": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["blue_spot"]
                            ),
                            "GiantPacific": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant_pacific"]
                            ),
                        },
                    ),
                    "grpc-async": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="OctopusAsyncClient",
                        rpcs={
                            "BlueSpot": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["blue_spot"]
                            ),
                            "GiantPacific": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant_pacific"]
                            ),
                        },
                    ),
                    "rest": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="OctopusClient",
                        rpcs={
                            "BlueSpot": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["blue_spot"]
                            ),
                            "GiantPacific": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant_pacific"]
                            ),
                        },
                    ),
                }
            ),
            "Squid": gapic_metadata_pb2.GapicMetadata.ServiceForTransport(
                api_version=apiVersion,
                clients={
                    "grpc": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="SquidClient",
                        rpcs={
                            "Giant": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant"]
                            ),
                            "Humboldt": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["humboldt"]
                            ),
                            "Ramshorn": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["ramshorn"]
                            ),
                        },
                    ),
                    "grpc-async": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="SquidAsyncClient",
                        rpcs={
                            "Giant": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant"]
                            ),
                            "Humboldt": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["humboldt"]
                            ),
                            "Ramshorn": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["ramshorn"]
                            ),
                        },
                    ),
                    "rest": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="SquidClient",
                        rpcs={
                            "Giant": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant"]
                            ),
                            "Humboldt": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["humboldt"]
                            ),
                            "Ramshorn": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["ramshorn"]
                            ),
                        },
                    ),
                },
            ),
        },
    )

    actual = api_schema.gapic_metadata(opts)
    assert expected == actual
    expected = MessageToJson(expected, sort_keys=True)
    actual = api_schema.gapic_metadata_json(opts)
    assert expected == actual


def test_gapic_metadata_internal_method():
    # Only have squid.Ramshorn as an internal method.
    service_yaml = get_service_yaml_for_selective_gapic_tests(
        apis=[
            "animalia.mollusca.v1.Squid",
            "animalia.mollusca.v1.Octopus",
        ],
        version="animalia.mollusca.v1",
        methods=[
            "animalia.mollusca.v1.Squid.Humboldt",
            "animalia.mollusca.v1.Squid.Giant",
            "animalia.mollusca.v1.Octopus.GiantPacific",
            "animalia.mollusca.v1.Octopus.BlueSpot",
        ],
        generate_omitted_as_internal=True,
    )

    api_schema = api.API.build(
        file_descriptors=[
            descriptor_pb2.FileDescriptorProto(
                name="cephalopod.proto",
                package="animalia.mollusca.v1",
                message_type=[
                    descriptor_pb2.DescriptorProto(
                        name="MolluscRequest",
                    ),
                    descriptor_pb2.DescriptorProto(
                        name="Mollusc",
                    ),
                ],
                service=[
                    descriptor_pb2.ServiceDescriptorProto(
                        name="Squid",
                        method=[
                            descriptor_pb2.MethodDescriptorProto(
                                name="Ramshorn",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                            descriptor_pb2.MethodDescriptorProto(
                                name="Humboldt",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                            descriptor_pb2.MethodDescriptorProto(
                                name="Giant",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                        ],
                    ),
                    descriptor_pb2.ServiceDescriptorProto(
                        name="Octopus",
                        method=[
                            descriptor_pb2.MethodDescriptorProto(
                                name="GiantPacific",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                            descriptor_pb2.MethodDescriptorProto(
                                name="BlueSpot",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                        ],
                    ),
                ],
            )
        ],
        package="animalia.mollusca.v1",
        opts=Options(service_yaml_config=service_yaml),
    )

    opts = Options.build("transport=grpc")
    expected = gapic_metadata_pb2.GapicMetadata(
        schema="1.0",
        comment="This file maps proto services/RPCs to the corresponding library clients/methods",
        language="python",
        proto_package="animalia.mollusca.v1",
        library_package="animalia.mollusca_v1",
        services={
            "Octopus": gapic_metadata_pb2.GapicMetadata.ServiceForTransport(
                clients={
                    "grpc": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="OctopusClient",
                        rpcs={
                            "BlueSpot": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["blue_spot"]
                            ),
                            "GiantPacific": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant_pacific"]
                            ),
                        },
                    ),
                    "grpc-async": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="OctopusAsyncClient",
                        rpcs={
                            "BlueSpot": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["blue_spot"]
                            ),
                            "GiantPacific": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant_pacific"]
                            ),
                        },
                    ),
                }
            ),
            "Squid": gapic_metadata_pb2.GapicMetadata.ServiceForTransport(
                clients={
                    "grpc": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="BaseSquidClient",
                        rpcs={
                            "Giant": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant"]
                            ),
                            "Humboldt": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["humboldt"]
                            ),
                            "Ramshorn": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["_ramshorn"]
                            ),
                        },
                    ),
                    "grpc-async": gapic_metadata_pb2.GapicMetadata.ServiceAsClient(
                        library_client="BaseSquidAsyncClient",
                        rpcs={
                            "Giant": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["giant"]
                            ),
                            "Humboldt": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["humboldt"]
                            ),
                            "Ramshorn": gapic_metadata_pb2.GapicMetadata.MethodList(
                                methods=["_ramshorn"]
                            ),
                        },
                    ),
                }
            ),
        },
    )

    actual = api_schema.gapic_metadata(opts)
    assert expected == actual
    expected = MessageToJson(expected, sort_keys=True)
    actual = api_schema.gapic_metadata_json(opts)
    assert expected == actual


def test_http_options(fs):
    fd = (
        make_file_pb2(
            name="example.proto",
            package="google.example.v1",
            messages=(make_message_pb2(name="ExampleRequest", fields=()),),
        ),
    )

    opts = Options(
        service_yaml_config={
            "http": {
                "rules": [
                    {
                        "selector": "Cancel",
                        "post": "/v3/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                    {
                        "selector": "Get",
                        "get": "/v3/{name=projects/*/locations/*/operations/*}",
                        "additional_bindings": [
                            {"get": "/v3/{name=/locations/*/operations/*}"}
                        ],
                    },
                ]
            }
        }
    )

    api_schema = api.API.build(fd, "google.example.v1", opts=opts)
    http_options = api_schema.http_options
    assert http_options == {
        "Cancel": [
            wrappers.HttpRule(
                method="post",
                uri="/v3/{name=projects/*/locations/*/operations/*}:cancel",
                body="*",
            )
        ],
        "Get": [
            wrappers.HttpRule(
                method="get",
                uri="/v3/{name=projects/*/locations/*/operations/*}",
                body=None,
            ),
            wrappers.HttpRule(
                method="get", uri="/v3/{name=/locations/*/operations/*}", body=None
            ),
        ],
    }


def generate_basic_extended_operations_setup():
    T = descriptor_pb2.FieldDescriptorProto.Type

    operation = make_message_pb2(
        name="Operation",
        fields=(
            make_field_pb2(name=name, type=T.Value("TYPE_STRING"), number=i)
            for i, name in enumerate(
                ("name", "status", "error_code", "error_message"), start=1
            )
        ),
    )

    for f in operation.field:
        options = descriptor_pb2.FieldOptions()
        # Note: The field numbers were carefully chosen to be the corresponding enum values.
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    options = descriptor_pb2.MethodOptions()
    options.Extensions[ex_ops_pb2.operation_polling_method] = True

    polling_method = descriptor_pb2.MethodDescriptorProto(
        name="Get",
        input_type="google.extended_operations.v1.stuff.GetOperation",
        output_type="google.extended_operations.v1.stuff.Operation",
        options=options,
    )

    delete_input_message = make_message_pb2(name="Input")
    delete_output_message = make_message_pb2(name="Output")
    ops_service = descriptor_pb2.ServiceDescriptorProto(
        name="CustomOperations",
        method=[
            polling_method,
            descriptor_pb2.MethodDescriptorProto(
                name="Delete",
                input_type="google.extended_operations.v1.stuff.Input",
                output_type="google.extended_operations.v1.stuff.Output",
            ),
        ],
    )

    request = make_message_pb2(
        name="GetOperation",
        fields=[make_field_pb2(name="name", type=T.Value("TYPE_STRING"), number=1)],
    )

    initial_opts = descriptor_pb2.MethodOptions()
    initial_opts.Extensions[ex_ops_pb2.operation_service] = ops_service.name
    initial_input_message = make_message_pb2(name="Initial")
    initial_method = descriptor_pb2.MethodDescriptorProto(
        name="CreateTask",
        input_type="google.extended_operations.v1.stuff.GetOperation",
        output_type="google.extended_operations.v1.stuff.Operation",
        options=initial_opts,
    )

    regular_service = descriptor_pb2.ServiceDescriptorProto(
        name="RegularService",
        method=[
            initial_method,
        ],
    )

    file_protos = [
        make_file_pb2(
            name="extended_operations.proto",
            package="google.extended_operations.v1.stuff",
            messages=[
                operation,
                request,
                delete_output_message,
                delete_input_message,
                initial_input_message,
            ],
            services=[
                ops_service,
                regular_service,
            ],
        ),
    ]

    return file_protos


def test_extended_operations_lro_operation_service():
    file_protos = generate_basic_extended_operations_setup()
    api_schema = api.API.build(file_protos)
    regular_service = api_schema.services[
        "google.extended_operations.v1.stuff.RegularService"
    ]
    initial_method = regular_service.methods["CreateTask"]

    operation_service = api_schema.services[
        "google.extended_operations.v1.stuff.CustomOperations"
    ]
    expected = operation_service
    actual = api_schema.get_custom_operation_service(initial_method)

    assert expected is actual

    assert actual.operation_polling_method is actual.methods["Get"]

    expected = {operation_service}
    actual = api_schema.get_extended_operations_services(regular_service)
    assert expected == actual


def test_extended_operations_lro_operation_service_no_annotation():
    file_protos = generate_basic_extended_operations_setup()
    api_schema = api.API.build(file_protos)
    initial_method = api_schema.services[
        "google.extended_operations.v1.stuff.RegularService"
    ].methods["CreateTask"]

    # It's easier to manipulate data structures after building the API.
    del initial_method.options.Extensions[ex_ops_pb2.operation_service]

    with pytest.raises(ValueError):
        api_schema.get_custom_operation_service(initial_method)


def test_extended_operations_lro_operation_service_no_such_service():
    file_protos = generate_basic_extended_operations_setup()

    api_schema = api.API.build(file_protos)
    initial_method = api_schema.services[
        "google.extended_operations.v1.stuff.RegularService"
    ].methods["CreateTask"]
    initial_method.options.Extensions[ex_ops_pb2.operation_service] = "UnrealService"

    with pytest.raises(ValueError):
        api_schema.get_custom_operation_service(initial_method)


def test_extended_operations_lro_operation_service_not_an_lro():
    file_protos = generate_basic_extended_operations_setup()

    api_schema = api.API.build(file_protos)
    initial_method = api_schema.services[
        "google.extended_operations.v1.stuff.RegularService"
    ].methods["CreateTask"]
    # Hack to pretend that the initial_method is not an LRO
    super(type(initial_method), initial_method).__setattr__(
        "output", initial_method.input
    )

    with pytest.raises(ValueError):
        api_schema.get_custom_operation_service(initial_method)


def test_extended_operations_lro_operation_service_no_polling_method():
    file_protos = generate_basic_extended_operations_setup()

    api_schema = api.API.build(file_protos)
    initial_method = api_schema.services[
        "google.extended_operations.v1.stuff.RegularService"
    ].methods["CreateTask"]

    operation_service = api_schema.services[
        "google.extended_operations.v1.stuff.CustomOperations"
    ]
    del operation_service.methods["Get"].options.Extensions[
        ex_ops_pb2.operation_polling_method
    ]

    with pytest.raises(ValueError):
        api_schema.get_custom_operation_service(initial_method)


def methods_from_service(service_pb, name: str):
    service = service_pb.DESCRIPTOR.services_by_name[name]
    res = {}
    for m in service.methods:
        x = descriptor_pb2.MethodDescriptorProto()
        m.CopyToProto(x)
        res[x.name] = x
    return res


def test_mixin_api_methods_locations():
    fd = (
        make_file_pb2(
            name="example.proto",
            package="google.example.v1",
            messages=(make_message_pb2(name="ExampleRequest", fields=()),),
        ),
    )
    opts = Options(
        service_yaml_config={
            "apis": [{"name": "google.cloud.location.Locations"}],
            "http": {
                "rules": [
                    {
                        "selector": "google.cloud.location.Locations.ListLocations",
                        "get": "/v1/{name=examples/*}/*",
                        "body": "*",
                    },
                    {
                        "selector": "google.cloud.location.Locations.GetLocation",
                        "get": "/v1/{name=examples/*}/*",
                        "body": "*",
                    },
                    {
                        "selector": "google.example.v1.Example",
                    },
                ]
            },
        }
    )
    ms = methods_from_service(locations_pb2, "Locations")
    assert len(ms) == 2
    m1 = ms["ListLocations"]
    m1.options.ClearExtension(annotations_pb2.http)
    m1.options.Extensions[
        annotations_pb2.http
    ].selector = "google.cloud.location.Locations.ListLocations"
    m1.options.Extensions[annotations_pb2.http].get = "/v1/{name=examples/*}/*"
    m1.options.Extensions[annotations_pb2.http].body = "*"
    m2 = ms["GetLocation"]
    m2.options.ClearExtension(annotations_pb2.http)
    m2.options.Extensions[
        annotations_pb2.http
    ].selector = "google.cloud.location.Locations.GetLocation"
    m2.options.Extensions[annotations_pb2.http].get = "/v1/{name=examples/*}/*"
    m2.options.Extensions[annotations_pb2.http].body = "*"
    api_schema = api.API.build(fd, "google.example.v1", opts=opts)
    assert api_schema.mixin_api_methods == {"ListLocations": m1, "GetLocation": m2}


def test_mixin_api_methods_iam():
    fd = (
        make_file_pb2(
            name="example.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="ExampleRequest", fields=()),
                make_message_pb2(name="ExampleResponse", fields=()),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="FooMethod",
                            # Input and output types don't matter.
                            input_type="google.example.v1.ExampleRequest",
                            output_type="google.example.v1.ExampleResponse",
                        ),
                    ),
                ),
            ),
        ),
    )
    r1 = {
        "selector": "google.iam.v1.IAMPolicy.SetIamPolicy",
        "post": "/v1/{resource=examples/*}/*",
        "body": "*",
    }
    r2 = {
        "selector": "google.iam.v1.IAMPolicy.GetIamPolicy",
        "get": "/v1/{resource=examples/*}/*",
        "body": "*",
    }
    r3 = {
        "selector": "google.iam.v1.IAMPolicy.TestIamPermissions",
        "post": "/v1/{resource=examples/*}/*",
        "body": "*",
    }
    opts = Options(
        service_yaml_config={
            "apis": [{"name": "google.iam.v1.IAMPolicy"}],
            "http": {"rules": [r1, r2, r3]},
        }
    )
    ms = methods_from_service(iam_policy_pb2, "IAMPolicy")
    assert len(ms) == 3
    m1 = ms["SetIamPolicy"]
    m1.options.ClearExtension(annotations_pb2.http)
    m1.options.Extensions[annotations_pb2.http].selector = r1["selector"]
    m1.options.Extensions[annotations_pb2.http].post = r1["post"]
    m1.options.Extensions[annotations_pb2.http].body = r1["body"]
    m2 = ms["GetIamPolicy"]
    m2.options.ClearExtension(annotations_pb2.http)
    m2.options.Extensions[annotations_pb2.http].selector = r2["selector"]
    m2.options.Extensions[annotations_pb2.http].get = r2["get"]
    m2.options.Extensions[annotations_pb2.http].body = r2["body"]
    m3 = ms["TestIamPermissions"]
    m3.options.ClearExtension(annotations_pb2.http)
    m3.options.Extensions[annotations_pb2.http].selector = r3["selector"]
    m3.options.Extensions[annotations_pb2.http].post = r3["post"]
    m3.options.Extensions[annotations_pb2.http].body = r3["body"]
    api_schema = api.API.build(fd, "google.example.v1", opts=opts)
    assert api_schema.mixin_api_methods == {
        "SetIamPolicy": m1,
        "GetIamPolicy": m2,
        "TestIamPermissions": m3,
    }
    assert not api_schema.has_operations_mixin


def test_mixin_api_methods_iam_overrides():
    fd = (
        make_file_pb2(
            name="example.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="ExampleRequest", fields=()),
                make_message_pb2(name="ExampleResponse", fields=()),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="TestIamPermissions",
                            # Input and output types don't matter.
                            input_type="google.example.v1.ExampleRequest",
                            output_type="google.example.v1.ExampleResponse",
                        ),
                    ),
                ),
            ),
        ),
    )
    r1 = {
        "selector": "google.iam.v1.IAMPolicy.SetIamPolicy",
        "post": "/v1/{resource=examples/*}/*",
        "body": "*",
    }
    r2 = {
        "selector": "google.iam.v1.IAMPolicy.GetIamPolicy",
        "get": "/v1/{resource=examples/*}/*",
        "body": "*",
    }
    r3 = {
        "selector": "google.iam.v1.IAMPolicy.TestIamPermissions",
        "post": "/v1/{resource=examples/*}/*",
        "body": "*",
    }
    opts = Options(
        service_yaml_config={
            "apis": [{"name": "google.iam.v1.IAMPolicy"}],
            "http": {"rules": [r1, r2, r3]},
        }
    )
    api_schema = api.API.build(fd, "google.example.v1", opts=opts)
    assert api_schema.mixin_api_methods == {}


def create_service_config_with_all_mixins(http_opt_uri="/v1/{name=examples/*}/*"):
    service_yaml_config = {
        "apis": [
            {
                "name": "google.cloud.location.Locations",
            },
            {
                "name": "google.longrunning.Operations",
            },
            {
                "name": "google.iam.v1.IAMPolicy",
            },
        ],
        "http": {
            "rules": [
                # Locations
                {
                    "selector": "google.cloud.location.Locations.ListLocations",
                    "get": http_opt_uri,
                    "body": "*",
                },
                {
                    "selector": "google.cloud.location.Locations.GetLocation",
                    "get": http_opt_uri,
                    "body": "*",
                },
                # LRO
                {
                    "selector": "google.longrunning.Operations.CancelOperation",
                    "post": http_opt_uri,
                    "body": "*",
                },
                {
                    "selector": "google.longrunning.Operations.DeleteOperation",
                    "get": http_opt_uri,
                    "body": "*",
                },
                {
                    "selector": "google.longrunning.Operations.WaitOperation",
                    "post": http_opt_uri,
                    "body": "*",
                },
                {
                    "selector": "google.longrunning.Operations.GetOperation",
                    "post": http_opt_uri,
                    "body": "*",
                },
                {
                    "selector": "google.longrunning.Operations.ListOperations",
                    "post": http_opt_uri,
                    "body": "*",
                },
                # IAM
                {
                    "selector": "google.iam.v1.IAMPolicy.SetIamPolicy",
                    "post": http_opt_uri,
                    "body": "*",
                },
                {
                    "selector": "google.iam.v1.IAMPolicy.GetIamPolicy",
                    "get": http_opt_uri,
                    "body": "*",
                },
                {
                    "selector": "google.iam.v1.IAMPolicy.TestIamPermissions",
                    "post": http_opt_uri,
                    "body": "*",
                },
                {
                    "selector": "google.example.v1.Example",
                },
            ]
        },
    }
    return service_yaml_config


def test_mixin_api_signatures():
    fd = (
        make_file_pb2(
            name="example.proto",
            package="google.example.v1",
            messages=(make_message_pb2(name="ExampleRequest", fields=()),),
        ),
    )
    opts = Options(service_yaml_config=create_service_config_with_all_mixins())
    api_schema = api.API.build(fd, "google.example.v1", opts=opts)
    res = api_schema.mixin_api_signatures
    assert res == mixins.MIXINS_MAP
    assert res["GetOperation"].rpc_name == "google.longrunning.Operations/GetOperation"
    assert res["GetIamPolicy"].rpc_name == "google.iam.v1.IAMPolicy/GetIamPolicy"
    assert res["GetLocation"].rpc_name == "google.cloud.location.Locations/GetLocation"


def test_mixin_http_options():
    fd = (
        make_file_pb2(
            name="example.proto",
            package="google.example.v1",
            messages=(make_message_pb2(name="ExampleRequest", fields=()),),
        ),
    )
    opts = Options(
        service_yaml_config={
            "apis": [
                {
                    "name": "google.cloud.location.Locations",
                },
                {
                    "name": "google.longrunning.Operations",
                },
                {
                    "name": "google.iam.v1.IAMPolicy",
                },
            ],
            "http": {
                "rules": [
                    # LRO
                    {
                        "selector": "google.longrunning.Operations.CancelOperation",
                        "post": "/v1/{name=examples/*}/*",
                        "body": "*",
                    },
                    {
                        "selector": "google.longrunning.Operations.DeleteOperation",
                        "get": "/v1/{name=examples/*}/*",
                        "body": "*",
                    },
                    {
                        "selector": "google.longrunning.Operations.WaitOperation",
                        "post": "/v1/{name=examples/*}/*",
                        "body": "*",
                    },
                    {
                        "selector": "google.longrunning.Operations.GetOperation",
                        "post": "/v1/{name=examples/*}/*",
                        "body": "*",
                    },
                    {
                        "selector": "google.longrunning.Operations.ListOperations",
                        "post": "/v1/{name=examples/*}/*",
                        "body": "*",
                    },
                ]
            },
        }
    )
    api_schema = api.API.build(fd, "google.example.v1", opts=opts)
    res = api_schema.mixin_http_options
    assert res == {
        "ListOperations": [
            wrappers.MixinHttpRule("post", "/v1/{name=examples/*}/*", "*")
        ],
        "GetOperation": [
            wrappers.MixinHttpRule("post", "/v1/{name=examples/*}/*", "*")
        ],
        "DeleteOperation": [
            wrappers.MixinHttpRule("get", "/v1/{name=examples/*}/*", "*")
        ],
        "CancelOperation": [
            wrappers.MixinHttpRule("post", "/v1/{name=examples/*}/*", "*")
        ],
        "WaitOperation": [
            wrappers.MixinHttpRule("post", "/v1/{name=examples/*}/*", "*")
        ],
    }


def test_mixin_api_methods_lro():
    fd = (
        make_file_pb2(
            name="example.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="ExampleRequest", fields=()),
                make_message_pb2(name="ExampleResponse", fields=()),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="FooMethod",
                            # Input and output types don't matter.
                            input_type="google.example.v1.ExampleRequest",
                            output_type="google.example.v1.ExampleResponse",
                        ),
                    ),
                ),
            ),
        ),
    )
    r1 = {
        "selector": "google.longrunning.Operations.CancelOperation",
        "post": "/v1/{name=examples/*}/*",
        "body": "*",
    }
    r2 = {
        "selector": "google.longrunning.Operations.DeleteOperation",
        "get": "/v1/{name=examples/*}/*",
        "body": "*",
    }
    r3 = {
        "selector": "google.longrunning.Operations.WaitOperation",
        "post": "/v1/{name=examples/*}/*",
        "body": "*",
    }
    r4 = {
        "selector": "google.longrunning.Operations.GetOperation",
        "post": "/v1/{name=examples/*}/*",
        "body": "*",
    }
    opts = Options(
        service_yaml_config={
            "apis": [{"name": "google.longrunning.Operations"}],
            "http": {"rules": [r1, r2, r3, r4]},
        }
    )

    ms = methods_from_service(operations_pb2, "Operations")
    assert len(ms) == 5
    m1 = ms["CancelOperation"]
    m1.options.ClearExtension(annotations_pb2.http)
    m1.options.Extensions[annotations_pb2.http].selector = r1["selector"]
    m1.options.Extensions[annotations_pb2.http].post = r1["post"]
    m1.options.Extensions[annotations_pb2.http].body = r1["body"]
    m2 = ms["DeleteOperation"]
    m2.options.ClearExtension(annotations_pb2.http)
    m2.options.Extensions[annotations_pb2.http].selector = r2["selector"]
    m2.options.Extensions[annotations_pb2.http].get = r2["get"]
    m2.options.Extensions[annotations_pb2.http].body = r2["body"]
    m3 = ms["WaitOperation"]
    m3.options.ClearExtension(annotations_pb2.http)
    m3.options.Extensions[annotations_pb2.http].selector = r3["selector"]
    m3.options.Extensions[annotations_pb2.http].post = r3["post"]
    m3.options.Extensions[annotations_pb2.http].body = r3["body"]
    m4 = ms["GetOperation"]
    m4.options.ClearExtension(annotations_pb2.http)
    m4.options.Extensions[annotations_pb2.http].selector = r4["selector"]
    m4.options.Extensions[annotations_pb2.http].post = r4["post"]
    m4.options.Extensions[annotations_pb2.http].body = r4["body"]

    api_schema = api.API.build(fd, "google.example.v1", opts=opts)
    assert api_schema.mixin_api_methods == {
        "CancelOperation": m1,
        "DeleteOperation": m2,
        "WaitOperation": m3,
        "GetOperation": m4,
    }


def test_has_iam_mixin():
    # Check that has_iam_mixin() property of API returns True when the
    # service YAML contains `google.iam.v1.IAMPolicy`.
    fd = (
        make_file_pb2(
            name="example.proto",
            package="google.example.v1",
            messages=(make_message_pb2(name="ExampleRequest", fields=()),),
        ),
    )
    opts = Options(
        service_yaml_config={
            "apis": [{"name": "google.iam.v1.IAMPolicy"}],
        }
    )
    api_schema = api.API.build(fd, "google.example.v1", opts=opts)
    assert api_schema.has_iam_mixin


def get_file_descriptor_proto_for_tests(
    fields: Sequence[descriptor_pb2.FieldDescriptorProto] = None,
    client_streaming: bool = False,
    server_streaming: bool = False,
) -> descriptor_pb2.FileDescriptorProto:
    """
    Args:
        fields (Sequence[descriptor_pb2.FieldDescriptorProto]): Fields to include
            in messages in the return object `descriptor_pb2.FileDescriptorProto`.
        client_streaming (bool): Whether the methods in the return object
            `descriptor_pb2.FileDescriptorProto` should use client streaming.
        server_streaming (bool): Whether the methods in the return object
            `descriptor_pb2.FileDescriptorProto` should use server streaming.
    Returns:
        descriptor_pb2.FileDescriptorProto: Returns an object describing the API.
    """

    field_options = descriptor_pb2.FieldOptions()
    field_options.Extensions[
        field_info_pb2.field_info
    ].format = field_info_pb2.FieldInfo.Format.Value("UUID4")

    fd = (
        make_file_pb2(
            name="someexample.proto",
            package="google.example.v1beta1",
            messages=(
                make_message_pb2(name="ExampleRequest", fields=fields),
                make_message_pb2(name="ExampleResponse", fields=()),
                make_message_pb2(
                    name="NestedMessage",
                    fields=(
                        make_field_pb2(
                            name="squid",
                            options=field_options,
                            type="TYPE_STRING",
                            number=1,
                        ),
                    ),
                    options=descriptor_pb2.MessageOptions(map_entry=True),
                ),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="ServiceOne",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="Example1",
                            input_type="google.example.v1beta1.ExampleRequest",
                            output_type="google.example.v1beta1.ExampleResponse",
                            client_streaming=client_streaming,
                            server_streaming=server_streaming,
                        ),
                    ),
                ),
                descriptor_pb2.ServiceDescriptorProto(
                    name="ServiceTwo",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="Example1",
                            input_type="google.example.v1beta1.ExampleRequest",
                            output_type="google.example.v1beta1.ExampleResponse",
                            client_streaming=client_streaming,
                            server_streaming=server_streaming,
                        ),
                    ),
                ),
            ),
        ),
    )
    return fd


def test_api_all_methods():
    """
    Tests the `all_methods` method of `gapic.schema.api` method which returns a map of
    all methods for the API.
    """
    fd = get_file_descriptor_proto_for_tests()
    api_schema = api.API.build(fd, "google.example.v1beta1")
    assert len(api_schema.all_methods) == 2
    assert list(api_schema.all_methods.keys()) == [
        "google.example.v1beta1.ServiceOne.Example1",
        "google.example.v1beta1.ServiceTwo.Example1",
    ]


def test_read_python_settings_from_service_yaml():
    service_yaml_config = {
        "apis": [
            {"name": "google.example.v1beta1.ServiceOne.Example1"},
        ],
        "publishing": {
            "library_settings": [
                {
                    "version": "google.example.v1beta1",
                    "python_settings": {
                        "experimental_features": {"rest_async_io_enabled": True},
                    },
                }
            ]
        },
    }
    cli_options = Options(service_yaml_config=service_yaml_config)
    fd = get_file_descriptor_proto_for_tests(fields=[])
    api_schema = api.API.build(fd, "google.example.v1beta1", opts=cli_options)
    assert api_schema.all_library_settings == {
        "google.example.v1beta1": client_pb2.ClientLibrarySettings(
            version="google.example.v1beta1",
            python_settings=client_pb2.PythonSettings(
                experimental_features=client_pb2.PythonSettings.ExperimentalFeatures(
                    rest_async_io_enabled=True
                )
            ),
        )
    }


def test_read_empty_python_settings_from_service_yaml():
    service_yaml_config = {
        "apis": [
            {"name": "google.example.v1beta1.ServiceOne.Example1"},
        ],
    }
    cli_options = Options(service_yaml_config=service_yaml_config)
    fd = get_file_descriptor_proto_for_tests(fields=[])
    api_schema = api.API.build(fd, "google.example.v1beta1", opts=cli_options)
    assert (
        api_schema.all_library_settings["google.example.v1beta1"].python_settings
        == client_pb2.PythonSettings()
    )
    assert (
        api_schema.all_library_settings[
            "google.example.v1beta1"
        ].python_settings.experimental_features
        == client_pb2.PythonSettings.ExperimentalFeatures()
    )
    assert (
        api_schema.all_library_settings[
            "google.example.v1beta1"
        ].python_settings.experimental_features.rest_async_io_enabled
        == False
    )
    assert (
        api_schema.all_library_settings[api_schema.naming.proto_package].python_settings
        == client_pb2.PythonSettings()
    )


def test_python_settings_selective_gapic_nonexistent_method_raises_error():
    """
    Test that `ClientLibrarySettingsError` is raised when there are nonexistent methods in
    `client_pb2.ClientLibrarySettings.PythonSettings.CommonSettings.SelectiveGapicGeneration`.
    """
    client_library_settings = [
        client_pb2.ClientLibrarySettings(
            version="google.example.v1beta1",
            python_settings=client_pb2.PythonSettings(
                common=client_pb2.CommonLanguageSettings(
                    selective_gapic_generation=client_pb2.SelectiveGapicGeneration(
                        methods=["google.example.v1beta1.ServiceOne.DoesNotExist"]
                    )
                )
            ),
        )
    ]
    fd = get_file_descriptor_proto_for_tests(fields=[])
    api_schema = api.API.build(fd, "google.example.v1beta1")
    with pytest.raises(
        api.ClientLibrarySettingsError,
        match="(?i)google.example.v1beta1.ServiceOne.DoesNotExist: Method does not exist",
    ):
        api_schema.enforce_valid_library_settings(client_library_settings)


def test_python_settings_selective_gapic_version_mismatch_method_raises_error():
    """
    Test that `ClientLibrarySettingsError` is raised when a method listed for selective generation
    exists only in a different version of the library.
    """
    client_library_settings = [
        client_pb2.ClientLibrarySettings(
            version="google.example.v2beta2",
            python_settings=client_pb2.PythonSettings(
                common=client_pb2.CommonLanguageSettings(
                    selective_gapic_generation=client_pb2.SelectiveGapicGeneration(
                        methods=["google.example.v1beta1.ServiceOne.Example1"]
                    )
                )
            ),
        )
    ]
    fd = get_file_descriptor_proto_for_tests(fields=[])
    api_schema = api.API.build(fd, "google.example.v1beta1")
    with pytest.raises(
        api.ClientLibrarySettingsError,
        match="(?i)google.example.v1beta1.ServiceOne.Example1: Mismatched version for method.",
    ):
        api_schema.enforce_valid_library_settings(client_library_settings)


def get_service_yaml_for_selective_gapic_tests(
    apis: Sequence[str] = ["google.example.v1.FooService"],
    version: str = "google.example.v1",
    methods=["google.example.v1.FooService.GetFoo"],
    generate_omitted_as_internal=False,
) -> Dict[str, Any]:
    return {
        "apis": [{"name": api} for api in apis],
        "publishing": {
            "library_settings": [
                {
                    "version": version,
                    "python_settings": {
                        "experimental_features": {"rest_async_io_enabled": True},
                        "common": {
                            "selective_gapic_generation": {
                                "methods": methods,
                                "generate_omitted_as_internal": generate_omitted_as_internal,
                            }
                        },
                    },
                }
            ]
        },
    }


def test_selective_gapic_api_build():
    # Put together a couple of minimal protos.
    fd = (
        make_file_pb2(
            name="dep.proto",
            package="google.dep",
            messages=(make_message_pb2(name="ImportedMessage", fields=()),),
        ),
        make_file_pb2(
            name="common.proto",
            package="google.example.v1.common",
            messages=(
                make_message_pb2(name="Bar"),
                make_message_pb2(name="Baz"),
            ),
        ),
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Foo", fields=()),
                make_message_pb2(
                    name="GetFooRequest",
                    fields=(
                        make_field_pb2(
                            name="imported_message",
                            number=1,
                            type_name=".google.dep.ImportedMessage",
                        ),
                        make_field_pb2(name="primitive", number=2, type=1),
                        make_field_pb2(
                            name="bar",
                            number=1,
                            type_name=".google.example.v1.common.Bar",
                        ),
                    ),
                ),
                make_message_pb2(
                    name="GetFooResponse",
                    fields=(
                        make_field_pb2(
                            name="foo", number=1, type_name=".google.example.v1.Foo"
                        ),
                    ),
                ),
                make_message_pb2(
                    name="DeleteFooRequest",
                    fields=(
                        make_field_pb2(
                            name="foo", number=1, type_name=".google.example.v1.Foo"
                        ),
                        make_field_pb2(
                            name="baz",
                            number=2,
                            type_name=".google.example.v1.common.Baz",
                        ),
                    ),
                ),
                make_message_pb2(
                    name="DeleteFooResponse",
                    fields=(make_field_pb2(name="success", number=1, type=8),),
                ),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetFoo",
                            input_type="google.example.v1.GetFooRequest",
                            output_type="google.example.v1.GetFooResponse",
                        ),
                        descriptor_pb2.MethodDescriptorProto(
                            name="DeleteFoo",
                            input_type="google.example.v1.DeleteFooRequest",
                            output_type="google.example.v1.DeleteFooResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        methods=["google.example.v1.FooService.GetFoo"]
    )
    opts = Options(service_yaml_config=service_yaml_config)

    # Create an API with those protos.
    api_schema = api.API.build(fd, package="google.example.v1", opts=opts)

    # Establish that the API has the data expected.
    assert isinstance(api_schema, api.API)

    # foo.proto, common.proto, dep.proto
    assert len(api_schema.all_protos) == 3
    assert len(api_schema.protos) == 2  # foo.proto, common.proto

    assert "google.dep.ImportedMessage" not in api_schema.messages
    assert "google.example.v1.Foo" in api_schema.messages
    assert "google.example.v1.GetFooRequest" in api_schema.messages
    assert "google.example.v1.GetFooResponse" in api_schema.messages
    assert "google.example.v1.DeleteFooRequest" not in api_schema.messages
    assert "google.example.v1.DeleteFooResponse" not in api_schema.messages
    # Baz is used by DeleteFooRequest, which is omitted, but Baz itself should be kept.
    assert "google.example.v1.common.Baz" in api_schema.messages
    assert "google.example.v1.FooService" in api_schema.services
    assert len(api_schema.enums) == 0
    assert api_schema.protos["foo.proto"].python_modules == (
        imp.Import(package=("google", "dep"), module="dep_pb2"),
        imp.Import(
            package=("google", "example_v1", "common", "types"), module="common"
        ),
    )

    assert api_schema.requires_package(("google", "example", "v1"))

    assert not api_schema.requires_package(("elgoog", "example", "v1"))

    # Establish that the subpackages still work even when they are transitively
    # partially pruned.
    assert "common" in api_schema.subpackages
    sub = api_schema.subpackages["common"]
    assert len(sub.protos) == 1
    assert "google.example.v1.common.Bar" in sub.messages
    # Baz is reachable from DeleteFooRequest, which is omitted, but
    # Baz itself should be part of the generation.
    assert "google.example.v1.common.Baz" in sub.messages
    # Establish that methods have been truncated
    assert "google.example.v1.FooService.GetFoo" in api_schema.all_methods
    assert "google.example.v1.FooService.DeleteFoo" not in api_schema.all_methods

    foo_service = api_schema.protos["foo.proto"].services[
        "google.example.v1.FooService"
    ]
    assert "DeleteFoo" not in foo_service.methods
    assert "GetFoo" in foo_service.methods


def test_selective_gapic_api_build_with_lro():
    # Set up a prior proto that mimics google/protobuf/empty.proto
    lro_proto = api.Proto.build(
        make_file_pb2(
            name="operations.proto",
            package="google.longrunning",
            messages=(make_message_pb2(name="Operation"),),
        ),
        file_to_generate=False,
        naming=make_naming(),
    )

    # Set up methods with LRO annotations.
    create_foo_method_pb2 = descriptor_pb2.MethodDescriptorProto(
        name="AsyncCreateFoo",
        input_type="google.example.v1.AsyncCreateFooRequest",
        output_type="google.longrunning.Operation",
    )
    create_foo_method_pb2.options.Extensions[operations_pb2.operation_info].MergeFrom(
        operations_pb2.OperationInfo(
            response_type="google.example.v1.AsyncCreateFooResponse",
            metadata_type="google.example.v1.AsyncCreateFooMetadata",
        ),
    )

    create_bar_method_pb2 = descriptor_pb2.MethodDescriptorProto(
        name="AsyncCreateBar",
        input_type="google.example.v1.AsyncCreateBarRequest",
        output_type="google.longrunning.Operation",
    )
    create_bar_method_pb2.options.Extensions[operations_pb2.operation_info].MergeFrom(
        operations_pb2.OperationInfo(
            response_type="google.example.v1.AsyncCreateBarResponse",
            metadata_type="google.example.v1.AsyncCreateBarMetadata",
        ),
    )

    # Set up the service with an RPC.
    fd = (
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Foo", fields=()),
                make_message_pb2(name="Bar", fields=()),
                make_message_pb2(name="AsyncCreateFooRequest", fields=()),
                make_message_pb2(name="AsyncCreateFooResponse", fields=()),
                make_message_pb2(
                    name="AsyncCreateFooMetadata",
                    fields=(
                        make_field_pb2(
                            name="foo", number=1, type_name=".google.example.v1.Foo"
                        ),
                    ),
                ),
                make_message_pb2(name="AsyncCreateBarRequest", fields=()),
                make_message_pb2(name="AsyncCreateBarResponse", fields=()),
                make_message_pb2(
                    name="AsyncCreateBarMetadata",
                    fields=(
                        make_field_pb2(
                            name="bar", number=1, type_name=".google.example.v1.Bar"
                        ),
                    ),
                ),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        create_foo_method_pb2,
                        create_bar_method_pb2,
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        apis=["google.example.v1.FooService"],
        methods=["google.example.v1.FooService.AsyncCreateFoo"],
    )
    opts = Options(service_yaml_config=service_yaml_config)

    api_schema = api.API.build(
        fd,
        "google.example.v1",
        opts=opts,
        prior_protos={
            "google/longrunning/operations.proto": lro_proto,
        },
    )

    assert "google.example.v1.Foo" in api_schema.messages
    assert "google.example.v1.AsyncCreateFooRequest" in api_schema.messages
    assert "google.example.v1.AsyncCreateFooResponse" in api_schema.messages
    assert "google.example.v1.AsyncCreateFooMetadata" in api_schema.messages

    # Top-level request/response messages for omitted RPCs are still omitted.
    assert "google.example.v1.AsyncCreateBarRequest" not in api_schema.messages
    # AsyncCreateBarResponse and AsyncCreateBarMetadata are LRO response/metadata types
    # for an omitted RPC, so they should be omitted.
    assert "google.example.v1.AsyncCreateBarResponse" not in api_schema.messages
    assert "google.example.v1.AsyncCreateBarMetadata" not in api_schema.messages

    # Bar is reachable from AsyncCreateBarMetadata, and since Bar itself is NOT
    # a top-level request/response message of an omitted RPC, it should be KEPT.
    assert "google.example.v1.Bar" in api_schema.messages


def test_selective_gapic_api_build_remove_unnecessary_services():
    # Put together a couple of minimal protos.
    fd = (
        make_file_pb2(
            name="foobar.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Foo", fields=()),
                make_message_pb2(name="Bar", fields=()),
                make_message_pb2(
                    name="GetFooRequest",
                    fields=(
                        make_field_pb2(
                            name="foo", number=1, type_name=".google.example.v1.Foo"
                        ),
                    ),
                ),
                make_message_pb2(name="GetFooResponse", fields=()),
                make_message_pb2(
                    name="GetBarRequest",
                    fields=(
                        make_field_pb2(
                            name="bar", number=1, type_name=".google.example.v1.Bar"
                        ),
                    ),
                ),
                make_message_pb2(name="GetBarResponse", fields=()),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetFoo",
                            input_type="google.example.v1.GetFooRequest",
                            output_type="google.example.v1.GetFooResponse",
                        ),
                    ),
                ),
                descriptor_pb2.ServiceDescriptorProto(
                    name="BarService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetBar",
                            input_type="google.example.v1.GetBarRequest",
                            output_type="google.example.v1.GetBarResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        apis=["google.example.v1.FooService", "google.example.v1.BarService"],
        methods=["google.example.v1.FooService.GetFoo"],
    )
    opts = Options(service_yaml_config=service_yaml_config)

    api_schema = api.API.build(fd, "google.example.v1", opts=opts)

    assert "google.example.v1.Foo" in api_schema.messages
    assert "google.example.v1.GetFooRequest" in api_schema.messages
    assert "google.example.v1.GetFooResponse" in api_schema.messages

    # Bar is used by GetBarRequest (omitted), so Bar itself should be kept.
    assert "google.example.v1.Bar" in api_schema.messages
    assert "google.example.v1.GetBarRequest" not in api_schema.messages
    assert "google.example.v1.GetBarResponse" not in api_schema.messages

    assert "google.example.v1.FooService" in api_schema.services
    assert "google.example.v1.BarService" not in api_schema.services


def test_selective_gapic_api_build_remove_unnecessary_proto_files():
    fd = (
        make_file_pb2(
            name="foo_common.proto",
            package="google.example.v1.foo_common",
            messages=(make_message_pb2(name="Foo"),),
        ),
        make_file_pb2(
            name="bar_common.proto",
            package="google.example.v1.bar_common",
            messages=(make_message_pb2(name="Bar"),),
        ),
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Foo", fields=()),
                make_message_pb2(
                    name="GetFooRequest",
                    fields=(
                        make_field_pb2(
                            name="foo",
                            number=1,
                            type_name=".google.example.v1.foo_common.Foo",
                        ),
                    ),
                ),
                make_message_pb2(name="GetFooResponse", fields=()),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetFoo",
                            input_type="google.example.v1.GetFooRequest",
                            output_type="google.example.v1.GetFooResponse",
                        ),
                    ),
                ),
            ),
        ),
        make_file_pb2(
            name="bar.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Bar", fields=()),
                make_message_pb2(
                    name="GetBarRequest",
                    fields=(
                        make_field_pb2(
                            name="bar_local",
                            number=1,
                            type_name=".google.example.v1.Bar",
                        ),
                        make_field_pb2(
                            name="bar_common",
                            number=2,
                            type_name=".google.example.v1.bar_common.Bar",
                        ),
                    ),
                ),
                make_message_pb2(name="GetBarResponse", fields=()),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="BarService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetBar",
                            input_type="google.example.v1.GetBarRequest",
                            output_type="google.example.v1.GetBarResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        apis=["google.example.v1.FooService", "google.example.v1.BarService"],
        methods=["google.example.v1.FooService.GetFoo"],
    )
    opts = Options(service_yaml_config=service_yaml_config)

    api_schema = api.API.build(fd, "google.example.v1", opts=opts)

    assert "google.example.v1.foo_common.Foo" in api_schema.messages
    assert "google.example.v1.GetFooRequest" in api_schema.messages
    assert "google.example.v1.GetFooResponse" in api_schema.messages

    # Bar (in bar_common) is used by GetBarRequest (in bar.proto, omitted),
    # so Bar itself should be kept.
    assert "google.example.v1.bar_common.Bar" in api_schema.messages
    assert "google.example.v1.GetBarRequest" not in api_schema.messages
    assert "google.example.v1.GetBarResponse" not in api_schema.messages

    assert "google.example.v1.FooService" in api_schema.services
    assert "google.example.v1.BarService" not in api_schema.services

    assert "foo.proto" in api_schema.protos
    assert "foo_common.proto" in api_schema.protos
    # bar.proto is NOT omitted because it contains the kept Bar message
    # (even if the RPC that uses it is omitted).
    assert "bar.proto" in api_schema.protos
    assert "bar_common.proto" in api_schema.protos

    # Check that the sub-packages that have been completely pruned are excluded from generation,
    # but the ones that have only been partially pruned will still be appropriately included.
    assert "foo_common" in api_schema.subpackages
    sub = api_schema.subpackages["foo_common"]
    assert len(sub.protos) == 1
    assert "google.example.v1.foo_common.Foo" in sub.messages
    assert "bar_common" in api_schema.subpackages
    sub = api_schema.subpackages["bar_common"]
    assert len(sub.protos) == 1
    assert "google.example.v1.bar_common.Bar" in sub.messages


def test_selective_gapic_api_build_keep_messages_within_omitted_rpcs():
    fd = (
        make_file_pb2(
            name="foobar.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(
                    name="IncludedRequest",
                ),
                make_message_pb2(
                    name="IncludedResponse",
                ),
                make_message_pb2(
                    name="OmittedRequest",
                    fields=(
                        make_field_pb2(
                            name="nested",
                            number=1,
                            type_name=".google.example.v1.NestedMessage",
                        ),
                    ),
                ),
                make_message_pb2(
                    name="OmittedResponse",
                ),
                make_message_pb2(
                    name="NestedMessage",
                ),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="IncludedMethod",
                            input_type="google.example.v1.IncludedRequest",
                            output_type="google.example.v1.IncludedResponse",
                        ),
                        descriptor_pb2.MethodDescriptorProto(
                            name="OmittedMethod",
                            input_type="google.example.v1.OmittedRequest",
                            output_type="google.example.v1.OmittedResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        apis=["google.example.v1.FooService"],
        methods=["google.example.v1.FooService.IncludedMethod"],
    )
    opts = Options(service_yaml_config=service_yaml_config)

    api_schema = api.API.build(fd, "google.example.v1", opts=opts)

    # Included RPC and its messages should be present
    assert "google.example.v1.IncludedRequest" in api_schema.messages
    assert "google.example.v1.IncludedResponse" in api_schema.messages

    # Omitted RPC top-level messages should be ABSENT
    assert "google.example.v1.OmittedRequest" not in api_schema.messages
    assert "google.example.v1.OmittedResponse" not in api_schema.messages

    # Nested message ONLY reachable from omitted RPC should be PRESENT
    assert "google.example.v1.NestedMessage" in api_schema.messages


def test_selective_gapic_api_build_with_enums():
    fd = (
        make_file_pb2(
            name="foobar.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(
                    name="Foo",
                    fields=(
                        make_field_pb2(
                            name="status",
                            number=1,
                            type=14,
                            type_name=".google.example.v1.FooStatus",
                        ),
                    ),
                ),
                make_message_pb2(
                    name="Bar",
                    fields=(
                        make_field_pb2(
                            name="status",
                            number=1,
                            type=14,
                            type_name=".google.example.v1.BarStatus",
                        ),
                    ),
                ),
                make_message_pb2(
                    name="GetFooRequest",
                    fields=(
                        make_field_pb2(
                            name="foo", number=1, type_name=".google.example.v1.Foo"
                        ),
                    ),
                ),
                make_message_pb2(name="GetFooResponse", fields=()),
                make_message_pb2(
                    name="GetBarRequest",
                    fields=(
                        make_field_pb2(
                            name="bar", number=1, type_name=".google.example.v1.Bar"
                        ),
                    ),
                ),
                make_message_pb2(name="GetBarResponse", fields=()),
            ),
            enums=(
                make_enum_pb2("FooStatus", "YES", "NO"),
                make_enum_pb2("BarStatus", "YES", "NO"),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetFoo",
                            input_type="google.example.v1.GetFooRequest",
                            output_type="google.example.v1.GetFooResponse",
                        ),
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetBar",
                            input_type="google.example.v1.GetBarRequest",
                            output_type="google.example.v1.GetBarResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        apis=["google.example.v1.FooService"],
        methods=["google.example.v1.FooService.GetFoo"],
    )
    opts = Options(service_yaml_config=service_yaml_config)

    api_schema = api.API.build(fd, "google.example.v1", opts=opts)

    assert "google.example.v1.FooStatus" in api_schema.enums
    # BarStatus is reachable from Bar, which is used by GetBarRequest (omitted),
    # but Bar and its enums should be kept.
    assert "google.example.v1.BarStatus" in api_schema.enums
    assert "google.example.v1.FooStatus" in api_schema.top_level_enums
    assert "google.example.v1.BarStatus" in api_schema.top_level_enums


def test_selective_gapic_api_build_with_nested_fields():
    # Test that, when including or excluding messages for selective GAPIC generation,
    # any nested messages they may contain are included or excluded appropriately.
    fd = (
        make_file_pb2(
            name="foobar.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(
                    name="Foo",
                    nested_type=(
                        make_message_pb2(
                            name="Bar",
                            fields=(
                                make_field_pb2(
                                    name="baz",
                                    number=1,
                                    type_name=".google.example.v1.Baz",
                                ),
                            ),
                        ),
                    ),
                    enum_type=(make_enum_pb2("FooStatus", "YES", "NO"),),
                ),
                make_message_pb2(
                    name="Spam",
                    nested_type=(
                        make_message_pb2(
                            name="Ham",
                            fields=(
                                make_field_pb2(
                                    name="eggs",
                                    number=1,
                                    type_name=".google.example.v1.Eggs",
                                ),
                            ),
                        ),
                    ),
                    enum_type=(make_enum_pb2("SpamStatus", "YES", "NO"),),
                ),
                make_message_pb2(name="Baz"),
                make_message_pb2(name="Eggs"),
                make_message_pb2(
                    name="GetFooRequest",
                    fields=(
                        make_field_pb2(
                            name="foo", number=1, type_name=".google.example.v1.Foo"
                        ),
                    ),
                ),
                make_message_pb2(name="GetFooResponse", fields=()),
                make_message_pb2(
                    name="GetBarRequest",
                    fields=(
                        make_field_pb2(
                            name="spam", number=1, type_name=".google.example.v1.Spam"
                        ),
                    ),
                ),
                make_message_pb2(name="GetBarResponse", fields=()),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetFoo",
                            input_type="google.example.v1.GetFooRequest",
                            output_type="google.example.v1.GetFooResponse",
                        ),
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetBar",
                            input_type="google.example.v1.GetBarRequest",
                            output_type="google.example.v1.GetBarResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        apis=["google.example.v1.FooService"],
        methods=["google.example.v1.FooService.GetFoo"],
    )
    opts = Options(service_yaml_config=service_yaml_config)

    api_schema = api.API.build(fd, "google.example.v1", opts=opts)

    assert "google.example.v1.Baz" in api_schema.messages
    assert "google.example.v1.Foo.FooStatus" in api_schema.enums
    assert "google.example.v1.Foo.Bar" in api_schema.messages

    # Spam is used by GetBarRequest (omitted), so Spam and its nested types should be kept.
    assert "google.example.v1.Spam" in api_schema.messages
    assert "google.example.v1.Spam.SpamStatus" in api_schema.enums
    assert "google.example.v1.Spam.Ham" in api_schema.messages

    # Top-level request/response messages for omitted RPCs are still omitted.
    assert "google.example.v1.GetBarRequest" not in api_schema.messages
    assert "google.example.v1.GetBarResponse" not in api_schema.messages


@pytest.mark.parametrize("reference_attr", ["type", "child_type"])
def test_selective_gapic_api_build_with_resources(reference_attr):
    test_input_names = [
        ("foo.bar/Foo", "Foo", "FooDep", "GetFooRequest", "GetFooResponse"),
        ("foo.bar/Bar", "Bar", "BarDep", "GetBarRequest", "GetBarResponse"),
    ]

    messages = []

    for (
        resource_type,
        message_name,
        message_dep_name,
        request_message_name,
        response_message_name,
    ) in test_input_names:
        resource_message_dep = make_message_pb2(name=message_dep_name)

        # Make sure that we traverse down the fields in the referenced message type.
        resource_message = make_message_pb2(
            name=message_name,
            fields=(
                make_field_pb2(
                    name="dep",
                    number=1,
                    type_name=f".google.example.v1.{message_dep_name}",
                ),
            ),
        )
        request_message = make_message_pb2(
            name=request_message_name,
            fields=(make_field_pb2(name="thing", number=1, type=9),),
        )
        response_message = make_message_pb2(name=response_message_name)

        # Set up the resource
        resource_message_opts = resource_message.options.Extensions[
            resource_pb2.resource
        ]
        resource_message_opts.type = resource_type
        resource_message_opts.pattern.append("octopus/{octopus}/squid/{squid}")

        # Set up the reference
        request_message_thing_field_opts = request_message.field[0].options.Extensions[
            resource_pb2.resource_reference
        ]
        setattr(request_message_thing_field_opts, reference_attr, resource_type)

        # Add to messages
        messages.append(resource_message_dep)
        messages.append(resource_message)
        messages.append(request_message)
        messages.append(response_message)

    fds = (
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=messages,
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetFoo",
                            input_type="google.example.v1.GetFooRequest",
                            output_type="google.example.v1.GetFooResponse",
                        ),
                        descriptor_pb2.MethodDescriptorProto(
                            name="GetBar",
                            input_type="google.example.v1.GetBarRequest",
                            output_type="google.example.v1.GetBarResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        methods=["google.example.v1.FooService.GetFoo"]
    )
    opts = Options(service_yaml_config=service_yaml_config)

    api_schema = api.API.build(fds, package="google.example.v1", opts=opts)

    assert "google.example.v1.Foo" in api_schema.messages
    assert "google.example.v1.FooDep" in api_schema.messages
    assert "google.example.v1.GetFooRequest" in api_schema.messages
    assert "google.example.v1.GetFooResponse" in api_schema.messages

    # Bar and BarDep are reachable from GetBarRequest (omitted),
    # but they should be kept.
    assert "google.example.v1.Bar" in api_schema.messages
    assert "google.example.v1.BarDep" in api_schema.messages
    assert "google.example.v1.GetBarRequest" not in api_schema.messages
    assert "google.example.v1.GetBarResponse" not in api_schema.messages

    # Ensure we're also pruning resource messages for the files
    resource_messages = api_schema.protos["foo.proto"].resource_messages
    assert "foo.bar/Foo" in resource_messages
    # Bar is reachable via GetBarRequest, so it should be kept in resource_messages.
    assert "foo.bar/Bar" in resource_messages


def test_selective_gapic_api_build_extended_lro():
    def make_initiate_options(service_name):
        options = descriptor_pb2.MethodOptions()
        options.Extensions[ex_ops_pb2.operation_service] = service_name
        return options

    polling_method_options = descriptor_pb2.MethodOptions()
    polling_method_options.Extensions[ex_ops_pb2.operation_polling_method] = True

    T = descriptor_pb2.FieldDescriptorProto.Type
    operation_fields = tuple(
        make_field_pb2(name=name, type=T.Value("TYPE_STRING"), number=i)
        for i, name in enumerate(
            ("name", "status", "error_code", "error_message"), start=1
        )
    )
    for f in operation_fields:
        options = descriptor_pb2.FieldOptions()
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    fds = (
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="Operation", fields=operation_fields),
                make_message_pb2(name="CreateFooRequest"),
                make_message_pb2(name="GetFooOperationRequest"),
                make_message_pb2(name="CreateBarRequest"),
                make_message_pb2(name="GetBarOperationRequest"),
                make_message_pb2(name="PoorlyOrganizedMethodRequest"),
                make_message_pb2(name="PoorlyOrganizedMethodResponse"),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="FooOpsService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="Get",
                            input_type="google.example.v1.GetFooOperationRequest",
                            output_type="google.example.v1.Operation",
                            options=polling_method_options,
                        ),
                        descriptor_pb2.MethodDescriptorProto(
                            name="PoorlyOrganizedMethod",
                            input_type="google.example.v1.PoorlyOrganizedMethodRequest",
                            output_type="google.example.v1.PoorlyOrganizedMethodResponse",
                        ),
                    ),
                ),
                descriptor_pb2.ServiceDescriptorProto(
                    name="BarOpsService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="Get",
                            input_type="google.example.v1.GetBarOperationRequest",
                            output_type="google.example.v1.Operation",
                            options=polling_method_options,
                        ),
                    ),
                ),
                descriptor_pb2.ServiceDescriptorProto(
                    name="BasicService",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="CreateFoo",
                            input_type="google.example.v1.CreateFooRequest",
                            output_type="google.example.v1.Operation",
                            options=make_initiate_options("FooOpsService"),
                        ),
                        descriptor_pb2.MethodDescriptorProto(
                            name="CreateBar",
                            input_type="google.example.v1.CreateBarRequest",
                            output_type="google.example.v1.Operation",
                            options=make_initiate_options("BarOpsService"),
                        ),
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        apis=[
            "google.example.v1.FooOpsService",
            "google.example.v1.BarOpsService",
            "google.example.v1.BasicService",
        ],
        methods=[
            "google.example.v1.BasicService.CreateFoo",
        ],
    )
    opts = Options(service_yaml_config=service_yaml_config)

    api_schema = api.API.build(fds, "google.example.v1", opts=opts)

    assert "google.example.v1.BasicService" in api_schema.services
    assert "google.example.v1.FooOpsService" in api_schema.services
    assert "google.example.v1.FooOpsService.Get" in api_schema.all_methods
    assert "google.example.v1.Operation" in api_schema.messages
    assert "google.example.v1.CreateFooRequest" in api_schema.messages
    assert "google.example.v1.GetFooOperationRequest" in api_schema.messages

    assert "google.example.v1.BarOpsService" not in api_schema.services
    assert "google.example.v1.GetBarOperationRequest" not in api_schema.messages
    assert "google.example.v1.CreateBarRequest" not in api_schema.messages
    assert (
        "google.example.v1.FooOpsService.PoorlyOrganizedMethod"
        not in api_schema.all_methods
    )


def test_selective_gapic_api_build_generate_omitted_as_internal():
    # Put together a couple of minimal protos.
    fds = (
        make_file_pb2(
            name="foo.proto",
            package="google.example.v1",
            messages=(
                make_message_pb2(name="GenericRequest", fields=()),
                make_message_pb2(name="GenericResponse", fields=()),
            ),
            services=(
                descriptor_pb2.ServiceDescriptorProto(
                    name="ServiceOne",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="InternalMethod",
                            input_type="google.example.v1.GenericRequest",
                            output_type="google.example.v1.GenericResponse",
                        ),
                        descriptor_pb2.MethodDescriptorProto(
                            name="NonInternalMethod",
                            input_type="google.example.v1.GenericRequest",
                            output_type="google.example.v1.GenericResponse",
                        ),
                    ),
                ),
                descriptor_pb2.ServiceDescriptorProto(
                    name="ServiceTwo",
                    method=(
                        descriptor_pb2.MethodDescriptorProto(
                            name="NonInternalMethod",
                            input_type="google.example.v1.GenericRequest",
                            output_type="google.example.v1.GenericResponse",
                        ),
                    ),
                ),
            ),
        ),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        apis=["google.example.v1.ServiceOne", "google.example.v1.ServiceTwo"],
        methods=[
            "google.example.v1.ServiceOne.NonInternalMethod",
            "google.example.v1.ServiceTwo.NonInternalMethod",
        ],
        generate_omitted_as_internal=True,
    )

    opts = Options(service_yaml_config=service_yaml_config)

    api_schema = api.API.build(fds, "google.example.v1", opts=opts)

    assert "google.example.v1.ServiceOne" in api_schema.services
    assert "google.example.v1.ServiceTwo" in api_schema.services
    assert "google.example.v1.ServiceOne.InternalMethod" in api_schema.all_methods

    assert api_schema.services["google.example.v1.ServiceOne"].is_internal
    assert not api_schema.services["google.example.v1.ServiceTwo"].is_internal
    assert api_schema.all_methods[
        "google.example.v1.ServiceOne.InternalMethod"
    ].is_internal
    assert not api_schema.all_methods[
        "google.example.v1.ServiceOne.NonInternalMethod"
    ].is_internal
    assert not api_schema.all_methods[
        "google.example.v1.ServiceTwo.NonInternalMethod"
    ].is_internal

    assert (
        api_schema.services["google.example.v1.ServiceOne"].client_name
        == "BaseServiceOneClient"
    )
    assert (
        api_schema.services["google.example.v1.ServiceOne"].async_client_name
        == "BaseServiceOneAsyncClient"
    )
    assert (
        api_schema.all_methods[
            "google.example.v1.ServiceOne.InternalMethod"
        ].client_method_name
        == "_InternalMethod"
    )


def test_read_empty_python_settings_from_service_yaml():
    service_yaml_config = {
        "apis": [
            {"name": "google.example.v1beta1.ServiceOne.Example1"},
        ],
        "publishing": {
            "library_settings": [
                {
                    "version": "google.example.v1",
                    "python_settings": {
                        "experimental_features": {"rest_async_io_enabled": True},
                    },
                }
            ]
        },
    }
    cli_options = Options(service_yaml_config=service_yaml_config)
    fd = get_file_descriptor_proto_for_tests(fields=[])
    api_schema = api.API.build(fd, "google.example.v1beta1", opts=cli_options)
    assert (
        api_schema.all_library_settings[api_schema.naming.proto_package].python_settings
        == client_pb2.PythonSettings()
    )


def test_python_settings_duplicate_version_raises_error():
    """
    Test that `ClientLibrarySettingsError` is raised when there are duplicate versions in
    `client_pb2.ClientLibrarySettings`.
    """
    fd = get_file_descriptor_proto_for_tests()
    api_schema = api.API.build(fd, "google.example.v1beta1")
    clientlibrarysettings = [
        client_pb2.ClientLibrarySettings(
            version="google.example.v1beta1",
        ),
        client_pb2.ClientLibrarySettings(
            version="google.example.v1beta1",
        ),
    ]
    with pytest.raises(api.ClientLibrarySettingsError, match="(?i)duplicate version"):
        api_schema.enforce_valid_library_settings(clientlibrarysettings)


def test_read_method_settings_from_service_yaml():
    """
    Tests the `gapic.schema.api.all_method_settings` method which reads
    `MethodSettings` from the service config YAML.
    https://github.com/googleapis/googleapis/blob/7dab3de7ec79098bb367b6b2ac3815512a49dd56/google/api/client.proto#L325
    """
    service_yaml_config = {
        "apis": [
            {"name": "google.example.v1beta1.ServiceOne.Example1"},
        ],
        "publishing": {
            "method_settings": [
                {
                    "selector": "google.example.v1beta1.ServiceOne.Example1",
                    "auto_populated_fields": [
                        "squid",
                        "mollusc",
                    ],
                },
            ]
        },
    }
    cli_options = Options(service_yaml_config=service_yaml_config)
    field_options = descriptor_pb2.FieldOptions()
    field_options.Extensions[
        field_info_pb2.field_info
    ].format = field_info_pb2.FieldInfo.Format.Value("UUID4")

    squid = make_field_pb2(
        name="squid", type="TYPE_STRING", options=field_options, number=1
    )
    mollusc = make_field_pb2(
        name="mollusc", type="TYPE_STRING", options=field_options, number=2
    )
    fields = [squid, mollusc]
    fd = get_file_descriptor_proto_for_tests(fields=fields)
    api_schema = api.API.build(fd, "google.example.v1beta1", opts=cli_options)
    assert api_schema.all_method_settings == {
        "google.example.v1beta1.ServiceOne.Example1": client_pb2.MethodSettings(
            selector="google.example.v1beta1.ServiceOne.Example1",
            auto_populated_fields=["squid", "mollusc"],
            long_running=client_pb2.MethodSettings.LongRunning(),
        )
    }


def test_method_settings_duplicate_selector_raises_error():
    """
    Test that `MethodSettingsError` is raised when there are duplicate selectors in
    `client_pb2.MethodSettings`.
    """
    fd = get_file_descriptor_proto_for_tests()
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.ServiceOne.Example1",
        ),
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.ServiceOne.Example1",
        ),
    ]
    with pytest.raises(api.MethodSettingsError, match="(?i)duplicate selector"):
        api_schema.enforce_valid_method_settings(methodsettings)


def test_method_settings_invalid_selector_raises_error():
    """
    Test that `MethodSettingsError` when `client_pb2.MethodSettings.selector`
    cannot be mapped to a method in the API.
    """
    method_example1 = "google.example.v1beta1.DoesNotExist.Example1"
    method_example2 = "google.example.v1beta1.ServiceOne.DoesNotExist"

    fd = get_file_descriptor_proto_for_tests()
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector=method_example1,
        ),
        client_pb2.MethodSettings(
            selector=method_example2,
        ),
    ]

    with pytest.raises(api.MethodSettingsError) as ex:
        api_schema.enforce_valid_method_settings(methodsettings)

    error_yaml = yaml.safe_load(ex.value.args[0])

    assert re.match(".*not found.*", error_yaml[method_example1][0].lower())
    assert re.match(".*not found.*", error_yaml[method_example2][0].lower())


def test_method_settings_unsupported_auto_populated_field_type_raises_error():
    """
    Test that `MethodSettingsError` is raised when a field in
    `client_pb2.MethodSettings.auto_populated_fields` is not of type string.
    """
    squid = make_field_pb2(name="squid", type="TYPE_INT32", number=1)
    fd = get_file_descriptor_proto_for_tests(fields=[squid])
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.ServiceOne.Example1",
            auto_populated_fields=["squid"],
        ),
    ]
    with pytest.raises(api.MethodSettingsError, match="(?i)type string"):
        api_schema.enforce_valid_method_settings(methodsettings)


def test_method_settings_auto_populated_field_not_found_raises_error():
    """
    Test that `MethodSettingsError` is raised when a field in
    `client_pb2.MethodSettings.auto_populated_fields` is not found in the top-level
    request message of the selector.
    """
    fd = get_file_descriptor_proto_for_tests()
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.ServiceOne.Example1",
            auto_populated_fields=["whelk"],
        ),
    ]
    with pytest.raises(api.MethodSettingsError, match="(?i)not found"):
        api_schema.enforce_valid_method_settings(methodsettings)


def test_method_settings_auto_populated_nested_field_raises_error():
    """
    Test that `MethodSettingsError` is raised when a field in
    `client_pb2.MethodSettings.auto_populated_fields` is not found in the top-level
    request message of the selector. Instead, the field exists in a nested message.
    """

    octopus = make_field(
        name="octopus",
        type_name="google.example.v1beta1.NestedMessage",
        label=3,
        type="TYPE_MESSAGE",
    )

    fd = get_file_descriptor_proto_for_tests(fields=[octopus.field_pb])
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.ServiceOne.Example1",
            auto_populated_fields=["squid"],
        ),
    ]
    with pytest.raises(api.MethodSettingsError, match="(?i)not found"):
        api_schema.enforce_valid_method_settings(methodsettings)


def test_method_settings_auto_populated_field_client_streaming_rpc_raises_error():
    """
    Test that `MethodSettingsError` is raised when the selector in
    `client_pb2.MethodSettings.selector` maps to a method which uses client streaming.
    """
    fd = get_file_descriptor_proto_for_tests(client_streaming=True)
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.ServiceOne.Example1",
            auto_populated_fields=["squid"],
        ),
    ]
    with pytest.raises(api.MethodSettingsError, match="(?i)not a unary method"):
        api_schema.enforce_valid_method_settings(methodsettings)


def test_method_settings_auto_populated_field_server_streaming_rpc_raises_error():
    """
    Test that `MethodSettingsError` is raised when the selector in
    `client_pb2.MethodSettings.selector` maps to a method which uses server streaming.
    """
    fd = get_file_descriptor_proto_for_tests(server_streaming=True)
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.ServiceOne.Example1",
            auto_populated_fields=["squid"],
        ),
    ]
    with pytest.raises(api.MethodSettingsError, match="(?i)not a unary method"):
        api_schema.enforce_valid_method_settings(methodsettings)


def test_method_settings_unsupported_auto_populated_field_behavior_raises_error():
    """
    Test that `MethodSettingsError` is raised when a field in
    `client_pb2.MethodSettings.auto_populated_fields` is a required field.
    """
    field_options = descriptor_pb2.FieldOptions()
    field_options.Extensions[field_behavior_pb2.field_behavior].append(
        field_behavior_pb2.FieldBehavior.Value("REQUIRED")
    )
    squid = make_field_pb2(
        name="squid", type="TYPE_STRING", options=field_options, number=1
    )
    fd = get_file_descriptor_proto_for_tests(fields=[squid])
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.ServiceOne.Example1",
            auto_populated_fields=["squid"],
        ),
    ]
    with pytest.raises(api.MethodSettingsError, match="(?i)required field"):
        api_schema.enforce_valid_method_settings(methodsettings)


def test_method_settings_auto_populated_field_field_info_format_not_specified_raises_error():
    """
    Test that `MethodSettingsError` is raised when a field in
    `client_pb2.MethodSettings.auto_populated_fields` is not annotated with
    `google.api.field_info.format = UUID4`. For this test case,
    the format of the field is not specified.
    """
    squid = make_field_pb2(name="squid", type="TYPE_STRING", number=1)
    fd = get_file_descriptor_proto_for_tests(fields=[squid])
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.SomeExample.Example1",
            auto_populated_fields=["squid"],
        ),
    ]
    with pytest.raises(api.MethodSettingsError):
        api_schema.enforce_valid_method_settings(methodsettings)


def test_method_settings_unsupported_auto_populated_field_field_info_format_raises_error():
    """
    Test that `MethodSettingsError` is raised when a field in
    `client_pb2.MethodSettings.auto_populated_fields` is not annotated with
    `google.api.field_info.format = UUID4`.For this test case,
    the format of the field is `IPV4`.
    """
    field_options = descriptor_pb2.FieldOptions()
    field_options.Extensions[
        field_info_pb2.field_info
    ].format = field_info_pb2.FieldInfo.Format.Value("IPV4")
    squid = make_field_pb2(
        name="squid", type="TYPE_STRING", options=field_options, number=1
    )
    fd = get_file_descriptor_proto_for_tests(fields=[squid])
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector="google.example.v1beta1.SomeExample.Example1",
            auto_populated_fields=["squid"],
        ),
    ]
    with pytest.raises(api.MethodSettingsError):
        api_schema.enforce_valid_method_settings(methodsettings)


def test_method_settings_invalid_multiple_issues():
    """
    A kitchen sink type of test to ensure `MethodSettingsError` is raised and the contents
    of the exception includes sufficient detail describing each issue.
    """
    method_example1 = "google.example.v1beta1.ServiceTwo.Example1"
    method_example2 = "google.example.v1beta1.ServiceThree.Example2"
    field_options = descriptor_pb2.FieldOptions()

    # Field Squid Errors
    # - Not annotated with google.api.field_info.format = UUID4
    # - Not of type string
    # - Required field
    field_options.Extensions[
        field_info_pb2.field_info
    ].format = field_info_pb2.FieldInfo.Format.Value("IPV4")
    squid = make_field_pb2(
        name="squid", type="TYPE_INT32", options=field_options, number=1
    )
    field_options = descriptor_pb2.FieldOptions()
    field_options.Extensions[field_behavior_pb2.field_behavior].append(
        field_behavior_pb2.FieldBehavior.Value("REQUIRED")
    )

    # Field Octopus Errors
    # - Not annotated with google.api.field_info.format = UUID4
    octopus = make_field_pb2(name="octopus", type="TYPE_STRING", number=1)
    fd = get_file_descriptor_proto_for_tests(fields=[squid, octopus])
    api_schema = api.API.build(fd, "google.example.v1beta1")
    methodsettings = [
        client_pb2.MethodSettings(
            selector=method_example1,
            auto_populated_fields=[
                "squid",
                "octopus",
            ],
        ),
        client_pb2.MethodSettings(
            selector=method_example2,
            auto_populated_fields=["squid", "octopus"],
        ),
    ]
    with pytest.raises(api.MethodSettingsError) as ex:
        api_schema.enforce_valid_method_settings(methodsettings)

    error_yaml = yaml.safe_load(ex.value.args[0])

    assert re.match(".*squid.*not.*string.*", error_yaml[method_example1][0].lower())
    assert re.match(".*squid.*not.*uuid4.*", error_yaml[method_example1][1].lower())
    assert re.match(".*octopus.*not.*uuid4.*", error_yaml[method_example1][2].lower())
    assert re.match(".*method.*not found.*", error_yaml[method_example2][0].lower())


def test_file_level_resources_with_aliases():
    """Proves that CLI aliases are passed down to file-level CommonResources."""
    fdp = make_file_pb2(
        name="nomenclature.proto",
        package="nomenclature.linneaen.v1",
        messages=(
            make_message_pb2(
                name="CreateSpeciesRequest",
                fields=(make_field_pb2(name="species", number=1, type=9),),
            ),
        ),
    )
    res_pb2 = fdp.options.Extensions[resource_pb2.resource_definition]
    resource_definition = res_pb2.add()
    resource_definition.type = "nomenclature.linnaen.com/Species"
    resource_definition.pattern.append(
        "families/{family}/genera/{genus}/species/{species}"
    )

    # Pass down the resource-name-alias cli option
    opts = Options.build(
        "resource-name-alias=nomenclature.linnaen.com/Species:CustomSpecies"
    )

    api_schema = api.API.build([fdp], package="nomenclature.linneaen.v1", opts=opts)

    # Trigger the property that evaluates the CommonResource
    resource_msgs = api_schema.protos["nomenclature.proto"].resource_messages

    # Verify that the resource exists with the overriden type
    assert "nomenclature.linnaen.com/Species" in resource_msgs
    assert (
        resource_msgs["nomenclature.linnaen.com/Species"].resource_type
        == "CustomSpecies"
    )


from test_utils.test_utils import (
    make_file_pb2,
    make_message_pb2,
)


def test_proto_with_selective_generation_returns_none():
    # Proto A: will be omitted because its only method is not in the allow-list.
    fd_a = make_file_pb2(
        name="proto_a.proto",
        package="google.example.v1",
        services=(
            descriptor_pb2.ServiceDescriptorProto(
                name="ServiceA",
                method=(
                    descriptor_pb2.MethodDescriptorProto(
                        name="MethodA",
                        input_type="google.example.v1.ReqA",
                        output_type="google.example.v1.RespA",
                    ),
                ),
            ),
        ),
        messages=(
            make_message_pb2("ReqA"),
            make_message_pb2("RespA"),
        ),
    )

    # Proto B: will be kept because its method IS in the allow-list.
    fd_b = make_file_pb2(
        name="proto_b.proto",
        package="google.example.v1",
        services=(
            descriptor_pb2.ServiceDescriptorProto(
                name="ServiceB",
                method=(
                    descriptor_pb2.MethodDescriptorProto(
                        name="MethodB",
                        input_type="google.example.v1.ReqB",
                        output_type="google.example.v1.RespB",
                    ),
                ),
            ),
        ),
        messages=(
            make_message_pb2("ReqB"),
            make_message_pb2("RespB"),
        ),
    )

    # Selective generation only including ServiceB.MethodB.
    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        methods=["google.example.v1.ServiceB.MethodB"]
    )
    opts = Options(service_yaml_config=service_yaml_config)

    # Building the API will call with_selective_generation for both protos.
    api_schema = api.API.build([fd_a, fd_b], package="google.example.v1", opts=opts)

    # proto_a.proto should be excluded.
    assert "proto_a.proto" not in api_schema.protos
    assert "proto_b.proto" in api_schema.protos


def test_api_build_selective_multiple_protos_kept():
    fd1 = make_file_pb2(
        name="proto1.proto",
        package="google.example.v1",
        services=(
            descriptor_pb2.ServiceDescriptorProto(
                name="Service1",
                method=(
                    descriptor_pb2.MethodDescriptorProto(
                        name="Method1",
                        input_type="google.example.v1.Req1",
                        output_type="google.example.v1.Resp1",
                    ),
                ),
            ),
        ),
        messages=(make_message_pb2("Req1"), make_message_pb2("Resp1")),
    )
    fd2 = make_file_pb2(
        name="proto2.proto",
        package="google.example.v1",
        services=(
            descriptor_pb2.ServiceDescriptorProto(
                name="Service2",
                method=(
                    descriptor_pb2.MethodDescriptorProto(
                        name="Method2",
                        input_type="google.example.v1.Req2",
                        output_type="google.example.v1.Resp2",
                    ),
                ),
            ),
        ),
        messages=(make_message_pb2("Req2"), make_message_pb2("Resp2")),
    )

    service_yaml_config = get_service_yaml_for_selective_gapic_tests(
        methods=[
            "google.example.v1.Service1.Method1",
            "google.example.v1.Service2.Method2",
        ]
    )
    opts = Options(service_yaml_config=service_yaml_config)
    api_schema = api.API.build([fd1, fd2], package="google.example.v1", opts=opts)

    # Both protos should be kept. This covers the case where multiple protos
    # are processed in the selective generation loop, taking the 534->528 branch.
    assert len(api_schema.protos) == 2
    assert "proto1.proto" in api_schema.protos
    assert "proto2.proto" in api_schema.protos
    assert not api_schema.has_resumable_upload_methods


def test_api_has_resumable_upload_methods():
    # Verify that an API containing a recognized resumable upload method
    # reports has_resumable_upload_methods as True.
    # Note: In MethodDescriptorProto, output_type is the protobuf RPC response
    # message defined in the .proto file (e.g. UploadResponse).
    fd = make_file_pb2(
        name="upload.proto",
        package="google.example.v1",
        services=(
            descriptor_pb2.ServiceDescriptorProto(
                name="UploadService",
                method=(
                    descriptor_pb2.MethodDescriptorProto(
                        name="UploadMedia",
                        input_type="google.example.v1.UploadRequest",
                        output_type="google.example.v1.UploadResponse",
                    ),
                ),
            ),
        ),
        messages=(
            make_message_pb2("UploadRequest"),
            make_message_pb2("UploadResponse"),
        ),
    )
    api_schema = api.API.build([fd], package="google.example.v1")
    assert api_schema.has_resumable_upload_methods
