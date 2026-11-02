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
# Snippet for CreateBackup
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-alloydb


# [START alloydb_v1alpha_generated_AlloyDBAdmin_CreateBackup_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import alloydb_v1alpha


def sample_create_backup():
    # Create a client
    client = alloydb_v1alpha.AlloyDBAdminClient()

    # Initialize request argument(s)
    backup = alloydb_v1alpha.Backup()
    backup.cluster_name = "cluster_name_value"

    request = alloydb_v1alpha.CreateBackupRequest(
        parent="parent_value",
        backup_id="backup_id_value",
        backup=backup,
    )

    # Make the request
    operation = client.create_backup(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END alloydb_v1alpha_generated_AlloyDBAdmin_CreateBackup_sync]
