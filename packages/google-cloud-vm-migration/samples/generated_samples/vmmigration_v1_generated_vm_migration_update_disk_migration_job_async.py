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
# Snippet for UpdateDiskMigrationJob
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-vm-migration


# [START vmmigration_v1_generated_VmMigration_UpdateDiskMigrationJob_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import vmmigration_v1


async def sample_update_disk_migration_job():
    # Create a client
    client = vmmigration_v1.VmMigrationAsyncClient()

    # Initialize request argument(s)
    disk_migration_job = vmmigration_v1.DiskMigrationJob()
    disk_migration_job.aws_source_disk_details.volume_id = "volume_id_value"
    disk_migration_job.target_details.target_disk.zone = "zone_value"
    disk_migration_job.target_details.target_disk.disk_type = (
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED"
    )
    disk_migration_job.target_details.target_project = "target_project_value"

    request = vmmigration_v1.UpdateDiskMigrationJobRequest(
        disk_migration_job=disk_migration_job,
    )

    # Make the request
    operation = await client.update_disk_migration_job(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END vmmigration_v1_generated_VmMigration_UpdateDiskMigrationJob_async]
