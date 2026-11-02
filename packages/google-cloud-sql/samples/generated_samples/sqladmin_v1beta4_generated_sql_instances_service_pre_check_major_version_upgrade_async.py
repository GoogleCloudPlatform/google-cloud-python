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
# Snippet for PreCheckMajorVersionUpgrade
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-sql


# [START sqladmin_v1beta4_generated_SqlInstancesService_PreCheckMajorVersionUpgrade_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import sqladmin_v1beta4


async def sample_pre_check_major_version_upgrade():
    # Create a client
    client = sqladmin_v1beta4.SqlInstancesServiceAsyncClient()

    # Initialize request argument(s)
    body = sqladmin_v1beta4.InstancesPreCheckMajorVersionUpgradeRequest()
    body.pre_check_major_version_upgrade_context.target_database_version = (
        "SQLSERVER_2025_EXPRESS"
    )

    request = sqladmin_v1beta4.SqlInstancesPreCheckMajorVersionUpgradeRequest(
        instance="instance_value",
        project="project_value",
        body=body,
    )

    # Make the request
    response = await client.pre_check_major_version_upgrade(request=request)

    # Handle the response
    print(response)


# [END sqladmin_v1beta4_generated_SqlInstancesService_PreCheckMajorVersionUpgrade_async]
