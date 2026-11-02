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
# Snippet for CreateReportConfig
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-migrationcenter


# [START migrationcenter_v1_generated_MigrationCenter_CreateReportConfig_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import migrationcenter_v1


def sample_create_report_config():
    # Create a client
    client = migrationcenter_v1.MigrationCenterClient()

    # Initialize request argument(s)
    report_config = migrationcenter_v1.ReportConfig()
    report_config.group_preferenceset_assignments.group = "group_value"
    report_config.group_preferenceset_assignments.preference_set = (
        "preference_set_value"
    )

    request = migrationcenter_v1.CreateReportConfigRequest(
        parent="parent_value",
        report_config_id="report_config_id_value",
        report_config=report_config,
    )

    # Make the request
    operation = client.create_report_config(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END migrationcenter_v1_generated_MigrationCenter_CreateReportConfig_sync]
