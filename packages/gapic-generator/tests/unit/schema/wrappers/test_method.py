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
import dataclasses
import json
import pytest
from typing import Sequence

from google.api import field_behavior_pb2
from google.api import http_pb2
from google.api import routing_pb2
from google.cloud import extended_operations_pb2 as ex_ops_pb2
from google.protobuf import descriptor_pb2
from google.protobuf import wrappers_pb2

from gapic.schema import metadata
from gapic.schema import wrappers

from test_utils.test_utils import (
    make_enum,
    make_field,
    make_message,
    make_method,
)


def test_method_types():
    input_msg = make_message(name="Input", module="baz")
    output_msg = make_message(name="Output", module="baz")
    method = make_method(
        "DoSomething", input_msg, output_msg, package="foo.bar", module="bacon"
    )
    assert method.name == "DoSomething"
    assert method.input.name == "Input"
    assert method.output.name == "Output"


def test_method_void():
    empty = make_message(name="Empty", package="google.protobuf")
    method = make_method("Meh", output_message=empty)
    assert method.void


def test_method_not_void():
    not_empty = make_message(name="OutputMessage", package="foo.bar.v1")
    method = make_method("Meh", output_message=not_empty)
    assert not method.void


def test_method_deprecated():
    method = make_method("DeprecatedMethod", is_deprecated=True)
    assert method.is_deprecated


def test_method_client_output():
    output = make_message(name="Input", module="baz")
    method = make_method("DoStuff", output_message=output)
    assert method.client_output is method.output


def test_method_client_output_empty():
    empty = make_message(name="Empty", package="google.protobuf")
    method = make_method("Meh", output_message=empty)
    assert method.client_output == wrappers.PrimitiveType.build(None)


def test_method_client_output_paged():
    paged = make_field(name="foos", message=make_message("Foo"), repeated=True)
    parent = make_field(name="parent", type=9)  # str
    page_size = make_field(name="page_size", type=5)  # int
    page_token = make_field(name="page_token", type=9)  # str

    input_msg = make_message(
        name="ListFoosRequest",
        fields=(
            parent,
            page_size,
            page_token,
        ),
    )
    output_msg = make_message(
        name="ListFoosResponse",
        fields=(
            paged,
            make_field(name="next_page_token", type=9),  # str
        ),
    )
    method = make_method(
        "ListFoos",
        input_message=input_msg,
        output_message=output_msg,
    )
    assert method.paged_result_field == paged
    assert method.client_output.ident.name == "ListFoosPager"

    max_results = make_field(name="max_results", type=5)  # int
    input_msg = make_message(
        name="ListFoosRequest",
        fields=(
            parent,
            max_results,
            page_token,
        ),
    )
    method = make_method(
        "ListFoos",
        input_message=input_msg,
        output_message=output_msg,
    )
    assert method.paged_result_field == paged
    assert method.client_output.ident.name == "ListFoosPager"


def test_method_client_output_async_empty():
    empty = make_message(name="Empty", package="google.protobuf")
    method = make_method("Meh", output_message=empty)
    assert method.client_output_async == wrappers.PrimitiveType.build(None)


def test_method_paged_result_field_not_first():
    paged = make_field(name="foos", message=make_message("Foo"), repeated=True)
    input_msg = make_message(
        name="ListFoosRequest",
        fields=(
            make_field(name="parent", type=9),  # str
            make_field(name="page_size", type=5),  # int
            make_field(name="page_token", type=9),  # str
        ),
    )
    output_msg = make_message(
        name="ListFoosResponse",
        fields=(
            make_field(name="next_page_token", type=9),  # str
            paged,
        ),
    )
    method = make_method(
        "ListFoos",
        input_message=input_msg,
        output_message=output_msg,
    )
    assert method.paged_result_field == paged


def test_method_paged_result_field_no_page_field():
    input_msg = make_message(
        name="ListFoosRequest",
        fields=(
            make_field(name="parent", type=9),  # str
            make_field(name="page_size", type=5),  # int
            make_field(name="page_token", type=9),  # str
        ),
    )
    output_msg = make_message(
        name="ListFoosResponse",
        fields=(
            make_field(name="foos", message=make_message("Foo"), repeated=False),
            make_field(name="next_page_token", type=9),  # str
        ),
    )
    method = make_method(
        "ListFoos",
        input_message=input_msg,
        output_message=output_msg,
    )
    assert method.paged_result_field is None

    method = make_method(
        name="Foo",
        input_message=make_message(
            name="FooRequest",
            fields=(make_field(name="page_token", type=9),),  # str
        ),
        output_message=make_message(
            name="FooResponse",
            fields=(make_field(name="next_page_token", type=9),),  # str
        ),
    )
    assert method.paged_result_field is None


def test_method_paged_result_field_invalid_wrapper_type():
    """Validate paged_result_field() returns None if page_size/max_results wrappertypes
    are not allowed types.
    """

    # page_size is not allowed wrappertype
    parent = make_field(name="parent", type="TYPE_STRING")
    page_size = make_field(name="page_size", type="TYPE_DOUBLE")  # not an allowed type
    page_token = make_field(name="page_token", type="TYPE_STRING")
    foos = make_field(name="foos", message=make_message("Foo"), repeated=True)
    next_page_token = make_field(name="next_page_token", type="TYPE_STRING")

    input_msg = make_message(
        name="ListFoosRequest",
        fields=(
            parent,
            page_size,
            page_token,
        ),
    )
    output_msg = make_message(
        name="ListFoosResponse",
        fields=(
            foos,
            next_page_token,
        ),
    )
    method = make_method(
        "ListFoos",
        input_message=input_msg,
        output_message=output_msg,
    )
    assert method.paged_result_field is None

    # max_results is not allowed wrappertype
    max_results = make_field(
        name="max_results", type="TYPE_STRING"
    )  # not an allowed type

    input_msg = make_message(
        name="ListFoosRequest",
        fields=(
            parent,
            max_results,
            page_token,
        ),
    )

    method = make_method(
        "ListFoos",
        input_message=input_msg,
        output_message=output_msg,
    )

    assert method.paged_result_field is None


def test_method_paged_result_ref_types():
    input_msg = make_message(
        name="ListSquidsRequest",
        fields=(
            make_field(name="parent", type=9),  # str
            make_field(name="page_size", type=5),  # int
            make_field(name="page_token", type=9),  # str
        ),
        module="squid",
    )
    mollusc_msg = make_message("Mollusc", module="mollusc")
    output_msg = make_message(
        name="ListMolluscsResponse",
        fields=(
            make_field(name="molluscs", message=mollusc_msg, repeated=True),
            make_field(name="next_page_token", type=9),  # str
        ),
        module="mollusc",
    )
    method = make_method(
        "ListSquids", input_message=input_msg, output_message=output_msg, module="squid"
    )

    ref_type_names = {t.name for t in method.ref_types}
    assert ref_type_names == {
        "ListSquidsRequest",
        "ListSquidsPager",
        "ListSquidsAsyncPager",
        "Mollusc",
    }


def test_flattened_ref_types():
    method = make_method(
        "IdentifyMollusc",
        input_message=make_message(
            "IdentifyMolluscRequest",
            fields=(
                make_field(
                    "cephalopod",
                    message=make_message(
                        "Cephalopod",
                        fields=(
                            make_field("mass_kg", type="TYPE_INT32"),
                            make_field(
                                "squid",
                                number=2,
                                message=make_message("Squid"),
                            ),
                            make_field(
                                "clam",
                                number=3,
                                message=make_message("Clam"),
                            ),
                        ),
                    ),
                ),
                make_field(
                    "stratum",
                    enum=make_enum(
                        "Stratum",
                    ),
                ),
            ),
        ),
        signatures=("cephalopod.squid,stratum",),
        output_message=make_message("Mollusc"),
    )

    expected_flat_ref_type_names = {
        "IdentifyMolluscRequest",
        "Squid",
        "Stratum",
        "Mollusc",
    }
    actual_flat_ref_type_names = {t.name for t in method.flat_ref_types}
    assert expected_flat_ref_type_names == actual_flat_ref_type_names


def test_method_paged_result_primitive():
    paged = make_field(name="squids", type=9, repeated=True)  # str
    input_msg = make_message(
        name="ListSquidsRequest",
        fields=(
            make_field(name="parent", type=9),  # str
            make_field(name="page_size", type=5),  # int
            make_field(name="page_token", type=9),  # str
        ),
    )
    output_msg = make_message(
        name="ListFoosResponse",
        fields=(
            paged,
            make_field(name="next_page_token", type=9),  # str
        ),
    )
    method = make_method(
        "ListSquids",
        input_message=input_msg,
        output_message=output_msg,
    )
    assert method.paged_result_field == paged
    assert method.client_output.ident.name == "ListSquidsPager"


def test_method_field_headers_none():
    method = make_method("DoSomething")
    assert isinstance(method.field_headers, collections.abc.Sequence)


def test_method_field_headers_present():
    verbs = [
        "get",
        "put",
        "post",
        "delete",
        "patch",
    ]

    for v in verbs:
        rule = http_pb2.HttpRule(**{v: "/v1/{parent=projects/*}/topics"})
        method = make_method("DoSomething", http_rule=rule)
        assert method.field_headers == (wrappers.FieldHeader("parent"),)
        assert method.field_headers[0].raw == "parent"
        assert method.field_headers[0].disambiguated == "parent"

        # test that reserved keyword in field header is disambiguated
        rule = http_pb2.HttpRule(**{v: "/v1/{object=objects/*}/topics"})
        method = make_method("DoSomething", http_rule=rule)
        assert method.field_headers == (wrappers.FieldHeader("object"),)
        assert method.field_headers[0].raw == "object"
        assert method.field_headers[0].disambiguated == "object_"

        # test w/o equal sign
        rule = http_pb2.HttpRule(**{v: "/v1/{parent}/topics"})
        method = make_method("DoSomething", http_rule=rule)
        assert method.field_headers == (wrappers.FieldHeader("parent"),)
        assert method.field_headers[0].raw == "parent"
        assert method.field_headers[0].disambiguated == "parent"


def test_method_routing_rule():
    routing_rule = routing_pb2.RoutingRule()
    param = routing_rule.routing_parameters.add()
    param.field = "table_name"
    param.path_template = "projects/*/{table_location=instances/*}/tables/*"
    method = make_method("DoSomething", routing_rule=routing_rule)
    assert method.explicit_routing
    assert method.routing_rule.routing_parameters == [
        wrappers.RoutingParameter(x.field, x.path_template)
        for x in routing_rule.routing_parameters
    ]
    assert method.routing_rule.routing_parameters[0].sample_request is not None


def test_method_routing_rule_empty_routing_parameters():
    routing_rule = routing_pb2.RoutingRule()
    method = make_method("DoSomething", routing_rule=routing_rule)
    assert method.routing_rule is None


def test_method_routing_rule_not_set():
    method = make_method("DoSomething")
    assert method.routing_rule is None


def test_method_http_opt():
    http_rule = http_pb2.HttpRule(post="/v1/{parent=projects/*}/topics", body="*")
    method = make_method("DoSomething", http_rule=http_rule)
    assert method.http_opt == {
        "verb": "post",
        "url": "/v1/{parent=projects/*}/topics",
        "body": "*",
    }


# TODO(yon-mg) to test:  grpc transcoding,
#                       correct handling of path/query params
#                       correct handling of body & additional binding


def test_method_http_opt_no_body():
    http_rule = http_pb2.HttpRule(post="/v1/{parent=projects/*}/topics")
    method = make_method("DoSomething", http_rule=http_rule)
    assert method.http_opt == {"verb": "post", "url": "/v1/{parent=projects/*}/topics"}


def test_method_http_opt_no_http_rule():
    method = make_method("DoSomething")
    assert method.http_opt == None


def test_method_path_params():
    # tests only the basic case of grpc transcoding
    http_rule = http_pb2.HttpRule(post="/v1/{project}/topics")
    method = make_method("DoSomething", http_rule=http_rule)
    assert method.path_params == ["project"]

    http_rule2 = http_pb2.HttpRule(post="/v1beta1/{name=rooms/*/blurbs/*}")
    method2 = make_method("DoSomething", http_rule=http_rule2)
    assert method2.path_params == ["name"]


def test_method_path_params_no_http_rule():
    method = make_method("DoSomething")
    assert method.path_params == []


def test_body_fields():
    http_rule = http_pb2.HttpRule(post="/v1/{arms_shape=arms/*}/squids", body="mantle")

    mantle_stuff = make_field(name="mantle_stuff", type=9)
    message = make_message("Mantle", fields=(mantle_stuff,))
    mantle = make_field("mantle", type=11, type_name="Mantle", message=message)
    arms_shape = make_field("arms_shape", type=9)
    input_message = make_message("Squid", fields=(mantle, arms_shape))
    method = make_method("PutSquid", input_message=input_message, http_rule=http_rule)
    assert set(method.body_fields) == {"mantle"}
    mock_value = method.body_fields["mantle"].mock_value
    assert mock_value == "baz.Mantle(mantle_stuff='mantle_stuff_value')"


def test_body_fields_no_body():
    http_rule = http_pb2.HttpRule(
        post="/v1/{arms_shape=arms/*}/squids",
    )

    method = make_method("PutSquid", http_rule=http_rule)

    assert not method.body_fields


def test_method_http_options():
    verbs = ["get", "put", "post", "delete", "patch"]
    for v in verbs:
        http_rule = http_pb2.HttpRule(**{v: "/v1/{parent=projects/*}/topics"})
        method = make_method("DoSomething", http_rule=http_rule)
        assert [dataclasses.asdict(http) for http in method.http_options] == [
            {"method": v, "uri": "/v1/{parent=projects/*}/topics", "body": None}
        ]


def test_method_http_options_empty_http_rule():
    http_rule = http_pb2.HttpRule()
    method = make_method("DoSomething", http_rule=http_rule)
    assert method.http_options == []

    http_rule = http_pb2.HttpRule(get="")
    method = make_method("DoSomething", http_rule=http_rule)
    assert method.http_options == []


def test_method_http_options_no_http_rule():
    method = make_method("DoSomething")
    assert method.path_params == []


def test_method_http_options_body_star():
    http_rule = http_pb2.HttpRule(post="/v1/{parent=projects/*}/topics", body="*")
    method = make_method("DoSomething", http_rule=http_rule)
    assert [dataclasses.asdict(http) for http in method.http_options] == [
        {"method": "post", "uri": "/v1/{parent=projects/*}/topics", "body": "*"}
    ]


def test_method_http_options_body_field():
    http_rule = http_pb2.HttpRule(
        post="/v1/{parent=projects/*}/topics", body="body_field"
    )
    method = make_method("DoSomething", http_rule=http_rule)
    assert [dataclasses.asdict(http) for http in method.http_options] == [
        {
            "method": "post",
            "uri": "/v1/{parent=projects/*}/topics",
            "body": "body_field",
        }
    ]


def test_method_http_options_additional_bindings():
    http_rule = http_pb2.HttpRule(
        post="/v1/{parent=projects/*}/topics",
        body="*",
        additional_bindings=[
            http_pb2.HttpRule(
                post="/v1/{parent=projects/*/regions/*}/topics",
                body="*",
            ),
            http_pb2.HttpRule(
                post="/v1/projects/p1/topics",
                body="body_field",
            ),
        ],
    )
    method = make_method("DoSomething", http_rule=http_rule)
    assert [dataclasses.asdict(http) for http in method.http_options] == [
        {"method": "post", "uri": "/v1/{parent=projects/*}/topics", "body": "*"},
        {
            "method": "post",
            "uri": "/v1/{parent=projects/*/regions/*}/topics",
            "body": "*",
        },
        {"method": "post", "uri": "/v1/projects/p1/topics", "body": "body_field"},
    ]


def test_method_http_options_reserved_name_in_url():
    http_rule = http_pb2.HttpRule(post="/v1/license/{license=lic/*}", body="*")
    method = make_method("DoSomething", http_rule=http_rule)
    assert [dataclasses.asdict(http) for http in method.http_options] == [
        {"method": "post", "uri": "/v1/license/{license_=lic/*}", "body": "*"}
    ]


def test_method_http_options_reserved_name_in_body():
    http_rule = http_pb2.HttpRule(post="/v1/license/{license=lic/*}", body="breakpoint")
    method = make_method("DoSomething", http_rule=http_rule)
    assert [dataclasses.asdict(http) for http in method.http_options] == [
        {"method": "post", "uri": "/v1/license/{license_=lic/*}", "body": "breakpoint_"}
    ]


def test_method_http_options_generate_sample():
    http_rule = http_pb2.HttpRule(
        get="/v1/{resource.id=projects/*/regions/*/id/**}/stuff",
    )

    method = make_method(
        "DoSomething",
        make_message(
            name="Input",
            fields=[
                make_field(
                    name="resource",
                    number=1,
                    type=11,
                    message=make_message(
                        "Resource",
                        fields=[
                            make_field(name="id", type=9),
                        ],
                    ),
                ),
            ],
        ),
        http_rule=http_rule,
    )
    sample = method.http_options[0].sample_request(method)
    assert sample == {"resource": {"id": "projects/sample1/regions/sample2/id/sample3"}}


def test_method_http_options_generate_sample_implicit_template():
    http_rule = http_pb2.HttpRule(
        get="/v1/{resource.id}/stuff",
    )
    method = make_method(
        "DoSomething",
        make_message(
            name="Input",
            fields=[
                make_field(
                    name="resource",
                    number=1,
                    message=make_message(
                        "Resource",
                        fields=[
                            make_field(name="id", type=9),
                        ],
                    ),
                ),
            ],
        ),
        http_rule=http_rule,
    )

    sample = method.http_options[0].sample_request(method)
    assert sample == {"resource": {"id": "sample1"}}


def test_method_query_params():
    # tests only the basic case of grpc transcoding
    http_rule = http_pb2.HttpRule(post="/v1/{project}/topics", body="address")
    input_message = make_message(
        "MethodInput",
        fields=(make_field("region"), make_field("project"), make_field("address")),
    )
    method = make_method(
        "DoSomething", http_rule=http_rule, input_message=input_message
    )
    assert method.query_params == {"region"}


def test_method_query_params_no_body():
    # tests only the basic case of grpc transcoding
    http_rule = http_pb2.HttpRule(post="/v1/{project}/topics")
    input_message = make_message(
        "MethodInput",
        fields=(
            make_field("region"),
            make_field("project"),
        ),
    )
    method = make_method(
        "DoSomething", http_rule=http_rule, input_message=input_message
    )
    assert method.query_params == {"region"}


def test_method_query_params_star_body():
    # tests only the basic case of grpc transcoding
    http_rule = http_pb2.HttpRule(post="/v1/{project}/topics", body="*")
    input_message = make_message(
        "MethodInput",
        fields=(make_field("region"), make_field("project"), make_field("address")),
    )
    method = make_method(
        "DoSomething", http_rule=http_rule, input_message=input_message
    )
    assert method.query_params == set()


def test_method_query_params_no_http_rule():
    method = make_method("DoSomething")
    assert method.query_params == set()


def test_method_idempotent_yes():
    http_rule = http_pb2.HttpRule(get="/v1/{parent=projects/*}/topics")
    method = make_method("DoSomething", http_rule=http_rule)
    assert method.idempotent is True


def test_method_idempotent_no():
    http_rule = http_pb2.HttpRule(post="/v1/{parent=projects/*}/topics")
    method = make_method("DoSomething", http_rule=http_rule)
    assert method.idempotent is False


def test_method_idempotent_no_http_rule():
    method = make_method("DoSomething")
    assert method.idempotent is False


def test_method_unary_unary():
    method = make_method("F", client_streaming=False, server_streaming=False)
    assert method.grpc_stub_type == "unary_unary"


def test_method_unary_stream():
    method = make_method("F", client_streaming=False, server_streaming=True)
    assert method.grpc_stub_type == "unary_stream"


def test_method_stream_unary():
    method = make_method("F", client_streaming=True, server_streaming=False)
    assert method.grpc_stub_type == "stream_unary"


def test_method_stream_stream():
    method = make_method("F", client_streaming=True, server_streaming=True)
    assert method.grpc_stub_type == "stream_stream"


def test_method_flattened_fields():
    a = make_field("a", type=5)  # int
    b = make_field("b", type=5)
    input_msg = make_message("Z", fields=(a, b))
    method = make_method("F", input_message=input_msg, signatures=("a,b",))
    assert len(method.flattened_fields) == 2
    assert "a" in method.flattened_fields
    assert "b" in method.flattened_fields


def test_method_flattened_fields_empty_sig():
    a = make_field("a", type=5)  # int
    b = make_field("b", type=5)
    input_msg = make_message("Z", fields=(a, b))
    method = make_method("F", input_message=input_msg, signatures=("",))
    assert len(method.flattened_fields) == 0


def test_method_flattened_fields_different_package_non_primitive():
    # This test verifies that method flattening handles a special case where:
    # * the method's request message type lives in a different package and
    # * a field in the method_signature is a non-primitive.
    #
    # If the message is defined in a different package it is not guaranteed to
    # be a proto-plus wrapped type, which puts restrictions on assigning
    # directly to its fields, which complicates request construction.
    # The easiest solution in this case is to just prohibit these fields
    # in the method flattening.
    message = make_message("Mantle", package="mollusc.cephalopod.v1", module="squid")
    mantle = make_field(
        "mantle", type=11, type_name="Mantle", message=message, meta=message.meta
    )
    arms_count = make_field("arms_count", type=5, meta=message.meta)
    input_message = make_message(
        "Squid",
        fields=(mantle, arms_count),
        package=".".join(message.meta.address.package),
        module=message.meta.address.module,
    )
    method = make_method(
        "PutSquid",
        input_message=input_message,
        package="remote.package.v1",
        module="module",
        signatures=("mantle,arms_count",),
    )
    assert set(method.flattened_fields) == {"arms_count"}


def test_method_include_flattened_message_fields():
    a = make_field("a", type=5)
    b = make_field("b", type=11, type_name="Eggs", message=make_message("Eggs"))
    input_msg = make_message("Z", fields=(a, b))
    method = make_method("F", input_message=input_msg, signatures=("a,b",))
    assert len(method.flattened_fields) == 2


def test_method_legacy_flattened_fields():
    required_options = descriptor_pb2.FieldOptions()
    required_options.Extensions[field_behavior_pb2.field_behavior].append(
        field_behavior_pb2.FieldBehavior.Value("REQUIRED")
    )

    # Cephalopods are required.
    squid = make_field(name="squid", options=required_options)
    octopus = make_field(
        name="octopus",
        message=make_message(
            name="Octopus", fields=[make_field(name="mass", options=required_options)]
        ),
        options=required_options,
    )

    # Bivalves are optional.
    clam = make_field(name="clam")
    oyster = make_field(
        name="oyster",
        message=make_message(name="Oyster", fields=[make_field(name="has_pearl")]),
    )

    # Interleave required and optional fields to make sure
    # that, in the legacy flattening, required fields are always first.
    request = make_message("request", fields=[squid, clam, octopus, oyster])

    method = make_method(
        name="CreateMolluscs",
        input_message=request,
        # Signatures should be ignored.
        signatures=["squid,octopus.mass", "squid,octopus,oyster.has_pearl"],
    )

    # Use an ordered dict because ordering is important:
    # required fields should come first.
    expected = collections.OrderedDict(
        [("squid", squid), ("octopus", octopus), ("clam", clam), ("oyster", oyster)]
    )

    assert method.legacy_flattened_fields == expected


def test_flattened_oneof_fields():
    mass_kg = make_field(name="mass_kg", oneof="mass", type=5)
    mass_lbs = make_field(name="mass_lbs", oneof="mass", type=5)

    length_m = make_field(name="length_m", oneof="length", type=5)
    length_f = make_field(name="length_f", oneof="length", type=5)

    color = make_field(name="color", type=5)
    mantle = make_field(
        name="mantle",
        message=make_message(
            name="Mantle",
            fields=(
                make_field(name="color", type=5),
                mass_kg,
                mass_lbs,
            ),
        ),
    )
    request = make_message(
        name="CreateMolluscRequest",
        fields=(
            length_m,
            length_f,
            color,
            mantle,
        ),
    )
    method = make_method(
        name="CreateMollusc",
        input_message=request,
        signatures=[
            "length_m,",
            "length_f,",
            "mantle.mass_kg,",
            "mantle.mass_lbs,",
            "color",
        ],
    )

    expected = {"mass": [mass_kg, mass_lbs], "length": [length_m, length_f]}
    actual = method.flattened_oneof_fields()
    assert expected == actual

    # Check this method too because the setup is a lot of work.
    expected = {
        "color": "color",
        "length_m": "length_m",
        "length_f": "length_f",
        "mass_kg": "mantle.mass_kg",
        "mass_lbs": "mantle.mass_lbs",
    }
    actual = method.flattened_field_to_key
    assert expected == actual


def test_is_operation_polling_method():
    T = descriptor_pb2.FieldDescriptorProto.Type

    operation = make_message(
        name="Operation",
        fields=[
            make_field(name=name, type=T.Value("TYPE_STRING"), number=i)
            for i, name in enumerate(
                ("name", "status", "error_code", "error_message"), start=1
            )
        ],
    )
    for f in operation.fields.values():
        options = descriptor_pb2.FieldOptions()
        # Note: The field numbers were carefully chosen to be the corresponding enum values.
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    request = make_message(
        name="GetOperation",
        fields=[make_field(name="name", type=T.Value("TYPE_STRING"), number=1)],
    )

    # Correct positive
    options = descriptor_pb2.MethodOptions()
    options.Extensions[ex_ops_pb2.operation_polling_method] = True
    polling_method = make_method(
        name="Get",
        input_message=request,
        output_message=operation,
        options=options,
    )

    assert polling_method.is_operation_polling_method

    # Normal method that returns operation
    normal_method = make_method(
        name="Get",
        input_message=request,
        output_message=operation,
    )

    assert not normal_method.is_operation_polling_method

    # Method with invalid options combination
    response = make_message(name="Response", fields=[make_field(name="name")])

    invalid_method = make_method(
        name="Get",
        input_message=request,
        output_message=response,
        options=options,  # Reuse options from the actual polling method
    )

    assert not invalid_method.is_operation_polling_method


@pytest.mark.parametrize(
    "all_field_names,canonical_name_to_field_name",
    [
        [
            [
                "name",
                "status",
                "error_code",
                "error_message",
            ],
            {},
        ],
        [
            [
                "moniker",
                "done_ness",
                "errno",
                "warning",
            ],
            {
                "name": "moniker",
                "status": "done_ness",
                "error_code": "errno",
                "error_message": "warning",
            },
        ],
        [
            [
                "name",
                "status",
                "http_error_code",
                "http_error_message",
            ],
            {
                "error_code": "http_error_code",
                "error_message": "http_error_message",
            },
        ],
        # No fields means this cannot be an extended operation.
        [[], None],
    ],
)
def test_differently_named_extended_operation_fields(
    all_field_names,
    canonical_name_to_field_name,
):
    T = descriptor_pb2.FieldDescriptorProto.Type
    operation = make_message(
        name="Operation",
        fields=[
            make_field(
                name=name.lower(),
                type=T.Value("TYPE_STRING"),
                number=i,
            )
            for i, name in enumerate(all_field_names, start=1)
        ],
    )
    for f in operation.fields.values():
        options = descriptor_pb2.FieldOptions()
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    expected = (
        {k: operation.fields[v] for k, v in canonical_name_to_field_name.items()}
        if canonical_name_to_field_name is not None
        else None
    )
    actual = operation.differently_named_extended_operation_fields

    assert expected == actual


def test_transport_safe_name():
    unsafe_methods = {
        name: make_method(name=name)
        for name in [
            "CreateChannel",
            "GrpcChannel",
            "OperationsClient",
            "import",
            "Import",
            "Raise",
        ]
    }

    safe_methods = {name: make_method(name=name) for name in ["Call", "Put", "Hold"]}

    for name, method in safe_methods.items():
        assert method.transport_safe_name == name

    for name, method in unsafe_methods.items():
        assert method.transport_safe_name == f"{name}_"


def test_client_method_name():
    unsafe_methods = {
        name: make_method(name=name) for name in ["import", "Import", "Raise"]
    }

    safe_methods = {name: make_method(name=name) for name in ["Call", "Put", "Hold"]}

    internal_unsafe_methods = {
        k: dataclasses.replace(v, is_internal=True) for k, v in unsafe_methods.items()
    }

    internal_safe_methods = {
        k: dataclasses.replace(v, is_internal=True) for k, v in safe_methods.items()
    }

    for name, method in safe_methods.items():
        assert method.client_method_name == name

    for name, method in unsafe_methods.items():
        assert method.client_method_name == f"{name}_"

    for name, method in internal_safe_methods.items():
        assert method.client_method_name == f"_{name}"

    for name, method in internal_unsafe_methods.items():
        assert method.client_method_name == f"_{name}_"


def test_mixin_rule():
    m = wrappers.MixinHttpRule("get", "/v1beta1/{name=projects/*}/locations", None)
    e = {"name": "projects/sample1"}
    assert e == m.sample_request

    m = wrappers.MixinHttpRule("get", "/v1beta1/{name=projects/*}/locations", "city")
    e = {
        "name": "projects/sample1",
        "city": {},
    }
    assert e == m.sample_request


@pytest.mark.parametrize(
    "field_type, pb_type, expected",
    [
        # valid paged_result_field candidates
        (int, "TYPE_INT32", True),
        (wrappers_pb2.UInt32Value, "TYPE_MESSAGE", True),
        (wrappers_pb2.Int32Value, "TYPE_MESSAGE", True),
        # invalid paged_result_field candidates
        (float, "TYPE_DOUBLE", False),
        (wrappers_pb2.UInt32Value, "TYPE_DOUBLE", False),
        (wrappers_pb2.Int32Value, "TYPE_DOUBLE", False),
    ],
)
def test__validate_paged_field_size_type(field_type, pb_type, expected):
    """Test _validate_paged_field_size_type with wrapper types and type indicators."""

    # Setup
    if pb_type in {"TYPE_INT32", "TYPE_DOUBLE"}:
        page_size = make_field(name="page_size", type=pb_type)
    else:
        # expecting TYPE_MESSAGE which in this context is associated with
        # *Int32Value in legacy APIs such as BigQuery.
        # See: https://github.com/googleapis/gapic-generator-python/blob/c8b7229ba2865d6a2f5966aa151be121de81f92d/gapic/schema/wrappers.py#L378C1-L411C10
        page_size = make_field(
            name="max_results",
            type=pb_type,
            message=make_message(name=field_type.DESCRIPTOR.name),
        )

    parent = make_field(name="parent", type="TYPE_STRING")
    page_token = make_field(name="page_token", type="TYPE_STRING")
    next_page_token = make_field(name="next_page_token", type="TYPE_STRING")

    input_msg = make_message(
        name="ListFoosRequest",
        fields=(
            parent,
            page_size,
            page_token,
        ),
    )

    output_msg = make_message(
        name="ListFoosResponse",
        fields=(
            make_field(name="foos", message=make_message("Foo"), repeated=True),
            next_page_token,
        ),
    )

    method = make_method(
        "ListFoos",
        input_message=input_msg,
        output_message=output_msg,
    )

    actual = method._validate_paged_field_size_type(page_field_size=page_size)
    assert actual == expected


def test_method_is_resumable_upload():
    # UploadMedia (and CreateYouTubeVideoUpload) are temporarily hardcoded as
    # resumable upload method names until resumable upload proto annotations
    # are adopted in the future.
    # Verify that UploadMedia is identified as a resumable upload method and
    # configures ResumableUploadSession / AsyncResumableUploadSession as the
    # client output while retaining the raw output message in ref_types.
    method_upload = make_method("UploadMedia")
    assert method_upload.is_resumable_upload
    assert method_upload.client_output.ident.name == "ResumableUploadSession"
    assert (
        str(method_upload.client_output.ident)
        == "resumable_transfer.ResumableUploadSession"
    )
    assert (
        method_upload.client_output_async.ident.name == "AsyncResumableUploadSession"
    )
    assert (
        str(method_upload.client_output_async.ident)
        == "resumable_transfer.AsyncResumableUploadSession"
    )
    assert method_upload.output in method_upload.ref_types

    # Verify that CreateYouTubeVideoUpload is also recognized as a resumable upload method.
    method_youtube_upload = make_method("CreateYouTubeVideoUpload")
    assert method_youtube_upload.is_resumable_upload

    # Verify that a non-resumable method name is not marked as a resumable upload.
    method_other = make_method("OtherMethod")
    assert not method_other.is_resumable_upload

