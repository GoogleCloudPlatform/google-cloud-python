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
# Snippet for CreateConnection
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-designcenter


# [START designcenter_v1_generated_DesignCenter_CreateConnection_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import designcenter_v1


async def sample_create_connection():
    # Create a client
    client = designcenter_v1.DesignCenterAsyncClient()

    # Initialize request argument(s)
    connection = designcenter_v1.Connection()
    connection.destination_component_uri = "destination_component_uri_value"

    request = designcenter_v1.CreateConnectionRequest(
        parent="parent_value",
        connection_id="connection_id_value",
        connection=connection,
    )

    # Make the request
    response = await client.create_connection(request=request)

    # Handle the response
    print(response)


# [END designcenter_v1_generated_DesignCenter_CreateConnection_async]
