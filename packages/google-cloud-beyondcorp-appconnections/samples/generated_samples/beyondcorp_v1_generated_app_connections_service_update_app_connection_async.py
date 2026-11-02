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
# Snippet for UpdateAppConnection
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-beyondcorp-appconnections


# [START beyondcorp_v1_generated_AppConnectionsService_UpdateAppConnection_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import beyondcorp_appconnections_v1


async def sample_update_app_connection():
    # Create a client
    client = beyondcorp_appconnections_v1.AppConnectionsServiceAsyncClient()

    # Initialize request argument(s)
    app_connection = beyondcorp_appconnections_v1.AppConnection()
    app_connection.name = "name_value"
    app_connection.type_ = "TCP_PROXY"
    app_connection.application_endpoint.host = "host_value"
    app_connection.application_endpoint.port = 453

    request = beyondcorp_appconnections_v1.UpdateAppConnectionRequest(
        app_connection=app_connection,
    )

    # Make the request
    operation = await client.update_app_connection(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END beyondcorp_v1_generated_AppConnectionsService_UpdateAppConnection_async]
