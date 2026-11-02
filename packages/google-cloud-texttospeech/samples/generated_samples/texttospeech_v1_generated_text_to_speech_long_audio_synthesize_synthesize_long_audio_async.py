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
# Snippet for SynthesizeLongAudio
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-texttospeech


# [START texttospeech_v1_generated_TextToSpeechLongAudioSynthesize_SynthesizeLongAudio_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import texttospeech_v1


async def sample_synthesize_long_audio():
    # Create a client
    client = texttospeech_v1.TextToSpeechLongAudioSynthesizeAsyncClient()

    # Initialize request argument(s)
    input = texttospeech_v1.SynthesisInput()
    input.text = "text_value"

    audio_config = texttospeech_v1.AudioConfig()
    audio_config.audio_encoding = "M4A"

    voice = texttospeech_v1.VoiceSelectionParams()
    voice.language_code = "language_code_value"

    request = texttospeech_v1.SynthesizeLongAudioRequest(
        input=input,
        audio_config=audio_config,
        output_gcs_uri="output_gcs_uri_value",
        voice=voice,
    )

    # Make the request
    operation = await client.synthesize_long_audio(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END texttospeech_v1_generated_TextToSpeechLongAudioSynthesize_SynthesizeLongAudio_async]
