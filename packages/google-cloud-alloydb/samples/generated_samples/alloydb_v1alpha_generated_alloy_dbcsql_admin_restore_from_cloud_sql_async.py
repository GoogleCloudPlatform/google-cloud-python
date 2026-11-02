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
# Snippet for RestoreFromCloudSQL
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-alloydb


# [START alloydb_v1alpha_generated_AlloyDBCSQLAdmin_RestoreFromCloudSQL_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import alloydb_v1alpha


async def sample_restore_from_cloud_sql():
    # Create a client
    client = alloydb_v1alpha.AlloyDBCSQLAdminAsyncClient()

    # Initialize request argument(s)
    cloudsql_backup_run_source = alloydb_v1alpha.CloudSQLBackupRunSource()
    cloudsql_backup_run_source.instance_id = "instance_id_value"
    cloudsql_backup_run_source.backup_run_id = 1366

    cluster = alloydb_v1alpha.Cluster()
    cluster.backup_source.backup_name = "backup_name_value"
    cluster.network = "network_value"

    request = alloydb_v1alpha.RestoreFromCloudSQLRequest(
        cloudsql_backup_run_source=cloudsql_backup_run_source,
        parent="parent_value",
        cluster_id="cluster_id_value",
        cluster=cluster,
    )

    # Make the request
    operation = await client.restore_from_cloud_sql(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END alloydb_v1alpha_generated_AlloyDBCSQLAdmin_RestoreFromCloudSQL_async]
