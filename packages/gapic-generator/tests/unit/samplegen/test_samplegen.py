# Copyright (C) 2019  Google LLC
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

import yaml
import pytest

from textwrap import dedent
from typing import TypeVar, Sequence
from collections import OrderedDict, namedtuple
from google.api import client_pb2
from google.api import resource_pb2
from google.protobuf import descriptor_pb2
from google.protobuf import json_format


import gapic.samplegen.samplegen as samplegen
import gapic.samplegen_utils.types as types
import gapic.samplegen_utils.yaml as gapic_yaml
from gapic.schema import api, metadata, naming
import gapic.schema.wrappers as wrappers
from gapic.utils import Options

from ..common_types import (
    DummyApiSchema,
    DummyField,
    DummyIdent,
    DummyNaming,
    DummyMessage,
    DummyMessageTypePB,
    DummyService,
    DummyMethod,
    message_factory,
    enum_factory,
)
from gapic.samplegen_utils import utils


@pytest.fixture(scope="module")
def api_naming():
    return DummyNaming(
        warehouse_package_name="mollusc-cephalopod-teuthida-",
        versioned_module_name="teuthida_v1",
        module_namespace=("mollusc", "cephalopod"),
        proto_package="mollusc.cephalopod",
    )


@pytest.fixture(scope="module")
def request_message():
    return DummyMessage(
        fields={
            "parent": DummyField(
                is_primitive=True, type=str, required=True, name="parent"
            ),
        },
        type=DummyMessageTypePB(name="ClassifyRequest"),
        ident=DummyIdent(name="ClassifyRequest"),
    )


@pytest.fixture(scope="module")
def request_message_from_another_package(api_naming):
    return DummyMessage(
        fields={
            "parent": DummyField(
                is_primitive=True, type=str, required=True, name="parent"
            ),
        },
        type=DummyMessageTypePB(name="ClassifyRequest"),
        ident=DummyIdent(name="ClassifyRequest"),
        meta=metadata.Metadata(
            address=metadata.Address(
                api_naming=api_naming,
                package=(
                    "a",
                    "b",
                ),
                module="c",
            )
        ),
    )


@pytest.fixture(scope="module")
def dummy_api_schema(request_message, api_naming):
    return DummyApiSchema(
        services={
            "Mollusc": DummyService(
                methods={}, client_name="MolluscClient", resource_messages_dict={}
            )
        },
        naming=api_naming,
        messages=request_message,
    )


@pytest.fixture(scope="module")
def dummy_api_schema_with_request_from_another_package(
    request_message_from_another_package, api_naming
):
    return DummyApiSchema(
        services={
            "Mollusc": DummyService(
                methods={}, client_name="MolluscClient", resource_messages_dict={}
            )
        },
        naming=api_naming,
        messages=request_message_from_another_package,
    )


def test_define(dummy_api_schema):
    define = {"define": "squid=$resp"}
    v = samplegen.Validator(
        DummyMethod(output=message_factory("mollusc")), api_schema=dummy_api_schema
    )
    v.validate_response([define])


def test_define_undefined_var(dummy_api_schema):
    define = {"define": "squid=humboldt"}
    v = samplegen.Validator(
        DummyMethod(output=message_factory("mollusc")), api_schema=dummy_api_schema
    )
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response([define])


def test_define_reserved_varname(dummy_api_schema):
    define = {"define": "class=$resp"}
    v = samplegen.Validator(
        DummyMethod(output=message_factory("mollusc")), api_schema=dummy_api_schema
    )
    with pytest.raises(types.ReservedVariableName):
        v.validate_response([define])


def test_define_add_var(dummy_api_schema):
    v = samplegen.Validator(
        DummyMethod(output=message_factory("mollusc.name")), api_schema=dummy_api_schema
    )
    v.validate_response([{"define": "squid=$resp"}, {"define": "name=squid.name"}])


def test_define_bad_form(dummy_api_schema):
    define = {"define": "mollusc=$resp.squid=$resp.clam"}
    v = samplegen.Validator(
        DummyMethod(output=message_factory("mollusc")), api_schema=dummy_api_schema
    )
    with pytest.raises(types.BadAssignment):
        v.validate_response([define])


def test_define_redefinition(dummy_api_schema):
    statements = [
        {"define": "molluscs=$resp.molluscs"},
        {"define": "molluscs=$resp.molluscs"},
    ]
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.molluscs", repeated_iter=[True])),
        api_schema=dummy_api_schema,
    )
    with pytest.raises(types.RedefinedVariable):
        v.validate_response(statements)


def test_preprocess_sample():
    # Verify that the default response is added.
    sample = {"service": "Mollusc", "rpc": "Classify"}

    classify_request_message = DummyMessage(
        fields={
            "parent": DummyField(
                is_primitive=True, type=str, required=True, name="parent"
            ),
        },
        type=DummyMessageTypePB(name="ClassifyRequest"),
        ident=DummyIdent(name="ClassifyRequest"),
    )

    api_schema = DummyApiSchema(
        services={
            "Mollusc": DummyService(
                methods={}, client_name="MolluscClient", resource_messages_dict={}
            )
        },
        naming=DummyNaming(
            warehouse_package_name="mollusc-cephalopod-teuthida-",
            versioned_module_name="teuthida_v1",
            module_namespace="mollusc.cephalopod",
        ),
        messages=classify_request_message,
    )

    rpc = DummyMethod(input=classify_request_message)

    samplegen.Validator.preprocess_sample(sample, api_schema, rpc)

    response = sample.get("response")
    assert response == [{"print": ["%s", "$resp"]}]

    package_name = sample.get("package_name")
    assert package_name == "mollusc-cephalopod-teuthida-"

    module_name = sample.get("module_name")
    assert module_name == "teuthida_v1"

    module_namespace = sample.get("module_namespace")
    assert module_namespace == "mollusc.cephalopod"

    client_name = sample.get("client_name")
    assert client_name == "MolluscClient"

    request_type = sample.get("request_type")
    assert request_type.ident.name == "ClassifyRequest"

    # assert mock request is created
    assert sample["request"] == [{"field": "parent", "value": "mock_value"}]


@pytest.mark.parametrize(
    "repeated_enum,expected", [(False, "TYPE_2"), (True, ["TYPE_2"])]
)
def test_preprocess_sample_with_enum_field(repeated_enum, expected):
    # Verify that the default response is added.
    sample = {"service": "Mollusc", "rpc": "Classify"}

    classify_request_message = DummyMessage(
        fields={
            "type": DummyField(
                name="type",
                required=True,
                repeated=repeated_enum,
                type=enum_factory("type", ["TYPE_1", "TYPE_2"]),
                enum=enum_factory("type", ["TYPE_1", "TYPE_2"]),
            )
        },
        type=DummyMessageTypePB(name="ClassifyRequest"),
        ident=DummyIdent(name="ClassifyRequest"),
    )

    api_schema = DummyApiSchema(
        services={
            "Mollusc": DummyService(
                methods={}, client_name="MolluscClient", resource_messages_dict={}
            )
        },
        naming=DummyNaming(
            warehouse_package_name="mollusc-cephalopod-teuthida-",
            versioned_module_name="teuthida_v1",
            module_namespace="mollusc.cephalopod",
        ),
        messages=classify_request_message,
    )

    rpc = DummyMethod(input=classify_request_message)

    samplegen.Validator.preprocess_sample(sample, api_schema, rpc)

    response = sample.get("response")
    assert response == [{"print": ["%s", "$resp"]}]

    package_name = sample.get("package_name")
    assert package_name == "mollusc-cephalopod-teuthida-"

    module_name = sample.get("module_name")
    assert module_name == "teuthida_v1"

    module_namespace = sample.get("module_namespace")
    assert module_namespace == "mollusc.cephalopod"

    client_name = sample.get("client_name")
    assert client_name == "MolluscClient"

    request_type = sample.get("request_type")
    assert request_type.ident.name == "ClassifyRequest"

    # assert mock request is created
    assert sample["request"] == [{"field": "type", "value": expected}]


def test_preprocess_sample_nested_message_field():
    # Verify that the default response is added.
    sample = {"service": "Mollusc", "rpc": "Classify"}

    classify_request_message = DummyMessage(
        fields={
            "config": DummyField(
                name="config",
                is_primitive=False,
                required=True,
                oneof=False,
                type=DummyMessage(
                    fields={
                        "name": DummyField(
                            is_primitive=True,
                            type=str,
                            name="name",
                            required=True,
                            oneof=False,
                        )
                    },
                ),
            )
        },
        type=DummyMessageTypePB(name="ClassifyRequest"),
        ident=DummyIdent(name="ClassifyRequest"),
    )

    api_schema = DummyApiSchema(
        services={
            "Mollusc": DummyService(
                methods={}, client_name="MolluscClient", resource_messages_dict={}
            )
        },
        naming=DummyNaming(
            warehouse_package_name="mollusc-cephalopod-teuthida-",
            versioned_module_name="teuthida_v1",
            module_namespace="mollusc.cephalopod",
        ),
        messages=classify_request_message,
    )

    rpc = DummyMethod(input=classify_request_message)

    samplegen.Validator.preprocess_sample(sample, api_schema, rpc)

    # assert mock request is created
    assert sample["request"] == [
        {"field": "config.name", "value": "mock_value"},
    ]


def test_preprocess_sample_void_method():
    sample = {"service": "Mollusc", "rpc": "Classify"}
    api_schema = DummyApiSchema(
        services={"Mollusc": DummyService(methods={}, client_name="MolluscClient")},
        naming=DummyNaming(
            warehouse_package_name="mollusc-cephalopod-teuthida-",
            versioned_module_name="teuthida_v1",
            module_namespace="mollusc.cephalopod",
        ),
    )

    rpc = DummyMethod(
        void=True, input=DummyMessage(ident=DummyIdent(name="ClassifyRequest"))
    )

    samplegen.Validator.preprocess_sample(sample, api_schema, rpc)

    assert sample["response"] == []


def test_preprocess_sample_with_request_module_name(
    dummy_api_schema_with_request_from_another_package,
):
    sample = {"service": "Mollusc", "rpc": "Classify"}
    api_schema = dummy_api_schema_with_request_from_another_package
    rpc = DummyMethod(input=api_schema.messages)

    samplegen.Validator.preprocess_sample(sample, api_schema, rpc)

    request_module_name = sample.get("request_module_name")
    assert request_module_name == "c_pb2"


def test_get_sample_imports(dummy_api_schema):
    sample = {"service": "Mollusc", "rpc": "Classify"}
    api_schema = dummy_api_schema
    rpc = DummyMethod(input=api_schema.messages)

    samplegen.Validator.preprocess_sample(sample, api_schema, rpc)
    imports = samplegen._get_sample_imports(sample, rpc)

    assert imports == ["from mollusc.cephalopod import teuthida_v1"]


def test_get_sample_imports_with_request_from_another_package(
    dummy_api_schema_with_request_from_another_package,
):
    sample = {"service": "Mollusc", "rpc": "Classify"}
    api_schema = dummy_api_schema_with_request_from_another_package
    rpc = DummyMethod(input=api_schema.messages)

    samplegen.Validator.preprocess_sample(sample, api_schema, rpc)
    imports = samplegen._get_sample_imports(sample, rpc)

    assert imports == [
        "from mollusc.cephalopod import teuthida_v1",
        "import a.b.c_pb2 as c_pb2  # type: ignore",
    ]


def test_define_input_param(dummy_api_schema):
    v = samplegen.Validator(
        DummyMethod(input=message_factory("mollusc.squid.mantle_length")),
        dummy_api_schema,
    )
    v.validate_and_transform_request(
        types.CallingForm.Request,
        [
            {
                "field": "squid.mantle_length",
                "value": "100 cm",
                "input_parameter": "mantle_length",
            }
        ],
    )
    v.validate_response([{"define": "length=mantle_length"}])


def test_define_input_param_redefinition(dummy_api_schema):
    v = samplegen.Validator(
        DummyMethod(input=message_factory("mollusc.squid.mantle_length")),
        dummy_api_schema,
    )
    v.validate_and_transform_request(
        types.CallingForm.Request,
        [
            {
                "field": "squid.mantle_length",
                "value": "100 cm",
                "input_parameter": "mantle_length",
            }
        ],
    )
    with pytest.raises(types.RedefinedVariable):
        v.validate_response([{"define": "mantle_length=mantle_length"}])


def test_print_basic(dummy_api_schema):
    print_statement = {"print": ["This is a squid"]}
    samplegen.Validator(DummyMethod(), dummy_api_schema).validate_response(
        [print_statement]
    )


def test_print_fmt_str(dummy_api_schema):
    print_statement = {"print": ["This is a squid named %s", "$resp.name"]}
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.name")), dummy_api_schema
    )
    v.validate_response([print_statement])


def test_print_fmt_mismatch(dummy_api_schema):
    print_statement = {"print": ["This is a squid named %s"]}
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.name")), dummy_api_schema
    )
    with pytest.raises(types.MismatchedFormatSpecifier):
        v.validate_response([print_statement])


def test_print_fmt_mismatch2(dummy_api_schema):
    print_statement = {"print": ["This is a squid", "$resp.name"]}
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.name")), dummy_api_schema
    )
    with pytest.raises(types.MismatchedFormatSpecifier):
        v.validate_response([print_statement])


def test_print_undefined_var(dummy_api_schema):
    print_statement = {"print": ["This mollusc is a %s", "mollusc.type"]}
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.type")), dummy_api_schema
    )
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response([print_statement])


def test_comment(dummy_api_schema):
    comment = {"comment": ["This is a mollusc"]}
    samplegen.Validator(DummyMethod(), dummy_api_schema).validate_response([comment])


def test_comment_fmt_str(dummy_api_schema):
    comment = {"comment": ["This is a mollusc of class %s", "$resp.klass"]}
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.klass")), dummy_api_schema
    )
    v.validate_response([comment])


def test_comment_fmt_undefined_var(dummy_api_schema):
    comment = {"comment": ["This is a mollusc of class %s", "cephalopod"]}
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response([comment])


def test_comment_fmt_mismatch(dummy_api_schema):
    comment = {"comment": ["This is a mollusc of class %s"]}
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.MismatchedFormatSpecifier):
        v.validate_response([comment])


def test_comment_fmt_mismatch2(dummy_api_schema):
    comment = {"comment": ["This is a mollusc of class ", "$resp.class"]}
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.MismatchedFormatSpecifier):
        v.validate_response([comment])


def test_loop_collection(dummy_api_schema):
    loop = {
        "loop": {
            "collection": "$resp.molluscs",
            "variable": "m",
            "body": [{"print": ["Mollusc of class: %s", "m.class"]}],
        }
    }
    OutputType = message_factory("$resp.molluscs.class", repeated_iter=[True, False])
    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    v.validate_response([loop])


def test_loop_collection_redefinition(dummy_api_schema):
    statements = [
        {"define": "m=$resp.molluscs"},
        {
            "loop": {
                "collection": "$resp.molluscs",
                "variable": "m",
                "body": [{"print": ["Mollusc of class: %s", "m.class"]}],
            }
        },
    ]
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.molluscs", repeated_iter=[True])),
        dummy_api_schema,
    )
    with pytest.raises(types.RedefinedVariable):
        v.validate_response(statements)


def test_loop_undefined_collection(dummy_api_schema):
    loop = {
        "loop": {
            "collection": "squid",
            "variable": "s",
            "body": [{"print": ["Squid: %s", "s"]}],
        }
    }
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response([loop])


def test_loop_collection_extra_kword(dummy_api_schema):
    loop = {
        "loop": {
            "collection": "$resp.molluscs",
            "squid": "$resp.squids",
            "variable": "m",
            "body": [{"print": ["Mollusc of class: %s", "m.class"]}],
        }
    }
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.BadLoop):
        v.validate_response([loop])


def test_loop_collection_missing_kword(dummy_api_schema):
    loop = {
        "loop": {
            "collection": "$resp.molluscs",
            "body": [{"print": ["Mollusc of class: %s", "m.class"]}],
        }
    }
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.BadLoop):
        v.validate_response([loop])


def test_loop_collection_reserved_loop_var(dummy_api_schema):
    loop = {
        "loop": {
            "collection": "$resp.molluscs",
            "variable": "class",
            "body": [{"print": ["Mollusc: %s", "class.name"]}],
        }
    }
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.molluscs", repeated_iter=[True])),
        dummy_api_schema,
    )
    with pytest.raises(types.ReservedVariableName):
        v.validate_response([loop])


def test_loop_map(dummy_api_schema):
    loop = {
        "loop": {
            "map": "$resp.molluscs",
            "key": "cls",
            "value": "mollusc",
            "body": [{"print": ["A %s is a %s", "mollusc", "cls"]}],
        }
    }
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="MOLLUSC_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )
    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    v.validate_response([loop])


def test_collection_loop_lexical_scope_variable(dummy_api_schema):
    statements = [
        {
            "loop": {
                "collection": "$resp.molluscs",
                "variable": "m",
                "body": [{"define": "squid=m"}],
            }
        },
        {"define": "cephalopod=m"},
    ]
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.molluscs", repeated_iter=[True])),
        dummy_api_schema,
    )
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response(statements)


def test_collection_loop_lexical_scope_inline(dummy_api_schema):
    statements = [
        {
            "loop": {
                "collection": "$resp.molluscs",
                "variable": "m",
                "body": [{"define": "squid=m"}],
            }
        },
        {"define": "cephalopod=squid"},
    ]
    v = samplegen.Validator(
        DummyMethod(output=message_factory("$resp.molluscs", repeated_iter=[True])),
        dummy_api_schema,
    )
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response(statements)


def test_map_loop_lexical_scope_key(dummy_api_schema):
    statements = [
        {
            "loop": {
                "map": "$resp.molluscs",
                "key": "cls",
                "value": "mollusc",
                "body": [{"define": "tmp=cls"}],
            }
        },
        # 'cls' is outside the visible lexical scope according to strict
        # samplegen rules, even though it is valid python.
        {"define": "last_cls=cls"},
    ]
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="MOLLUSC_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response(statements)


def test_map_loop_lexical_scope_value(dummy_api_schema):
    statements = [
        {
            "loop": {
                "map": "$resp.molluscs",
                "key": "cls",
                "value": "mollusc",
                "body": [{"define": "tmp=mollusc"}],
            }
        },
        # 'mollusc' is outside the visible lexical scope according to strict
        # samplegen rules, even though it is valid python.
        {"define": "last_mollusc=mollusc"},
    ]
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="MOLLUSC_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response(statements)


def test_map_loop_lexical_scope_inline(dummy_api_schema):
    statements = [
        {
            "loop": {
                "map": "$resp.molluscs",
                "key": "cls",
                "value": "mollusc",
                "body": [{"define": "tmp=mollusc"}],
            }
        },
        # 'tmp' is outside the visible lexical scope according to strict
        # samplegen rules, even though it is valid python.
        {"define": "last_mollusc=tmp"},
    ]
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="MOLLUSC_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )
    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response(statements)


def test_loop_map_reserved_key(dummy_api_schema):
    loop = {
        "loop": {
            "map": "$resp.molluscs",
            # Can't use 'class' since it's a reserved keyword
            "key": "class",
            "value": "mollusc",
            "body": [{"print": ["A %s is a %s", "mollusc", "class"]}],
        }
    }
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="MOLLUSC_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.ReservedVariableName):
        v.validate_response([loop])


def test_loop_map_reserved_val(dummy_api_schema):
    loop = {
        "loop": {
            "map": "$resp.molluscs",
            "key": "m",
            # Can't use 'class' since it's a reserved keyword
            "value": "class",
            "body": [{"print": ["A %s is a %s", "m", "class"]}],
        }
    }
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="CLASS_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.ReservedVariableName):
        v.validate_response([loop])


def test_loop_map_undefined(dummy_api_schema):
    loop = {
        "loop": {
            "map": "molluscs",
            "key": "name",
            "value": "mollusc",
            "body": [{"print": ["A %s is a %s", "mollusc", "name"]}],
        }
    }
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response([loop])


def test_loop_map_no_key(dummy_api_schema):
    loop = {
        "loop": {
            "map": "$resp.molluscs",
            "value": "mollusc",
            "body": [{"print": ["Mollusc: %s", "mollusc"]}],
        }
    }
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="CLASS_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    v.validate_response([loop])


def test_loop_map_no_value(dummy_api_schema):
    loop = {
        "loop": {
            "map": "$resp.molluscs",
            "key": "mollusc",
            "body": [{"print": ["Mollusc: %s", "mollusc"]}],
        }
    }
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="CLASS_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    v.validate_response([loop])


def test_loop_map_no_key_or_value(dummy_api_schema):
    loop = {
        "loop": {
            "map": "$resp.molluscs",
            # Need at least one of 'key' or 'value'
            "body": [{"print": ["Dead loop"]}],
        }
    }
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="CLASS_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.BadLoop):
        v.validate_response([loop])


def test_loop_map_no_map(dummy_api_schema):
    loop = {
        "loop": {
            "key": "name",
            "value": "mollusc",
            "body": [{"print": ["A %s is a %s", "mollusc", "name"]}],
        }
    }
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.BadLoop):
        v.validate_response([loop])


def test_loop_map_no_body(dummy_api_schema):
    loop = {"loop": {"map": "$resp.molluscs", "key": "name", "value": "mollusc"}}
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.BadLoop):
        v.validate_response([loop])


def test_loop_map_extra_kword(dummy_api_schema):
    loop = {
        "loop": {
            "map": "$resp.molluscs",
            "key": "name",
            "value": "mollusc",
            "phylum": "$resp.phylum",
            "body": [{"print": ["A %s is a %s", "mollusc", "name"]}],
        }
    }
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.BadLoop):
        v.validate_response([loop])


def test_loop_map_redefined_key(dummy_api_schema):
    statements = [
        {"define": "mollusc=$resp.molluscs"},
        {
            "loop": {
                "map": "$resp.molluscs",
                # Can't redefine mollusc, which was defined one statement above.
                "key": "mollusc",
                "body": [{"print": ["Mollusc: %s", "mollusc"]}],
            }
        },
    ]
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="CLASS_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.RedefinedVariable):
        v.validate_response(statements)


def test_loop_map_redefined_value(dummy_api_schema):
    statements = [
        {"define": "mollusc=$resp.molluscs"},
        {
            "loop": {
                "map": "$resp.molluscs",
                # Can't redefine 'mollusc', which was defined one statement above.
                "value": "mollusc",
                "body": [{"print": ["Mollusc: %s", "mollusc"]}],
            }
        },
    ]
    OutputType = DummyMessage(
        fields={
            "molluscs": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(fields={}, type="CLASS_TYPE")
                        ),
                    },
                    type="MOLLUSCS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            ),
        },
        type="RESPONSE_TYPE",
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.RedefinedVariable):
        v.validate_response(statements)


def test_validate_write_file(dummy_api_schema):
    statements = [
        {
            "write_file": {
                "filename": ["specimen-%s", "$resp.species"],
                "contents": "$resp.photo",
            }
        }
    ]
    OutputType = DummyMessage(
        fields={
            "species": DummyField(message=DummyMessage(fields={})),
            "photo": DummyField(message=DummyMessage(fields={})),
        }
    )
    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    v.validate_response(statements)


def test_validate_write_file_fname_fmt(dummy_api_schema):
    statements = [
        {"write_file": {"filename": ["specimen-%s"], "contents": "$resp.photo"}}
    ]
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.MismatchedFormatSpecifier):
        v.validate_response(statements)


def test_validate_write_file_fname_bad_var(dummy_api_schema):
    statements = [
        {
            "write_file": {
                "filename": ["specimen-%s", "squid.species"],
                "contents": "$resp.photo",
            }
        }
    ]
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response(statements)


def test_validate_write_file_missing_fname(dummy_api_schema):
    statements = [{"write_file": {"contents": "$resp.photo"}}]
    OutputType = DummyMessage(
        fields={
            "filename": DummyField(message=DummyMessage(fields={})),
            "photo": DummyField(message=DummyMessage(fields={})),
        }
    )
    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.InvalidStatement):
        v.validate_response(statements)


def test_validate_write_file_missing_contents(dummy_api_schema):
    statements = [{"write_file": {"filename": ["specimen-%s", "$resp.species"]}}]
    OutputType = DummyMessage(
        fields={
            "species": DummyField(message=DummyMessage(fields={})),
            "photo": DummyField(message=DummyMessage(fields={})),
        }
    )

    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.InvalidStatement):
        v.validate_response(statements)


def test_validate_write_file_bad_contents_var(dummy_api_schema):
    statements = [
        {
            "write_file": {
                "filename": ["specimen-%s", "$resp.species"],
                "contents": "squid.photo",
            }
        }
    ]
    OutputType = DummyMessage(
        fields={
            "species": DummyField(message=DummyMessage(fields={})),
            "photo": DummyField(message=DummyMessage(fields={})),
        }
    )
    v = samplegen.Validator(DummyMethod(output=OutputType), dummy_api_schema)
    with pytest.raises(types.UndefinedVariableReference):
        v.validate_response(statements)


def test_invalid_statement(dummy_api_schema):
    statements = [{"print": ["Name"], "comment": ["Value"]}]
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.InvalidStatement):
        v.validate_response(statements)


def test_invalid_statement2(dummy_api_schema):
    statements = [{"squidify": ["Statement body"]}]
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.InvalidStatement):
        v.validate_response(statements)


# validate_and_transform_request tests
def test_validate_request_basic(dummy_api_schema):
    input_type = DummyMessage(
        fields={
            "squid": DummyField(
                message=DummyMessage(
                    fields={
                        "mantle_length": DummyField(
                            message=DummyMessage(type="LENGTH_TYPE")
                        ),
                        "mantle_mass": DummyField(
                            message=DummyMessage(type="MASS_TYPE")
                        ),
                        "num_tentacles": DummyField(
                            message=DummyMessage(type="MASS_TYPE")
                        ),
                    },
                    type="SQUID_TYPE",
                )
            )
        },
        type="REQUEST_TYPE",
    )

    v = samplegen.Validator(DummyMethod(input=input_type), dummy_api_schema)
    actual = v.validate_and_transform_request(
        types.CallingForm.Request,
        [
            {"field": "squid.mantle_length", "value": '100 "cm'},
            {"field": "squid.mantle_mass", "value": "10 kg"},
            {"field": "squid.num_tentacles", "value": 10},
        ],
    )
    expected = samplegen.FullRequest(
        request_list=[
            samplegen.TransformedRequest(
                base="squid",
                body=[
                    samplegen.AttributeRequestSetup(
                        field="mantle_length", value='"100 \\"cm"'
                    ),
                    samplegen.AttributeRequestSetup(
                        field="mantle_mass", value='"10 kg"'
                    ),
                    samplegen.AttributeRequestSetup(field="num_tentacles", value=10),
                ],
                single=None,
            )
        ]
    )

    assert actual == expected


def test_validate_request_no_field_parameter(dummy_api_schema):
    # May need to remeove this test because it doesn't necessarily make sense any more.
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.InvalidRequestSetup):
        v.validate_and_transform_request(
            types.CallingForm.Request, [{"squid": "humboldt", "value": "teuthida"}]
        )


def test_validate_request_no_such_attribute(dummy_api_schema):
    v = samplegen.Validator(
        DummyMethod(input=message_factory("mollusc.squid.mantle")), dummy_api_schema
    )
    with pytest.raises(types.BadAttributeLookup):
        v.validate_and_transform_request(
            types.CallingForm.Request, [{"field": "clam.shell", "value": "20"}]
        )


def test_validate_request_top_level_field(dummy_api_schema):
    v = samplegen.Validator(
        DummyMethod(input=message_factory("mollusc.squid")), dummy_api_schema
    )
    actual = v.validate_and_transform_request(
        types.CallingForm.Request, [{"field": "squid", "value": "humboldt"}]
    )

    expected = samplegen.FullRequest(
        request_list=[
            samplegen.TransformedRequest(
                base="squid",
                body=None,
                single=samplegen.AttributeRequestSetup(value='"humboldt"'),
            )
        ]
    )

    assert actual == expected


def test_validate_request_missing_keyword(dummy_api_schema, kword="field"):
    v = samplegen.Validator(
        DummyMethod(input=message_factory("mollusc.squid")), dummy_api_schema
    )
    with pytest.raises(types.InvalidRequestSetup):
        v.validate_and_transform_request(types.CallingForm.Request, [{kword: "squid"}])


def test_validate_request_missing_value(dummy_api_schema):
    test_validate_request_missing_keyword(dummy_api_schema, kword="value")


def test_validate_request_spurious_kword(dummy_api_schema):
    v = samplegen.Validator(
        DummyMethod(input=message_factory("mollusc.squid")), dummy_api_schema
    )
    with pytest.raises(types.InvalidRequestSetup):
        v.validate_and_transform_request(
            types.CallingForm.Request,
            [{"field": "mollusc.squid", "value": "humboldt", "order": "teuthida"}],
        )


def test_validate_request_unknown_field_type(dummy_api_schema):
    v = samplegen.Validator(
        DummyMethod(input=DummyMessage(fields={"squid": DummyField()})),
        dummy_api_schema,
    )
    with pytest.raises(TypeError):
        v.validate_and_transform_request(
            types.CallingForm.Request, [{"field": "squid", "value": "humboldt"}]
        )


def test_validate_request_duplicate_top_level_fields(dummy_api_schema):
    v = samplegen.Validator(
        DummyMethod(input=message_factory("mollusc.squid")), dummy_api_schema
    )
    with pytest.raises(types.InvalidRequestSetup):
        v.validate_and_transform_request(
            types.CallingForm.Request,
            [
                {"field": "squid", "value": "humboldt"},
                {"field": "squid", "value": "bobtail"},
            ],
        )


def test_validate_request_multiple_arguments(dummy_api_schema):
    input_type = DummyMessage(
        fields={
            "squid": DummyField(
                message=DummyMessage(
                    fields={
                        "mantle_length": DummyField(
                            message=DummyMessage(type="LENGTH_TYPE")
                        )
                    },
                    type="SQUID_TYPE",
                )
            ),
            "clam": DummyField(
                message=DummyMessage(
                    fields={
                        "shell_mass": DummyField(message=DummyMessage(type="MASS_TYPE"))
                    },
                    type="CLAM_TYPE",
                )
            ),
        },
        type="REQUEST_TYPE",
    )

    v = samplegen.Validator(DummyMethod(input=input_type), dummy_api_schema)
    actual = v.validate_and_transform_request(
        types.CallingForm.Request,
        [
            {"field": "squid.mantle_length", "value": "100 cm", "value_is_file": True},
            {
                "field": "clam.shell_mass",
                "value": "100 kg",
                "comment": "Clams can be large",
            },
        ],
    )
    expected = samplegen.FullRequest(
        request_list=[
            samplegen.TransformedRequest(
                base="squid",
                body=[
                    samplegen.AttributeRequestSetup(
                        field="mantle_length", value='"100 cm"', value_is_file=True
                    )
                ],
                single=None,
            ),
            samplegen.TransformedRequest(
                base="clam",
                body=[
                    samplegen.AttributeRequestSetup(
                        field="shell_mass",
                        value='"100 kg"',
                        comment="Clams can be large",
                    )
                ],
                single=None,
            ),
        ]
    )

    assert actual == expected


def test_validate_request_duplicate_input_param(dummy_api_schema):
    input_type = DummyMessage(
        fields={
            "squid": DummyField(
                message=DummyMessage(
                    fields={
                        "mantle_mass": DummyField(
                            message=DummyMessage(type="MASS_TYPE")
                        )
                    },
                    type="SQUID_TYPE",
                )
            ),
            "clam": DummyField(
                message=DummyMessage(
                    fields={
                        "mantle_mass": DummyField(
                            message=DummyMessage(type="MASS_TYPE")
                        )
                    },
                    type="CLAM_TYPE",
                )
            ),
        },
        type="REQUEST_TYPE",
    )

    v = samplegen.Validator(DummyMethod(input=input_type), dummy_api_schema)
    with pytest.raises(types.RedefinedVariable):
        v.validate_and_transform_request(
            types.CallingForm.Request,
            [
                {
                    "field": "squid.mantle_mass",
                    "value": "10 kg",
                    "input_parameter": "mantle_mass",
                },
                {
                    "field": "clam.mantle_mass",
                    "value": "1 kg",
                    "input_parameter": "mantle_mass",
                },
            ],
        )


def test_validate_request_reserved_input_param(dummy_api_schema):
    v = samplegen.Validator(DummyMethod(), dummy_api_schema)
    with pytest.raises(types.ReservedVariableName):
        v.validate_and_transform_request(
            types.CallingForm.Request,
            [
                {
                    "field": "mollusc.class",
                    "value": "cephalopoda",
                    "input_parameter": "class",
                }
            ],
        )


def test_validate_request_calling_form():
    assert (
        types.CallingForm.method_default(DummyMethod(lro=True))
        == types.CallingForm.LongRunningRequestPromise
    )

    assert (
        types.CallingForm.method_default(DummyMethod(paged_result_field=True))
        == types.CallingForm.RequestPagedAll
    )

    assert (
        types.CallingForm.method_default(DummyMethod(client_streaming=True))
        == types.CallingForm.RequestStreamingClient
    )

    assert (
        types.CallingForm.method_default(DummyMethod(server_streaming=True))
        == types.CallingForm.RequestStreamingServer
    )

    assert types.CallingForm.method_default(DummyMethod()) == types.CallingForm.Request

    assert (
        types.CallingForm.method_default(
            DummyMethod(client_streaming=True, server_streaming=True)
        )
        == types.CallingForm.RequestStreamingBidi
    )


def test_coerce_response_name():
    # Don't really need a test, but it shuts up code coverage.
    assert utils.coerce_response_name("$resp.squid") == "response.squid"
    assert utils.coerce_response_name("mollusc.squid") == "mollusc.squid"


def test_regular_response_type(dummy_api_schema):
    OutputType = TypeVar("OutputType")
    method = DummyMethod(output=OutputType)

    v = samplegen.Validator(method, dummy_api_schema)
    assert v.var_field("$resp").message == OutputType


def test_paged_response_type(dummy_api_schema):
    OutputType = TypeVar("OutputType")
    PagedType = TypeVar("PagedType")
    PagedField = DummyField(message=PagedType)
    method = DummyMethod(output=OutputType, paged_result_field=PagedField)

    v = samplegen.Validator(method, dummy_api_schema)
    assert v.var_field("$resp").message == PagedType


def test_lro_response_type(dummy_api_schema):
    OutputType = TypeVar("OutputType")
    LroType = TypeVar("LroType")
    method = DummyMethod(
        output=OutputType, lro=namedtuple("operation", ["response_type"])(LroType)
    )

    v = samplegen.Validator(method, dummy_api_schema)
    assert v.var_field("$resp").message == LroType


def test_validate_expression(dummy_api_schema):
    exp = "$resp.coleoidea.octopodiformes.octopus"
    OutputType = message_factory(exp)
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)

    exp_type = v.validate_expression(exp)
    assert exp_type.message.type == "OCTOPUS_TYPE"


def test_validate_expression_undefined_base(dummy_api_schema):
    exp = "$resp.coleoidea.octopodiformes.octopus"
    OutputType = message_factory(exp)
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)

    with pytest.raises(types.UndefinedVariableReference):
        v.validate_expression("mollusc")


def test_validate_expression_no_such_attr(dummy_api_schema):
    OutputType = message_factory("$resp.coleoidea")
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)

    with pytest.raises(types.BadAttributeLookup):
        v.validate_expression("$resp.nautiloidea")


def test_validate_expression_non_indexed_non_terminal_repeated(dummy_api_schema):
    # This is a little tricky: there's an attribute hierarchy
    # of response/coleoidea/octopodiformes, but coleoidea is a repeated field,
    # so accessing $resp.coleoidea.octopodiformes doesn't make any sense.
    exp = "$resp.coleoidea.octopodiformes"
    OutputType = message_factory(exp, repeated_iter=[True, False])
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)

    with pytest.raises(types.BadAttributeLookup):
        v.validate_response([{"define": "octopus=$resp.coleoidea.octopodiformes"}])


def test_validate_expression_collection(dummy_api_schema):
    exp = "$resp.molluscs"
    OutputType = message_factory(exp, repeated_iter=[True])
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    v.validate_response(
        [
            {
                "loop": {
                    "collection": "$resp.molluscs",
                    "variable": "m",
                    "body": [{"print": ["%s", "m"]}],
                }
            }
        ]
    )


def test_validate_expression_collection_error(dummy_api_schema):
    exp = "$resp.molluscs.mollusc"
    OutputType = message_factory(exp)
    method = DummyMethod(output=OutputType)

    statement = {
        "loop": {
            "collection": "$resp.molluscs",
            "variable": "m",
            "body": [{"print": ["%s", "m"]}],
        }
    }

    v = samplegen.Validator(method, dummy_api_schema)

    # Because 'molluscs' isn't repeated
    with pytest.raises(types.BadLoop):
        v.validate_response([statement])


def test_validate_expression_repeated_lookup(dummy_api_schema):
    exp = "$resp.molluscs.mantle"
    OutputType = message_factory(exp, repeated_iter=[True, False])
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    v.validate_expression("$resp.molluscs[0].mantle")


def test_validate_expression_repeated_lookup_nested(dummy_api_schema):
    exp = "$resp.molluscs.tentacles.club"
    OutputType = message_factory(exp, [True, True, False])
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    v.validate_expression("$resp.molluscs[0].tentacles[0].club")


def test_validate_expression_repeated_lookup_invalid(dummy_api_schema):
    exp = "$resp.molluscs.mantle"
    OutputType = message_factory(exp)
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    with pytest.raises(types.BadAttributeLookup):
        v.validate_expression("$resp.molluscs[0].mantle")


def test_validate_expression_base_attr_is_repeated(dummy_api_schema):
    exp = "$resp.molluscs.mantle"
    OutputType = message_factory(exp, repeated_iter=[True, False])
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    v.validate_response([{"define": "molluscs=$resp.molluscs"}])
    v.validate_expression("molluscs[0].mantle")


def test_validate_expression_map_lookup(dummy_api_schema):
    # See https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/descriptor.proto#L475
    # for details on how mapped attributes get transformed by the protoc compiler.
    OutputType = DummyMessage(
        fields={
            "cephalopods": DummyField(
                message=DummyMessage(
                    fields={
                        # real type is most likely str in real protos
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(
                                fields={
                                    "mantle": DummyField(
                                        message=DummyMessage(
                                            type="MANTLE_TYPE", fields={}
                                        ),
                                    )
                                },
                                type="CEPHALOPOD_TYPE",
                            )
                        ),
                    },
                    type="CEPHALOPODS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            )
        },
        type="MOLLUSC_TYPE",
    )
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    v.validate_expression('$resp.cephalopods{"squid"}.mantle')


def test_validate_expression_map_lookup_terminal_lookup(dummy_api_schema):
    OutputType = DummyMessage(
        fields={
            "cephalopods": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(
                                fields={
                                    "mantle": DummyField(
                                        message=DummyMessage(
                                            type="MANTLE_TYPE", fields={}
                                        ),
                                    )
                                },
                                type="CEPHALOPOD_TYPE",
                            )
                        ),
                    },
                    type="CEPHALOPODS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            )
        },
        type="MOLLUSC_TYPE",
    )
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    v.validate_expression('$resp.cephalopods{"squid"}')


def test_validate_expression_mapped_no_map_field(dummy_api_schema):
    OutputType = DummyMessage(
        fields={
            "cephalopods": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        "value": DummyField(
                            message=DummyMessage(
                                fields={
                                    "mantle": DummyField(
                                        message=DummyMessage(
                                            type="MANTLE_TYPE", fields={}
                                        ),
                                    )
                                },
                                type="CEPHALOPOD_TYPE",
                            )
                        ),
                    },
                    type="CEPHALOPODS_TYPE",
                    # The map_field attribute in the options indicates whether
                    # a message type is 'really' a map or just looks like one.
                    options=namedtuple("MessageOptions", ["map_field"])(False),
                ),
                repeated=True,
            )
        },
        type="MOLLUSC_TYPE",
    )
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    with pytest.raises(types.BadAttributeLookup):
        v.validate_expression('$resp.cephalopods{"squid"}.mantle')


def test_validate_expression_mapped_no_value(dummy_api_schema):
    OutputType = DummyMessage(
        fields={
            "cephalopods": DummyField(
                message=DummyMessage(
                    # Maps need 'key' AND 'value' attributes.
                    fields={"key": DummyField()},
                    type="CEPHALOPODS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            )
        },
        type="MOLLUSC_TYPE",
    )
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    with pytest.raises(types.BadAttributeLookup):
        v.validate_expression('$resp.cephalopods{"squid"}.mantle')


def test_validate_expression_mapped_no_message(dummy_api_schema):
    OutputType = DummyMessage(
        fields={
            "cephalopods": DummyField(
                message=DummyMessage(
                    fields={
                        "key": DummyField(),
                        # The value field needs a message.
                        "value": DummyField(),
                    },
                    type="CEPHALOPODS_TYPE",
                    options=namedtuple("MessageOptions", ["map_field"])(True),
                ),
                repeated=True,
            )
        },
        type="MOLLUSC_TYPE",
    )
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    with pytest.raises(types.BadAttributeLookup):
        v.validate_expression('$resp.cephalopods{"squid"}.mantle')


def test_validate_expresssion_lookup_unrepeated_base(dummy_api_schema):
    exp = "$resp.molluscs"
    OutputType = message_factory(exp)
    method = DummyMethod(output=OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    with pytest.raises(types.BadAttributeLookup):
        v.validate_response([{"define": "m=$resp[0]"}])


def test_validate_expression_malformed_base(dummy_api_schema):
    # Note the mistype
    exp = "r$esp.mollusc"
    OutputType = message_factory(exp)
    method = DummyMethod(OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    with pytest.raises(types.BadAttributeLookup):
        v.validate_expression(exp)


def test_validate_expression_malformed_attr(dummy_api_schema):
    # Note the mistype
    exp = "$resp.mollu$c"
    OutputType = message_factory(exp)
    method = DummyMethod(OutputType)
    v = samplegen.Validator(method, dummy_api_schema)
    with pytest.raises(types.BadAttributeLookup):
        v.validate_expression(exp)


def test_validate_request_enum(dummy_api_schema):
    enum = enum_factory("subclass", ["AMMONOIDEA", "COLEOIDEA", "NAUTILOIDEA"])
    request_type = message_factory("mollusc.cephalopod.subclass", enum=enum)

    v = samplegen.Validator(DummyMethod(input=request_type), dummy_api_schema)
    actual = v.validate_and_transform_request(
        types.CallingForm.Request,
        [{"field": "cephalopod.subclass", "value": "COLEOIDEA"}],
    )
    expected = samplegen.FullRequest(
        request_list=[
            samplegen.TransformedRequest(
                "cephalopod",
                body=[
                    samplegen.AttributeRequestSetup(
                        field="subclass", value='"COLEOIDEA"'
                    )
                ],
                single=None,
            )
        ]
    )
    assert actual == expected


def test_validate_request_enum_top_level(dummy_api_schema):
    enum = enum_factory("subclass", ["AMMONOIDEA", "COLEOIDEA", "NAUTILOIDEA"])
    request_type = message_factory("mollusc.subclass", enum=enum)

    v = samplegen.Validator(DummyMethod(input=request_type), dummy_api_schema)
    actual = v.validate_and_transform_request(
        types.CallingForm.Request, [{"field": "subclass", "value": "COLEOIDEA"}]
    )
    expected = samplegen.FullRequest(
        request_list=[
            samplegen.TransformedRequest(
                "subclass",
                single=samplegen.AttributeRequestSetup(value='"COLEOIDEA"'),
                body=None,
            )
        ]
    )
    assert actual == expected


def test_validate_request_enum_invalid_value(dummy_api_schema):
    enum = enum_factory("subclass", ["AMMONOIDEA", "COLEOIDEA", "NAUTILOIDEA"])
    request_type = message_factory("mollusc.cephalopod.subclass", enum=enum)
    v = samplegen.Validator(
        DummyMethod(output=message_factory("mollusc_result"), input=request_type),
        dummy_api_schema,
    )
    with pytest.raises(types.InvalidEnumVariant):
        v.validate_and_transform_request(
            types.CallingForm.Request,
            # Heterodonta are bivalves, not cephalopods
            [{"field": "cephalopod.subclass", "value": "HETERODONTA"}],
        )


def test_validate_request_enum_not_last_attr(dummy_api_schema):
    # enum = enum_factory("subclass", ["AMMONOIDEA", "COLEOIDEA", "NAUTILOIDEA"])
    # field = make_field(name="subclass", enum=enum)
    request_type = make_message(
        name="mollusc",
        fields=[
            make_field(
                name="subclass",
                enum=enum_factory(
                    "subclass", ["AMMONOIDEA", "COLEOIDEA", "NAUTILOIDEA"]
                ),
            )
        ],
    )

    # request_type = message_factory("mollusc.subclass", enum=enum)
    v = samplegen.Validator(
        DummyMethod(output=message_factory("mollusc_result"), input=request_type),
        dummy_api_schema,
    )
    with pytest.raises(types.NonTerminalPrimitiveOrEnum):
        v.validate_and_transform_request(
            types.CallingForm.Request,
            [{"field": "subclass.order", "value": "COLEOIDEA"}],
        )


def test_validate_request_resource_name():
    request = [
        {"field": "taxon%kingdom", "value": "animalia"},
        {"field": "taxon%phylum", "value": "mollusca", "input_parameter": "phylum"},
    ]

    resource_type = "taxonomy.google.com/Linnaean"
    taxon_field = make_field(name="taxon")
    rr = taxon_field.options.Extensions[resource_pb2.resource_reference]
    rr.type = resource_type
    request_descriptor = make_message(name="Request", fields=[taxon_field])

    # Strictly speaking, 'phylum' is the resource, but it's not what we're
    # manipulating to let samplegen know it's the resource.
    phylum_options = descriptor_pb2.MessageOptions()
    resource = phylum_options.Extensions[resource_pb2.resource]
    resource.type = resource_type
    resource.pattern.append("kingdom/{kingdom}/phylum/{phylum}")
    phylum_descriptor = make_message(name="Phylum", options=phylum_options)

    method = DummyMethod(input=request_descriptor)
    # We don't actually care about the key,
    # but the 'messages' property is a mapping type,
    # and the implementation code expects this.
    api_schema = DummyApiSchema(
        messages={
            k: v
            for k, v in enumerate(
                [
                    request_descriptor,
                    phylum_descriptor,
                ]
            )
        },
        services={
            "Mollusc": DummyService(
                methods={},
                client_name="MolluscClient",
                resource_messages_dict={resource_type: phylum_descriptor},
            )
        },
    )

    v = samplegen.Validator(method=method, api_schema=api_schema)

    actual = v.validate_and_transform_request(types.CallingForm.Request, request)

    expected = samplegen.FullRequest(
        request_list=[
            samplegen.TransformedRequest(
                base="taxon",
                pattern="kingdom/{kingdom}/phylum/{phylum}",
                single=None,
                body=[
                    samplegen.AttributeRequestSetup(
                        field="kingdom",
                        value="animalia",
                    ),
                    samplegen.AttributeRequestSetup(
                        field="phylum",
                        value="mollusca",
                        input_parameter="phylum",
                    ),
                ],
            )
        ]
    )

    assert actual == expected


def test_validate_request_primitive_field(dummy_api_schema):
    field = make_field(name="species", type="TYPE_STRING")
    request_type = make_message(name="request", fields=[field])

    request = [{"field": "species", "value": "Architeuthis dux"}]
    v = samplegen.Validator(
        DummyMethod(output=message_factory("mollusc_result"), input=request_type),
        dummy_api_schema,
    )

    actual = v.validate_and_transform_request(types.CallingForm.Request, request)
    expected = samplegen.FullRequest(
        request_list=[
            samplegen.TransformedRequest(
                base="species",
                body=None,
                single=samplegen.AttributeRequestSetup(value='"Architeuthis dux"'),
            )
        ]
    )

    assert actual == expected


def test_validate_request_resource_name_mixed(request=None):
    # Note the mixing of resource name and non-resource name request field
    request = request or [
        {"field": "taxon%kingdom", "value": "animalia"},
        {"field": "taxon.domain", "value": "eukarya"},
    ]
    v = samplegen.Validator(
        method=DummyMethod(
            input=make_message(
                name="taxonomy",
                fields=[
                    make_field(
                        name="taxon",
                        message=make_message(
                            name="Taxon",
                            fields=[
                                make_field(
                                    name="domain", message=make_message(name="Domain")
                                )
                            ],
                        ),
                    )
                ],
            ),
        ),
        api_schema=None,
    )

    with pytest.raises(types.ResourceRequestMismatch):
        v.validate_and_transform_request(types.CallingForm.Request, request)


def test_validate_request_resource_name_mixed_reversed():
    # Again, note the mixed use of . and %
    request = [
        {"field": "taxon.domain", "value": "eukarya"},
        {"field": "taxon%kingdom", "value": "animalia"},
    ]
    test_validate_request_resource_name_mixed(request)


def test_validate_request_no_such_attr(dummy_api_schema):
    request = [{"field": "taxon%kingdom", "value": "animalia"}]
    method = DummyMethod(input=make_message(name="Request"))
    v = samplegen.Validator(method, dummy_api_schema)

    with pytest.raises(types.BadAttributeLookup):
        v.validate_and_transform_request(types.CallingForm.Request, request)


def test_validate_request_no_such_resource():
    request = [{"field": "taxon%kingdom", "value": "animalia"}]
    resource_type = "taxonomy.google.com/Linnaean"
    taxon_field = make_field(name="taxon")
    rr = taxon_field.options.Extensions[resource_pb2.resource_reference]
    rr.type = resource_type
    request_descriptor = make_message(name="Request", fields=[taxon_field])

    method = DummyMethod(input=request_descriptor)
    api_schema = DummyApiSchema(
        messages={k: v for k, v in enumerate([request_descriptor])},
        services={
            "Mollusc": DummyService(
                methods={}, client_name="MolluscClient", resource_messages_dict={}
            )
        },
    )

    v = samplegen.Validator(method=method, api_schema=api_schema)
    with pytest.raises(types.NoSuchResource):
        v.validate_and_transform_request(types.CallingForm.Request, request)


def test_validate_request_no_such_pattern():
    request = [
        # Note that there's only the one attribute, 'phylum', and that the only
        # pattern expects both 'kingdom' and 'phylum'.
        {"field": "taxon%phylum", "value": "mollusca", "input_parameter": "phylum"}
    ]

    resource_type = "taxonomy.google.com/Linnaean"
    taxon_field = make_field(name="taxon")
    rr = taxon_field.options.Extensions[resource_pb2.resource_reference]
    rr.type = resource_type
    request_descriptor = make_message(name="Request", fields=[taxon_field])

    phylum_options = descriptor_pb2.MessageOptions()
    resource = phylum_options.Extensions[resource_pb2.resource]
    resource.type = resource_type
    resource.pattern.append("kingdom/{kingdom}/phylum/{phylum}")
    phylum_descriptor = make_message(name="Phylum", options=phylum_options)

    method = DummyMethod(input=request_descriptor)
    api_schema = DummyApiSchema(
        messages={
            k: v
            for k, v in enumerate(
                [
                    request_descriptor,
                    phylum_descriptor,
                ]
            )
        },
        services={
            "Mollusc": DummyService(
                methods={},
                client_name="MolluscClient",
                resource_messages_dict={resource_type: phylum_descriptor},
            )
        },
    )

    v = samplegen.Validator(method=method, api_schema=api_schema)
    with pytest.raises(types.NoSuchResourcePattern):
        v.validate_and_transform_request(types.CallingForm.Request, request)


def test_validate_request_non_terminal_primitive_field(dummy_api_schema):
    field = make_field(name="species", type="TYPE_STRING")
    request_type = make_message(name="request", fields=[field])

    request = [{"field": "species.nomenclature", "value": "Architeuthis dux"}]
    v = samplegen.Validator(
        DummyMethod(output=message_factory("mollusc_result"), input=request_type),
        dummy_api_schema,
    )

    with pytest.raises(types.NonTerminalPrimitiveOrEnum):
        v.validate_and_transform_request(types.CallingForm.Request, request)


def test_parse_invalid_handwritten_spec(fs):
    fpath = "sampledir/sample.yaml"
    fs.create_file(
        fpath,
        # spec is missing type
        contents=dedent(
            """
            ---
            schema_version: 1.2.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            """
        ),
    )

    with pytest.raises(types.InvalidConfig):
        list(samplegen.parse_handwritten_specs(sample_configs=[fpath]))


@pytest.mark.parametrize(
    "opts_transport,expected",
    [
        (
            "transport=grpc+rest",
            [
                {
                    "rpc": "Ramshorn",
                    "transport": "grpc",
                    "service": "animalia.mollusca.v1.Squid",
                    "region_tag": "example_v1_generated_Squid_Ramshorn_sync",
                    "description": "Snippet for ramshorn",
                },
                {
                    "rpc": "Ramshorn",
                    "transport": "grpc-async",
                    "service": "animalia.mollusca.v1.Squid",
                    "region_tag": "example_v1_generated_Squid_Ramshorn_async",
                    "description": "Snippet for ramshorn",
                },
            ],
        ),
        (
            "transport=rest",
            [
                {
                    "rpc": "Ramshorn",
                    "transport": "rest",
                    "service": "animalia.mollusca.v1.Squid",
                    "region_tag": "example_v1_generated_Squid_Ramshorn_sync",
                    "description": "Snippet for ramshorn",
                }
            ],
        ),
    ],
)
def test_generate_sample_spec_basic(opts_transport, expected):
    service_options = descriptor_pb2.ServiceOptions()
    service_options.Extensions[client_pb2.default_host] = "example.googleapis.com"

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
                        options=service_options,
                        method=[
                            descriptor_pb2.MethodDescriptorProto(
                                name="Ramshorn",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                        ],
                    ),
                ],
            )
        ]
    )
    opts = Options.build(opts_transport)
    specs = sorted(
        samplegen.generate_sample_specs(api_schema, opts=opts),
        key=lambda x: x["transport"],
    )
    specs.sort(key=lambda x: x["transport"])
    assert specs == expected


def test_generate_sample_spec_internal_method():
    service_options = descriptor_pb2.ServiceOptions()
    service_options.Extensions[client_pb2.default_host] = "example.googleapis.com"

    file_descriptors = [
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
                    options=service_options,
                    method=[
                        descriptor_pb2.MethodDescriptorProto(
                            name="Ramshorn",
                            input_type="animalia.mollusca.v1.MolluscRequest",
                            output_type="animalia.mollusca.v1.Mollusc",
                        ),
                        descriptor_pb2.MethodDescriptorProto(
                            name="NotRamshorn",
                            input_type="animalia.mollusca.v1.MolluscRequest",
                            output_type="animalia.mollusca.v1.Mollusc",
                        ),
                    ],
                ),
                descriptor_pb2.ServiceDescriptorProto(
                    name="Octopus",
                    options=service_options,
                    method=[
                        descriptor_pb2.MethodDescriptorProto(
                            name="Bighead",
                            input_type="animalia.mollusca.v1.MolluscRequest",
                            output_type="animalia.mollusca.v1.Mollusc",
                        ),
                    ],
                ),
            ],
        )
    ]

    # The internal method should be animalia.mollusca.v1.Squid.NotRamshorn
    service_yaml = {
        "apis": [{"name": "animalia.mollusca.v1"}],
        "publishing": {
            "library_settings": [
                {
                    "version": "animalia.mollusca.v1",
                    "python_settings": {
                        "experimental_features": {"rest_async_io_enabled": True},
                        "common": {
                            "selective_gapic_generation": {
                                "methods": [
                                    "animalia.mollusca.v1.Squid.Ramshorn",
                                    "animalia.mollusca.v1.Octopus.Bighead",
                                ],
                                "generate_omitted_as_internal": True,
                            }
                        },
                    },
                }
            ]
        },
    }

    api_opts = Options(service_yaml_config=service_yaml)

    api_schema = api.API.build(file_descriptors, "animalia.mollusca.v1", opts=api_opts)

    samplegen_opts = Options.build("transport=rest")

    specs = sorted(
        samplegen.generate_sample_specs(api_schema, opts=samplegen_opts),
        key=lambda x: x["rpc"],
    )
    specs.sort(key=lambda x: x["rpc"])

    expected_specs = [
        {
            "rpc": "Bighead",
            "transport": "rest",
            "service": "animalia.mollusca.v1.Octopus",
            "region_tag": "example_v1_generated_Octopus_Bighead_sync",
            "description": "Snippet for bighead",
        },
        {
            "rpc": "NotRamshorn",
            "transport": "rest",
            "service": "animalia.mollusca.v1.Squid",
            "region_tag": "example_v1_generated_Squid_NotRamshorn_sync_internal",
            "description": "Snippet for not_ramshorn",
        },
        {
            "rpc": "Ramshorn",
            "transport": "rest",
            "service": "animalia.mollusca.v1.Squid",
            "region_tag": "example_v1_generated_Squid_Ramshorn_sync",
            "description": "Snippet for ramshorn",
        },
    ]

    assert specs == expected_specs


def test__set_sample_metadata_server_streaming():
    sample = {
        "rpc": "Ramshorn",
        "transport": "grpc",
        "service": "animalia.mollusca.v1.Squid",
        "region_tag": "example_v1_generated_Squid_Ramshorn_sync",
        "description": "Snippet for ramshorn",
        "module_namespace": ["animalia"],
        "module_name": "mollusca_v1",
    }

    service_options = descriptor_pb2.ServiceOptions()
    service_options.Extensions[client_pb2.default_host] = "example.googleapis.com"

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
                        options=service_options,
                        method=[
                            descriptor_pb2.MethodDescriptorProto(
                                server_streaming=True,
                                name="Ramshorn",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                        ],
                    ),
                ],
            )
        ]
    )

    snippet_metadata = samplegen._fill_sample_metadata(sample, api_schema)

    assert json_format.MessageToDict(snippet_metadata) == {
        "regionTag": "example_v1_generated_Squid_Ramshorn_sync",
        "description": "Sample for Ramshorn",
        "language": "PYTHON",
        "clientMethod": {
            "shortName": "ramshorn",
            "fullName": "animalia.mollusca_v1.SquidClient.ramshorn",
            "parameters": [
                {
                    "type": "animalia.mollusca_v1.types.MolluscRequest",
                    "name": "request",
                },
                {"type": "google.api_core.retry.Retry", "name": "retry"},
                {"type": "float", "name": "timeout"},
                {"type": "Sequence[Tuple[str, Union[str, bytes]]]", "name": "metadata"},
            ],
            "resultType": "Iterable[animalia.mollusca_v1.types.Mollusc]",
            "client": {
                "shortName": "SquidClient",
                "fullName": "animalia.mollusca_v1.SquidClient",  # FIX THE FULL NAME
            },
            "method": {
                "shortName": "Ramshorn",
                "fullName": "animalia.mollusca.v1.Squid.Ramshorn",
                "service": {
                    "shortName": "Squid",
                    "fullName": "animalia.mollusca.v1.Squid",
                },
            },
        },
        "canonical": True,
        "origin": "API_DEFINITION",
    }


def test__set_sample_metadata_client_streaming():
    sample = {
        "rpc": "Ramshorn",
        "transport": "grpc",
        "service": "animalia.mollusca.v1.Squid",
        "region_tag": "example_v1_generated_Squid_Ramshorn_sync",
        "description": "Snippet for ramshorn",
        "module_namespace": ["animalia"],
        "module_name": "mollusca_v1",
    }

    service_options = descriptor_pb2.ServiceOptions()
    service_options.Extensions[client_pb2.default_host] = "example.googleapis.com"

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
                        options=service_options,
                        method=[
                            descriptor_pb2.MethodDescriptorProto(
                                client_streaming=True,
                                name="Ramshorn",
                                input_type="animalia.mollusca.v1.MolluscRequest",
                                output_type="animalia.mollusca.v1.Mollusc",
                            ),
                        ],
                    ),
                ],
            )
        ]
    )

    snippet_metadata = samplegen._fill_sample_metadata(sample, api_schema)

    print(json_format.MessageToDict(snippet_metadata))

    assert json_format.MessageToDict(snippet_metadata) == {
        "regionTag": "example_v1_generated_Squid_Ramshorn_sync",
        "description": "Sample for Ramshorn",
        "language": "PYTHON",
        "clientMethod": {
            "shortName": "ramshorn",
            "fullName": "animalia.mollusca_v1.SquidClient.ramshorn",
            "parameters": [
                {
                    "type": "Iterator[animalia.mollusca_v1.types.MolluscRequest]",
                    "name": "requests",
                },
                {"type": "google.api_core.retry.Retry", "name": "retry"},
                {"type": "float", "name": "timeout"},
                {"type": "Sequence[Tuple[str, Union[str, bytes]]]", "name": "metadata"},
            ],
            "resultType": "animalia.mollusca_v1.types.Mollusc",
            "client": {
                "shortName": "SquidClient",
                "fullName": "animalia.mollusca_v1.SquidClient",
            },
            "method": {
                "shortName": "Ramshorn",
                "fullName": "animalia.mollusca.v1.Squid.Ramshorn",
                "service": {
                    "shortName": "Squid",
                    "fullName": "animalia.mollusca.v1.Squid",
                },
            },
        },
        "canonical": True,
        "origin": "API_DEFINITION",
    }


def make_message(
    name: str,
    package: str = "animalia.mollusca.v1",
    module: str = "cephalopoda",
    fields: Sequence[wrappers.Field] = (),
    meta: metadata.Metadata = None,
    options: descriptor_pb2.MethodOptions = None,
) -> wrappers.MessageType:
    message_pb = descriptor_pb2.DescriptorProto(
        name=name,
        field=[i.field_pb for i in fields],
        options=options,
    )
    return wrappers.MessageType(
        message_pb=message_pb,
        fields=OrderedDict((i.name, i) for i in fields),
        nested_messages={},
        nested_enums={},
        meta=meta
        or metadata.Metadata(
            address=metadata.Address(
                name=name,
                package=tuple(package.split(".")),
                module=module,
            )
        ),
    )


# Borrowed from test_field.py
def make_field(*, message=None, enum=None, **kwargs) -> wrappers.Field:
    T = descriptor_pb2.FieldDescriptorProto.Type
    kwargs.setdefault("name", "my_field")
    kwargs.setdefault("number", 1)
    kwargs.setdefault("type", T.Value("TYPE_BOOL"))
    if isinstance(kwargs["type"], str):
        kwargs["type"] = T.Value(kwargs["type"])
    field_pb = descriptor_pb2.FieldDescriptorProto(**kwargs)
    return wrappers.Field(field_pb=field_pb, message=message, enum=enum)
