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
# Snippet for TriggerAction
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-shopping-merchant-issueresolution


# [START merchantapi_v1_generated_IssueResolutionService_TriggerAction_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.shopping import merchant_issueresolution_v1


async def sample_trigger_action():
    # Create a client
    client = merchant_issueresolution_v1.IssueResolutionServiceAsyncClient()

    # Initialize request argument(s)
    payload = merchant_issueresolution_v1.TriggerActionPayload()
    payload.action_context = "action_context_value"
    payload.action_input.action_flow_id = "action_flow_id_value"
    payload.action_input.input_values.text_input_value.value = "value_value"
    payload.action_input.input_values.input_field_id = "input_field_id_value"

    request = merchant_issueresolution_v1.TriggerActionRequest(
        name="name_value",
        payload=payload,
    )

    # Make the request
    response = await client.trigger_action(request=request)

    # Handle the response
    print(response)


# [END merchantapi_v1_generated_IssueResolutionService_TriggerAction_async]
