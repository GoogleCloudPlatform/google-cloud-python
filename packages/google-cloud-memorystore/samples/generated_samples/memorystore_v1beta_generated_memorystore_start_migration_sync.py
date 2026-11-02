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
# Snippet for StartMigration
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-memorystore


# [START memorystore_v1beta_generated_Memorystore_StartMigration_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import memorystore_v1beta


def sample_start_migration():
    # Create a client
    client = memorystore_v1beta.MemorystoreClient()

    # Initialize request argument(s)
    self_managed_source = memorystore_v1beta.SelfManagedSource()
    self_managed_source.ip_address = "ip_address_value"
    self_managed_source.port = 453
    self_managed_source.network_attachment = "network_attachment_value"

    request = memorystore_v1beta.StartMigrationRequest(
        self_managed_source=self_managed_source,
        name="name_value",
    )

    # Make the request
    operation = client.start_migration(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END memorystore_v1beta_generated_Memorystore_StartMigration_sync]
