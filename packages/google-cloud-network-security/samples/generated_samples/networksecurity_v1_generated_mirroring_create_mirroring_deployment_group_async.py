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
# Snippet for CreateMirroringDeploymentGroup
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-network-security


# [START networksecurity_v1_generated_Mirroring_CreateMirroringDeploymentGroup_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import network_security_v1


async def sample_create_mirroring_deployment_group():
    # Create a client
    client = network_security_v1.MirroringAsyncClient()

    # Initialize request argument(s)
    mirroring_deployment_group = network_security_v1.MirroringDeploymentGroup()
    mirroring_deployment_group.network = "network_value"

    request = network_security_v1.CreateMirroringDeploymentGroupRequest(
        parent="parent_value",
        mirroring_deployment_group_id="mirroring_deployment_group_id_value",
        mirroring_deployment_group=mirroring_deployment_group,
    )

    # Make the request
    operation = await client.create_mirroring_deployment_group(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END networksecurity_v1_generated_Mirroring_CreateMirroringDeploymentGroup_async]
