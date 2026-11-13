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
# Snippet for CreateAutoProtectionPolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-backupdr


# [START backupdr_v1beta_generated_BackupDR_CreateAutoProtectionPolicy_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import backupdr_v1beta


def sample_create_auto_protection_policy():
    # Create a client
    client = backupdr_v1beta.BackupDRClient()

    # Initialize request argument(s)
    auto_protection_policy = backupdr_v1beta.AutoProtectionPolicy()
    auto_protection_policy.backup_plan_details.resource_type = "resource_type_value"
    auto_protection_policy.backup_plan_details.backup_plan = "backup_plan_value"
    auto_protection_policy.criteria.matching_conditions.label_condition.key = (
        "key_value"
    )
    auto_protection_policy.criteria.matching_conditions.label_condition.values = [
        "values_value1",
        "values_value2",
    ]

    request = backupdr_v1beta.CreateAutoProtectionPolicyRequest(
        parent="parent_value",
        auto_protection_policy_id="auto_protection_policy_id_value",
        auto_protection_policy=auto_protection_policy,
    )

    # Make the request
    operation = client.create_auto_protection_policy(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END backupdr_v1beta_generated_BackupDR_CreateAutoProtectionPolicy_sync]
