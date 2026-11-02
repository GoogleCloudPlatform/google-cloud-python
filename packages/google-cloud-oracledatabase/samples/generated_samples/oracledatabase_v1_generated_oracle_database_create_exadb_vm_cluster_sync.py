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
# Snippet for CreateExadbVmCluster
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-oracledatabase


# [START oracledatabase_v1_generated_OracleDatabase_CreateExadbVmCluster_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import oracledatabase_v1


def sample_create_exadb_vm_cluster():
    # Create a client
    client = oracledatabase_v1.OracleDatabaseClient()

    # Initialize request argument(s)
    exadb_vm_cluster = oracledatabase_v1.ExadbVmCluster()
    exadb_vm_cluster.properties.grid_image_id = "grid_image_id_value"
    exadb_vm_cluster.properties.node_count = 1070
    exadb_vm_cluster.properties.enabled_ecpu_count_per_node = 2826
    exadb_vm_cluster.properties.vm_file_system_storage.size_in_gbs_per_node = 2103
    exadb_vm_cluster.properties.exascale_db_storage_vault = (
        "exascale_db_storage_vault_value"
    )
    exadb_vm_cluster.properties.hostname_prefix = "hostname_prefix_value"
    exadb_vm_cluster.properties.ssh_public_keys = [
        "ssh_public_keys_value1",
        "ssh_public_keys_value2",
    ]
    exadb_vm_cluster.properties.shape_attribute = "BLOCK_STORAGE"
    exadb_vm_cluster.odb_subnet = "odb_subnet_value"
    exadb_vm_cluster.backup_odb_subnet = "backup_odb_subnet_value"
    exadb_vm_cluster.display_name = "display_name_value"

    request = oracledatabase_v1.CreateExadbVmClusterRequest(
        parent="parent_value",
        exadb_vm_cluster_id="exadb_vm_cluster_id_value",
        exadb_vm_cluster=exadb_vm_cluster,
    )

    # Make the request
    operation = client.create_exadb_vm_cluster(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END oracledatabase_v1_generated_OracleDatabase_CreateExadbVmCluster_sync]
