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

import json

from google.protobuf import json_format
import pytest

from gapic.samplegen_utils import snippet_metadata_pb2
from gapic.samplegen_utils import snippet_index, types
from ..common_types import DummyApiSchema, DummyService, DummyMethod, DummyNaming


@pytest.fixture
def sample_str():
    return """# [START mollusc_classify_sync]
from molluscs.v1 import molluscclient


def sample_classify(video, location):
    # Create a client
    client = molluscclient.MolluscServiceClient()

    # Initialize request argument(s)
    classify_target = molluscclient.ClassifyTarget()

    # video = "path/to/mollusc/video.mkv"
    with open(video, "rb") as f:
        classify_target.video = f.read()

    # location = "New Zealand"
    classify_target.location_annotation = location

    request = molluscclient.molluscs.v1.ClassifyRequest(
        classify_target=classify_target,
    )

    # Make the request
    response = client.classify(request=request)

    # Handle the response
    print(f"Mollusc is a \"{response.taxonomy}\"")

# [END mollusc_classify_sync]"""


def test_snippet_init(sample_str):
    # We are not trying to exhaustively test the snippet metadata protobuf,
    # just checking that fields are not unset
    sample_metadata = snippet_metadata_pb2.Snippet(title="classify_squid.py")
    sample_metadata.language = snippet_metadata_pb2.Language.PYTHON
    snippet = snippet_index.Snippet(sample_str, sample_metadata)

    assert snippet.sample_str == sample_str

    # It's easier to eyeball diffs on the dictionary representation
    assert json_format.MessageToDict(snippet.metadata) == {
        "language": "PYTHON",
        "title": "classify_squid.py",
        "segments": [
            {"end": 28, "start": 2, "type": "FULL"},
            {"end": 28, "start": 2, "type": "SHORT"},
            {"end": 8, "start": 6, "type": "CLIENT_INITIALIZATION"},
            {"end": 22, "start": 9, "type": "REQUEST_INITIALIZATION"},
            {"end": 25, "start": 23, "type": "REQUEST_EXECUTION"},
            {"end": 29, "start": 26, "type": "RESPONSE_HANDLING"},
        ],
    }

    # This is the same as the sample_str above, minus the # [START ...]
    # and # [END ...] lines
    expected_full_snippet = """from molluscs.v1 import molluscclient


def sample_classify(video, location):
    # Create a client
    client = molluscclient.MolluscServiceClient()

    # Initialize request argument(s)
    classify_target = molluscclient.ClassifyTarget()

    # video = "path/to/mollusc/video.mkv"
    with open(video, "rb") as f:
        classify_target.video = f.read()

    # location = "New Zealand"
    classify_target.location_annotation = location

    request = molluscclient.molluscs.v1.ClassifyRequest(
        classify_target=classify_target,
    )

    # Make the request
    response = client.classify(request=request)

    # Handle the response
    print(f"Mollusc is a \"{response.taxonomy}\"")

"""

    assert snippet.full_snippet == expected_full_snippet


def test_add_snippet_no_matching_service(sample_str):
    snippet_metadata = snippet_metadata_pb2.Snippet()
    snippet_metadata.client_method.method.service.short_name = "Clam"
    snippet = snippet_index.Snippet(sample_str, snippet_metadata)

    # No 'Clam' service in API Schema
    index = snippet_index.SnippetIndex(
        api_schema=DummyApiSchema(
            services={"Squid": DummyService(name="Squid", methods={})},
            naming=DummyNaming(
                proto_package="google.mollusca",
                warehouse_package_name="google-mollusca",
                version="v1",
            ),
        )
    )
    with pytest.raises(types.UnknownService):
        index.add_snippet(snippet)


def test_add_snippet_no_matching_rpc(sample_str):
    snippet_metadata = snippet_metadata_pb2.Snippet()
    snippet_metadata.client_method.method.service.short_name = "Squid"
    snippet_metadata.client_method.short_name = "classify"
    snippet = snippet_index.Snippet(sample_str, snippet_metadata)

    # No 'classify' method in 'Squid' service
    index = snippet_index.SnippetIndex(
        api_schema=DummyApiSchema(
            services={"Squid": DummyService(name="Squid", methods={"list": None})},
            naming=DummyNaming(
                proto_package="google.mollusca",
                warehouse_package_name="google-mollusca",
                version="v1",
            ),
        )
    )
    with pytest.raises(types.RpcMethodNotFound):
        index.add_snippet(snippet)


def test_get_snippet_no_matching_service():
    index = snippet_index.SnippetIndex(
        api_schema=DummyApiSchema(
            naming=DummyNaming(
                proto_package="google.mollusca",
                warehouse_package_name="google-mollusca",
                version="v1",
            ),
            services={
                "Squid": DummyService(name="Squid", methods={"classify": DummyMethod()})
            },
        )
    )

    # No 'Clam' service in API Schema
    with pytest.raises(types.UnknownService):
        index.get_snippet(service_name="Clam", rpc_name="classify")


def test_get_snippet_no_matching_rpc():
    index = snippet_index.SnippetIndex(
        api_schema=DummyApiSchema(
            services={
                "Squid": DummyService(name="Squid", methods={"classify": DummyMethod()})
            },
            naming=DummyNaming(
                proto_package="google.mollusca",
                warehouse_package_name="google-mollusca",
                version="v1",
            ),
        )
    )

    # No 'list' RPC in 'Squid' service
    with pytest.raises(types.RpcMethodNotFound):
        index.get_snippet(service_name="Squid", rpc_name="list")


def test_add_and_get_snippet_sync(sample_str):
    snippet_metadata = snippet_metadata_pb2.Snippet()
    snippet_metadata.client_method.method.service.short_name = "Squid"
    snippet_metadata.client_method.method.short_name = "classify"
    snippet = snippet_index.Snippet(sample_str, snippet_metadata)

    index = snippet_index.SnippetIndex(
        api_schema=DummyApiSchema(
            services={
                "Squid": DummyService(name="Squid", methods={"classify": DummyMethod()})
            },
            naming=DummyNaming(
                proto_package="google.mollusca",
                warehouse_package_name="google-mollusca",
                version="v1",
            ),
        )
    )

    index.add_snippet(snippet)

    index.get_snippet(service_name="Squid", rpc_name="classify")


def test_add_and_get_snippet_async(sample_str):
    snippet_metadata = snippet_metadata_pb2.Snippet()
    snippet_metadata.client_method.method.service.short_name = "Squid"
    snippet_metadata.client_method.method.short_name = "classify"
    setattr(snippet_metadata.client_method, "async", True)
    snippet = snippet_index.Snippet(sample_str, snippet_metadata)

    index = snippet_index.SnippetIndex(
        api_schema=DummyApiSchema(
            services={
                "Squid": DummyService(name="Squid", methods={"classify": DummyMethod()})
            },
            naming=DummyNaming(
                proto_package="google.mollusca",
                warehouse_package_name="google-mollusca",
                version="v1",
            ),
        )
    )

    index.add_snippet(snippet)

    index.get_snippet(service_name="Squid", rpc_name="classify", sync=False)


def test_get_metadata_json(sample_str):
    snippet_metadata = snippet_metadata_pb2.Snippet()
    snippet_metadata.client_method.method.service.short_name = "Squid"
    snippet_metadata.client_method.method.short_name = "classify"
    snippet = snippet_index.Snippet(sample_str, snippet_metadata)

    index = snippet_index.SnippetIndex(
        api_schema=DummyApiSchema(
            services={
                "Squid": DummyService(name="Squid", methods={"classify": DummyMethod()})
            },
            naming=DummyNaming(
                proto_package="google.mollusca",
                warehouse_package_name="google-mollusca",
                version="v1",
            ),
        )
    )

    index.add_snippet(snippet)

    print(index.get_metadata_json())
    assert json.loads(index.get_metadata_json()) == {
        "clientLibrary": {
            "apis": [{"id": "google.mollusca", "version": "v1"}],
            "language": "PYTHON",
            "name": "google-mollusca",
            "version": "0.0.0",
        },
        "snippets": [
            {
                "clientMethod": {
                    "method": {
                        "service": {"shortName": "Squid"},
                        "shortName": "classify",
                    }
                },
                "segments": [
                    {"end": 28, "start": 2, "type": "FULL"},
                    {"end": 28, "start": 2, "type": "SHORT"},
                    {"end": 8, "start": 6, "type": "CLIENT_INITIALIZATION"},
                    {"end": 22, "start": 9, "type": "REQUEST_INITIALIZATION"},
                    {"end": 25, "start": 23, "type": "REQUEST_EXECUTION"},
                    {"end": 29, "start": 26, "type": "RESPONSE_HANDLING"},
                ],
            }
        ],
    }
