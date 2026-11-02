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
# Snippet for CreateSingleTenantHsmInstanceProposal
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-kms


# [START cloudkms_v1_generated_HsmManagement_CreateSingleTenantHsmInstanceProposal_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import kms_v1


async def sample_create_single_tenant_hsm_instance_proposal():
    # Create a client
    client = kms_v1.HsmManagementAsyncClient()

    # Initialize request argument(s)
    single_tenant_hsm_instance_proposal = kms_v1.SingleTenantHsmInstanceProposal()
    single_tenant_hsm_instance_proposal.register_two_factor_auth_keys.required_approver_count = 2487
    single_tenant_hsm_instance_proposal.register_two_factor_auth_keys.two_factor_public_key_pems = [
        "two_factor_public_key_pems_value1",
        "two_factor_public_key_pems_value2",
    ]

    request = kms_v1.CreateSingleTenantHsmInstanceProposalRequest(
        parent="parent_value",
        single_tenant_hsm_instance_proposal=single_tenant_hsm_instance_proposal,
    )

    # Make the request
    operation = await client.create_single_tenant_hsm_instance_proposal(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END cloudkms_v1_generated_HsmManagement_CreateSingleTenantHsmInstanceProposal_async]
