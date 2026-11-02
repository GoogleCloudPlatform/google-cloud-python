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
# Snippet for UpdateAwsCluster
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-gke-multicloud


# [START gkemulticloud_v1_generated_AwsClusters_UpdateAwsCluster_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import gke_multicloud_v1


async def sample_update_aws_cluster():
    # Create a client
    client = gke_multicloud_v1.AwsClustersAsyncClient()

    # Initialize request argument(s)
    aws_cluster = gke_multicloud_v1.AwsCluster()
    aws_cluster.networking.vpc_id = "vpc_id_value"
    aws_cluster.networking.pod_address_cidr_blocks = [
        "pod_address_cidr_blocks_value1",
        "pod_address_cidr_blocks_value2",
    ]
    aws_cluster.networking.service_address_cidr_blocks = [
        "service_address_cidr_blocks_value1",
        "service_address_cidr_blocks_value2",
    ]
    aws_cluster.aws_region = "aws_region_value"
    aws_cluster.control_plane.version = "version_value"
    aws_cluster.control_plane.subnet_ids = ["subnet_ids_value1", "subnet_ids_value2"]
    aws_cluster.control_plane.iam_instance_profile = "iam_instance_profile_value"
    aws_cluster.control_plane.database_encryption.kms_key_arn = "kms_key_arn_value"
    aws_cluster.control_plane.aws_services_authentication.role_arn = "role_arn_value"
    aws_cluster.control_plane.config_encryption.kms_key_arn = "kms_key_arn_value"
    aws_cluster.fleet.project = "project_value"

    request = gke_multicloud_v1.UpdateAwsClusterRequest(
        aws_cluster=aws_cluster,
    )

    # Make the request
    operation = await client.update_aws_cluster(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END gkemulticloud_v1_generated_AwsClusters_UpdateAwsCluster_async]
