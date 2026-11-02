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
# Snippet for CreateNetworkPeering
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-vmwareengine


# [START vmwareengine_v1_generated_VmwareEngine_CreateNetworkPeering_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import vmwareengine_v1


def sample_create_network_peering():
    # Create a client
    client = vmwareengine_v1.VmwareEngineClient()

    # Initialize request argument(s)
    network_peering = vmwareengine_v1.NetworkPeering()
    network_peering.peer_network = "peer_network_value"
    network_peering.peer_network_type = "GOOGLE_CLOUD_NETAPP_VOLUMES"
    network_peering.vmware_engine_network = "vmware_engine_network_value"

    request = vmwareengine_v1.CreateNetworkPeeringRequest(
        parent="parent_value",
        network_peering_id="network_peering_id_value",
        network_peering=network_peering,
    )

    # Make the request
    operation = client.create_network_peering(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END vmwareengine_v1_generated_VmwareEngine_CreateNetworkPeering_sync]
