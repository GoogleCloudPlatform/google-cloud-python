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
# Snippet for CountTextTokens
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-ai-generativelanguage


# [START generativelanguage_v1beta3_generated_TextService_CountTextTokens_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.ai import generativelanguage_v1beta3


def sample_count_text_tokens():
    # Create a client
    client = generativelanguage_v1beta3.TextServiceClient()

    # Initialize request argument(s)
    prompt = generativelanguage_v1beta3.TextPrompt()
    prompt.text = "text_value"

    request = generativelanguage_v1beta3.CountTextTokensRequest(
        model="model_value",
        prompt=prompt,
    )

    # Make the request
    response = client.count_text_tokens(request=request)

    # Handle the response
    print(response)


# [END generativelanguage_v1beta3_generated_TextService_CountTextTokens_sync]
