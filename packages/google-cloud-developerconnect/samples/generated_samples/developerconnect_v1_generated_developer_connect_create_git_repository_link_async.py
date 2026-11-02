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
# Snippet for CreateGitRepositoryLink
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-developerconnect


# [START developerconnect_v1_generated_DeveloperConnect_CreateGitRepositoryLink_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import developerconnect_v1


async def sample_create_git_repository_link():
    # Create a client
    client = developerconnect_v1.DeveloperConnectAsyncClient()

    # Initialize request argument(s)
    git_repository_link = developerconnect_v1.GitRepositoryLink()
    git_repository_link.clone_uri = "clone_uri_value"

    request = developerconnect_v1.CreateGitRepositoryLinkRequest(
        parent="parent_value",
        git_repository_link=git_repository_link,
        git_repository_link_id="git_repository_link_id_value",
    )

    # Make the request
    operation = await client.create_git_repository_link(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END developerconnect_v1_generated_DeveloperConnect_CreateGitRepositoryLink_async]
