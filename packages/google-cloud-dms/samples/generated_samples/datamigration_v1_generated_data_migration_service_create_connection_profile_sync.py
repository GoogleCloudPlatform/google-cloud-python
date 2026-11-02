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
# Snippet for CreateConnectionProfile
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dms


# [START datamigration_v1_generated_DataMigrationService_CreateConnectionProfile_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import clouddms_v1


def sample_create_connection_profile():
    # Create a client
    client = clouddms_v1.DataMigrationServiceClient()

    # Initialize request argument(s)
    connection_profile = clouddms_v1.ConnectionProfile()
    connection_profile.mysql.host = "host_value"
    connection_profile.mysql.port = 453
    connection_profile.mysql.username = "username_value"
    connection_profile.mysql.password = "password_value"

    request = clouddms_v1.CreateConnectionProfileRequest(
        parent="parent_value",
        connection_profile_id="connection_profile_id_value",
        connection_profile=connection_profile,
    )

    # Make the request
    operation = client.create_connection_profile(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END datamigration_v1_generated_DataMigrationService_CreateConnectionProfile_sync]
