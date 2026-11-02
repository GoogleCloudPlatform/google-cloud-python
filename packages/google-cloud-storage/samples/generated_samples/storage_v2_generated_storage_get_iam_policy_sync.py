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
# Snippet for GetIamPolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-storage


# [START storage_v2_generated_Storage_GetIamPolicy_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

from google.cloud import _storage_v2


def sample_get_iam_policy():
    # Create a client
    client = _storage_v2.StorageClient()

    # Initialize request argument(s)
    request = iam_policy_pb2.GetIamPolicyRequest(
        resource="resource_value",
    )

    # Make the request
    response = client.get_iam_policy(request=request)

    # Handle the response
    print(response)


# [END storage_v2_generated_Storage_GetIamPolicy_sync]
