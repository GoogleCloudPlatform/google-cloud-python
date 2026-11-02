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
# Snippet for StreamingTranslateSpeech
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-media-translation


# [START mediatranslation_v1beta1_generated_SpeechTranslationService_StreamingTranslateSpeech_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import mediatranslation_v1beta1


def sample_streaming_translate_speech():
    # Create a client
    client = mediatranslation_v1beta1.SpeechTranslationServiceClient()

    # Initialize request argument(s)
    streaming_config = mediatranslation_v1beta1.StreamingTranslateSpeechConfig()
    streaming_config.audio_config.audio_encoding = "audio_encoding_value"
    streaming_config.audio_config.source_language_code = "source_language_code_value"
    streaming_config.audio_config.target_language_code = "target_language_code_value"

    request = mediatranslation_v1beta1.StreamingTranslateSpeechRequest(
        streaming_config=streaming_config,
    )

    # This method expects an iterator which contains
    # 'mediatranslation_v1beta1.StreamingTranslateSpeechRequest' objects
    # Here we create a generator that yields a single `request` for
    # demonstrative purposes.
    requests = [request]

    def request_generator():
        for request in requests:
            yield request

    # Make the request
    stream = client.streaming_translate_speech(requests=request_generator())

    # Handle the response
    for response in stream:
        print(response)


# [END mediatranslation_v1beta1_generated_SpeechTranslationService_StreamingTranslateSpeech_sync]
