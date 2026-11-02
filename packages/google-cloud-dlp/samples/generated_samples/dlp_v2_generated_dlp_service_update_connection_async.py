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
# Snippet for UpdateConnection
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dlp


# [START dlp_v2_generated_DlpService_UpdateConnection_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import dlp_v2


async def sample_update_connection():
    # Create a client
    client = dlp_v2.DlpServiceAsyncClient()

    # Initialize request argument(s)
    connection = dlp_v2.Connection()
    connection.cloud_sql.username_password.username = "username_value"
    connection.cloud_sql.username_password.password_secret_version_name = (
        "password_secret_version_name_value"
    )
    connection.cloud_sql.max_connections = 1608
    connection.cloud_sql.database_engine = "DATABASE_ENGINE_POSTGRES"
    connection.state = "ERROR"

    request = dlp_v2.UpdateConnectionRequest(
        name="name_value",
        connection=connection,
    )

    # Make the request
    response = await client.update_connection(request=request)

    # Handle the response
    print(response)


# [END dlp_v2_generated_DlpService_UpdateConnection_async]
