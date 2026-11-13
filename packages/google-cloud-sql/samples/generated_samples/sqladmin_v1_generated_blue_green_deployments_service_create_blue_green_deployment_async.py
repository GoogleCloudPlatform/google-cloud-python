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
# Snippet for CreateBlueGreenDeployment
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-sql


# [START sqladmin_v1_generated_BlueGreenDeploymentsService_CreateBlueGreenDeployment_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import sqladmin_v1


async def sample_create_blue_green_deployment():
    # Create a client
    client = sqladmin_v1.BlueGreenDeploymentsServiceAsyncClient()

    # Initialize request argument(s)
    blue_green_deployment = sqladmin_v1.BlueGreenDeployment()
    blue_green_deployment.source_instance = "source_instance_value"

    request = sqladmin_v1.CreateBlueGreenDeploymentRequest(
        parent="parent_value",
        blue_green_deployment_id="blue_green_deployment_id_value",
        blue_green_deployment=blue_green_deployment,
    )

    # Make the request
    response = await client.create_blue_green_deployment(request=request)

    # Handle the response
    print(response)


# [END sqladmin_v1_generated_BlueGreenDeploymentsService_CreateBlueGreenDeployment_async]
