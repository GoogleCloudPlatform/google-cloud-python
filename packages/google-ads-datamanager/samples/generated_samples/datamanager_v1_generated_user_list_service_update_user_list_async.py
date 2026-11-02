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
# Snippet for UpdateUserList
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-ads-datamanager


# [START datamanager_v1_generated_UserListService_UpdateUserList_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.ads import datamanager_v1


async def sample_update_user_list():
    # Create a client
    client = datamanager_v1.UserListServiceAsyncClient()

    # Initialize request argument(s)
    user_list = datamanager_v1.UserList()
    user_list.ingested_user_list_info.upload_key_types = ["PSEUDONYMOUS_ID"]

    request = datamanager_v1.UpdateUserListRequest(
        user_list=user_list,
    )

    # Make the request
    response = await client.update_user_list(request=request)

    # Handle the response
    print(response)


# [END datamanager_v1_generated_UserListService_UpdateUserList_async]
