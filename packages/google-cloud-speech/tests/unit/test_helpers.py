# Copyright 2017, Google LLC All rights reserved.
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

from __future__ import absolute_import

from types import GeneratorType
from unittest import mock

import google.auth.credentials

from google.cloud.speech_v1 import SpeechClient, types


def make_speech_client():
    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    return SpeechClient(credentials=credentials)


def test_streaming_recognize():
    client = make_speech_client()

    config = types.StreamingRecognitionConfig()
    requests = [types.StreamingRecognizeRequest(audio_content=b"...")]
    super_patch = mock.patch(
        "google.cloud.speech_v1.services.speech.SpeechClient.streaming_recognize",
        autospec=True,
    )

    with super_patch as streaming_recognize:
        client.streaming_recognize(config, requests)

    # Assert that we called streaming recognize with an iterable
    # that evaluates to the correct format.
    _, args, kwargs = streaming_recognize.mock_calls[0]
    api_requests = kwargs["requests"]
    assert isinstance(api_requests, GeneratorType)
    assert list(api_requests) == [
        {"streaming_config": config},
        requests[0],
    ]
    assert "retry" in kwargs
    assert "timeout" in kwargs
