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
# Snippet for CreateTraceScope
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-observability


# [START observability_v1_generated_Observability_CreateTraceScope_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import observability_v1


async def sample_create_trace_scope():
    # Create a client
    client = observability_v1.ObservabilityAsyncClient()

    # Initialize request argument(s)
    trace_scope = observability_v1.TraceScope()
    trace_scope.resource_names = ["resource_names_value1", "resource_names_value2"]

    request = observability_v1.CreateTraceScopeRequest(
        parent="parent_value",
        trace_scope_id="trace_scope_id_value",
        trace_scope=trace_scope,
    )

    # Make the request
    response = await client.create_trace_scope(request=request)

    # Handle the response
    print(response)


# [END observability_v1_generated_Observability_CreateTraceScope_async]
