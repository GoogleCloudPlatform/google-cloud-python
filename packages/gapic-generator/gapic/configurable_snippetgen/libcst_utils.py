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

from typing import Sequence, Tuple

import libcst

from gapic.configurable_snippetgen import snippet_config_language_pb2


def empty_module() -> libcst.Module:
    return libcst.Module(body=[])


def base_function_def(function_name: str, is_sync: bool) -> libcst.FunctionDef:
    """Returns a FunctionDef node with a placeholder docstring."""
    params = libcst.Parameters(params=[])
    body = libcst.IndentedBlock(body=[libcst.parse_statement('""')])
    asynchronous = None if is_sync else libcst.Asynchronous()
    function_def = libcst.FunctionDef(
        name=libcst.Name(value=function_name),
        params=params,
        body=body,
        asynchronous=asynchronous,
    )

    return function_def


def convert_expression(
    config_expression: snippet_config_language_pb2.Expression,
) -> libcst.BaseExpression:
    value_name = config_expression.WhichOneof("value")
    if value_name == "string_value":
        string_value = config_expression.string_value
        return libcst.SimpleString(value=f'"{string_value}"')
    else:
        raise ValueError(f"Conversion from Expression value {value_name} unsupported.")


def convert_parameter(
    config_parameter: snippet_config_language_pb2.Statement.Declaration,
) -> libcst.Param:
    # TODO: https://github.com/googleapis/gapic-generator-python/issues/1537, add typing annotation in sample function parameters.
    param = libcst.Param(
        name=libcst.Name(value=config_parameter.name),
        default=convert_expression(config_parameter.value),
    )
    return param


def convert_py_dict(key_value_pairs: Sequence[Tuple[str, str]]) -> libcst.Dict:
    elements = []
    for key, value in key_value_pairs:
        if not (isinstance(key, str) and isinstance(value, str)):
            raise ValueError(f"convert_py_dict supports only string keys and values.")
        elements.append(
            libcst.DictElement(
                libcst.SimpleString(f'"{key}"'), libcst.SimpleString(f'"{value}"')
            )
        )
    return libcst.Dict(elements=elements)
