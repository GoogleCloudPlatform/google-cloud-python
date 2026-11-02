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
# Snippet for CreateClientTlsPolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-network-security


# [START networksecurity_v1_generated_NetworkSecurity_CreateClientTlsPolicy_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import network_security_v1


async def sample_create_client_tls_policy():
    # Create a client
    client = network_security_v1.NetworkSecurityAsyncClient()

    # Initialize request argument(s)
    client_tls_policy = network_security_v1.ClientTlsPolicy()
    client_tls_policy.name = "name_value"

    request = network_security_v1.CreateClientTlsPolicyRequest(
        parent="parent_value",
        client_tls_policy_id="client_tls_policy_id_value",
        client_tls_policy=client_tls_policy,
    )

    # Make the request
    operation = await client.create_client_tls_policy(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END networksecurity_v1_generated_NetworkSecurity_CreateClientTlsPolicy_async]
