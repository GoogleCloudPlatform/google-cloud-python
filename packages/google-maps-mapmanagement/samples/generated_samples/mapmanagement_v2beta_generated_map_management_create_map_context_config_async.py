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
# Snippet for CreateMapContextConfig
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-maps-mapmanagement


# [START mapmanagement_v2beta_generated_MapManagement_CreateMapContextConfig_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.maps import mapmanagement_v2beta


async def sample_create_map_context_config():
    # Create a client
    client = mapmanagement_v2beta.MapManagementAsyncClient()

    # Initialize request argument(s)
    map_context_config = mapmanagement_v2beta.MapContextConfig()
    map_context_config.map_config = "map_config_value"
    map_context_config.style_config = "style_config_value"
    map_context_config.map_variants = ["PHOTOREALISTIC3D"]

    request = mapmanagement_v2beta.CreateMapContextConfigRequest(
        parent="parent_value",
        map_context_config=map_context_config,
    )

    # Make the request
    response = await client.create_map_context_config(request=request)

    # Handle the response
    print(response)


# [END mapmanagement_v2beta_generated_MapManagement_CreateMapContextConfig_async]
