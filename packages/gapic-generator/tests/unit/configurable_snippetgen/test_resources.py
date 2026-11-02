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

from google.protobuf.compiler import plugin_pb2
import pytest

from gapic import utils
from gapic.schema import api


CURRENT_DIRECTORY = Path(__file__).parent.absolute()
SPEECH_V1_REQUEST_PATH = CURRENT_DIRECTORY / "resources" / "speech" / "request.desc"


def test_request():
    with open(SPEECH_V1_REQUEST_PATH, "rb") as f:
        req = plugin_pb2.CodeGeneratorRequest.FromString(f.read())

    # From gapic/cli/generator.py.
    opts = utils.Options.build(req.parameter)
    api_schema = api.API.build(
        req.proto_file,
        opts=opts,
        package="google.cloud.speech.v1",
    )

    expected_services = [
        "google.cloud.speech.v1.Adaptation",
        "google.cloud.speech.v1.Speech",
    ]

    # We are only making sure that the dumped request.desc file can be
    # successfully loaded to rebuild API schema.
    assert list(api_schema.services.keys()) == expected_services
