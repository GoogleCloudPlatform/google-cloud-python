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
# Snippet for UpdateDataPolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-bigquery-datapolicies


# [START bigquerydatapolicy_v2_generated_DataPolicyService_UpdateDataPolicy_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import bigquery_datapolicies_v2


async def sample_update_data_policy():
    # Create a client
    client = bigquery_datapolicies_v2.DataPolicyServiceAsyncClient()

    # Initialize request argument(s)
    data_policy = bigquery_datapolicies_v2.DataPolicy()
    data_policy.data_masking_policy.predefined_expression = "RANDOM_HASH"
    data_policy.data_policy_type = "COLUMN_LEVEL_SECURITY_POLICY"

    request = bigquery_datapolicies_v2.UpdateDataPolicyRequest(
        data_policy=data_policy,
    )

    # Make the request
    response = await client.update_data_policy(request=request)

    # Handle the response
    print(response)


# [END bigquerydatapolicy_v2_generated_DataPolicyService_UpdateDataPolicy_async]
