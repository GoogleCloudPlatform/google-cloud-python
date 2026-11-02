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

from pathlib import Path

from google.protobuf import json_format
from google.protobuf.compiler import plugin_pb2
import libcst
import pytest

from gapic import utils
from gapic.configurable_snippetgen import configured_snippet
from gapic.configurable_snippetgen import snippet_config_language_pb2
from gapic.schema import api


CURRENT_DIRECTORY = Path(__file__).parent.absolute()
SPEECH_V1_REQUEST_PATH = CURRENT_DIRECTORY / "resources" / "speech" / "request.desc"
CONFIG_JSON_PATH = (
    CURRENT_DIRECTORY / "resources" / "speech" / "speech_createCustomClass.json"
)


def _load_api_schema(request_path: Path) -> api.API:
    with open(request_path, "rb") as f:
        request_bytes = f.read()

    req = plugin_pb2.CodeGeneratorRequest.FromString(request_bytes)

    # From gapic/cli/generator.py.
    opts = utils.Options.build(req.parameter)
    api_schema = api.API.build(
        req.proto_file,
        opts=opts,
        package="google.cloud.speech.v1",
    )

    return api_schema


def _load_snippet_config(
    config_path: Path,
) -> snippet_config_language_pb2.SnippetConfig:
    with open(config_path, "r") as f:
        config_json = f.read()

    snippet_config = json_format.Parse(
        config_json, snippet_config_language_pb2.SnippetConfig()
    )

    return snippet_config


def _make_configured_snippet(
    request_path: Path = SPEECH_V1_REQUEST_PATH,
    config_path: Path = CONFIG_JSON_PATH,
    api_version: str = "v1",
    is_sync: bool = True,
) -> configured_snippet.ConfiguredSnippet:
    api_schema = _load_api_schema(request_path)
    snippet_config = _load_snippet_config(config_path)
    return configured_snippet.ConfiguredSnippet(
        api_schema, snippet_config, api_version, is_sync
    )


@pytest.fixture
def snippet():
    return _make_configured_snippet()


@pytest.fixture
def snippet_without_endpoint():
    snippet = _make_configured_snippet()
    snippet.config.snippet.service_client_initialization.ClearField(
        "custom_service_endpoint"
    )
    return snippet


@pytest.fixture
def snippet_bidi_streaming():
    snippet = _make_configured_snippet()
    snippet.config.snippet.ClearField("standard")
    snippet.config.snippet.bidi_streaming.CopyFrom(
        snippet_config_language_pb2.Snippet.BidiStreaming()
    )
    return snippet


def test_gapic_module_name(snippet):
    assert snippet.gapic_module_name == "speech_v1"


@pytest.mark.parametrize(
    "is_sync,expected",
    [
        (True, "speech_v1_config_Adaptation_CreateCustomClass_Basic_sync"),
        (False, "speech_v1_config_Adaptation_CreateCustomClass_Basic_async"),
    ],
)
def test_region_tag(is_sync, expected):
    snippet = _make_configured_snippet(is_sync=is_sync)
    assert snippet.region_tag == expected


def test_sample_function_name(snippet):
    assert snippet.sample_function_name == "sample_create_custom_class_Basic"


@pytest.mark.parametrize(
    "is_sync,expected",
    [
        (True, "AdaptationClient"),
        (False, "AdaptationAsyncClient"),
    ],
)
def test_client_class_name(is_sync, expected):
    snippet = _make_configured_snippet(is_sync=is_sync)
    assert snippet.client_class_name == expected


@pytest.mark.parametrize(
    "is_sync,expected",
    [
        (True, "speech_v1_generated_Adaptation_create_custom_class_Basic_sync.py"),
        (False, "speech_v1_generated_Adaptation_create_custom_class_Basic_async.py"),
    ],
)
def test_filename(is_sync, expected):
    snippet = _make_configured_snippet(is_sync=is_sync)
    assert snippet.filename == expected


@pytest.mark.parametrize(
    "custom_service_endpoint_dict,expected",
    [
        (
            {
                "region": "us",
                "port": 123,
                "schema": "HTTP",
            },
            None,  # host is missing.
        ),
        (
            {
                "host": "speech.googleapis.com",
            },
            "speech.googleapis.com",
        ),
        (
            {
                "host": "speech.googleapis.com",
                "region": "us",
            },
            "us-speech.googleapis.com",
        ),
        (
            {
                "host": "speech.googleapis.com",
                "region": "us",
                "port": 123,
            },
            "us-speech.googleapis.com:123",
        ),
        (
            {
                "host": "speech.googleapis.com",
                "region": "us",
                "port": 123,
                "schema": "HTTP",
            },
            "http://us-speech.googleapis.com:123",
        ),
        (
            {
                "host": "speech.googleapis.com",
                "schema": "HTTPS",
            },
            "speech.googleapis.com",
        ),
    ],
)
def test_api_endpoint(custom_service_endpoint_dict, expected):
    # api_schema, api_version, and is_sync do not matter here.
    api_schema = _load_api_schema(SPEECH_V1_REQUEST_PATH)
    api_version = "v1"
    is_sync = True

    snippet_config_dict = {
        "snippet": {
            "serviceClientInitialization": {
                "customServiceEndpoint": custom_service_endpoint_dict
            },
        }
    }

    snippet_config = json_format.ParseDict(
        snippet_config_dict, snippet_config_language_pb2.SnippetConfig()
    )
    snippet = configured_snippet.ConfiguredSnippet(
        api_schema, snippet_config, api_version, is_sync
    )
    assert snippet.api_endpoint == expected


@pytest.mark.parametrize(
    "is_sync,expected",
    [
        (True, "speech_v1_generated_Adaptation_create_custom_class_Basic_sync.py"),
        (False, "speech_v1_generated_Adaptation_create_custom_class_Basic_async.py"),
    ],
)
def test_filename(is_sync, expected):
    snippet = _make_configured_snippet(is_sync=is_sync)
    assert snippet.filename == expected


def test_AppendToSampleFunctionBody():
    # Start with a function def with nonempty body to we can be sure the
    # transformer appends the statement.
    function_def = libcst.parse_statement("def f():\n    'hello'")
    statement = libcst.parse_statement("'world'")
    transformer = configured_snippet._AppendToSampleFunctionBody(statement)
    updated_function_def = function_def.visit(transformer)
    expected_function_def = libcst.parse_statement("def f():\n    'hello'\n    'world'")
    assert updated_function_def.deep_equals(expected_function_def)


def test_AppendToSampleFunctionBody():
    # Start with a function def with nonempty body to we can be sure the
    # transformer appends the statement.
    function_def = libcst.parse_statement("def f():\n    'hello'")
    statement = libcst.parse_statement("'world'")
    transformer = configured_snippet._AppendToSampleFunctionBody(statement)
    updated_function_def = function_def.visit(transformer)
    expected_function_def = libcst.parse_statement("def f():\n    'hello'\n    'world'")
    assert updated_function_def.deep_equals(expected_function_def)


def test_code(snippet):
    snippet.generate()

    # https://github.com/googleapis/gapic-generator-python/issues/1522
    # Placeholder code.  We will gradually add to the ConfiguredSnippet class
    # until the generated code is the same as that of the golden file.
    expected_code = """def sample_create_custom_class_Basic(parent = "projects/[PROJECT]/locations/us", custom_class_id = "passengerships"):
    \"\"
    client = speech_v1.AdaptationClient(client_options = {"api_endpoint": "us-speech.googleapis.com"})
"""
    assert snippet.code == expected_code


def test_code_without_endpoint(snippet_without_endpoint):
    snippet_without_endpoint.generate()

    # https://github.com/googleapis/gapic-generator-python/issues/1522
    expected_code = """def sample_create_custom_class_Basic(parent = "projects/[PROJECT]/locations/us", custom_class_id = "passengerships"):
    \"\"
    client = speech_v1.AdaptationClient()
"""
    assert snippet_without_endpoint.code == expected_code


def test_generate_should_raise_error_if_unsupported(snippet_bidi_streaming):
    with pytest.raises(ValueError):
        snippet_bidi_streaming.generate()
