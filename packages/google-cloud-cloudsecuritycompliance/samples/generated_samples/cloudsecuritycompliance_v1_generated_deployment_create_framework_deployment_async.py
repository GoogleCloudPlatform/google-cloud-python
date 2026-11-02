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
# Snippet for CreateFrameworkDeployment
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-cloudsecuritycompliance


# [START cloudsecuritycompliance_v1_generated_Deployment_CreateFrameworkDeployment_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import cloudsecuritycompliance_v1


async def sample_create_framework_deployment():
    # Create a client
    client = cloudsecuritycompliance_v1.DeploymentAsyncClient()

    # Initialize request argument(s)
    framework_deployment = cloudsecuritycompliance_v1.FrameworkDeployment()
    framework_deployment.target_resource_config.existing_target_resource = (
        "existing_target_resource_value"
    )
    framework_deployment.framework.framework = "framework_value"
    framework_deployment.cloud_control_metadata.cloud_control_details.name = (
        "name_value"
    )
    framework_deployment.cloud_control_metadata.cloud_control_details.major_revision_id = 1811
    framework_deployment.cloud_control_metadata.enforcement_mode = "AUDIT"

    request = cloudsecuritycompliance_v1.CreateFrameworkDeploymentRequest(
        parent="parent_value",
        framework_deployment=framework_deployment,
    )

    # Make the request
    operation = await client.create_framework_deployment(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)


# [END cloudsecuritycompliance_v1_generated_Deployment_CreateFrameworkDeployment_async]
