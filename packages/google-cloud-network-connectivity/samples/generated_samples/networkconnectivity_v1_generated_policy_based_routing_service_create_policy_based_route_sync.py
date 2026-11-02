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
# Snippet for CreatePolicyBasedRoute
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-network-connectivity


# [START networkconnectivity_v1_generated_PolicyBasedRoutingService_CreatePolicyBasedRoute_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import networkconnectivity_v1


def sample_create_policy_based_route():
    # Create a client
    client = networkconnectivity_v1.PolicyBasedRoutingServiceClient()

    # Initialize request argument(s)
    policy_based_route = networkconnectivity_v1.PolicyBasedRoute()
    policy_based_route.next_hop_ilb_ip = "next_hop_ilb_ip_value"
    policy_based_route.network = "network_value"
    policy_based_route.filter.protocol_version = "IPV4"

    request = networkconnectivity_v1.CreatePolicyBasedRouteRequest(
        parent="parent_value",
        policy_based_route_id="policy_based_route_id_value",
        policy_based_route=policy_based_route,
    )

    # Make the request
    operation = client.create_policy_based_route(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END networkconnectivity_v1_generated_PolicyBasedRoutingService_CreatePolicyBasedRoute_sync]
