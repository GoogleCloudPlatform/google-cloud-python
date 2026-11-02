# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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

import libcst
import pytest

from gapic.configurable_snippetgen import libcst_utils
from gapic.configurable_snippetgen import snippet_config_language_pb2


def _assert_code_equal(node: libcst.CSTNode, code: str) -> str:
    assert libcst.Module(body=[node]).code == code


@pytest.mark.parametrize(
    "is_sync,expected_code",
    [
        (True, 'def some_function():\n    ""\n'),
        (False, 'async def some_function():\n    ""\n'),
    ],
)
def test_base_function_def(is_sync, expected_code):
    node = libcst_utils.base_function_def("some_function", is_sync)

    expected_node = libcst.parse_statement(expected_code)

    # Whenever possible we try to control the shape of the nodes,
    # because we will be manipulating them during snippet generation.
    assert node.deep_equals(expected_node), (node, expected_node)

    # Sometimes it is more convenient to just verify the code.
    _assert_code_equal(node, expected_code)


def test_convert_expression_string_value():
    config_expression = snippet_config_language_pb2.Expression(
        string_value="hello world"
    )
    node = libcst_utils.convert_expression(config_expression)
    expected_node = libcst.SimpleString(value='"hello world"')

    assert node.deep_equals(expected_node), (node, expected_node)


def test_convert_expression_should_raise_error_if_unsupported():
    config_expression = snippet_config_language_pb2.Expression(
        default_value=snippet_config_language_pb2.Expression.DefaultValue.DEFAULT_VALUE
    )
    with pytest.raises(ValueError):
        libcst_utils.convert_expression(config_expression)


def test_convert_parameter():
    config_parameter = snippet_config_language_pb2.Statement.Declaration(
        name="some_variable",
        value=snippet_config_language_pb2.Expression(string_value="hello world"),
    )
    node = libcst_utils.convert_parameter(config_parameter)
    expected_node = libcst.Param(
        name=libcst.Name(value="some_variable"),
        default=libcst.SimpleString(value='"hello world"'),
    )

    assert node.deep_equals(expected_node), (node, expected_node)


def test_convert_py_dict():
    key_value_pairs = [("key1", "value1"), ("key2", "value2")]
    node = libcst_utils.convert_py_dict(key_value_pairs)
    expected_node = libcst.Dict(
        [
            libcst.DictElement(
                libcst.SimpleString('"key1"'), libcst.SimpleString('"value1"')
            ),
            libcst.DictElement(
                libcst.SimpleString('"key2"'), libcst.SimpleString('"value2"')
            ),
        ]
    )

    assert node.deep_equals(expected_node), (node, expected_node)


def test_convert_py_dict_should_raise_error_if_unsupported():
    key_value_pairs = [("key1", 5)]
    with pytest.raises(ValueError):
        libcst_utils.convert_py_dict(key_value_pairs)
