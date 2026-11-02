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
# Snippet for RemoveProductImageBackground
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-shopping-merchant-productstudio


# [START merchantapi_v1alpha_generated_ImageService_RemoveProductImageBackground_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.shopping import merchant_productstudio_v1alpha


async def sample_remove_product_image_background():
    # Create a client
    client = merchant_productstudio_v1alpha.ImageServiceAsyncClient()

    # Initialize request argument(s)
    input_image = merchant_productstudio_v1alpha.InputImage()
    input_image.image_uri = "image_uri_value"

    request = merchant_productstudio_v1alpha.RemoveProductImageBackgroundRequest(
        name="name_value",
        input_image=input_image,
    )

    # Make the request
    response = await client.remove_product_image_background(request=request)

    # Handle the response
    print(response)


# [END merchantapi_v1alpha_generated_ImageService_RemoveProductImageBackground_async]
