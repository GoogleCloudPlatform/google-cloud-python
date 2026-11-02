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
# Snippet for UpdateCssProductInput
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-shopping-css


# [START css_v1_generated_CssProductInputsService_UpdateCssProductInput_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.shopping import css_v1


async def sample_update_css_product_input():
    # Create a client
    client = css_v1.CssProductInputsServiceAsyncClient()

    # Initialize request argument(s)
    css_product_input = css_v1.CssProductInput()
    css_product_input.raw_provided_id = "raw_provided_id_value"
    css_product_input.content_language = "content_language_value"
    css_product_input.feed_label = "feed_label_value"

    request = css_v1.UpdateCssProductInputRequest(
        css_product_input=css_product_input,
    )

    # Make the request
    response = await client.update_css_product_input(request=request)

    # Handle the response
    print(response)


# [END css_v1_generated_CssProductInputsService_UpdateCssProductInput_async]
