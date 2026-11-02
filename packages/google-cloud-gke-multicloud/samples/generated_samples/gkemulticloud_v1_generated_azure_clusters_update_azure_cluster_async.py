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
# Snippet for UpdateAzureCluster
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-gke-multicloud


# [START gkemulticloud_v1_generated_AzureClusters_UpdateAzureCluster_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import gke_multicloud_v1


async def sample_update_azure_cluster():
    # Create a client
    client = gke_multicloud_v1.AzureClustersAsyncClient()

    # Initialize request argument(s)
    azure_cluster = gke_multicloud_v1.AzureCluster()
    azure_cluster.azure_region = "azure_region_value"
    azure_cluster.resource_group_id = "resource_group_id_value"
    azure_cluster.networking.virtual_network_id = "virtual_network_id_value"
    azure_cluster.networking.pod_address_cidr_blocks = [
        "pod_address_cidr_blocks_value1",
        "pod_address_cidr_blocks_value2",
    ]
    azure_cluster.networking.service_address_cidr_blocks = [
        "service_address_cidr_blocks_value1",
        "service_address_cidr_blocks_value2",
    ]
    azure_cluster.control_plane.version = "version_value"
    azure_cluster.control_plane.ssh_config.authorized_key = "authorized_key_value"
    azure_cluster.fleet.project = "project_value"

    request = gke_multicloud_v1.UpdateAzureClusterRequest(
        azure_cluster=azure_cluster,
    )

    # Make the request
    operation = await client.update_azure_cluster(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END gkemulticloud_v1_generated_AzureClusters_UpdateAzureCluster_async]
