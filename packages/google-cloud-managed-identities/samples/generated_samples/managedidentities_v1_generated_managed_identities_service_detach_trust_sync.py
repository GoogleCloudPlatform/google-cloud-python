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
# Snippet for DetachTrust
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-managed-identities


# [START managedidentities_v1_generated_ManagedIdentitiesService_DetachTrust_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import managedidentities_v1


def sample_detach_trust():
    # Create a client
    client = managedidentities_v1.ManagedIdentitiesServiceClient()

    # Initialize request argument(s)
    trust = managedidentities_v1.Trust()
    trust.target_domain_name = "target_domain_name_value"
    trust.trust_type = "EXTERNAL"
    trust.trust_direction = "BIDIRECTIONAL"
    trust.target_dns_ip_addresses = [
        "target_dns_ip_addresses_value1",
        "target_dns_ip_addresses_value2",
    ]
    trust.trust_handshake_secret = "trust_handshake_secret_value"

    request = managedidentities_v1.DetachTrustRequest(
        name="name_value",
        trust=trust,
    )

    # Make the request
    operation = client.detach_trust(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END managedidentities_v1_generated_ManagedIdentitiesService_DetachTrust_sync]
