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
# Snippet for CreatePrivateCloud
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-vmwareengine


# [START vmwareengine_v1_generated_VmwareEngine_CreatePrivateCloud_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import vmwareengine_v1


def sample_create_private_cloud():
    # Create a client
    client = vmwareengine_v1.VmwareEngineClient()

    # Initialize request argument(s)
    private_cloud = vmwareengine_v1.PrivateCloud()
    private_cloud.network_config.management_cidr = "management_cidr_value"
    private_cloud.management_cluster.cluster_id = "cluster_id_value"

    request = vmwareengine_v1.CreatePrivateCloudRequest(
        parent="parent_value",
        private_cloud_id="private_cloud_id_value",
        private_cloud=private_cloud,
    )

    # Make the request
    operation = client.create_private_cloud(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END vmwareengine_v1_generated_VmwareEngine_CreatePrivateCloud_sync]
