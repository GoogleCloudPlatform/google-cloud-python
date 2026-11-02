# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for BidiStreamingAnalyzeContent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_v2beta1_generated_Participants_BidiStreamingAnalyzeContent_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import dialogflow_v2beta1


def sample_bidi_streaming_analyze_content():
    # Create a client
    client = dialogflow_v2beta1.ParticipantsClient()

    # Initialize request argument(s)
    config = dialogflow_v2beta1.Config()
    config.voice_session_config.input_audio_encoding = "AUDIO_ENCODING_ALAW"
    config.voice_session_config.input_audio_sample_rate_hertz = 3097
    config.voice_session_config.output_audio_encoding = "OUTPUT_AUDIO_ENCODING_ALAW"
    config.voice_session_config.output_audio_sample_rate_hertz = 3226
    config.participant = "participant_value"

    request = dialogflow_v2beta1.BidiStreamingAnalyzeContentRequest(
        config=config,
    )

    # This method expects an iterator which contains
    # 'dialogflow_v2beta1.BidiStreamingAnalyzeContentRequest' objects
    # Here we create a generator that yields a single `request` for
    # demonstrative purposes.
    requests = [request]

    def request_generator():
        for request in requests:
            yield request

    # Make the request
    stream = client.bidi_streaming_analyze_content(requests=request_generator())

    # Handle the response
    for response in stream:
        print(response)


# [END dialogflow_v2beta1_generated_Participants_BidiStreamingAnalyzeContent_sync]
