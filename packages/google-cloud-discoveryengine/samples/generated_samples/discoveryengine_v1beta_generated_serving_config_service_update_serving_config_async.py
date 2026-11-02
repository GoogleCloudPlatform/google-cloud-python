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
# Snippet for UpdateServingConfig
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-discoveryengine


# [START discoveryengine_v1beta_generated_ServingConfigService_UpdateServingConfig_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import discoveryengine_v1beta


async def sample_update_serving_config():
    # Create a client
    client = discoveryengine_v1beta.ServingConfigServiceAsyncClient()

    # Initialize request argument(s)
    serving_config = discoveryengine_v1beta.ServingConfig()
    serving_config.media_config.content_watched_percentage_threshold = 0.3811
    serving_config.display_name = "display_name_value"
    serving_config.solution_type = "SOLUTION_TYPE_AI_MODE"

    request = discoveryengine_v1beta.UpdateServingConfigRequest(
        serving_config=serving_config,
    )

    # Make the request
    response = await client.update_serving_config(request=request)

    # Handle the response
    print(response)


# [END discoveryengine_v1beta_generated_ServingConfigService_UpdateServingConfig_async]
