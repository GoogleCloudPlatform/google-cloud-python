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

import jinja2
import os.path as path
import pytest
from pathlib import Path

from google.protobuf import json_format

import gapic.utils as utils

from gapic.samplegen import samplegen
from gapic.samplegen_utils import types, utils as gapic_utils
from gapic.samplegen_utils import snippet_metadata_pb2
from gapic.schema import naming, wrappers

from ..common_types import (
    DummyField,
    DummyMessage,
    DummyMessageTypePB,
    DummyMethod,
    DummyService,
    DummyIdent,
    DummyApiSchema,
    DummyNaming,
    enum_factory,
    message_factory,
)

from collections import namedtuple
from textwrap import dedent


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        searchpath=path.realpath(
            path.join(path.dirname(__file__), "..", "..", "..", "gapic", "templates")
        )
    ),
    undefined=jinja2.StrictUndefined,
    extensions=["jinja2.ext.do"],
    trim_blocks=True,
    lstrip_blocks=True,
)
env.filters["snake_case"] = utils.to_snake_case
env.filters["coerce_response_name"] = gapic_utils.coerce_response_name
env.filters["render_format_string"] = gapic_utils.render_format_string


def golden_snippet(filename: str) -> str:
    """Load the golden snippet with the name provided"""
    snippet_path = Path(__file__).parent / "golden_snippets" / filename
    return snippet_path.read_text()


def test_generate_sample_basic():
    # Note: the sample integration tests are needfully large
    # and difficult to eyeball parse. They are intended to be integration tests
    # that catch errors in behavior that is emergent from combining smaller features
    # or in features that are sufficiently small and trivial that it doesn't make sense
    # to have standalone tests.

    classify_target_field = DummyField(
        name="classify_target",
        type=DummyMessageTypePB(name="ClassifyTarget"),
        message=DummyMessage(
            type="CLASSIFY TYPE",
            fields={
                "video": DummyField(
                    type=DummyMessageTypePB(name="Video"),
                    message=DummyMessage(type="VIDEO TYPE"),
                ),
                "location_annotation": DummyField(
                    type=DummyMessageTypePB(name="Location"),
                    message=DummyMessage(type="LOCATION TYPE"),
                ),
            },
        ),
        ident=DummyIdent(sphinx="molluscs_v1.ClassifyTarget"),
    )

    input_type = DummyMessage(
        type="REQUEST TYPE",
        fields={"classify_target": classify_target_field},
        ident=DummyIdent(
            name="molluscs.v1.ClassifyRequest", sphinx="molluscs_v1.classify_request"
        ),
    )

    output_type = DummyMessage(
        type="RESPONSE TYPE",
        fields={
            "classification": DummyField(
                type=DummyMessageTypePB(name="Classification"),
            )
        },
        ident=DummyIdent(sphinx="molluscs_v1.classification"),
    )

    api_naming = naming.NewNaming(name="MolluscClient", namespace=("molluscs", "v1"))
    service = wrappers.Service(
        service_pb=namedtuple("service_pb", ["name"])("MolluscService"),
        methods={
            "Classify": DummyMethod(
                name="Classify",
                input=input_type,
                output=message_factory("$resp.taxonomy"),
                client_output=output_type,
                flattened_fields={"classify_target": classify_target_field},
            )
        },
        visible_resources={},
    )

    schema = DummyApiSchema(
        services={"animalia.mollusca.v1.Mollusc": service},
        naming=api_naming,
    )

    sample = {
        "service": "animalia.mollusca.v1.Mollusc",
        "region_tag": "molluscs_generated_molluscs_v1_Mollusc_Classify_sync",
        "rpc": "Classify",
        "id": "mollusc_classify_sync",
        "description": "Determine the full taxonomy of input mollusc",
        "request": [
            {
                "field": "classify_target.video",
                "value": "path/to/mollusc/video.mkv",
                "input_parameter": "video",
                "value_is_file": True,
            },
            {
                "field": "classify_target.location_annotation",
                "value": "New Zealand",
                "input_parameter": "location",
            },
        ],
        "response": [{"print": ['Mollusc is a "%s"', "$resp.taxonomy"]}],
    }

    sample_str, metadata = samplegen.generate_sample(
        sample, schema, env.get_template("examples/sample.py.j2")
    )

    assert sample_str == golden_snippet("sample_basic.py")

    assert json_format.MessageToDict(metadata) == {
        "regionTag": "molluscs_generated_molluscs_v1_Mollusc_Classify_sync",
        "description": "Sample for Classify",
        "language": "PYTHON",
        "clientMethod": {
            "shortName": "classify",
            "fullName": "molluscs.v1.molluscclient.MolluscServiceClient.classify",
            "parameters": [
                {"type": "molluscs_v1.classify_request", "name": "request"},
                {"type": "molluscs_v1.ClassifyTarget", "name": "classify_target"},
                {"type": "google.api_core.retry.Retry", "name": "retry"},
                {"type": "float", "name": "timeout"},
                {"type": "Sequence[Tuple[str, Union[str, bytes]]]", "name": "metadata"},
            ],
            "resultType": "molluscs_v1.classification",
            "client": {
                "shortName": "MolluscServiceClient",
                "fullName": "molluscs.v1.molluscclient.MolluscServiceClient",
            },
            "method": {
                "shortName": "Classify",
                "fullName": ".MolluscService.Classify",
                "service": {
                    "shortName": "MolluscService",
                    "fullName": ".MolluscService",
                },
            },
        },
        "canonical": True,
        "origin": "API_DEFINITION",
    }


def test_generate_sample_basic_async():
    # Note: the sample integration tests are needfully large
    # and difficult to eyeball parse. They are intended to be integration tests
    # that catch errors in behavior that is emergent from combining smaller features
    # or in features that are sufficiently small and trivial that it doesn't make sense
    # to have standalone tests.

    classify_target_field = DummyField(
        name="classify_target",
        type=DummyMessageTypePB(name="ClassifyTarget"),
        message=DummyMessage(
            type="CLASSIFY TYPE",
            fields={
                "video": DummyField(
                    type=DummyMessageTypePB(name="Video"),
                    message=DummyMessage(type="VIDEO TYPE"),
                ),
                "location_annotation": DummyField(
                    type=DummyMessageTypePB(name="Location"),
                    message=DummyMessage(type="LOCATION TYPE"),
                ),
            },
        ),
        ident=DummyIdent(sphinx="molluscs_v1.ClassifyTarget"),
    )

    input_type = DummyMessage(
        type="REQUEST TYPE",
        fields={"classify_target": classify_target_field},
        ident=DummyIdent(
            name="molluscs.v1.ClassifyRequest", sphinx="molluscs_v1.classify_request"
        ),
    )

    output_type = DummyMessage(
        type="RESPONSE TYPE",
        fields={
            "classification": DummyField(
                type=DummyMessageTypePB(name="Classification"),
            )
        },
        ident=DummyIdent(sphinx="molluscs_v1.classification"),
    )

    api_naming = naming.NewNaming(name="MolluscClient", namespace=("molluscs", "v1"))
    service = wrappers.Service(
        service_pb=namedtuple("service_pb", ["name"])("MolluscService"),
        methods={
            "Classify": DummyMethod(
                name="Classify",
                input=input_type,
                output=message_factory("$resp.taxonomy"),
                client_output_async=output_type,
                client_output=output_type,
                flattened_fields={"classify_target": classify_target_field},
            )
        },
        visible_resources={},
    )

    schema = DummyApiSchema(
        services={"animalia.mollusca.v1.Mollusc": service},
        naming=api_naming,
    )

    sample = {
        "service": "animalia.mollusca.v1.Mollusc",
        "region_tag": "molluscs_generated_molluscs_v1_Mollusc_Classify_async",
        "rpc": "Classify",
        "transport": "grpc-async",
        "id": "mollusc_classify_sync",
        "description": "Determine the full taxonomy of input mollusc",
        "request": [
            {
                "field": "classify_target.video",
                "value": "path/to/mollusc/video.mkv",
                "input_parameter": "video",
                "value_is_file": True,
            },
            {
                "field": "classify_target.location_annotation",
                "value": "New Zealand",
                "input_parameter": "location",
            },
        ],
        "response": [{"print": ['Mollusc is a "%s"', "$resp.taxonomy"]}],
    }

    sample_str, metadata = samplegen.generate_sample(
        sample, schema, env.get_template("examples/sample.py.j2")
    )

    assert sample_str == golden_snippet("sample_basic_async.py")

    assert json_format.MessageToDict(metadata) == {
        "regionTag": "molluscs_generated_molluscs_v1_Mollusc_Classify_async",
        "description": "Sample for Classify",
        "language": "PYTHON",
        "clientMethod": {
            "shortName": "classify",
            "fullName": "molluscs.v1.molluscclient.MolluscServiceAsyncClient.classify",
            "async": True,
            "parameters": [
                {"type": "molluscs_v1.classify_request", "name": "request"},
                {"type": "molluscs_v1.ClassifyTarget", "name": "classify_target"},
                {"type": "google.api_core.retry.Retry", "name": "retry"},
                {"type": "float", "name": "timeout"},
                {"type": "Sequence[Tuple[str, Union[str, bytes]]]", "name": "metadata"},
            ],
            "resultType": "molluscs_v1.classification",
            "client": {
                "shortName": "MolluscServiceAsyncClient",
                "fullName": "molluscs.v1.molluscclient.MolluscServiceAsyncClient",
            },
            "method": {
                "shortName": "Classify",
                "fullName": ".MolluscService.Classify",
                "service": {
                    "shortName": "MolluscService",
                    "fullName": ".MolluscService",
                },
            },
        },
        "canonical": True,
        "origin": "API_DEFINITION",
    }


def test_generate_sample_basic_unflattenable():
    # Note: the sample integration tests are needfully large
    # and difficult to eyeball parse. They are intended to be integration tests
    # that catch errors in behavior that is emergent from combining smaller features
    # or in features that are sufficiently small and trivial that it doesn't make sense
    # to have standalone tests.
    input_type = DummyMessage(
        type="REQUEST TYPE",
        fields={
            "classify_target": DummyField(
                type=DummyMessageTypePB(name="ClassifyTarget"),
                message=DummyMessage(
                    fields={
                        "video": DummyField(
                            type=DummyMessageTypePB(name="Video"),
                            message=DummyMessage(type="VIDEO TYPE"),
                        ),
                        "location_annotation": DummyField(
                            type=DummyMessageTypePB(name="Location"),
                            message=DummyMessage(type="LOCATION TYPE"),
                        ),
                    },
                ),
            )
        },
        ident=DummyIdent(
            name="molluscs.v1.ClassifyRequest", sphinx="molluscs_v1.classify_request"
        ),
    )

    output_type = DummyMessage(
        type="RESPONSE TYPE",
        fields={
            "classification": DummyField(
                type=DummyMessageTypePB(name="Classification"),
            )
        },
        ident=DummyIdent(sphinx="molluscs_v1.classification"),
    )

    api_naming = naming.NewNaming(name="MolluscClient", namespace=("molluscs", "v1"))
    service = wrappers.Service(
        service_pb=namedtuple("service_pb", ["name"])("MolluscService"),
        methods={
            "Classify": DummyMethod(
                name="Classify",
                input=input_type,
                output=message_factory("$resp.taxonomy"),
                client_output=output_type,
            )
        },
        visible_resources={},
    )

    schema = DummyApiSchema(
        services={"animalia.mollusca.v1.Mollusc": service},
        naming=api_naming,
    )

    sample = {
        "service": "animalia.mollusca.v1.Mollusc",
        "region_tag": "molluscs_generated_molluscs_v1_Mollusc_Classify_sync",
        "rpc": "Classify",
        "id": "mollusc_classify_sync",
        "description": "Determine the full taxonomy of input mollusc",
        "request": [
            {
                "field": "classify_target.video",
                "value": "path/to/mollusc/video.mkv",
                "input_parameter": "video",
                "value_is_file": True,
            },
            {
                "field": "classify_target.location_annotation",
                "value": "New Zealand",
                "input_parameter": "location",
            },
        ],
        "response": [{"print": ['Mollusc is a "%s"', "$resp.taxonomy"]}],
    }

    sample_str, metadata = samplegen.generate_sample(
        sample, schema, env.get_template("examples/sample.py.j2")
    )

    assert sample_str == golden_snippet("sample_basic_unflattenable.py")

    assert json_format.MessageToDict(metadata) == {
        "regionTag": "molluscs_generated_molluscs_v1_Mollusc_Classify_sync",
        "description": "Sample for Classify",
        "language": "PYTHON",
        "clientMethod": {
            "shortName": "classify",
            "fullName": "molluscs.v1.molluscclient.MolluscServiceClient.classify",
            "parameters": [
                {"type": "molluscs_v1.classify_request", "name": "request"},
                {"type": "google.api_core.retry.Retry", "name": "retry"},
                {"type": "float", "name": "timeout"},
                {"type": "Sequence[Tuple[str, Union[str, bytes]]]", "name": "metadata"},
            ],
            "resultType": "molluscs_v1.classification",
            "client": {
                "shortName": "MolluscServiceClient",
                "fullName": "molluscs.v1.molluscclient.MolluscServiceClient",
            },
            "method": {
                "shortName": "Classify",
                "fullName": ".MolluscService.Classify",
                "service": {
                    "shortName": "MolluscService",
                    "fullName": ".MolluscService",
                },
            },
        },
        "canonical": True,
        "origin": "API_DEFINITION",
    }


def test_generate_sample_void_method():
    classify_target_field = DummyField(
        name="classify_target",
        type=DummyMessageTypePB(name="ClassifyTarget"),
        message=DummyMessage(
            type="CLASSIFY TYPE",
            fields={
                "video": DummyField(
                    type=DummyMessageTypePB(name="Video"),
                    message=DummyMessage(type="VIDEO TYPE"),
                ),
                "location_annotation": DummyField(
                    type=DummyMessageTypePB(name="Location"),
                    message=DummyMessage(type="LOCATION TYPE"),
                ),
            },
        ),
        ident=DummyIdent(sphinx="molluscs_v1.ClassifyTarget"),
    )

    input_type = DummyMessage(
        type="REQUEST TYPE",
        fields={"classify_target": classify_target_field},
        ident=DummyIdent(
            name="molluscs.v1.ClassifyRequest", sphinx="molluscs_v1.classify_request"
        ),
    )

    api_naming = naming.NewNaming(name="MolluscClient", namespace=("molluscs", "v1"))
    service = wrappers.Service(
        service_pb=namedtuple("service_pb", ["name"])("MolluscService"),
        methods={
            "Classify": DummyMethod(
                name="Classify",
                client_output=DummyIdent(name="classify", sphinx="classify"),
                void=True,
                input=input_type,
                output=message_factory("$resp.taxonomy"),
                flattened_fields={
                    "classify_target": classify_target_field,
                },
            )
        },
        visible_resources={},
    )

    schema = DummyApiSchema(
        services={"animalia.mollusca.v1.Mollusc": service},
        naming=api_naming,
    )

    sample = {
        "service": "animalia.mollusca.v1.Mollusc",
        "region_tag": "molluscs_generated_molluscs_v1_Mollusc_Classify_sync",
        "rpc": "Classify",
        "id": "mollusc_classify_sync",
        "description": "Determine the full taxonomy of input mollusc",
        "request": [
            {
                "field": "classify_target.video",
                "value": "path/to/mollusc/video.mkv",
                "input_parameter": "video",
                "value_is_file": True,
            },
            {
                "field": "classify_target.location_annotation",
                "value": "New Zealand",
                "input_parameter": "location",
            },
        ],
    }

    sample_str, metadata = samplegen.generate_sample(
        sample, schema, env.get_template("examples/sample.py.j2")
    )

    assert sample_str == golden_snippet("sample_basic_void_method.py")

    assert json_format.MessageToDict(metadata) == {
        "regionTag": "molluscs_generated_molluscs_v1_Mollusc_Classify_sync",
        "description": "Sample for Classify",
        "language": "PYTHON",
        "clientMethod": {
            "shortName": "classify",
            "fullName": "molluscs.v1.molluscclient.MolluscServiceClient.classify",
            "parameters": [
                {"type": "molluscs_v1.classify_request", "name": "request"},
                {"type": "molluscs_v1.ClassifyTarget", "name": "classify_target"},
                {"type": "google.api_core.retry.Retry", "name": "retry"},
                {"type": "float", "name": "timeout"},
                {"type": "Sequence[Tuple[str, Union[str, bytes]]]", "name": "metadata"},
            ],
            "client": {
                "shortName": "MolluscServiceClient",
                "fullName": "molluscs.v1.molluscclient.MolluscServiceClient",
            },
            "method": {
                "shortName": "Classify",
                "fullName": ".MolluscService.Classify",
                "service": {
                    "shortName": "MolluscService",
                    "fullName": ".MolluscService",
                },
            },
        },
        "canonical": True,
        "origin": "API_DEFINITION",
    }


def test_generate_sample_basic_internal():
    # Note: the sample integration tests are needfully large
    # and difficult to eyeball parse. They are intended to be integration tests
    # that catch errors in behavior that is emergent from combining smaller features
    # or in features that are sufficiently small and trivial that it doesn't make sense
    # to have standalone tests.

    classify_target_field = DummyField(
        name="classify_target",
        type=DummyMessageTypePB(name="ClassifyTarget"),
        message=DummyMessage(
            type="CLASSIFY TYPE",
            fields={
                "video": DummyField(
                    type=DummyMessageTypePB(name="Video"),
                    message=DummyMessage(type="VIDEO TYPE"),
                ),
                "location_annotation": DummyField(
                    type=DummyMessageTypePB(name="Location"),
                    message=DummyMessage(type="LOCATION TYPE"),
                ),
            },
        ),
        ident=DummyIdent(sphinx="molluscs_v1.ClassifyTarget"),
    )

    input_type = DummyMessage(
        type="REQUEST TYPE",
        fields={"classify_target": classify_target_field},
        ident=DummyIdent(
            name="molluscs.v1.ClassifyRequest", sphinx="molluscs_v1.classify_request"
        ),
    )

    output_type = DummyMessage(
        type="RESPONSE TYPE",
        fields={
            "classification": DummyField(
                type=DummyMessageTypePB(name="Classification"),
            )
        },
        ident=DummyIdent(sphinx="molluscs_v1.classification"),
    )

    api_naming = naming.NewNaming(name="MolluscClient", namespace=("molluscs", "v1"))
    service = wrappers.Service(
        service_pb=namedtuple("service_pb", ["name"])("MolluscService"),
        methods={
            "Classify": DummyMethod(
                name="Classify",
                input=input_type,
                output=message_factory("$resp.taxonomy"),
                client_output=output_type,
                flattened_fields={"classify_target": classify_target_field},
                is_internal=True,
            )
        },
        visible_resources={},
    )

    schema = DummyApiSchema(
        services={"animalia.mollusca.v1.Mollusc": service},
        naming=api_naming,
    )

    sample = {
        "service": "animalia.mollusca.v1.Mollusc",
        "region_tag": "molluscs_generated_molluscs_v1_Mollusc_Classify_sync_internal",
        "rpc": "Classify",
        "id": "mollusc_classify_sync_internal",
        "description": "Determine the full taxonomy of input mollusc",
        "request": [
            {
                "field": "classify_target.video",
                "value": "path/to/mollusc/video.mkv",
                "input_parameter": "video",
                "value_is_file": True,
            },
            {
                "field": "classify_target.location_annotation",
                "value": "New Zealand",
                "input_parameter": "location",
            },
        ],
        "response": [{"print": ['Mollusc is a "%s"', "$resp.taxonomy"]}],
    }

    sample_str, metadata = samplegen.generate_sample(
        sample, schema, env.get_template("examples/sample.py.j2")
    )

    assert sample_str == golden_snippet("sample_basic_internal.py")

    assert json_format.MessageToDict(metadata) == {
        "regionTag": "molluscs_generated_molluscs_v1_Mollusc_Classify_sync_internal",
        "description": "Sample for Classify",
        "language": "PYTHON",
        "clientMethod": {
            "shortName": "_classify",
            "fullName": "molluscs.v1.molluscclient.BaseMolluscServiceClient._classify",
            "parameters": [
                {"type": "molluscs_v1.classify_request", "name": "request"},
                {"type": "molluscs_v1.ClassifyTarget", "name": "classify_target"},
                {"type": "google.api_core.retry.Retry", "name": "retry"},
                {"type": "float", "name": "timeout"},
                {"type": "Sequence[Tuple[str, Union[str, bytes]]]", "name": "metadata"},
            ],
            "resultType": "molluscs_v1.classification",
            "client": {
                "shortName": "BaseMolluscServiceClient",
                "fullName": "molluscs.v1.molluscclient.BaseMolluscServiceClient",
            },
            "method": {
                "shortName": "Classify",
                "fullName": ".MolluscService.Classify",
                "service": {
                    "shortName": "MolluscService",
                    "fullName": ".MolluscService",
                },
            },
        },
        "canonical": True,
        "origin": "API_DEFINITION",
    }


def test_generate_sample_service_not_found():
    schema = DummyApiSchema({}, DummyNaming("pkg_name"))
    sample = {"service": "Mollusc"}

    with pytest.raises(types.UnknownService):
        samplegen.generate_sample(
            sample,
            schema,
            env.get_template("examples/sample.py.j2"),
        )


def test_generate_sample_rpc_not_found():
    schema = DummyApiSchema(
        {"Mollusc": DummyService(methods={}, client_name="ClassifyClient")},
        DummyNaming("pkg_name"),
    )
    sample = {"service": "Mollusc", "rpc": "Classify"}

    with pytest.raises(types.RpcMethodNotFound):
        list(
            samplegen.generate_sample(
                sample, schema, env.get_template("examples/sample.py.j2")
            ),
        )


def test_generate_sample_config_fpaths(fs):
    expected_path = "cfgs/sample_config.yaml"
    fs.create_file(
        expected_path,
        contents=dedent(
            """
            ---
            type: com.google.api.codegen.samplegen.v1p2.SampleConfigProto
            schema_version: 1.2.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            """
        ),
    )
    actual_paths = list(gapic_utils.generate_all_sample_fpaths(expected_path))

    assert actual_paths == [expected_path]


def test_generate_sample_config_fpaths_not_yaml(fs):
    expected_path = "cfgs/sample_config.not_yaml"
    fs.create_file(expected_path)

    with pytest.raises(types.InvalidConfig):
        list(gapic_utils.generate_all_sample_fpaths(expected_path))


def test_generate_sample_config_fpaths_bad_contents(
    fs,
    # Note the typo: SampleConfigPronto
    contents=dedent(
        """
            ---
            type: com.google.api.codegen.SampleConfigPronto
            schema_version: 1.2.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            """
    ),
):
    expected_path = "cfgs/sample_config.yaml"
    fs.create_file(expected_path, contents=contents)

    with pytest.raises(types.InvalidConfig):
        list(gapic_utils.generate_all_sample_fpaths(expected_path))


def test_generate_sample_config_fpaths_bad_contents_old(fs):
    test_generate_sample_config_fpaths_bad_contents(
        fs,
        contents=dedent(
            """
            ---
            type: com.google.api.codegen.samplegen.v1p2.SampleConfigProto
            schema_version: 1.1.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            """
        ),
    )


def test_generate_sample_config_fpaths_bad_contents_no_samples(fs):
    test_generate_sample_config_fpaths_bad_contents(
        fs,
        contents=dedent(
            """
            ---
            type: com.google.api.codegen.samplegen.v1p2.SampleConfigProto
            schema_version: 1.2.0
            """
        ),
    )


def test_generate_sample_config_partial_config(fs):
    expected_path = "sample.yaml"
    fs.create_file(
        expected_path,
        # Note the typo: SampleConfigPronto
        contents=dedent(
            """
            ---
            # Note: not a valid config because of the type.
            type: com.google.api.codegen.samplegen.v1p2.SampleConfigPronto
            schema_version: 1.2.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            ---
            # Note: this one IS a valid config
            type: com.google.api.codegen.samplegen.v1p2.SampleConfigProto
            schema_version: 1.2.0
            samples:
            - service: google.cloud.language.v1.LanguageService
            """
        ),
    )
    expected_paths = [expected_path]

    actual_paths = list(gapic_utils.generate_all_sample_fpaths(expected_path))

    assert actual_paths == expected_paths


def test_generate_sample_config_fpaths_no_such_file(fs):
    with pytest.raises(types.InvalidConfig):
        list(gapic_utils.generate_all_sample_fpaths("cfgs/sample_config.yaml"))


def test_generate_sample_resumable_upload():
    classify_target_field = DummyField(
        name="classify_target",
        type=DummyMessageTypePB(name="ClassifyTarget"),
        message=DummyMessage(
            type="CLASSIFY TYPE",
            fields={
                "location_annotation": DummyField(
                    type=DummyMessageTypePB(name="Location"),
                    message=DummyMessage(type="LOCATION TYPE"),
                ),
            },
        ),
        ident=DummyIdent(sphinx="molluscs_v1.ClassifyTarget"),
    )

    input_type = DummyMessage(
        type="REQUEST TYPE",
        fields={"classify_target": classify_target_field},
        ident=DummyIdent(
            name="molluscs.v1.ClassifyRequest", sphinx="molluscs_v1.classify_request"
        ),
    )

    output_type = DummyMessage(
        type="RESPONSE TYPE",
        fields={
            "classification": DummyField(
                type=DummyMessageTypePB(name="Classification"),
            )
        },
        ident=DummyIdent(sphinx="molluscs_v1.classification"),
    )

    api_naming = naming.NewNaming(name="MolluscClient", namespace=("molluscs", "v1"))
    service = wrappers.Service(
        service_pb=namedtuple("service_pb", ["name"])("MolluscService"),
        methods={
            "Classify": DummyMethod(
                name="Classify",
                input=input_type,
                output=message_factory("$resp.taxonomy"),
                client_output_async=output_type,
                client_output=output_type,
                flattened_fields={"classify_target": classify_target_field},
                is_resumable_upload=True,
            )
        },
        visible_resources={},
    )

    schema = DummyApiSchema(
        services={"animalia.mollusca.v1.Mollusc": service},
        naming=api_naming,
    )

    sample = {
        "service": "animalia.mollusca.v1.Mollusc",
        "region_tag": "molluscs_generated_molluscs_v1_Mollusc_Classify_sync",
        "rpc": "Classify",
        "transport": "grpc",
        "id": "mollusc_classify_sync",
        "description": "Determine the full taxonomy of input mollusc",
        "request": [
            {
                "field": "classify_target.location_annotation",
                "value": "New Zealand",
                "input_parameter": "location",
            },
        ],
        "response": [{"print": ['Mollusc is a "%s"', "$resp.taxonomy"]}],
    }

    sample_str, _ = samplegen.generate_sample(
        sample, schema, env.get_template("examples/sample.py.j2")
    )

    assert (
        "from google.api_core.resumable_transfer import ResumableUploadConfig"
        in sample_str
    )
    assert "import io" in sample_str
    assert "# Make the request" in sample_str
    assert "upload_session = client.classify(request=request, config=config)" in sample_str
    assert 'stream = io.BytesIO(b"Example upload data")' in sample_str
    assert "response = upload_session.upload(stream)" in sample_str
    assert "# for progress in upload_session.iter_upload(stream):" in sample_str
    assert "# response = upload_session.resume(upload_url, stream, chunk_size=config.chunk_size)" in sample_str
    assert "# for progress in upload_session.iter_resume(upload_url, stream, chunk_size=config.chunk_size):" in sample_str


def test_generate_sample_resumable_upload_async():
    classify_target_field = DummyField(
        name="classify_target",
        type=DummyMessageTypePB(name="ClassifyTarget"),
        message=DummyMessage(
            type="CLASSIFY TYPE",
            fields={
                "location_annotation": DummyField(
                    type=DummyMessageTypePB(name="Location"),
                    message=DummyMessage(type="LOCATION TYPE"),
                ),
            },
        ),
        ident=DummyIdent(sphinx="molluscs_v1.ClassifyTarget"),
    )

    input_type = DummyMessage(
        type="REQUEST TYPE",
        fields={"classify_target": classify_target_field},
        ident=DummyIdent(
            name="molluscs.v1.ClassifyRequest", sphinx="molluscs_v1.classify_request"
        ),
    )

    output_type = DummyMessage(
        type="RESPONSE TYPE",
        fields={
            "classification": DummyField(
                type=DummyMessageTypePB(name="Classification"),
            )
        },
        ident=DummyIdent(sphinx="molluscs_v1.classification"),
    )

    api_naming = naming.NewNaming(name="MolluscClient", namespace=("molluscs", "v1"))
    service = wrappers.Service(
        service_pb=namedtuple("service_pb", ["name"])("MolluscService"),
        methods={
            "Classify": DummyMethod(
                name="Classify",
                input=input_type,
                output=message_factory("$resp.taxonomy"),
                client_output_async=output_type,
                client_output=output_type,
                flattened_fields={"classify_target": classify_target_field},
                is_resumable_upload=True,
            )
        },
        visible_resources={},
    )

    schema = DummyApiSchema(
        services={"animalia.mollusca.v1.Mollusc": service},
        naming=api_naming,
    )

    sample = {
        "service": "animalia.mollusca.v1.Mollusc",
        "region_tag": "molluscs_generated_molluscs_v1_Mollusc_Classify_async",
        "rpc": "Classify",
        "transport": "grpc-async",
        "id": "mollusc_classify_async",
        "description": "Determine the full taxonomy of input mollusc",
        "request": [
            {
                "field": "classify_target.location_annotation",
                "value": "New Zealand",
                "input_parameter": "location",
            },
        ],
        "response": [{"print": ['Mollusc is a "%s"', "$resp.taxonomy"]}],
    }

    sample_str, _ = samplegen.generate_sample(
        sample, schema, env.get_template("examples/sample.py.j2")
    )

    assert (
        "from google.api_core.resumable_transfer import ResumableUploadConfig"
        in sample_str
    )
    assert "import io" in sample_str
    assert "python3 -m pip install molluscs-v1-molluscclient[async_rest]" in sample_str
    assert "# Make the request" in sample_str
    assert "upload_session = await client.classify(request=request, config=config)" in sample_str
    assert 'stream = io.BytesIO(b"Example upload data")' in sample_str
    assert "response = await upload_session.upload(stream)" in sample_str
    assert "# async for progress in upload_session.upload(stream):" in sample_str
    assert "# response = await upload_session.resume(upload_url, stream, chunk_size=config.chunk_size)" in sample_str
    assert "# async for progress in upload_session.resume(upload_url, stream, chunk_size=config.chunk_size):" in sample_str


