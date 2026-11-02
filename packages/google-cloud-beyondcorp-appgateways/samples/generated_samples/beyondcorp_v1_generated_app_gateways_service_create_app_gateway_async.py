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
# Snippet for CreateAppGateway
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-beyondcorp-appgateways


# [START beyondcorp_v1_generated_AppGatewaysService_CreateAppGateway_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import beyondcorp_appgateways_v1


async def sample_create_app_gateway():
    # Create a client
    client = beyondcorp_appgateways_v1.AppGatewaysServiceAsyncClient()

    # Initialize request argument(s)
    app_gateway = beyondcorp_appgateways_v1.AppGateway()
    app_gateway.name = "name_value"
    app_gateway.type_ = "TCP_PROXY"
    app_gateway.host_type = "GCP_REGIONAL_MIG"

    request = beyondcorp_appgateways_v1.CreateAppGatewayRequest(
        parent="parent_value",
        app_gateway=app_gateway,
    )

    # Make the request
    operation = await client.create_app_gateway(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END beyondcorp_v1_generated_AppGatewaysService_CreateAppGateway_async]
