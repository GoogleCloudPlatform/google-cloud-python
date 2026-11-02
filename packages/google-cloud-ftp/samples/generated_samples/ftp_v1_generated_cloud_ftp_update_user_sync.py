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
# Snippet for UpdateUser
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-ftp


# [START ftp_v1_generated_CloudFtp_UpdateUser_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import ftp_v1


def sample_update_user():
    # Create a client
    client = ftp_v1.CloudFtpClient()

    # Initialize request argument(s)
    user = ftp_v1.User()
    user.customer_service_account = "customer_service_account_value"
    user.user_credentials.credential_name = "credential_name_value"
    user.user_credentials.credential_type = "PUBLIC_KEY"
    user.storage_directory_mappings.bucket = "bucket_value"
    user.storage_directory_mappings.directory = "directory_value"
    user.storage_directory_mappings.permission = "READ_WRITE"

    request = ftp_v1.UpdateUserRequest(
        user=user,
    )

    # Make the request
    operation = client.update_user(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)


# [END ftp_v1_generated_CloudFtp_UpdateUser_sync]
